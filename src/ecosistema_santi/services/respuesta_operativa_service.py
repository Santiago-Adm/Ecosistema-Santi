from __future__ import annotations

from typing import Protocol

from ..domain.respuesta_operativa import RespuestaOperativa
from ..logging_config import get_logger

_logger = get_logger("services.respuesta_operativa")


class ConsultaRepository(Protocol):
    def get_by_id(self, consulta_id: str) -> object | None:
        ...


class ConsultaEstadoService(Protocol):
    def recalcular_estado(self, consulta_id: str) -> str:
        ...


class RespuestaOperativaRepository(Protocol):
    def save(self, respuesta: RespuestaOperativa) -> RespuestaOperativa:
        ...

    def get_by_consulta_id(self, consulta_id: str) -> RespuestaOperativa | None:
        ...


class RespuestaOperativaService:
    def __init__(
        self,
        respuesta_repository: RespuestaOperativaRepository,
        consulta_repository: ConsultaRepository,
        estado_service: ConsultaEstadoService,
    ) -> None:
        self._respuesta_repository = respuesta_repository
        self._consulta_repository = consulta_repository
        self._estado_service = estado_service

    def registrar_respuesta(
        self,
        consulta_id: str,
        estado_general: str,
        observacion: str,
        costo_estimado: float | None = None,
    ) -> RespuestaOperativa:
        if self._consulta_repository.get_by_id(consulta_id) is None:
            _logger.warning("respuesta_operativa_consulta_no_existe", extra={"consulta_id": consulta_id})
            raise ValueError("consulta inexistente")
        respuesta = RespuestaOperativa.crear(
            consulta_id=consulta_id,
            estado_general=estado_general,
            observacion=observacion,
            costo_estimado=costo_estimado,
        )
        resultado = self._respuesta_repository.save(respuesta)
        nuevo_estado = self._estado_service.recalcular_estado(consulta_id)
        _logger.info("respuesta_operativa_registrada", extra={
            "consulta_id": consulta_id,
            "estado_general": estado_general,
            "costo_estimado": costo_estimado,
            "estado_consulta": nuevo_estado,
        })
        return resultado

    def obtener_respuesta(self, consulta_id: str) -> RespuestaOperativa | None:
        if self._consulta_repository.get_by_id(consulta_id) is None:
            raise ValueError("consulta inexistente")
        return self._respuesta_repository.get_by_consulta_id(consulta_id)
