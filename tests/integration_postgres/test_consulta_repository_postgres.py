import pytest
from testcontainers.postgres import PostgresContainer
import psycopg2
from psycopg2.extensions import connection as PgConnection

from datetime import datetime
import uuid

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.persistence.postgres_connection import create_connection, ensure_schema

# Definir un repositorio para las pruebas contra PostgreSQL
# Esto se mantiene dentro del ámbito de las pruebas y no afecta el código de producción.
class _PostgresConsultaRepository:
    def __init__(self, conn: PgConnection) -> None:
        self._conn = conn

    def save(self, consulta: ConsultaAtencion) -> ConsultaAtencion:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO consultas (
                    id, conductor_id, motivo, descripcion, estado, creada_en
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    consulta.id,
                    consulta.conductor_id,
                    consulta.motivo,
                    consulta.descripcion,
                    consulta.estado,
                    consulta.creada_en.isoformat(),
                ),
            )
        self._conn.commit()
        return consulta

    def get_by_id(self, consulta_id: str) -> ConsultaAtencion | None:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, conductor_id, motivo, descripcion, estado, creada_en
                FROM consultas
                WHERE id = %s
                """,
                (consulta_id,),
            )
            row = cursor.fetchone()
        if row is None:
            return None
        return ConsultaAtencion(
            id=row[0], # Acceder por índice ya que psycopg2 no retorna Row object por defecto
            conductor_id=row[1],
            motivo=row[2],
            descripcion=row[3],
            estado=row[4],
            creada_en=datetime.fromisoformat(row[5]),
        )

    def update_estado(self, consulta_id: str, estado: str) -> ConsultaAtencion | None:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE consultas
                SET estado = %s
                WHERE id = %s
                """,
                (estado, consulta_id),
            )
            self._conn.commit()
            if cursor.rowcount == 0:
                return None
        return self.get_by_id(consulta_id)

    def list_all(self) -> list[ConsultaAtencion]:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, conductor_id, motivo, descripcion, estado, creada_en
                FROM consultas
                """
            )
            rows = cursor.fetchall()
        return [
            ConsultaAtencion(
                id=row[0],
                conductor_id=row[1],
                motivo=row[2],
                descripcion=row[3],
                estado=row[4],
                creada_en=datetime.fromisoformat(row[5]),
            )
            for row in rows
        ]

    def close(self) -> None:
        self._conn.close()


@pytest.fixture(scope="module")
def postgres_container():
    with PostgresContainer("postgres:16-alpine") as postgres:
        yield postgres


@pytest.fixture(scope="function")
def consulta_repository(postgres_container):
    conn = create_connection(postgres_container.get_connection_url())
    ensure_schema(conn) # Asegurar el esquema para cada función de prueba
    repo = _PostgresConsultaRepository(conn)
    yield repo
    conn.close()


def test_save_and_get_by_id_consulta_atencion(consulta_repository):
    conductor_id = "cond-123"
    motivo = "problema_motor"
    descripcion = "El motor hace un ruido extraño."
    consulta = ConsultaAtencion.crear(conductor_id, motivo, descripcion)

    saved_consulta = consulta_repository.save(consulta)
    assert saved_consulta == consulta

    retrieved_consulta = consulta_repository.get_by_id(consulta.id)
    assert retrieved_consulta == consulta


def test_update_estado_consulta_atencion(consulta_repository):
    conductor_id = "cond-456"
    motivo = "cambio_aceite"
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
    # Asegurarse de que no haya consultas previas en esta sesión de prueba
    assert len(consulta_repository.list_all()) == 0

    consulta1 = ConsultaAtencion.crear("cond-A", "repuesto_faltante", "Falta el filtro.")
    consulta2 = ConsultaAtencion.crear("cond-B", "revision_general", "Checkup anual.")
    consulta3 = ConsultaAtencion.crear("cond-C", "problema_frenos", "Frenos chirrían.")

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
