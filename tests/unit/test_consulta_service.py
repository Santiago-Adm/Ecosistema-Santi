import pytest

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.services.consulta_service import ConsultaService


class FakeRepository:
    def __init__(self) -> None:
        self.saved = None

    def save(self, consulta: ConsultaAtencion) -> ConsultaAtencion:
        self.saved = consulta
        return consulta


def test_registrar_consulta_guarda_en_repositorio():
    repo = FakeRepository()
    service = ConsultaService(repo)

    consulta = service.registrar_consulta(
        conductor_id="conductor-1",
        motivo="reparacion_correctiva",
        descripcion="no enciende al girar la llave",
    )

    assert repo.saved == consulta
    assert consulta.conductor_id == "conductor-1"
    assert consulta.motivo == "reparacion_correctiva"


def test_registrar_consulta_valida_datos():
    repo = FakeRepository()
    service = ConsultaService(repo)

    with pytest.raises(ValueError):
        service.registrar_consulta(
            conductor_id="",
            motivo="repuesto",
            descripcion="falta espejo",
        )
