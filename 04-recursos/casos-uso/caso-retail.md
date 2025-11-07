# Caso de Uso: Sistema de Ventas Omnicanal - Retail

## Contexto del Negocio

**Empresa:** RetailCorp  
**Industria:** Retail / E-commerce  
**Tamaño:** 150 tiendas físicas + plataforma online  
**Desafío:** Integrar datos de múltiples canales para análisis unificado

## Problema a Resolver

RetailCorp opera en múltiples canales:
- 150 tiendas físicas con sistemas POS (Point of Sale)
- Sitio web e-commerce
- Aplicación móvil
- Marketplace (Amazon, MercadoLibre)
- Redes sociales con venta integrada

**Desafíos actuales:**
1. Datos aislados en cada canal (silos de información)
2. Imposibilidad de ver el recorrido completo del cliente
3. Inventario desincronizado entre canales
4. Reportes manuales que toman días en generarse
5. Sin visibilidad en tiempo real de ventas

## Objetivos del Proyecto

### Objetivos de Negocio
- 📊 Vista unificada de ventas cross-canal
- 👥 Perfil 360° de clientes
- 📦 Sincronización de inventario en tiempo real
- 📈 Dashboards ejecutivos actualizados cada hora
- 🎯 Personalización de campañas de marketing

### Objetivos Técnicos
- Integrar 5 fuentes de datos diferentes
- Procesar 1M+ transacciones diarias
- Latencia < 15 minutos para datos críticos
- Disponibilidad 99.9%
- Costo operativo optimizado

## Fuentes de Datos

### 1. Sistemas POS (Tiendas Físicas)
- **Formato:** SQL Server (bases locales)
- **Volumen:** ~50K transacciones/día
- **Frecuencia:** Sincronización cada 15 minutos
- **Datos clave:** 
  - Transacciones de venta
  - Inventario por tienda
  - Datos de empleados

### 2. E-commerce (Sitio Web)
- **Formato:** PostgreSQL + Logs en JSON
- **Volumen:** ~30K pedidos/día
- **Frecuencia:** Streaming en tiempo real
- **Datos clave:**
  - Pedidos online
  - Sesiones de usuario
  - Carrito abandonado
  - Eventos de navegación

### 3. Aplicación Móvil
- **Formato:** Firebase / MongoDB
- **Volumen:** ~100K eventos/día
- **Frecuencia:** Streaming
- **Datos clave:**
  - Eventos de app
  - Compras in-app
  - Geolocalización
  - Notificaciones push

### 4. Marketplaces
- **Formato:** APIs REST (JSON)
- **Volumen:** ~20K pedidos/día
- **Frecuencia:** Batch cada hora
- **Datos clave:**
  - Pedidos externos
  - Reviews y calificaciones
  - Devoluciones

### 5. ERP (Sistema Central)
- **Formato:** SAP / Oracle
- **Volumen:** Master data + transacciones
- **Frecuencia:** Batch diario + CDC para críticos
- **Datos clave:**
  - Productos maestros
  - Proveedores
  - Finanzas y contabilidad

## Arquitectura Propuesta

### Nivel Junior - Modelo Conceptual

```
Entidades principales:
- Cliente
- Producto  
- Venta
- Tienda
- Canal

Relaciones:
- Cliente realiza Venta
- Venta contiene Producto
- Venta ocurre en Canal
- Producto está en Tienda
```

### Nivel Mid - Arquitectura de Capas

**Capa Raw (Bronze):**
- Datos crudos de cada fuente
- Sin transformaciones
- Formato original preservado

**Capa Curated (Silver):**
- Limpieza y normalización
- Deduplicación
- Validación de esquemas

**Capa Trusted (Gold):**
- Modelos de negocio integrados
- Modelo dimensional (estrella)
- Listo para consumo

**Consumo:**
- Dashboards Power BI
- APIs para apps
- Alertas y notificaciones

### Nivel Senior - Consideraciones Avanzadas

**Gobierno:**
- Clasificación de PII (email, teléfono)
- Políticas de retención (7 años)
- Control de acceso por rol
- Auditoría de accesos

**Seguridad:**
- Encriptación en reposo (AES-256)
- Enmascaramiento de datos sensibles
- Compliance con GDPR/LGPD

**FinOps:**
- Particionamiento por fecha (reducir scanning)
- Compresión (Parquet con Snappy)
- Lifecycle policies (Raw → Archive después de 90 días)
- Estimación de costos: $5K-8K mensuales en cloud

## Modelo de Datos

### Modelo Dimensional (Estrella)

**Tabla de Hechos: fact_ventas**
```
- venta_id (PK)
- cliente_id (FK)
- producto_id (FK)
- tienda_id (FK)
- canal_id (FK)
- fecha_id (FK)
- cantidad
- precio_unitario
- descuento
- impuesto
- total_venta
- costo_producto
- margen_bruto
```

**Dimensiones:**

1. **dim_cliente**
   - cliente_id (PK)
   - nombre
   - email (PII - enmascarado)
   - telefono (PII - enmascarado)
   - fecha_nacimiento
   - segmento
   - valor_lifetime

2. **dim_producto**
   - producto_id (PK)
   - sku
   - nombre
   - categoria
   - subcategoria
   - marca
   - precio_lista

3. **dim_tienda**
   - tienda_id (PK)
   - nombre
   - region
   - ciudad
   - tipo (física/online)
   - fecha_apertura

4. **dim_canal**
   - canal_id (PK)
   - nombre (POS/Web/App/Marketplace)
   - tipo
   - comision_porcentaje

5. **dim_fecha**
   - fecha_id (PK)
   - fecha
   - dia_semana
   - mes
   - trimestre
   - año
   - es_feriado

## KPIs y Métricas

### KPIs de Negocio
- **Ventas Totales:** SUM(total_venta)
- **Ticket Promedio:** AVG(total_venta)
- **Productos por Transacción:** AVG(cantidad)
- **Tasa de Conversión:** (Compras / Visitas) * 100
- **Customer Lifetime Value (CLV)**
- **Tasa de Retención de Clientes**

### Métricas Técnicas
- **Latencia de datos:** < 15 min para críticos
- **Disponibilidad:** 99.9% uptime
- **Calidad de datos:** > 98% registros válidos
- **Costos cloud:** $5K-8K mensuales

## Ejercicios por Nivel

### Ejercicio Nivel Junior
Diseña el modelo ER conceptual y lógico para este caso de uso. Incluye:
1. Diagrama de entidades y relaciones
2. Atributos de cada entidad
3. Llaves primarias y foráneas
4. Cardinalidades

### Ejercicio Nivel Mid
Propón una arquitectura de capas (Raw/Curated/Trusted/Gold) que incluya:
1. Diagrama de flujo de datos
2. Tecnologías para cada capa
3. Estrategia de integración batch vs streaming
4. Modelo dimensional (estrella o copo de nieve)

### Ejercicio Nivel Senior
Diseña un marco de gobierno completo:
1. Políticas de clasificación de datos
2. Controles de acceso (RBAC)
3. Estrategia de compliance (GDPR/LGPD)
4. Plan de optimización de costos (FinOps)
5. Monitoreo y alertas

## Datos de Ejemplo

Ver carpeta: `datasets/retail/` (próximamente)

**Archivos planificados:**
- `ventas_pos.csv` - Transacciones de tiendas
- `pedidos_online.json` - Pedidos e-commerce
- `productos.csv` - Catálogo de productos
- `clientes.csv` - Datos de clientes (sintéticos)

---

**Nota:** Este caso de uso está diseñado para ser progresivo. Los estudiantes de cada nivel deben completar los ejercicios correspondientes a su nivel.
