import pytest
from testcontainers.postgres import PostgresContainer

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.disponibilidad_repuesto import DisponibilidadRepuesto
from ecosistema_santi.persistence.postgres_connection import create_connection, ensure_schema
from tests.integration_postgres.postgres_repos import (
    _PostgresConsultaRepository,
    _PostgresDisponibilidadRepuestoRepository,
)


@pytest.fixture(scope="module")
def postgres_container():
    with PostgresContainer("postgres:16-alpine") as postgres:
        yield postgres


@pytest.fixture(scope="function")
def repository_pair(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn)
    with conn.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE consultas CASCADE;")
    conn.commit()
    consulta_repo = _PostgresConsultaRepository(conn)
    repuesto_repo = _PostgresDisponibilidadRepuestoRepository(conn)
    yield consulta_repo, repuesto_repo
    conn.close()


def test_postgres_persistencia_disponibilidad_repuesto(repository_pair):
    consulta_repo, repuesto_repo = repository_pair

    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="repuesto",
        descripcion="necesito llanta delantera",
    )
    consulta_repo.save(consulta)

    disponibilidad = DisponibilidadRepuesto.crear(
        consulta_id=consulta.id,
        estado="no_disponible",
    )
    repuesto_repo.save(disponibilidad)

    recuperada = repuesto_repo.get_by_consulta_id(consulta.id)
    assert recuperada == disponibilidad


def test_postgres_reemplaza_disponibilidad_existente(repository_pair):
    consulta_repo, repuesto_repo = repository_pair

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
    repuesto_repo.save(disponibilidad_inicial)

    disponibilidad_actualizada = DisponibilidadRepuesto.crear(
        consulta_id=consulta.id,
        estado="disponible",
    )
    repuesto_repo.save(disponibilidad_actualizada)

    recuperada = repuesto_repo.get_by_consulta_id(consulta.id)
    assert recuperada == disponibilidad_actualizada


def test_postgres_disponibilidad_repuesto_repository_close(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn)
    repo = _PostgresDisponibilidadRepuestoRepository(conn)
    repo.close()
