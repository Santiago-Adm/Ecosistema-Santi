from __future__ import annotations

_PATHS: dict[str, str] = {
    "layers":    "M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5",
    "list":      "M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01",
    "plus":      "M12 5v14M5 12h14",
    "check":     "M20 6L9 17l-5-5",
    "x":         "M18 6L6 18M6 6l12 12",
    "clock":     "M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM12 6v6l4 2",
    "alert":     "M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0zM12 9v4M12 17h.01",
    "info":      "M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM12 16v-4M12 8h.01",
    "user":      "M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2M12 11a4 4 0 100-8 4 4 0 000 8z",
    "tool":      "M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z",
    "arrow-r":   "M5 12h14M12 5l7 7-7 7",
    "arrow-l":   "M19 12H5M12 19l-7-7 7-7",
    "copy":      "M8 17.929H6c-1.105 0-2-.912-2-2.036V5.036C4 3.91 4.895 3 6 3h8c1.105 0 2 .911 2 2.036v1.866m-6 .17h8c1.105 0 2 .91 2 2.035v10.857C20 21.09 19.105 22 18 22h-8c-1.105 0-2-.911-2-2.036V9.107c0-1.124.895-2.036 2-2.036z",
    "chevron-d": "M6 9l6 6 6-6",
    "chevron-u": "M18 15l-6-6-6 6",
    "wrench":    "M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z",
    "package":   "M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16zM3.27 6.96L12 12.01l8.73-5.05M12 22.08V12",
    "home":      "M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2zM9 22V12h6v10",
    "activity":  "M22 12h-4l-3 9L9 3l-3 9H2",
    "filter":    "M22 3H2l8 9.46V19l4 2v-8.54L22 3z",
    "search":    "M21 21l-4.35-4.35M17 11A6 6 0 115 11a6 6 0 0112 0z",
}


def ico(name: str, size: int = 18) -> str:
    s = str(size)
    d = _PATHS.get(name, "M12 12h.01")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" '
        f'viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
        f'style="display:inline-block;vertical-align:-3px;flex-shrink:0">'
        f'<path d="{d}"/></svg>'
    )
