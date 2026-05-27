# Índice maestro del repositorio

## Propósito del documento

Este documento actúa como punto central de orientación para el trabajo asistido por CLI dentro del repositorio. Su finalidad es indicar a la CLI y al operador humano qué documentos existen, cuál es su función, en qué estado se encuentran, en qué orden deben consultarse y desde qué punto debe retomarse el trabajo cuando una sesión haya sido interrumpida o cerrada parcialmente.

El índice maestro no es solo una tabla de contenido. También cumple función operativa de continuidad, trazabilidad y control de foco, permitiendo que cada nueva sesión parta desde un estado documental explícito y no desde supuestos implícitos o memoria incompleta.

## Ubicación oficial del índice maestro

Ruta oficial del documento:
`/home/san/Proyectos/ecosistema-santi/Docs/00-indice-maestro-repositorio.md`

Este archivo es el punto de entrada documental del proyecto y debe ser la primera referencia para cualquier sesión CLI o revisión humana del repositorio.

## Convenciones de escritura y referencias

Dentro de este repositorio se utilizará Markdown como formato principal de documentación. Cuando sea útil para la navegación entre notas, se podrán usar referencias tipo Obsidian mediante enlaces internos `[[...]]`, siempre que el archivo destino exista y la extensión de VS Code lo soporte correctamente.

Estas referencias deberán usarse con criterio, como ayuda de navegación y continuidad, no como sustituto de la estructura formal del índice maestro.

## Estructura actual del directorio Docs

- `00-indice-maestro-repositorio.md`
- `01-gobierno-metodologico.md`
- `02-contexto-problema.md`
- `03-requisitos-y-alcance.md`
- `04-diseno-y-arquitectura.md`
- `05-estrategia-pruebas-y-trazabilidad.md`
- `07-retrospectiva-metodologica.md`
- `08-evidencia-construccion-autonoma.md`

## Función operativa del índice maestro

Dentro de este proyecto, la CLI deberá utilizar este documento como primer punto de entrada antes de iniciar cualquier tarea relevante. Su uso busca reducir ambigüedad, evitar relecturas innecesarias, impedir expansión de alcance y facilitar la reanudación ordenada del trabajo.

Por tanto, el índice maestro deberá servir para:

- ubicar rápidamente el documento rector según el tipo de tarea;
- identificar qué artefactos ya están cerrados y cuáles siguen activos;
- conocer dependencias entre documentos;
- determinar qué checklist aplicar antes de continuar;
- y permitir retomar una sesión interrumpida desde el último estado válido registrado.

## Regla de uso para sesiones CLI

Antes de ejecutar análisis, diseño, implementación, corrección o validación, la CLI deberá revisar este índice maestro para determinar:

- cuál es la tarea actual;
- qué documento gobierna esa tarea;
- qué estado tiene el trabajo previo;
- qué contexto mínimo debe releerse;
- y qué validaciones son obligatorias antes de continuar.

Si una sesión anterior quedó incompleta, la CLI no deberá avanzar directamente desde el último mensaje disponible sin antes contrastar el estado documental indicado en este índice.

## Principio de continuidad por estado documentado

La continuidad del trabajo no deberá depender únicamente del historial conversacional o de la memoria contextual de la herramienta. Como criterio operativo, se considerará más confiable retomar una tarea desde estado documentado que desde inferencia contextual no verificada.

Por ello, cuando exista interrupción, cambio de sesión, cambio de operador o pérdida parcial de contexto, la CLI deberá volver a este índice maestro, identificar el último estado registrado y reconstruir el contexto mínimo necesario antes de continuar.

## Relación entre índice maestro y checklists

Los checklists del proyecto cumplen una función complementaria al índice maestro. Mientras el índice define dónde está cada cosa, en qué estado se encuentra y qué documento manda, los checklists permiten verificar qué debe leerse, validarse o confirmarse antes de continuar o cerrar una sesión.

En conjunto, índice maestro y checklists permiten:

- reingresar al repositorio sin reconstruir todo desde cero;
- retomar trabajo interrumpido con menor riesgo de desalineación;
- mantener foco en el alcance definido;
- y asegurar que el avance ocurra desde evidencia y estado explícito.

## Tabla maestra de documentos

El índice maestro deberá incluir una tabla central que permita identificar rápidamente qué documentos existen, cuál es su función y cuándo deben consultarse. Esta tabla servirá como mapa de navegación operativa para la CLI y para cualquier revisión humana posterior.

| Código | Archivo | Propósito principal | Cuándo consultarlo | Estado |
|--------|---------|---------------------|--------------------|--------|
| 00 | `00-indice-maestro-repositorio.md` | Punto de entrada, navegación, continuidad y reglas de relectura | Al iniciar cualquier sesión relevante | Activo |
| 01 | `01-gobierno-metodologico.md` | Define enfoque, límites, principios y marco del experimento | Antes de decisiones metodológicas o de alcance | Cerrado |
| 02 | `02-contexto-problema.md` | Explica problema, necesidad, motivación y contexto del proyecto | Antes de análisis funcional o de diseño | Cerrado |
| 03 | `03-requisitos-y-alcance.md` | Consolida requisitos, restricciones y límites del sistema | Antes de diseñar, implementar o validar | Cerrado |
| 04 | `04-diseno-y-arquitectura.md` | Define estructura técnica, componentes y decisiones de diseño | Antes de implementación técnica o refactor relevante | Cerrado |
| 05 | `05-estrategia-pruebas-y-trazabilidad.md` | Establece enfoque de pruebas, cobertura y trazabilidad ligera | Antes de crear pruebas o validar cambios | Cerrado |
| 07 | `07-retrospectiva-metodologica.md` | Evalúa si la metodología aplicada fue realmente útil o no | Al cierre de hitos, iteraciones o experimento | Cerrado |
| 08 | `08-evidencia-construccion-autonoma.md` | Evidencia técnica y metodológica de construcción autónoma | Al cierre del experimento o auditoría de ejecución | Activo |

La tabla deberá mantenerse actualizada si se agregan nuevos documentos rectores. Si un archivo cambia de propósito, estado o dependencia, el índice maestro deberá reflejarlo expresamente.

## Estados posibles de un documento

Para evitar ambigüedad, cada documento del proyecto deberá tener un estado visible dentro del índice maestro. Esto permite que la CLI no asuma que un archivo está listo solo porque existe.

Se utilizarán, como mínimo, los siguientes estados:

- borrador: documento iniciado pero todavía inestable;
- en revisión: documento casi completo, pendiente de ajuste o validación;
- activo: documento vigente y utilizable como referencia operativa;
- cerrado: documento terminado y aceptado como base;
- y sustituido: documento reemplazado por otra versión o por otro artefacto.

La CLI deberá interpretar estos estados de la siguiente forma:

- si el documento está en borrador, no debe tratarlo como fuente final;
- si está en revisión, puede usarlo con cautela y señalando incertidumbre;
- si está activo o cerrado, puede usarlo como referencia principal;
- y si está sustituido, deberá consultar el artefacto que lo reemplaza.

## Orden de lectura según tipo de tarea

La CLI no deberá releer todos los documentos en cada sesión. En su lugar, deberá seguir un orden de lectura mínimo según el tipo de tarea a realizar.

### Para análisis

- `00-indice-maestro-repositorio.md`
- `01-gobierno-metodologico.md`
- `02-contexto-problema.md`
- `03-requisitos-y-alcance.md`

### Para diseño

- `00-indice-maestro-repositorio.md`
- `03-requisitos-y-alcance.md`
- `04-diseno-y-arquitectura.md`
- `05-estrategia-pruebas-y-trazabilidad.md` cuando aplique

### Para implementación

- `00-indice-maestro-repositorio.md`
- `03-requisitos-y-alcance.md`
- `04-diseno-y-arquitectura.md`
- `05-estrategia-pruebas-y-trazabilidad.md`

### Para pruebas o validación

- `00-indice-maestro-repositorio.md`
- `03-requisitos-y-alcance.md`
- `05-estrategia-pruebas-y-trazabilidad.md`

### Para retrospectiva o ajuste metodológico

- `00-indice-maestro-repositorio.md`
- `01-gobierno-metodologico.md`
- `07-retrospectiva-metodologica.md`

Este orden de lectura busca equilibrio entre continuidad y eficiencia. La CLI deberá releer lo necesario para no perder foco, pero sin reconstruir todo el repositorio si la tarea exige solo un subconjunto claro de contexto.

## Checklist de reentrada tras interrupción

Cuando una sesión CLI haya sido interrumpida, suspendida o continuada en otro momento, no deberá retomarse la tarea directamente desde el último mensaje conversacional sin verificación previa. Antes de continuar, la CLI deberá aplicar el siguiente checklist de reentrada:

- identificar la tarea exacta que estaba en curso;
- confirmar el último resultado tangible producido;
- verificar si el documento o módulo asociado quedó cerrado, parcial o pendiente;
- releer el índice maestro;
- releer los documentos mínimos según el tipo de tarea;
- identificar supuestos pendientes o incertidumbres abiertas;
- comprobar si existe validación pendiente;
- confirmar el siguiente paso permitido dentro del alcance;
- y solo entonces continuar la ejecución.

Si alguno de estos puntos no puede confirmarse, la CLI deberá detener avance y reconstruir primero el contexto mínimo necesario.

## Regla de no continuidad ciega

Como principio del proyecto, la CLI no deberá continuar una tarea solo porque “parece claro” dónde se quedó. Siempre que exista interrupción relevante, cambio de sesión o riesgo de desalineación, deberá preferirse una reentrada controlada basada en documentos y checklist antes que una continuación por inferencia débil.

Esta regla busca reducir errores acumulativos, desvíos de alcance y repeticiones innecesarias. También ayuda a que el proyecto siga siendo mantenible incluso si la continuidad no depende de una sola sesión o de un único operador.

## Checklist de cierre por sesión

Al terminar una sesión relevante, la CLI deberá dejar suficiente rastro para que una reentrada futura no dependa de memoria implícita. Como mínimo, deberá verificarse lo siguiente:

- objetivo de la sesión indicado de forma explícita;
- resultado tangible identificado;
- archivos o documentos afectados reconocibles;
- estado final de la tarea indicado;
- validación aplicada o pendiente registrada;
- siguiente paso sugerido dentro del alcance;
- y advertencias o bloqueos señalados si existen.

Cuanto mejor quede registrado este cierre, menos costosa será la reentrada posterior.

## Inicialización operativa del proyecto

Una vez creado este índice maestro, la CLI deberá considerarlo el punto de inicio estándar para cualquier sesión futura del proyecto. Su lectura deberá preceder tareas de análisis, diseño, implementación, validación, corrección o continuidad tras interrupción.

Con ello, el repositorio pasa a contar con un mecanismo explícito de orientación, reingreso y control de foco, reduciendo la dependencia de contexto conversacional disperso y mejorando la continuidad operativa del experimento.