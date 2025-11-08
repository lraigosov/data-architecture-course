# Mejores Prácticas de Arquitectura de Datos

Esta guía resume prácticas ampliamente aceptadas en la industria para diseñar, operar y gobernar plataformas de datos. Está alineada con DAMA-DMBOK, DataOps/MLOps, principios FAIR y marcos de observabilidad/FinOps. Usa esta guía como referencia transversal a los niveles Junior, Mid y Senior.

> Nota: Consulta los enlaces oficiales en `04-recursos/referencias.md` para profundizar (Kafka, Flink/Spark, Delta/Iceberg/Hudi, OpenLineage, DataHub, Great Expectations, Feast, FAISS, etc.).

## 1. Modelado y Contratos de Datos
- Diseña primero el modelo conceptual (negocio/KPIs) → lógico → físico. Mantén trazabilidad.
- Usa contratos de datos versionados (schema + SLAs + calidad + owner). Evita breaking changes sin plan de compatibilidad.
- Gestiona compatibilidad de esquemas: backward-compatible por defecto; documenta cambios breaking y plan de migración (expand-contract).
- Evita duplicidades: Single Source of Truth (SSOT) y catálogo actualizado.

## 2. Almacenamiento y Formatos
- Elige lakehouse transaccional (Delta/Iceberg/Hudi) cuando necesites ACID en data lake y evolución de esquemas.
- Estandariza en formatos columnares (Parquet/ORC) con compresión y tamaños de archivo consistentes (e.g., 128–512 MB) para scans eficientes.
- Define capas claras (Bronze/Silver/Gold) y políticas de retención (hot/warm/cold).

## 3. Procesamiento (Batch/Streaming)
- Selecciona batch/streaming según objetivos de latencia y costo; evita Lambda si Kappa (streaming + replays) cubre el caso.
- En streaming, define delivery semantics (at-least-once por defecto) e idempotencia en sinks; documenta ventanas y watermarks.
- Planifica particionamiento y paralelismo para evitar skew; mide P95/P99 de latencia.

## 4. Calidad de Datos
- Implementa aserciones como código cerca de la transformación (DataOps). Versiona y ejecuta en CI/CD.
- Mínimo: nulls, duplicados, rangos, cardinalidad, frescura. Registra métricas y alertas.
- Establece políticas de backfill (incremental/shadow/full) con comunicación de impacto.

## 5. Seguridad y Privacidad
- Clasifica datos (PII/PCI/PHI). Aplica mínimo privilegio (RBAC/ABAC) y segmentación por ambientes.
- Cifrado in-transit (TLS) y at-rest (KMS/TDE). Registra accesos y cambios (auditoría).
- Pseudonimización/masking dinámico cuando corresponda. Prevé derecho al olvido y retención.

## 6. Gobernanza y Catálogo
- Define roles claros: Data Owner, Steward, Custodian; matriz RACI por procesos clave (acceso, cambios de esquema).
- Mantén catálogo con metadatos técnicos/negocio/operacionales y linaje (idealmente automatizado con OpenLineage/Atlas/DataHub).
- Mide salud de gobernanza: % datasets con steward, % con reglas de calidad, cumplimiento de SLAs.

## 7. Observabilidad y SLOs
- Golden signals adaptados a datos: Latency, Throughput, Errors, Saturation; añade Freshness y Completeness.
- Publica SLOs por data product; gestiona error budgets y post-mortems de incidentes.
- Centraliza métricas/logs/traces; enlaza alertas con ownership y runbooks.

## 8. FinOps (Costo y Eficiencia)
- Etiquetado (tagging) consistente por dominio/producto/ambiente. Presupuestos y alertas de gasto.
- Optimiza con particionado, compaction, Z-Order/clusterización, caching selectivo y right-sizing.
- Mide costo por workload y por insight; prioriza optimizaciones por impacto.

## 9. Arquitecturas Descentralizadas (Data Mesh/Fabric)
- Trátalo como producto: contrato, owner, métricas de adopción y salud. Plataforma self-service mínima viable.
- Gobernanza federada con políticas globales + libertades locales; interoperabilidad mediante glosario y semántica ligera.
- Evita “mesh” sin plataforma/catálogo; asegura discoverability y trazabilidad de linaje.

## 10. ML Readiness (Feature Stores / MLOps)
- Doble capa de features: offline (training) + online (inference) con versionado y linaje.
- Registro de modelos con estados (dev/staging/prod) y validaciones previas (data quality/fairness/drift).
- Observabilidad de ML: performance del modelo, data drift, calidad de features, costos.

## 11. Búsqueda Vectorial y Semántica
- Normaliza embeddings si usas similitud coseno; IndexFlatIP en FAISS emula coseno con vectores normalizados.
- Evalúa trade-off latencia vs recall@K; documenta configuración del índice y tamaño del dataset.
- Versiona embeddings (modelo y parámetros). Gestiona actualización y reindexado.

## 12. Resiliencia y Recuperación
- DRP: RPO/RTO definidos por dominio. Backups verificados y pruebas de recuperación.
- Multi-AZ/Regiones según criticidad y costos; minimiza egress en multi-cloud.

## 13. Documentación y ADRs
- Documenta decisiones clave como ADRs (Contexto → Decisión → Consecuencias → Alternativas).
- Mantén READMEs por nivel y glosario actualizado; enlaza a referencias oficiales.

---

Última actualización: Noviembre 2025
