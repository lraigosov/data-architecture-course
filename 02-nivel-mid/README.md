# Nivel Mid - Almacenamiento e Integración

## Objetivo del Nivel

Diseñar soluciones de almacenamiento e integración escalables (Data Warehouse, Data Lake, Lakehouse) y flujos ETL/ELT gobernados.

## Contenido Disponible (Real)

### 1. Almacenamiento e Integración de Datos
- Notebook: `01_almacenamiento_e_integracion.ipynb`
- Comparativa: Data Warehouse vs Data Lake vs Lakehouse
- Capas Medallion (Bronze / Silver / Gold)
- ETL vs ELT (criterios de elección)
- Estrategias de ingestión: batch, streaming, micro-batch, CDC
- Integración de fuentes heterogéneas (estructuradas, semiestructuradas, no estructuradas)
- Normalización / aplanado de JSON y construcción de tablas de hechos
- Ejercicio guiado de diseño (retail omnicanal)

## Próximos Módulos (Planificados)

Estos módulos aún no existen en el repositorio y se crearán posteriormente:
1. Arquitecturas orientadas a eventos y microservicios
2. Lambda vs Kappa (procesamiento batch + streaming)
3. Arquitecturas Cloud y Multi-Cloud (servicios comparados)
4. Diseño detallado de capas de datos (raw/curated/trusted/gold) y gobierno

## Proyecto del Nivel

**Diseño Arquitectónico Híbrido**

Diseñar una arquitectura completa que incluya:
1. Diagrama de almacenamiento (DW / Lake / Lakehouse) y flujo entre capas
2. Justificación de decisiones (costos, latencia, gobernanza)
3. Flujos de ingestión (batch/stream/CDC) y transformación (ETL/ELT)
4. Estrategias de calidad, observabilidad y seguridad

## Evaluación (Propuesta)

- Notebooks completados: 30%
- Casos de estudio: 30%
- Proyecto final: 40%
  - Diseño arquitectónico: 20%
  - Presentación oral: 20%

## Requisitos Previos

- Completar Nivel Junior
- Conocimientos básicos de SQL y modelado dimensional
- Familiaridad inicial con almacenamiento en la nube (deseable)

## Tiempo Estimado (Progresivo)

Duración total estimada al completar todos los módulos: 6–8 semanas.
Actualmente: 1 módulo disponible.

## Recursos Relacionados

- [Glosario](../04-recursos/glosario.md)
- [Referencias](../04-recursos/referencias.md)
- Casos de uso (retail) en `../04-recursos/casos-uso/`

## Estado

✅ Módulo 1 disponible  
⏳ Módulos adicionales pendientes de creación

## Proyecto del Nivel

**Diseño Arquitectónico Híbrido**

Diseñar una arquitectura completa que incluya:
1. Diagramas de arquitectura (capas y componentes)
2. Justificación de decisiones técnicas
3. Flujos de datos end-to-end
4. Consideraciones de escalabilidad y seguridad

## Evaluación

- **Notebooks completados:** 30%
- **Casos de estudio:** 30%
- **Proyecto final:** 40%
  - Diseño arquitectónico: 20%
  - Presentación oral: 20%

Ver detalles en: [Evaluación Nivel Mid](../05-evaluaciones/mid/)

## Requisitos Previos

- Completar Nivel Junior
- Conocimientos de sistemas distribuidos (recomendado)
- Familiaridad con conceptos cloud (básico)

## Tiempo Estimado

**Duración total:** 6-8 semanas (30-35 horas de estudio)

## Recursos Adicionales

- [Casos de uso](../04-recursos/casos-uso/)
- [Patrones de arquitectura](../04-recursos/patrones/)
- [Referencias cloud](../04-recursos/referencias-cloud.md)
