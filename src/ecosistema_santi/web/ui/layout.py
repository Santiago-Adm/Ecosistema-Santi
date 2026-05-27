from __future__ import annotations

from .formatters import escape
from .icons import ico
from .theme import CSS, JS


def nav(active_path: str) -> str:
    def _link(path: str, label: str, icon: str) -> str:
        cls = "active" if active_path == path else ""
        return (
            f"<a class='{cls}' href='{path}'>"
            f"{ico(icon, 16)}{escape(label)}"
            f"</a>"
        )
    return (
        "<nav class='site-nav'>"
        + _link("/", "Panel", "home")
        + _link("/consultas", "Consultas", "list")
        + _link("/consultas/nueva", "Nueva consulta", "plus")
        + "</nav>"
    )


def page(title: str, body: str, message: str | None = None, active_path: str = "/") -> str:
    alerta = ""
    if message:
        alerta = (
            f"<div class='alert alert-error'>"
            f"{ico('alert', 16)}"
            f"<span>{escape(message)}</span>"
            f"</div>"
        )
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} — Ecosistema Santi</title>
  <style>{CSS}</style>
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <a class="site-logo" href="/">
        <div class="logo-icon">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.5" stroke-linecap="round">
            <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
          </svg>
        </div>
        <div>
          <div class="site-name">Ecosistema Santi</div>
          <div class="site-tagline">Gestión de consultas mototaxi</div>
        </div>
      </a>
      {nav(active_path)}
      <div class="header-status">
        <div class="status-dot"></div>
        Sistema activo
      </div>
    </div>
  </header>
  <div class="page-wrap">
    {alerta}
    {body}
  </div>
  <script>{JS}</script>
</body>
</html>"""
