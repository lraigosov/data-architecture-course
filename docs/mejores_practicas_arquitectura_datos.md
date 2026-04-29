# Mejores Prácticas de Arquitectura de Datos

Esta guía resume criterios prácticos para diseñar, operar y gobernar plataformas de datos. Está alineada con DAMA-DMBOK, principios FAIR, FinOps, observabilidad moderna y gestión de riesgos para datos usados en analítica e IA.

Úsala como referencia transversal para los niveles Junior, Mid y Senior. Cuando una decisión dependa de una tecnología concreta, valida siempre la documentación oficial enlazada en `04-recursos/referencias.md`.

## 1. Modelado y Contratos de Datos
- Diseña primero el modelo conceptual (negocio/KPIs) -> lógico -> físico. Mantén trazabilidad.
- Usa contratos de datos versionados: esquema, semántica, reglas de calidad, SLAs, owner, términos de uso y estado del contrato.
- Gestiona compatibilidad de esquemas: backward-compatible por defecto; documenta cambios breaking y plan de migración (expand-contract).
- Evita duplicidades: Single Source of Truth (SSOT) y catálogo actualizado.

## 2. Almacenamiento y Formatos
- Elige un formato de tabla transaccional en data lake cuando necesites snapshots, evolución de esquema, aislamiento de lecturas o actualizaciones controladas. Iceberg, Delta Lake y Hudi resuelven necesidades parecidas con modelos operativos distintos.
- Estandariza formatos columnares como Parquet u ORC para cargas analíticas. Define compresión, particionamiento y compaction con base en patrones reales de consulta.
- Define capas claras (Bronze/Silver/Gold o equivalentes) y políticas de retención por sensibilidad, costo, valor de negocio y requisitos legales.
- Evita particionar por columnas de alta cardinalidad si no hay beneficio claro en pruning; mide antes de convertir una convención en estándar.

## 3. Procesamiento (Batch/Streaming)
- Selecciona batch/streaming según objetivos de latencia y costo; evita Lambda si Kappa (streaming + replays) cubre el caso.
- En streaming, define delivery semantics, idempotencia en sinks, claves de deduplicación, ventanas, watermarks y reglas para datos tardíos.
- Usa CloudEvents u otra convención explícita cuando necesites interoperabilidad de metadatos entre productores y consumidores de eventos.
- Planifica particionamiento y paralelismo para evitar skew; mide P95/P99 de latencia.

## 4. Calidad de Datos
- Implementa aserciones como código cerca de la transformación. Versiona reglas y ejecútalas en CI/CD o en el orquestador antes de publicar datos críticos.
- Mínimo recomendado: schema, missingness, uniqueness, rangos, integridad referencial, volumen, frescura y distribución.
- Publica resultados de validación en un lugar legible por consumidores, no solo en logs técnicos.
- Establece políticas de backfill (incremental/shadow/full) con comunicación de impacto.

## 5. Seguridad y Privacidad
- Clasifica datos (PII/PCI/PHI). Aplica mínimo privilegio (RBAC/ABAC) y segmentación por ambientes.
- Cifrado in-transit (TLS) y at-rest (KMS/TDE). Registra accesos y cambios (auditoría).
- Pseudonimización, tokenización o masking dinámico cuando corresponda. Prevé retención, eliminación, evidencia de consentimiento y atención de derechos de titulares.
- Para datasets usados en IA, documenta usos permitidos y prohibidos, procedencia, sesgos conocidos y restricciones regulatorias.

## 6. Gobernanza y Catálogo
- Define roles claros: Data Owner, Steward, Custodian; matriz RACI por procesos clave (acceso, cambios de esquema).
- Mantén catálogo con metadatos técnicos/negocio/operacionales y linaje (idealmente automatizado con OpenLineage/Atlas/DataHub).
- Mide salud de gobernanza: % datasets con steward, % con reglas de calidad, cumplimiento de SLAs.
- Incluye metadatos de uso: consumidores, dashboards, modelos, consultas principales y dependencias críticas.

## 7. Observabilidad y SLOs
- Golden signals adaptados a datos: Latency, Throughput, Errors, Saturation; añade Freshness y Completeness.
- Publica SLOs por data product; gestiona error budgets y post-mortems de incidentes.
- Centraliza métricas/logs/traces; enlaza alertas con ownership y runbooks.
- Separa alertas de síntomas (pipeline falló) y alertas de impacto (producto de datos incumplió frescura o completitud).

## 8. FinOps (Costo y Eficiencia)
- Etiquetado (tagging) consistente por dominio/producto/ambiente. Presupuestos y alertas de gasto.
- Optimiza con particionado, compaction, Z-Order/clusterización, caching selectivo y right-sizing.
- Mide costo por workload, producto de datos o unidad de valor. Prioriza optimizaciones por impacto y no por intuición.
- Lleva decisiones de costo a revisiones de arquitectura: retención, egress, frecuencia de actualización, SLAs y duplicación de datos.

## 9. Arquitecturas Descentralizadas (Data Mesh/Fabric)
- Trátalo como producto: contrato, owner, métricas de adopción y salud. Plataforma self-service mínima viable.
- Gobernanza federada con políticas globales + libertades locales; interoperabilidad mediante glosario y semántica ligera.
- Evita adoptar Data Mesh solo como organigrama. Sin plataforma, catálogo, contratos y ownership real, suele convertirse en fragmentación.
- Data Fabric no reemplaza automáticamente el ownership de dominios; úsalo como enfoque de integración, automatización y metadatos activos cuando aporte valor.

## 10. ML Readiness (Feature Stores / MLOps)
- Doble capa de features: offline (training) + online (inference) con versionado y linaje.
- Registro de modelos con estados (dev/staging/prod) y validaciones previas (data quality/fairness/drift).
- Observabilidad de ML: performance del modelo, data drift, calidad de features, costos.
- Aplica gestión de riesgo para IA cuando los datos alimenten decisiones sensibles: privacidad, explicabilidad, fairness, robustez, seguridad y monitoreo posterior al despliegue.

## 11. Búsqueda Vectorial y Semántica
- Normaliza embeddings si usas similitud coseno; IndexFlatIP en FAISS emula coseno con vectores normalizados.
- Evalúa trade-off latencia vs recall@K; documenta configuración del índice y tamaño del dataset.
- Versiona embeddings (modelo y parámetros). Gestiona actualización y reindexado.
- Diseña estrategia de evaluación: conjunto de consultas, relevancia esperada, recall@K, precisión percibida, latencia y costo de indexación.

## 12. Resiliencia y Recuperación
- DRP: RPO/RTO definidos por dominio. Backups verificados y pruebas de recuperación.
- Multi-AZ/Regiones según criticidad y costos; minimiza egress en multi-cloud.
- Prueba restauraciones y replays; un backup no verificado es solo una hipótesis.

## 13. Documentación y ADRs
- Documenta decisiones clave como ADRs (Contexto -> Decisión -> Consecuencias -> Alternativas).
- Mantén READMEs por nivel y glosario actualizado; enlaza a referencias oficiales.
- Revisa enlaces y vigencia de referencias antes de publicar material nuevo.

## Referencias base

- DAMA International, **DAMA-DMBOK2**.
- GO FAIR, **FAIR Principles**.
- FinOps Foundation, **FinOps Framework**.
- NIST, **AI Risk Management Framework 1.0** y **Generative AI Profile**.
- CNCF, **CloudEvents**.
- Apache Iceberg, Delta Lake y Apache Hudi, documentación oficial de formatos de tabla.
- OpenLineage, DataHub, OpenMetadata y Great Expectations, documentación oficial de metadatos, linaje, contratos y calidad.

---

Última actualización: Abril 2026
