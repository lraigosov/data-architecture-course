# Evaluación Nivel Mid

## Componentes de Evaluación

### 1. Notebooks y Ejercicios (30%)

**Notebooks requeridos**, agrupados según la ruta recomendada del nivel:

**Bloque 1 - Fundamentos de plataforma**
1. `01_almacenamiento_e_integracion.ipynb`
2. `02_procesamiento_batch_streaming_y_data_mesh.ipynb`
3. `03_lambda_kappa_event_driven.ipynb`
4. `04_calidad_y_backfill.ipynb`

**Bloque 2 - Gobierno operativo**
5. `05_metadatos_catalogo_linaje.ipynb`
6. `06_implementacion_controles_seguridad.ipynb`
7. `07_optimizacion_dimensionamiento_finops.ipynb`
8. `08_patrones_arquitectura_datos.ipynb`

**Bloque 3 - Semántica, nube y comunicación**
9. `09_modelado_semantico_ontologias_kg.ipynb`
10. `10_gobernanza_metadatos_semanticos_y_kg.ipynb`
11. `11_arquitecturas_cloud_y_multi_cloud.ipynb`
12. `12_diagramas_componentes_flujos_datos.ipynb`
13. `13_arquitectura_habilitadora_cultura_data_driven.ipynb`
14. `14_observabilidad_evolucion_arquitectura.ipynb`

**Bloque 4 - Arquitecturas AI-ready**
15. `15_arquitectura_ai_ready_feature_stores_streaming.ipynb`
16. `16_frameworks_big_data_modernos_comparativo.ipynb`
17. `17_mini_data_mesh_dos_dominios_catalogo_compartido.ipynb`
18. `18_observabilidad_metadata_linaje_ia_bigdata_simulacion.ipynb`
19. `19_streaming_inferencia_tiempo_real_caso_practico.ipynb`
20. `20_vector_search_embeddings_similitud.ipynb`
21. `21_vector_search_faiss_vs_bruteforce.ipynb`

**Criterios por notebook:**
- Todos los ejercicios completados (40%)
- Código ejecutable sin errores, con decisiones justificadas en celdas markdown (30%)
- Respuestas correctas a preguntas de cierre de cada notebook (20%)
- Documentación y comentarios (10%)

**Umbral mínimo:** al menos 17 de 21 notebooks completados (81%), con cobertura de los 4 bloques (no basta con completar solo un bloque).

### 2. Caso de Estudio Aplicado (30%)

**Formato:** análisis escrito + cuestionario de aplicación (no memorístico) sobre un caso de negocio asignado.
**Duración sugerida:** 2-3 horas, entrega asincrónica.

**Temas evaluados** (uno o más por caso, según el escenario asignado):
- Decisión batch vs. streaming vs. híbrido (Lambda/Kappa) para un flujo de datos dado (Bloque 1).
- Diseño de contrato de datos + estrategia de backfill ante un cambio de esquema (Bloque 1).
- Diseño de controles de seguridad (RBAC/ABAC, masking, cifrado) para un dataset con PII (Bloque 2).
- Cálculo y justificación de una estrategia FinOps (right-sizing, particionamiento, detección de anomalías de costo) (Bloque 2).
- Modelado semántico mínimo (glosario + mapeo a un KG simple) para interoperabilidad entre dos dominios (Bloque 3).
- Diseño de un data product para un mini Data Mesh: contrato, ownership, catálogo compartido (Bloque 4).

**Criterios:**
- Aplica el marco conceptual correcto al escenario (no una respuesta genérica).
- Justifica trade-offs (costo, latencia, complejidad operativa, gobierno) en vez de dar una única "receta".
- Usa terminología y patrones vistos en los notebooks del bloque correspondiente.

### 3. Proyecto Final: Diseño Arquitectónico Híbrido (40%)

**Descripción:**
Diseñar la arquitectura de datos híbrida (batch + streaming, con gobierno operativo) para un caso de negocio asignado (retail, fintech, salud, manufactura u otro dominio equivalente al usado en los ejercicios del nivel).

Este es el mismo "Entregable del Nivel" descrito en [`02-nivel-mid/README.md`](../../02-nivel-mid/README.md#entregable-del-nivel), formalizado aquí como proyecto evaluable.

**Entregables:**

#### A. Diagrama y Justificación Arquitectónica (10%)
- Diagrama de capas, componentes y flujos de datos (Mermaid o equivalente, ver notebook 12).
- Justificación de decisiones: latencia, costo, seguridad, gobierno, complejidad operativa.

#### B. Ingestión, Calidad y Contratos (10%)
- Estrategia de ingestión y procesamiento: batch, streaming, CDC o combinación, con justificación.
- Contratos de datos, reglas de calidad (`04-recursos/helpers/quality_rules.py` como referencia) y plan de backfill.

#### C. Gobierno, Seguridad y Observabilidad (10%)
- Metadatos, catálogo, linaje y responsables (owner/steward/custodian).
- Controles de seguridad, privacidad y auditoría (RBAC/ABAC, masking, cifrado).
- Observabilidad, SLOs y runbooks básicos ante incidentes.

#### D. FinOps y Presentación Oral (10%)
- Estimación FinOps y criterios de optimización (dimensionamiento, particionamiento, alertas de costo).
- Presentación oral de 10-15 minutos defendiendo las decisiones ante el instructor o pares (formato equivalente a un ADR presentado en comité de arquitectura).

**Formato de entrega:**
- Documento PDF o Markdown con diagramas embebidos.
- Repositorio o carpeta con los artefactos de código/ejercicios de apoyo (opcional pero recomendado).
- Grabación o sesión en vivo de la presentación oral.

---

## Rúbrica Detallada del Proyecto

### A. Diagrama y Justificación (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Claridad del Diagrama** | Diagrama completo, capas y flujos claros, notación consistente | Diagrama claro con capas principales | Diagrama comprensible con esfuerzo | Diagrama confuso o incompleto |
| **Justificación de Decisiones** | Cada decisión clave (latencia/costo/seguridad/gobierno) justificada con trade-offs explícitos | La mayoría de decisiones justificadas | Justificación básica, sin trade-offs | Decisiones sin justificar |

### B. Ingestión, Calidad y Contratos (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Estrategia de Ingestión** | Elección batch/streaming/CDC justificada con SLOs concretos | Elección razonable, justificación parcial | Elección presente sin justificación sólida | Sin estrategia clara |
| **Contratos y Calidad** | Contrato de datos completo + reglas de calidad + plan de backfill ante cambios de esquema | Contrato y reglas presentes, backfill básico | Contrato parcial | Sin contrato ni reglas de calidad |

### C. Gobierno, Seguridad y Observabilidad (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Metadatos y Linaje** | Catálogo, linaje y responsables (owner/steward/custodian) completos | Catálogo y linaje presentes, responsables parciales | Metadatos básicos | Sin metadatos ni linaje |
| **Seguridad y Observabilidad** | Controles RBAC/ABAC + masking/cifrado + SLOs y runbooks definidos | Controles y SLOs presentes, runbook básico | Controles básicos, sin SLOs | Sin controles de seguridad definidos |

### D. FinOps y Presentación (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Estimación FinOps** | Estimación de costos con supuestos explícitos y plan de optimización priorizado | Estimación presente, optimización básica | Estimación superficial | Sin estimación de costos |
| **Presentación Oral** | Defensa clara, responde preguntas de trade-offs con seguridad | Defensa clara, algunas dudas en preguntas | Presentación básica | Sin presentación o no defiende decisiones |

---

## Ejemplos de Preguntas del Caso de Estudio

### Sección 1: Batch vs. Streaming (Bloque 1)

**Pregunta 1 (Aplicación):**
Un marketplace recibe actualizaciones de inventario cada 30 segundos desde 200 tiendas, y el equipo de BI necesita reportes con máximo 15 minutos de retraso. ¿Batch, streaming o híbrido? Justifica con al menos 2 trade-offs (costo, complejidad operativa, latencia).

**Respuesta esperada:** Híbrido (Kappa o micro-batch) justificado por el SLO de 15 min, considerando que streaming puro añadiría complejidad operativa innecesaria si el negocio no requiere latencia de segundos.

### Sección 2: Seguridad (Bloque 2)

**Pregunta 2 (Aplicación):**
Un dataset `gold.clientes_360` contiene email, teléfono e historial de compras. Los analistas de Marketing necesitan segmentar clientes sin ver PII directamente. Propón un control (RBAC/ABAC + masking) y explica qué campo(s) enmascararías y por qué.

### Sección 3: FinOps (Bloque 2)

**Pregunta 3 (Cálculo):**
Un clúster corre 10 horas/día; de esas, 4 horas no tienen jobs activos (idle). Calcula el `waste_pct` (usa `04-recursos/helpers/cost_metrics.py` como referencia de la fórmula ya definida en el curso: `waste_pct = idle_hours / (active_hours + idle_hours)`) y propone 2 acciones concretas para reducirlo.

**Respuesta esperada:** `waste_pct = 4 / 10 = 0.4 = 40%`. Acciones: auto-scaling/apagado programado fuera de horario, o scheduling que agrupe jobs para reducir tiempo idle.

### Sección 4: Data Mesh y Semántica (Bloques 3-4)

**Pregunta 4 (Diseño):**
Dos dominios (Ventas y Marketing) necesitan compartir el concepto "Cliente" sin duplicar lógica. ¿Qué mecanismo del curso usarías para lograr interoperabilidad sin acoplar los dominios? Menciona el rol del catálogo compartido y la capa semántica.

---

## Instrucciones de Entrega

### Formato
- **Notebooks:** Subir archivos `.ipynb` ejecutados a repositorio GitHub.
- **Caso de estudio:** Documento Markdown o PDF subido a la plataforma LMS.
- **Proyecto final:** PDF/Markdown con diagramas + presentación oral (en vivo o grabada).

### Plazos
- **Notebooks:** Al finalizar cada bloque (progresivo, 4 entregas).
- **Caso de estudio:** Última semana del nivel.
- **Proyecto final:** 3 semanas después de completar todos los notebooks.

### Naming Convention
```
apellido_nombre_mid_proyecto.pdf
apellido_nombre_mid_caso_estudio.md
apellido_nombre_05_metadatos_catalogo_linaje.ipynb
```

---

## Criterios de Aprobación

- **Calificación mínima:** 70% (consistente con la escala general en [`05-evaluaciones/README.md`](../README.md#escala-de-calificación)).
- **Proyecto mínimo:** 65% en el proyecto final.
- **Notebooks:** Al menos 17 de 21 completados, cubriendo los 4 bloques.
- La revisión del proyecto se apoya en el checklist transversal: [`docs/checklist_revision_arquitectura.md`](../../docs/checklist_revision_arquitectura.md), tal como indica el README del nivel.

## Feedback

- Caso de estudio: retroalimentación en 5-7 días laborables.
- Notebooks: retroalimentación en 3-5 días laborables.
- Proyecto final: retroalimentación detallada en 10-14 días laborables, incluyendo notas de la presentación oral.

## Recursos de Apoyo

- Horas de oficina: según calendario del programa que adopte el curso.
- Foro de dudas en plataforma LMS.
- Material de referencia en `04-recursos/` y `docs/mejores_practicas_arquitectura_datos.md`.

---

**¡Éxito en tu evaluación!**
