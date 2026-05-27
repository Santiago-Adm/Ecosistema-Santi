# Copilot Instructions

## Propósito del repositorio

Este repositorio corresponde al proyecto **Ecosistema Santi**.

La documentación del proyecto es una documentación viva y debe considerarse la fuente principal de verdad para orientar el análisis, diseño, implementación, validación y continuidad del trabajo.

## Punto de entrada obligatorio

Antes de iniciar cualquier tarea relevante, lee primero:

`Docs/00-indice-maestro-repositorio.md`

No empieces una tarea importante sin revisar antes ese archivo.

## Regla general de trabajo

Trabaja siempre con enfoque incremental, proceso por proceso, dentro del alcance solicitado.

No expandas funcionalidades por iniciativa propia.
No mezcles análisis, rediseño amplio, implementación completa y validación total en una sola sesión si no fue pedido explícitamente.

## Relectura mínima por tipo de tarea

Después de leer el índice maestro, relee solo el contexto mínimo necesario según el tipo de tarea:

- análisis: `Docs/01-gobierno-metodologico.md`, `Docs/02-contexto-problema.md`, `Docs/03-requisitos-y-alcance.md`
- diseño: `Docs/03-requisitos-y-alcance.md`, `Docs/04-diseno-y-arquitectura.md`
- implementación: `Docs/03-requisitos-y-alcance.md`, `Docs/04-diseno-y-arquitectura.md`, `Docs/05-estrategia-pruebas-y-trazabilidad.md`, `Docs/06-guia-operativa-cli.md`
- pruebas o validación: `Docs/03-requisitos-y-alcance.md`, `Docs/05-estrategia-pruebas-y-trazabilidad.md`, `Docs/06-guia-operativa-cli.md`
- retrospectiva o ajuste metodológico: `Docs/01-gobierno-metodologico.md`, `Docs/06-guia-operativa-cli.md`, `Docs/07-retrospectiva-metodologica.md`

## Regla de continuidad

No continúes una tarea por intuición ni solo por memoria conversacional.

Si hubo interrupción, error, cambio de sesión o pérdida parcial de contexto, vuelve al índice maestro y aplica el checklist de reentrada antes de continuar.

## Checklist de reentrada obligatorio

Antes de retomar trabajo interrumpido, verifica como mínimo:

- tarea exacta en curso;
- último resultado tangible producido;
- estado del archivo, módulo o proceso afectado;
- documentos mínimos que deben releerse;
- supuestos pendientes o incertidumbres abiertas;
- validación pendiente;
- siguiente paso permitido dentro del alcance.

Si no puedes confirmar estos puntos, no continúes todavía. Reconstruye primero el contexto mínimo necesario.

## Regla antes de modificar archivos

Antes de crear, editar o eliminar archivos, debes dejar explícito:

- objetivo concreto de la sesión;
- alcance de la modificación;
- archivos que serán revisados;
- resultado tangible esperado;
- validación mínima que aplicarás.

## Validación mínima

No des por terminado un cambio solo porque parece correcto.

Toda tarea debe cerrarse con validación proporcional al tipo de trabajo realizado:

- consistencia documental, si fue una tarea de documentación;
- coherencia con requisitos y arquitectura, si fue diseño o implementación;
- pruebas, cobertura o evidencia verificable, si fue una tarea técnica o funcional;
- registro de pendientes, si algo quedó parcial.

## Salida esperada al cierre de cada sesión

Al terminar una sesión, entrega una salida estructurada con:

- objetivo realizado;
- archivos afectados;
- resultado tangible producido;
- validación aplicada o pendiente;
- estado final de la tarea;
- siguiente paso recomendado;
- bloqueos, advertencias o riesgos si existen.

## Manejo de ambigüedad

Si detectas ambigüedad, contradicción documental, falta de contexto o riesgo de expansión de alcance, detén el avance y solicita o reconstruye primero el contexto mínimo necesario.

## Criterio permanente

Tu trabajo en este repositorio debe ser:

- trazable;
- incremental;
- verificable;
- reanudable;
- y alineado con la documentación viva del proyecto.
