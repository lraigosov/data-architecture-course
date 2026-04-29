# Curso Modular de Arquitectura de Datos

![Licencia](https://img.shields.io/badge/Licencia-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## Descripción

Curso práctico orientado a formar arquitectos de datos capaces de diseñar, implementar y gobernar arquitecturas modernas, escalables y alineadas con los marcos DAMA-DMBOK y las mejores prácticas de la industria.

> **Nota:** Este curso se enfoca en **Arquitectura de Datos**. Los contenidos de Ingeniería de Datos (pipelines, ETL, automatización) se abordan en un programa complementario.

## Tabla de Contenidos

1. [Estructura del Curso](#estructura-del-curso)
2. [Guía de Inicio Rápido](#guía-de-inicio-rápido)
3. [Metodología](#metodología)
4. [Evaluación](#evaluación)
5. [Recursos y Estándares](#recursos-y-estándares)
6. [Contribuciones](#contribuciones)

---

## Estructura del Curso

El programa se organiza en **tres niveles progresivos**:

### 📘 Nivel Junior - Fundamentos
**Objetivo:** Comprender la base conceptual de la arquitectura de datos y su rol en el ecosistema empresarial.
- **Ubicación:** [`01-nivel-junior/`](./01-nivel-junior/)
- **Temas Clave:** OLTP vs OLAP, Modelado (ERD, Dimensional), Calidad de Datos, Seguridad básica.
- **Novedades:** Big Data, Streaming básico.

### 📗 Nivel Mid - Arquitecturas Híbridas
**Objetivo:** Diseñar arquitecturas de datos híbridas y modernas (Data Mesh, Fabric, Lakehouse).
- **Ubicación:** [`02-nivel-mid/`](./02-nivel-mid/)
- **Temas Clave:** Data Lakehouse, Lambda/Kappa, Cloud/Multi-cloud, Capas de datos (Raw/Curated/Gold).
- **Novedades:** Interoperabilidad, Catálogos de datos.

### 📕 Nivel Senior - Gobierno y Estrategia
**Objetivo:** Liderar estrategias de gobierno, seguridad, optimización (FinOps) y operación a escala.
- **Ubicación:** [`03-nivel-senior/`](./03-nivel-senior/)
- **Temas Clave:** Gobernanza avanzada, FinOps, Observabilidad, Linaje, Estrategia de IA.

---

## Guía de Inicio Rápido

### Requisitos
- **Software:** Python 3.8+, Git.
- **Opcional:** Jupyter Notebook o acceso a Google Colab.

### Instalación Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/lraigosov/data-architecture-course.git
   cd data-architecture-course
   ```

2. **Configurar entorno:**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar instalación:**
   Ejecuta el smoke test para validar que los helpers funcionan correctamente.
   ```bash
   python tests/smoke_test.py
   ```

### Opción Google Colab
Puedes abrir cualquier notebook directamente en Colab pegando la URL del archivo desde GitHub en [Google Colab](https://colab.research.google.com/).

---

## Metodología

- **Aprendizaje Activo:** Cada módulo incluye teoría validada, ejercicios guiados y evaluación aplicada.
- **Notebooks Interactivos:** Todo el contenido práctico se entrega en Jupyter Notebooks ejecutables.
- **Casos Reales:** Proyectos de referencia basados en industrias como Retail, Manufactura y Banca.

---

## Evaluación

El curso propone la siguiente matriz de evaluación por nivel:

| Nivel  | Entregable Principal                            | Herramientas de Evaluación             |
| ------ | ----------------------------------------------- | -------------------------------------- |
| **Junior** | Modelo conceptual y lógico                      | Cuestionario + Notebook validado       |
| **Mid**    | Diseño arquitectónico híbrido                   | Revisión técnica y presentación oral   |
| **Senior** | Documento de arquitectura con gobierno y FinOps | Evaluación por pares + defensa técnica |

> **Certificación:** Se recomienda aprobar con >= 70% en cada nivel.

---

## Recursos y Estándares

Para garantizar consistencia y calidad, consulta:

- **Glosario Técnico:** [`04-recursos/glosario.md`](./04-recursos/glosario.md)
- **Mejores Prácticas:** [`docs/mejores_practicas_arquitectura_datos.md`](./docs/mejores_practicas_arquitectura_datos.md)
- **Estándar de Notebooks:** [`docs/estandar_notebooks.md`](./docs/estandar_notebooks.md)

---

## Contribuciones

¡Tu ayuda es bienvenida!
1. Lee [CONTRIBUTING.md](./CONTRIBUTING.md).
2. Revisa los issues abiertos.
3. Envía Pull Requests siguiendo el estándar del curso.

---

**Autor:** Luis Raigoso (@lraigosov)
**Última actualización:** Diciembre 2025
