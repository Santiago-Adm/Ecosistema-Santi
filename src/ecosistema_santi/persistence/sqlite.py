import sqlite3

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


def create_connection(db_path: str) -> sqlite3.Connection:
    # check_same_thread=False permite usar la conexión desde el thread del servidor HTTP
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn


def ensure_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()
