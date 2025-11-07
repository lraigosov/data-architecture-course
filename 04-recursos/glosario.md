# Glosario de Arquitectura de Datos

## A

**Agregación:** Proceso de combinar múltiples registros de datos en un resumen o total.

**Arquitectura de Datos:** Diseño estructural que define cómo se capturan, almacenan, integran, transforman y acceden los datos dentro de una organización.

**Arquitectura Lambda:** Patrón arquitectónico que combina procesamiento batch y streaming para manejar grandes volúmenes de datos.

**Atributo:** Característica o propiedad de una entidad en un modelo de datos.

## B

**Batch Processing:** Procesamiento por lotes, donde los datos se procesan en grupos en intervalos programados.

**BI (Business Intelligence):** Conjunto de herramientas y procesos para transformar datos en información útil para la toma de decisiones.

## C

**Calidad del Dato:** Grado en que los datos son aptos para su uso previsto.

**Capa de Datos:** Nivel lógico en una arquitectura que agrupa datos con características similares (Raw, Curated, Trusted, Gold).

**Cardinalidad:** Número de instancias de una entidad que pueden relacionarse con instancias de otra entidad.

**Catálogo de Datos:** Inventario organizado de activos de datos con metadatos descriptivos.

**CDC (Change Data Capture):** Técnica para identificar y capturar cambios en los datos.

**Clave Foránea (Foreign Key):** Atributo que hace referencia a la clave primaria de otra tabla.

**Clave Primaria (Primary Key):** Atributo o conjunto de atributos que identifican únicamente un registro.

**Clave Surogada:** Identificador artificial creado para actuar como clave primaria.

## D

**DAMA-DMBOK:** Marco de referencia para la gestión de datos desarrollado por DAMA International.

**Data Lake:** Repositorio centralizado que almacena datos estructurados y no estructurados a escala.

**Data Lakehouse:** Arquitectura que combina características de Data Warehouse y Data Lake.

**Data Lineage:** Seguimiento del origen, movimientos y transformaciones de los datos a lo largo de su ciclo de vida.

**Data Mart:** Subconjunto de un Data Warehouse enfocado en un área de negocio específica.

**Data Warehouse:** Repositorio centralizado de datos integrados, históricos y orientado a consultas analíticas.

**Desnormalización:** Proceso de agregar redundancia a un modelo normalizado para mejorar el rendimiento de lectura.

**Dimensión:** En modelado dimensional, tabla que contiene atributos descriptivos (quién, qué, dónde, cuándo).

**Dimensión Conformada:** Dimensión compartida entre múltiples procesos de negocio.

**Dimensión de Cambio Lento (SCD):** Técnica para manejar cambios en dimensiones a lo largo del tiempo.

## E

**ELT (Extract, Load, Transform):** Proceso donde los datos se extraen, cargan en destino y luego se transforman.

**Entidad:** Objeto o concepto del mundo real que puede ser identificado y sobre el cual se almacena información.

**ERD (Entity-Relationship Diagram):** Diagrama que representa entidades y sus relaciones.

**Esquema en Copo de Nieve (Snowflake):** Modelo dimensional donde las dimensiones están normalizadas.

**Esquema en Estrella (Star Schema):** Modelo dimensional con una tabla de hechos central rodeada de tablas de dimensión.

**ETL (Extract, Transform, Load):** Proceso de extracción, transformación y carga de datos.

## F

**FinOps:** Práctica de gestión financiera cloud que optimiza costos.

**Formas Normales (1FN, 2FN, 3FN):** Niveles de normalización que eliminan redundancia y anomalías.

## G

**Gobierno de Datos:** Conjunto de procesos, políticas y estándares que aseguran la gestión efectiva de los activos de datos.

**Granularidad:** Nivel de detalle de los datos almacenados.

## H

**Hechos (Facts):** En modelado dimensional, métricas o medidas numéricas del negocio.

## I

**Índice:** Estructura de base de datos que mejora la velocidad de recuperación de datos.

**Integridad Referencial:** Garantía de que las relaciones entre tablas permanecen consistentes.

## K

**Kappa (Arquitectura):** Patrón arquitectónico que usa solo streaming para procesamiento de datos.

## L

**Lago de Datos (Data Lake):** Ver Data Lake.

**Linaje de Datos:** Ver Data Lineage.

## M

**MDM (Master Data Management):** Gestión de datos maestros para asegurar consistencia.

**Metadatos:** Datos que describen otros datos (estructura, origen, calidad, etc.).

**Modelo Conceptual:** Representación de alto nivel de entidades y relaciones del negocio.

**Modelo Dimensional:** Técnica de modelado optimizada para consultas analíticas (estrella, copo de nieve).

**Modelo Físico:** Implementación específica de un modelo en un DBMS particular.

**Modelo Lógico:** Modelo de datos independiente de tecnología con atributos y tipos definidos.

## N

**Normalización:** Proceso de organizar datos para reducir redundancia y mejorar integridad.

## O

**OLAP (Online Analytical Processing):** Sistemas diseñados para consultas analíticas complejas.

**OLTP (Online Transaction Processing):** Sistemas diseñados para transacciones operacionales en tiempo real.

## P

**Partición:** División de tablas grandes en segmentos más pequeños para mejorar rendimiento.

**PII (Personally Identifiable Information):** Información que puede identificar a un individuo.

## R

**RBAC (Role-Based Access Control):** Control de acceso basado en roles.

**Relación:** Asociación entre dos o más entidades.

**Resiliencia:** Capacidad de un sistema para recuperarse de fallos.

## S

**SCD (Slowly Changing Dimension):** Ver Dimensión de Cambio Lento.

**Streaming:** Procesamiento de datos en tiempo real conforme llegan.

## T

**Tabla de Hechos:** Tabla central en modelo dimensional que contiene métricas.

**Tipo de Dato:** Clasificación que especifica qué tipo de valor puede contener un atributo.

## W

**Warehouse:** Ver Data Warehouse.

---

## Referencias

- DAMA International. (2017). *DAMA-DMBOK: Data Management Body of Knowledge* (2nd ed.)
- Kimball, R., & Ross, M. (2013). *The Data Warehouse Toolkit* (3rd ed.)
- Inmon, W. H. (2005). *Building the Data Warehouse* (4th ed.)
