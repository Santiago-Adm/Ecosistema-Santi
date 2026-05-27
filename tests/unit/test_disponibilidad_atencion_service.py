import pytest

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.disponibilidad_atencion import DisponibilidadAtencion
from ecosistema_santi.services.disponibilidad_atencion_service import (
    DisponibilidadAtencionService,
)


class FakeRepository:
    def __init__(self) -> None:
        self.saved = None
        self.items = {}

    def save(self, disponibilidad: DisponibilidadAtencion) -> DisponibilidadAtencion:
        self.saved = disponibilidad
        self.items[disponibilidad.consulta_id] = disponibilidad
        return disponibilidad

    def get_by_consulta_id(self, consulta_id: str) -> DisponibilidadAtencion | None:
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


def test_registrar_disponibilidad_guarda_en_repositorio():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="repuesto",
        descripcion="necesito llanta delantera",
    )
    consulta_repo.add(consulta)
    service = DisponibilidadAtencionService(repo, consulta_repo, estado_service)

    disponibilidad = service.registrar_disponibilidad(
        consulta_id=consulta.id,
        estado="disponible",
    )

    assert repo.saved == disponibilidad
    assert disponibilidad.estado == "disponible"
    assert estado_service.calls == [consulta.id]


def test_registrar_disponibilidad_valida_datos():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    service = DisponibilidadAtencionService(repo, consulta_repo, estado_service)

    with pytest.raises(ValueError):
        service.registrar_disponibilidad(
            consulta_id="",
            estado="disponible",
        )


def test_registrar_disponibilidad_exige_consulta_existente():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    service = DisponibilidadAtencionService(repo, consulta_repo, estado_service)

    with pytest.raises(ValueError, match="consulta inexistente"):
        service.registrar_disponibilidad(
            consulta_id="consulta-inexistente",
            estado="disponible",
        )


def test_obtener_disponibilidad():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="mantenimiento_preventivo",
        descripcion="ruido en el motor",
    )
    consulta_repo.add(consulta)
    service = DisponibilidadAtencionService(repo, consulta_repo, estado_service)

    service.registrar_disponibilidad(
        consulta_id=consulta.id,
        estado="pendiente_confirmacion",
    )

    encontrada = service.obtener_disponibilidad(consulta.id)
    assert encontrada is not None
    assert encontrada.estado == "pendiente_confirmacion"


def test_obtener_disponibilidad_pendiente_si_no_existe():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-2",
        motivo="reparacion_correctiva",
        descripcion="no enciende",
    )
    consulta_repo.add(consulta)
    service = DisponibilidadAtencionService(repo, consulta_repo, estado_service)

    disponible = service.obtener_disponibilidad(consulta.id)

    assert disponible.estado == "pendiente_confirmacion"


def test_obtener_disponibilidad_exige_consulta_existente():
    repo = FakeRepository()
    consulta_repo = FakeConsultaRepository()
    estado_service = FakeEstadoService()
    service = DisponibilidadAtencionService(repo, consulta_repo, estado_service)

    with pytest.raises(ValueError, match="consulta inexistente"):
        service.obtener_disponibilidad("consulta-inexistente")
