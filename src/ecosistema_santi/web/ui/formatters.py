from __future__ import annotations

import html
from datetime import datetime, timezone
from typing import Any


def escape(valor: Any) -> str:
    return html.escape(str(valor))


def format_costo(costo: float | None) -> str:
    if costo is None:
        return "no registrado"
    return f"S/ {costo:.2f}"


def format_fecha(dt: datetime) -> str:
    now = datetime.now(timezone.utc)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    delta = now - dt
    s = int(delta.total_seconds())
    if s < 60:
        return "hace un momento"
    if s < 3600:
        return f"hace {s // 60} min"
    if s < 86400:
        return f"hace {s // 3600} h"
    d = s // 86400
    if d < 30:
        return f"hace {d} días"
    return dt.strftime("%d/%m/%Y")


def motivo_label(motivo: str) -> str:
    mapping = {
        "mantenimiento_preventivo": "Mantenimiento",
        "reparacion_correctiva":    "Reparación",
        "repuesto":                 "Repuesto",
    }
    return mapping.get(motivo, motivo.replace("_", " "))


def motivo_icono(motivo: str) -> str:
    mapping = {
        "mantenimiento_preventivo": "tool",
        "reparacion_correctiva":    "wrench",
        "repuesto":                 "package",
    }
    return mapping.get(motivo, "layers")


def field(form: dict[str, list[str]], name: str) -> str:
    return form.get(name, [""])[0].strip()


def select_options(opciones: list[str], seleccionado: str | None) -> str:
    parts = []
    for opcion in opciones:
        selected = " selected" if opcion == seleccionado else ""
        label = opcion.replace("_", " ").title() if opcion else "— Todos —"
        parts.append(
            f"<option value='{escape(opcion)}'{selected}>{escape(label)}</option>"
        )
    return "\n".join(parts)
