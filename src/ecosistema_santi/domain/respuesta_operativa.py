from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


def _validar_texto_no_vacio(valor: str, campo: str) -> str:
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} es obligatorio")
    return valor.strip()


def _validar_costo(costo: float | None) -> float | None:
    if costo is None:
        return None
    if not isinstance(costo, (int, float)):
        raise ValueError("costo_estimado inválido")
    return float(costo)


@dataclass(frozen=True)
class RespuestaOperativa:
    consulta_id: str
    estado_general: str
    observacion: str
    costo_estimado: float | None
    actualizado_en: datetime

    @staticmethod
    def crear(
        consulta_id: str, estado_general: str, observacion: str, costo_estimado: float | None
    ) -> "RespuestaOperativa":
        consulta_validada = _validar_texto_no_vacio(consulta_id, "consulta_id")
        estado_validado = _validar_texto_no_vacio(estado_general, "estado_general")
        observacion_validada = _validar_texto_no_vacio(observacion, "observacion")
        costo_validado = _validar_costo(costo_estimado)
        actualizado_en = datetime.now(timezone.utc)

        return RespuestaOperativa(
            consulta_id=consulta_validada,
            estado_general=estado_validado,
            observacion=observacion_validada,
            costo_estimado=costo_validado,
            actualizado_en=actualizado_en,
        )
