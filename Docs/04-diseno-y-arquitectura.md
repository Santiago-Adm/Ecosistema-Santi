# Diseño del sistema

## Propósito del documento

Este documento define la estructura del sistema propuesta para responder a la definición funcional previamente establecida. Su finalidad es describir cómo se organizará la solución en términos de arquitectura general, módulos principales, persistencia, contratos internos, responsabilidades técnicas y criterios de diseño necesarios para construir el experimento con claridad y control.

Este archivo pertenece a la capa de diseño del sistema y actúa como contrato técnico base para la implementación posterior. No redefine el problema de negocio ni la funcionalidad esperada, sino que traduce esa definición en una estructura técnica mínima, coherente y suficientemente robusta para ser construida y validada.

## Alcance de esta capa documental

La presente capa se enfoca en describir la solución desde una perspectiva estructural. Su alcance incluye la arquitectura general del sistema, la separación entre frontend y backend, la estrategia de persistencia local, la organización de módulos principales, las decisiones técnicas esenciales y las restricciones arquitectónicas que protegen el experimento.

Quedan fuera de esta capa la implementación concreta de clases, funciones o archivos finales, así como el detalle completo de pruebas automatizadas, pipelines de despliegue y procedimientos operativos específicos, los cuales serán tratados en documentos posteriores o en artefactos de ejecución.

## Principios rectores de diseño

El diseño del sistema en este proyecto deberá regirse por los siguientes principios:

- La arquitectura debe seguir al problema y no al deseo de complejidad.
- La solución debe ser tan simple como sea posible, pero suficientemente sólida para sostener pruebas, persistencia y evolución.
- El backend constituye el núcleo principal de validación del experimento.
- El frontend existirá como medio funcional de interacción, no como eje principal del valor técnico en esta etapa.
- Toda decisión de diseño debe poder justificarse por claridad, viabilidad local, mantenibilidad o necesidad de validación.
- La estructura propuesta debe facilitar alta cobertura de pruebas en los módulos críticos.
- La arquitectura debe poder levantarse localmente en un entorno controlado sin dependencias externas innecesarias.

## Criterio de arquitectura mínima viable

La arquitectura del experimento se define bajo el principio de mínima arquitectura viable. Esto implica construir solo la estructura técnica necesaria para sostener el flujo funcional prioritario, permitir validación robusta y evitar sobrediseño prematuro.

En este proyecto, una arquitectura se considerará mínima y viable si cumple simultáneamente las siguientes condiciones:

- permite ejecutar el sistema localmente;
- sostiene la persistencia funcional básica en base de datos SQL local;
- facilita separación clara de responsabilidades;
- permite pruebas unitarias y de integración con bajo acoplamiento;
- evita integraciones externas críticas en la primera etapa;
- y puede evolucionar sin necesidad de rehacer completamente la base técnica inicial.

## Relación con la definición funcional

Toda decisión estructural descrita en este documento debe responder a necesidades ya registradas en `02-definicion-funcional.md`. La arquitectura no debe introducir funcionalidades nuevas por iniciativa propia ni ampliar el alcance sin justificación explícita.

El diseño del sistema existe para soportar las funcionalidades priorizadas, los requisitos no funcionales críticos y la estrategia de validación posterior. Por ello, la arquitectura se considerará correcta solo si mantiene coherencia con el alcance, las prioridades y los límites ya definidos en capas anteriores.

## Visión arquitectónica general

La solución será diseñada como una aplicación de estructura simple y controlada, orientada a validación local, bajo una arquitectura por capas con separación explícita entre presentación, lógica de aplicación y persistencia de datos.

En esta primera etapa, la arquitectura debe priorizar claridad, mantenibilidad, facilidad de prueba y capacidad de ejecución local. No se persigue todavía una estructura distribuida ni una plataforma orientada a escalado masivo, sino una base técnica coherente que permita construir, validar y evolucionar el sistema sin complejidad innecesaria.

## Estilo arquitectónico elegido

El estilo arquitectónico base del proyecto será un monolito modular con separación de responsabilidades internas. Esta decisión permite mantener despliegue simple, ejecución local directa y menor sobrecarga operativa, al mismo tiempo que conserva límites claros entre módulos funcionales y técnicos.

La solución no se diseñará como microservicios en esta etapa, ya que ello introduciría complejidad de comunicación, despliegue, observabilidad y coordinación que no aporta valor directo al objetivo actual del experimento.

## Separación principal del sistema

La estructura general del sistema se dividirá en tres áreas principales:

### 1. Capa de presentación

Responsable de ofrecer la interfaz mínima necesaria para interactuar con el sistema. En esta etapa su objetivo será funcional, no experiencial. Debe permitir registrar consultas, visualizar estados y mostrar respuestas de manera suficiente para validar el flujo principal.

### 2. Capa de aplicación o backend

Responsable de concentrar la lógica de negocio, las reglas del flujo, la validación de datos, la coordinación entre actores funcionales y la exposición de contratos de entrada y salida del sistema. Esta capa constituye el núcleo técnico principal del experimento y será el principal foco de pruebas.

### 3. Capa de persistencia

Responsable de almacenar y recuperar la información necesaria para sostener consultas, estados, respuestas e historial básico del flujo. Esta capa utilizará una base de datos SQL local y deberá permitir validación realista en entorno controlado.

## Relación entre frontend y backend

El frontend no accederá directamente a la base de datos ni contendrá reglas críticas del negocio. Toda interacción del usuario deberá pasar por la capa de aplicación, donde se centralizarán validaciones, decisiones de flujo y control del estado funcional.

Esta separación se adopta para proteger la mantenibilidad, evitar duplicidad de lógica y asegurar que las pruebas sobre el comportamiento principal puedan concentrarse en una capa técnica claramente delimitada.

## Persistencia SQL local

La solución utilizará persistencia en una base de datos SQL local como parte obligatoria del experimento. Esta decisión responde a la necesidad de validar flujos con almacenamiento real, mantener consistencia básica de información y probar el comportamiento del sistema en condiciones cercanas a un uso real controlado.

La base de datos deberá ser suficiente para registrar consultas, estados, respuestas, referencias mínimas del conductor y trazas básicas necesarias para el flujo principal, sin convertir el modelo de datos en un diseño sobredimensionado desde el inicio.

## Límites técnicos explícitos de la arquitectura

Para proteger el alcance del experimento, se establecen los siguientes límites técnicos:

- No se incorporarán microservicios en esta etapa.
- No se integrarán servicios externos críticos para que el sistema funcione.
- No se distribuirá la lógica de negocio entre múltiples aplicaciones independientes.
- No se diseñará una infraestructura orientada a alta disponibilidad o escalado horizontal temprano.
- No se permitirá acceso directo desde la interfaz de usuario hacia la base de datos.
- No se incorporará complejidad técnica que no aporte a la validación del flujo funcional prioritario.

## Módulos principales del backend

La capa de backend se organizará en módulos funcionales y técnicos con responsabilidades claramente delimitadas. Esta organización busca facilitar mantenibilidad, pruebas, bajo acoplamiento y evolución controlada del sistema.

En esta primera etapa, se proponen los siguientes módulos principales:

### 1. Módulo de consultas de atención

Responsable de registrar, recuperar y gestionar las consultas iniciales realizadas por el conductor. Este módulo constituye el núcleo funcional principal del sistema, ya que concentra el flujo de apertura, seguimiento y actualización de solicitudes.

Sus responsabilidades incluyen:

- registrar nuevas consultas;
- asociar motivo principal de atención;
- almacenar descripción libre del problema;
- mantener estado general de la consulta;
- permitir recuperación por identificador o historial;
- servir como punto principal de coordinación del flujo.

### 2. Módulo de disponibilidad de atención

Responsable de representar y actualizar la disponibilidad inicial del mecánico o del taller para atender una consulta. Su función es ayudar a determinar si la solicitud puede avanzar, si requiere espera o si permanece pendiente de confirmación.

Sus responsabilidades incluyen:

- registrar disponibilidad básica de atención;
- actualizar estado de disponibilidad;
- relacionar disponibilidad con una consulta concreta;
- mantener coherencia entre disponibilidad y estado funcional del flujo.

### 3. Módulo de disponibilidad de repuestos

Responsable de registrar o consultar la disponibilidad de repuestos vinculados a una necesidad reportada. Este módulo no pretende resolver en esta etapa un catálogo completo de inventario, sino ofrecer una validación mínima de disponibilidad o falta de confirmación.

Sus responsabilidades incluyen:

- registrar disponibilidad de repuesto;
- indicar si la disponibilidad está confirmada, no disponible o pendiente;
- relacionar la información de stock con una consulta activa;
- soportar validación progresiva cuando el repuesto no esté identificado con precisión desde el inicio.

### 4. Módulo de respuestas y estimaciones

Responsable de registrar la respuesta funcional emitida por taller o tienda respecto a una consulta. En este módulo se concentrará la información útil para la decisión del conductor, incluyendo observaciones, respuesta operativa y costo estimado cuando exista.

Sus responsabilidades incluyen:

- registrar respuesta a una consulta;
- actualizar observaciones relevantes;
- asociar costo estimado inicial cuando haya información suficiente;
- mantener la última respuesta vigente del flujo.

### 5. Módulo de historial y seguimiento

Responsable de ofrecer trazabilidad operativa básica sobre las consultas realizadas. Este módulo permitirá revisar solicitudes previas, su evolución y sus estados, tanto para validación del experimento como para comportamiento básico del sistema.

Sus responsabilidades incluyen:

- recuperar historial de consultas;
- diferenciar estados activos y cerrados cuando corresponda;
- exponer información resumida útil para seguimiento;
- apoyar validación de comportamiento histórico en pruebas e inspección funcional.

## Módulos técnicos transversales

Además de los módulos funcionales principales, la solución deberá contar con componentes técnicos transversales que soporten el sistema de forma consistente.

### 1. Módulo de validación de entrada

Responsable de validar estructuras mínimas de entrada, consistencia básica de datos y reglas de formato antes de que la información ingrese a la lógica de aplicación.

### 2. Módulo de persistencia y acceso a datos

Responsable de coordinar el almacenamiento y recuperación de entidades o modelos persistentes en la base de datos SQL local, manteniendo separación respecto a la lógica del dominio o de aplicación.

### 3. Módulo de mapeo y contratos

Responsable de transformar datos entre estructuras de entrada, objetos internos, respuestas y modelos persistentes cuando sea necesario, evitando fuga de estructuras técnicas entre capas.

### 4. Módulo de manejo de errores y estados

Responsable de asegurar respuestas coherentes, controladas y suficientemente claras ante validaciones fallidas, ausencia de datos, inconsistencias del flujo o errores recuperables.

## Fronteras iniciales de dominio

Para este experimento se definen como fronteras iniciales de dominio las siguientes áreas conceptuales:

- Consulta de atención.
- Disponibilidad de servicio.
- Disponibilidad de repuesto.
- Respuesta operativa.
- Seguimiento histórico.

Estas fronteras no deben entenderse todavía como dominios completamente aislados, pero sí como separaciones iniciales útiles para evitar mezclar toda la lógica del sistema en un solo bloque indiferenciado.

## Regla de relación entre módulos

Los módulos deberán relacionarse mediante contratos internos claros y dependencias controladas. Ningún módulo funcional debe asumir internamente responsabilidades completas de otro módulo ni acceder de forma desordenada a estructuras ajenas sin mediación de la capa correspondiente.

La lógica principal del flujo deberá mantenerse coordinada desde la capa de aplicación, evitando acoplamiento directo excesivo entre módulos y reduciendo el riesgo de que una modificación en una parte del sistema rompa comportamientos no relacionados.

## Flujo general de información

El flujo general del sistema seguirá una secuencia controlada desde la interacción del usuario hasta la persistencia y la respuesta final. La lógica general será la siguiente:

1. El conductor interactúa con la interfaz para registrar una consulta o revisar una existente.
2. La capa de presentación envía la solicitud al backend mediante un contrato definido.
3. La capa de aplicación valida los datos de entrada, aplica reglas del flujo y coordina los módulos funcionales correspondientes.
4. Cuando la operación requiere persistencia o consulta histórica, la capa de aplicación interactúa con la capa de acceso a datos.
5. La base de datos SQL local almacena o recupera la información requerida.
6. El backend compone la respuesta funcional y la devuelve a la interfaz.
7. La interfaz presenta el estado, resultado o información necesaria para la decisión del usuario.

Este flujo busca mantener centralizada la lógica de negocio y evitar dependencias cruzadas o decisiones dispersas entre frontend, backend y persistencia.

## Conceptos principales del sistema

A nivel conceptual, el sistema se apoyará inicialmente en los siguientes elementos principales de información:

### 1. Consulta

Representa la solicitud inicial realizada por el conductor. Constituye la entidad central del experimento, ya que articula el problema reportado, el estado del flujo y las respuestas recibidas.

### 2. Motivo de atención

Representa la categoría principal de la necesidad del conductor, por ejemplo mantenimiento preventivo, reparación correctiva o necesidad de repuesto.

### 3. Estado de consulta

Representa la situación funcional actual de la consulta dentro del flujo. Debe permitir indicar si la consulta está pendiente, en revisión, confirmada parcialmente, confirmada o no resuelta.

### 4. Disponibilidad de atención

Representa la posibilidad inicial de que el taller o el mecánico atiendan la solicitud planteada.

### 5. Disponibilidad de repuesto

Representa la confirmación, ausencia o falta de validación de la pieza o insumo requerido para continuar el flujo.

### 6. Respuesta operativa

Representa la información emitida por el taller o la tienda para ayudar al conductor a decidir. Puede incluir observación, respuesta funcional, estado actualizado y costo estimado cuando corresponda.

### 7. Historial

Representa el conjunto de consultas y cambios relevantes asociados al seguimiento del flujo, útil tanto para validación del experimento como para uso básico del sistema.

## Relación conceptual inicial entre entidades

La relación conceptual inicial del sistema se define de forma simple y suficiente para la etapa actual:

- Un conductor puede generar múltiples consultas.
- Cada consulta tiene un motivo principal de atención.
- Cada consulta posee un estado funcional actual.
- Cada consulta puede tener información asociada de disponibilidad de atención.
- Cada consulta puede tener información asociada de disponibilidad de repuesto.
- Cada consulta puede recibir una o varias respuestas operativas, aunque inicialmente se priorizará la última respuesta vigente.
- Cada consulta forma parte del historial general del sistema y del seguimiento del usuario correspondiente.

Esta relación deberá transformarse posteriormente en un modelo de datos más formal dentro del diseño de persistencia, manteniendo el principio de simplicidad suficiente para la primera etapa.

## Modelo de estado de ConsultaAtencion (especificación)

Esta especificación define el estado de la consulta y sus transiciones permitidas. No introduce estados adicionales a los ya definidos en la capa funcional.

### Estados válidos

- `pendiente`: consulta creada sin disponibilidad confirmada ni respuesta operativa registrada.
- `en_revision`: existe al menos una respuesta operativa o un inicio de validación, pero aún no hay confirmación suficiente.
- `confirmada_parcial`: una de las disponibilidades está confirmada como `disponible` y la otra sigue `pendiente_confirmacion` o no registrada.
- `confirmada`: disponibilidad de atención y disponibilidad de repuesto confirmadas como `disponible`.
- `no_resuelta`: al menos una disponibilidad confirmada como `no_disponible`.

### Transiciones permitidas (deterministas)

Las transiciones se recalculan después de cualquier actualización de disponibilidad o respuesta:

1. `pendiente` → `en_revision`  
   - cuando se registra una respuesta operativa pero no hay disponibilidad confirmada.
2. `pendiente` / `en_revision` → `confirmada_parcial`  
   - cuando solo una disponibilidad está confirmada como `disponible` y la otra sigue `pendiente_confirmacion` o sin registro.
3. `pendiente` / `en_revision` / `confirmada_parcial` → `confirmada`  
   - cuando disponibilidad de atención y de repuesto son `disponible`.
4. `pendiente` / `en_revision` / `confirmada_parcial` → `no_resuelta`  
   - cuando disponibilidad de atención o de repuesto es `no_disponible`.

`confirmada` y `no_resuelta` se consideran estados terminales en este corte. No se define reapertura en esta etapa.

### Sincronización con módulos

- **Disponibilidad de atención**: actualiza el estado de consulta según las reglas anteriores.  
- **Disponibilidad de repuesto**: actualiza el estado de consulta según las reglas anteriores.  
- **Respuesta operativa**: si la consulta está `pendiente` y aún no hay disponibilidad confirmada, pasa a `en_revision`. No puede convertir por sí sola una consulta en `confirmada` o `no_resuelta`.

### Criterio de consulta activa vs cerrada

- **Activa**: `pendiente`, `en_revision`, `confirmada_parcial`.
- **Cerrada**: `confirmada`, `no_resuelta`.

### Decisiones y pendientes

| Decisión | Estado | Justificación |
|---|---|---|
| Estados válidos: `pendiente`, `en_revision`, `confirmada_parcial`, `confirmada`, `no_resuelta` | Aprobada | Coinciden con RF-07 y no introducen estados nuevos. |
| `no_resuelta` se activa si cualquier disponibilidad es `no_disponible` | Aprobada | Prioriza claridad y cierre temprano ante imposibilidad operativa. |
| `confirmada` requiere ambas disponibilidades en `disponible` | Aprobada | Evita estados ambiguos sin confirmación completa. |
| Respuesta operativa solo dispara `en_revision` si no hay disponibilidad confirmada | Aprobada | Mantiene separación entre respuesta informativa y disponibilidad verificable. |
| Reapertura de consultas cerradas | Pendiente | No definido en el alcance actual. |
| Uso de `estado_general` para mapear estado de consulta | Pendiente | No existe taxonomía documentada para `estado_general`. |

## Contratos internos del sistema

La comunicación entre capas y módulos deberá apoyarse en contratos internos explícitos, incluso si en esta primera etapa todos los componentes residen dentro del mismo monolito modular. Esto permitirá reducir acoplamiento, facilitar pruebas y mantener claridad en la evolución del sistema.

Los contratos internos deberán definir al menos:

- estructura mínima de entrada de una consulta;
- estructura de respuesta de disponibilidad;
- estructura de respuesta operativa;
- estructura de estado funcional de una consulta;
- estructura básica de historial o resumen.

Ningún módulo deberá depender de estructuras implícitas o manipular directamente datos ajenos sin una interfaz clara de intercambio.

## Contrato externo de interacción

La interfaz del sistema deberá comunicarse con el backend mediante contratos externos simples, consistentes y estables. Estos contratos describirán las operaciones mínimas necesarias para registrar consultas, consultar estados, obtener historial y actualizar respuestas del flujo.

En etapas posteriores, estos contratos deberan formalizarse de manera mas explicita, idealmente mediante una especificacion tipo OpenAPI o equivalente, con el fin de mantener alineacion entre frontend, backend y pruebas de integracion.

En el corte actual, el contrato externo se materializa como una interfaz CLI ejecutable mediante `python -m ecosistema_santi` y una capa web minima ejecutable con `python -m ecosistema_santi.web`, ambas con operaciones para registrar consultas, consultar estados, actualizar disponibilidades, registrar respuestas y obtener historial. Estas interfaces cumplen la funcion de capa de presentacion minima hasta contar con una interfaz dedicada.

## Primera aproximación al modelo de persistencia

La persistencia inicial del sistema será relacional y orientada a almacenar solo la información necesaria para sostener el experimento funcional. La base de datos SQL local deberá contener, como mínimo, estructuras relacionadas con:

- conductores o referencias mínimas de usuario;
- consultas;
- motivos de atención;
- estados de consulta;
- disponibilidad de atención;
- disponibilidad de repuesto;
- respuestas operativas;
- historial o marcas temporales relevantes del flujo.

La persistencia no buscará desde el inicio representar todos los detalles posibles del negocio, sino capturar de forma consistente la información suficiente para validar el flujo principal y sostener pruebas confiables.

### Implementación actual de persistencia (corte inicial)

En la implementación actual, la persistencia se concretó con las siguientes tablas mínimas:

- `consultas` (consulta de atención).
- `disponibilidad_atencion` (estado en `disponible`, `no_disponible`, `pendiente_confirmacion`).
- `disponibilidad_repuesto` (estado en `disponible`, `no_disponible`, `pendiente_confirmacion`).
- `respuestas_operativas` (estado_general libre, observacion obligatoria, costo_estimado opcional).

El historial se deriva del listado de consultas (`consultas`) y no utiliza tabla específica en esta etapa.

## Regla de diseño de datos

El modelo de datos deberá priorizar coherencia, claridad y soporte al flujo funcional antes que sofisticación estructural. No se agregarán tablas, relaciones o normalizaciones complejas si no aportan valor real a la validación del experimento.

Toda decisión de persistencia deberá justificarse por una de estas razones:

- soportar una funcionalidad priorizada;
- permitir trazabilidad funcional básica;
- facilitar pruebas;
- o mantener integridad suficiente en el comportamiento del sistema.

## Decisiones técnicas principales

A partir de las necesidades del experimento y de los límites previamente establecidos, se adoptan las siguientes decisiones técnicas principales:

- El backend se implementará en Python, priorizando velocidad de desarrollo, claridad de código y facilidad de prueba.
- La lógica principal del sistema se concentrará en backend y no en la interfaz.
- Las pruebas unitarias y de integración del backend se ejecutarán con `pytest`.
- La cobertura de código se medirá con `pytest-cov`.
- La observación de cobertura en el entorno de desarrollo podrá apoyarse en las capacidades de pruebas y cobertura de Visual Studio Code.
- Los dobles de prueba y mocks se implementarán con `unittest.mock` o con apoyo de `pytest-mock` cuando aporte mayor claridad.
- La persistencia se realizará sobre una base de datos SQL local.
- La comunicación entre frontend y backend se definirá mediante contratos claros y estables, formalizables posteriormente en una especificación tipo OpenAPI.
- La solución se ejecutará como monolito modular de despliegue simple en entorno local.

Estas decisiones se consideran suficientes para sostener el experimento actual sin introducir dependencias o complejidades que no aporten directamente a la validación principal.

## Criterios de selección tecnológica

La selección tecnológica del proyecto responde a criterios explícitos y no a preferencia arbitraria. Toda tecnología adoptada en esta etapa debe cumplir al menos con la mayoría de las siguientes condiciones:

- compatibilidad con ejecución local simple;
- facilidad de integración con flujo por CLI;
- soporte sólido para pruebas unitarias y de integración;
- buena mantenibilidad y claridad estructural;
- facilidad de observación de cobertura y resultados de pruebas;
- bajo costo operativo inicial;
- baja dependencia de servicios externos obligatorios;
- y alineación con el objetivo del experimento de construir rápido sin perder control de calidad.

Bajo estos criterios, Python y su ecosistema de pruebas resultan adecuados para el experimento, especialmente por su velocidad de iteración, su soporte para `pytest`, su integración con Visual Studio Code y su capacidad de trabajar con mocks, cobertura y persistencia local de forma simple y verificable.

## Observabilidad y manejo de errores

La solución deberá incorporar una observabilidad básica desde la primera etapa, suficiente para comprender el comportamiento del sistema durante ejecución local, depuración y pruebas.

### Observabilidad mínima esperada

El sistema deberá producir:

- logs estructurados;
- mensajes suficientemente claros para identificar operación, contexto y resultado;
- registro de errores relevantes del flujo;
- y señales mínimas de trazabilidad de ejecución sobre operaciones críticas.

Cuando sea posible, los logs deberán producirse en formato estructurado, preferiblemente JSON, para facilitar inspección, filtrado y futura evolución hacia herramientas de monitoreo más completas.

### Manejo de errores

El sistema no deberá resolver errores mediante salidas improvisadas o mensajes ambiguos. Todo error relevante del flujo debe manejarse de forma controlada, con respuesta coherente y contexto suficiente para depuración.

Se establecen las siguientes reglas:

- no usar `print()` como mecanismo principal de manejo de errores del sistema;
- no exponer detalles sensibles de excepción al usuario final;
- mantener errores técnicos separados de mensajes funcionales comprensibles;
- validar entradas antes de aplicar lógica de negocio;
- y responder con estados controlados ante datos inválidos, ausencia de información o fallos recuperables.

## Seguridad base

La primera etapa del experimento no exige una arquitectura de seguridad avanzada, pero sí una base mínima obligatoria de seguridad por diseño.

Se establecen las siguientes reglas de seguridad base:

- toda entrada debe validarse de manera explícita;
- no debe confiarse en datos provenientes del usuario sin control previo;
- la salida del sistema no debe exponer información sensible innecesaria;
- las credenciales o configuraciones sensibles no deben almacenarse dentro del código fuente;
- la aplicación debe operar con el menor privilegio posible en el entorno local;
- y la solución debe evitar integraciones externas que amplíen innecesariamente la superficie de riesgo en esta primera etapa.

También deberá evitarse el registro de datos sensibles en logs, especialmente si más adelante el sistema evoluciona hacia ejecución compartida o remota.

## Criterio de transición hacia la estrategia de pruebas

El proyecto podrá avanzar desde la capa de diseño del sistema hacia `04-estrategia-pruebas.md` cuando se considere que la estructura técnica base ya ofrece suficiente claridad para definir cómo será validada.

La transición será válida si se cumplen al menos las siguientes condiciones:

- la arquitectura general está definida;
- los módulos principales del backend están identificados;
- el flujo general de información está claro;
- existen conceptos principales de persistencia suficientemente delimitados;
- las decisiones tecnológicas esenciales ya fueron adoptadas;
- y el sistema puede pensarse en términos de unidades, integraciones y puntos de validación concretos.

En ese punto, la estrategia de pruebas podrá construirse sobre una base técnica realista y no sobre supuestos vagos de implementación.

## Cierre de la capa de diseño

Con la información registrada en este documento, el proyecto cuenta con una base de diseño del sistema suficiente para continuar. Se dispone de una arquitectura general explícita, un estilo estructural controlado, módulos principales delimitados, flujo de información definido, criterios de persistencia, decisiones tecnológicas principales y restricciones técnicas claras.

En consecuencia, se considera razonable cerrar esta 