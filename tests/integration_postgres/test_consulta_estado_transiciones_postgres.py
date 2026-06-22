import pytest
from testcontainers.postgres import PostgresContainer

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.persistence.postgres_connection import create_connection, ensure_schema
from ecosistema_santi.services.consulta_estado_service import ConsultaEstadoService
from ecosistema_santi.services.disponibilidad_atencion_service import (
    DisponibilidadAtencionService,
)
from ecosistema_santi.services.disponibilidad_repuesto_service import (
    DisponibilidadRepuestoService,
)
from ecosistema_santi.services.respuesta_operativa_service import RespuestaOperativaService
from tests.integration_postgres.postgres_repos import (
    _PostgresConsultaRepository,
    _PostgresDisponibilidadAtencionRepository,
    _PostgresDisponibilidadRepuestoRepository,
    _PostgresRespuestaOperativaRepository,
)


@pytest.fixture(scope="module")
def postgres_container():
    with PostgresContainer("postgres:16-alpine") as postgres:
        yield postgres


@pytest.fixture(scope="function")
def servicios_postgres(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn)
    with conn.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE consultas CASCADE;")
    conn.commit()

    consulta_repo = _PostgresConsultaRepository(conn)
    atencion_repo = _PostgresDisponibilidadAtencionRepository(conn)
    repuesto_repo = _PostgresDisponibilidadRepuestoRepository(conn)
    respuesta_repo = _PostgresRespuestaOperativaRepository(conn)

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

    yield consulta_repo, atencion_service, repuesto_service, respuesta_service
    conn.close()


def test_transicion_en_revision_por_respuesta(servicios_postgres):
    consulta_repo, _, _, respuesta_service = servicios_postgres

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


def test_transicion_confirmada_parcial_por_atencion_disponible(servicios_postgres):
    consulta_repo, atencion_service, _, _ = servicios_postgres

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


def test_transicion_confirmada_con_ambas_disponibilidades(servicios_postgres):
    consulta_repo, atencion_service, repuesto_service, _ = servicios_postgres

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


def test_transicion_no_resuelta_por_no_disponible(servicios_postgres):
    consulta_repo, _, repuesto_service, _ = servicios_postgres

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
