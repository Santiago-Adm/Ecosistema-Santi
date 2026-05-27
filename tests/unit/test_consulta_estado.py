import pytest

from ecosistema_santi.domain.consulta import calcular_estado


def test_estado_pendiente_sin_disponibilidad_ni_respuesta():
    assert calcular_estado(None, None, False) == "pendiente"


def test_estado_en_revision_con_respuesta_sin_disponibilidad():
    assert calcular_estado(None, None, True) == "en_revision"


def test_estado_confirmada_parcial_por_atencion_disponible():
    assert (
        calcular_estado("disponible", "pendiente_confirmacion", False)
        == "confirmada_parcial"
    )


def test_estado_confirmada_parcial_por_repuesto_disponible():
    assert calcular_estado("pendiente_confirmacion", "disponible", True) == "confirmada_parcial"


def test_estado_confirmada_con_ambas_disponibilidades():
    assert calcular_estado("disponible", "disponible", False) == "confirmada"


def test_estado_no_resuelta_si_alguna_no_disponible():
    assert calcular_estado("no_disponible", "pendiente_confirmacion", True) == "no_resuelta"
    assert calcular_estado("pendiente_confirmacion", "no_disponible", False) == "no_resuelta"


def test_estado_valida_disponibilidad():
    with pytest.raises(ValueError, match="disponibilidad_atencion no permitido"):
        calcular_estado("otro", None, False)
