from __future__ import annotations

from datetime import datetime

from ..domain.disponibilidad_atencion import DisponibilidadAtencion
from .sqlite import create_connection, ensure_schema


class SQLiteDisponibilidadAtencionRepository:
    def __init__(self, db_path: str) -> None:
        self._conn = create_connection(db_path)
        ensure_schema(self._conn)

    def save(self, disponibilidad: DisponibilidadAtencion) -> DisponibilidadAtencion:
        self._conn.execute(
            """
            INSERT INTO disponibilidad_atencion (
                consulta_id, estado, actualizado_en
            )
            VALUES (?, ?, ?)
            ON CONFLICT(consulta_id) DO UPDATE SET
                estado = excluded.estado,
                actualizado_en = excluded.actualizado_en
            """,
            (
                disponibilidad.consulta_id,
                disponibilidad.estado,
                disponibilidad.actualizado_en.isoformat(),
            ),
        )
        self._conn.commit()
        return disponibilidad

    def get_by_consulta_id(self, consulta_id: str) -> DisponibilidadAtencion | None:
        row = self._conn.execute(
            """
            SELECT consulta_id, estado, actualizado_en
            FROM disponibilidad_atencion
            WHERE consulta_id = ?
            """,
            (consulta_id,),
        ).fetchone()
        if row is None:
            return None
        return DisponibilidadAtencion(
            consulta_id=row["consulta_id"],
            estado=row["estado"],
            actualizado_en=datetime.fromisoformat(row["actualizado_en"]),
        )

    def close(self) -> None:
        self._conn.close()
