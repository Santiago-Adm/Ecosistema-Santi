from ecosistema_santi.domain.consulta import ConsultaAtencion
from ecosistema_santi.services.historial_consultas_service import HistorialConsultasService


class FakeConsultaRepository:
    def __init__(self, consultas):
        self._consultas = consultas

    def list_all(self):
        return list(self._consultas)


def test_obtener_historial_resumen():
    consulta = ConsultaAtencion.crear(
        conductor_id="conductor-1",
        motivo="repuesto",
        descripcion="necesito llanta delantera",
    )
    repo = FakeConsultaRepository([consulta])
    service = HistorialConsultasService(repo)

    historial = service.obtener_historial()

    assert len(historial) == 1
    assert historial[0].id == consulta.id
    assert historial[0].motivo == consulta.motivo
    assert historial[0].estado == consulta.estado
    assert historial[0].es_activa is True
