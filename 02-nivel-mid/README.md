# Nivel Mid - Arquitecturas de Datos Aplicadas

## Objetivo del Nivel

Diseñar arquitecturas de datos escalables y gobernadas, combinando almacenamiento, integración, procesamiento batch/streaming, seguridad, observabilidad, FinOps y preparación para casos de IA.

Este nivel toma los fundamentos del nivel Junior y los lleva a decisiones de arquitectura: qué patrón conviene, qué compromisos acepta el diseño y qué controles son necesarios para operar la solución con confianza.

## Ruta Recomendada

### Bloque 1 - Fundamentos de plataforma
- `01_almacenamiento_e_integracion.ipynb`: Data Warehouse, Data Lake, Lakehouse, capas Medallion, ETL/ELT e ingestión batch, streaming y CDC.
- `02_procesamiento_batch_streaming_y_data_mesh.ipynb`: criterios para batch y streaming, Lambda/Kappa, eventos, ventanas, watermarks, idempotencia y SLOs.
- `03_lambda_kappa_event_driven.ipynb`: reprocesos, versionado de esquemas, compatibilidad y contratos de datos.
- `04_calidad_y_backfill.ipynb`: validaciones, aserciones reutilizables y estrategias de backfill.

### Bloque 2 - Gobierno operativo
- `05_metadatos_catalogo_linaje.ipynb`: metadatos técnicos, de negocio y operacionales; catálogo, linaje e impacto de cambios.
- `06_implementacion_controles_seguridad.ipynb`: RBAC, ABAC, cifrado, auditoría, masking y protección de datos sensibles.
- `07_optimizacion_dimensionamiento_finops.ipynb`: dimensionamiento, particionamiento, compresión, presupuestos, alertas y anomalías de costo.
- `08_patrones_arquitectura_datos.ipynb`: data bus, event-driven architecture, microservicios de datos, CQRS, contratos y datos como producto.

### Bloque 3 - Semántica, nube y comunicación
- `09_modelado_semantico_ontologias_kg.ipynb`: RDF, RDFS, OWL, SPARQL, SKOS y mapeo semántico de contratos.
- `10_gobernanza_metadatos_semanticos_y_kg.ipynb`: discovery, reutilización, Knowledge Graph y validación mínima de metadatos.
- `11_arquitecturas_cloud_y_multi_cloud.ipynb`: patrones single-cloud y multi-cloud, egress, resiliencia, riesgos y migración por fases.
- `12_diagramas_componentes_flujos_datos.ipynb`: C4 Model, flujos end-to-end, Mermaid y diagramas versionables.
- `13_arquitectura_habilitadora_cultura_data_driven.ipynb`: self-service, catálogos, contratos, métricas de adopción y confianza.
- `14_observabilidad_evolucion_arquitectura.ipynb`: golden signals, freshness, completeness, schema drift, deuda técnica y evolución incremental.

### Bloque 4 - Arquitecturas AI-ready
- `15_arquitectura_ai_ready_feature_stores_streaming.ipynb`: Feature Store offline/online, entrenamiento, inferencia y serving de features.
- `16_frameworks_big_data_modernos_comparativo.ipynb`: Spark, Flink, Ray, Dask, Parquet, Delta Lake, Iceberg, Hudi y bases vectoriales.
- `17_mini_data_mesh_dos_dominios_catalogo_compartido.ipynb`: data products, ownership, catálogo compartido y semántica ligera.
- `18_observabilidad_metadata_linaje_ia_bigdata_simulacion.ipynb`: freshness, error rate, throughput, linaje e impacto de cambios.
- `19_streaming_inferencia_tiempo_real_caso_practico.ipynb`: feature store en memoria, inferencia online, latencia y throughput.
- `20_vector_search_embeddings_similitud.ipynb`: embeddings, similitud coseno, top-k, re-ranking y límites de búsqueda exacta.
- `21_vector_search_faiss_vs_bruteforce.ipynb`: FAISS, producto interno con vectores normalizados, recall@K y benchmark frente a NumPy.

## Entregable del Nivel

El entregable central es un **diseño arquitectónico híbrido** para un caso de negocio. Debe incluir:

1. Diagrama de capas, componentes y flujos de datos.
2. Justificación de decisiones: latencia, costo, seguridad, gobierno y complejidad operativa.
3. Estrategia de ingestión y procesamiento: batch, streaming, CDC o combinación.
4. Contratos de datos, reglas de calidad y plan de backfill.
5. Metadatos, catálogo, linaje y responsables.
6. Controles de seguridad, privacidad y auditoría.
7. Observabilidad, SLOs y runbooks básicos.
8. Estimación FinOps y criterios de optimización.

## Evaluación

- Notebooks y ejercicios: 30%
- Caso de estudio aplicado: 30%
- Proyecto final: 40%

La revisión debe apoyarse en el checklist transversal: [`../docs/checklist_revision_arquitectura.md`](../docs/checklist_revision_arquitectura.md).

## Requisitos Previos

- Haber completado el nivel Junior o contar con experiencia equivalente.
- Entender SQL, modelado dimensional y conceptos básicos de cloud.
- Poder leer notebooks de Python y adaptar ejemplos sencillos.

## Tiempo Estimado

Duración orientativa: 6-8 semanas, con una dedicación sugerida de 30-35 horas en total. La profundidad puede ajustarse si el curso se dicta como bootcamp, módulo universitario o capacitación corporativa.

## Recursos Relacionados

- [Glosario](../04-recursos/glosario.md)
- [Referencias](../04-recursos/referencias.md)
- [Casos de uso](../04-recursos/casos-uso/)
- [Contratos de datos](../04-recursos/contratos-datos/)
- [Mejores prácticas](../docs/mejores_practicas_arquitectura_datos.md)
