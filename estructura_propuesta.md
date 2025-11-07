# Canvas del Curso Modular de Arquitectura de Datos

## 1. Propósito del Programa

Formar profesionales capaces de diseñar, implementar y gobernar arquitecturas de datos modernas, seguras, escalables y alineadas con los marcos DAMA-DMBOK y las mejores prácticas de la industria. Este curso no incluye contenidos de **Ingeniería de Datos**, los cuales se abordan en un programa complementario.

---

## 2. Estructura Modular del Programa

El curso se organiza en tres niveles progresivos: **Junior**, **Mid**, y **Senior**, con un enfoque teórico-práctico soportado en **Notebooks interactivos (Jupyter o Colab)** y proyectos reales.

### Nivel Junior: Fundamentos y Conceptos Clave

**Objetivo:** Comprender la base conceptual de la arquitectura de datos y su rol en el ecosistema empresarial.

* Introducción a la Arquitectura de Datos y sus componentes.
* Diferencias entre sistemas transaccionales (OLTP) y analíticos (OLAP).
* Conceptos de modelo de datos, metadatos y calidad del dato.
* Diseño de modelos conceptuales y lógicos (ERD, modelos en estrella y copo de nieve).
* **Fundamentos de calidad de datos:** Dimensiones (precisión, completitud, consistencia, validez, unicidad, puntualidad), medición y corrección.
* Ejercicios prácticos: modelado de datos simple con herramientas visuales.

### Nivel Mid: Arquitecturas y Estrategias de Integración

**Objetivo:** Diseñar arquitecturas de datos híbridas y modernas aplicando buenas prácticas.

* Tipologías de arquitecturas: monolítica, orientada a servicios, orientada a eventos y microservicios.
* Diferencias entre Data Warehouse, Data Lake y Data Lakehouse.
* Arquitecturas Lambda y Kappa (procesamiento batch y streaming).
* Introducción a arquitecturas cloud y multi-cloud.
* Diseño de capas de datos: Raw, Curated, Trusted, Gold.
* **Metadatos, catálogo y linaje:** Tipos de metadatos (técnicos, negocio, operacionales), catálogo centralizado, data lineage (auditoría, impacto, trazabilidad), herramientas (OpenLineage, Atlas, Amundsen, DataHub).
* Casos de estudio con notebooks de exploración arquitectónica.

### Nivel Senior: Gobierno, Escalabilidad y Observabilidad

**Objetivo:** Liderar gobierno, seguridad, optimización y operación confiable de plataformas de datos a escala.

**Contenidos actuales (notebooks):**
1. Gobernanza, seguridad y cumplimiento → `03-nivel-senior/01_gobernanza_seguridad_cumplimiento.ipynb`
   - **Roles y responsabilidades detalladas:** Data Owner, Steward, Custodian, Governance Lead, matriz RACI.
   - **Políticas de datos:** Clasificación, acceso, retención, calidad (definición y enforcement).
   - **Procedimientos (workflows):** Solicitud de acceso, cambio de esquema, quality gates.
   - **Herramientas de gobernanza:** Catálogo (Atlan, Collibra, DataHub), calidad (Great Expectations, Soda), lineage (OpenLineage, Marquez), seguridad (Ranger, Privacera).
   - Dashboard de métricas de gobierno.
2. Escalabilidad, rendimiento y costos (FinOps) → `03-nivel-senior/02_escalabilidad_rendimiento_costos.ipynb`
3. Observabilidad, lineage y automatización → `03-nivel-senior/03_observabilidad_lineage_automatizacion.ipynb`

**Recursos de apoyo:**
- Dataset de ejemplo: `04-recursos/datasets/ejemplo_ventas.csv` (para demos de frescura/calidad/alertas)

**Próximas extensiones:**
- Taller integral end-to-end con decisiones arquitectónicas y trade-offs
- Ampliación de contratos de datos y catálogo activo

---

## 3. Metodología de Aprendizaje

* **Aprendizaje activo:** cada tema incluye teoría validada, ejercicios guiados y evaluación aplicada.
* **Laboratorios interactivos:** notebooks con simulaciones y análisis de arquitecturas.
* **Casos de uso reales:** proyectos de referencia basados en retail, manufactura y banca.
* **Evaluaciones progresivas:** rúbricas de desempeño por nivel (Junior/Mid/Senior).

---

## 4. Entregables y Evaluación

| Nivel  | Entregable Principal                            | Herramientas de Evaluación             |
| ------ | ----------------------------------------------- | -------------------------------------- |
| Junior | Modelo conceptual y lógico                      | Cuestionario + notebook validado       |
| Mid    | Diseño arquitectónico híbrido                   | Revisión técnica y presentación oral   |
| Senior | Documento de arquitectura con gobierno y FinOps | Evaluación por pares + defensa técnica |

---

## 5. Tecnologías de Soporte

* **Visualización y diseño:** Lucidchart, Draw.io, Diagrams.net
* **Notebooks interactivos:** Jupyter, Google Colab
* **Gobernanza y documentación:** Atlan, Collibra, Google Data Catalog
* **Gestión y seguimiento:** GitHub Classroom, Notion, Trello

---

## 6. Cierre del Programa

Los estudiantes culminarán con la capacidad de:

* Evaluar y diseñar arquitecturas de datos completas.
* Integrar componentes de gobierno, calidad y seguridad.
* Liderar decisiones estratégicas en entornos cloud y multi-cloud.

> **Nota:** Para la implementación técnica, pipelines, procesamiento o automatización, se debe remitir al curso de **Ingeniería de Datos**, complementario a este programa.
