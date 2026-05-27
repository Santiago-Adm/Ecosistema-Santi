from __future__ import annotations

from ...domain.consulta import ConsultaAtencion
from ...domain.disponibilidad_atencion import DisponibilidadAtencion
from ...domain.disponibilidad_repuesto import DisponibilidadRepuesto
from ...domain.historial import ConsultaResumen
from ...domain.respuesta_operativa import RespuestaOperativa
from .components import (
    actividad_reciente,
    avail_icon_cls,
    avail_icon_svg,
    badge,
    barra_estados,
    kpi_card,
    timeline_estado,
)
from .formatters import escape, format_costo, format_fecha, motivo_icono, motivo_label
from .forms import form_ir_consulta
from .icons import ico


# ── KPI summary ──────────────────────────────────────────────────────────────

def render_resumen(historial: list[ConsultaResumen]) -> str:
    total = len(historial)
    activas = sum(1 for x in historial if x.es_activa)
    confirmadas = sum(1 for x in historial if x.estado == "confirmada")
    no_resueltas = sum(1 for x in historial if x.estado == "no_resuelta")
    return (
        "<div class='kpi-grid'>"
        + kpi_card("Total",        total,        "consultas registradas",  "blue",  "layers")
        + kpi_card("Activas",      activas,      "en proceso",             "amber", "clock")
        + kpi_card("Confirmadas",  confirmadas,  "listas para atender",    "green", "check")
        + kpi_card("No resueltas", no_resueltas, "sin disponibilidad",     "red",   "x")
        + "</div>"
    )


# ── Historial table ───────────────────────────────────────────────────────────

def render_historial(historial: list[ConsultaResumen]) -> str:
    if not historial:
        return (
            "<div class='table-wrap'>"
            "<div class='empty-state'>"
            "<div class='empty-state-icon'>" + ico("list", 26) + "</div>"
            "<p class='empty-state-title'>Sin consultas</p>"
            "<p class='empty-state-text'>No hay consultas que coincidan con los filtros aplicados.</p>"
            f"<a href='/consultas/nueva' class='btn btn-primary'>{ico('plus', 16)} Nueva consulta</a>"
            "</div></div>"
        )

    rows = []
    for item in historial:
        m_label = motivo_label(item.motivo)
        m_ico = ico(motivo_icono(item.motivo), 14)
        rows.append(
            "<tr>"
            f"<td class='td-mono'><a href='/consultas/{escape(item.id)}' "
            f"style='color:var(--primary);text-decoration:none;font-family:var(--font-mono)'>"
            f"{escape(item.id[:8])}…</a></td>"
            f"<td><span class='motivo-chip'>{m_ico} {escape(m_label)}</span></td>"
            f"<td>{badge(item.estado, 'consulta')}</td>"
            f"<td class='muted'>{escape(format_fecha(item.creada_en))}</td>"
            f"<td class='td-action'><a href='/consultas/{escape(item.id)}'>Ver detalle</a></td>"
            "</tr>"
        )

    n = len(historial)
    return (
        "<div class='table-wrap'>"
        f"<div class='table-toolbar'>"
        f"<span class='table-count'>{ico('list', 14)} {escape(n)} resultado{'s' if n != 1 else ''}</span>"
        f"</div>"
        "<table>"
        "<thead><tr><th>ID</th><th>Motivo</th><th>Estado</th><th>Creada</th><th>Acción</th></tr></thead>"
        "<tbody>" + "".join(rows) + "</tbody>"
        "</table></div>"
    )


# ── Dashboard ─────────────────────────────────────────────────────────────────

def render_dashboard(historial: list[ConsultaResumen]) -> str:
    total = len(historial)
    activas = sum(1 for x in historial if x.es_activa)
    pendientes = sum(1 for x in historial if x.estado == "pendiente")

    sidebar = (
        actividad_reciente(historial, 5)
        + "<div class='card' style='margin-top:16px'>"
        + f"<p class='section-title' style='margin-top:0'>{ico('arrow-r', 16)} Flujo operativo</p>"
        + "<ol style='margin:0;padding-left:20px;font-size:14px;color:var(--text-muted);line-height:2'>"
        + "<li>Conductor registra la consulta</li>"
        + "<li>Taller actualiza disponibilidad de atención</li>"
        + "<li>Tienda confirma disponibilidad de repuesto</li>"
        + "<li>Se registra respuesta con costo estimado</li>"
        + "<li>Conductor revisa estado y decide si acude</li>"
        + "</ol>"
        + "</div>"
    )

    quick = (
        f"<div class='quick-actions'>"
        f"<a href='/consultas/nueva' class='btn btn-primary'>{ico('plus', 16)} Nueva consulta</a>"
        f"<a href='/consultas' class='btn btn-secondary'>{ico('list', 16)} Ver historial</a>"
        f"</div>"
        + form_ir_consulta()
    )

    main_col = render_resumen(historial) + barra_estados(historial) + quick
    subtitle = (
        f"{escape(total)} consultas totales · "
        f"{escape(activas)} activas · "
        f"{escape(pendientes)} pendientes de respuesta"
    )

    return (
        f"<div class='page-header'>"
        f"<h1 class='page-title'>{ico('home', 20)} Panel principal</h1>"
        f"<p class='page-subtitle'>{subtitle}</p>"
        f"</div>"
        f"<div class='dashboard-grid'>"
        f"<div>{main_col}</div>"
        f"<div>{sidebar}</div>"
        f"</div>"
    )


# ── Detail page sub-renders ───────────────────────────────────────────────────

def render_consulta_header(consulta: ConsultaAtencion) -> str:
    m_label = motivo_label(consulta.motivo)
    m_ico = ico(motivo_icono(consulta.motivo), 18)
    fecha_str = (
        consulta.creada_en.strftime("%d/%m/%Y %H:%M")
        if hasattr(consulta.creada_en, "strftime")
        else str(consulta.creada_en)
    )
    return (
        "<div class='card mb-24'>"
        f"<div class='detalle-header'>"
        f"<div class='detalle-meta'>"
        f"<h2 class='detalle-title'>{m_ico} {escape(m_label)}</h2>"
        f"<div style='display:flex;gap:10px;align-items:center;flex-wrap:wrap'>"
        f"{badge(consulta.estado, 'consulta')}"
        f"<span class='detalle-id' data-id='{escape(consulta.id)}'>"
        f"{ico('copy', 12)} {escape(consulta.id)}"
        f"</span>"
        f"</div>"
        f"</div>"
        f"</div>"
        f"<hr class='divider'>"
        f"<div class='info-row'><span class='info-key'>{ico('user', 14)} Conductor</span>"
        f"<span class='info-val'>{escape(consulta.conductor_id)}</span></div>"
        f"<div class='info-row'><span class='info-key'>{ico('clock', 14)} Registrada</span>"
        f"<span class='info-val'>{escape(format_fecha(consulta.creada_en))}"
        f" <span class='muted'>— {escape(fecha_str)}</span></span></div>"
        f"<div class='info-row' style='border-bottom:none'>"
        f"<span class='info-key'>{ico('info', 14)} Descripción</span>"
        f"<span class='info-val'><span class='descripcion-text'>{escape(consulta.descripcion)}</span></span></div>"
        f"</div>"
    )


def render_disponibilidad(
    disp: DisponibilidadAtencion | DisponibilidadRepuesto,
    titulo: str,
) -> str:
    cls = avail_icon_cls(disp.estado)
    svg = avail_icon_svg(disp.estado)
    return (
        f"<div class='avail-card'>"
        f"<div class='avail-header'><p class='avail-title'>{escape(titulo)}</p></div>"
        f"<div class='avail-status'>"
        f"<div class='avail-icon {cls}'>{svg}</div>"
        f"<div>"
        f"<p class='avail-text'>{badge(disp.estado, 'disponibilidad')}</p>"
        f"<p class='avail-ts'>{escape(format_fecha(disp.actualizado_en))}</p>"
        f"</div>"
        f"</div>"
        f"</div>"
    )


def render_respuesta(respuesta: RespuestaOperativa | None) -> str:
    if respuesta is None:
        return (
            "<div class='avail-card'>"
            f"<p class='muted' style='display:flex;align-items:center;gap:6px'>"
            f"{ico('clock', 14)} Sin respuesta registrada aún.</p>"
            "</div>"
        )
    costo_html = (
        f"<span class='costo-valor'>{escape(format_costo(respuesta.costo_estimado))}</span>"
        if respuesta.costo_estimado is not None
        else "<span class='costo-nulo'>No registrado</span>"
    )
    return (
        "<div class='resp-card'>"
        f"<div class='resp-estado'>{ico('check', 14)} {escape(respuesta.estado_general)}</div>"
        f"<p class='resp-obs'>{escape(respuesta.observacion)}</p>"
        f"<div class='resp-costo'>"
        f"{ico('activity', 14)}"
        f"<span style='color:var(--text-muted)'>Costo estimado:</span>"
        f"{costo_html}"
        f"</div>"
        f"<p class='avail-ts' style='margin-top:8px'>Actualizado {escape(format_fecha(respuesta.actualizado_en))}</p>"
        "</div>"
    )
