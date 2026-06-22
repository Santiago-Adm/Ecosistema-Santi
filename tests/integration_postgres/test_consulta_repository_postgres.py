import uuid

import pytest
from testcontainers.postgres import PostgresContainer

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.persistence.postgres_connection import (
    create_connection,
    ensure_schema,
)
from tests.integration_postgres.postgres_repos import _PostgresConsultaRepository


@pytest.fixture(scope="module")
def postgres_container():
    with PostgresContainer("postgres:16-alpine") as postgres:
        yield postgres


@pytest.fixture(scope="function")
def consulta_repository(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn)
    # Truncate tables to ensure isolation between tests
    with conn.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE consultas CASCADE;")
    conn.commit()
    repo = _PostgresConsultaRepository(conn)
    yield repo
    conn.close()


def test_save_and_get_by_id_consulta_atencion(consulta_repository):
    conductor_id = "cond-123"
    motivo = "repuesto"
    descripcion = "El motor hace un ruido extraño."
    consulta = ConsultaAtencion.crear(conductor_id, motivo, descripcion)

    saved_consulta = consulta_repository.save(consulta)
    assert saved_consulta == consulta

    retrieved_consulta = consulta_repository.get_by_id(consulta.id)
    assert retrieved_consulta == consulta


def test_update_estado_consulta_atencion(consulta_repository):
    conductor_id = "cond-456"
    motivo = "mantenimiento_preventivo"
    descripcion = "Necesita cambio de aceite."
    consulta = ConsultaAtencion.crear(conductor_id, motivo, descripcion)
    consulta_repository.save(consulta)

    nuevo_estado = "en_revision"
    updated_consulta = consulta_repository.update_estado(consulta.id, nuevo_estado)

    assert updated_consulta is not None
    assert updated_consulta.id == consulta.id
    assert updated_consulta.estado == nuevo_estado
    assert consulta_repository.get_by_id(consulta.id).estado == nuevo_estado


def test_list_all_consultas_atencion(consulta_repository):
    assert len(consulta_repository.list_all()) == 0

    consulta1 = ConsultaAtencion.crear("cond-A", "repuesto", "Falta el filtro.")
    consulta2 = ConsultaAtencion.crear(
        "cond-B", "mantenimiento_preventivo", "Checkup anual."
    )
    consulta3 = ConsultaAtencion.crear(
        "cond-C", "reparacion_correctiva", "Frenos chirrían."
    )

    consulta_repository.save(consulta1)
    consulta_repository.save(consulta2)
    consulta_repository.save(consulta3)

    all_consultas = consulta_repository.list_all()
    assert len(all_consultas) == 3
    assert consulta1 in all_consultas
    assert consulta2 in all_consultas
    assert consulta3 in all_consultas


def test_get_by_id_returns_none_if_not_found(consulta_repository):
    non_existent_id = str(uuid.uuid4())
    retrieved_consulta = consulta_repository.get_by_id(non_existent_id)
    assert retrieved_consulta is None


def test_update_estado_returns_none_if_not_found(consulta_repository):
    non_existent_id = str(uuid.uuid4())
    updated_consulta = consulta_repository.update_estado(non_existent_id, "confirmada")
    assert updated_consulta is None


def test_postgres_consulta_repository_close(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn)
    repo = _PostgresConsultaRepository(conn)
    repo.close()
