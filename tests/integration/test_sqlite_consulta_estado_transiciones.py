from pathlib import Path
import tempfile

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.persistence.consulta_repository import SQLiteConsultaRepository
from ecosistema_santi.persistence.disponibilidad_atencion_repository import (
    SQLiteDisponibilidadAtencionRepository,
)
from ecosistema_santi.persistence.disponibilidad_repuesto_repository import (
    SQLiteDisponibilidadRepuestoRepository,
)
from ecosistema_santi.persistence.respuesta_operativa_repository import (
    SQLiteRespuestaOperativaRepository,
)
from ecosistema_santi.services.consulta_estado_service import ConsultaEstadoService
from ecosistema_santi.services.disponibilidad_atencion_service import (
    DisponibilidadAtencionService,
)
from ecosistema_santi.services.disponibilidad_repuesto_service import (
    DisponibilidadRepuestoService,
)
from ecosistema_santi.services.respuesta_operativa_service import RespuestaOperativaService


def _crear_servicios(db_path: str):
    consulta_repo = SQLiteConsultaRepository(db_path)
    atencion_repo = SQLiteDisponibilidadAtencionRepository(db_path)
    repuesto_repo = SQLiteDisponibilidadRepuestoRepository(db_path)
    respuesta_repo = SQLiteRespuestaOperativaRepository(db_path)
    estado_service = ConsultaEstadoService(
        consulta_repo, atencion_repo, repuesto_repo, respuesta_repo
    )
    atencion_service = DisponibilidadAtencionService(
        atencion_repo, consulta_repo, estado_service
    )
    repuesto_service = DisponibilidadRepuestoService(
        repuesto_repo, consulta_repo, estado_service
    )
    respuesta_service = RespuestaOperativaService(
        respuesta_repo, consulta_repo, estado_service
    )
    return (
        consulta_repo,
        atencion_service,
        repuesto_service,
        respuesta_service,
    )


def test_transicion_en_revision_por_respuesta():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = str(Path(temp_dir) / "consultas.db")
        consulta_repo, _, _, respuesta_service = _crear_servicios(db_path)

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-1",
            motivo="repuesto",
            descripcion="necesito llanta delantera",
        )
        consulta_repo.save(consulta)

        respuesta_service.registrar_respuesta(
            consulta_id=consulta.id,
            estado_general="pendiente",
            observacion="revisando stock",
            costo_estimado=None,
        )

        actualizada = consulta_repo.get_by_id(consulta.id)
        assert actualizada is not None
        assert actualizada.estado == "en_revision"


def test_transicion_confirmada_parcial_por_atencion_disponible():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = str(Path(temp_dir) / "consultas.db")
        consulta_repo, atencion_service, _, _ = _crear_servicios(db_path)

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-2",
            motivo="mantenimiento_preventivo",
            descripcion="cambio de aceite",
        )
        consulta_repo.save(consulta)

        atencion_service.registrar_disponibilidad(
            consulta_id=consulta.id,
            estado="disponible",
        )

        actualizada = consulta_repo.get_by_id(consulta.id)
        assert actualizada is not None
        assert actualizada.estado == "confirmada_parcial"


def test_transicion_confirmada_con_ambas_disponibilidades():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = str(Path(temp_dir) / "consultas.db")
        consulta_repo, atencion_service, repuesto_service, _ = _crear_servicios(db_path)

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-3",
            motivo="repuesto",
            descripcion="necesito frenos",
        )
        consulta_repo.save(consulta)

        atencion_service.registrar_disponibilidad(
            consulta_id=consulta.id,
            estado="disponible",
        )
        repuesto_service.registrar_disponibilidad(
            consulta_id=consulta.id,
            estado="disponible",
        )

        actualizada = consulta_repo.get_by_id(consulta.id)
        assert actualizada is not None
        assert actualizada.estado == "confirmada"


def test_transicion_no_resuelta_por_no_disponible():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = str(Path(temp_dir) / "consultas.db")
        consulta_repo, _, repuesto_service, _ = _crear_servicios(db_path)

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-4",
            motivo="reparacion_correctiva",
            descripcion="no enciende",
        )
        consulta_repo.save(consulta)

        repuesto_service.registrar_disponibilidad(
            consulta_id=consulta.id,
            estado="no_disponible",
        )

        actualizada = consulta_repo.get_by_id(consulta.id)
        assert actualizada is not None
        assert actualizada.estado == "no_resuelta"
