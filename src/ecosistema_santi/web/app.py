from __future__ import annotations

import argparse
import sys
from http.server import HTTPServer
from pathlib import Path

from ..container import construir_servicios, resolver_db_path
from .handler import handler


def run_server(host: str, port: int, db_path: str) -> None:
    resolved = resolver_db_path(db_path)
    services = construir_servicios(resolved)
    handler_class = handler(services)
    server = HTTPServer((host, port), handler_class)
    print(f"Servidor web en http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        services.close()
        server.server_close()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="ecosistema-santi-web")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    parser.add_argument(
        "--db",
        default=str(Path("data") / "consultas.db"),
        help="Ruta a la base de datos SQLite (por defecto: data/consultas.db)",
    )
    args = parser.parse_args(argv)
    try:
        run_server(args.host, args.port, args.db)
    except OSError as exc:
        print(f"Error al iniciar servidor: {exc}", file=sys.stderr)
        return 1
    return 0
