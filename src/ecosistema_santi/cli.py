from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from .container import construir_servicios, resolver_db_path
from .domain.consulta import ConsultaAtencion
from .domain.disponibilidad_atencion import DisponibilidadAtencion
from .domain.disponibilidad_repuesto import DisponibilidadRepuesto
from .domain.historial import ConsultaResumen
from .domain.respuesta_operativa import RespuestaOperativa


def _isoformat(fecha: datetime) -> str:
    return fecha.isoformat()


def _serializar_consulta(consulta: ConsultaAtencion) -> dict[str, Any]:
    return {
        "id": consulta.id,
        "conductor_id": consulta.conductor_id,
        "motivo": consulta.motivo,
        "descripcion": consulta.descripcion,
        "estado": consulta.estado,
        "creada_en": _isoformat(consulta.creada_en),
    }


def _serializar_resumen(resumen: ConsultaResumen) -> dict[str, Any]:
    return {
        "id": resumen.id,
        "motivo": resumen.motivo,
        "estado": resumen.estado,
        "creada_en": _isoformat(resumen.creada_en),
        "es_activa": resumen.es_activa,
    }


def _serializar_disponibilidad(
    disponibilidad: DisponibilidadAtencion | DisponibilidadRepuesto,
) -> dict[str, Any]:
    return {
        "consulta_id": disponibilidad.consulta_id,
        "estado": disponibilidad.estado,
        "actualizado_en": _isoformat(disponibilidad.actualizado_en),
    }


def _serializar_respuesta(respuesta: RespuestaOperativa) -> dict[str, Any]:
    return {
        "consulta_id": respuesta.consulta_id,
        "estado_general": respuesta.estado_general,
        "observacion": respuesta.observacion,
        "costo_estimado": respuesta.costo_estimado,
        "actualizado_en": _isoformat(respuesta.actualizado_en),
    }


def _imprimir_salida(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def _crear_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ecosistema-santi")
    parser.add_argument(
        "--db",
        default=str(Path("data") / "consultas.db"),
        help="Ruta a la base de datos SQLite (por defecto: data/consultas.db)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    crear = subparsers.add_parser("crear-consulta")
    crear.add_argument("--conductor-id", required=True)
    crear.add_argument(
        "--motivo",
        required=True,
        choices=["mantenimiento_preventivo", "reparacion_correctiva", "repuesto"],
    )
    crear.add_argument("--descripcion", required=True)

    obtener = subparsers.add_parser("obtener-consulta")
    obtener.add_argument("--consulta-id", required=True)

    subparsers.add_parser("listar-consultas")

    atencion = subparsers.add_parser("registrar-atencion")
    atencion.add_argument("--consulta-id", required=True)
    atencion.add_argument(
        "--estado",
        required=True,
        choices=["disponible", "no_disponible", "pendiente_confirmacion"],
    )

    repuesto = subparsers.add_parser("registrar-repuesto")
    repuesto.add_argument("--consulta-id", required=True)
    repuesto.add_argument(
        "--estado",
        required=True,
        choices=["disponible", "no_disponible", "pendiente_confirmacion"],
    )

    respuesta = subparsers.add_parser("registrar-respuesta")
    respuesta.add_argument("--consulta-id", required=True)
    respuesta.add_argument("--estado-general", required=True)
    respuesta.add_argument("--observacion", required=True)
    respuesta.add_argument("--costo-estimado", type=float, required=False)

    obtener_atencion = subparsers.add_parser("obtener-atencion")
    obtener_atencion.add_argument("--consulta-id", required=True)

    obtener_repuesto = subparsers.add_parser("obtener-repuesto")
    obtener_repuesto.add_argument("--consulta-id", required=True)

    obtener_respuesta = subparsers.add_parser("obtener-respuesta")
    obtener_respuesta.add_argument("--consulta-id", required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _crear_parser()
    args = parser.parse_args(argv)
    db_path = resolver_db_path(args.db)
    servicios = construir_servicios(db_path)
    try:
        if args.command == "crear-consulta":
            consulta = servicios.consulta_service.registrar_consulta(
                conductor_id=args.conductor_id,
                motivo=args.motivo,
                descripcion=args.descripcion,
            )
            _imprimir_salida(_serializar_consulta(consulta))
            return 0

        if args.command == "obtener-consulta":
            consulta = servicios.consulta_repo.get_by_id(args.consulta_id)
            if consulta is None:
                raise ValueError("consulta inexistente")
            _imprimir_salida(_serializar_consulta(consulta))
            return 0

        if args.command == "listar-consultas":
            historial = servicios.historial_service.obtener_historial()
            _imprimir_salida([_serializar_resumen(item) for item in historial])
            return 0

        if args.command == "registrar-atencion":
            disponibilidad = servicios.atencion_service.registrar_disponibilidad(
                consulta_id=args.consulta_id,
                estado=args.estado,
            )
            _imprimir_salida(_serializar_disponibilidad(disponibilidad))
            return 0

        if args.command == "registrar-repuesto":
            disponibilidad = servicios.repuesto_service.registrar_disponibilidad(
                consulta_id=args.consulta_id,
                estado=args.estado,
            )
            _imprimir_salida(_serializar_disponibilidad(disponibilidad))
            return 0

        if args.command == "registrar-respuesta":
            respuesta = servicios.respuesta_service.registrar_respuesta(
                consulta_id=args.consulta_id,
                estado_general=args.estado_general,
                observacion=args.observacion,
                costo_estimado=args.costo_estimado,
            )
            _imprimir_salida(_serializar_respuesta(respuesta))
            return 0

        if args.command == "obtener-atencion":
            disponibilidad = servicios.atencion_service.obtener_disponibilidad(
                args.consulta_id
            )
            _imprimir_salida(_serializar_disponibilidad(disponibilidad))
            return 0

        if args.command == "obtener-repuesto":
            disponibilidad = servicios.repuesto_service.obtener_disponibilidad(
                args.consulta_id
            )
            _imprimir_salida(_serializar_disponibilidad(disponibilidad))
            return 0

        if args.command == "obtener-respuesta":
            respuesta = servicios.respuesta_service.obtener_respuesta(args.consulta_id)
            payload = (
                _serializar_respuesta(respuesta)
                if respuesta is not None
                else None
            )
            _imprimir_salida({"consulta_id": args.consulta_id, "respuesta": payload})
            return 0

        parser.error("comando no soportado")
    except ValueError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1
    finally:
        servicios.close()


if __name__ == "__main__":
    raise SystemExit(main())
