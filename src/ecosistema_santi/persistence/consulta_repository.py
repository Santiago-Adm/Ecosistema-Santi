from __future__ import annotations

from datetime import datetime

from ..domain.consulta import ConsultaAtencion
from .sqlite import create_connection, ensure_schema


class SQLiteConsultaRepository:
    def __init__(self, db_path: str) -> None:
        self._conn = create_connection(db_path)
        ensure_schema(self._conn)

    def save(self, consulta: ConsultaAtencion) -> ConsultaAtencion:
        self._conn.execute(
            """
            INSERT INTO consultas (
                id, conductor_id, motivo, descripcion, estado, creada_en
            )
            VALUES (?, ?, ?, ?, ?, ?)
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
        row = self._conn.execute(
            """
            SELECT id, conductor_id, motivo, descripcion, estado, creada_en
            FROM consultas
            WHERE id = ?
            """,
            (consulta_id,),
        ).fetchone()
        if row is None:
            return None
        return ConsultaAtencion(
            id=row["id"],
            conductor_id=row["conductor_id"],
            motivo=row["motivo"],
            descripcion=row["descripcion"],
            estado=row["estado"],
            creada_en=datetime.fromisoformat(row["creada_en"]),
        )

    def update_estado(self, consulta_id: str, estado: str) -> ConsultaAtencion | None:
        cursor = self._conn.execute(
            """
            UPDATE consultas
            SET estado = ?
            WHERE id = ?
            """,
            (estado, consulta_id),
        )
        self._conn.commit()
        if cursor.rowcount == 0:
            return None
        return self.get_by_id(consulta_id)

    def list_all(self) -> list[ConsultaAtencion]:
        rows = self._conn.execute(
            """
            SELECT id, conductor_id, motivo, descripcion, estado, creada_en
            FROM consultas
            """
        ).fetchall()
        return [
            ConsultaAtencion(
                id=row["id"],
                conductor_id=row["conductor_id"],
                motivo=row["motivo"],
                descripcion=row["descripcion"],
                estado=row["estado"],
                creada_en=datetime.fromisoformat(row["creada_en"]),
            )
            for row in rows
        ]

    def close(self) -> None:
        self._conn.close()
