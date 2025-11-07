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
- Clasificación y manejo de datos sensibles (PII / GDPR / CCPA)
- RBAC vs ABAC y controles prácticos
- Enmascaramiento / derecho al olvido / auditoría
- Lineage conceptual y base para catálogo
- **Ejercicio integrador:** Caso RetailCorp (roles/RACI/clasificación/lineage/políticas/workflow) en `../04-recursos/casos-uso/caso_integrador_gobierno_retail.md`

### 2. Escalabilidad, Rendimiento y Costos (FinOps de Datos)
- Notebook: `02_escalabilidad_rendimiento_costos.ipynb`
- Patrones de optimización (pruning, proyección selectiva, particionamiento, clustering)
- Modelos de costo (Snowflake, BigQuery, Databricks) y trade-offs
- Estrategias FinOps (right-sizing, scheduling, tiering, Z-order, compaction)
- Métricas de eficiencia y accountability de costos

### 3. Observabilidad, Lineage y Automatización
- Notebook: `03_observabilidad_lineage_automatizacion.ipynb`
- Métricas: frescura, completitud, calidad, latencia, error-rate
- SLOs / SLAs / Error Budgets en datos
- Eventos OpenLineage y ecosistema (Marquez)
- Gates de calidad y verificación de contratos en CI/CD
- Alerting, ownership y manejo de incidentes

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
