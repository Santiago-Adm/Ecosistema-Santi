from pathlib import Path
import tempfile

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.disponibilidad_repuesto import DisponibilidadRepuesto
from ecosistema_santi.persistence.consulta_repository import SQLiteConsultaRepository
from ecosistema_santi.persistence.disponibilidad_repuesto_repository import (
    SQLiteDisponibilidadRepuestoRepository,
)


def test_sqlite_persistencia_disponibilidad_repuesto():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        consulta_repo = SQLiteConsultaRepository(str(db_path))
        disponibilidad_repo = SQLiteDisponibilidadRepuestoRepository(str(db_path))

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-1",
            motivo="repuesto",
            descripcion="necesito pastillas de freno",
        )
        consulta_repo.save(consulta)

        disponibilidad = DisponibilidadRepuesto.crear(
            consulta_id=consulta.id,
            estado="no_disponible",
        )
        disponibilidad_repo.save(disponibilidad)

        recuperada = disponibilidad_repo.get_by_consulta_id(consulta.id)

        assert recuperada == disponibilidad


def test_sqlite_reemplaza_disponibilidad_existente():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        consulta_repo = SQLiteConsultaRepository(str(db_path))
        disponibilidad_repo = SQLiteDisponibilidadRepuestoRepository(str(db_path))

        consulta = ConsultaAtencion.crear(
            conductor_id="conductor-2",
            motivo="mantenimiento_preventivo",
            descripcion="cambio de aceite",
        )
        consulta_repo.save(consulta)

        disponibilidad_inicial = DisponibilidadRepuesto.crear(
            consulta_id=consulta.id,
            estado="pendiente_confirmacion",
        )
        disponibilidad_repo.save(disponibilidad_inicial)

        disponibilidad_actualizada = DisponibilidadRepuesto.crear(
            consulta_id=consulta.id,
            estado="disponible",
        )
        disponibilidad_repo.save(disponibilidad_actualizada)

        recuperada = disponibilidad_repo.get_by_consulta_id(consulta.id)

        assert recuperada == disponibilidad_actualizada


def test_sqlite_disponibilidad_repuesto_repository_close():
    with tempfile.TemporaryDirectory() as temp_dir:
        db_path = Path(temp_dir) / "consultas.db"
        repo = SQLiteDisponibilidadRepuestoRepository(str(db_path))
        repo.close()
