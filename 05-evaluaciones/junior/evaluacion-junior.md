# Evaluación Nivel Junior

## Componentes de Evaluación

### 1. Cuestionario Teórico (40%)

**Formato:** Multiple choice + preguntas cortas  
**Duración:** 90 minutos  
**Temas evaluados:**

- Conceptos de arquitectura de datos (20%)
- OLTP vs OLAP (20%)
- Modelado de datos y metadatos (30%)
- Calidad del dato (15%)
- Modelos ERD y dimensionales (15%)

**Criterios:**
- Comprensión de conceptos fundamentales
- Capacidad de distinguir entre diferentes enfoques
- Aplicación de teoría a casos prácticos

### 2. Notebooks Completados (30%)

**Notebooks requeridos:**
1. `01_introduccion_arquitectura_datos.ipynb` (6%)
2. `02_oltp_vs_olap.ipynb` (6%)
3. `03_fundamentos_modelado.ipynb` (6%)
4. `04_modelos_erd.ipynb` (6%)
5. `05_modelos_estrella_copo_nieve.ipynb` (6%)

**Criterios por notebook:**
- Todos los ejercicios completados (40%)
- Código ejecutable sin errores (30%)
- Respuestas correctas a preguntas (20%)
- Documentación y comentarios (10%)

### 3. Proyecto Final: Modelo Conceptual y Lógico (30%)

**Descripción:**
Diseñar un modelo de datos completo para un caso de negocio asignado (retail, manufactura o banca).

**Entregables:**

#### A. Modelo Conceptual (10%)
- Diagrama ERD de alto nivel
- Identificación de entidades principales
- Relaciones y cardinalidades
- Reglas de negocio documentadas

#### B. Modelo Lógico (10%)
- Diagrama ERD detallado con atributos
- Tipos de datos especificados
- Llaves primarias y foráneas
- Normalización justificada (hasta 3FN)

#### C. Modelo Dimensional (10%)
- Diseño de modelo estrella o copo de nieve
- Tabla(s) de hechos con métricas
- Tablas de dimensión
- Justificación del diseño elegido

**Formato de entrega:**
- Archivo PDF con diagramas
- Documento Word/Markdown con explicaciones
- (Opcional) Archivos de herramienta de modelado (.erdplus, .drawio)

---

## Rúbrica Detallada del Proyecto

### Modelo Conceptual (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Identificación de Entidades** | Todas las entidades relevantes identificadas y bien nombradas | La mayoría de entidades identificadas, nombres apropiados | Entidades principales presentes, algunos nombres poco claros | Entidades importantes faltantes o mal definidas |
| **Relaciones** | Todas las relaciones correctamente identificadas con cardinalidades precisas | La mayoría de relaciones correctas, cardinalidades mayormente precisas | Relaciones principales presentes, algunas cardinalidades incorrectas | Relaciones importantes faltantes o incorrectas |
| **Claridad del Diagrama** | Diagrama muy claro, profesional, fácil de entender | Diagrama claro y legible | Diagrama comprensible con esfuerzo | Diagrama confuso o difícil de leer |
| **Documentación** | Reglas de negocio completamente documentadas | La mayoría de reglas documentadas | Documentación básica presente | Documentación insuficiente |

### Modelo Lógico (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Atributos** | Todos los atributos necesarios, bien nombrados y tipos apropiados | La mayoría de atributos correctos | Atributos principales presentes, algunos tipos incorrectos | Atributos importantes faltantes |
| **Llaves** | PKs y FKs correctamente definidas en todas las tablas | La mayoría de llaves correctas | Llaves principales definidas, algunas incorrectas | Llaves mal definidas o faltantes |
| **Normalización** | Correctamente normalizado a 3FN con justificación clara | Normalización correcta, justificación básica | Parcialmente normalizado | Problemas graves de normalización |
| **Integridad** | Todas las restricciones y reglas de integridad definidas | La mayoría de restricciones definidas | Restricciones básicas presentes | Restricciones importantes faltantes |

### Modelo Dimensional (10 puntos)

| Criterio | Excelente (9-10) | Bueno (7-8) | Satisfactorio (5-6) | Necesita Mejora (< 5) |
|----------|------------------|-------------|---------------------|----------------------|
| **Diseño de Hechos** | Tabla(s) de hechos con todas las métricas relevantes y granularidad apropiada | La mayoría de métricas presentes, granularidad adecuada | Tabla de hechos básica con métricas principales | Tabla de hechos mal diseñada |
| **Diseño de Dimensiones** | Dimensiones completas, conformadas donde aplica, SCDs considerados | Dimensiones bien diseñadas | Dimensiones básicas presentes | Dimensiones incompletas o mal diseñadas |
| **Elección de Modelo** | Justificación clara de estrella vs copo de nieve, decisión apropiada | Buena justificación de la elección | Justificación básica | Sin justificación o elección inapropiada |
| **Escalabilidad** | Diseño considera crecimiento futuro y performance | Consideraciones básicas de escalabilidad | Diseño funcional sin considerar futuro | Sin consideraciones de escalabilidad |

---

## Ejemplos de Preguntas del Cuestionario

### Sección 1: Conceptos Fundamentales

**Pregunta 1 (Multiple Choice):**
¿Cuál de las siguientes NO es una capa típica de una arquitectura de datos?

a) Capa de Ingesta  
b) Capa de Almacenamiento  
c) Capa de Compilación  
d) Capa de Consumo

**Respuesta correcta:** c) Capa de Compilación

---

**Pregunta 2 (Pregunta Corta):**
Explica en 2-3 frases la diferencia principal entre el rol de un Arquitecto de Datos y un Ingeniero de Datos.

**Respuesta esperada:**
El Arquitecto de Datos se enfoca en el diseño estratégico y conceptual, definiendo QUÉ estructura necesita la organización y POR QUÉ. El Ingeniero de Datos se enfoca en la implementación y operación, construyendo CÓMO se implementa esa arquitectura mediante pipelines, código y automatización.

---

### Sección 2: OLTP vs OLAP

**Pregunta 3 (Multiple Choice):**
Un sistema que procesa 5,000 transacciones de venta por segundo con consultas simples tipo INSERT/UPDATE es un ejemplo de:

a) OLTP  
b) OLAP  
c) Data Lake  
d) ETL

**Respuesta correcta:** a) OLTP

---

**Pregunta 4 (Verdadero/Falso):**
Los sistemas OLAP típicamente usan modelos de datos normalizados en 3FN para optimizar el rendimiento de consultas analíticas.

**Respuesta correcta:** Falso (OLAP usa modelos desnormalizados como estrella/copo de nieve)

---

### Sección 3: Calidad de Datos

**Pregunta 5 (Matching):**
Relaciona cada dimensión de calidad con su descripción:

| Dimensión | Descripción |
|-----------|-------------|
| 1. Exactitud | A. Los datos están actualizados |
| 2. Completitud | B. No hay registros duplicados |
| 3. Vigencia | C. Todos los campos requeridos tienen valor |
| 4. Unicidad | D. Los datos reflejan la realidad correctamente |

**Respuesta correcta:** 1-D, 2-C, 3-A, 4-B

---

## Instrucciones de Entrega

### Formato
- **Cuestionario:** Se realiza en plataforma online (tiempo limitado)
- **Notebooks:** Subir archivos .ipynb ejecutados a repositorio GitHub
- **Proyecto:** Subir PDF + documento explicativo a plataforma LMS

### Plazos
- **Notebooks:** Al finalizar cada módulo (progresivo)
- **Cuestionario:** Última semana del nivel
- **Proyecto:** 2 semanas después de completar todos los notebooks

### Naming Convention
```
apellido_nombre_junior_proyecto.pdf
apellido_nombre_junior_explicacion.docx
apellido_nombre_01_introduccion.ipynb
```

---

## Criterios de Aprobación

- **Calificación mínima:** 70%
- **Proyecto mínimo:** 60% en el proyecto final
- **Notebooks:** Al menos 4 de 5 completados

## Feedback

- Resultados del cuestionario: Inmediatos (automático)
- Notebooks: Retroalimentación en 3-5 días laborables
- Proyecto: Retroalimentación detallada en 7-10 días laborables

## Recursos de Apoyo

- Horas de oficina: Martes y Jueves 16:00-18:00
- Foro de dudas en plataforma LMS
- Material de referencia en carpeta `04-recursos/`

---

**¡Éxito en tu evaluación!**
