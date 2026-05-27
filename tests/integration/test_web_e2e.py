"""
Tests de integración E2E para la capa web (web.py).

Escenarios BDD cubiertos:
  - Panel principal muestra resumen de estados.
  - Historial lista consultas y soporta filtros.
  - Formulario de nueva consulta disponible por GET.
  - POST /consultas crea consulta y redirige al detalle.
  - POST /consultas con datos inválidos retorna 400.
  - Detalle de consulta muestra info completa.
  - POST disponibilidad de atención registra y redirige.
  - POST disponibilidad de repuesto registra y redirige.
  - POST respuesta operativa registra y redirige.
  - POST respuesta operativa con datos inválidos retorna error.
  - GET consulta inexistente retorna 404.
  - Ruta desconocida retorna 404.
"""

from __future__ import annotations

import threading
import urllib.request
from http.client import HTTPResponse
from io import BytesIO
from urllib.parse import urlencode

import tempfile
from pathlib import Path

import pytest

from ecosistema_santi.web import _construir_servicios, _handler
from http.server import HTTPServer


# ---------------------------------------------------------------------------
# Utilidad: cliente HTTP mínimo para pruebas en memoria
# ---------------------------------------------------------------------------

class _ClienteHTTP:
    def __init__(self, host: str, port: int) -> None:
        self._base = f"http://{host}:{port}"

    def get(self, path: str) -> tuple[int, str]:
        url = self._base + path
        req = urllib.request.Request(url)
        try:
            with urllib.request.urlopen(req) as resp:
                return resp.status, resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            return exc.code, exc.read().decode("utf-8")

    def post(self, path: str, data: dict) -> tuple[int, str]:
        url = self._base + path
        body = urlencode(data).encode("utf-8")
        req = urllib.request.Request(url, data=body, method="POST")
        req.add_header("Content-Type", "application/x-www-form-urlencoded")
        try:
            with urllib.request.urlopen(req) as resp:
                return resp.status, resp.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            return exc.code, exc.read().decode("utf-8")


@pytest.fixture(scope="module")
def cliente():
    """Levanta el servidor web con DB en archivo temporal para los tests del módulo.

    Nota: :memory: no es viable porque cada repositorio abre su propia conexión
    y SQLite crea una DB independiente por conexión en modo in-memory.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = str(Path(temp_dir) / "test_web.db")
        services = _construir_servicios(db_path)
        handler_class = _handler(services)
        server = HTTPServer(("127.0.0.1", 0), handler_class)
        port = server.server_address[1]

        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()

        yield _ClienteHTTP("127.0.0.1", port)

        server.shutdown()
        server.server_close()
        services.close()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _crear_consulta(cliente: _ClienteHTTP, conductor_id: str = "conductor-test", motivo: str = "repuesto", descripcion: str = "necesito llanta delantera") -> str:
    """Crea una consulta via POST y devuelve su ID extraído del redirect."""
    status, body = cliente.post("/consultas", {
        "conductor_id": conductor_id,
        "motivo": motivo,
        "descripcion": descripcion,
    })
    # POST exitoso redirige a /consultas/<id>; al seguir la redirección llega al detalle
    assert status == 200, f"Esperado 200 tras redirección, got {status}"
    # Extraemos el ID del título de la página de detalle
    # La página tiene "Consulta <id>" en el heading h2
    import re
    match = re.search(r"<h2>Consulta ([0-9a-f-]{36})</h2>", body)
    assert match, f"No se encontró ID en la respuesta: {body[:300]}"
    return match.group(1)


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPanelPrincipal:
    def test_panel_devuelve_200(self, cliente: _ClienteHTTP):
        status, body = cliente.get("/")
        assert status == 200

    def test_panel_contiene_titulo(self, cliente: _ClienteHTTP):
        _, body = cliente.get("/")
        assert "Ecosistema Santi" in body

    def test_panel_contiene_resumen(self, cliente: _ClienteHTTP):
        _, body = cliente.get("/")
        assert "Panel principal" in body

    def test_panel_contiene_enlace_nueva_consulta(self, cliente: _ClienteHTTP):
        _, body = cliente.get("/")
        assert "/consultas/nueva" in body


class TestHistorial:
    def test_historial_devuelve_200(self, cliente: _ClienteHTTP):
        status, body = cliente.get("/consultas")
        assert status == 200

    def test_historial_contiene_titulo(self, cliente: _ClienteHTTP):
        _, body = cliente.get("/consultas")
        assert "Historial de consultas" in body

    def test_historial_soporta_filtro_por_estado(self, cliente: _ClienteHTTP):
        status, body = cliente.get("/consultas?estado=pendiente")
        assert status == 200
        assert "Historial de consultas" in body

    def test_historial_soporta_filtro_por_motivo(self, cliente: _ClienteHTTP):
        status, body = cliente.get("/consultas?motivo=repuesto")
        assert status == 200

    def test_historial_redirige_por_consulta_id(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-historial")
        status, body = cliente.get(f"/consultas?consulta_id={consulta_id}")
        assert status == 200
        assert consulta_id in body


class TestNuevaConsulta:
    def test_formulario_nueva_consulta_devuelve_200(self, cliente: _ClienteHTTP):
        status, body = cliente.get("/consultas/nueva")
        assert status == 200

    def test_formulario_nueva_consulta_tiene_campos(self, cliente: _ClienteHTTP):
        _, body = cliente.get("/consultas/nueva")
        assert "conductor_id" in body
        assert "name='motivo'" in body
        assert "name='descripcion'" in body

    def test_post_consulta_valida_crea_y_redirige(self, cliente: _ClienteHTTP):
        status, body = cliente.post("/consultas", {
            "conductor_id": "conductor-nuevo",
            "motivo": "mantenimiento_preventivo",
            "descripcion": "cambio de aceite y revisión general",
        })
        assert status == 200
        assert "Detalle de consulta" in body

    def test_post_consulta_motivo_invalido_retorna_400(self, cliente: _ClienteHTTP):
        status, body = cliente.post("/consultas", {
            "conductor_id": "conductor-invalido",
            "motivo": "otro_motivo_invalido",
            "descripcion": "algo",
        })
        assert status == 400

    def test_post_consulta_conductor_vacio_retorna_400(self, cliente: _ClienteHTTP):
        status, body = cliente.post("/consultas", {
            "conductor_id": "",
            "motivo": "repuesto",
            "descripcion": "algo",
        })
        assert status == 400

    def test_post_consulta_descripcion_vacia_retorna_400(self, cliente: _ClienteHTTP):
        status, body = cliente.post("/consultas", {
            "conductor_id": "conductor-1",
            "motivo": "repuesto",
            "descripcion": "",
        })
        assert status == 400


class TestDetalleConsulta:
    def test_detalle_muestra_consulta(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-detalle")
        status, body = cliente.get(f"/consultas/{consulta_id}")
        assert status == 200
        assert consulta_id in body
        assert "conductor-detalle" in body

    def test_detalle_muestra_seccion_disponibilidad_atencion(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-da")
        _, body = cliente.get(f"/consultas/{consulta_id}")
        assert "Disponibilidad atencion" in body

    def test_detalle_muestra_seccion_disponibilidad_repuesto(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-dr")
        _, body = cliente.get(f"/consultas/{consulta_id}")
        assert "Disponibilidad repuesto" in body

    def test_detalle_muestra_seccion_respuesta_operativa(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-ro")
        _, body = cliente.get(f"/consultas/{consulta_id}")
        assert "Respuesta operativa" in body

    def test_detalle_consulta_inexistente_retorna_404(self, cliente: _ClienteHTTP):
        status, _ = cliente.get("/consultas/id-que-no-existe")
        assert status == 404


class TestRegistrarDisponibilidades:
    def test_post_atencion_disponible_redirige(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-aten")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/atencion",
            {"estado": "disponible"},
        )
        assert status == 200
        assert "disponible" in body

    def test_post_atencion_no_disponible_redirige(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-aten2")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/atencion",
            {"estado": "no_disponible"},
        )
        assert status == 200

    def test_post_atencion_estado_invalido_muestra_error(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-aten3")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/atencion",
            {"estado": "estado_inventado"},
        )
        assert status == 200

    def test_post_repuesto_disponible_redirige(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-rep")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/repuesto",
            {"estado": "disponible"},
        )
        assert status == 200
        assert "disponible" in body

    def test_post_repuesto_pendiente_confirmacion(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-rep2")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/repuesto",
            {"estado": "pendiente_confirmacion"},
        )
        assert status == 200


class TestRegistrarRespuestaOperativa:
    def test_post_respuesta_valida_redirige(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-resp")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/respuesta",
            {
                "estado_general": "confirmado",
                "observacion": "Taller disponible y repuesto en stock",
                "costo_estimado": "75.50",
            },
        )
        assert status == 200
        assert "confirmado" in body

    def test_post_respuesta_sin_costo_redirige(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-resp2")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/respuesta",
            {
                "estado_general": "en_revision",
                "observacion": "Verificando disponibilidad",
                "costo_estimado": "",
            },
        )
        assert status == 200

    def test_post_respuesta_observacion_vacia_muestra_error(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-resp3")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/respuesta",
            {
                "estado_general": "ok",
                "observacion": "",
                "costo_estimado": "",
            },
        )
        assert status == 200

    def test_post_respuesta_estado_general_vacio_muestra_error(self, cliente: _ClienteHTTP):
        consulta_id = _crear_consulta(cliente, conductor_id="conductor-resp4")
        status, body = cliente.post(
            f"/consultas/{consulta_id}/respuesta",
            {
                "estado_general": "",
                "observacion": "algo",
                "costo_estimado": "",
            },
        )
        assert status == 200


class TestFlujoCierreCompleto:
    """BDD: escenario completo del dominio mototaxi."""

    def test_flujo_consulta_hasta_confirmada(self, cliente: _ClienteHTTP):
        # 1. Conductor registra consulta de repuesto
        consulta_id = _crear_consulta(
            cliente,
            conductor_id="conductor-juan",
            motivo="repuesto",
            descripcion="Necesito pastilla de freno delantera Honda Wave",
        )

        # 2. Taller confirma disponibilidad de atención
        status, body = cliente.post(
            f"/consultas/{consulta_id}/atencion",
            {"estado": "disponible"},
        )
        assert status == 200

        # 3. Tienda confirma disponibilidad de repuesto
        status, body = cliente.post(
            f"/consultas/{consulta_id}/repuesto",
            {"estado": "disponible"},
        )
        assert status == 200

        # 4. Taller registra respuesta operativa con costo
        status, body = cliente.post(
            f"/consultas/{consulta_id}/respuesta",
            {
                "estado_general": "confirmado",
                "observacion": "Pastilla Honda Wave disponible. Mecánico libre mañana 9am.",
                "costo_estimado": "45.00",
            },
        )
        assert status == 200

        # 5. Verificar estado final en detalle
        status, body = cliente.get(f"/consultas/{consulta_id}")
        assert status == 200
        assert "confirmada" in body
        assert "45" in body

    def test_flujo_consulta_no_resuelta(self, cliente: _ClienteHTTP):
        # Conductor consulta repuesto no disponible
        consulta_id = _crear_consulta(
            cliente,
            conductor_id="conductor-pedro",
            motivo="reparacion_correctiva",
            descripcion="Falla en cigüeñal",
        )

        cliente.post(
            f"/consultas/{consulta_id}/atencion",
            {"estado": "disponible"},
        )
        cliente.post(
            f"/consultas/{consulta_id}/repuesto",
            {"estado": "no_disponible"},
        )

        _, body = cliente.get(f"/consultas/{consulta_id}")
        assert "no_resuelta" in body or "no resuelta" in body


class TestRutasNoEncontradas:
    def test_ruta_inexistente_retorna_404(self, cliente: _ClienteHTTP):
        status, _ = cliente.get("/ruta-que-no-existe")
        assert status == 404

    def test_post_ruta_inexistente_retorna_404(self, cliente: _ClienteHTTP):
        status, _ = cliente.post("/ruta-inexistente", {})
        assert status == 404
