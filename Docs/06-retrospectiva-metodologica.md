# Retrospectiva metodológica

## Propósito del documento

Este documento define el enfoque retrospectivo del experimento metodológico aplicado al proyecto. Su finalidad es evaluar, de manera estructurada, si el flujo de trabajo basado en TDD-BDD-SDD y asistido por CLI produjo un desarrollo más claro, más controlado, más rápido y suficientemente validado en comparación con un enfoque menos guiado.

La retrospectiva no busca únicamente registrar impresiones subjetivas sobre el proceso. Su objetivo principal es determinar si la metodología adoptada aportó valor real al desarrollo, identificar qué partes funcionaron, qué partes generaron fricción y qué ajustes deben realizarse para siguientes iteraciones.

## Objeto de evaluación

El objeto de esta retrospectiva no es solamente la aplicación construida, sino el modo en que fue concebida, documentada, implementada y validada. En consecuencia, la evaluación se centrará en la interacción entre:

- gobierno metodológico inicial;
- definición funcional;
- diseño del sistema;
- estrategia de pruebas;
- trazabilidad ligera;
- guía operativa de uso de CLI;
- y ejecución real del trabajo técnico durante el experimento.

La pregunta central que este documento busca responder es la siguiente:

¿El uso de una estructura documental guiada, combinada con TDD-BDD-SDD y soporte de CLI asistida por IA, mejoró de forma observable la calidad del desarrollo sin introducir una carga excesiva de proceso?

## Alcance de la retrospectiva

La retrospectiva abarcará tanto aspectos metodológicos como operativos. No se limitará a medir si el código funciona, sino también si el flujo de trabajo fue sostenible, entendible, útil y compatible con el objetivo de acelerar desarrollo sin perder control.

El alcance incluye:

- claridad de los documentos generados;
- utilidad real del contexto documental para la CLI;
- calidad de delimitación funcional y técnica;
- efectividad de la estrategia de pruebas;
- valor práctico de la trazabilidad ligera;
- eficiencia del flujo de trabajo por sesiones;
- y grado de correspondencia entre lo definido y lo efectivamente construido.

Quedan fuera de esta retrospectiva comparaciones exhaustivas con marcos empresariales completos, validaciones organizacionales amplias o análisis de productividad a escala de múltiples equipos.

## Principios rectores de la retrospectiva

La evaluación retrospectiva del experimento deberá regirse por los siguientes principios:

- analizar el proceso y no buscar culpables;
- combinar percepción cualitativa con evidencia observable;
- evaluar utilidad real y no solo cumplimiento documental;
- distinguir entre complejidad necesaria y fricción evitable;
- identificar patrones repetidos y no incidentes aislados;
- y traducir hallazgos en decisiones o ajustes concretos.

La retrospectiva solo será útil si permite aprender del experimento y rediseñar mejor el flujo futuro del proyecto.

## Hipótesis metodológica a revisar

La retrospectiva se apoyará en una hipótesis principal de trabajo:

Una estructura documental ligera pero bien secuenciada, unida a una estrategia de desarrollo basada en TDD-BDD-SDD y ejecutada con apoyo de CLI asistida por IA, puede mejorar orientación, trazabilidad, calidad y velocidad de desarrollo en comparación con un flujo menos estructurado.

A partir de esta hipótesis principal, la retrospectiva podrá revisar subhipótesis como las siguientes:

- la documentación previa redujo ambigüedad durante la implementación;
- la CLI trabajó mejor cuando existió contexto bien delimitado;
- la estrategia de pruebas ayudó a sostener la calidad sin frenar en exceso;
- la trazabilidad ligera fue suficiente sin volverse burocrática;
- y la secuencia de capas redujo decisiones prematuras o retrabajo.

## Valor esperado del documento

Este documento deberá permitir tomar decisiones sobre continuidad metodológica. Su función no es solo describir qué ocurrió, sino ofrecer base para decidir si el enfoque debe:

- mantenerse;
- ajustarse;
- simplificarse;
- reforzarse en algunos puntos;
- o reemplazarse parcialmente en iteraciones futuras.

En ese sentido, la retrospectiva forma parte del propio experimento y no un documento accesorio posterior.

## Dimensiones de evaluación retrospectiva

La retrospectiva metodológica del experimento se organizará en dimensiones de evaluación claramente diferenciadas. Esto permitirá analizar el proceso con mayor precisión y evitar conclusiones vagas o demasiado generales.

Como base inicial, se adoptan las siguientes dimensiones:

### 1. Claridad metodológica

Evalúa si la secuencia documental y metodológica ayudó a comprender qué hacer, en qué orden hacerlo y bajo qué criterios avanzar o detenerse.

### 2. Eficiencia operativa

Evalúa si el flujo apoyado por CLI permitió avanzar con menor fricción, menor retrabajo y mejor continuidad entre sesiones.

### 3. Calidad funcional y técnica

Evalúa si la solución construida mantuvo coherencia con requisitos, diseño, pruebas y comportamiento esperado.

### 4. Efectividad de validación

Evalúa si la estrategia de pruebas, cobertura y evidencia fue suficiente para sostener confianza razonable en el resultado.

### 5. Utilidad del contexto documental

Evalúa si los documentos producidos realmente orientaron el trabajo de la CLI y del operador, o si se transformaron en carga documental de bajo valor.

### 6. Valor de la trazabilidad ligera

Evalúa si el modelo de trazabilidad fue suficiente para entender relaciones entre problema, requisitos, historias, pruebas y evidencia sin volverse burocrático.

## Métricas cualitativas de evaluación

La retrospectiva deberá apoyarse en observaciones cualitativas estructuradas para capturar utilidad real, fricción percibida y comportamiento del proceso que no siempre se refleja en métricas numéricas.

Como criterios cualitativos iniciales, deberán observarse al menos los siguientes aspectos:

- nivel de claridad al iniciar una sesión de trabajo;
- facilidad para delimitar tareas pequeñas;
- facilidad para retomar trabajo entre sesiones;
- percepción de utilidad real de los documentos base;
- percepción de control sobre alcance y decisiones;
- nivel de confianza en los cambios realizados;
- y grado de carga o fricción introducida por la metodología.

Estas observaciones deberán registrarse con lenguaje claro, comparando lo esperado con lo realmente experimentado durante el desarrollo.

## Métricas cuantitativas de evaluación

Además de la lectura cualitativa, la retrospectiva deberá incorporar métricas cuantitativas simples que permitan observar señales objetivas del comportamiento del proceso.

Se consideran métricas cuantitativas iniciales apropiadas para este experimento:

- número de sesiones necesarias para completar una funcionalidad relevante;
- cantidad de retrabajos detectados por mala definición previa;
- número de cambios corregidos por pruebas fallidas;
- cobertura de código alcanzada en módulos críticos;
- cantidad de pruebas unitarias y de integración ejecutadas;
- cantidad de bloques o sesiones detenidas por ambigüedad funcional o técnica;
- número de cambios que requirieron ampliación inesperada del contexto;
- y proporción entre sesiones completadas y sesiones parciales o bloqueadas.

Estas métricas no deberán interpretarse de manera aislada. Su valor principal estará en relación con el contexto del experimento y con las observaciones cualitativas que ayuden a explicar sus causas.

## Preguntas guía de la retrospectiva

La retrospectiva deberá responder de forma estructurada un conjunto de preguntas guía. Estas preguntas no pretenden agotar todo el análisis, pero sí asegurar una lectura consistente del experimento.

### Sobre claridad metodológica

- ¿La secuencia documental ayudó a saber qué hacer antes de implementar?
- ¿Las capas definidas evitaron decisiones prematuras?
- ¿Hubo documentos que orientaron claramente y otros que aportaron poco valor?

### Sobre eficiencia operativa

- ¿La CLI trabajó mejor cuando el contexto estuvo bien delimitado?
- ¿Las sesiones pequeñas facilitaron continuidad y validación?
- ¿La metodología aceleró el trabajo o introdujo fricción excesiva?

### Sobre calidad y validación

- ¿Las pruebas ayudaron a detectar errores relevantes?
- ¿La cobertura obtenida fue útil o solo aparente?
- ¿Los mocks se usaron con criterio o redujeron realismo de validación?

### Sobre trazabilidad y documentación

- ¿La trazabilidad ligera fue suficiente para entender relaciones importantes?
- ¿Los documentos facilitaron retomar decisiones y justificar cambios?
- ¿Se produjo sobrecarga documental en algún punto del experimento?

### Sobre continuidad futura

- ¿Qué partes de la metodología deberían mantenerse?
- ¿Qué partes deberían simplificarse o ajustarse?
- ¿Qué prácticas demostraron mayor retorno real para el desarrollo?

## Evidencias a revisar en la retrospectiva

La retrospectiva no deberá apoyarse únicamente en memoria o percepción general. Siempre que sea posible, deberá revisar evidencias observables del trabajo realizado.

Como base de revisión, deberán considerarse al menos las siguientes evidencias:

- documentos del proyecto generados durante el experimento;
- historial de sesiones o resultados operativos de la CLI;
- pruebas creadas y resultados de ejecución;
- reportes de cobertura;
- cambios relevantes en código o documentación;
- registros de bloqueos, dudas o reformulaciones;
- y observaciones acumuladas durante implementación y validación.

La calidad de la retrospectiva dependerá en parte de la calidad de estas evidencias y de la honestidad con que sean interpretadas.

## Regla de interpretación de hallazgos

Todo hallazgo retrospectivo deberá interpretarse con criterio causal y no solo descriptivo. No basta con afirmar que algo fue lento, útil o confuso; deberá intentarse explicar por qué ocurrió, en qué condiciones apareció y si se trató de un patrón o de un evento aislado.

Como regla general, cada hallazgo relevante debería intentar responder:

- qué ocurrió;
- por qué ocurrió;
- qué impacto tuvo;
- y qué decisión futura sugiere.

## Criterio de equilibrio entre datos y juicio

La retrospectiva combinará datos observables y juicio experto del operador. Ninguna métrica por sí sola será suficiente para decidir continuidad metodológica, pero tampoco se aceptará una evaluación puramente subjetiva sin evidencia mínima.

El equilibrio buscado será el siguiente:

- los datos orientan;
- la experiencia interpreta;
- y las decisiones de ajuste se toman a partir de ambos.


## Formato de registro retrospectivo

Para mantener consistencia entre iteraciones, la retrospectiva deberá registrarse con una estructura breve pero suficientemente analítica. Cada ciclo retrospectivo del experimento debería documentar, como mínimo, los siguientes elementos:

- período o tramo evaluado;
- objetivo del tramo revisado;
- evidencias consideradas;
- hallazgos positivos;
- fricciones o problemas observados;
- causas probables;
- impacto sobre velocidad, claridad o calidad;
- decisiones de ajuste;
- y acciones concretas para la siguiente iteración.

Este formato busca evitar retrospectivas vagas o puramente narrativas. La intención es dejar un rastro claro de aprendizaje metodológico acumulado.

## Escala simple de evaluación

Para facilitar interpretación y comparación entre dimensiones, se utilizará una escala simple de evaluación cualitativa con cinco niveles:

- muy bajo;
- bajo;
- medio;
- bueno;
- y muy bueno.

Esta escala podrá aplicarse a dimensiones como claridad metodológica, utilidad documental, eficiencia operativa, calidad de validación y valor de la trazabilidad. Su propósito no es producir precisión matemática artificial, sino permitir una lectura comparativa suficientemente clara entre componentes del experimento.

Como criterio orientador:

- muy bajo: aporta poco valor o genera fricción importante;
- bajo: aporta valor limitado y requiere rediseño claro;
- medio: cumple de forma parcial, con utilidad irregular;
- bueno: aporta valor consistente con fricción manejable;
- muy bueno: aporta valor alto, estable y claramente reutilizable.

## Plantilla de valoración por dimensión

Cada dimensión retrospectiva podrá registrarse con una plantilla breve como la siguiente:

### Dimensión evaluada

Nombre de la dimensión.

### Valoración

Muy bajo, bajo, medio, bueno o muy bueno.

### Evidencia observada

Descripción breve de hechos, sesiones, resultados o patrones que justifican la valoración.

### Interpretación

Explicación de por qué la dimensión obtuvo esa valoración y qué relación guarda con el comportamiento real del experimento.

### Ajuste sugerido

Decisión práctica para mantener, corregir, simplificar o reforzar la dimensión evaluada.

Esta plantilla permitirá comparar dimensiones sin perder trazabilidad argumentativa.

## Acciones de mejora derivadas

Todo resultado retrospectivo relevante deberá traducirse en acciones de mejora concretas. No bastará con identificar problemas o virtudes; será necesario convertirlos en decisiones operativas para el siguiente ciclo de trabajo.

Las acciones de mejora deberán cumplir, en la medida de lo posible, con los siguientes criterios:

- ser específicas;
- ser ejecutables;
- tener relación directa con un hallazgo;
- evitar soluciones excesivamente abstractas;
- y poder verificarse en una iteración posterior.

Como regla práctica, una retrospectiva útil debería producir pocas acciones, pero claramente priorizadas. Un exceso de acciones diluye el aprendizaje y dificulta su aplicación real.

## Priorización de acciones

Las acciones derivadas de la retrospectiva deberán priorizarse según dos variables principales:

- impacto esperado sobre el proceso;
- y costo o dificultad de implementación.

Con base en ello, podrán clasificarse de forma simple como:

- acción prioritaria inmediata;
- acción importante de siguiente iteración;
- acción deseable pero no urgente;
- o acción a observar antes de intervenir.

Esta priorización ayuda a evitar que la retrospectiva se convierta en una lista extensa de intenciones sin ejecución real.

## Criterio de conclusión del experimento

La retrospectiva metodológica deberá permitir emitir un juicio razonado sobre el experimento. Ese juicio no necesita ser absoluto, pero sí suficientemente claro para orientar la continuidad del enfoque.

Como criterio general, el experimento podrá considerarse metodológicamente favorable si la evidencia muestra, de forma acumulada, que:

- la estructura documental redujo ambigüedad relevante;
- la CLI trabajó mejor con el contexto definido;
- la estrategia de pruebas sostuvo confianza razonable;
- la trazabilidad ligera fue útil sin exceso burocrático;
- y el costo metodológico adicional fue aceptable frente al valor obtenido.

En cambio, el experimento deberá considerarse metodológicamente débil o necesitado de rediseño si la evidencia muestra que:

- la documentación aportó poco valor práctico;
- la metodología introdujo fricción excesiva;
- la CLI no obtuvo mejora clara por disponer de contexto;
- la validación fue insuficiente pese al esfuerzo invertido;
- o la estructura general produjo más carga que aprendizaje.

## Posibles decisiones posteriores

A partir de la conclusión retrospectiva, el proyecto podrá adoptar una o varias de las siguientes decisiones:

- mantener la metodología actual con ajustes menores;
- simplificar algunas capas documentales;
- reforzar la estrategia de pruebas;
- redefinir la guía operativa de sesiones CLI;
- acotar mejor el uso de trazabilidad;
- o rediseñar parcialmente el flujo metodológico para futuras iteraciones.

Estas decisiones deberán surgir de la evidencia reunida y no de preferencia intuitiva aislada.

## Frecuencia de aplicación retrospectiva

La retrospectiva metodológica no necesita ejecutarse únicamente al final total del proyecto. También puede aplicarse al cierre de hitos, incrementos relevantes o bloques de trabajo suficientemente representativos.

Como criterio práctico, conviene realizar retrospectivas cuando exista material suficiente para evaluar patrones, pero antes de que el aprendizaje se pierda por distancia temporal. Esto favorece ajustes tempranos y evita repetir fricciones ya identificadas.

## Limitaciones de la retrospectiva

Toda retrospectiva tiene límites y este documento debe reconocerlos expresamente. La evaluación metodológica puede verse afectada por factores como el tamaño del proyecto, la experiencia del operador, la calidad variable de los prompts, la naturaleza de la funcionalidad desarrollada o las restricciones del entorno técnico.

Por ello, las conclusiones de esta retrospectiva deberán interpretarse como evidencia contextual del experimento y no como prueba universal de superioridad metodológica aplicable a cualquier proyecto.

## Cierre del documento

Con el contenido desarrollado en este archivo, el proyecto dispone de un marco suficiente para evaluar de manera ordenada el experimento metodológico aplicado. Se han definido propósito, objeto de evaluación, alcance, hipótesis, dimensiones, métricas, preguntas guía, evidencias, formato de registro, escala de valoración, acciones de mejora y criterios de conclusión.

En consecuencia, `07-retrospectiva-metodologica.md` puede considerarse cerrado como documento base para revisar críticamente la utilidad real del enfoque TDD-BDD-SDD asistido por CLI dentro del proyecto.