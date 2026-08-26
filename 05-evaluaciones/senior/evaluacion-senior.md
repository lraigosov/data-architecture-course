# Evaluación Nivel Senior

## Componentes de Evaluación

### 1. Notebooks y Ejercicios (30%)

**Notebooks requeridos:**

1. `01_gobernanza_seguridad_cumplimiento.ipynb` — roles, RACI, políticas, GDPR/CCPA/Ley 1581.
2. `02_escalabilidad_rendimiento_costos.ipynb` — dimensionamiento, FinOps avanzado, observabilidad.
3. `03_observabilidad_lineage_automatizacion.ipynb` — SLOs/SLAs, OpenLineage, gates de calidad en CI/CD.
4. `04_arquitecturas_referencia.ipynb` — DW/Lake/Lakehouse/Mesh, ADRs, Data Product Registry.
5. `05_alineacion_estrategica_modelos_dominio.ipynb` — estrategia → dominios → ontología → KPIs.
6. `06_gobernanza_semantica_y_kg_descubrimiento_reutilizacion.ipynb` — gobernanza semántica, SHACL, discovery/reuse.
7. `07_estrategia_multi_cloud_migracion_costos.ipynb` — decisión single/multi-cloud, migración por fases.
8. `08_visualizacion_ejecutiva_analisis_impacto.ipynb` — VSM, capability maps, ROI ejecutivo.
9. `09_transformacion_cultural_data_driven_estrategia.ipynb` — change management, madurez cultural.
10. `10_evolucion_arquitectonica_estrategica.ipynb` — fitness functions, deuda técnica, modernización.
11. `11_arquitectura_empresarial_ml_escala.ipynb` — ML Platform, Model Registry, observabilidad de ML.
12. `12_arquitectura_big_data_iot_taller.ipynb` — pipeline IoT extremo a extremo, Lambda vs Kappa.
13. `13_transicion_centralizado_a_mesh_fabric_taller_evaluacion.ipynb` — roadmap Mesh/Fabric, gobernanza federada.
14. `14_gobernanza_ia_ready_politicas_privacidad_sesgo_taller.ipynb` — fairness, drift, checklist IA-ready.
15. `15_arquitectura_iot_industrial_streaming_edge_taller.ipynb` — edge-cloud, latency budget, feedback loop.

**Criterios por notebook:**
- Todos los ejercicios y talleres integradores completados (40%)
- Código y frameworks (fitness functions, calculadoras ROI/madurez, simuladores) ejecutables sin errores (25%)
- Decisiones y ADRs justificados con trade-offs explícitos, no solo descriptivos (25%)
- Documentación y referencias verificables (10%)

**Umbral mínimo:** al menos 13 de 15 notebooks completados (87%). Dado el carácter estratégico del nivel, no se recomienda promediar déficits entre notebooks técnicos y estratégicos: ambos tipos deben estar representados en lo entregado.

### 2. Documento Ejecutivo (40%)

Ver "Proyecto del Nivel" abajo — es el mismo entregable, formalizado aquí como componente evaluable con rúbrica.

### 3. Defensa Técnica / Revisión Arquitectónica (30%)

**Formato:** presentación de 20-30 minutos ante un comité (instructor + pares), seguida de preguntas, tal como indica el README del nivel ("Incluye peer review y checklist de madurez").

**Qué se evalúa:**
- Capacidad de defender decisiones arquitectónicas bajo cuestionamiento (no solo presentar).
- Respuestas a escenarios "¿qué pasaría si...?" (cambio de escala, incidente de seguridad, restricción regulatoria nueva).
- Retroalimentación de pares registrada con al menos 2 observaciones por evaluador.
- Uso del checklist de madurez transversal: [`docs/checklist_revision_arquitectura.md`](../../docs/checklist_revision_arquitectura.md).

---

## Proyecto del Nivel: Documento de Arquitectura Ejecutiva

**Descripción:**
Elaborar un Documento de Arquitectura Ejecutiva para una organización ficticia (o un caso real anonimizado) que integre estrategia de negocio, gobierno, arquitectura, seguridad, observabilidad, FinOps y plan de adopción — dirigido a un comité ejecutivo, no solo a un equipo técnico.

Este es el mismo entregable descrito en [`03-nivel-senior/README.md`](../../03-nivel-senior/README.md#proyecto-del-nivel).

**Entregables:**

#### A. Estrategia y Gobierno (10%)
1. Estrategia y objetivos de negocio alineados a datos.
2. Dominios y modelo de gobierno (roles, RACI, flujos de aprobación).

#### B. Arquitectura y Cumplimiento (15%)
3. Arquitectura lógica y física (diagramas + decisiones justificadas, con al menos un ADR formal).
4. Seguridad, privacidad y cumplimiento (controles técnicos y procesos; referenciar el marco regulatorio aplicable — GDPR, CCPA, Ley 1581 u otro).

#### C. Observabilidad y FinOps (10%)
5. Estrategia de observabilidad (métricas, SLOs, flujos de lineage, alertas).
6. Optimización y plan FinOps (baseline de costos y roadmap de eficiencia).

#### D. Plan de Adopción (5%)
7. Plan de adopción / fases / riesgos / KPIs de éxito.

**Formato de entrega:**
- Documento PDF (formato ejecutivo: resumen inicial, sin exceso de jerga técnica en las secciones dirigidas a negocio).
- Anexo técnico con diagramas detallados y ADRs completos.
- (Opcional) Slides ejecutivos de apoyo para la defensa técnica.

---

## Rúbrica Detallada del Proyecto

### A. Estrategia y Gobierno (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Alineación Estratégica** | Objetivos de negocio claramente conectados a decisiones de datos, con KPIs de negocio | Conexión presente, KPIs parciales | Conexión superficial | Sin conexión a estrategia de negocio |
| **Modelo de Gobierno** | Roles, RACI y flujos de aprobación completos y realistas | Roles y RACI presentes, flujos básicos | Gobierno mencionado sin detalle | Sin modelo de gobierno |

### B. Arquitectura y Cumplimiento (15 puntos)

| Criterio | Excelente (13-15) | Bueno (10-12) | Satisfactorio (7-9) | Necesita Mejora (< 7) |
|----------|-------------------|----------------|----------------------|------------------------|
| **Arquitectura y ADRs** | Arquitectura completa con al menos un ADR formal (contexto/decisión/alternativas/consecuencias) | Arquitectura clara, ADR parcial | Arquitectura básica sin ADR formal | Arquitectura incompleta o inconsistente |
| **Seguridad y Cumplimiento** | Controles técnicos + marco regulatorio aplicable identificado y justificado | Controles presentes, marco regulatorio mencionado | Controles básicos, sin marco regulatorio claro | Sin controles de seguridad ni cumplimiento |

### C. Observabilidad y FinOps (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Observabilidad** | SLOs, métricas y flujo de lineage definidos con alertas accionables | SLOs y métricas presentes, alertas básicas | Observabilidad mencionada sin SLOs | Sin estrategia de observabilidad |
| **FinOps** | Baseline de costos + roadmap de eficiencia con impacto estimado | Baseline presente, roadmap básico | Estimación superficial | Sin baseline de costos |

### D. Plan de Adopción (5 puntos)

| Criterio | Excelente (5) | Bueno (4) | Satisfactorio (3) | Necesita Mejora (< 3) |
|----------|----------------|-----------|---------------------|------------------------|
| **Fases, Riesgos y KPIs** | Roadmap por fases con riesgos, mitigaciones y KPIs de éxito medibles | Roadmap presente, riesgos parciales | Plan mencionado sin detalle | Sin plan de adopción |

### Defensa Técnica (evaluada aparte, 30% del total)

| Criterio | Excelente (27-30) | Bueno (21-26) | Satisfactorio (15-20) | Necesita Mejora (< 15) |
|----------|--------------------|-----------------|--------------------------|--------------------------|
| **Defensa de Decisiones** | Responde con seguridad y evidencia a preguntas de trade-offs y escenarios hipotéticos | Responde la mayoría de preguntas con solidez | Responde preguntas básicas | No puede defender decisiones clave |
| **Uso de Feedback de Pares** | Incorpora o discute activamente el feedback de al menos 2 pares | Reconoce el feedback recibido | Feedback registrado sin discusión | Sin registro de peer review |

---

## Ejemplos de Preguntas / Escenarios de Defensa

### Sección 1: Gobierno y Cumplimiento (Notebook 1)

**Escenario 1:**
Tu Data Product Registry muestra que `gold.clientes_360` no tiene Steward asignado hace 3 meses. Un regulador solicita evidencia de gobierno de datos personales bajo GDPR. ¿Qué expones primero y por qué? ¿Qué riesgo regulatorio específico señala esta brecha?

### Sección 2: Escalabilidad y FinOps (Notebook 2)

**Escenario 2:**
Tu plataforma proyecta triplicar volumen en 12 meses (capacity planning a 5 años). El comité pregunta: ¿shardear ahora o esperar? Justifica con el framework Inform → Optimize → Operate y al menos una métrica de FinOps concreta.

### Sección 3: Arquitectura de Referencia (Notebook 4)

**Escenario 3:**
Un stakeholder propone migrar de Lakehouse a Data Mesh "porque está de moda". Usa el framework de decisión ponderado del notebook 4 para argumentar a favor o en contra, citando al menos 2 de los 4 principios de Data Mesh.

### Sección 4: ML a Escala y Gobernanza IA-Ready (Notebooks 11, 14)

**Escenario 4:**
El `DriftReport` del notebook 11 marca `is_drifted=True` (`drift_score > 0.3`) para la feature `transaction_amount` de un modelo en producción. Según la política de `drift_monitoring` del notebook 14, ¿qué brecha de gobernanza señala esto si el modelo no tenía monitoreo de drift habilitado, y qué decisión (rollback, retrain, alerta) tomarías y por qué?

---

## Instrucciones de Entrega

### Formato
- **Notebooks:** Subir archivos `.ipynb` ejecutados a repositorio GitHub.
- **Documento ejecutivo:** PDF subido a la plataforma LMS + anexo técnico.
- **Defensa técnica:** Sesión en vivo (presencial o remota) con registro de feedback de pares.

### Plazos
- **Notebooks:** Progresivo, según avance del nivel.
- **Documento ejecutivo:** Última semana del nivel.
- **Defensa técnica:** Hasta 2 semanas después de la entrega del documento ejecutivo.

### Naming Convention
```
apellido_nombre_senior_documento_ejecutivo.pdf
apellido_nombre_senior_anexo_tecnico.pdf
apellido_nombre_01_gobernanza_seguridad_cumplimiento.ipynb
```

---

## Criterios de Aprobación

- **Calificación mínima:** 70% (escala general en [`05-evaluaciones/README.md`](../README.md#escala-de-calificación)).
- **Criterio de dominio senior sugerido:** ≥ 85%, tal como indica [`03-nivel-senior/README.md`](../../03-nivel-senior/README.md#criterio-de-dominio-sugerido) para programas que emitan constancias o insignias propias.
- **Notebooks:** Al menos 13 de 15 completados.
- **Defensa técnica:** Obligatoria para aprobar el nivel — el documento ejecutivo por sí solo no es suficiente sin la defensa.

## Feedback

- Notebooks: retroalimentación en 3-5 días laborables.
- Documento ejecutivo: retroalimentación detallada en 10-14 días laborables.
- Defensa técnica: feedback inmediato de pares + informe consolidado del instructor en 5 días laborables.

## Recursos de Apoyo

- Horas de oficina: según calendario del programa que adopte el curso.
- Foro de dudas en plataforma LMS.
- Material de referencia en `04-recursos/` y `docs/mejores_practicas_arquitectura_datos.md`.

---

**¡Éxito en tu evaluación!**
