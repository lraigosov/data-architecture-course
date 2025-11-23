# Plantilla de Ejercicio Transversal

## 1. Contexto
Describa brevemente el escenario organizacional y la necesidad de arquitectura / calidad / gobernanza / ML / FinOps que se abordará.

**Ejemplo:** "Compañía omni‑canal con canal e‑commerce y tiendas físicas; se requiere unificar ventas y eventos para habilitar recomendaciones en tiempo real y reporting financiero confiable".

## 2. Datasets Proporcionados
| Nombre | Archivo | Descripción | Frecuencia | Problemas Intencionales |
|--------|---------|-------------|-----------|-------------------------|
| Ventas | `datasets/sales_orders.csv` | Órdenes históricas con detalles y estado | Batch diario | Nulos, duplicados, montos inconsistentes |
| Eventos Streaming | `datasets/streaming_events.csv` | Clicks y acciones de usuario en sesiones | Tiempo real | Orden temporal parcial, tipos variados |
| Clientes | `datasets/customers_dim.csv` | Dimensión maestro de clientes | Actualización incremental | Campos opcionales, segmentación incompleta |

## 3. Objetivos del Ejercicio
1. Definir arquitectura de ingestión y zonas (Bronze/Silver/Gold) o equivalente por dominio.
2. Proponer modelo lógico para un data product clave (ej: "Customer 360" o "Real‑Time Sales Dashboard").
3. Diseñar pipeline de calidad (checks + métricas) y criterios de aceptación.
4. Especificar contratos de datos (campos obligatorios, reglas de negocio, SLAs de frescura y calidad).
5. Definir enfoque de costo y optimización (almacenamiento vs cómputo) y tagging FinOps básico.
6. Elaborar un ADR resumido justificando tecnología elegida (formato, motor, catálogo, feature store si aplica).

## 4. Entregables Esperados
| Entregable | Formato | Descripción |
|------------|---------|-------------|
| Diagrama Arquitectura | Imagen / ASCII | Flujo end‑to‑end ingestión → procesamiento → consumo |
| Modelo Lógico | Tabla / Diagrama | Entidades, claves, relaciones principales |
| Data Contract | Markdown | Esquema + tipos + reglas + SLAs + ownership |
| Lista de Quality Checks | Markdown / Pseudocódigo | Reglas con severidad y métricas derivadas |
| ADR | Markdown | Contexto, decisión, consecuencias, alternativas |
| Plan FinOps | Markdown | Principios + quick wins + métricas recurrentes |

## 5. Criterios de Evaluación (Rúbrica)
| Criterio | Básico (1) | Intermedio (2) | Avanzado (3) | Peso |
|----------|------------|----------------|--------------|------|
| Arquitectura | Lista lineal de pasos | Diagrama con capas y zonas | Dominios + flujos batch/stream integrados | 0.20 |
| Modelo Datos | Solo campos listados | Normalización/SCD parcial | Diseño orientado a producto + extensibilidad | 0.15 |
| Calidad & Checks | Reglas genéricas | Checks por dimensión + severidad | Métricas (SLO/SLA) + alertas y linaje | 0.15 |
| Data Contract | Campos sin metadatos | Definición tipos + obligatorios | Completo: semántica, SLAs, ownership, versioning | 0.15 |
| ADR | Sin estructura | Contexto + decisión + alternativa | Completo: consecuencias, riesgos, mitigaciones | 0.10 |
| FinOps | Mención ahorro costo | Principios + tagging | Estimaciones + optimización tarea concreta + roadmap | 0.10 |
| Integración Tiempo Real | No considerado | Menciona streaming superficial | Patrones concretos (CDC, ventana, upsert) | 0.15 |

**Score Final:** Sumatoria (puntaje criterio × peso). >2.4 excelente; 2.0–2.39 adecuado; <2.0 requiere mejora.

## 6. Guía / Pasos Sugeridos
1. Analizar estructura de cada CSV: tipos, problemas evidentes.
2. Definir clasificación de zonas: Bronze (raw), Silver (limpio), Gold (producto analítico / ML).
3. Listar transformaciones clave: deduplicación, validación de rangos, enriquecimientos, agregaciones.
4. Redactar contracto de datos para `customer_360` (mínimo 10 campos con reglas).
5. Formular checks: not_null, uniqueness, range, foreign_key, freshness, derived_consistency.
6. Redactar ADR con 3 alternativas y escoger formato de almacenamiento (Delta vs Iceberg vs Warehouse).
7. Identificar 3 quick wins FinOps (ej: compresión columnar, particionado por fecha, TTL caché streaming).
8. Diseñar métrica de éxito: Tiempo onboarding analista, latencia ingestion→Gold, costo mensual por TB.

## 7. Extensiones Avanzadas (Opcional)
- Añadir capa de Feature Store (offline + online) para recomendación en tiempo real.
- Integrar esquema de versionado semántico para el data product (v1.x → v2.x).
- Definir tablero de observabilidad con métricas negocio + técnicas + calidad.
- Incorporar evaluación de sesgo (si aplica ML sobre clientes).

## 8. Ejemplo de Solución (Esqueleto)
```markdown
# Diagrama (ASCII)
Ingest POS/Clickstream -> Bronze (Raw CSV) -> Quality Gate -> Silver (Clean Parquet) -> Enrichment + Aggregations -> Gold (customer_360 + sales_metrics API/SQL)

# Data Contract (fragmento)
field: customer_id | type: string | nullable: false | semantics: Identificador único CRM | quality: uniqueness=100%, completeness>99.5%
field: lifetime_value | type: decimal(12,2) | nullable: true | calc: SUM(order_amount last 24m) | freshness < 24h
...

# ADR (resumen)
Context: duplicación entre sistemas, necesidad real-time + auditoría.
Decision: Delta Lake en S3 + catálogo unificado + streaming CDC Debezium.
Alternatives: (1) Snowflake, (2) Pure Data Lake (sin ACID), (3) Iceberg + Presto.
Consequences: +ACID, +time travel, - vendor lock-in parcial.

# FinOps Quick Wins
1. Particionado por fecha + cliente_region.
2. Compresión ZSTD Parquet (reduce ~30-50% storage).
3. Autoscaling streaming consumer baselined por throughput horario.
```

## 9. Checklist de Entrega
- [ ] Diagrama arquitectura
- [ ] Modelo lógico
- [ ] Data contract
- [ ] Lista quality checks + severidades
- [ ] ADR completo
- [ ] Plan FinOps
- [ ] Métricas definidas
- [ ] Puntos de extensión (si aplica)

---
**Versión:** 1.0 / Nov 2025  
**Licencia:** Ver LICENSE  
**Mantenimiento:** Equipo de arquitectura de datos
