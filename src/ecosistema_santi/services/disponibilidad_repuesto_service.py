from __future__ import annotations

from typing import Protocol

from ..domain.disponibilidad_repuesto import DisponibilidadRepuesto
from ..logging_config import get_logger

_logger = get_logger("services.disponibilidad_repuesto")


class ConsultaRepository(Protocol):
    def get_by_id(self, consulta_id: str) -> object | None:
        ...


class ConsultaEstadoService(Protocol):
    def recalcular_estado(self, consulta_id: str) -> str:
        ...


class DisponibilidadRepuestoRepository(Protocol):
    def save(self, disponibilidad: DisponibilidadRepuesto) -> DisponibilidadRepuesto:
        ...

    def get_by_consulta_id(self, consulta_id: str) -> DisponibilidadRepuesto | None:
        ...


class DisponibilidadRepuestoService:
    def __init__(
        self,
        disponibilidad_repository: DisponibilidadRepuestoRepository,
        consulta_repository: ConsultaRepository,
        estado_service: ConsultaEstadoService,
    ) -> None:
        self._disponibilidad_repository = disponibilidad_repository
        self._consulta_repository = consulta_repository
        self._estado_service = estado_service

    def registrar_disponibilidad(
        self, consulta_id: str, estado: str
    ) -> DisponibilidadRepuesto:
        if self._consulta_repository.get_by_id(consulta_id) is None:
            _logger.warning("disponibilidad_repuesto_consulta_no_existe", extra={"consulta_id": consulta_id})
            raise ValueError("consulta inexistente")
        disponibilidad = DisponibilidadRepuesto.crear(
            consulta_id=consulta_id,
            estado=estado,
        )
        resultado = self._disponibilidad_repository.save(disponibilidad)
        nuevo_estado = self._estado_service.recalcular_estado(consulta_id)
        _logger.info("disponibilidad_repuesto_registrada", extra={
            "consulta_id": consulta_id,
            "estado_disponibilidad": estado,
            "estado_consulta": nuevo_estado,
        })
        return resultado

    def obtener_disponibilidad(self, consulta_id: str) -> DisponibilidadRepuesto:
        if self._consulta_repository.get_by_id(consulta_id) is None:
            raise ValueError("consulta inexistente")
        disponibilidad = self._disponibilidad_repository.get_by_consulta_id(consulta_id)
        if disponibilidad is not None:
            return disponibilidad
        return DisponibilidadRepuesto.crear(
            consulta_id=consulta_id,
            estado="pendiente_confirmacion",
        )
