from pathlib import Path
import tempfile

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.respuesta_operativa import RespuestaOperativa
from ecosistema_santi.persistence.consulta_repository import SQLiteConsultaRepository
from ecosistema_santi.persistence.respuesta_operativa_repository import (
    SQLiteRespuestaOperativaRepository,
)


def test_sqlite_persistencia_respuesta_operativa():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        consulta_repo = SQLiteConsultaRepository(str(db_path))
        respuesta_repo = SQLiteRespuestaOperativaRepository(str(db_path))

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-1",
            motivo="repuesto",
            descripcion="necesito pastillas de freno",
        )
        consulta_repo.save(consulta)

        respuesta = RespuestaOperativa.crear(
            consulta_id=consulta.id,
            estado_general="en revision",
            observacion="revisando stock",
            costo_estimado=120.5,
        )
        respuesta_repo.save(respuesta)

        recuperada = respuesta_repo.get_by_consulta_id(consulta.id)

        assert recuperada == respuesta


def test_sqlite_reemplaza_respuesta_existente():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        consulta_repo = SQLiteConsultaRepository(str(db_path))
        respuesta_repo = SQLiteRespuestaOperativaRepository(str(db_path))

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-2",
            motivo="mantenimiento_preventivo",
            descripcion="cambio de aceite",
        )
        consulta_repo.save(consulta)

        respuesta_inicial = RespuestaOperativa.crear(
            consulta_id=consulta.id,
            estado_general="pendiente",
            observacion="a la espera",
            costo_estimado=None,
        )
        respuesta_repo.save(respuesta_inicial)

        respuesta_actualizada = RespuestaOperativa.crear(
            consulta_id=consulta.id,
            estado_general="confirmada",
            observacion="taller disponible",
            costo_estimado=80.0,
        )
        respuesta_repo.save(respuesta_actualizada)

        recuperada = respuesta_repo.get_by_consulta_id(consulta.id)

        assert recuperada == respuesta_actualizada


def test_sqlite_respuesta_operativa_repository_close():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteRespuestaOperativaRepository(str(db_path))
        repo.close()
