from pathlib import Path
import tempfile

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.persistence.consulta_repository import SQLiteConsultaRepository


def test_sqlite_persistencia_de_consulta():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteConsultaRepository(str(db_path))

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-1",
            motivo="repuesto",
            descripcion="necesito pastillas de freno",
        )
        repo.save(consulta)

        recuperada = repo.get_by_id(consulta.id)

        assert recuperada == consulta


def test_sqlite_listar_consultas():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteConsultaRepository(str(db_path))

        consulta_1 = ConsultaAtencion.crear(
            conductor_id="conductor-1",
            motivo="repuesto",
            descripcion="necesito llanta delantera",
        )
        consulta_2 = ConsultaAtencion.crear(
            conductor_id="conductor-2",
            motivo="mantenimiento_preventivo",
            descripcion="cambio de aceite",
        )
        repo.save(consulta_1)
        repo.save(consulta_2)

        consultas = repo.list_all()

        ids = {consulta.id for consulta in consultas}
        assert consulta_1.id in ids
        assert consulta_2.id in ids


def test_sqlite_actualizar_estado_consulta():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteConsultaRepository(str(db_path))

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-3",
            motivo="reparacion_correctiva",
            descripcion="no enciende",
        )
        repo.save(consulta)

        actualizada = repo.update_estado(consulta.id, "en_revision")

        assert actualizada is not None
        assert actualizada.estado == "en_revision"


def test_sqlite_get_by_id_retorna_none_si_no_existe():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteConsultaRepository(str(db_path))
        assert repo.get_by_id("id-inexistente") is None


def test_sqlite_update_estado_retorna_none_si_no_existe():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteConsultaRepository(str(db_path))
        assert repo.update_estado("id-inexistente", "en_revision") is None


def test_sqlite_consulta_repository_close():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteConsultaRepository(str(db_path))
        repo.close()
