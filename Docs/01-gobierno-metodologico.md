# Gobierno metodologico del proyecto

## Propósito del documento

Este documento define los principios metodologicos y la estructura oficial de documentos vivos del proyecto. Su finalidad es establecer qué artefactos documentales existirán, qué función cumple cada uno, cuándo deben utilizarse y cómo se relacionan entre sí dentro del flujo de desarrollo.

Este archivo actúa como contrato metodologico base para el experimento de desarrollo orientado por CLI, con foco en velocidad, calidad y capacidad de levantar el sistema sin introducir documentación innecesaria o ambigua.

## Alcance

El alcance de este documento se limita a organizar la documentación viva del proyecto. No describe todavía el problema de negocio, los requisitos funcionales, la arquitectura del sistema ni la estrategia detallada de pruebas, sino la forma en que esos contenidos serán distribuidos y mantenidos en archivos separados y trazables.

Su función es servir como punto de referencia común para la creación, consulta, actualización y control de los documentos que acompañarán el ciclo de análisis, definición funcional, diseño, validación y retrospectiva del proyecto.

## Principio de documento vivo

Todos los documentos definidos en este proyecto se consideran documentos vivos. Esto significa que deben mantenerse actualizados conforme evolucionen las decisiones, restricciones, hipótesis, pruebas y resultados del desarrollo.

Un documento vivo no se redacta una sola vez para quedar congelado, sino que se corrige, amplía, reduce o reorganiza cuando el proyecto lo exige. Su valor no está en su extensión, sino en su vigencia, claridad y utilidad para orientar decisiones reales.

## Regla de crecimiento y separación

Cada archivo documental debe mantenerse lo suficientemente pequeño, claro y específico como para poder ser usado de forma efectiva por personas y herramientas CLI con asistencia de IA.

Mientras un documento conserve claridad, cohesión temática y facilidad de mantenimiento, permanecerá como un único archivo vivo. Si un documento crece hasta dificultar su lectura, actualización o uso operativo, podrá dividirse en secciones o artefactos derivados, siempre manteniendo trazabilidad explícita con el archivo original.

La separación de un documento no debe responder a preferencia estética, sino a necesidad operativa, reducción de ambigüedad o mejora de mantenibilidad documental.

## Principios rectores

La documentación de este proyecto debe ser breve, útil, actualizable y orientada a decisiones reales. Cada documento debe existir para ayudar a analizar, definir, diseñar, validar o controlar el desarrollo, no para acumular información sin uso operativo.

Toda sección incluida en este archivo debe responder a una necesidad concreta del proyecto. Si una parte no ayuda a construir, decidir, probar o comprender el sistema, no debe permanecer en el documento.

## Regla de uso por la CLI

La CLI debe utilizar este documento como referencia estructural y no como texto para reproducir de forma literal. Su función es definir qué documentos existen, qué rol cumple cada uno y cómo se relacionan entre sí.

Cuando una tarea requiera información específica, la CLI debe consultar únicamente el archivo vivo pertinente y, si es necesario, la sección concreta relacionada con la decisión actual. No debe asumirse que todo el documento maestro necesita ser leído en cada paso.

## Criterio de actualización

Cada documento vivo debe actualizarse cuando ocurra una decisión relevante, un cambio de alcance, una validación nueva o una corrección de criterio. El objetivo no es mantener versiones históricas extensas, sino conservar la versión actual más útil para el proyecto.

Cuando una sección pierda claridad, deje de ser suficiente o acumule demasiado contenido, debe reescribirse o separarse en un artefacto nuevo, manteniendo trazabilidad con el documento original.

## Regla de separación

Un bloque documental puede permanecer en un solo archivo mientras conserve cohesión temática, claridad y facilidad de mantenimiento. Si el bloque empieza a crecer hasta dificultar su lectura, actualización o uso por la CLI, puede dividirse en secciones o documentos derivados.

La separación debe hacerse solo por necesidad operativa, no por preferencia estética. El criterio principal será siempre la utilidad real del documento para avanzar con velocidad, calidad y capacidad de levantar el sistema.

## Taxonomía oficial de capas documentales

La documentación viva del proyecto se organiza en capas documentales con responsabilidades diferenciadas. Esta separación busca reducir ambigüedad, evitar mezcla de criterios y facilitar el uso progresivo de los artefactos durante el desarrollo.

Las capas oficiales del proyecto son las siguientes:

### 1. Capa de análisis

Esta capa contiene los artefactos que permiten comprender el problema, el contexto, los actores, el dolor principal, las hipótesis del experimento, las restricciones y los límites explícitos del alcance inicial.

Su propósito no es diseñar la solución técnica, sino definir con claridad qué problema existe, por qué vale la pena resolverlo y bajo qué condiciones se considera viable continuar.

### 2. Capa de definición funcional

Esta capa traduce el contexto y el problema en elementos funcionales verificables. Aquí se ubican los requisitos funcionales y no funcionales, las historias de usuario, los criterios de aceptación y los casos de uso críticos cuando sean necesarios para reducir ambigüedad.

Su propósito es conectar el problema identificado con el comportamiento esperado del sistema, sin entrar todavía en la implementación técnica detallada.

### 3. Capa de diseño del sistema

Esta capa describe cómo será estructurado el sistema para responder a las necesidades definidas. Aquí se ubican la arquitectura elegida, los patrones aplicables, la separación entre backend y frontend, la base de datos, los contratos entre capas, los módulos del sistema y las decisiones técnicas principales.

Su propósito es convertir la definición funcional en una estructura técnica coherente, mínima y suficiente para sostener el desarrollo.

### 4. Capa de validación y calidad

Esta capa define cómo será validado el sistema durante su construcción. Aquí se ubican el enfoque TDD-BDD, la estrategia de pruebas unitarias, el uso de mocks, la cobertura objetivo, las pruebas de integración y los criterios de calidad esperados para el backend y demás partes críticas del sistema.

Su propósito es asegurar que la construcción del sistema no dependa solo de implementación funcional, sino de evidencia verificable y repetible.

### 5. Capa de control y aprendizaje

Esta capa agrupa los artefactos orientados a trazabilidad ligera, control de avance, evaluación del experimento y aprendizaje retrospectivo. Aquí se ubican la matriz de trazabilidad documental y funcional, así como la retrospectiva de viabilidad del enfoque de desarrollo asistido por CLI.

Su propósito es permitir seguimiento, ajuste y validación del propio proceso de desarrollo, no solo del producto construido.

## Lista oficial de archivos vivos del proyecto

A partir de la taxonomía anterior, el proyecto define como base los siguientes archivos vivos:

- `00-indice-maestro-repositorio.md`
- `01-gobierno-metodologico.md`
- `02-contexto-problema.md`
- `03-requisitos-y-alcance.md`
- `04-diseno-y-arquitectura.md`
- `05-estrategia-pruebas-y-trazabilidad.md`
- `06-guia-operativa-cli.md`
- `07-retrospectiva-metodologica.md`
- `08-evidencia-construccion-autonoma.md`

## Relación entre capas y archivos

Cada archivo vivo pertenece principalmente a una capa documental, aunque puede mantener relación con artefactos de otras capas mediante referencias cruzadas o trazabilidad explícita.

La relación oficial inicial será la siguiente:

- `00-indice-maestro-repositorio.md` → marco documental y continuidad.
- `01-gobierno-metodologico.md` → marco metodologico.
- `02-contexto-problema.md` → capa de analisis.
- `03-requisitos-y-alcance.md` → capa de definicion funcional.
- `04-diseno-y-arquitectura.md` → capa de diseno del sistema.
- `05-estrategia-pruebas-y-trazabilidad.md` → capa de validacion y control.
- `06-guia-operativa-cli.md` → capa de operacion.
- `07-retrospectiva-metodologica.md` → capa de control y aprendizaje.
- `08-evidencia-construccion-autonoma.md` → evidencia de ejecucion.

Cada uno de estos archivos debe mantenerse como fuente viva de referencia para su propósito principal y podrá relacionarse con otros documentos únicamente cuando esa relación aporte claridad, control o reducción de ambigüedad.

## Tabla maestra de archivos vivos del proyecto

| Archivo vivo | Capa documental | Proposito principal | Contenido minimo esperado | Momento de uso por la CLI | Regla critica |
|---|---|---|---|---|---|
| `00-indice-maestro-repositorio.md` | Marco documental | Punto de entrada, navegacion y continuidad | proposito, estados, orden de lectura, checklist | Al iniciar cualquier sesion relevante | No sustituye documentos funcionales. |
| `01-gobierno-metodologico.md` | Marco metodologico | Principios, limites y reglas del experimento | objetivos, limites, reglas de uso | Antes de decisiones de alcance o metodologia | No redefine requisitos. |
| `02-contexto-problema.md` | Analisis | Definir el problema, el contexto y la viabilidad del experimento | contexto general, actor, dolor, hipotesis, limites, criterios de viabilidad | Antes del diseno y la definicion funcional | No introduce solucion tecnica. |
| `03-requisitos-y-alcance.md` | Definicion funcional | Consolidar requisitos y limites del sistema | requisitos funcionales y no funcionales, historias, criterios de aceptacion | Antes de disenar o implementar funcionalidades | Toda funcionalidad debe nacer aqui. |
| `04-diseno-y-arquitectura.md` | Diseno del sistema | Definir la estructura tecnica y decisiones clave | arquitectura, modulos, contratos, datos | Antes de implementacion tecnica | No cambia alcance funcional. |
| `05-estrategia-pruebas-y-trazabilidad.md` | Validacion y control | Estrategia de pruebas y trazabilidad ligera | niveles de prueba, cobertura, evidencias, trazabilidad | Antes y durante la implementacion | La validacion del backend es prioritaria. |
| `06-guia-operativa-cli.md` | Operacion | Guia de trabajo para CLI | flujo de sesion, reglas, validacion | Antes de ejecutar trabajo operativo | No define requisitos. |
| `07-retrospectiva-metodologica.md` | Control y aprendizaje | Evaluar la metodologia aplicada | hallazgos, fricciones, mejoras, decision de continuidad | Al cierre de hitos | No reescribe el alcance. |
| `08-evidencia-construccion-autonoma.md` | Evidencia | Evidencia tecnica y metodologica de ejecucion | resultados de pruebas, ejecucion, observaciones | Al cierre de entregables | Debe basarse en evidencia verificable. |