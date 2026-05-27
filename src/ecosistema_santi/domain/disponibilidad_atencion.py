from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

ESTADOS_DISPONIBILIDAD_ATENCION = {
    "disponible",
    "no_disponible",
    "pendiente_confirmacion",
}


def _validar_texto_no_vacio(valor: str, campo: str) -> str:
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} es obligatorio")
    return valor.strip()


def _validar_estado(estado: str) -> str:
    estado_normalizado = _validar_texto_no_vacio(estado, "estado")
    if estado_normalizado not in ESTADOS_DISPONIBILIDAD_ATENCION:
        raise ValueError("estado no permitido")
    return estado_normalizado


@dataclass(frozen=True)
class DisponibilidadAtencion:
    consulta_id: str
    estado: str
    actualizado_en: datetime

    @staticmethod
    def crear(consulta_id: str, estado: str) -> "DisponibilidadAtencion":
        consulta_validada = _validar_texto_no_vacio(consulta_id, "consulta_id")
        estado_validado = _validar_estado(estado)
        actualizado_en = datetime.now(timezone.utc)

        return DisponibilidadAtencion(
            consulta_id=consulta_validada,
            estado=estado_validado,
            actualizado_en=actualizado_en,
        )
