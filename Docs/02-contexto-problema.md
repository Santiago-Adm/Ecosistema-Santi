# Contexto del proyecto

## Propósito del documento

Este documento define el contexto inicial del proyecto y establece el problema principal que justifica el experimento de desarrollo. Su finalidad es describir con claridad la situación actual del usuario objetivo, el dolor observado, las condiciones del entorno y la viabilidad inicial del problema a resolver.

Este archivo pertenece a la capa de análisis y actúa como base para la posterior definición funcional, el diseño del sistema y la estrategia de validación. No contiene aún decisiones técnicas de arquitectura, stack o implementación.

## Contexto general del proyecto

El proyecto surge a partir de la observación de un problema recurrente en el proceso de mantenimiento, reparación y adquisición de repuestos para mototaxis. El contexto identificado muestra que el usuario depende de su vehículo como fuente principal de ingresos y que cualquier falla, demora o incertidumbre en el proceso de atención afecta directamente su economía, su rutina diaria y su estabilidad operativa.

La necesidad detectada no se limita únicamente a comprar repuestos. El problema involucra también disponibilidad del mecánico, confirmación de stock, tiempo de espera, coordinación con la tienda, estimación de costos y reducción de incertidumbre antes de trasladarse físicamente al taller o al punto de compra.

## Actor principal observado

El actor principal observado es un conductor de mototaxi con experiencia prolongada en su actividad y alta dependencia operativa de su unidad de trabajo. Utiliza su vehículo como herramienta principal de generación de ingresos y requiere mantenimiento preventivo mensual, además de resolver fallas correctivas cuando ocurren averías o desgaste por uso continuo.

El actor no presenta un perfil altamente técnico respecto a repuestos o compatibilidades mecánicas, por lo que depende de manera importante del criterio del mecánico, de la tienda y de confirmaciones externas para tomar decisiones de compra o reparación.

## Problema principal observado

El problema principal identificado es la pérdida de tiempo y de capacidad de trabajo ocasionada por no tener certeza suficiente, antes de desplazarse o esperar, sobre tres factores críticos: disponibilidad de repuestos, disponibilidad del mecánico y tiempo real de resolución.

La situación actual obliga al usuario a llamar, escribir, esperar respuesta, acudir físicamente al taller o regresar en otro momento sin garantía de atención inmediata ni de disponibilidad completa de piezas. Esta incertidumbre produce fricción operativa, retraso en la reparación y mayor desgaste económico.

## Impacto inicial observado

El impacto del problema es directo sobre los ingresos diarios del usuario, ya que la mototaxi constituye su fuente principal de sustento. Cuando el vehículo no está operativo o la atención se retrasa, el usuario pierde horas de trabajo, reorganiza actividades familiares y posterga otras obligaciones del día.

Además del impacto económico, existe un impacto operativo importante: pérdida de tiempo en desplazamientos, espera improductiva, compras incompletas, consultas repetidas y dependencia de información informal. También se observa un componente emocional asociado a preocupación, frustración e incertidumbre respecto a cuándo podrá volver a trabajar con normalidad.

## Evidencia principal observada

La evidencia inicial del proyecto proviene de una entrevista contextual realizada a un conductor de mototaxi con experiencia directa en el uso, mantenimiento y reparación de su unidad. El entrevistado describe una relación operativa crítica con su vehículo, ya que este representa su principal fuente de ingresos y sostiene parte importante de su rutina económica y familiar.

A lo largo de la entrevista se observan patrones repetidos de dependencia hacia el mecánico y la tienda, uso frecuente de llamadas o visitas presenciales para confirmar disponibilidad, dificultad para anticipar costos y una necesidad constante de resolver fallas o mantenimientos con el menor tiempo posible de detención.

También se identifica que el usuario no siempre puede nombrar con exactitud el repuesto que necesita y que en muchas ocasiones depende de apoyo humano, fotos o validación del mecánico para evitar errores de compra o reparaciones incompletas.

## Hallazgos clave del caso observado

A partir de la entrevista se identifican los siguientes hallazgos principales:

- El usuario no solo necesita repuestos; necesita certeza previa antes de desplazarse o esperar.
- La disponibilidad del mecánico es tan importante como la disponibilidad del repuesto.
- La pérdida de tiempo se traduce directamente en pérdida de ingresos diarios.
- El canal actual dominante es la llamada telefónica, con uso complementario de WhatsApp.
- El usuario confía más en personas conocidas que en procesos impersonales.
- Existe disposición a usar medios remotos si estos ofrecen certeza, claridad y confianza.
- El usuario presenta alfabetización técnica limitada respecto al nombre exacto o compatibilidad de ciertos repuestos.
- La incertidumbre actual afecta decisiones económicas, tiempos de trabajo y organización familiar.

## Patrones observados en el comportamiento del usuario

El caso analizado permite identificar patrones de comportamiento relevantes para el problema:

### 1. Dependencia operativa de terceros

El usuario depende del criterio del mecánico y de la tienda para diagnosticar, identificar, cotizar y confirmar disponibilidad. Esta dependencia reduce autonomía y aumenta la necesidad de canales confiables de comunicación y confirmación.

### 2. Compra y reparación bajo urgencia

Aunque existen mantenimientos preventivos mensuales, una parte importante de las decisiones ocurre bajo urgencia, falla inesperada o necesidad inmediata de volver a trabajar. Esto eleva la sensibilidad al tiempo de respuesta y a la certeza de atención.

### 3. Tolerancia limitada a la incertidumbre

El usuario tolera cierta espera, pero percibe como especialmente grave no saber si encontrará el repuesto, si el mecánico estará libre o si el gasto final será asumible. La incertidumbre pesa más que la simple demora.

### 4. Preferencia por apoyo humano validado

El usuario confía en respuestas remotas cuando provienen de actores con los que ya tiene una relación previa. La confianza no surge de la tecnología por sí sola, sino de la continuidad con la experiencia de atención existente.

## Formulación inicial de hipótesis

A partir del análisis del caso se proponen las siguientes hipótesis iniciales del proyecto:

### Hipótesis 1

Si el usuario puede conocer antes de desplazarse si el repuesto está disponible y si el mecánico puede atenderlo, entonces reducirá tiempos muertos y pérdidas operativas, porque hoy la principal fricción está en la incertidumbre previa a la atención.

### Hipótesis 2

Si el sistema presenta información clara sobre disponibilidad, costo estimado y estado de atención, entonces el usuario podrá tomar decisiones con mayor seguridad, porque actualmente depende de confirmaciones informales, llamadas repetidas o visitas presenciales.

### Hipótesis 3

Si el proceso permite apoyo visual o validación asistida para identificar repuestos, entonces disminuirán errores de compra o consultas ambiguas, porque el usuario no siempre domina la nomenclatura técnica exacta.

### Hipótesis 4

Si se reduce el tiempo de coordinación entre conductor, mecánico y tienda, entonces aumentará la percepción de rapidez y confiabilidad del servicio, porque el problema no está solo en el repuesto, sino en toda la coordinación alrededor de la atención.

## Valor analítico inicial del caso

Este caso ofrece evidencia suficiente para considerar que el problema observado no es anecdótico ni superficial. La entrevista muestra un dolor real, una frecuencia operativa relevante, impacto económico directo y patrones claros de comportamiento que justifican avanzar hacia una definición funcional posterior.

Sin embargo, esta evidencia aún debe considerarse inicial. El objetivo de esta etapa no es asumir que todas las hipótesis están confirmadas, sino registrar una base analítica suficientemente sólida como para continuar con la formulación del problema, la delimitación del experimento y la construcción de los siguientes artefactos del proyecto.
## Objetivo del proyecto

El objetivo del proyecto es explorar la viabilidad de una solución digital que reduzca la incertidumbre operativa del conductor de mototaxi antes de desplazarse o iniciar una reparación, especialmente en relación con la disponibilidad de repuestos, la disponibilidad del mecánico y el tiempo estimado de atención.

En esta etapa, el objetivo no es construir una plataforma completa ni resolver todo el ecosistema de compra y reparación de repuestos, sino validar si una estructura de desarrollo guiada por documentación viva, CLI y enfoque TDD-BDD-SDD puede producir una solución funcional con velocidad, calidad y capacidad real de ejecución local.

## Alcance inicial del experimento

El alcance inicial del experimento se limita a un flujo mínimo que permita representar y validar el problema principal observado. El sistema deberá orientarse a reducir la fricción de coordinación previa entre conductor, taller y disponibilidad de atención, sin intentar abarcar desde el inicio todas las posibles variantes operativas del negocio.

El experimento buscará demostrar si es posible construir una solución suficientemente útil y verificable a partir de un conjunto mínimo de documentos vivos, una arquitectura controlada, pruebas centradas en backend y una implementación guiada por contexto estructurado.

## Límites explícitos del experimento

Para proteger el enfoque de velocidad, calidad y capacidad de levantar el sistema, se establecen los siguientes límites explícitos:

- No se desarrollará una solución completa para todos los canales de comunicación del negocio.
- No se integrarán en la primera etapa APIs reales de WhatsApp, llamadas automatizadas ni servicios externos de mensajería.
- No se priorizarán funcionalidades visuales avanzadas, catálogos extensos de imágenes ni experiencias ricas de frontend que no aporten directamente a la validación del problema principal.
- No se abordará en esta etapa la totalidad de la casuística logística, comercial o administrativa del taller y la tienda.
- No se buscará una cobertura total del sistema completo, sino una validación fuerte y medible sobre el backend y los módulos críticos.
- No se considerará esta primera iteración como producto final, sino como experimento controlado de viabilidad funcional y metodológica.

## Criterio de viabilidad inicial

El proyecto se considerará inicialmente viable si cumple con las siguientes condiciones:

- Existe un dolor real, frecuente o económicamente relevante identificado en la entrevista.
- El problema puede traducirse en comportamiento funcional verificable.
- El alcance puede mantenerse limitado sin perder valor de validación.
- El sistema puede levantarse de forma local en un entorno controlado.
- El backend puede probarse con cobertura alta y criterios de calidad explícitos.
- La documentación viva permite orientar a la CLI sin necesidad de reconstruir todo el contexto en cada interacción.

## Criterio de éxito del experimento

El experimento será considerado exitoso si logra demostrar, en esta etapa inicial, que una estructura documental mínima pero bien organizada puede servir de base para desarrollar una solución funcional, trazable y validable con apoyo de CLI.

El éxito no dependerá de tener el producto final más completo, sino de comprobar que el flujo metodológico propuesto reduce ambigüedad, mejora claridad de construcción, permite sostener pruebas sobre backend y facilita levantar el sistema localmente con menor fricción.

## Exclusiones conscientes

Quedan fuera del alcance inicial todas las funcionalidades o decisiones que no contribuyan directamente a validar la hipótesis principal del proyecto. Esto incluye automatizaciones externas complejas, ampliaciones de alcance comercial, optimizaciones prematuras de experiencia visual, integraciones de alta dependencia externa y crecimiento funcional no respaldado por evidencia del problema actual.

Toda nueva incorporación deberá justificar de forma explícita por qué aporta a la validación del experimento y no simplemente al aumento del tamaño aparente del sistema.

## Supuestos iniciales del proyecto

A partir del contexto analizado y de la entrevista realizada, este proyecto parte de los siguientes supuestos iniciales:

- El problema de incertidumbre previa a la atención es suficientemente relevante como para justificar una solución digital inicial.
- La reducción de tiempo muerto y de pérdida operativa generará valor percibido para el conductor.
- El usuario aceptará una solución simple si esta mantiene continuidad con la lógica de atención actual y no rompe su confianza con el taller o la tienda.
- La información mínima más valiosa antes del desplazamiento será la relacionada con disponibilidad de repuestos, disponibilidad del mecánico y estimación inicial de atención o costo.
- Un enfoque documental mínimo, guiado por CLI y validación fuerte en backend, será suficiente para construir una primera solución funcional sin necesidad de ampliar el alcance desde el inicio.

Estos supuestos no se consideran confirmados todavía. Su función es servir como base de trabajo para formular requisitos, pruebas y decisiones posteriores con mayor claridad.

## Riesgos iniciales identificados

El análisis también permite reconocer riesgos tempranos que podrían afectar la viabilidad del experimento o la utilidad real del sistema:

### 1. Riesgo de sobredimensionar la solución

Existe el riesgo de intentar resolver demasiado pronto múltiples necesidades del negocio, integraciones externas o variaciones del flujo real, lo que desviaría el experimento de su objetivo principal.

### 2. Riesgo de depender excesivamente de un solo caso observado

Aunque la entrevista analizada ofrece evidencia útil, todavía representa una base inicial limitada. Existe el riesgo de generalizar en exceso comportamientos o prioridades que podrían variar en otros usuarios o contextos similares.

### 3. Riesgo de mantener ambigüedad funcional

Si las necesidades detectadas no se convierten en requisitos, historias y criterios de aceptación claros, la implementación podría crecer de forma difusa o contradictoria.

### 4. Riesgo de introducir complejidad técnica prematura

Agregar integraciones reales, automatizaciones externas o capas adicionales demasiado pronto podría afectar velocidad, enfoque y capacidad de levantar el sistema en un entorno controlado.

### 5. Riesgo de validar solo construcción y no valor

Existe el riesgo de que el proyecto llegue a ser implementable desde el punto de vista técnico, pero no demuestre con suficiente claridad que reduce el dolor principal del usuario observado.

## Preguntas abiertas

Antes de avanzar a la siguiente capa documental, deben mantenerse visibles las siguientes preguntas abiertas:

- ¿Qué información mínima necesita realmente el usuario para decidir si se desplaza o espera?
- ¿Qué parte del problema genera mayor valor si se resuelve primero: stock, disponibilidad del mecánico o estimación de atención?
- ¿Qué nivel de detalle funcional es suficiente para validar la hipótesis sin ampliar el alcance?
- ¿Qué comportamientos observados en esta entrevista deben considerarse estructurales y cuáles podrían ser particulares del caso?
- ¿Qué restricciones operativas del taller y de la tienda condicionarán el comportamiento real del sistema?
- ¿Qué partes del flujo pueden validarse con una simulación controlada y cuáles exigirán evidencia operativa adicional?

Estas preguntas no bloquean el avance inmediato, pero deben permanecer activas porque orientan la definición funcional posterior y ayudan a prevenir ambigüedad.

## Criterio de transición hacia la definición funcional

El proyecto podrá avanzar desde la capa de análisis hacia la capa de definición funcional cuando se considere que el problema principal está formulado con suficiente claridad, que las hipótesis iniciales están explícitamente registradas y que el alcance del experimento se encuentra limitado de forma razonable.

La transición no exige validación total del mercado ni cierre absoluto de todas las dudas, pero sí una base analítica suficientemente coherente para transformar el problema en requisitos funcionales, historias de usuario y criterios de aceptación sin perder el foco del experimento.

## Cierre analítico inicial

Con la información disponible en esta etapa, el proyecto cuenta con una base analítica inicial suficiente para continuar. Se dispone de un actor principal identificado, un problema concreto con impacto económico y operativo, evidencia cualitativa directa, hipótesis explícitas, límites iniciales del experimento y criterios mínimos para seguir avanzando.

En consecuencia, se considera razonable cerrar esta primera fase de análisis y utilizar este documento como referencia de entrada para la construcción del archivo `02-definicion-funcional.md`.