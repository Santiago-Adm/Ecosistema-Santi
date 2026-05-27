from __future__ import annotations

from ...domain.historial import ConsultaResumen
from .formatters import escape, format_fecha, motivo_label, motivo_icono
from .icons import ico


def badge(estado: str, tipo: str) -> str:
    if tipo == "consulta":
        mapping = {
            "pendiente":          "badge badge-info",
            "en_revision":        "badge badge-warn",
            "confirmada_parcial": "badge badge-warn",
            "confirmada":         "badge badge-ok",
            "no_resuelta":        "badge badge-bad",
        }
    else:
        mapping = {
            "disponible":             "badge badge-ok",
            "no_disponible":          "badge badge-bad",
            "pendiente_confirmacion": "badge badge-warn",
        }
    cls = mapping.get(estado, "badge badge-gray")
    etiqueta = estado.replace("_", " ")
    return f"<span class='{cls}'>{escape(etiqueta)}</span>"


def kpi_card(label: str, value: int, sub: str, color: str, icon: str) -> str:
    return (
        f"<div class='kpi-card'>"
        f"<div class='kpi-icon {color}'>{ico(icon, 22)}</div>"
        f"<div class='kpi-body'>"
        f"<p class='kpi-label'>{escape(label)}</p>"
        f"<p class='kpi-value'>{escape(value)}</p>"
        f"<p class='kpi-sub'>{escape(sub)}</p>"
        f"</div></div>"
    )


def barra_estados(historial: list[ConsultaResumen]) -> str:
    estados_cfg = [
        ("pendiente",          "var(--info)",    "Pendiente"),
        ("en_revision",        "var(--warning)", "En revisión"),
        ("confirmada_parcial", "var(--warning)", "Conf. parcial"),
        ("confirmada",         "var(--success)", "Confirmada"),
        ("no_resuelta",        "var(--danger)",  "No resuelta"),
    ]
    conteo: dict[str, int] = {e: 0 for e, _, _ in estados_cfg}
    for item in historial:
        if item.estado in conteo:
            conteo[item.estado] += 1
    total = len(historial) or 1

    filas = []
    for key, color, label in estados_cfg:
        pct = int(conteo[key] / total * 100)
        filas.append(
            f"<div class='bar-row'>"
            f"<span class='bar-label'>{escape(label)}</span>"
            f"<div class='bar-track'>"
            f"<div class='bar-fill' style='width:{pct}%;background:{color}'></div>"
            f"</div>"
            f"<span class='bar-count'>{escape(conteo[key])}</span>"
            f"</div>"
        )
    return (
        "<div class='chart-wrap'>"
        f"<p class='chart-title'>{ico('activity', 16)} Distribución de estados</p>"
        "<div class='chart-bars'>" + "".join(filas) + "</div>"
        "</div>"
    )


def actividad_reciente(historial: list[ConsultaResumen], limite: int = 6) -> str:
    if not historial:
        return (
            "<div class='card'>"
            "<p class='muted' style='text-align:center;padding:16px'>Sin actividad reciente.</p>"
            "</div>"
        )
    recientes = sorted(historial, key=lambda x: x.creada_en, reverse=True)[:limite]
    items = []
    for item in recientes:
        items.append(
            f"<div class='activity-item'>"
            f"<div class='activity-dot {escape(item.estado)}'></div>"
            f"<div class='activity-body'>"
            f"<p class='activity-title'><a href='/consultas/{escape(item.id)}' "
            f"style='color:var(--text);text-decoration:none'>"
            f"{escape(motivo_label(item.motivo))}</a></p>"
            f"<p class='activity-meta'>{escape(format_fecha(item.creada_en))}</p>"
            f"</div>"
            f"<div class='activity-badge'>{badge(item.estado, 'consulta')}</div>"
            f"</div>"
        )
    return (
        "<div class='card'>"
        f"<p class='section-title' style='margin-top:0'>{ico('activity', 16)} Actividad reciente</p>"
        "<div class='activity-list'>" + "".join(items) + "</div>"
        "</div>"
    )


def timeline_estado(estado: str) -> str:
    pasos = [
        ("pendiente",          "1", "Pendiente",          "Consulta registrada, esperando respuesta."),
        ("en_revision",        "2", "En revisión",        "Taller o tienda procesando la solicitud."),
        ("confirmada_parcial", "3", "Confirmada parcial", "Una disponibilidad confirmada, otra pendiente."),
        ("confirmada",         "4", "Confirmada",         "Todo confirmado. Conductor puede acudir."),
        ("no_resuelta",        "✕", "No resuelta",        "No hay disponibilidad suficiente."),
    ]
    flujo_normal = ["pendiente", "en_revision", "confirmada_parcial", "confirmada"]
    es_terminal_bad = estado == "no_resuelta"

    html_steps = []
    for key, num, label, desc in pasos:
        if es_terminal_bad and key == "no_resuelta":
            cls = "bad"
        elif es_terminal_bad:
            cls = "done" if key == "pendiente" else ""
        elif key == estado:
            cls = "active"
        elif (
            key in flujo_normal
            and estado in flujo_normal
            and flujo_normal.index(key) < flujo_normal.index(estado)
        ):
            cls = "done"
        else:
            cls = ""

        html_steps.append(
            f"<div class='timeline-step {cls}'>"
            f"<div class='timeline-dot'>{escape(num)}</div>"
            f"<div class='timeline-info'>"
            f"<p class='timeline-label'>{escape(label)}</p>"
            f"<p class='timeline-desc'>{escape(desc)}</p>"
            f"</div>"
            f"</div>"
        )
    return "<div class='state-timeline'>" + "".join(html_steps) + "</div>"


def avail_icon_cls(estado: str) -> str:
    return {
        "disponible":             "ok",
        "no_disponible":          "bad",
        "pendiente_confirmacion": "warn",
    }.get(estado, "info")


def avail_icon_svg(estado: str) -> str:
    mapping = {
        "disponible":             ico("check", 20),
        "no_disponible":          ico("x", 20),
        "pendiente_confirmacion": ico("clock", 20),
    }
    return mapping.get(estado, ico("info", 20))
