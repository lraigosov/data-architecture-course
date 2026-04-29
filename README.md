# Curso Modular de Arquitectura de Datos

![Licencia](https://img.shields.io/badge/Licencia-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## Descripción

Curso práctico orientado a formar arquitectos de datos capaces de diseñar, implementar y gobernar arquitecturas modernas, escalables y auditables. El contenido combina fundamentos de DAMA-DMBOK con prácticas actuales de lakehouse, Data Mesh, observabilidad, FinOps, contratos de datos y preparación de plataformas para IA.

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
- **Temas clave:** OLTP vs OLAP, modelado conceptual/lógico/físico, modelado dimensional, calidad, seguridad, cloud, cultura data-driven, Big Data y streaming básico.

### 📗 Nivel Mid - Arquitecturas Híbridas
**Objetivo:** Diseñar arquitecturas de datos híbridas y modernas, con criterios explícitos para batch, streaming, lakehouse, Data Mesh, semántica, observabilidad y AI-readiness.
- **Ubicación:** [`02-nivel-mid/`](./02-nivel-mid/)
- **Temas clave:** Data Lakehouse, Lambda/Kappa, cloud/multi-cloud, contratos de datos, catálogo, linaje, seguridad, FinOps, feature stores y búsqueda vectorial.

### 📕 Nivel Senior - Gobierno y Estrategia
**Objetivo:** Liderar estrategias de gobierno, seguridad, optimización y operación de plataformas de datos empresariales.
- **Ubicación:** [`03-nivel-senior/`](./03-nivel-senior/)
- **Temas clave:** Gobierno federado, cumplimiento, FinOps, observabilidad, linaje, evolución arquitectónica, arquitectura empresarial para ML e IoT industrial.

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

- **Aprendizaje activo:** cada módulo combina explicación, ejemplo ejecutable, ejercicios y criterios de revisión.
- **Decisiones explícitas:** los diseños se justifican con trade-offs de costo, latencia, seguridad, gobierno y operación.
- **Evidencia verificable:** los conceptos técnicos se apoyan en documentación oficial, estándares o referencias primarias.
- **Casos aplicados:** los ejercicios trabajan escenarios de retail, manufactura, banca, IoT, analítica e IA.

---

## Evaluación

El curso propone la siguiente matriz de evaluación por nivel:

| Nivel  | Entregable Principal                            | Herramientas de Evaluación             |
| ------ | ----------------------------------------------- | -------------------------------------- |
| **Junior** | Modelo conceptual y lógico                      | Cuestionario + Notebook validado       |
| **Mid**    | Diseño arquitectónico híbrido                   | Revisión técnica y presentación oral   |
| **Senior** | Documento de arquitectura con gobierno y FinOps | Evaluación por pares + defensa técnica |

> **Criterio sugerido:** aprobar con al menos 70% en cada nivel antes de avanzar al siguiente.

---

## Recursos y Estándares

Para garantizar consistencia y calidad, consulta:

- **Glosario Técnico:** [`04-recursos/glosario.md`](./04-recursos/glosario.md)
- **Referencias:** [`04-recursos/referencias.md`](./04-recursos/referencias.md)
- **Mejores Prácticas:** [`docs/mejores_practicas_arquitectura_datos.md`](./docs/mejores_practicas_arquitectura_datos.md)
- **Estándar de Notebooks:** [`docs/estandar_notebooks.md`](./docs/estandar_notebooks.md)
- **Checklist de Revisión:** [`docs/checklist_revision_arquitectura.md`](./docs/checklist_revision_arquitectura.md)

---

## Contribuciones

¡Tu ayuda es bienvenida!
1. Lee [CONTRIBUTING.md](./CONTRIBUTING.md).
2. Revisa los issues abiertos.
3. Envía Pull Requests siguiendo el estándar del curso.

---

**Autor:** Luis Raigoso (@lraigosov)  
**Última actualización:** Abril 2026
