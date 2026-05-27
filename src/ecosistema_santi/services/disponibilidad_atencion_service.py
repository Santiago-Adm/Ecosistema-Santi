from __future__ import annotations

from typing import Protocol

from ..domain.disponibilidad_atencion import DisponibilidadAtencion
from ..logging_config import get_logger

_logger = get_logger("services.disponibilidad_atencion")


class ConsultaRepository(Protocol):
    def get_by_id(self, consulta_id: str) -> object | None:
        ...


class ConsultaEstadoService(Protocol):
    def recalcular_estado(self, consulta_id: str) -> str:
        ...


class DisponibilidadAtencionRepository(Protocol):
    def save(self, disponibilidad: DisponibilidadAtencion) -> DisponibilidadAtencion:
        ...

    def get_by_consulta_id(self, consulta_id: str) -> DisponibilidadAtencion | None:
        ...


class DisponibilidadAtencionService:
    def __init__(
        self,
        disponibilidad_repository: DisponibilidadAtencionRepository,
        consulta_repository: ConsultaRepository,
        estado_service: ConsultaEstadoService,
    ) -> None:
        self._disponibilidad_repository = disponibilidad_repository
        self._consulta_repository = consulta_repository
        self._estado_service = estado_service

    def registrar_disponibilidad(
        self, consulta_id: str, estado: str
    ) -> DisponibilidadAtencion:
        if self._consulta_repository.get_by_id(consulta_id) is None:
            _logger.warning("disponibilidad_atencion_consulta_no_existe", extra={"consulta_id": consulta_id})
            raise ValueError("consulta inexistente")
        disponibilidad = DisponibilidadAtencion.crear(
            consulta_id=consulta_id,
            estado=estado,
        )
        resultado = self._disponibilidad_repository.save(disponibilidad)
        nuevo_estado = self._estado_service.recalcular_estado(consulta_id)
        _logger.info("disponibilidad_atencion_registrada", extra={
            "consulta_id": consulta_id,
            "estado_disponibilidad": estado,
            "estado_consulta": nuevo_estado,
        })
        return resultado

    def obtener_disponibilidad(self, consulta_id: str) -> DisponibilidadAtencion | None:
        if self._consulta_repository.get_by_id(consulta_id) is None:
            raise ValueError("consulta inexistente")
        disponibilidad = self._disponibilidad_repository.get_by_consulta_id(consulta_id)
        if disponibilidad is not None:
            return disponibilidad
        return DisponibilidadAtencion.crear(
            consulta_id=consulta_id,
            estado="pendiente_confirmacion",
        )
