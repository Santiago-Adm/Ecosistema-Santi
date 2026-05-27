"""
Configuración de logging estructurado para Ecosistema Santi.

Provee un formatter JSON y una función get_logger() para que
los servicios críticos emitan trazas en formato estructurado.
"""

from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone
from typing import Any


class _JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        extra_keys = {
            k: v
            for k, v in record.__dict__.items()
            if k not in {
                "name", "msg", "args", "levelname", "levelno", "pathname",
                "filename", "module", "exc_info", "exc_text", "stack_info",
                "lineno", "funcName", "created", "msecs", "relativeCreated",
                "thread", "threadName", "processName", "process", "message",
                "taskName",
            }
        }
        if extra_keys:
            payload.update(extra_keys)
        return json.dumps(payload, ensure_ascii=False, default=str)


def _configurar_handler_si_no_existe(logger: logging.Logger) -> None:
    if not logger.handlers and not logging.root.handlers:
        handler = logging.StreamHandler(sys.stderr)
        handler.setFormatter(_JSONFormatter())
        logger.addHandler(handler)
        logger.propagate = False


def get_logger(nombre: str) -> logging.Logger:
    logger = logging.getLogger(f"ecosistema_santi.{nombre}")
    logger.setLevel(logging.INFO)
    _configurar_handler_si_no_existe(logger)
    return logger
