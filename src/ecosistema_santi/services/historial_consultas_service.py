from __future__ import annotations

from typing import Protocol

from ..domain.consulta import ConsultaAtencion, es_activa
from ..domain.historial import ConsultaResumen


class ConsultaRepository(Protocol):
    def list_all(self) -> list[ConsultaAtencion]:
        ...


class HistorialConsultasService:
    def __init__(self, consulta_repository: ConsultaRepository) -> None:
        self._consulta_repository = consulta_repository

    def obtener_historial(self) -> list[ConsultaResumen]:
        consultas = self._consulta_repository.list_all()
        return [
            ConsultaResumen(
                id=consulta.id,
                motivo=consulta.motivo,
                estado=consulta.estado,
                creada_en=consulta.creada_en,
                es_activa=es_activa(consulta.estado),
            )
            for consulta in consultas
        ]
