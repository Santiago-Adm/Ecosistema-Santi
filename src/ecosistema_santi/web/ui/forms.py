from __future__ import annotations

from .formatters import escape
from .icons import ico


def form_crear_consulta(valores: dict[str, str]) -> str:
    motivos = [
        ("mantenimiento_preventivo", "Mantenimiento preventivo",
         "Cambio de aceite, filtros, revisión periódica programada"),
        ("reparacion_correctiva",    "Reparación correctiva",
         "Falla, avería o daño que impide el funcionamiento normal"),
        ("repuesto",                 "Necesito un repuesto",
         "Búsqueda y adquisición de pieza o componente específico"),
    ]
    opts = []
    for val, label, _ in motivos:
        selected = " selected" if val == valores.get("motivo") else ""
        opts.append(f"<option value='{val}'{selected}>{escape(label)}</option>")

    return (
        f"<div class='form-card'>"
        f"<div class='form-card-header'>"
        f"<h2>{ico('plus', 20)} Nueva consulta</h2>"
        f"<p>Registra tu necesidad y el taller validará disponibilidad.</p>"
        f"</div>"
        f"<div class='form-card-body'>"
        f"<form method='post' action='/consultas'>"
        f"<div class='form-group'>"
        f"<label class='form-label' for='conductor_id'>{ico('user', 14)} Identificación del conductor</label>"
        f"<input type='text' id='conductor_id' name='conductor_id' "
        f"value='{escape(valores.get('conductor_id', ''))}' "
        f"placeholder='Ej: conductor-juan-01' required>"
        f"<p class='form-help'>Tu código o nombre para identificar la consulta.</p>"
        f"</div>"
        f"<div class='form-group'>"
        f"<label class='form-label' for='motivo'>{ico('layers', 14)} Motivo de la consulta</label>"
        f"<select id='motivo' name='motivo' required>"
        + "\n".join(opts) +
        f"</select>"
        f"</div>"
        f"<div class='form-group'>"
        f"<label class='form-label' for='descripcion'>{ico('info', 14)} Descripción del problema</label>"
        f"<textarea id='descripcion' name='descripcion' "
        f"placeholder='Describe el problema en tus propias palabras.' "
        f"required>{escape(valores.get('descripcion', ''))}</textarea>"
        f"<p class='form-help'>Usa lenguaje simple. Más detalle ayuda al taller a prepararse.</p>"
        f"</div>"
        f"<div class='btn-row'>"
        f"<button type='submit' class='btn btn-primary btn-lg'>{ico('arrow-r', 16)} Registrar consulta</button>"
        f"<a href='/consultas' class='btn btn-secondary'>Cancelar</a>"
        f"</div>"
        f"</form>"
        f"</div>"
        f"</div>"
    )


def form_disponibilidad(consulta_id: str, tipo: str) -> str:
    titulo = (
        "Actualizar disponibilidad de atención"
        if tipo == "atencion"
        else "Actualizar disponibilidad de repuesto"
    )
    icon_name = "tool" if tipo == "atencion" else "package"
    opts = [
        ("disponible",             "Disponible"),
        ("no_disponible",          "No disponible"),
        ("pendiente_confirmacion", "Pendiente de confirmación"),
    ]
    opt_html = "\n".join(
        f"<option value='{v}'>{escape(l)}</option>" for v, l in opts
    )
    return (
        f"<div class='form-section'>"
        f"<div class='form-section-header'>"
        f"<span class='form-section-title'>{ico(icon_name, 15)} {escape(titulo)}</span>"
        f"<span class='toggle-icon'>▼</span>"
        f"</div>"
        f"<div class='form-section-body'>"
        f"<form method='post' action='/consultas/{escape(consulta_id)}/{escape(tipo)}'>"
        f"<div class='form-group'>"
        f"<label class='form-label'>Estado de {escape(tipo)}</label>"
        f"<select name='estado' required>{opt_html}</select>"
        f"</div>"
        f"<div class='btn-row' style='margin-top:12px'>"
        f"<button type='submit' class='btn btn-primary btn-sm'>{ico('check', 14)} Registrar</button>"
        f"</div>"
        f"</form>"
        f"</div>"
        f"</div>"
    )


def form_respuesta(consulta_id: str, valores: dict[str, str]) -> str:
    return (
        f"<div class='form-section'>"
        f"<div class='form-section-header'>"
        f"<span class='form-section-title'>{ico('activity', 15)} Registrar respuesta operativa</span>"
        f"<span class='toggle-icon'>▼</span>"
        f"</div>"
        f"<div class='form-section-body'>"
        f"<form method='post' action='/consultas/{escape(consulta_id)}/respuesta'>"
        f"<div class='form-group'>"
        f"<label class='form-label'>Estado general</label>"
        f"<input type='text' name='estado_general' "
        f"value='{escape(valores.get('estado_general', ''))}' "
        f"placeholder='Ej: confirmado, en proceso, no disponible' required>"
        f"</div>"
        f"<div class='form-group'>"
        f"<label class='form-label'>Observación</label>"
        f"<textarea name='observacion' "
        f"placeholder='Detalles útiles para que el conductor decida si acude o espera.' "
        f"required>{escape(valores.get('observacion', ''))}</textarea>"
        f"</div>"
        f"<div class='form-group'>"
        f"<label class='form-label'>Costo estimado <span class='muted'>(opcional)</span></label>"
        f"<input type='number' step='0.01' name='costo_estimado' "
        f"value='{escape(valores.get('costo_estimado', ''))}' "
        f"placeholder='0.00'>"
        f"<p class='form-help'>En soles. Solo si ya tienes información suficiente.</p>"
        f"</div>"
        f"<div class='btn-row' style='margin-top:12px'>"
        f"<button type='submit' class='btn btn-success btn-sm'>{ico('check', 14)} Registrar respuesta</button>"
        f"</div>"
        f"</form>"
        f"</div>"
        f"</div>"
    )


def form_filtros(estado: str, motivo: str) -> str:
    estados = ["", "pendiente", "en_revision", "confirmada_parcial", "confirmada", "no_resuelta"]
    motivos = ["", "mantenimiento_preventivo", "reparacion_correctiva", "repuesto"]

    def opts(lista: list[str], sel: str | None) -> str:
        parts = []
        for v in lista:
            selected = " selected" if v == sel else ""
            label = v.replace("_", " ").title() if v else "— Todos —"
            parts.append(f"<option value='{escape(v)}'{selected}>{escape(label)}</option>")
        return "\n".join(parts)

    return (
        f"<div class='filter-bar'>"
        f"<div class='filter-group'>"
        f"<span class='filter-label'>{ico('filter', 12)} Estado</span>"
        f"<form id='filter-form' method='get' action='/consultas'>"
        f"<select name='estado'>{opts(estados, estado or None)}</select>"
        f"</form>"
        f"</div>"
        f"<div class='filter-group'>"
        f"<span class='filter-label'>{ico('layers', 12)} Motivo</span>"
        f"<select name='motivo' form='filter-form'>{opts(motivos, motivo or None)}</select>"
        f"</div>"
        f"<div style='display:flex;gap:8px;align-items:flex-end'>"
        f"<button type='submit' form='filter-form' class='btn btn-primary btn-sm'>{ico('filter', 14)} Filtrar</button>"
        f"<a href='/consultas' class='btn btn-secondary btn-sm'>Limpiar</a>"
        f"</div>"
        f"</div>"
    )


def form_ir_consulta() -> str:
    return (
        f"<form method='get' action='/consultas' style='display:flex;gap:8px;align-items:flex-end;margin-bottom:20px'>"
        f"<div style='flex:1'>"
        f"<input type='text' name='consulta_id' placeholder='Pegar UUID de consulta…' style='margin:0'>"
        f"</div>"
        f"<button type='submit' class='btn btn-secondary btn-sm'>{ico('search', 14)} Buscar</button>"
        f"</form>"
    )
