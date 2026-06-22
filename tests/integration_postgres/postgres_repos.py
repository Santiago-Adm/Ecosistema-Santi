from __future__ import annotations

from datetime import datetime
from psycopg2.extensions import connection as PgConnection

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.disponibilidad_atencion import DisponibilidadAtencion
from ecosistema_santi.domain.disponibilidad_repuesto import DisponibilidadRepuesto
from ecosistema_santi.domain.respuesta_operativa import RespuestaOperativa


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
            id=row[0],
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


class _PostgresDisponibilidadAtencionRepository:
    def __init__(self, conn: PgConnection) -> None:
        self._conn = conn

    def save(self, disponibilidad: DisponibilidadAtencion) -> DisponibilidadAtencion:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO disponibilidad_atencion (
                    consulta_id, estado, actualizado_en
                )
                VALUES (%s, %s, %s)
                ON CONFLICT(consulta_id) DO UPDATE SET
                    estado = EXCLUDED.estado,
                    actualizado_en = EXCLUDED.actualizado_en
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
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT consulta_id, estado, actualizado_en
                FROM disponibilidad_atencion
                WHERE consulta_id = %s
                """,
                (consulta_id,),
            )
            row = cursor.fetchone()
        if row is None:
            return None
        return DisponibilidadAtencion(
            consulta_id=row[0],
            estado=row[1],
            actualizado_en=datetime.fromisoformat(row[2]),
        )

    def close(self) -> None:
        self._conn.close()


class _PostgresDisponibilidadRepuestoRepository:
    def __init__(self, conn: PgConnection) -> None:
        self._conn = conn

    def save(self, disponibilidad: DisponibilidadRepuesto) -> DisponibilidadRepuesto:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO disponibilidad_repuesto (
                    consulta_id, estado, actualizado_en
                )
                VALUES (%s, %s, %s)
                ON CONFLICT(consulta_id) DO UPDATE SET
                    estado = EXCLUDED.estado,
                    actualizado_en = EXCLUDED.actualizado_en
                """,
                (
                    disponibilidad.consulta_id,
                    disponibilidad.estado,
                    disponibilidad.actualizado_en.isoformat(),
                ),
            )
        self._conn.commit()
        return disponibilidad

    def get_by_consulta_id(self, consulta_id: str) -> DisponibilidadRepuesto | None:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT consulta_id, estado, actualizado_en
                FROM disponibilidad_repuesto
                WHERE consulta_id = %s
                """,
                (consulta_id,),
            )
            row = cursor.fetchone()
        if row is None:
            return None
        return DisponibilidadRepuesto(
            consulta_id=row[0],
            estado=row[1],
            actualizado_en=datetime.fromisoformat(row[2]),
        )

    def close(self) -> None:
        self._conn.close()


class _PostgresRespuestaOperativaRepository:
    def __init__(self, conn: PgConnection) -> None:
        self._conn = conn

    def save(self, respuesta: RespuestaOperativa) -> RespuestaOperativa:
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO respuestas_operativas (
                    consulta_id, estado_general, observacion, costo_estimado, actualizado_en
                )
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT(consulta_id) DO UPDATE SET
                    estado_general = EXCLUDED.estado_general,
                    observacion = EXCLUDED.observacion,
                    costo_estimado = EXCLUDED.costo_estimado,
                    actualizado_en = EXCLUDED.actualizado_en
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
        with self._conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT consulta_id, estado_general, observacion, costo_estimado, actualizado_en
                FROM respuestas_operativas
                WHERE consulta_id = %s
                """,
                (consulta_id,),
            )
            row = cursor.fetchone()
        if row is None:
            return None
        return RespuestaOperativa(
            consulta_id=row[0],
            estado_general=row[1],
            observacion=row[2],
            costo_estimado=row[3],
            actualizado_en=datetime.fromisoformat(row[4]),
        )

    def close(self) -> None:
        self._conn.close()
