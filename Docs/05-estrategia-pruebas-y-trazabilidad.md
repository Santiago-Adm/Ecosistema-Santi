# Estrategia de pruebas

## Propósito del documento

Este documento define la estrategia de validación del sistema para el experimento de desarrollo. Su finalidad es establecer cómo se comprobará que la solución construida responde al comportamiento esperado, mantiene calidad técnica suficiente y puede evolucionar con confianza dentro del alcance delimitado del proyecto.

Este archivo pertenece a la capa de validación y calidad y actúa como contrato de pruebas para backend, integraciones controladas y flujos funcionales críticos. No describe todavía cada caso de prueba individual, sino el enfoque general, los niveles de validación, las reglas de cobertura, el uso de mocks y los criterios mínimos de evidencia.

## Alcance de la estrategia de pruebas

La estrategia de pruebas del proyecto se concentrará principalmente en el backend, ya que este constituye el núcleo principal de validación del experimento. El objetivo es demostrar que la lógica crítica del sistema puede construirse con buena calidad, bajo control técnico y con alto nivel de verificación.

El alcance incluye:

- pruebas unitarias sobre lógica de negocio y servicios;
- pruebas de integración sobre persistencia y flujos clave;
- validación de criterios de aceptación mediante escenarios funcionales;
- uso controlado de mocks y dobles de prueba;
- medición de cobertura en módulos críticos;
- y evidencia suficiente para sostener la viabilidad del flujo TDD-BDD-SDD.

Quedan fuera de esta etapa una estrategia exhaustiva de pruebas E2E de interfaz, automatización avanzada de UI o validación de integraciones externas reales no incluidas en el alcance del experimento.

## Rol de TDD en el proyecto

TDD será utilizado como práctica principal para el desarrollo de lógica interna, servicios, reglas del dominio y componentes críticos del backend. Su propósito en este proyecto es mejorar diseño, favorecer desacoplamiento, aumentar testeabilidad y reducir regresiones durante la implementación.

En este contexto, TDD se aplicará especialmente sobre:

- validaciones del flujo;
- reglas de cambio de estado;
- composición de respuestas funcionales;
- consistencia de servicios de aplicación;
- y módulos con impacto directo sobre el comportamiento principal del sistema.

## Rol de BDD en el proyecto

BDD será utilizado como mecanismo para expresar comportamiento esperado de las funcionalidades desde una perspectiva funcional y comprensible. Su propósito en este proyecto no es reemplazar las pruebas unitarias, sino servir como puente entre requisitos, historias de usuario y validación del comportamiento observable.

BDD se apoyará principalmente en:

- historias de usuario definidas en `02-definicion-funcional.md`;
- criterios de aceptación verificables;
- escenarios tipo Given/When/Then cuando aporten claridad real;
- y trazabilidad con el comportamiento que luego será respaldado por pruebas técnicas.

## Principios rectores de la estrategia de pruebas

La estrategia de pruebas del proyecto se regirá por los siguientes principios:

- La validación debe concentrarse primero en lo más crítico para el problema principal.
- Deben existir más pruebas unitarias que pruebas de integración, y muchas menos pruebas de extremo a extremo.
- La cobertura es una métrica de apoyo, no una prueba automática de calidad por sí sola.
- Los mocks deben usarse para aislar dependencias, no para esconder defectos de diseño.
- Toda prueba importante debe poder rastrearse a una necesidad funcional o técnica real.
- La suite de pruebas debe favorecer feedback rápido y confianza sostenida.
- Las pruebas deben ayudar a diseñar mejor el sistema, no solo a verificarlo al final.


## Niveles de prueba del proyecto

La estrategia de validación del proyecto se organizará en niveles de prueba complementarios, con prioridad en pruebas unitarias y de integración, y con uso muy limitado de pruebas amplias de flujo completo.

### 1. Pruebas unitarias

Las pruebas unitarias constituirán la base principal de la estrategia. Su función será validar lógica de negocio, reglas de aplicación, validaciones, transformaciones y comportamiento interno de componentes críticos en aislamiento controlado.

Estas pruebas deberán ser:

- rápidas;
- deterministas;
- independientes entre sí;
- fáciles de ejecutar de forma frecuente;
- y centradas en una sola responsabilidad por caso.

### 2. Pruebas de integración

Las pruebas de integración se utilizarán para validar la interacción entre componentes relevantes del sistema, especialmente en relación con persistencia SQL local, repositorios, servicios de aplicación y contratos internos del backend.

Estas pruebas deberán verificar, al menos, que:

- la persistencia funciona de forma coherente;
- los módulos principales cooperan correctamente;
- los flujos críticos pueden ejecutarse con datos reales o casi reales;
- y las interfaces entre capas no rompen el comportamiento esperado.

### 3. Pruebas funcionales orientadas a criterios de aceptación

Las pruebas funcionales se utilizarán para validar que historias y criterios de aceptación se expresan de forma comprobable. En esta etapa no se busca una automatización exhaustiva de interfaz, sino una validación clara de comportamiento observable, principalmente desde backend o mediante escenarios controlados.

### 4. Pruebas amplias o de flujo completo

Las pruebas de flujo completo no serán el foco principal del experimento. Solo se utilizarán de forma muy limitada para verificar recorridos esenciales del sistema cuando aporten confianza adicional sin introducir una carga desproporcionada de mantenimiento.

## Distribución esperada del esfuerzo de pruebas

La distribución esperada del esfuerzo seguirá una lógica de pirámide de pruebas:

- mayoría de pruebas unitarias;
- menor cantidad de pruebas de integración;
- y muy pocas pruebas amplias de flujo completo.

Esta distribución se adopta para mantener retroalimentación rápida, reducir fragilidad innecesaria y concentrar el mayor volumen de validación en las capas donde el experimento obtiene más valor técnico.

## Política de mocks y dobles de prueba

Los mocks y dobles de prueba se utilizarán de forma controlada y deliberada. Su propósito será aislar dependencias externas o componentes secundarios cuando ello permita validar mejor una unidad concreta sin introducir inestabilidad o lentitud artificial.

### Uso permitido de mocks

Se permitirá el uso de mocks principalmente para:

- aislar servicios o colaboradores no esenciales a la unidad probada;
- evitar dependencias externas en pruebas unitarias;
- verificar interacciones relevantes entre componentes cuando corresponda;
- simular respuestas de módulos que no forman parte directa del comportamiento que se desea validar;
- y controlar condiciones excepcionales difíciles de reproducir con precisión en una prueba unitaria.

### Uso restringido de mocks

No deberán utilizarse mocks para:

- reemplazar sistemáticamente la persistencia en pruebas que deban validar integración real;
- ocultar deficiencias de diseño o dependencias excesivas;
- simular de forma innecesaria comportamiento que puede validarse con componentes reales de bajo costo;
- o inflar artificialmente cobertura sin comprobar comportamiento real.

## Meta de cobertura de código

La cobertura de código se utilizará como señal auxiliar de salud de pruebas y no como único objetivo de calidad. No obstante, para este experimento se establece una meta explícita alta en los módulos críticos del backend.

### Objetivo de cobertura

- Módulos críticos de backend: entre 90% y 95% de cobertura objetivo.
- Componentes menos críticos o auxiliares: cobertura suficiente según valor real del componente.
- Funcionalidades de seguridad, validación o manejo sensible de datos: prioridad de cobertura reforzada.

La cobertura deberá observarse principalmente sobre:

- servicios de aplicación;
- validaciones;
- reglas de estado;
- orquestación del flujo principal;
- y transformaciones críticas del comportamiento esperado.

### Interpretación de la cobertura

Una cobertura alta se considerará valiosa solo si está asociada a pruebas significativas. No se considerará suficiente ejecutar líneas de código sin verificar comportamiento, bordes, errores y decisiones relevantes del flujo.

Por ello, la cobertura se analizará junto con:

- calidad de aserciones;
- variedad de escenarios;
- casos límite;
- manejo de errores;
- y coherencia con requisitos e historias de usuario.

## Separación operativa de suites de prueba

Las pruebas deberán poder separarse operativamente por tipo para facilitar ejecución rápida, depuración y uso dentro del flujo de desarrollo.

Como criterio general:

- las pruebas unitarias deben ejecutarse primero y con mayor frecuencia;
- las pruebas de integración deben poder ejecutarse por separado;
- y las pruebas amplias deben reservarse para momentos específicos de validación.

Esta separación busca mantener velocidad de feedback durante desarrollo por CLI y evitar que el costo total de validación vuelva lento el ciclo principal de trabajo.

## Trazabilidad entre requisitos, historias y pruebas

La estrategia de pruebas deberá mantener una trazabilidad ligera pero suficiente entre el origen funcional del sistema y su validación técnica. No se construirá una matriz documental excesiva en esta etapa, pero sí una relación explícita entre requisito, historia, criterio de aceptación y evidencia de prueba.

La lógica mínima de trazabilidad será la siguiente:

- problema o necesidad identificada;
- requisito funcional o no funcional asociado;
- historia de usuario correspondiente;
- criterio de aceptación verificable;
- tipo de prueba aplicable;
- evidencia o resultado obtenido.

Esta relación permitirá verificar que las pruebas no existan aisladas del propósito del sistema y que cada funcionalidad crítica cuente con respaldo observable de validación.

## Identificación mínima de pruebas

Cada prueba importante del proyecto deberá poder asociarse, como mínimo, a uno de los siguientes orígenes:

- un requisito funcional;
- un requisito no funcional;
- una historia de usuario;
- un criterio de aceptación;
- o una decisión técnica crítica del diseño del sistema.

No se considera aceptable construir suites extensas de pruebas sin vínculo claro con una necesidad real del sistema, salvo en los casos de utilidades técnicas generales claramente justificadas.

## Evidencias esperadas de validación

La validación del experimento deberá producir evidencia suficiente para demostrar no solo que se ejecutaron pruebas, sino que los resultados son interpretables y útiles para tomar decisiones.

Se consideran evidencias mínimas esperadas:

- resultados de ejecución de pruebas unitarias;
- resultados de ejecución de pruebas de integración;
- reporte de cobertura de código;
- registro de pruebas fallidas y corregidas cuando corresponda;
- evidencia de validación de flujos críticos;
- y observaciones relevantes sobre límites, riesgos o comportamientos detectados.

Cuando sea posible, estas evidencias deberán conservarse en formatos simples y fáciles de revisar dentro del entorno de desarrollo o del repositorio del proyecto.

## Definition of Done de pruebas

Una funcionalidad o incremento validado solo podrá considerarse suficientemente probado cuando cumpla, como mínimo, las siguientes condiciones:

- existe relación identificable con una necesidad funcional o técnica real;
- cuenta con pruebas adecuadas al nivel de riesgo del componente;
- las pruebas relevantes ejecutan y pasan de forma consistente;
- los criterios de aceptación aplicables han sido cubiertos de manera verificable;
- la cobertura objetivo del módulo crítico no se degrada sin justificación;
- los errores conocidos no bloquean el comportamiento principal del flujo;
- y la evidencia de validación está disponible para revisión.

Una funcionalidad no se considerará suficientemente validada solo porque compile, se ejecute una vez o muestre comportamiento aparentemente correcto en una prueba manual aislada.

## Riesgos principales de validación

La estrategia reconoce desde el inicio los siguientes riesgos principales:

- uso excesivo de mocks que reduzca realismo de validación;
- cobertura alta con pruebas débiles o poco significativas;
- pruebas lentas que deterioren el ciclo de feedback del desarrollo;
- acoplamiento excesivo entre pruebas e implementación interna;
- ambigüedad funcional que impida verificar criterios de aceptación;
- dependencia excesiva de validación manual no reproducible;
- y fragilidad de pruebas de integración si el entorno local no está bien controlado.

Estos riesgos deberán observarse durante la implementación y revisarse de forma retrospectiva para ajustar la estrategia cuando sea necesario.

## Criterio de transición hacia trazabilidad ligera

El proyecto podrá avanzar desde `04-estrategia-pruebas.md` hacia `05-trazabilidad-ligera.md` cuando la estrategia ya permita responder con claridad qué se probará, cómo se probará, con qué nivel de profundidad y con qué evidencia mínima se considerará aceptable la validación.

La transición será válida si se cumplen al menos las siguientes condiciones:

- la estrategia de pruebas está definida;
- los niveles de prueba están claros;
- la política de mocks está delimitada;
- existe un objetivo explícito de cobertura;
- la noción de evidencia ya está establecida;
- y la relación entre funcionalidad y validación puede expresarse de manera trazable.

## Cierre de la estrategia de pruebas

Con la información registrada en este documento, el proyecto cuenta con una estrategia de pruebas suficientemente definida para sostener la implementación y la validación del experimento. Se dispone de propósito, alcance, enfoque TDD-BDD, niveles de prueba, política de mocks, meta de cobertura, criterios de evidencia y definición básica de cierre de calidad.

En consecuencia, se considera razonable cerrar esta capa documental y utilizar este archivo como base para la construcción de una trazabilidad ligera, práctica y útil para el flujo real del proyecto.

# Trazabilidad ligera

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

| ID origen | Tipo | Descripción breve | Relación principal | Artefacto asociado | Prueba asociada | Evidencia | Estado |
|----------|------|-------------------|--------------------|--------------------|-----------------|-----------|--------|
| RF-01 | Requisito funcional | Registrar consulta inicial | HU-01 | DS-01 | TP-01 | EV-01 | Vigente |
| HU-01 | Historia de usuario | Registrar una consulta inicial | CA-01, CA-02 | DS-01 | TP-01, TP-02 | EV-01 | Vigente |
| RF-06 | Requisito funcional | Consultar disponibilidad de repuesto | HU-04 | DS-03 | TP-08 | EV-05 | Vigente |

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