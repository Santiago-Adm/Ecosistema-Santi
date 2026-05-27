from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

MOTIVOS_PERMITIDOS = {
    "mantenimiento_preventivo",
    "reparacion_correctiva",
    "repuesto",
}

ESTADOS_PERMITIDOS = {
    "pendiente",
    "en_revision",
    "confirmada_parcial",
    "confirmada",
    "no_resuelta",
}

ESTADOS_ACTIVOS = {
    "pendiente",
    "en_revision",
    "confirmada_parcial",
}

ESTADOS_CERRADOS = {
    "confirmada",
    "no_resuelta",
}

ESTADOS_DISPONIBILIDAD = {
    "disponible",
    "no_disponible",
    "pendiente_confirmacion",
}


def _validar_texto_no_vacio(valor: str, campo: str) -> str:
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} es obligatorio")
    return valor.strip()


def _validar_motivo(motivo: str) -> str:
    motivo_normalizado = _validar_texto_no_vacio(motivo, "motivo")
    if motivo_normalizado not in MOTIVOS_PERMITIDOS:
        raise ValueError("motivo no permitido")
    return motivo_normalizado


def _validar_disponibilidad(estado: str | None, campo: str) -> str | None:
    if estado is None:
        return None
    estado_normalizado = _validar_texto_no_vacio(estado, campo)
    if estado_normalizado not in ESTADOS_DISPONIBILIDAD:
        raise ValueError(f"{campo} no permitido")
    return estado_normalizado


def calcular_estado(
    disponibilidad_atencion: str | None,
    disponibilidad_repuesto: str | None,
    tiene_respuesta: bool,
) -> str:
    atencion = _validar_disponibilidad(disponibilidad_atencion, "disponibilidad_atencion")
    repuesto = _validar_disponibilidad(disponibilidad_repuesto, "disponibilidad_repuesto")

    if "no_disponible" in {atencion, repuesto}:
        return "no_resuelta"
    if atencion == "disponible" and repuesto == "disponible":
        return "confirmada"
    if (
        (atencion == "disponible" and repuesto in {None, "pendiente_confirmacion"})
        or (repuesto == "disponible" and atencion in {None, "pendiente_confirmacion"})
    ):
        return "confirmada_parcial"
    if tiene_respuesta:
        return "en_revision"
    return "pendiente"


def es_activa(estado: str) -> bool:
    estado_normalizado = _validar_texto_no_vacio(estado, "estado")
    if estado_normalizado not in ESTADOS_PERMITIDOS:
        raise ValueError("estado no permitido")
    return estado_normalizado in ESTADOS_ACTIVOS


@dataclass(frozen=True)
class ConsultaAtencion:
    id: str
    conductor_id: str
    motivo: str
    descripcion: str
    estado: str
    creada_en: datetime

    @staticmethod
    def crear(conductor_id: str, motivo: str, descripcion: str) -> "ConsultaAtencion":
        conductor_validado = _validar_texto_no_vacio(conductor_id, "conductor_id")
        motivo_validado = _validar_motivo(motivo)
        descripcion_validada = _validar_texto_no_vacio(descripcion, "descripcion")
        creada_en = datetime.now(timezone.utc)

        return ConsultaAtencion(
            id=str(uuid4()),
            conductor_id=conductor_validado,
            motivo=motivo_validado,
            descripcion=descripcion_validada,
            estado="pendiente",
            creada_en=creada_en,
        )
