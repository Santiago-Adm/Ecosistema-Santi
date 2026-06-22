import pytest
from testcontainers.postgres import PostgresContainer

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.disponibilidad_atencion import DisponibilidadAtencion
from ecosistema_santi.persistence.postgres_connection import create_connection, ensure_schema
from tests.integration_postgres.postgres_repos import (
    _PostgresConsultaRepository,
    _PostgresDisponibilidadAtencionRepository,
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
    atencion_repo = _PostgresDisponibilidadAtencionRepository(conn)
    yield consulta_repo, atencion_repo
    conn.close()


def test_postgres_persistencia_disponibilidad_atencion(repository_pair):
    consulta_repo, atencion_repo = repository_pair

    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="repuesto",
        descripcion="necesito llanta delantera",
    )
    consulta_repo.save(consulta)

    disponibilidad = DisponibilidadAtencion.crear(
        consulta_id=consulta.id,
        estado="no_disponible",
    )
    atencion_repo.save(disponibilidad)

    recuperada = atencion_repo.get_by_consulta_id(consulta.id)
    assert recuperada == disponibilidad


def test_postgres_reemplaza_disponibilidad_existente(repository_pair):
    consulta_repo, atencion_repo = repository_pair

    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-2",
        motivo="mantenimiento_preventivo",
        descripcion="cambio de aceite",
    )
    consulta_repo.save(consulta)

    disponibilidad_inicial = DisponibilidadAtencion.crear(
        consulta_id=consulta.id,
        estado="pendiente_confirmacion",
    )
    atencion_repo.save(disponibilidad_inicial)

    disponibilidad_actualizada = DisponibilidadAtencion.crear(
        consulta_id=consulta.id,
        estado="disponible",
    )
    atencion_repo.save(disponibilidad_actualizada)

    recuperada = atencion_repo.get_by_consulta_id(consulta.id)
    assert recuperada == disponibilidad_actualizada


def test_postgres_disponibilidad_atencion_repository_close(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn)
    repo = _PostgresDisponibilidadAtencionRepository(conn)
    repo.close()
