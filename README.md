# Ecosistema Santi

Ecosistema Santi es una aplicación en Python para apoyar la coordinación entre conductor, taller y repuestos en el contexto de mantenimiento y reparación de mototaxis. Su objetivo es reducir la incertidumbre antes de desplazarse o iniciar una atención, mostrando si hay disponibilidad de atención, disponibilidad de repuesto, estado de la consulta y un historial básico de seguimiento.

## Qué problema resuelve

El proyecto ataca un problema operativo sencillo pero costoso: perder tiempo e ingresos por no saber con certeza si habrá atención, si existe el repuesto necesario o si una consulta ya fue confirmada. La aplicación centraliza esa información para que la decisión de ir, esperar o posponer sea más clara.

## Organización general

A alto nivel, el sistema se organiza en cuatro partes:

- lógica de dominio y servicios de aplicación, donde vive el comportamiento principal;
- persistencia local con SQLite, para guardar consultas, disponibilidades y respuestas;
- interfaz web y entrada por CLI, para operar el flujo principal;
- pruebas automatizadas, que validan reglas, persistencia y flujos de extremo a extremo.

## Validación actual

El proyecto cuenta con validación automatizada amplia. La evidencia disponible registra 124 tests aprobados y una cobertura de backend de 98.90%.

La suite incluye pruebas unitarias, de integración y E2E sobre los flujos principales del sistema.

## Estado del refactor

El refactor estructural ya avanzó desde un monolito inicial hacia una organización modular más clara. El backend, la persistencia, la capa web y los puntos de entrada quedaron separados por responsabilidades, con el objetivo de mantener el sistema más mantenible, testeable y fácil de ejecutar de forma local.

## Alcance

Este repositorio publica la base funcional del sistema y su validación técnica principal. No depende de servicios externos críticos para operar.
