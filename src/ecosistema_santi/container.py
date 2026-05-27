from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .persistence.consulta_repository import SQLiteConsultaRepository
from .persistence.disponibilidad_atencion_repository import (
    SQLiteDisponibilidadAtencionRepository,
)
from .persistence.disponibilidad_repuesto_repository import (
    SQLiteDisponibilidadRepuestoRepository,
)
from .persistence.respuesta_operativa_repository import (
    SQLiteRespuestaOperativaRepository,
)
from .services.consulta_estado_service import ConsultaEstadoService
from .services.consulta_service import ConsultaService
from .services.disponibilidad_atencion_service import DisponibilidadAtencionService
from .services.disponibilidad_repuesto_service import DisponibilidadRepuestoService
from .services.historial_consultas_service import HistorialConsultasService
from .services.respuesta_operativa_service import RespuestaOperativaService


@dataclass
class Servicios:
    consulta_repo: SQLiteConsultaRepository
    atencion_repo: SQLiteDisponibilidadAtencionRepository
    repuesto_repo: SQLiteDisponibilidadRepuestoRepository
    respuesta_repo: SQLiteRespuestaOperativaRepository
    consulta_service: ConsultaService
    estado_service: ConsultaEstadoService
    atencion_service: DisponibilidadAtencionService
    repuesto_service: DisponibilidadRepuestoService
    respuesta_service: RespuestaOperativaService
    historial_service: HistorialConsultasService

    def close(self) -> None:
        self.consulta_repo.close()
        self.atencion_repo.close()
        self.repuesto_repo.close()
        self.respuesta_repo.close()


def resolver_db_path(db_path: str) -> str:
    if db_path == ":memory:":
        return db_path
    ruta = Path(db_path)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    return str(ruta)


def construir_servicios(db_path: str) -> Servicios:
    consulta_repo = SQLiteConsultaRepository(db_path)
    atencion_repo = SQLiteDisponibilidadAtencionRepository(db_path)
    repuesto_repo = SQLiteDisponibilidadRepuestoRepository(db_path)
    respuesta_repo = SQLiteRespuestaOperativaRepository(db_path)
    estado_service = ConsultaEstadoService(
        consulta_repo, atencion_repo, repuesto_repo, respuesta_repo
    )
    consulta_service = ConsultaService(consulta_repo)
    atencion_service = DisponibilidadAtencionService(
        atencion_repo, consulta_repo, estado_service
    )
    repuesto_service = DisponibilidadRepuestoService(
        repuesto_repo, consulta_repo, estado_service
    )
    respuesta_service = RespuestaOperativaService(
        respuesta_repo, consulta_repo, estado_service
    )
    historial_service = HistorialConsultasService(consulta_repo)
    return Servicios(
        consulta_repo=consulta_repo,
        atencion_repo=atencion_repo,
        repuesto_repo=repuesto_repo,
        respuesta_repo=respuesta_repo,
        consulta_service=consulta_service,
        estado_service=estado_service,
        atencion_service=atencion_service,
        repuesto_service=repuesto_service,
        respuesta_service=respuesta_service,
        historial_service=historial_service,
    )
