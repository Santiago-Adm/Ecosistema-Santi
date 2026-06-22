"""Tests para el módulo de logging estructurado."""

import json
import logging

from ecosistema_santi.logging_config import _JSONFormatter, get_logger


def test_get_logger_retorna_logger():
    logger = get_logger("test_modulo")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "ecosistema_santi.test_modulo"


def test_get_logger_idempotente():
    logger_a = get_logger("mismo_nombre_x")
    logger_b = get_logger("mismo_nombre_x")
    assert logger_a is logger_b


def test_json_formatter_produce_json_valido():
    formatter = _JSONFormatter()
    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="",
        lineno=0,
        msg="evento_prueba",
        args=(),
        exc_info=None,
    )
    salida = formatter.format(record)
    datos = json.loads(salida)
    assert datos["level"] == "INFO"
    assert datos["msg"] == "evento_prueba"
    assert "ts" in datos
    assert "logger" in datos


def test_json_formatter_incluye_extra():
    formatter = _JSONFormatter()
    record = logging.LogRecord(
        name="test",
        level=logging.WARNING,
        pathname="",
        lineno=0,
        msg="alerta",
        args=(),
        exc_info=None,
    )
    record.consulta_id = "id-123"
    record.estado = "pendiente"
    salida = formatter.format(record)
    datos = json.loads(salida)
    assert datos["consulta_id"] == "id-123"
    assert datos["estado"] == "pendiente"


def test_json_formatter_nivel_warning():
    formatter = _JSONFormatter()
    record = logging.LogRecord(
        name="test",
        level=logging.WARNING,
        pathname="",
        lineno=0,
        msg="advertencia",
        args=(),
        exc_info=None,
    )
    salida = formatter.format(record)
    datos = json.loads(salida)
    assert datos["level"] == "WARNING"


def test_logger_captura_con_caplog(caplog):
    with caplog.at_level(logging.INFO, logger="ecosistema_santi.services.test_cap"):
        logger = get_logger("services.test_cap")
        logger.info("evento_capturado", extra={"clave": "valor"})
    assert any("evento_capturado" in r.message for r in caplog.records)


def test_json_formatter_incluye_excepcion():
    formatter = _JSONFormatter()
    try:
        raise ValueError("error de prueba")
    except ValueError:
        import sys

        exc_info = sys.exc_info()

    record = logging.LogRecord(
        name="test",
        level=logging.ERROR,
        pathname="",
        lineno=0,
        msg="error ocurrido",
        args=(),
        exc_info=exc_info,
    )
    salida = formatter.format(record)
    datos = json.loads(salida)
    assert datos["level"] == "ERROR"
    assert datos["msg"] == "error ocurrido"
    assert "exc" in datos
    assert "ValueError: error de prueba" in datos["exc"]


def test_configurar_handler_si_no_existe_crea_handler():
    old_root_handlers = list(logging.root.handlers)
    logging.root.handlers = []
    try:
        logger = get_logger("logger_sin_handlers_de_prueba")
        assert len(logger.handlers) == 1
        assert isinstance(logger.handlers[0], logging.StreamHandler)
        assert isinstance(logger.handlers[0].formatter, _JSONFormatter)
        assert logger.propagate is False
    finally:
        logging.root.handlers = old_root_handlers
