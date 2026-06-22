import pytest
from testcontainers.postgres import PostgresContainer

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.respuesta_operativa import RespuestaOperativa
from ecosistema_santi.persistence.postgres_connection import create_connection, ensure_schema
from tests.integration_postgres.postgres_repos import (
    _PostgresConsultaRepository,
    _PostgresRespuestaOperativaRepository,
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
    respuesta_repo = _PostgresRespuestaOperativaRepository(conn)
    yield consulta_repo, respuesta_repo
    conn.close()


def test_postgres_persistencia_respuesta_operativa(repository_pair):
    consulta_repo, respuesta_repo = repository_pair

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


def test_postgres_reemplaza_respuesta_existente(repository_pair):
    consulta_repo, respuesta_repo = repository_pair

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


def test_postgres_respuesta_operativa_repository_close(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn)
    repo = _PostgresRespuestaOperativaRepository(conn)
    repo.close()
