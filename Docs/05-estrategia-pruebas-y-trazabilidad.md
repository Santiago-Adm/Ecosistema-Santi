<!--toc:start-->

- [Propósito del documento](#propósito-del-documento)
- [Alcance de la estrategia de pruebas](#alcance-de-la-estrategia-de-pruebas)
- [Rol de TDD en el proyecto](#rol-de-tdd-en-el-proyecto)
- [Rol de BDD en el proyecto](#rol-de-bdd-en-el-proyecto)
- [Principios rectores de la estrategia de pruebas](#principios-rectores-de-la-estrategia-de-pruebas)
- [Niveles de prueba del proyecto](#niveles-de-prueba-del-proyecto)
  - [1. Pruebas unitarias](#1-pruebas-unitarias)
  - [2. Pruebas de integración](#2-pruebas-de-integración)
  - [3. Pruebas funcionales orientadas a criterios de aceptación](#3-pruebas-funcionales-orientadas-a-criterios-de-aceptación)
  - [4. Pruebas amplias o de flujo completo](#4-pruebas-amplias-o-de-flujo-completo)
- [Distribución esperada del esfuerzo de pruebas](#distribución-esperada-del-esfuerzo-de-pruebas)
- [Política de mocks y dobles de prueba](#política-de-mocks-y-dobles-de-prueba)
  - [Uso permitido de mocks](#uso-permitido-de-mocks)
  - [Uso restringido de mocks](#uso-restringido-de-mocks)
- [Meta de cobertura de código](#meta-de-cobertura-de-código)
  - [Objetivo de cobertura](#objetivo-de-cobertura)
  - [Interpretación de la cobertura](#interpretación-de-la-cobertura)
- [Separación operativa de suites de prueba](#separación-operativa-de-suites-de-prueba)
- [Trazabilidad entre requisitos, historias y pruebas](#trazabilidad-entre-requisitos-historias-y-pruebas)
- [Identificación mínima de pruebas](#identificación-mínima-de-pruebas)
- [Evidencias esperadas de validación](#evidencias-esperadas-de-validación)
- [Definition of Done de pruebas](#definition-of-done-de-pruebas)
- [Riesgos principales de validación](#riesgos-principales-de-validación)
- [Criterio de transición hacia trazabilidad ligera](#criterio-de-transición-hacia-trazabilidad-ligera)
- [Cierre de la estrategia de pruebas](#cierre-de-la-estrategia-de-pruebas)
- [Trazabilidad ligera](#trazabilidad-ligera)
  - [Propósito del documento](#propósito-del-documento-1)
  - [Alcance de la trazabilidad](#alcance-de-la-trazabilidad)
  - [Principio rector de ligereza](#principio-rector-de-ligereza)
  - [Modelo mínimo de trazabilidad](#modelo-mínimo-de-trazabilidad)
  - [Regla de bidireccionalidad mínima](#regla-de-bidireccionalidad-mínima)
  - [Sistema de identificadores mínimos](#sistema-de-identificadores-mínimos)
  - [Regla de mantenimiento práctico](#regla-de-mantenimiento-práctico)
  - [Estructura mínima de trazabilidad](#estructura-mínima-de-trazabilidad)
  - [Tabla base de relaciones](#tabla-base-de-relaciones)
  - [Plantilla mínima por fila de trazabilidad](#plantilla-mínima-por-fila-de-trazabilidad)
  - [Reglas de actualización](#reglas-de-actualización)
  - [Reglas de enlace entre artefactos](#reglas-de-enlace-entre-artefactos)
  - [Ejemplo mínimo de trazabilidad aplicada](#ejemplo-mínimo-de-trazabilidad-aplicada)
  - [Formato práctico de mantenimiento](#formato-práctico-de-mantenimiento)
  - [Revisión periódica de la trazabilidad](#revisión-periódica-de-la-trazabilidad)
  - [Riesgos de degradación de la trazabilidad](#riesgos-de-degradación-de-la-trazabilidad)
  - [Reglas de corrección ante desalineación](#reglas-de-corrección-ante-desalineación)
  - [Definition of Done de trazabilidad ligera](#definition-of-done-de-trazabilidad-ligera)
  - [Criterio de suficiencia para el experimento](#criterio-de-suficiencia-para-el-experimento)
  - [Transición hacia la siguiente capa](#transición-hacia-la-siguiente-capa)
  - [Cierre del documento](#cierre-del-documento)
  - [Sub-experimento: pruebas de integración con Testcontainers (PostgreSQL)](#sub-experimento-pruebas-de-integración-con-testcontainers-postgresql) - [Propósito](#propósito) - [Hipótesis evaluada](#hipótesis-evaluada) - [Resultado: hipótesis confirmada](#resultado-hipótesis-confirmada) - [Hallazgos técnicos](#hallazgos-técnicos) - [Decisión de alcance: suite Postgres queda como complemento permanente](#decisión-de-alcance-suite-postgres-queda-como-complemento-permanente) - [Pendiente — explícitamente abierto, no resuelto en este sub-experimento](#pendiente-explícitamente-abierto-no-resuelto-en-este-sub-experimento)
  <!--toc:end-->

## Propósito del documento

Este documento define el modelo de trazabilidad ligera del proyecto. Su finalidad es mantener una relación visible, simple y útil entre el problema identificado, los requisitos definidos, las historias de usuario, las pruebas realizadas y la evidencia generada durante el experimento.

La intención de esta capa no es introducir burocracia documental, sino asegurar que el desarrollo asistido por CLI conserve orientación, coherencia y capacidad de revisión retrospectiva. La trazabilidad aquí propuesta debe ayudar a comprender qué se construyó, por qué se construyó, cómo se validó y con qué evidencia puede sostenerse esa validación.

## Alcance de la trazabilidad

La trazabilidad del proyecto abarcará únicamente los artefactos mínimos necesarios para mantener control real del experimento. En esta etapa, la relación se concentrará en los siguientes elementos:

- problema o necesidad principal;
- requisitos funcionales y no funcionales;
- historias de usuario;
- criterios de aceptación;
- decisiones de diseño relevantes;
- pruebas ejecutadas;
- y evidencia principal de validación.

No se pretende rastrear cada línea de código, cada archivo auxiliar o cada decisión menor de implementación. La trazabilidad se limitará a lo que tenga valor real para comprender cobertura funcional, impacto de cambios y consistencia del desarrollo.

## Principio rector de ligereza

La trazabilidad del proyecto deberá ser suficientemente clara para sostener revisión y control, pero lo bastante ligera para no sobrecargar el flujo de trabajo. Cualquier relación documental que no aporte visibilidad, impacto o capacidad real de decisión deberá considerarse prescindible en esta etapa.

Por ello, este documento adopta los siguientes principios:

- trazar solo lo importante;
- usar identificadores simples y consistentes;
- mantener relaciones fáciles de leer;
- evitar matrices complejas si una tabla práctica basta;
- y priorizar utilidad operativa sobre formalismo excesivo.

## Modelo mínimo de trazabilidad

El modelo mínimo de trazabilidad del proyecto seguirá la siguiente cadena lógica:

1. Problema o necesidad.
2. Requisito asociado.
3. Historia de usuario correspondiente.
4. Criterio de aceptación verificable.
5. Diseño o módulo implicado.
6. Prueba aplicada.
7. Evidencia o resultado principal.

Este modelo busca asegurar dos direcciones de lectura:

- trazabilidad hacia adelante, desde el problema hasta la validación;
- y trazabilidad hacia atrás, desde una prueba, evidencia o decisión hasta su razón de existencia.

## Regla de bidireccionalidad mínima

Toda funcionalidad importante del sistema deberá poder rastrearse hacia su origen y hacia su validación. De forma equivalente, toda prueba crítica y toda evidencia relevante deberán poder vincularse con al menos un requisito, historia o criterio de aceptación.

No se considerará válida una trazabilidad que solo enumere artefactos sin mostrar relación entre ellos. La utilidad del modelo depende de que permita responder preguntas concretas, tales como:

- qué requisito cubre esta historia;
- qué prueba valida este criterio;
- qué evidencia respalda esta funcionalidad;
- o qué parte del sistema se ve afectada si un requisito cambia.

## Sistema de identificadores mínimos

Para mantener consistencia y lectura simple, el proyecto utilizará identificadores mínimos por tipo de artefacto. Como base inicial, se adoptan los siguientes prefijos:

- PRB para problemas o necesidades principales;
- RF para requisitos funcionales;
- RNF para requisitos no funcionales;
- HU para historias de usuario;
- CA para criterios de aceptación;
- DS para decisiones o referencias de diseño del sistema;
- TP para pruebas;
- EV para evidencias.

Los identificadores deberán ser únicos, estables y suficientemente simples como para ser utilizados tanto en documentos como en nombres de pruebas, tablas de relación o comentarios de implementación cuando sea útil.

## Regla de mantenimiento práctico

La trazabilidad deberá mantenerse dentro del propio repositorio y en formatos de lectura simple, preferiblemente Markdown y tablas ligeras. No se incorporarán herramientas externas complejas de gestión si no aportan valor real al tamaño y objetivo del experimento.

La actualización de relaciones deberá ocurrir principalmente cuando suceda alguno de los siguientes eventos:

- se crea un requisito nuevo;
- se modifica una historia o criterio de aceptación;
- se agrega una prueba crítica;
- se detecta una evidencia relevante;
- o se produce un cambio con impacto funcional o técnico importante.

## Estructura mínima de trazabilidad

La trazabilidad ligera del proyecto se mantendrá mediante una tabla principal de relaciones. Esta tabla no reemplaza los documentos funcionales, de diseño o de pruebas, sino que actúa como vista resumida de conexión entre ellos.

La tabla deberá permitir responder, de manera rápida, al menos estas preguntas:

- qué requisito está cubierto;
- qué historia lo representa;
- qué criterio de aceptación se verifica;
- qué módulo o diseño está implicado;
- qué prueba lo valida;
- y qué evidencia respalda el resultado.

## Tabla base de relaciones

La trazabilidad principal podrá mantenerse con la siguiente estructura mínima:

| ID origen | Tipo                | Descripción breve                    | Relación principal | Artefacto asociado | Prueba asociada | Evidencia | Estado  |
| --------- | ------------------- | ------------------------------------ | ------------------ | ------------------ | --------------- | --------- | ------- |
| RF-01     | Requisito funcional | Registrar consulta inicial           | HU-01              | DS-01              | TP-01           | EV-01     | Vigente |
| HU-01     | Historia de usuario | Registrar una consulta inicial       | CA-01, CA-02       | DS-01              | TP-01, TP-02    | EV-01     | Vigente |
| RF-06     | Requisito funcional | Consultar disponibilidad de repuesto | HU-04              | DS-03              | TP-08           | EV-05     | Vigente |

Esta tabla es intencionalmente compacta. Su propósito no es capturar todo el detalle, sino ofrecer una visión práctica y cruzada del estado de cobertura funcional y técnica.

## Plantilla mínima por fila de trazabilidad

Cada relación importante de la tabla deberá construirse con una lógica uniforme:

- un identificador de origen;
- un tipo de artefacto;
- una descripción breve y precisa;
- una referencia al artefacto relacionado más importante;
- una referencia a diseño o módulo implicado cuando aplique;
- una o más pruebas asociadas;
- una evidencia principal;
- y un estado actual.

Los estados permitidos podrán ser, como base inicial:

- pendiente;
- en definición;
- en desarrollo;
- en prueba;
- validado;
- observado;
- o descartado.

## Reglas de actualización

La tabla de trazabilidad deberá actualizarse únicamente cuando exista un cambio relevante. No se requiere edición constante por cada actividad menor del proyecto.

Como criterio práctico, la tabla se actualizará cuando ocurra alguno de estos eventos:

- se agrega un requisito nuevo;
- se modifica una historia de usuario existente;
- se redefine un criterio de aceptación importante;
- se incorpora una prueba crítica nueva;
- se obtiene una evidencia relevante de validación;
- se detecta una observación importante;
- o se descarta una relación previamente considerada válida.

Toda actualización debe priorizar claridad y consistencia antes que nivel extremo de detalle.

## Reglas de enlace entre artefactos

Para mantener utilidad real, se adoptan las siguientes reglas de enlace:

- todo requisito funcional importante debe relacionarse con al menos una historia de usuario;
- toda historia prioritaria debe relacionarse con al menos un criterio de aceptación verificable;
- todo criterio de aceptación relevante debe poder vincularse con una prueba;
- toda prueba crítica debe apuntar a un origen funcional o técnico claro;
- y toda evidencia relevante debe estar asociada a una prueba, requisito o decisión concreta.

No deben existir pruebas críticas huérfanas ni funcionalidades relevantes sin vínculo visible con validación.

## Ejemplo mínimo de trazabilidad aplicada

A continuación se muestra un ejemplo simple de relación trazable dentro del experimento:

- PRB-01: el conductor necesita conocer información útil antes de desplazarse;
- RF-01: el sistema debe permitir registrar una consulta inicial;
- HU-01: como conductor, quiero registrar una consulta para iniciar el proceso;
- CA-01: la consulta debe poder crearse con información mínima válida;
- DS-01: módulo de consultas de atención;
- TP-01: prueba unitaria de creación válida de consulta;
- TP-02: prueba de integración de persistencia de consulta;
- EV-01: resultado exitoso de pruebas y evidencia de cobertura del módulo.

Este ejemplo muestra la lógica esperada de la trazabilidad: una cadena simple, coherente y fácil de revisar.

## Formato práctico de mantenimiento

La tabla podrá mantenerse directamente dentro de este mismo archivo Markdown o en una sección específica del repositorio si en algún momento se decide separar el artefacto. No se recomienda dividirla en demasiados archivos durante esta primera etapa, ya que ello podría fragmentar la visibilidad.

La preferencia del proyecto será mantener una trazabilidad:

- visible;
- editable por texto plano;
- fácil de revisar en Git;
- y suficientemente compacta como para ser utilizada también por herramientas asistidas por IA sin sobrecarga excesiva de contexto.

## Revisión periódica de la trazabilidad

La trazabilidad ligera deberá revisarse de manera periódica y también ante cambios relevantes del proyecto. El objetivo de esta revisión no es auditar en exceso, sino confirmar que las relaciones principales siguen siendo comprensibles, útiles y consistentes con el estado real del sistema.

Como criterio práctico, la revisión deberá realizarse:

- al cierre de una iteración documental importante;
- cuando cambie un requisito funcional o no funcional crítico;
- cuando se agreguen historias o pruebas con impacto en el flujo principal;
- cuando exista evidencia de desalineación entre lo definido y lo validado;
- o durante una retrospectiva técnica del experimento.

## Riesgos de degradación de la trazabilidad

La trazabilidad del proyecto puede degradarse si no se mantiene bajo criterios simples y disciplinados. Se reconocen como riesgos principales los siguientes:

- relaciones incompletas entre requisito y prueba;
- identificadores inconsistentes o duplicados;
- historias sin vínculo visible con aceptación o validación;
- pruebas críticas sin origen funcional claro;
- evidencias no asociadas a resultados verificables;
- cambios de alcance no reflejados en la tabla principal;
- y crecimiento documental que vuelva ilegible la trazabilidad.

La presencia de uno o varios de estos riesgos deberá tratarse como señal de ajuste inmediato, no como detalle menor de documentación.

## Reglas de corrección ante desalineación

Cuando se detecte una ruptura de trazabilidad, la corrección deberá aplicarse en el punto de mayor valor explicativo. No siempre será necesario modificar todos los documentos involucrados; en muchos casos bastará con restaurar la relación principal en la tabla o en el artefacto de origen.

Como criterio general:

- si falta origen, debe corregirse el requisito o historia;
- si falta validación, debe corregirse la relación con pruebas;
- si falta evidencia, debe registrarse o vincularse el resultado disponible;
- y si el cambio volvió obsoleta una relación previa, el estado deberá actualizarse explícitamente.

No debe conservarse una relación solo por apariencia de completitud si ya no representa el estado real del proyecto.

## Definition of Done de trazabilidad ligera

La trazabilidad ligera de una funcionalidad, flujo o incremento podrá considerarse suficiente cuando cumpla, como mínimo, las siguientes condiciones:

- el origen funcional o técnico es identificable;
- existe un identificador consistente para el artefacto principal;
- la relación con historia, criterio o diseño relevante es visible;
- la prueba principal asociada está identificada;
- la evidencia básica de validación puede localizarse;
- el estado actual de la relación es comprensible;
- y la lectura de la cadena completa no requiere interpretación ambigua.

La trazabilidad no se considerará terminada solo porque exista una tabla creada. Debe existir correspondencia real entre los artefactos y el estado efectivo del desarrollo.

## Criterio de suficiencia para el experimento

Dado que este proyecto busca validar un flujo de desarrollo más ágil y apoyado por CLI, la trazabilidad se considerará suficiente si permite responder con rapidez y claridad preguntas como las siguientes:

- qué funcionalidad se construyó;
- por qué existe esa funcionalidad;
- cómo fue validada;
- qué evidencia la respalda;
- y qué impacto tendría modificarla.

Si el modelo de trazabilidad logra responder estas preguntas sin frenar de forma desproporcionada el avance del proyecto, entonces cumple su objetivo dentro del experimento.

## Transición hacia la siguiente capa

Una vez cerrada esta capa, el proyecto quedará en condiciones de avanzar hacia una fase de revisión retrospectiva, guía operativa del flujo o documento de ejecución del experimento, según la estructura que se decida adoptar a continuación.

La transición será válida si se cumplen al menos las siguientes condiciones:

- los artefactos principales del proyecto ya están conectados;
- existe una tabla base de relaciones;
- la lógica de actualización está definida;
- la revisión periódica está contemplada;
- y el modelo de trazabilidad resulta entendible sin necesidad de herramientas externas complejas.

## Cierre del documento

Con la información registrada en este archivo, el proyecto cuenta con un modelo de trazabilidad ligera suficiente para mantener visibilidad sobre el origen, desarrollo y validación de sus elementos principales. Se dispone de propósito, alcance, principios, identificadores, estructura de tabla, reglas de relación, revisión periódica, riesgos de degradación y criterio de suficiencia.

En consecuencia, se considera razonable cerrar `05-trazabilidad-ligera.md` como documento base de control documental liviano para el experimento.

## Sub-experimento: pruebas de integración con Testcontainers (PostgreSQL)

### Propósito

Esta sección registra el cierre de un sub-experimento acotado dentro de la
estrategia de pruebas: validar si las pruebas de integración del módulo de
persistencia ganan realismo al ejecutarse contra PostgreSQL real en
contenedor (vía Testcontainers), sin degradar la suite SQLite existente ni
el ciclo de feedback del desarrollo.

### Hipótesis evaluada

Si las pruebas de integración se ejecutan contra PostgreSQL real además de
SQLite, entonces aumenta el realismo de validación sin romper la suite
existente ni introducir fricción operativa inaceptable.

### Resultado: hipótesis confirmada

- Suite SQLite original: 124 tests, 0 fallos, 96.15% cobertura — sin cambios.
- Suite PostgreSQL nueva (aislada, `tests/integration_postgres/`): 19 tests,
  0 fallos, ~7s de ejecución incluyendo arranque/destrucción de contenedor.
- Suite combinada: 143 tests, 0 fallos, 98.93% cobertura.
- Aislamiento de puertos verificado: Testcontainers usa mapeo aleatorio de
  puerto del host, sin colisión con servicios fijos de otros proyectos
  locales (ej. Postgres en 5432 de otro repositorio en la misma máquina).
- La suite PostgreSQL no se ejecuta por defecto (excluida de `testpaths` en
  `pytest.ini`), preservando la velocidad del ciclo diario de pruebas.

### Hallazgos técnicos

- El esquema DDL de persistencia es 100% portable entre SQLite y PostgreSQL
  sin modificación.
- Las diferencias reales están en la capa de adaptador/driver, no en el
  esquema: marcadores de parámetro (`?` vs `%s`) y forma de acceso a filas
  (`sqlite3.Row` por nombre vs tuplas posicionales de `psycopg2`).
- El aislamiento entre pruebas se logró con `TRUNCATE ... CASCADE` sobre un
  contenedor persistente a nivel de módulo, en lugar de recrear la base en
  cada test (estrategia distinta a SQLite, justificada por costo de arranque
  del contenedor).

### Decisión de alcance: suite Postgres queda como complemento permanente

La suite `tests/integration_postgres/` se conserva como capa adicional de
validación de paridad de motor, ejecutable de forma manual o en CI cuando
se decida, sin sustituir ni alterar la suite SQLite que sigue siendo la
validación principal del flujo diario.

### Pendiente — explícitamente abierto, no resuelto en este sub-experimento

**OBS-TC-001 — Decisión de motor de persistencia en producción.**
No se decide en este punto si producción migra de SQLite a PostgreSQL.
Esta es una decisión de arquitectura (afecta `04-diseno-y-arquitectura.md`)
y debe tratarse en una sesión propia, con su propio plan y validación,
no como extensión de este sub-experimento. Si en el futuro se aprueba
explorar soporte multi-motor, el primer paso técnico identificado es
introducir una interfaz común (`Protocol` o `ABC`) para los repositorios,
evitando mantener dos implementaciones divergentes de la misma lógica de
persistencia.

**Estado:** cerrado como sub-experimento de pruebas. Pendiente de decisión
de producto/arquitectura registrado como OBS-TC-001.

