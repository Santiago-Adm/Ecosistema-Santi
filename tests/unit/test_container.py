"""Tests para el módulo container (wiring compartido)."""

import tempfile
from pathlib import Path

from ecosistema_santi.container import construir_servicios, resolver_db_path


def test_resolver_db_path_memory():
    assert resolver_db_path(":memory:") == ":memory:"


def test_resolver_db_path_crea_directorio(tmp_path):
    db = str(tmp_path / "sub" / "test.db")
    resultado = resolver_db_path(db)
    assert resultado == db
    assert Path(db).parent.exists()


def test_construir_servicios_devuelve_servicios():
    with tempfile.TemporaryDirectory() as tmpdir:
        db_path = str(Path(tmpdir) / "test.db")
        servicios = construir_servicios(db_path)
        try:
            assert servicios.consulta_service is not None
            assert servicios.historial_service is not None
            assert servicios.atencion_service is not None
            assert servicios.repuesto_service is not None
            assert servicios.respuesta_service is not None
        finally:
            servicios.close()
