from __future__ import annotations

from datetime import datetime

from ..domain.respuesta_operativa import RespuestaOperativa
from .sqlite import create_connection, ensure_schema


class SQLiteRespuestaOperativaRepository:
    def __init__(self, db_path: str) -> None:
        self._conn = create_connection(db_path)
        ensure_schema(self._conn)

    def save(self, respuesta: RespuestaOperativa) -> RespuestaOperativa:
        self._conn.execute(
            """
            INSERT INTO respuestas_operativas (
                consulta_id, estado_general, observacion, costo_estimado, actualizado_en
            )
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(consulta_id) DO UPDATE SET
                estado_general = excluded.estado_general,
                observacion = excluded.observacion,
                costo_estimado = excluded.costo_estimado,
                actualizado_en = excluded.actualizado_en
            """,
            (
                respuesta.consulta_id,
                respuesta.estado_general,
                respuesta.observacion,
                respuesta.costo_estimado,
                respuesta.actualizado_en.isoformat(),
            ),
        )
        self._conn.commit()
        return respuesta

    def get_by_consulta_id(self, consulta_id: str) -> RespuestaOperativa | None:
        row = self._conn.execute(
            """
            SELECT consulta_id, estado_general, observacion, costo_estimado, actualizado_en
            FROM respuestas_operativas
            WHERE consulta_id = ?
            """,
            (consulta_id,),
        ).fetchone()
        if row is None:
            return None
        return RespuestaOperativa(
            consulta_id=row["consulta_id"],
            estado_general=row["estado_general"],
            observacion=row["observacion"],
            costo_estimado=row["costo_estimado"],
            actualizado_en=datetime.fromisoformat(row["actualizado_en"]),
        )

    def close(self) -> None:
        self._conn.close()
