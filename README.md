# Curso Modular de Arquitectura de Datos

![Licencia](https://img.shields.io/badge/Licencia-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## Descripción

Curso práctico para formar arquitectos de datos capaces de diseñar, implementar y gobernar arquitecturas modernas, siguiendo el marco DAMA-DMBOK y las mejores prácticas de la industria.

> **Nota:** Este curso se enfoca en Arquitectura de Datos. Los contenidos de Ingeniería de Datos (pipelines, ETL, automatización) se abordan en un programa complementario.

## Estructura del Curso

El programa se organiza en **tres niveles progresivos**:

### 📘 Nivel Junior - Fundamentos (4-6 semanas)

**Objetivo:** Comprender la base conceptual de la arquitectura de datos.

**Contenidos disponibles:**
- ✅ Introducción a la Arquitectura de Datos
- ✅ OLTP vs OLAP  
- ✅ Fundamentos de Modelado de Datos

**Ubicación:** [`01-nivel-junior/`](./01-nivel-junior/)

### 🆕 Novedades destacadas (Q4 2025)
- Big Data de última generación (formatos columnares y frameworks): `01-nivel-junior/16_fundamentos_big_data_nube.ipynb`, `02-nivel-mid/16_frameworks_big_data_modernos_comparativo.ipynb`
- Arquitecturas descentralizadas y Gov-Ready (Data Mesh, Data Fabric, Capa Semántica): `01-nivel-junior/17_intro_arquitecturas_descentralizadas_data_mesh_fabric_semantica.ipynb`, `02-nivel-mid/17_mini_data_mesh_dos_dominios_catalogo_compartido.ipynb`, `03-nivel-senior/13_transicion_centralizado_a_mesh_fabric_taller_evaluacion.ipynb`
- Observabilidad, Metadata, Linaje y Gobierno para IA/Big Data: `02-nivel-mid/18_observabilidad_metadata_linaje_ia_bigdata_simulacion.ipynb`, `03-nivel-senior/14_gobernanza_ia_ready_politicas_privacidad_sesgo_taller.ipynb`
- Tiempo real, Edge & Streaming para IA/Big Data: `01-nivel-junior/18_fundamentos_streaming_edge_cloud.ipynb`, `02-nivel-mid/19_streaming_inferencia_tiempo_real_caso_practico.ipynb`, `03-nivel-senior/15_arquitectura_iot_industrial_streaming_edge_taller.ipynb`

### 📗 Nivel Mid - Arquitecturas (6-8 semanas)

**Objetivo:** Diseñar arquitecturas híbridas y modernas.

**Temas planificados:**
- Tipologías de arquitecturas
- Data Warehouse, Data Lake, Data Lakehouse
- Arquitecturas Lambda y Kappa
- Cloud y Multi-cloud
- Capas de datos (Raw, Curated, Trusted, Gold)

**Ubicación:** [`02-nivel-mid/`](./02-nivel-mid/)

### 📕 Nivel Senior - Gobierno, Escalabilidad y Observabilidad (8-10 semanas)

**Objetivo:** Liderar estrategias de gobierno, seguridad, optimización y operación confiable a escala.

**Contenidos disponibles:**
- ✅ Gobernanza, seguridad y cumplimiento → `03-nivel-senior/01_gobernanza_seguridad_cumplimiento.ipynb`
- ✅ Escalabilidad, rendimiento y costos (FinOps) → `03-nivel-senior/02_escalabilidad_rendimiento_costos.ipynb`
- ✅ Observabilidad, lineage y automatización → `03-nivel-senior/03_observabilidad_lineage_automatizacion.ipynb`

Recursos de apoyo:
- Dataset de ejemplo para métricas: `04-recursos/datasets/ejemplo_ventas.csv`

**Ubicación:** [`03-nivel-senior/`](./03-nivel-senior/)

## Instalación

### Requisitos Previos

**Conocimientos:**
- Bases de datos básicas
- SQL básico (SELECT, JOIN)
- Python básico (recomendado)

**Software:**
- Python 3.8+
- Jupyter Notebook o Google Colab
- Git

### Opción 1: Instalación Local

```bash
# Clonar el repositorio
git clone https://github.com/lraigosov/data-architecture-course.git
cd data-architecture-course

# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar Jupyter
jupyter notebook
```

### Opción 2: Google Colab (sin instalación)

1. Ir a [Google Colab](https://colab.research.google.com/)
2. Archivo > Abrir notebook > GitHub
3. Pegar: `https://github.com/lraigosov/data-architecture-course`
4. Seleccionar el notebook deseado

## Primeros Pasos

1. Comienza con [`01-nivel-junior/01_introduccion_arquitectura_datos.ipynb`](./01-nivel-junior/01_introduccion_arquitectura_datos.ipynb)
2. Completa los notebooks en orden
3. Realiza todos los ejercicios
4. Consulta el [glosario](./04-recursos/glosario.md) para términos técnicos

## Guía Rápida

### Para Estudiantes
1. Completa los notebooks de `01-nivel-junior/` en orden
2. Realiza todos los ejercicios prácticos
3. Consulta recursos en `04-recursos/` cuando sea necesario
4. Revisa las evaluaciones en `05-evaluaciones/`

### Para Instructores
- Cada nivel tiene su README con estructura completa
- Sistema de evaluación disponible en `05-evaluaciones/`
- Casos de uso en `04-recursos/casos-uso/`
- Rúbricas detalladas por nivel

### Para Contribuidores
- Lee [CONTRIBUTING.md](./CONTRIBUTING.md)
- Revisa issues abiertos en GitHub
- Envía pull requests con mejoras

## Recursos Adicionales

- **Glosario:** [`04-recursos/glosario.md`](./04-recursos/glosario.md) - 50+ términos técnicos
- **Referencias:** [`04-recursos/referencias.md`](./04-recursos/referencias.md) - Bibliografía curada
- **Casos de uso:** [`04-recursos/casos-uso/`](./04-recursos/casos-uso/) - Escenarios reales

## Preguntas Frecuentes

**¿Necesito experiencia previa?**  
Solo conocimientos básicos de bases de datos y SQL.

**¿Cuánto tiempo requiere?**  
- Nivel Junior: 5-7 horas/semana durante 4-6 semanas
- Nivel Mid: 6-8 horas/semana durante 6-8 semanas  
- Nivel Senior: 8-10 horas/semana durante 8-10 semanas

**¿Puedo usar Google Colab?**  
Sí, todos los notebooks son compatibles.

**¿Hay certificado?**  
Al completar cada nivel con >= 70% de calificación.

## Evaluación

Cada nivel incluye:
- Cuestionarios teóricos
- Ejercicios prácticos en notebooks
- Proyecto final

Ver detalles en [`05-evaluaciones/`](./05-evaluaciones/)

## Metodología

- **Aprendizaje activo:** Teoría + ejercicios + evaluación
- **Notebooks interactivos:** Jupyter con código ejecutable
- **Casos reales:** Retail, manufactura, banca
- **Evaluación progresiva:** Por nivel

## Licencia

Este proyecto está bajo licencia MIT. Ver [LICENSE](./LICENSE) para más detalles.

## Contribuciones

Las contribuciones son bienvenidas. Consulta [CONTRIBUTING.md](./CONTRIBUTING.md) para las guías.

---

**Autor:** Luis Raigoso (@lraigosov)  
**Última actualización:** Noviembre 2025
