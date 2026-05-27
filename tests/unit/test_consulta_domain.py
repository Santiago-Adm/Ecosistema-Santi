from datetime import timezone

import pytest

from ecosistema_santi.domain.consulta import ConsultaAtencion, es_activa


def test_crear_consulta_valida():
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="mantenimiento_preventivo",
        descripcion="la moto vibra al acelerar",
    )

    assert consulta.id
    assert consulta.estado == "pendiente"
    assert consulta.creada_en.tzinfo == timezone.utc
    assert es_activa(consulta.estado) is True


@pytest.mark.parametrize(
    "conductor_id",
    ["", "   ", None],
)
def test_crear_consulta_sin_conductor(conductor_id):
    with pytest.raises(ValueError, match="conductor_id es obligatorio"):
        ConsultaAtencion.crear(
            conductor_id=conductor_id,
            motivo="mantenimiento_preventivo",
            descripcion="ruido en el motor",
        )


def test_crear_consulta_motivo_invalido():
    with pytest.raises(ValueError, match="motivo no permitido"):
        ConsultaAtencion.crear(
            conductor_id="conductor-1",
            motivo="otro",
            descripcion="ruido en el motor",
        )


@pytest.mark.parametrize(
    "descripcion",
    ["", "   ", None],
)
def test_crear_consulta_descripcion_vacia(descripcion):
    with pytest.raises(ValueError, match="descripcion es obligatorio"):
        ConsultaAtencion.crear(
            conductor_id="conductor-1",
            motivo="repuesto",
            descripcion=descripcion,
        )


def test_es_activa_con_estado_invalido():
    with pytest.raises(ValueError, match="estado no permitido"):
        es_activa("estado_inexistente")
