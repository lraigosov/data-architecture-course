# Nivel Senior - Gobernanza, Seguridad, Escalabilidad y Observabilidad

## Objetivo del Nivel

Fortalecer las capacidades para diseñar, gobernar, asegurar, optimizar y operar plataformas de datos empresariales a escala con criterios de confiabilidad, costo y cumplimiento.

## Contenidos Actuales

### 1. Gobernanza, Seguridad y Cumplimiento
- Notebook: `01_gobernanza_seguridad_cumplimiento.ipynb`
- Governance (DAMA-DMBOK principios aplicados)
- **Roles y responsabilidades detalladas:** Data Owner, Steward, Custodian, Governance Lead
- **Matriz RACI:** Ejemplo para cambio de esquema
- **Políticas de datos:** Clasificación, acceso, retención, calidad (definición y enforcement)
- **Procedimientos (workflows):** Solicitud de acceso, cambio de esquema, quality gates
- **Herramientas de gobernanza:** Catálogo (Atlan, Collibra, DataHub), calidad (Great Expectations, Soda), lineage (OpenLineage, Marquez), seguridad (Ranger, Privacera)
- **Dashboard de métricas de gobierno:** % datasets con Steward, calidad validada, revisiones de acceso
- **Security by Design:** Seguridad integrada en todas las fases (ingesta, almacenamiento, procesamiento, exposición, retención)
- **Arquitectura en capas con controles:** Bronze/Silver/Gold con RBAC, cifrado, masking, auditoría
- **Segregación de funciones:** Ambientes separados, principio de mínimo privilegio, break-glass
- Clasificación y manejo de datos sensibles (PII / PCI / PHI)
- RBAC vs ABAC y controles prácticos
- Enmascaramiento / derecho al olvido / auditoría
- Lineage conceptual y base para catálogo
- **Cumplimiento normativo detallado:**
  - **GDPR (Unión Europea):** Principios, derechos del titular, DPIA, DPO, notificación 72h, multas hasta 4% ingresos
  - **CCPA (California, EE.UU.):** Derechos del consumidor, opt-out de venta, diferencias vs GDPR
  - **Colombia (Ley 1581/2012):** Habeas Data, consentimiento explícito, datos sensibles, registro SIC, sanciones
- **Monitoreo y reporte de compliance:** Inventario de datos personales, DPIA, políticas/procedimientos, capacitación, auditorías, gestión de incidentes, dashboard de métricas DSAR
- **Ejercicio integrador:** Caso RetailCorp (roles/RACI/clasificación/lineage/políticas/workflow) en `../04-recursos/casos-uso/caso_integrador_gobierno_retail.md`

### 2. Escalabilidad, Rendimiento y Costos (FinOps de Datos)
- Notebook: `02_escalabilidad_rendimiento_costos.ipynb`
- **Dimensionamiento estratégico según 3 V:**
  - Volumen: Capacity planning con crecimiento proyectado, código de proyección 5 años
  - Velocidad: Throughput, latencia, SLOs por caso de uso (BI, APIs, ML)
  - Variedad: Impacto en arquitectura (Lake vs Warehouse)
- Patrones de optimización (pruning, proyección selectiva, particionamiento, clustering)
- Modelos de costo (Snowflake, BigQuery, Databricks) y trade-offs
- **FinOps avanzado:**
  - Framework: Inform → Optimize → Operate
  - Chargeback vs Showback con código de atribución de costos
  - Cost anomaly detection con detección estadística (±2σ) y visualización
  - Reserved instances, spot instances, right-sizing
- **Observabilidad avanzada:**
  - Stack: Prometheus/Datadog → Grafana → PagerDuty
  - Métricas por capa: ingesta (throughput, lag), procesamiento (CPU, memory, skew), serving (latency, cache hit rate)
  - Golden Signals: Latency, Traffic, Errors, Saturation
  - SLOs y error budgets con código de compliance tracking
  - Dashboard completo (9 paneles) con métricas en tiempo real
- Estrategias FinOps (right-sizing, scheduling, tiering, Z-order, compaction)
- Métricas de eficiencia y accountability de costos
- **Ejercicio integrador avanzado:** Migración multi-cloud con reducción 30% costos

### 3. Observabilidad, Lineage y Automatización
- Notebook: `03_observabilidad_lineage_automatizacion.ipynb`
- Métricas: frescura, completitud, calidad, latencia, error-rate
- SLOs / SLAs / Error Budgets en datos
- Eventos OpenLineage y ecosistema (Marquez)
- Gates de calidad y verificación de contratos en CI/CD
- Alerting, ownership y manejo de incidentes

### 4. Arquitecturas de Referencia y Patrones Avanzados
- Notebook: `04_arquitecturas_referencia.ipynb`
- **Evolución histórica:** Data Warehouse (1990s) → Data Lake (2010s) → Lakehouse (2020s) → Data Mesh (futuro)
- **Arquitecturas tradicionales:** Data Warehouse (Inmon), Data Lake (Hadoop) con ventajas/limitaciones
- **Arquitecturas modernas:** Lakehouse (Delta/Iceberg/Hudi), Data Mesh con 4 principios
- **Comparativa detallada:** Tabla DW/Lake/Lakehouse/Mesh según 10 dimensiones
- **Trade-offs:** Centralizado vs descentralizado, batch vs streaming vs Lambda/Kappa
- **Framework de decisión:** Código con evaluación ponderada de arquitecturas, radar chart comparativo
- **Data Mesh profundo:** Anatomía data product con contrato completo, self-serve platform, federated governance
- **Data Product Registry:** Simulador con registro, discovery, métricas de uso, health reports con SLA compliance
- **ADRs (Architecture Decision Records):** Template completo con contexto/decisión/consecuencias/alternativas
- Ejercicio integrador: Banco multinacional (50M clientes, 10 PB datos, 5 dominios, GDPR/BCBS 239)

### 5. Alineación Estratégica con Modelos de Dominio, Ontologías y Taxonomías
- Notebook: `05_alineacion_estrategica_modelos_dominio.ipynb`
- De estrategia → capacidades → dominios → ontología → data products → KPIs
- Métricas de alineación: coverage, redundancia semántica, time-to-KPI, alignment de productos
- Governance semántica y policy-as-graph; integración con catálogo y lineage
- Madurez semántica organizacional y plan de evolución
- ADR de adopción de ontología empresarial (ejemplo completo)

### 6. Gobernanza Semántica y Knowledge Graphs para Discovery/Reutilización
- Notebook: `06_gobernanza_semantica_y_kg_descubrimiento_reutilizacion.ipynb`
- Marco de gobernanza de metadatos semánticos (principios, roles, procesos)
- Arquitectura de referencia: Catálogo + KG + Índice + API de búsqueda
- Políticas/validación (SHACL) y policy-as-graph integradas al CI/CD
- Métricas de discovery/reuse (SSR, ATD, RR) con simulador y objetivos
- Caso de estudio y ADR de adopción con metas a 12 meses

### 7. Estrategia Multi-Cloud: Migración, Costos y Gobierno Avanzado
- Notebook: `07_estrategia_multi_cloud_migracion_costos.ipynb`
- Framework de decisión single vs multi-cloud (ponderado por criterios)
- Plan de migración por fases, riesgos y mitigaciones
- Simulador de asignación de workloads (costos/latencia) entre nubes
- FinOps multi-cloud: tagging unificado, cost arbitration, budgeting cross-cloud
- ADR de estrategia multi-cloud y KPIs de éxito (ROI, SSR, savings)

## Próximas Extensiones (Plan Futuro)
- Taller integral end-to-end (arquitectura y trade-offs)
- Ejemplos ampliados de catálogo / data contracts productizados
- Profundización en Data Privacy Automation y Policy-as-Code

## Proyecto del Nivel

Elaborar un **Documento de Arquitectura Ejecutiva** que integre:
1. Estrategia y objetivos de negocio alineados a datos
2. Dominios y modelo de gobierno (roles, RACI, flujos)
3. Arquitectura lógica y física (diagramas + decisiones justificadas)
4. Seguridad, privacidad y cumplimiento (controles técnicos y procesos)
5. Estrategia de observabilidad (métricas, SLOs, flujos de lineage, alertas)
6. Optimización y plan FinOps (baseline de costos y roadmap de eficiencia)
7. Plan de adopción / fases / riesgos / KPIs

## Evaluación

- Notebooks y ejercicios: 30%
- Documento ejecutivo: 40%
- Defensa técnica / revisión arquitectónica: 30%

Incluye peer review y checklist de madurez.

## Requisitos Previos

- Completar Nivel Mid o experiencia equivalente
- Conocimientos de modelado, pipelines y gobierno básico
- Familiaridad con un motor analítico cloud (BigQuery, Snowflake o Databricks)

## Tiempo Estimado

6–8 semanas (30–40 horas) dependiendo de profundidad del proyecto final.

## Certificación

Calificación ≥ 85% otorga certificado **Arquitecto/a de Datos Senior**.

## Recursos Adicionales

- Principios DAMA-DMBOK (síntesis en recursos internos)
- Plantillas (RACI, decisión arquitectónica ADR, matriz de riesgos)
- Ejemplos de SLOs y contratos de datos (ver `../04-recursos/contratos-datos/`)

---

¿Sugerencias o casos que quieras agregar? Abre un issue o PR para evolucionar este nivel.
