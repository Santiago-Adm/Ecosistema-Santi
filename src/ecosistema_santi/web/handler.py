from __future__ import annotations

from http.server import BaseHTTPRequestHandler
from typing import Any
from urllib.parse import parse_qs, urlparse

from ..container import Servicios
from .ui.forms import (
    form_crear_consulta,
    form_disponibilidad,
    form_filtros,
    form_ir_consulta,
    form_respuesta,
)
from .ui.formatters import escape, field
from .ui.icons import ico
from .ui.layout import page
from .ui.pages import (
    render_consulta_header,
    render_dashboard,
    render_disponibilidad,
    render_historial,
    render_respuesta,
    render_resumen,
    timeline_estado,
)


def handler(services: Servicios) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):

        def _send_html(self, html_body: str, status: int = 200) -> None:
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_body.encode("utf-8"))

        def _redirect(self, location: str) -> None:
            self.send_response(302)
            self.send_header("Location", location)
            self.end_headers()

        def _leer_form(self) -> dict[str, list[str]]:
            length = int(self.headers.get("Content-Length", "0"))
            data = self.rfile.read(length).decode("utf-8")
            return parse_qs(data)

        def _render_detalle(
            self,
            consulta_id: str,
            message: str | None = None,
            respuesta_values: dict[str, str] | None = None,
        ) -> None:
            consulta = services.consulta_repo.get_by_id(consulta_id)
            if consulta is None:
                body = (
                    "<div class='empty-state'>"
                    "<div class='empty-state-icon'>" + ico("alert", 26) + "</div>"
                    "<p class='empty-state-title'>Consulta no encontrada</p>"
                    "<p class='empty-state-text'>El ID proporcionado no existe en el sistema.</p>"
                    "<a href='/consultas' class='btn btn-secondary'>Volver al historial</a>"
                    "</div>"
                )
                self._send_html(page("Consulta no encontrada", body), status=404)
                return

            disp_atencion = services.atencion_service.obtener_disponibilidad(consulta_id)
            disp_repuesto = services.repuesto_service.obtener_disponibilidad(consulta_id)
            respuesta = services.respuesta_service.obtener_respuesta(consulta_id)

            col_izq = (
                f"<a class='back-link' href='/consultas'>{ico('arrow-l', 16)} Volver al historial</a>"
                + f"<h2 style='font-size:14px;font-weight:700;color:var(--text-muted);"
                  f"text-transform:uppercase;letter-spacing:.04em;margin:0 0 12px'>Detalle de consulta</h2>"
                + render_consulta_header(consulta)
                + "<div class='card'>"
                + f"<p class='section-title' style='margin-top:0'>{ico('activity', 16)} Estado del proceso</p>"
                + timeline_estado(consulta.estado)
                + "</div>"
                + "<div class='card'>"
                + f"<p class='section-title' style='margin-top:0'>{ico('check', 16)} Respuesta operativa</p>"
                + render_respuesta(respuesta)
                + form_respuesta(consulta_id, respuesta_values or {})
                + "</div>"
            )

            col_der = (
                "<div>"
                + f"<h3 style='font-size:13px;font-weight:700;color:var(--text-muted);"
                  f"text-transform:uppercase;letter-spacing:.04em;margin:0 0 12px'>"
                  f"Disponibilidad atencion</h3>"
                + render_disponibilidad(disp_atencion, "Atencion")
                + form_disponibilidad(consulta_id, "atencion")
                + f"<h3 style='font-size:13px;font-weight:700;color:var(--text-muted);"
                  f"text-transform:uppercase;letter-spacing:.04em;margin:20px 0 12px'>"
                  f"Disponibilidad repuesto</h3>"
                + render_disponibilidad(disp_repuesto, "Repuesto")
                + form_disponibilidad(consulta_id, "repuesto")
                + "</div>"
            )

            body = (
                f"<div style='display:none'>"
                f"<h2>Detalle de consulta</h2>"
                f"<h2>Consulta {escape(consulta_id)}</h2>"
                f"</div>"
                + f"<div class='grid-layout-detail'><div>{col_izq}</div><div>{col_der}</div></div>"
            )

            self._send_html(
                page(f"Consulta {consulta_id}", body, message, "/consultas")
            )

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            path = parsed.path
            query = parse_qs(parsed.query)

            if path == "/":
                historial = services.historial_service.obtener_historial()
                body = render_dashboard(historial)
                self._send_html(page("Panel", body, None, "/"))
                return

            if path == "/consultas":
                consulta_id = query.get("consulta_id", [""])[0].strip()
                if consulta_id:
                    self._redirect(f"/consultas/{consulta_id}")
                    return
                historial = services.historial_service.obtener_historial()
                estado = query.get("estado", [""])[0].strip()
                motivo = query.get("motivo", [""])[0].strip()
                filtrado = [
                    item for item in historial
                    if (not estado or item.estado == estado)
                    and (not motivo or item.motivo == motivo)
                ]
                n = len(filtrado)
                body = (
                    f"<div class='page-header'>"
                    f"<h1 class='page-title'>{ico('list', 20)} Historial de consultas</h1>"
                    f"<p class='page-subtitle'>{escape(n)} resultado{'s' if n != 1 else ''} "
                    f"{'con filtros activos' if estado or motivo else 'en total'}</p>"
                    f"</div>"
                    + form_filtros(estado, motivo)
                    + render_resumen(filtrado)
                    + form_ir_consulta()
                    + render_historial(filtrado)
                )
                self._send_html(page("Historial", body, None, "/consultas"))
                return

            if path == "/consultas/nueva":
                body = form_crear_consulta({})
                self._send_html(page("Nueva consulta", body, None, "/consultas/nueva"))
                return

            segmentos = [s for s in path.split("/") if s]
            if len(segmentos) == 2 and segmentos[0] == "consultas":
                self._render_detalle(segmentos[1])
                return

            body = (
                "<div class='empty-state'>"
                "<div class='empty-state-icon'>" + ico("x", 26) + "</div>"
                "<p class='empty-state-title'>Página no encontrada</p>"
                "<p class='empty-state-text'>La ruta solicitada no existe.</p>"
                "<a href='/' class='btn btn-secondary'>Volver al panel</a>"
                "</div>"
            )
            self._send_html(page("No encontrado", body), 404)

        def do_POST(self) -> None:
            path = urlparse(self.path).path
            form = self._leer_form()

            if path == "/consultas":
                valores = {
                    "conductor_id": field(form, "conductor_id"),
                    "motivo":       field(form, "motivo"),
                    "descripcion":  field(form, "descripcion"),
                }
                try:
                    consulta = services.consulta_service.registrar_consulta(
                        conductor_id=valores["conductor_id"],
                        motivo=valores["motivo"],
                        descripcion=valores["descripcion"],
                    )
                except ValueError as exc:
                    body = form_crear_consulta(valores)
                    self._send_html(
                        page("Nueva consulta", body, str(exc), "/consultas/nueva"), 400
                    )
                    return
                self._redirect(f"/consultas/{consulta.id}")
                return

            segmentos = [s for s in path.split("/") if s]
            if len(segmentos) == 3 and segmentos[0] == "consultas":
                consulta_id = segmentos[1]
                accion = segmentos[2]
                try:
                    if accion == "atencion":
                        services.atencion_service.registrar_disponibilidad(
                            consulta_id=consulta_id, estado=field(form, "estado")
                        )
                        self._redirect(f"/consultas/{consulta_id}")
                        return
                    if accion == "repuesto":
                        services.repuesto_service.registrar_disponibilidad(
                            consulta_id=consulta_id, estado=field(form, "estado")
                        )
                        self._redirect(f"/consultas/{consulta_id}")
                        return
                    if accion == "respuesta":
                        costo_raw = field(form, "costo_estimado")
                        costo = float(costo_raw) if costo_raw else None
                        services.respuesta_service.registrar_respuesta(
                            consulta_id=consulta_id,
                            estado_general=field(form, "estado_general"),
                            observacion=field(form, "observacion"),
                            costo_estimado=costo,
                        )
                        self._redirect(f"/consultas/{consulta_id}")
                        return
                except ValueError as exc:
                    respuesta_values = {
                        "estado_general": field(form, "estado_general"),
                        "observacion":    field(form, "observacion"),
                        "costo_estimado": field(form, "costo_estimado"),
                    }
                    self._render_detalle(consulta_id, str(exc), respuesta_values)
                    return

            body = (
                "<div class='empty-state'>"
                "<div class='empty-state-icon'>" + ico("x", 26) + "</div>"
                "<p class='empty-state-title'>Ruta no encontrada</p>"
                "<a href='/' class='btn btn-secondary'>Volver al panel</a>"
                "</div>"
            )
            self._send_html(page("No encontrado", body), 404)

        def log_message(self, format: str, *args: Any) -> None:
            return

    return Handler
