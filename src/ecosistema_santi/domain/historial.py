from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ConsultaResumen:
    id: str
    motivo: str
    estado: str
    creada_en: datetime
    es_activa: bool
