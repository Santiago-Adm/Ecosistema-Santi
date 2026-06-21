import psycopg2
from psycopg2.extensions import connection as PgConnection
from urllib.parse import urlparse

SCHEMA = """
CREATE TABLE IF NOT EXISTS consultas (
    id TEXT PRIMARY KEY,
    conductor_id TEXT NOT NULL,
    motivo TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    estado TEXT NOT NULL,
    creada_en TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS disponibilidad_atencion (
    consulta_id TEXT PRIMARY KEY,
    estado TEXT NOT NULL,
    actualizado_en TEXT NOT NULL,
    FOREIGN KEY (consulta_id) REFERENCES consultas(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS disponibilidad_repuesto (
    consulta_id TEXT PRIMARY KEY,
    estado TEXT NOT NULL,
    actualizado_en TEXT NOT NULL,
    FOREIGN KEY (consulta_id) REFERENCES consultas(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS respuestas_operativas (
    consulta_id TEXT PRIMARY KEY,
    estado_general TEXT NOT NULL,
    observacion TEXT NOT NULL,
    costo_estimado REAL,
    actualizado_en TEXT NOT NULL,
    FOREIGN KEY (consulta_id) REFERENCES consultas(id) ON DELETE CASCADE
);
"""


def create_connection(db_url: str) -> PgConnection:
    parsed_url = urlparse(db_url)
    conn = psycopg2.connect(
        host=parsed_url.hostname,
        port=parsed_url.port,
        user=parsed_url.username,
        password=parsed_url.password,
        dbname=parsed_url.path.lstrip("/"),
    )
    conn.autocommit = False # Usamos commits explícitos como en SQLite
    return conn


def ensure_schema(conn: PgConnection) -> None:
    with conn.cursor() as cursor:
        cursor.execute(SCHEMA)
    conn.commit()
