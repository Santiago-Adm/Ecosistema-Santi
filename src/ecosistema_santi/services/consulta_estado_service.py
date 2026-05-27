from __future__ import annotations

from typing import Protocol

from ..domain.consulta import ConsultaAtencion, calcular_estado
from ..domain.disponibilidad_atencion import DisponibilidadAtencion
from ..domain.disponibilidad_repuesto import DisponibilidadRepuesto
from ..domain.respuesta_operativa import RespuestaOperativa
from ..logging_config import get_logger

_logger = get_logger("services.consulta_estado")


class ConsultaRepository(Protocol):
    def get_by_id(self, consulta_id: str) -> ConsultaAtencion | None:
        ...

    def update_estado(self, consulta_id: str, estado: str) -> ConsultaAtencion | None:
        ...


class DisponibilidadAtencionRepository(Protocol):
    def get_by_consulta_id(self, consulta_id: str) -> DisponibilidadAtencion | None:
        ...


class DisponibilidadRepuestoRepository(Protocol):
    def get_by_consulta_id(self, consulta_id: str) -> DisponibilidadRepuesto | None:
        ...


class RespuestaOperativaRepository(Protocol):
    def get_by_consulta_id(self, consulta_id: str) -> RespuestaOperativa | None:
        ...


class ConsultaEstadoService:
    def __init__(
        self,
        consulta_repository: ConsultaRepository,
        disponibilidad_atencion_repository: DisponibilidadAtencionRepository,
        disponibilidad_repuesto_repository: DisponibilidadRepuestoRepository,
        respuesta_operativa_repository: RespuestaOperativaRepository,
    ) -> None:
        self._consulta_repository = consulta_repository
        self._disponibilidad_atencion_repository = disponibilidad_atencion_repository
        self._disponibilidad_repuesto_repository = disponibilidad_repuesto_repository
        self._respuesta_operativa_repository = respuesta_operativa_repository

    def recalcular_estado(self, consulta_id: str) -> str:
        consulta = self._consulta_repository.get_by_id(consulta_id)
        if consulta is None:
            _logger.warning("recalcular_estado_consulta_no_existe", extra={"consulta_id": consulta_id})
            raise ValueError("consulta inexistente")

        disponibilidad_atencion = self._disponibilidad_atencion_repository.get_by_consulta_id(
            consulta_id
        )
        disponibilidad_repuesto = self._disponibilidad_repuesto_repository.get_by_consulta_id(
            consulta_id
        )
        respuesta = self._respuesta_operativa_repository.get_by_consulta_id(consulta_id)

        nuevo_estado = calcular_estado(
            disponibilidad_atencion.estado if disponibilidad_atencion else None,
            disponibilidad_repuesto.estado if disponibilidad_repuesto else None,
            respuesta is not None,
        )

        actualizado = self._consulta_repository.update_estado(consulta_id, nuevo_estado)
        if actualizado is None:
            _logger.error("recalcular_estado_update_fallido", extra={
                "consulta_id": consulta_id,
                "nuevo_estado": nuevo_estado,
            })
            raise ValueError("consulta inexistente")

        _logger.info("estado_consulta_recalculado", extra={
            "consulta_id": consulta_id,
            "estado_anterior": consulta.estado,
            "estado_nuevo": nuevo_estado,
        })
        return nuevo_estado
