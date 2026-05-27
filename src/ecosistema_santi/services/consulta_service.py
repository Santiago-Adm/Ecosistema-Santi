from __future__ import annotations

from typing import Protocol

from ..domain.consulta import ConsultaAtencion
from ..logging_config import get_logger

_logger = get_logger("services.consulta")


class ConsultaRepository(Protocol):
    def save(self, consulta: ConsultaAtencion) -> ConsultaAtencion:
        ...


class ConsultaService:
    def __init__(self, repository: ConsultaRepository) -> None:
        self._repository = repository

    def registrar_consulta(
        self, conductor_id: str, motivo: str, descripcion: str
    ) -> ConsultaAtencion:
        consulta = ConsultaAtencion.crear(
            conductor_id=conductor_id,
            motivo=motivo,
            descripcion=descripcion,
        )
        resultado = self._repository.save(consulta)
        _logger.info("consulta_registrada", extra={
            "consulta_id": resultado.id,
            "conductor_id": resultado.conductor_id,
            "motivo": resultado.motivo,
        })
        return resultado
