# Ecosistema Santi — Índice Maestro

**Estado actual:** `v0.3.0 — Arquitectura modular + seeds multi-nivel`
**Fecha:** 2026-05-25
**Fase:** Finish profesional — Modularización y enriquecimiento de datos

---

## Visión del sistema

Sistema digital que reduce la incertidumbre operativa del conductor de mototaxi antes de desplazarse, especialmente en relación con la disponibilidad de repuestos, la disponibilidad del mecánico y el tiempo estimado de atención. Permite registrar, consultar y seguir consultas de servicio desde CLI, servidor web o directamente via Python.

---

## Estado de módulos

| Módulo | Estado | Trazabilidad |
|--------|--------|--------------|
| Dominio (Consulta, Disponibilidades, Respuesta, Historial) | ✅ Completo y 100% cubierto | RF-01 a RF-10, HU-01 a HU-07 |
| Servicios de aplicación | ✅ Completo con logging estructurado | RF-05, RF-06, RF-07, RF-08 |
| Persistencia SQLite | ✅ Completa y 100% cubierta | RNF-02, SDD |
| Container (wiring compartido CLI+web) | ✅ Completo y 100% cubierto | Arquitectura |
| CLI (todos los comandos) | ✅ Completo | HU-01 a HU-07 |
| Web package modular (handler, ui/) | ✅ Completo | HU-01 a HU-07 |
| Tests unitarios (dominio + servicios + container) | ✅ 90 tests | RNF-03 |
| Tests integración (repositorios SQLite) | ✅ Completos | RNF-04 |
| Tests E2E web | ✅ 33 tests (flujos completos) | HU-01 a HU-07 |
| Seeds multi-nivel (base/demo/volumen) | ✅ 3 niveles: 5/25/55 escenarios | BDD |
| Logging estructurado JSON | ✅ En servicios críticos | Doc-04 |
| Cobertura backend | ✅ 98.90% (objetivo: 90-95%) | RNF-03 |
| Visualización 2D / 3D | 🔲 Backlog | HU-08, HU-10 |

---

## Estructura técnica real

```
ecosistema-santi/
├── INDICE_MAESTRO.md
├── Docs/
│   ├── 00-indice-maestro-repositorio.md
│   ├── 01-gobierno-metodologico.md
│   ├── 02-contexto-problema.md
│   ├── 03-requisitos-y-alcance.md
│   ├── 04-diseno-y-arquitectura.md
│   ├── 05-estrategia-pruebas-y-trazabilidad.md
│   ├── 06-guia-operativa-cli.md
│   ├── 07-retrospectiva-metodologica.md
│   └── 08-evidencia-construccion-autonoma.md
├── src/
│   └── ecosistema_santi/
│       ├── __init__.py
│       ├── __main__.py            ← entry point CLI: python -m ecosistema_santi
│       ├── cli.py                 ← CLI con 9 comandos (thin: usa container)
│       ├── container.py           ← Servicios dataclass + wiring (compartido CLI+web)
│       ├── logging_config.py      ← logging estructurado JSON
│       ├── domain/
│       │   ├── consulta.py
│       │   ├── disponibilidad_atencion.py
│       │   ├── disponibilidad_repuesto.py
│       │   ├── historial.py
│       │   └── respuesta_operativa.py
│       ├── persistence/
│       │   ├── sqlite.py
│       │   ├── consulta_repository.py
│       │   ├── disponibilidad_atencion_repository.py
│       │   ├── disponibilidad_repuesto_repository.py
│       │   └── respuesta_operativa_repository.py
│       ├── services/
│       │   ├── consulta_service.py
│       │   ├── consulta_estado_service.py
│       │   ├── disponibilidad_atencion_service.py
│       │   ├── disponibilidad_repuesto_service.py
│       │   ├── respuesta_operativa_service.py
│       │   └── historial_consultas_service.py
│       └── web/                   ← paquete web modular (antes: web.py monolítico 2038 líneas)
│           ├── __init__.py        ← re-exports públicos
│           ├── __main__.py        ← entry point: python -m ecosistema_santi.web
│           ├── app.py             ← run_server, main (argparse web)
│           ├── handler.py         ← _handler (HTTP routing, thin)
│           └── ui/                ← capa visual aislada
│               ├── __init__.py
│               ├── theme.py       ← CSS (design tokens) + JS
│               ├── icons.py       ← ico() — SVG inline sin dependencias
│               ├── formatters.py  ← escape, format_fecha, motivo_label, etc.
│               ├── layout.py      ← nav(), page() — estructura de página
│               ├── components.py  ← badge, kpi_card, barra_estados, timeline_estado, etc.
│               ├── forms.py       ← form_crear_consulta, form_disponibilidad, etc.
│               └── pages.py       ← render_dashboard, render_historial, render_detalle sub-renders
├── tests/
│   ├── unit/                      ← dominio + servicios + container (90 tests)
│   └── integration/               ← repositorios SQLite + web E2E (34 tests)
├── data/
│   ├── seed.py                    ← seed multi-nivel: --nivel base|demo|volumen
│   └── consultas.db
├── .coveragerc
├── pytest.ini
└── requirements.txt
```

---

## Stack técnico

| Capa | Tecnología |
|------|-----------|
| Runtime | Python 3.14, stdlib puro |
| Persistencia | SQLite via `sqlite3` (stdlib) |
| Servidor web | `http.server` (stdlib) |
| CLI | `argparse` (stdlib) |
| Tests | `pytest` + `pytest-cov` |
| Logging | `logging` stdlib + formatter JSON |

---

## Comandos de desarrollo

```bash
# Ejecutar suite completa con cobertura
python -m pytest tests/

# Poblar base de datos
python data/seed.py --reset                  # demo (25 escenarios, por defecto)
python data/seed.py --reset --nivel base     # 5 escenarios canónicos
python data/seed.py --reset --nivel volumen  # 55 escenarios para carga visual

# Iniciar servidor web
PYTHONPATH=src python -m ecosistema_santi.web --host 127.0.0.1 --port 8000

# CLI
PYTHONPATH=src python -m ecosistema_santi crear-consulta \
  --conductor-id conductor-1 --motivo repuesto \
  --descripcion "necesito pastilla de freno"
PYTHONPATH=src python -m ecosistema_santi listar-consultas
PYTHONPATH=src python -m ecosistema_santi registrar-atencion --consulta-id <id> --estado disponible
PYTHONPATH=src python -m ecosistema_santi registrar-repuesto  --consulta-id <id> --estado disponible
PYTHONPATH=src python -m ecosistema_santi registrar-respuesta \
  --consulta-id <id> --estado-general confirmado \
  --observacion "repuesto disponible" --costo-estimado 45.0

# Venv del proyecto
/home/san/.venv/ecosistema-santi/bin/python -m pytest tests/
```

---

## Métricas de calidad actuales

| Métrica | Valor | Objetivo |
|---------|-------|---------|
| Tests totales | 124 | — |
| Tests unitarios | 90 | — |
| Tests integración | 34 | — |
| Cobertura backend | 98.90% | 90-95% (RNF-03) |
| Tests fallando | 0 | 0 |

---

## Arquitectura de capas (v0.3.0)

```
                   ┌─────────────────────────────────────┐
                   │           Entrypoints                │
                   │   cli.py  /  web/__main__.py         │
                   └────────────┬────────────────────────┘
                                │ usa
                   ┌────────────▼────────────────────────┐
                   │         container.py                 │
                   │  Servicios + construir_servicios()   │
                   └────────────┬────────────────────────┘
                                │ instancia
              ┌─────────────────┼─────────────────┐
              │                 │                 │
    ┌─────────▼──────┐  ┌──────▼──────┐  ┌──────▼──────┐
    │   services/    │  │ persistence/│  │   domain/   │
    │  (reglas neg.) │  │  (SQLite)   │  │  (modelos)  │
    └────────────────┘  └─────────────┘  └─────────────┘

                   ┌─────────────────────────────────────┐
                   │          web/handler.py              │
                   │  HTTP routing — sin lógica de negocio│
                   └────────────┬────────────────────────┘
                                │ compone
                   ┌────────────▼────────────────────────┐
                   │           web/ui/                    │
                   │  theme · icons · formatters          │
                   │  layout · components · forms · pages │
                   └─────────────────────────────────────┘
```

---

## Seeds multi-nivel

| Nivel | Registros | Distribución | Uso |
|-------|-----------|--------------|-----|
| base | 5 | 1 por estado | Tests canónicos, demos mínimas |
| demo | 25 | 6P/4ER/3CP/7C/5NR | Dashboard, historial, filtros |
| volumen | 55 | 12P/8ER/6CP/18C/11NR | Carga visual completa, paginación |

---

## Brechas restantes (backlog)

1. Visualización 2D como grafo de relaciones (HU-08)
2. Dashboard estadístico con gráficos temporales
3. Capa 3D progresiva (HU-10 — solo cuando 2D esté cerrada)
4. Integración con canal externo (WhatsApp) — fuera del alcance actual

---

## Fuentes de verdad

1. Este índice maestro
2. `Docs/` — documentación viva y metodológica
3. `src/` — código fuente implementado
4. `tests/` — especificaciones ejecutables
5. `data/seed.py` — escenarios reales del dominio
