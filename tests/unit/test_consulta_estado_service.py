import pytest

from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.domain.disponibilidad_atencion import DisponibilidadAtencion
from ecosistema_santi.domain.disponibilidad_repuesto import DisponibilidadRepuesto
from ecosistema_santi.domain.respuesta_operativa import RespuestaOperativa
from ecosistema_santi.services.consulta_estado_service import ConsultaEstadoService


class FakeConsultaRepository:
    def __init__(self) -> None:
        self.items = {}

    def add(self, consulta: ConsultaAtencion) -> None:
        self.items[consulta.id] = consulta

    def get_by_id(self, consulta_id: str) -> ConsultaAtencion | None:
        return self.items.get(consulta_id)

    def update_estado(self, consulta_id: str, estado: str) -> ConsultaAtencion | None:
        consulta = self.items.get(consulta_id)
        if consulta is None:
            return None
        self.items[consulta_id] = ConsultaAtencion(
            id=consulta.id,
            conductor_id=consulta.conductor_id,
            motivo=consulta.motivo,
            descripcion=consulta.descripcion,
            estado=estado,
            creada_en=consulta.creada_en,
        )
        return self.items[consulta_id]


class FakeDisponibilidadAtencionRepository:
    def __init__(self) -> None:
        self.items = {}

    def set(self, disponibilidad: DisponibilidadAtencion) -> None:
        self.items[disponibilidad.consulta_id] = disponibilidad

    def get_by_consulta_id(self, consulta_id: str):
        return self.items.get(consulta_id)


class FakeDisponibilidadRepuestoRepository:
    def __init__(self) -> None:
        self.items = {}

    def set(self, disponibilidad: DisponibilidadRepuesto) -> None:
        self.items[disponibilidad.consulta_id] = disponibilidad

    def get_by_consulta_id(self, consulta_id: str):
        return self.items.get(consulta_id)


class FakeRespuestaOperativaRepository:
    def __init__(self) -> None:
        self.items = {}

    def set(self, respuesta: RespuestaOperativa) -> None:
        self.items[respuesta.consulta_id] = respuesta

    def get_by_consulta_id(self, consulta_id: str):
        return self.items.get(consulta_id)


def _crear_servicio(consulta: ConsultaAtencion):
    consulta_repo = FakeConsultaRepository()
    consulta_repo.add(consulta)
    atencion_repo = FakeDisponibilidadAtencionRepository()
    repuesto_repo = FakeDisponibilidadRepuestoRepository()
    respuesta_repo = FakeRespuestaOperativaRepository()
    service = ConsultaEstadoService(
        consulta_repo, atencion_repo, repuesto_repo, respuesta_repo
    )
    return service, consulta_repo, atencion_repo, repuesto_repo, respuesta_repo


def test_recalcular_estado_en_revision_por_respuesta():
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="repuesto",
        descripcion="necesito llanta delantera",
    )
    service, consulta_repo, _, _, respuesta_repo = _crear_servicio(consulta)

    respuesta_repo.set(
        RespuestaOperativa.crear(
            consulta_id=consulta.id,
            estado_general="pendiente",
            observacion="sin confirmacion",
            costo_estimado=None,
        )
    )

    estado = service.recalcular_estado(consulta.id)

    assert estado == "en_revision"
    assert consulta_repo.get_by_id(consulta.id).estado == "en_revision"


def test_recalcular_estado_confirmada_parcial():
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-2",
        motivo="mantenimiento_preventivo",
        descripcion="cambio de aceite",
    )
    service, consulta_repo, atencion_repo, repuesto_repo, _ = _crear_servicio(consulta)

    atencion_repo.set(
        DisponibilidadAtencion.crear(
            consulta_id=consulta.id,
            estado="disponible",
        )
    )
    repuesto_repo.set(
        DisponibilidadRepuesto.crear(
            consulta_id=consulta.id,
            estado="pendiente_confirmacion",
        )
    )

    estado = service.recalcular_estado(consulta.id)

    assert estado == "confirmada_parcial"
    assert consulta_repo.get_by_id(consulta.id).estado == "confirmada_parcial"


def test_recalcular_estado_confirmada():
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-3",
        motivo="repuesto",
        descripcion="necesito frenos",
    )
    service, consulta_repo, atencion_repo, repuesto_repo, _ = _crear_servicio(consulta)

    atencion_repo.set(
        DisponibilidadAtencion.crear(
            consulta_id=consulta.id,
            estado="disponible",
        )
    )
    repuesto_repo.set(
        DisponibilidadRepuesto.crear(
            consulta_id=consulta.id,
            estado="disponible",
        )
    )

    estado = service.recalcular_estado(consulta.id)

    assert estado == "confirmada"
    assert consulta_repo.get_by_id(consulta.id).estado == "confirmada"


def test_recalcular_estado_no_resuelta():
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-4",
        motivo="reparacion_correctiva",
        descripcion="no enciende",
    )
    service, consulta_repo, atencion_repo, repuesto_repo, _ = _crear_servicio(consulta)

    atencion_repo.set(
        DisponibilidadAtencion.crear(
            consulta_id=consulta.id,
            estado="no_disponible",
        )
    )
    repuesto_repo.set(
        DisponibilidadRepuesto.crear(
            consulta_id=consulta.id,
            estado="pendiente_confirmacion",
        )
    )

    estado = service.recalcular_estado(consulta.id)

    assert estado == "no_resuelta"
    assert consulta_repo.get_by_id(consulta.id).estado == "no_resuelta"


def test_recalcular_estado_exige_consulta_existente():
    consulta_repo = FakeConsultaRepository()
    atencion_repo = FakeDisponibilidadAtencionRepository()
    repuesto_repo = FakeDisponibilidadRepuestoRepository()
    respuesta_repo = FakeRespuestaOperativaRepository()
    service = ConsultaEstadoService(
        consulta_repo, atencion_repo, repuesto_repo, respuesta_repo
    )

    with pytest.raises(ValueError, match="consulta inexistente"):
        service.recalcular_estado("consulta-inexistente")


def test_recalcular_estado_falla_si_update_retorna_none():
    """Cubre la defensa cuando update_estado retorna None tras get_by_id exitoso."""

    class FakeConsultaRepositoryUpdateFallido(FakeConsultaRepository):
        def update_estado(self, consulta_id: str, estado: str) -> None:
            return None

    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-x",
        motivo="repuesto",
        descripcion="falla inesperada en update",
    )
    consulta_repo = FakeConsultaRepositoryUpdateFallido()
    consulta_repo.add(consulta)
    atencion_repo = FakeDisponibilidadAtencionRepository()
    repuesto_repo = FakeDisponibilidadRepuestoRepository()
    respuesta_repo = FakeRespuestaOperativaRepository()
    service = ConsultaEstadoService(
        consulta_repo, atencion_repo, repuesto_repo, respuesta_repo
    )

    with pytest.raises(ValueError, match="consulta inexistente"):
        service.recalcular_estado(consulta.id)
