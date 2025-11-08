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

### 2. Procesamiento por Lotes y en Tiempo Real + Data Mesh
- Notebook: `02_procesamiento_batch_streaming_y_data_mesh.ipynb`
- Diferencias batch vs streaming y latencia
- Arquitecturas Lambda vs Kappa (impacto en diseño)
- Principios de Data Mesh (dominios, datos como producto, self-serve, gobernanza)
- Gestión de eventos: ventanas, watermarks, idempotencia, delivery semantics
- Orquestación y observabilidad (lag, throughput, SLOs)

### 3. Lambda/Kappa Avanzado y Contratos de Datos
- Notebook: `03_lambda_kappa_event_driven.ipynb`
- Profundización en patrones Lambda vs Kappa (reprocesos históricos)
- Flujo CDC→Kafka→Procesamiento→Silver/Gold y SLOs (latencia/frescura)
- Versionado de esquemas y compatibilidad (backward/forward)
- Observabilidad (lag, P95, error rate) y alertas
- Contrato de datos ejemplo: `../04-recursos/contratos-datos/ejemplo_contrato_dominio_pagos.yaml`

### 4. Calidad de Datos y Backfill
- Notebook: `04_calidad_y_backfill.ipynb`
- Validaciones: nulos, duplicados, rangos y suite de calidad
- Aserciones reutilizables (patrón simple en Pandas)
- Estrategias de backfill (incremental, shadow, completo)
- Impacto en costo y SLAs; plan de reproceso controlado
- Contrato BI Gold ejemplo: `../04-recursos/contratos-datos/contrato_bi_gold_kpi_ventas.yaml`

### 5. Metadatos, Catálogo y Linaje de Datos
- Notebook: `05_metadatos_catalogo_linaje.ipynb`
- Tipos de metadatos: técnicos, de negocio, operacionales
- Catálogo de datos: descubrimiento, documentación, gobernanza
- Data lineage (linaje): table-level y column-level
- Usos: auditoría, análisis de impacto, cumplimiento (trazabilidad de PII)
- Herramientas: OpenLineage, Apache Atlas, Amundsen, DataHub, dbt lineage
- Integración catálogo + linaje + calidad

### 6. Implementación de Controles de Seguridad
- Notebook: `06_implementacion_controles_seguridad.ipynb`
- Control de acceso: RBAC (Role-Based) vs ABAC (Attribute-Based) con ejemplos de código
- Encriptación: at-rest (TDE, KMS) e in-transit (TLS/mTLS)
- Auditoría y logging: qué auditar, formato de logs, retención y protección
- Anonimización y masking dinámico: técnicas (supresión, generalización, tokenización, DDM)
- Ejercicio integrador: diseñar controles para dataset con PII

### 7. Optimización, Dimensionamiento y FinOps
- Notebook: `07_optimizacion_dimensionamiento_finops.ipynb`
- Dimensionamiento detallado según 3 V (Volumen, Velocidad, Variedad)
- Calculadora avanzada de recursos: storage (hot/cold), compute (vCPUs, RAM), network (ancho de banda)
- Técnicas de optimización: particionamiento, clustering/Z-ordering, compresión (Parquet), materialized views
- FinOps (Financial Operations): tagging, presupuestos, alertas, chargeback vs showback
- Modelos de costo multi-cloud: AWS vs Azure vs GCP (comparación detallada)
- Cost anomaly detection con código
- Observabilidad: métricas de rendimiento, calidad y costo con dashboards
- Ejercicio integrador: plataforma de streaming con dimensionamiento y optimización

### 8. Patrones de Arquitectura de Datos
- Notebook: `08_patrones_arquitectura_datos.ipynb`
- Data Bus: comunicación desacoplada entre sistemas (Kafka, Kinesis, Event Hub, Pub/Sub)
- Microservicios de datos: bounded contexts, ownership, API-first, autonomía
- Event-Driven Architecture detallada: Event Sourcing, CQRS, garantías de entrega
- Patrones de interoperabilidad: contratos de datos (schemas, SLAs, consumers)
- Data as a Product: principios, customer 360 como ejemplo
- Código: simulador de DataBus pub/sub, microservicios con orquestación
- Ejercicio integrador: plataforma de streaming con 100M usuarios

### 9. Modelado Semántico y Ontologías Empresariales
- Notebook: `09_modelado_semantico_ontologias_kg.ipynb`
- RDF/RDFS/OWL: clases, propiedades, dominio/rango y restricciones básicas
- SPARQL: consultas sobre grafo para responder preguntas de negocio
- SKOS: modelado de taxonomías (broader/narrower/related) y clasificación
- Mapeo de contratos de datos a IRIs (semántica explícita entre datasets)
- Integración hacia Knowledge Graph (Customer 360, recomendaciones, compliance)
- Ejercicio: añadir canales de compra y consulta agregada por canal

### 10. Gobernanza de Metadatos Semánticos y Knowledge Graphs (Aplicado)
- Notebook: `10_gobernanza_metadatos_semanticos_y_kg.ipynb`
- Modelo de grafo para discovery/reutilización: Dataset/Table/Column/Concept/Domain/DataProduct/KPI
- SPARQL para descubrir datasets por concepto/KPI y detectar PII
- Validación mínima de metadatos (título, dominio) como paso hacia SHACL en CI/CD
- Integración con catálogo y contratos de datos (facetas semánticas, API de búsqueda)
- Ejercicio: extender grafo con KPI Churn y reglas de validación por dominio

### 11. Arquitecturas Cloud y Multi-Cloud (Aplicado)
- Notebook: `11_arquitecturas_cloud_y_multi_cloud.ipynb`
- Patrones single-cloud: plataforma consolidada y lakehouse administrado
- Patrones multi-cloud: replicación activa, especialización, abstracción por capa, data exchange
- Ventajas vs retos: resiliencia, costos, complejidad operativa, egress, gobernanza
- Simulador de costos multi-cloud (storage, compute, egress, distribución workloads)
- Estrategias de optimización: locality, compresión, caching selectivo, acuerdos comerciales
- Migración por fases y matriz de riesgos/mitigaciones

### 12. Diagramas de Componentes y Flujos de Datos (Aplicado)
- Notebook: `12_diagramas_componentes_flujos_datos.ipynb`
- C4 Model: 4 niveles de abstracción (Context, Containers, Components, Code)
- Flujos end-to-end con swimlanes y sequence diagrams
- Wireframes de arquitectura para diseño iterativo
- Generación de diagramas con código Mermaid (versionables en Git)
- Integración con catálogo y lineage para trazabilidad visual
- Ejercicio: C4 Nivel 2 para lakehouse con anotaciones de latencia

### 13. Arquitectura Habilitadora de Cultura Data-Driven (Aplicado)
- Notebook: `13_arquitectura_habilitadora_cultura_data_driven.ipynb`
- Conexión entre arquitectura y cultura: self-service, descubrimiento, confianza
- Plataformas self-service: catálogo, query builder, sandboxes, queries certificadas
- Catálogo de datos: búsqueda semántica, lineage visual, colaboración
- Código: simulador de catálogo con búsqueda, datasets más usados, alertas de frescura
- Contratos de datos: schema, SLAs, calidad, versionado para generar confianza
- Métricas de adopción: engagement, self-service ratio, time-to-insight, trust score
- Código: evaluador de madurez de adopción con 4 dimensiones
- Patrones anti-pattern a evitar (data swamp, shadow IT, documentation drift)

### 14. Observabilidad y Evolución de Arquitectura (Aplicado)
- Notebook: `14_observabilidad_evolucion_arquitectura.ipynb`
- Stack completo de observabilidad: Prometheus/Grafana (métricas), ELK (logs), Jaeger (tracing)
- Golden Signals adaptados a datos: Latency, Throughput, Errors, Saturation
- Métricas operacionales: data freshness, completeness, schema drift, query performance
- Código: sistema de monitoreo de pipelines con alertas automatizadas
- Gestión de deuda técnica: medición (complexity, coverage, TODOs), priorización (impacto/esfuerzo)
- Estrategias de refactoring seguro: Strangler Fig, Blue-Green, Feature Flags, Expand-Contract
- Versionado de schemas con Schema Registry (backward/forward compatibility)
- Código: simulador de versionado con validación de compatibilidad
- Planificación de evolución incremental con roadmap trimestral

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
Actualmente: 4 módulos disponibles.

## Recursos Relacionados

- [Glosario](../04-recursos/glosario.md)
- [Referencias](../04-recursos/referencias.md)
- Casos de uso (retail) en `../04-recursos/casos-uso/`

### 15. Arquitectura AI-Ready: Feature Stores y Streaming para ML
- Notebook: `15_arquitectura_ai_ready_feature_stores_streaming.ipynb`
- Arquitectura por capas para ML: ingesta → procesamiento → Feature Store → training/inference
- Feature Store detallado: arquitectura dual (offline/online) con código completo
- Diferencias tecnológicas: Hive/Delta Lake vs Redis/DynamoDB
- Pipeline de features: batch jobs + stream processing con sincronización
- Integración de datos multimodales: estructurados + texto + imágenes + video
- Pipeline multimodal: procesamiento de cada tipo y combinación de features
- Caso práctico completo: sistema de recomendación en streaming
- Stream processor con ventanas temporales y agregaciones (5 minutos)
- Router multi-modelo con estrategias A/B, canary y shadow mode
- Arquitectura event-driven para ML: desacoplamiento y escalabilidad
- Stack tecnológico recomendado por componente (ingesta, procesamiento, serving)
- Checklist de diseño: datos, feature engineering, entrenamiento, inferencia, monitoreo, gobernanza

### 16. Frameworks y Ecosistemas de Big Data de Última Generación (Comparativo)
- Notebook: `16_frameworks_big_data_modernos_comparativo.ipynb`
- Comparativa práctica: Spark vs Flink vs Ray vs Dask (latencia, throughput, facilidad de uso)
- Almacenamiento y formatos modernos: Parquet, Delta Lake, Iceberg, Hudi (tabla comparativa)
- NoSQL según caso de uso: document, wide-column, key-value, time-series (mapeo de decisiones)
- Fundamentos de Vector DBs: embeddings, ANN, índices (HNSW/IVF/Flat) y casos de búsqueda semántica
- Metodología de performance: dataset sintético, tiempos, recursos, costo por job
- Código base de benchmark: esqueleto para comparar jobs clásicos vs estructurados
- Resultados esperados y lectura de perfiles (CPU/memoria/IO)

### 17. Mini Data Mesh de Dos Dominios y Catálogo Semántico Compartido
- Notebook: `17_mini_data_mesh_dos_dominios_catalogo_compartido.ipynb`
- Diseño lógico de dos dominios (Ventas y Marketing) y sus data products
- Contratos de datos: esquema, SLA frescura, reglas de calidad, semántica
- Catálogo compartido con búsqueda por texto, tags y concepto semántico
- Interoperabilidad mediante glosario y capa semántica ligera
- Ejemplo de KPI compuesto (ROAS) y validación de calidad básica
- Próximos pasos: extender a policy-as-code, catálogo real y registry de productos

### 18. Observabilidad, Metadata y Linaje para IA/Big Data (Simulación)
- Notebook: `18_observabilidad_metadata_linaje_ia_bigdata_simulacion.ipynb`
- Métricas clave: freshness, error-rate, throughput; logs y alertas por umbral
- Modelo de linaje (table/column-level simplificado) y análisis de impacto
- Evento de cambio de esquema con reporte de datasets afectados
- Propagación de retrasos de frescura a consumidores downstream
- Reporte de gobernanza con recomendaciones y próximos pasos

### 19. Streaming + Inferencia en Tiempo Real (Caso Práctico)
- Notebook: `19_streaming_inferencia_tiempo_real_caso_practico.ipynb`
- Flujo completo: ingesta → feature store en memoria → inferencia online → sink de resultados
- Medición de latencias y throughput (P50/P95)
- Modelo dummy/logístico con umbral y tasa de alertas
- Extensiones: Kafka/Pulsar, Feature Store online, endpoint de inferencia, router de tráfico

## Estado
✅ Módulos 1–19 disponibles  
⏳ Más módulos por venir (iteraciones y profundizaciones)

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
