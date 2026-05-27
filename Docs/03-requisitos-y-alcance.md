# Definición funcional

## Propósito del documento

Este documento define el comportamiento esperado del sistema a partir del problema y del contexto previamente analizados. Su finalidad es traducir la necesidad observada en requisitos funcionales y no funcionales, historias de usuario, criterios de aceptación y casos de uso críticos cuando corresponda.

Este archivo pertenece a la capa de definición funcional y actúa como puente entre el análisis del problema y el diseño del sistema. No contiene todavía decisiones detalladas de arquitectura o implementación, pero sí establece qué debe hacer el sistema y bajo qué condiciones debe considerarse correcto.

## Alcance de esta capa documental

La presente capa se enfoca en describir el sistema desde el punto de vista del valor esperado, del comportamiento observable y de las condiciones mínimas necesarias para validar que dicho comportamiento responde al problema identificado.

Su alcance incluye:

- requisitos funcionales;
- requisitos no funcionales;
- historias de usuario;
- criterios de aceptación;
- casos de uso críticos cuando sean necesarios para reducir ambigüedad.

Quedan fuera de esta capa las decisiones de arquitectura, stack, estructura de módulos, patrones de diseño, definición técnica detallada de base de datos y aspectos internos de implementación.

## Principios de definición funcional

Toda definición funcional dentro de este proyecto debe cumplir los siguientes principios:

- Debe estar trazada al problema identificado en el análisis.
- Debe expresar valor o comportamiento verificable.
- Debe evitar ambigüedad, formulaciones vagas o deseos no medibles.
- Debe ser suficientemente clara como para permitir diseño, pruebas y validación posterior.
- Debe mantenerse dentro del alcance explícito del experimento.
- Debe priorizar lo necesario para validar la hipótesis principal del proyecto antes de ampliar el sistema.

## Relación entre requisitos, historias y criterios de aceptación

En este proyecto, los requisitos funcionales expresan capacidades o comportamientos que el sistema debe ofrecer. Las historias de usuario traducen esas capacidades a una perspectiva orientada al actor y al valor esperado. Los criterios de aceptación definen las condiciones observables que deben cumplirse para considerar correcta una historia o una funcionalidad.

La relación entre estos elementos será la siguiente:

- El requisito define qué comportamiento necesita existir.
- La historia de usuario expresa quién necesita ese comportamiento y para qué.
- El criterio de aceptación establece cómo confirmar que el comportamiento fue satisfecho.
- El caso de uso crítico se utilizará solo cuando una historia o requisito necesite una narrativa operativa más detallada para reducir ambigüedad.

## Regla de uso de casos de uso

Los casos de uso no serán obligatorios para todas las funcionalidades. Solo se documentarán en situaciones donde existan múltiples actores, decisiones críticas, pasos sensibles o riesgo alto de interpretación errónea.

En este proyecto, la regla general será trabajar principalmente con requisitos, historias de usuario y criterios de aceptación. Los casos de uso se incorporarán únicamente cuando aporten claridad real al flujo funcional y no como formalidad documental.

## Actores funcionales del sistema

Para esta primera etapa del proyecto se identifican los siguientes actores funcionales principales:

### 1. Conductor de mototaxi

Es el actor principal del sistema. Representa al usuario que necesita conocer información previa a una reparación, mantenimiento o compra de repuestos para tomar decisiones con menor incertidumbre y menor pérdida operativa.

### 2. Mecánico o personal del taller

Es el actor responsable de confirmar disponibilidad de atención, evaluar necesidades de reparación, validar piezas requeridas y actualizar el estado general del servicio cuando corresponda.

### 3. Responsable de tienda o repuestos

Es el actor encargado de consultar, confirmar o actualizar la disponibilidad de repuestos, así como de aportar información básica sobre stock, compatibilidad o costo estimado cuando el flujo lo requiera.

### 4. Sistema

Se considera como actor operativo interno en tanto coordina información, registra solicitudes, presenta estados y facilita la interacción entre conductor, taller y tienda sin reemplazar completamente la validación humana.

## Objetivos funcionales del sistema

El sistema deberá orientarse a cumplir los siguientes objetivos funcionales iniciales:

- Permitir al conductor conocer información relevante antes de desplazarse.
- Reducir incertidumbre respecto a disponibilidad de repuestos y atención.
- Facilitar una coordinación mínima entre conductor, taller y tienda.
- Registrar solicitudes o consultas necesarias para el flujo principal.
- Presentar estados claros que ayuden a decidir si conviene acudir, esperar o continuar con el proceso.
- Mantener un flujo suficientemente simple como para ser validado en entorno local y probado de forma robusta.

## Requisitos funcionales iniciales

A continuación se definen los requisitos funcionales iniciales del sistema para esta primera etapa del experimento.

### RF-01 — Registrar consulta de atención

El sistema debe permitir que el conductor registre una consulta o solicitud inicial relacionada con mantenimiento, reparación o necesidad de repuesto.

### RF-02 — Identificar necesidad principal

El sistema debe permitir que la consulta indique el motivo principal de atención, por ejemplo mantenimiento preventivo, falla mecánica o necesidad de repuesto.

### RF-03 — Permitir descripción libre del problema

El sistema debe permitir que el conductor describa en texto libre el problema observado cuando no conozca con precisión el nombre técnico del repuesto o de la falla.

### RF-04 — Permitir apoyo de referencia visual o descriptiva

El sistema debe contemplar un mecanismo básico para adjuntar o registrar referencias útiles para identificar mejor la necesidad, como una descripción ampliada, nombre aproximado o evidencia visual en una etapa posterior compatible con el alcance del experimento.

### RF-05 — Consultar disponibilidad de atención

El sistema debe permitir registrar o mostrar si existe disponibilidad inicial del mecánico o del taller para atender la solicitud.

### RF-06 — Consultar disponibilidad de repuesto

El sistema debe permitir registrar o mostrar si el repuesto requerido está disponible, no disponible o pendiente de confirmación.

### RF-07 — Mostrar estado de la consulta

El sistema debe mostrar un estado claro para cada solicitud o consulta realizada, de forma que el conductor pueda entender si está pendiente, en revisión, confirmada, parcialmente confirmada o no disponible.

### RF-08 — Registrar respuesta del taller o tienda

El sistema debe permitir que el personal correspondiente actualice la respuesta de la consulta con información relevante para la decisión del conductor.

### RF-09 — Mostrar costo estimado inicial

Cuando exista información suficiente, el sistema debe permitir registrar o mostrar un costo estimado inicial de atención o repuesto.

### RF-10 — Mantener historial básico de consultas

El sistema debe conservar un historial básico de las consultas realizadas para permitir seguimiento, revisión posterior o validación del flujo durante el experimento.

## Requisitos no funcionales iniciales

A continuación se definen los requisitos no funcionales iniciales que condicionan la calidad y viabilidad del sistema en esta primera etapa.

### RNF-01 — Ejecución local controlada

El sistema debe poder levantarse de forma local en un entorno de desarrollo controlado, compatible con la ejecución en laptop y flujo de trabajo por CLI.

### RNF-02 — Persistencia en base de datos SQL local

El sistema debe utilizar una base de datos SQL local para almacenar la información mínima necesaria del experimento, permitiendo validación funcional real y pruebas reproducibles.

### RNF-03 — Alta cobertura de pruebas en backend

Los módulos críticos del backend deben alcanzar una cobertura objetivo entre 90% y 95%, especialmente en reglas de negocio, servicios y flujos principales de validación.

### RNF-04 — Soporte para pruebas unitarias y de integración

La solución debe estar diseñada de manera que facilite pruebas unitarias con mocks cuando corresponda y pruebas de integración contra una base de datos local o un entorno controlado.

### RNF-05 — Claridad de estados y respuestas

El sistema debe manejar estados funcionales y respuestas comprensibles para evitar ambigüedad tanto en pruebas como en uso real del flujo.

### RNF-06 — Mantenibilidad documental y técnica

La solución debe poder evolucionar sin depender de contexto implícito excesivo. La documentación viva y la estructura funcional deben permitir comprender el sistema y continuar su desarrollo sin reconstruir desde cero todas las decisiones previas.

### RNF-07 — Restricción de complejidad inicial

La solución no debe incorporar complejidad técnica innecesaria, dependencias externas críticas o integraciones de alto costo operativo en esta primera etapa del experimento.

### RNF-08 — Trazabilidad ligera

Cada requisito funcional crítico debe poder relacionarse con al menos una historia de usuario, criterios de aceptación y pruebas asociadas en etapas posteriores del proyecto.

## Historias de usuario iniciales

A partir de los requisitos funcionales definidos, se establecen las siguientes historias de usuario iniciales para esta primera etapa del experimento.

### HU-01 — Registrar una consulta inicial

Como conductor de mototaxi, quiero registrar una consulta sobre mantenimiento, reparación o necesidad de repuesto, para iniciar el proceso sin depender únicamente de una llamada o visita presencial.

#### Criterios de aceptación

- El sistema debe permitir crear una consulta nueva.
- La consulta debe quedar asociada a un motivo principal de atención.
- La consulta debe registrar una fecha u orden temporal básico.
- La consulta creada debe quedar visible en el historial del usuario o del flujo correspondiente.
- Si la información mínima obligatoria no está completa, la consulta no debe registrarse como válida.

### HU-02 — Describir el problema en lenguaje simple

Como conductor de mototaxi, quiero describir el problema en mis propios términos, para poder solicitar ayuda aunque no conozca el nombre técnico del repuesto o de la falla.

#### Criterios de aceptación

- El sistema debe permitir una descripción libre del problema.
- La historia debe aceptar lenguaje no técnico o incompleto sin bloquear el registro inicial.
- La descripción debe poder ser consultada posteriormente por el taller o la tienda.
- El sistema no debe exigir conocimiento técnico como requisito para continuar con el flujo inicial.

### HU-03 — Conocer si existe disponibilidad de atención

Como conductor de mototaxi, quiero saber si el taller o el mecánico pueden atender mi solicitud, para decidir si me conviene desplazarme o esperar.

#### Criterios de aceptación

- El sistema debe permitir registrar o mostrar un estado de disponibilidad de atención.
- La disponibilidad debe poder reflejar al menos los estados disponible, no disponible o pendiente de confirmación.
- El conductor debe poder visualizar ese estado de forma clara.
- Si todavía no existe respuesta, el sistema debe mostrar que la consulta sigue pendiente.

### HU-04 — Conocer si el repuesto está disponible

Como conductor de mototaxi, quiero saber si el repuesto necesario está disponible, para evitar desplazamientos o compras fallidas.

#### Criterios de aceptación

- El sistema debe permitir registrar o mostrar disponibilidad de repuesto.
- La disponibilidad debe permitir al menos los estados disponible, no disponible o pendiente de confirmación.
- El conductor debe poder distinguir claramente entre disponibilidad confirmada y disponibilidad todavía no validada.
- La ausencia de confirmación no debe mostrarse como confirmación positiva.

### HU-05 — Recibir una respuesta útil para decidir

Como conductor de mototaxi, quiero recibir una respuesta clara sobre mi consulta, para decidir si acudir, esperar, continuar o buscar otra alternativa.

#### Criterios de aceptación

- El sistema debe permitir actualizar la consulta con una respuesta del taller o tienda.
- La respuesta debe poder incluir estado general, observación y costo estimado cuando exista.
- El conductor debe visualizar la última respuesta disponible asociada a su consulta.
- Si no existe costo estimado, el sistema no debe inventar ni mostrar valores ambiguos.

### HU-06 — Consultar el estado de mi solicitud

Como conductor de mototaxi, quiero revisar el estado de mi consulta, para saber en qué punto del proceso se encuentra.

#### Criterios de aceptación

- Cada consulta debe tener un estado visible.
- El estado debe pertenecer a un conjunto limitado y comprensible de valores.
- Los cambios de estado deben reflejar una transición coherente del flujo.
- El sistema no debe mostrar estados contradictorios para la misma consulta.

### HU-07 — Revisar historial básico de consultas

Como conductor de mototaxi, quiero revisar mis consultas anteriores, para recordar qué pedí, qué me respondieron y cómo evolucionó cada caso.

#### Criterios de aceptación

- El sistema debe conservar un historial básico de consultas registradas.
- Cada elemento del historial debe permitir identificar al menos motivo, estado y referencia temporal básica.
- El historial debe incluir también consultas aún no resueltas.
- El sistema debe diferenciar entre consultas activas y consultas cerradas si esa distinción es aplicada en el flujo.

## Criterios generales de aceptación de la capa funcional

Además de los criterios específicos por historia, toda funcionalidad de esta etapa debe cumplir con los siguientes criterios generales:

- Debe responder de forma directa al problema principal identificado en la capa de análisis.
- Debe poder ser validada mediante pruebas observables.
- Debe evitar dependencias innecesarias de integraciones externas en esta primera etapa.
- Debe mantener trazabilidad con al menos un requisito funcional.
- Debe poder incorporarse al flujo de pruebas del backend en etapas posteriores.

## Casos de uso críticos seleccionados

En esta etapa no se documentarán casos de uso para todas las historias. Sin embargo, se identifican como críticos los siguientes flujos potenciales para documentación posterior si se requiere mayor precisión:

- consulta inicial con disponibilidad pendiente;
- consulta con repuesto no identificado con precisión;
- consulta con disponibilidad parcial de atención y stock;
- consulta respondida con costo estimado;
- consulta sin confirmación suficiente para recomendar desplazamiento.

Estos casos se consideran candidatos prioritarios para formalización posterior si durante el diseño o las pruebas se detecta ambigüedad funcional relevante.

## Priorización funcional inicial con criterio MoSCoW

La priorización funcional del experimento se define mediante el criterio MoSCoW, con el fin de proteger el alcance inicial, evitar crecimiento prematuro y concentrar el desarrollo en aquello que realmente valida la hipótesis principal del proyecto.

### MUST

Las siguientes capacidades se consideran obligatorias para que el experimento tenga sentido en esta primera etapa:

- Registrar una consulta inicial.
- Permitir descripción libre del problema.
- Consultar o registrar disponibilidad de atención.
- Consultar o registrar disponibilidad de repuesto.
- Mostrar el estado de la consulta.
- Permitir respuesta útil por parte del taller o tienda.
- Mantener persistencia básica en base de datos SQL local.
- Permitir pruebas robustas sobre backend.

Si una de estas capacidades no está presente, la iteración no debe considerarse válida para la hipótesis principal del proyecto.

### SHOULD

Las siguientes capacidades son importantes pero no bloquean la validación principal si se difieren de forma justificada:

- Mostrar costo estimado inicial cuando exista información suficiente.
- Mantener historial básico de consultas.
- Distinguir con mayor precisión tipos de mantenimiento o atención.
- Mejorar la calidad de validación sobre flujos parcialmente confirmados.

### COULD

Las siguientes capacidades podrían aportar valor adicional, pero no forman parte del núcleo mínimo del experimento:

- Adjuntar referencia visual real dentro del flujo.
- Incorporar filtros o búsqueda en historial.
- Añadir clasificaciones más detalladas de fallas o repuestos.
- Mejorar visualización de estados en frontend más allá de lo estrictamente funcional.

### WON'T

Las siguientes capacidades quedan explícitamente fuera de esta primera etapa:

- Integraciones reales con WhatsApp u otros canales externos.
- Automatización de llamadas o notificaciones avanzadas.
- Catálogo completo de repuestos con cobertura amplia del negocio.
- Experiencias frontend complejas no necesarias para validar el flujo principal.
- Expansión a procesos administrativos, financieros o comerciales ajenos al problema principal.

## Regla de trazabilidad funcional

Toda funcionalidad crítica debe mantener una relación explícita con el análisis previo y con la validación posterior. Para este proyecto, la trazabilidad funcional mínima seguirá la siguiente lógica:

- problema identificado en `01-contexto-proyecto.md`;
- requisito funcional o no funcional en `02-definicion-funcional.md`;
- historia de usuario asociada;
- criterio de aceptación correspondiente;
- prueba o evidencia documentada en etapas posteriores.

La trazabilidad de esta etapa será ligera y práctica. No se busca construir una matriz pesada, sino asegurar que cada funcionalidad importante tenga origen claro, propósito definido y posibilidad real de validación.

## Definition of Done funcional

Una funcionalidad de esta etapa solo podrá considerarse terminada cuando cumpla, como mínimo, las siguientes condiciones:

- Tiene origen identificable en el problema o necesidad analizada.
- Está asociada a un requisito funcional o no funcional claro.
- Tiene historia de usuario definida.
- Posee criterios de aceptación verificables.
- Puede ser diseñada sin ambigüedad crítica.
- Puede ser incorporada al plan de pruebas posterior.
- No contradice el alcance inicial ni introduce complejidad innecesaria para el experimento.

Cumplir únicamente con la redacción de una historia no es suficiente para considerar terminada una funcionalidad. El cierre funcional exige coherencia entre necesidad, definición y posibilidad de validación.

## Criterio de transición hacia el diseño del sistema

El proyecto podrá avanzar desde la definición funcional hacia la capa de diseño del sistema cuando se considere que el comportamiento principal esperado ya está suficientemente delimitado, priorizado y expresado con claridad verificable.

La transición será válida si se cumplen al menos las siguientes condiciones:

- Existe una base funcional coherente con el problema analizado.
- Las funcionalidades MUST están identificadas y delimitadas.
- Los requisitos no funcionales principales están visibles.
- Las historias clave cuentan con criterios de aceptación utilizables.
- La ambigüedad restante no impide diseñar la estructura del sistema.

En ese punto, el archivo `03-diseno-sistema.md` podrá construirse como respuesta estructural a esta definición funcional, sin necesidad de redefinir nuevamente el problema o el alcance principal del experimento.

## Cierre de la capa funcional

Con la información registrada en este documento, el proyecto cuenta con una definición funcional inicial suficiente para continuar. Se dispone de actores identificados, objetivos funcionales, requisitos funcionales y no funcionales, historias de usuario iniciales, criterios de aceptación y una priorización explícita del alcance.

En consecuencia, se considera razonable cerrar esta capa documental y utilizar este archivo como contrato funcional base para la elaboración del diseño del sistema y la estrategia posterior de validación.