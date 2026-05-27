from datetime import timezone

import pytest

from ecosistema_santi.domain.disponibilidad_atencion import DisponibilidadAtencion


def test_crear_disponibilidad_valida():
    disponibilidad = DisponibilidadAtencion.crear(
        consulta_id="consulta-1",
        estado="pendiente_confirmacion",
    )

    assert disponibilidad.consulta_id == "consulta-1"
    assert disponibilidad.estado == "pendiente_confirmacion"
    assert disponibilidad.actualizado_en.tzinfo == timezone.utc


@pytest.mark.parametrize(
    "consulta_id",
    ["", "   ", None],
)
def test_crear_disponibilidad_sin_consulta(consulta_id):
    with pytest.raises(ValueError, match="consulta_id es obligatorio"):
        DisponibilidadAtencion.crear(
            consulta_id=consulta_id,
            estado="disponible",
        )


def test_crear_disponibilidad_estado_invalido():
    with pytest.raises(ValueError, match="estado no permitido"):
        DisponibilidadAtencion.crear(
            consulta_id="consulta-1",
            estado="otro",
        )
