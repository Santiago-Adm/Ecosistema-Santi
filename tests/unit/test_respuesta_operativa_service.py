import pytest

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.respuesta_operativa import RespuestaOperativa
from ecosistema_santi.services.respuesta_operativa_service import RespuestaOperativaService


class FakeRepository:
    def __init__(self) -> None:
        self.saved = None
        self.items = {}

    def save(self, respuesta: RespuestaOperativa) -> RespuestaOperativa:
        self.saved = respuesta
        self.items[respuesta.consulta_id] = respuesta
        return respuesta

    def get_by_consulta_id(self, consulta_id: str) -> RespuestaOperativa | None:
        return self.items.get(consulta_id)


class FakeConsultaRepository:
    def __init__(self) -> None:
        self.items = {}

    def add(self, consulta: ConsultaAtencion) -> None:
        self.items[consulta.id] = consulta

    def get_by_id(self, consulta_id: str) -> ConsultaAtencion | None:
        return self.items.get(consulta_id)


class FakeEstadoService:
    def __init__(self) -> None:
        self.calls = []

    def recalcular_estado(self, consulta_id: str) -> str:
        self.calls.append(consulta_id)
        return "pendiente"


def test_registrar_respuesta_guarda_en_repositorio():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="repuesto",
        descripcion="necesito llanta delantera",
    )
    consulta_repo.add(consulta)
    service = RespuestaOperativaService(repo, consulta_repo, estado_service)

    respuesta = service.registrar_respuesta(
        consulta_id=consulta.id,
        estado_general="en revision",
        observacion="revisando stock",
        costo_estimado=50.0,
    )

    assert repo.saved == respuesta
    assert respuesta.costo_estimado == 50.0
    assert estado_service.calls == [consulta.id]


def test_registrar_respuesta_exige_consulta_existente():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    service = RespuestaOperativaService(repo, consulta_repo, estado_service)

    with pytest.raises(ValueError, match="consulta inexistente"):
        service.registrar_respuesta(
            consulta_id="consulta-inexistente",
            estado_general="pendiente",
            observacion="sin datos",
            costo_estimado=None,
        )


def test_obtener_respuesta():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="mantenimiento_preventivo",
        descripcion="ruido en el motor",
    )
    consulta_repo.add(consulta)
    service = RespuestaOperativaService(repo, consulta_repo, estado_service)

    service.registrar_respuesta(
        consulta_id=consulta.id,
        estado_general="pendiente",
        observacion="a la espera del mecanico",
        costo_estimado=None,
    )

    encontrada = service.obtener_respuesta(consulta.id)
    assert encontrada is not None
    assert encontrada.estado_general == "pendiente"


def test_obtener_respuesta_exige_consulta_existente():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    service = RespuestaOperativaService(repo, consulta_repo, estado_service)

    with pytest.raises(ValueError, match="consulta inexistente"):
        service.obtener_respuesta("consulta-inexistente")
