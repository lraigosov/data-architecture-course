# Nivel Junior - Fundamentos y Conceptos Clave

## Objetivo del Nivel

Comprender la base conceptual de la arquitectura de datos y su rol en el ecosistema empresarial.

## Contenidos del Módulo

### 1. Introducción a la Arquitectura de Datos
- Notebook: `01_introduccion_arquitectura_datos.ipynb`
- Qué es la arquitectura de datos
- Componentes principales
- Rol del arquitecto de datos vs ingeniero de datos

### 2. Sistemas Transaccionales vs Analíticos
- Notebook: `02_oltp_vs_olap.ipynb`
- Diferencias entre OLTP (Online Transaction Processing) y OLAP (Online Analytical Processing)
- Casos de uso y ejemplos prácticos
- Ejercicios comparativos

### 3. Fundamentos de Modelado de Datos
- Notebook: `03_fundamentos_modelado.ipynb`
- Conceptos de modelo de datos
- Metadatos y su importancia
- Calidad del dato

### 4. Tres Esquemas: Conceptual, Lógico y Físico
- Notebook: `04_modelado_tres_esquemas.ipynb`
- Vistas externas, modelo conceptual (ERD) y modelo físico
- Normalización (1FN–3FN) con ejemplos
- Ejercicio práctico breve

### 5. Modelado Dimensional (Analítica)
- Notebook: `05_modelado_dimensional.ipynb`
- Hechos y dimensiones, granularidad
- Esquema estrella y copo de nieve; cuándo desnormalizar
- Optimización para analítica y ejercicio guiado

### 6. Fundamentos de Calidad de Datos
- Notebook: `06_fundamentos_calidad_datos.ipynb`
- Dimensiones de calidad (precisión, completitud, consistencia, validez, unicidad, puntualidad)
- Medición de calidad con métricas cuantitativas
- Reglas de calidad como assertions
- Estrategias de corrección (imputación, deduplicación, filtrado)

### 7. Fundamentos de Seguridad y Privacidad de Datos
- Notebook: `07_fundamentos_seguridad_privacidad.ipynb`
- Conceptos de seguridad de datos y riesgos comunes
- Tipos de datos sensibles (PII, PCI, PHI) y clasificación
- Principios de privacidad (GDPR) y derechos de titulares
- Controles básicos: autenticación, autorización, encriptación, pseudonimización
- Amenazas comunes y mitigaciones

### 8. Fundamentos de Escalabilidad y Rendimiento
- Notebook: `08_fundamentos_escalabilidad_rendimiento.ipynb`
- Escalabilidad vertical vs horizontal (cuándo usar cada una)
- Los 3 V del Big Data: Volumen, Velocidad, Variedad
- Dimensionamiento básico de recursos: storage, compute, network
- Métricas de rendimiento: throughput, latencia, P95/P99, disponibilidad
- Introducción a costos en la nube: componentes (storage, compute, egress)
- Trade-offs rendimiento vs costo
- Estrategias básicas de optimización

### 9. Introducción a Patrones Arquitectónicos
- Notebook: `09_introduccion_patrones_arquitectonicos.ipynb`
- ¿Qué son los patrones arquitectónicos? Ventajas y desventajas
- Arquitectura en capas: Bronze / Silver / Gold (Medallion Architecture)
- Monolítica vs Distribuida: comparación y trade-offs
- Event-Driven Architecture: eventos como mecanismo de comunicación
- Reutilización de datos: DRY y Single Source of Truth (SSOT)
- Ejercicio práctico: transformación Bronze → Silver → Gold con datos e-commerce

### 10. Modelos de Dominio, Ontologías y Taxonomías (Fundamentos)
- Notebook: `10_modelos_dominio_ontologias_taxonomias.ipynb`
- Diferencias: dominio vs modelo de dominio vs taxonomía vs ontología vs glosario
- Beneficios para la estrategia: alineación a KPIs, ownership, calidad, integración y evolución
- DDD básico aplicado a datos: bounded contexts, ubiquitous language, aggregates
- Construcción de una taxonomía sencilla y validación con código (Python)
- Ejercicio: glosario mínimo y clasificación para un caso bancario

## Ejercicios Prácticos

Cada notebook incluye:
- Teoría fundamentada
- Ejemplos visuales
- Ejercicios guiados paso a paso
- Retos de aplicación

## Entregable del Nivel

**Proyecto:** Diseño de un modelo conceptual y lógico para un caso de negocio

**Componentes:**
1. Modelo conceptual (ERD)
2. Modelo lógico normalizado
3. Modelo dimensional (estrella o copo de nieve)
4. Documentación de decisiones de diseño

## Evaluación

- **Cuestionario teórico:** 40%
- **Notebooks completados:** 30%
- **Proyecto final:** 30%

Ver detalles en: [Evaluación Nivel Junior](../05-evaluaciones/junior/)

## Requisitos Previos

- Conocimientos básicos de bases de datos
- SQL básico (SELECT, JOIN)
- Comprensión de conceptos de negocio

## Tiempo Estimado

**Duración total:** 4-6 semanas (20-25 horas de estudio)

## Recursos Adicionales

- [Glosario de términos](../04-recursos/glosario.md)
- [Referencias bibliográficas](../04-recursos/referencias.md)
