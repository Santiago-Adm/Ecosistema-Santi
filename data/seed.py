"""
Script de seed reproducible — Ecosistema Santi
Niveles:
  base   — 5 escenarios (1 por estado)
  demo   — 25 escenarios (distribución realista para dashboards)
  volumen — 55 escenarios (carga visual completa)

Uso:
  python data/seed.py --reset                  # demo (por defecto)
  python data/seed.py --reset --nivel base
  python data/seed.py --reset --nivel volumen
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from ecosistema_santi.persistence.sqlite import create_connection, ensure_schema


# ── Helpers ──────────────────────────────────────────────────────────────────

def _ts(offset_horas: float = 0) -> str:
    return (datetime.now(timezone.utc) - timedelta(hours=offset_horas)).isoformat()


def _ins_consulta(conn, id_: str, conductor: str, motivo: str, desc: str, estado: str, offset_h: float) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO consultas (id, conductor_id, motivo, descripcion, estado, creada_en) VALUES (?,?,?,?,?,?)",
        (id_, conductor, motivo, desc, estado, _ts(offset_h)),
    )


def _ins_atencion(conn, id_: str, estado: str, offset_h: float = 0) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO disponibilidad_atencion (consulta_id, estado, actualizado_en) VALUES (?,?,?)",
        (id_, estado, _ts(offset_h)),
    )


def _ins_repuesto(conn, id_: str, estado: str, offset_h: float = 0) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO disponibilidad_repuesto (consulta_id, estado, actualizado_en) VALUES (?,?,?)",
        (id_, estado, _ts(offset_h)),
    )


def _ins_respuesta(conn, id_: str, eg: str, obs: str, costo: float | None, offset_h: float = 0) -> None:
    conn.execute(
        "INSERT OR REPLACE INTO respuestas_operativas (consulta_id, estado_general, observacion, costo_estimado, actualizado_en) VALUES (?,?,?,?,?)",
        (id_, eg, obs, costo, _ts(offset_h)),
    )


def _reset(conn) -> None:
    conn.executescript("""
        DELETE FROM respuestas_operativas;
        DELETE FROM disponibilidad_repuesto;
        DELETE FROM disponibilidad_atencion;
        DELETE FROM consultas;
    """)


# ── Nivel BASE (5 escenarios canónicos) ──────────────────────────────────────

def _seed_base(conn) -> list[dict]:
    escenarios = [
        ("seed-b01-pendiente",          "conductor-juan-001",    "reparacion_correctiva",    "pendiente",
         "El freno delantero no agarra bien, hace ruido al frenar fuerte",
         2, None, None, None),
        ("seed-b02-en-revision",        "conductor-pedro-002",   "repuesto",                 "en_revision",
         "Necesito la banda de freno trasera Bajaj RE, no sé el modelo exacto",
         5, None, None, ("en_proceso", "Verificando stock de banda Bajaj RE. Respuesta en 30 min.", None)),
        ("seed-b03-confirmada-parcial", "conductor-carlos-003",  "mantenimiento_preventivo", "confirmada_parcial",
         "Mantenimiento mensual completo: aceite, filtro, cadena y revisión general",
         24, "disponible", "pendiente_confirmacion",
         ("parcialmente_confirmado", "Mecánico disponible desde las 9am. Filtro pendiente con proveedor.", 85.0)),
        ("seed-b04-confirmada",         "conductor-luis-004",    "repuesto",                 "confirmada",
         "Pastilla de freno delantera desgastada, modelo Honda Wave S",
         48, "disponible", "disponible",
         ("confirmado", "Pastilla Honda Wave en stock. Mecánico disponible mañana 9am.", 45.0)),
        ("seed-b05-no-resuelta",        "conductor-miguel-005",  "reparacion_correctiva",    "no_resuelta",
         "Motor hace ruido extraño al acelerar, posible falla en cigüeñal",
         72, "disponible", "no_disponible",
         ("no_disponible", "Repuesto cigüeñal no disponible localmente. Pedido 3-5 días.", 320.0)),
    ]
    _insertar_lista(conn, escenarios)
    return [{"id": e[0], "estado": e[3], "conductor_id": e[1]} for e in escenarios]


# ── Nivel DEMO (25 escenarios) ────────────────────────────────────────────────

def _seed_demo(conn) -> list[dict]:
    # (id, conductor, motivo, estado, descripcion, offset_h, atencion, repuesto, respuesta)
    # atencion/repuesto: estado string | None
    # respuesta: (estado_general, observacion, costo) | None
    escenarios = [
        # ── Pendientes (6) ──────────────────────────────────────────────────
        ("seed-d01", "conductor-juan-mototaxi",   "reparacion_correctiva",    "pendiente",
         "Freno delantero no agarra, ruido al frenar fuerte", 0.5, None, None, None),
        ("seed-d02", "conductor-ana-rivera",       "mantenimiento_preventivo", "pendiente",
         "Mantenimiento 3000km: aceite, filtro, revisión cadena y frenos", 1, None, None, None),
        ("seed-d03", "conductor-sofia-mendez",     "reparacion_correctiva",    "pendiente",
         "Ruido en suspensión trasera al pasar por baches", 2, None, None, None),
        ("seed-d04", "conductor-jose-huanca",      "repuesto",                 "pendiente",
         "Pastilla de freno trasera desgastada, moto Honda Wave 110", 3, None, None, None),
        ("seed-d05", "conductor-maria-quispe",     "mantenimiento_preventivo", "pendiente",
         "Cambio de cadena y piñones, kilometraje muy alto", 4, None, None, None),
        ("seed-d06", "conductor-ricardo-flores",   "reparacion_correctiva",    "pendiente",
         "Carburador falla al arrancar en frío, moto tarda en cebar", 5, None, None, None),
        # ── En revisión (4) ─────────────────────────────────────────────────
        ("seed-d07", "conductor-pedro-lima",       "repuesto",                 "en_revision",
         "Banda de freno trasera Bajaj RE, necesito urgente", 6, None, None,
         ("en_proceso", "Verificando stock en almacén. Confirmo disponibilidad en 1h.", None)),
        ("seed-d08", "conductor-roberto-torres",   "reparacion_correctiva",    "en_revision",
         "Embrague patina al subir pendientes, revisar disco y platillos", 8, None, None,
         ("en_revision", "Taller recibió. Diagnóstico inicial: desgaste disco embrague.", None)),
        ("seed-d09", "conductor-luis-veloz",       "mantenimiento_preventivo", "en_revision",
         "Filtro de aire completamente tapado, necesita reemplazo urgente", 10, None, None,
         ("consultando", "Revisando precio de filtro original vs genérico.", None)),
        ("seed-d10", "conductor-hector-mamani",    "reparacion_correctiva",    "en_revision",
         "Tensado de cadena y revisión de piñón de ataque", 12, None, None,
         ("en_proceso", "Mecánico revisó. Cadena con desgaste avanzado, recomienda cambio.", 55.0)),
        # ── Confirmada parcial (3) ───────────────────────────────────────────
        ("seed-d11", "conductor-carlos-express",   "mantenimiento_preventivo", "confirmada_parcial",
         "Servicio completo 5000km: aceite, bujía, filtros, frenos", 18, "disponible", "pendiente_confirmacion",
         ("parcialmente_confirmado", "Mecánico libre mañana 8am. Filtro de aceite pendiente confirmar.", 120.0)),
        ("seed-d12", "conductor-miguel-san-juan",  "reparacion_correctiva",    "confirmada_parcial",
         "Bujía y carburador sucios, moto pierde potencia al acelerar", 20, "disponible", "pendiente_confirmacion",
         ("en_proceso", "Mecánico puede atender. Carburador requiere kit de reparación.", 80.0)),
        ("seed-d13", "conductor-ana-rivera",       "repuesto",                 "confirmada_parcial",
         "Llanta delantera con corte, necesita reemplazo inmediato", 22, "pendiente_confirmacion", "disponible",
         ("parcial", "Llanta disponible en tienda. Confirmando mecánico de montaje.", 95.0)),
        # ── Confirmadas (7) ──────────────────────────────────────────────────
        ("seed-d14", "conductor-luis-veloz",       "repuesto",                 "confirmada",
         "Pastilla de freno delantera Honda Wave S desgastada al 10%", 30, "disponible", "disponible",
         ("confirmado", "Pastilla Honda Wave disponible. Mecánico libre 2pm. Puede acudir.", 45.0)),
        ("seed-d15", "conductor-sofia-mendez",     "mantenimiento_preventivo", "confirmada",
         "Cambio de aceite y filtro, revisión frenos y cadena", 36, "disponible", "disponible",
         ("confirmado", "Todo listo. Mecánico y materiales disponibles desde las 9am.", 75.0)),
        ("seed-d16", "conductor-carlos-express",   "reparacion_correctiva",    "confirmada",
         "Freno trasero rígido, no entra bien al pisar el pedal", 40, "disponible", "disponible",
         ("confirmado", "Cable de freno trasero disponible. Atención en 45 min.", 35.0)),
        ("seed-d17", "conductor-roberto-torres",   "repuesto",                 "confirmada",
         "Llanta trasera desgastada, necesita renovar antes de viaje largo", 48, "disponible", "disponible",
         ("confirmado", "Llanta 3.00-17 disponible. Mecánico confirma montaje hoy 4pm.", 110.0)),
        ("seed-d18", "conductor-hector-mamani",    "mantenimiento_preventivo", "confirmada",
         "Mantenimiento 5000km completo, primera vez en este taller", 52, "disponible", "disponible",
         ("confirmado", "Servicio completo disponible. Precio incluye mano de obra.", 145.0)),
        ("seed-d19", "conductor-jose-huanca",      "reparacion_correctiva",    "confirmada",
         "Luz trasera quemada, no enciende al frenar", 60, "disponible", "disponible",
         ("confirmado", "Foco disponible en tienda. Se instala en el momento.", 18.0)),
        ("seed-d20", "conductor-maria-quispe",     "repuesto",                 "confirmada",
         "Cadena de transmisión estirada, necesita ajuste o cambio", 72, "disponible", "disponible",
         ("confirmado", "Cadena de reemplazo disponible. Mecánico atiende mañana 8am.", 65.0)),
        # ── No resueltas (5) ─────────────────────────────────────────────────
        ("seed-d21", "conductor-miguel-san-juan",  "reparacion_correctiva",    "no_resuelta",
         "Motor hace ruido al acelerar, posible falla en cigüeñal o biela", 80, "disponible", "no_disponible",
         ("no_disponible", "Cigüeñal no disponible localmente. Pedido de Lima tarda 5-7 días.", 450.0)),
        ("seed-d22", "conductor-pedro-lima",       "repuesto",                 "no_resuelta",
         "Disco de freno delantero rayado, vibra al frenar a alta velocidad", 90, "no_disponible", "no_disponible",
         ("no_disponible", "Disco y pastilla no disponibles en stock local.", 180.0)),
        ("seed-d23", "conductor-jose-huanca",      "reparacion_correctiva",    "no_resuelta",
         "Amortiguador trasero completamente vencido, bota aceite", 96, "disponible", "no_disponible",
         ("no_disponible", "Amortiguador para Bajaj RE200 no hay stock. Llega en 10 días.", 220.0)),
        ("seed-d24", "conductor-ricardo-flores",   "reparacion_correctiva",    "no_resuelta",
         "Culata con fisura, pierde agua y aceite al mismo tiempo", 110, "no_disponible", "no_disponible",
         ("critico", "Reparación mayor. Requiere taller especializado, no hay en la ciudad.", 850.0)),
        ("seed-d25", "conductor-hector-mamani",    "reparacion_correctiva",    "no_resuelta",
         "Caja de velocidades traba en 3ra marcha, no entra ni sale", 120, "disponible", "no_disponible",
         ("no_disponible", "Caja de velocidades: requiere rebobinado. Solo taller Lima.", 620.0)),
    ]
    _insertar_lista(conn, escenarios)
    return [{"id": e[0], "estado": e[3], "conductor_id": e[1]} for e in escenarios]


# ── Nivel VOLUMEN (55 escenarios) ─────────────────────────────────────────────

def _seed_volumen(conn) -> list[dict]:
    conductores = [
        "conductor-juan-mototaxi",   "conductor-ana-rivera",     "conductor-sofia-mendez",
        "conductor-jose-huanca",     "conductor-maria-quispe",   "conductor-pedro-lima",
        "conductor-roberto-torres",  "conductor-luis-veloz",     "conductor-carlos-express",
        "conductor-miguel-san-juan", "conductor-hector-mamani",  "conductor-ricardo-flores",
        "conductor-teresa-condori",  "conductor-pablo-apaza",    "conductor-rosa-ccahuaya",
    ]
    motivos = ["reparacion_correctiva", "repuesto", "mantenimiento_preventivo"]
    descripciones = {
        "reparacion_correctiva": [
            "Freno delantero no responde correctamente al frenar",
            "Embrague patina al subir pendientes pronunciadas",
            "Motor vibra excesivamente a más de 40km/h",
            "Ruido metálico en caja de cambios al cambiar de marcha",
            "Aceite quemado, consumo anormal de lubricante",
            "Suspensión delantera rígida, golpea en baches",
        ],
        "repuesto": [
            "Pastilla de freno desgastada, necesita reemplazo urgente",
            "Banda de freno trasera sin material de fricción",
            "Llanta con corte lateral, no aguanta presión",
            "Cadena de transmisión estirada, necesita cambio",
            "Filtro de aire saturado, no entra suficiente mezcla",
            "Bujía gastada, falla encendido en frío",
        ],
        "mantenimiento_preventivo": [
            "Mantenimiento 3000km: aceite, filtro y revisión general",
            "Mantenimiento 5000km: servicio completo programado",
            "Cambio de aceite y revisión de frenos y luces",
            "Revisión general previa a temporada alta de viajes",
            "Mantenimiento semestral, incluye ajuste de válvulas",
            "Servicio periódico: bujía, filtros y cadena",
        ],
    }

    # Estado distribution: 12P + 8ER + 6CP + 18C + 11NR = 55
    plan = (
        [(c, "pendiente") for c in conductores[:12]]
        + [(c, "en_revision") for c in conductores[3:11]]
        + [(c, "confirmada_parcial") for c in conductores[:6]]
        + [(c, "confirmada") for c in conductores * 2][:18]
        + [(c, "no_resuelta") for c in conductores[4:15]]
    )[:55]

    import hashlib

    def _desc(conductor: str, motivo: str, idx: int) -> str:
        return descripciones[motivo][idx % len(descripciones[motivo])]

    escenarios = []
    for i, (conductor, estado) in enumerate(plan):
        motivo = motivos[i % 3]
        h = hashlib.md5(f"vol-{i}-{conductor}".encode()).hexdigest()[:8]
        id_ = f"seed-v{i+1:02d}-{h}"
        desc = _desc(conductor, motivo, i)
        offset_h = (i + 1) * 3.7

        if estado == "pendiente":
            aten, rep, resp = None, None, None
        elif estado == "en_revision":
            aten, rep = None, None
            resp = ("en_proceso", "Taller recibió solicitud. Verificando disponibilidad.", None)
        elif estado == "confirmada_parcial":
            aten, rep = "disponible", "pendiente_confirmacion"
            resp = ("parcial", "Atención confirmada. Repuesto pendiente de verificación.", 60.0)
        elif estado == "confirmada":
            aten, rep = "disponible", "disponible"
            costo = round(30 + (i % 8) * 20.0, 2)
            resp = ("confirmado", f"Todo disponible. Puede acudir con confianza. Atención en {20 + i%40} min.", costo)
        else:  # no_resuelta
            aten, rep = "disponible", "no_disponible"
            resp = ("no_disponible", "Repuesto no disponible localmente. Consultar en 3-5 días.", None)

        escenarios.append((id_, conductor, motivo, estado, desc, offset_h, aten, rep, resp))

    _insertar_lista(conn, escenarios)
    return [{"id": e[0], "estado": e[3], "conductor_id": e[1]} for e in escenarios]


# ── Inserción genérica ────────────────────────────────────────────────────────

def _insertar_lista(conn, escenarios: list) -> None:
    for row in escenarios:
        id_, conductor, motivo, estado, desc, offset_h, aten, rep, resp = row
        _ins_consulta(conn, id_, conductor, motivo, desc, estado, offset_h)
        if aten:
            _ins_atencion(conn, id_, aten, offset_h * 0.5)
        if rep:
            _ins_repuesto(conn, id_, rep, offset_h * 0.5)
        if resp:
            eg, obs, costo = resp
            _ins_respuesta(conn, id_, eg, obs, costo, offset_h * 0.3)


# ── Entrypoint ────────────────────────────────────────────────────────────────

_NIVELES = {
    "base":    _seed_base,
    "demo":    _seed_demo,
    "volumen": _seed_volumen,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Poblar base de datos con datos semilla")
    parser.add_argument("--db", default=str(Path("data") / "consultas.db"))
    parser.add_argument("--reset", action="store_true", help="Borrar datos existentes antes de insertar")
    parser.add_argument("--nivel", choices=list(_NIVELES), default="demo",
                        help="Nivel de seed: base (5), demo (25), volumen (55). Por defecto: demo")
    args = parser.parse_args(argv)

    db_path = args.db
    if db_path != ":memory:":
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    conn = create_connection(db_path)
    ensure_schema(conn)

    if args.reset:
        _reset(conn)

    fn = _NIVELES[args.nivel]
    resultados = fn(conn)
    conn.commit()
    conn.close()

    conteo = {}
    for r in resultados:
        conteo[r["estado"]] = conteo.get(r["estado"], 0) + 1

    print(f"Seed '{args.nivel}' completado: {len(resultados)} escenarios en {db_path}")
    for estado, n in sorted(conteo.items()):
        print(f"  {estado:25s} {n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
