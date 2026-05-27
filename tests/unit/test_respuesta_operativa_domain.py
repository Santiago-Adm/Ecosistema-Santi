from datetime import timezone

import pytest

from ecosistema_santi.domain.respuesta_operativa import RespuestaOperativa


def test_crear_respuesta_valida():
    respuesta = RespuestaOperativa.crear(
        consulta_id="consulta-1",
        estado_general="en revision",
        observacion="esperar confirmacion del mecanico",
        costo_estimado=120.5,
    )

    assert respuesta.consulta_id == "consulta-1"
    assert respuesta.estado_general == "en revision"
    assert respuesta.costo_estimado == 120.5
    assert respuesta.actualizado_en.tzinfo == timezone.utc


def test_crear_respuesta_sin_costo():
    respuesta = RespuestaOperativa.crear(
        consulta_id="consulta-1",
        estado_general="pendiente",
        observacion="aun sin confirmacion",
        costo_estimado=None,
    )

    assert respuesta.costo_estimado is None


@pytest.mark.parametrize("consulta_id", ["", "   ", None])
def test_crear_respuesta_sin_consulta(consulta_id):
    with pytest.raises(ValueError, match="consulta_id es obligatorio"):
        RespuestaOperativa.crear(
            consulta_id=consulta_id,
            estado_general="pendiente",
            observacion="aun sin confirmacion",
            costo_estimado=None,
        )


@pytest.mark.parametrize("estado_general", ["", "   ", None])
def test_crear_respuesta_sin_estado(estado_general):
    with pytest.raises(ValueError, match="estado_general es obligatorio"):
        RespuestaOperativa.crear(
            consulta_id="consulta-1",
            estado_general=estado_general,
            observacion="aun sin confirmacion",
            costo_estimado=None,
        )


@pytest.mark.parametrize("observacion", ["", "   ", None])
def test_crear_respuesta_sin_observacion(observacion):
    with pytest.raises(ValueError, match="observacion es obligatorio"):
        RespuestaOperativa.crear(
            consulta_id="consulta-1",
            estado_general="pendiente",
            observacion=observacion,
            costo_estimado=None,
        )


def test_crear_respuesta_costo_invalido():
    with pytest.raises(ValueError, match="costo_estimado inválido"):
        RespuestaOperativa.crear(
            consulta_id="consulta-1",
            estado_general="pendiente",
            observacion="aun sin confirmacion",
            costo_estimado="caro",
        )
