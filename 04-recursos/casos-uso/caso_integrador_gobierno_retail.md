# Caso Integrador: Gobierno de Datos en Retail Omnicanal

## Contexto de Negocio

**Empresa:** RetailCorp, cadena de retail con 200 tiendas físicas y plataforma e-commerce.

**Desafío:** La empresa está consolidando datos de múltiples fuentes (ERP, e-commerce, CRM, POS) en un Data Lakehouse (Databricks). Se identificaron problemas:
- Datasets sin clasificación ni owner asignado.
- Accesos descontrolados (usuarios con permisos que ya no necesitan).
- Calidad inconsistente (duplicados, nulls en campos críticos).
- Sin trazabilidad: no se sabe qué reportes se rompen si cambia un esquema.

**Objetivo del ejercicio:** Diseñar un marco de gobierno aplicando roles RACI, políticas, procedimientos y lineage para el dominio de **Ventas**.

---

## Parte 1: Inventario de Datasets

Datasets actuales en el dominio Ventas:

| Dataset | Ubicación | Filas | Contiene PII | Owner Actual | Clasificación Actual | Calidad Validada |
|---------|-----------|-------|--------------|--------------|---------------------|------------------|
| `bronze.pos_transacciones_raw` | s3://lake/bronze/pos/ | 5M | Sí (email_cliente opcional) | Sin asignar | Sin clasificar | No |
| `bronze.ecommerce_pedidos_raw` | s3://lake/bronze/ecom/ | 2M | Sí (nombre, email, dirección) | Sin asignar | Sin clasificar | No |
| `silver.ventas_unificadas` | delta:/silver/ventas | 6.8M | Sí (cliente_id hash) | Sin asignar | Sin clasificar | Parcial |
| `gold.kpi_ventas_diarias` | delta:/gold/kpi_ventas | 365 filas | No | Equipo BI | Interno | Sí |
| `gold.clientes_perfil_360` | delta:/gold/clientes | 1.2M | Sí (email, teléfono, historial compras) | Sin asignar | Sin clasificar | No |

---

## Parte 2: Ejercicio - Aplicar Gobierno

### Tarea 2.1: Asignar Roles y Responsabilidades

**Roles disponibles:**
- Gerente Comercial
- Analista de Calidad (Ventas)
- Equipo Infraestructura Datos
- Arquitecto de Datos Senior
- Equipo BI
- Equipo Marketing

**Instrucciones:**
Para cada dataset, asigna:
1. **Data Owner** (quien define reglas de negocio y aprueba accesos).
2. **Data Steward** (quien valida calidad y metadatos).
3. **Data Custodian** (quien implementa controles técnicos).

**Ejemplo para `gold.kpi_ventas_diarias`:**
- Owner: Equipo BI (consume y define KPIs)
- Steward: Analista de Calidad (Ventas)
- Custodian: Equipo Infraestructura Datos

**Tu turno:** Completa la tabla para los otros 4 datasets.

| Dataset | Owner | Steward | Custodian |
|---------|-------|---------|-----------|
| `bronze.pos_transacciones_raw` | ? | ? | ? |
| `bronze.ecommerce_pedidos_raw` | ? | ? | ? |
| `silver.ventas_unificadas` | ? | ? | ? |
| `gold.clientes_perfil_360` | ? | ? | ? |

---

### Tarea 2.2: Clasificar Datasets

Usando la política de clasificación (Público, Interno, Confidencial, Regulado):

**Criterios:**
- **Regulado:** Contiene PII sujeto a GDPR/CCPA.
- **Confidencial:** Información estratégica de negocio sin PII.
- **Interno:** Datos operativos agregados, no sensibles.
- **Público:** No aplica en este caso.

**Instrucciones:** Clasifica cada dataset y justifica.

**Ejemplo:**
- `gold.kpi_ventas_diarias` → **Interno** (agregados sin PII, uso interno para dashboards).

**Tu turno:**

| Dataset | Clasificación Propuesta | Justificación |
|---------|-------------------------|---------------|
| `bronze.pos_transacciones_raw` | ? | ? |
| `bronze.ecommerce_pedidos_raw` | ? | ? |
| `silver.ventas_unificadas` | ? | ? |
| `gold.clientes_perfil_360` | ? | ? |

---

### Tarea 2.3: Matriz RACI para Cambio de Esquema

**Escenario:** El equipo de e-commerce quiere agregar una columna `metodo_pago` a `bronze.ecommerce_pedidos_raw`, lo que impactará `silver.ventas_unificadas` y potencialmente `gold.kpi_ventas_diarias`.

**Actividades:**
1. Proponer cambio (con justificación).
2. Evaluar impacto en downstream (usando lineage).
3. Notificar a consumidores afectados.
4. Aprobar cambio.
5. Implementar en dev/staging/prod.
6. Actualizar documentación y contratos.

**Roles involucrados:**
- Owner de `bronze.ecommerce_pedidos_raw`
- Owner de `silver.ventas_unificadas`
- Owner de `gold.kpi_ventas_diarias`
- Steward de Ventas
- Custodian (Infra)
- Governance Lead
- Equipo BI (consumer)

**Instrucciones:** Completa la matriz RACI.

| Actividad | Owner Bronze | Owner Silver | Owner Gold | Steward | Custodian | Gov Lead | BI Team |
|-----------|--------------|--------------|------------|---------|-----------|----------|---------|
| 1. Proponer cambio | ? | ? | ? | ? | ? | ? | ? |
| 2. Evaluar impacto | ? | ? | ? | ? | ? | ? | ? |
| 3. Notificar consumidores | ? | ? | ? | ? | ? | ? | ? |
| 4. Aprobar cambio | ? | ? | ? | ? | ? | ? | ? |
| 5. Implementar | ? | ? | ? | ? | ? | ? | ? |
| 6. Actualizar docs | ? | ? | ? | ? | ? | ? | ? |

**Leyenda:** R=Responsable, A=Aprueba, C=Consultado, I=Informado

---

### Tarea 2.4: Construir Lineage (Grafo)

**Instrucciones:** Dibuja el grafo de lineage para los 5 datasets, indicando:
- **Fuentes externas:** ERP, POS, e-commerce.
- **Transformaciones:** "Limpiar, deduplicar", "Join + agregación", etc.
- **Destinos/consumidores:** Dashboard BI, modelo ML, reportes.

**Formato sugerido:**
```
ERP → bronze.pos_transacciones_raw → [Limpiar, validar] → silver.ventas_unificadas → [Agrupar por día] → gold.kpi_ventas_diarias → Dashboard BI
e-commerce → bronze.ecommerce_pedidos_raw → [Normalizar, deduplicar] → silver.ventas_unificadas
silver.ventas_unificadas → [Join clientes, calcular RFM] → gold.clientes_perfil_360 → Modelo ML Churn
```

**Tu turno:** Completa el grafo con todos los datasets y flujos.

---

### Tarea 2.5: Definir Política de Calidad

**Escenario:** `silver.ventas_unificadas` tiene problemas: 3% de filas con `cliente_id` nulo, duplicados por `pedido_id`.

**Instrucciones:**
1. Define 3 reglas de calidad específicas (formato assertion).
2. Propón SLO de calidad (ej. nulls_cliente_id < 1%).
3. Diseña procedimiento: ¿qué pasa si falla un quality gate?

**Ejemplo de regla:**
```python
def regla_no_duplicados(df):
    return not df.duplicated(subset=['pedido_id']).any()
```

**Tu turno:** Escribe las 3 reglas y el procedimiento.

---

### Tarea 2.6: Procedimiento de Solicitud de Acceso

**Escenario:** El equipo de Marketing solicita acceso de lectura a `gold.clientes_perfil_360` (clasificado Regulado).

**Instrucciones:**
1. Diseña un workflow de 6 pasos (basado en el procedimiento visto en Senior 01).
2. Indica quién aprueba (Owner, Seguridad, Governance Lead).
3. ¿Qué controles técnicos se aplican? (RBAC, masking, auditoría).

**Tu turno:** Describe el flujo completo.

---

## Parte 3: Solución Propuesta (Guía)

### 3.1. Roles y Responsabilidades

| Dataset | Owner | Steward | Custodian |
|---------|-------|---------|-----------|
| `bronze.pos_transacciones_raw` | Gerente Comercial | Analista Calidad | Equipo Infra |
| `bronze.ecommerce_pedidos_raw` | Gerente Comercial | Analista Calidad | Equipo Infra |
| `silver.ventas_unificadas` | Gerente Comercial | Analista Calidad | Equipo Infra |
| `gold.clientes_perfil_360` | Equipo Marketing | Analista Calidad | Equipo Infra |

---

### 3.2. Clasificación

| Dataset | Clasificación | Justificación |
|---------|---------------|---------------|
| `bronze.pos_transacciones_raw` | **Regulado** | Contiene email_cliente (PII) |
| `bronze.ecommerce_pedidos_raw` | **Regulado** | Contiene nombre, email, dirección (PII) |
| `silver.ventas_unificadas` | **Confidencial** | cliente_id hasheado (pseudo-PII), datos estratégicos |
| `gold.clientes_perfil_360` | **Regulado** | Email, teléfono, historial (PII completo) |

---

### 3.3. Matriz RACI

| Actividad | Owner Bronze | Owner Silver | Owner Gold | Steward | Custodian | Gov Lead | BI Team |
|-----------|--------------|--------------|------------|---------|-----------|----------|---------|
| 1. Proponer | **R** | I | I | C | I | I | I |
| 2. Evaluar impacto | C | **R** | **R** | **A** | C | C | C |
| 3. Notificar | I | **R** | I | C | I | **A** | **I** |
| 4. Aprobar | I | C | C | C | I | **A** | C |
| 5. Implementar | I | I | I | I | **R** | I | I |
| 6. Actualizar docs | C | **R** | I | **A** | C | I | I |

---

### 3.4. Lineage (Texto)

```
[ERP] → bronze.pos_transacciones_raw
[e-commerce API] → bronze.ecommerce_pedidos_raw

bronze.pos_transacciones_raw → [Limpiar nulls, validar rangos] → silver.ventas_unificadas
bronze.ecommerce_pedidos_raw → [Normalizar schema, deduplicar] → silver.ventas_unificadas

silver.ventas_unificadas → [Agrupar por fecha, sumar ventas] → gold.kpi_ventas_diarias → [Dashboard BI: Ventas]
silver.ventas_unificadas → [Join clientes, calcular RFM, agregar] → gold.clientes_perfil_360 → [Modelo ML: Churn Prediction]
```

---

### 3.5. Reglas de Calidad

```python
# Regla 1: No nulos en cliente_id
def regla_cliente_no_nulo(df):
    return df['cliente_id'].notna().all()

# Regla 2: Sin duplicados por pedido_id
def regla_sin_duplicados(df):
    return not df.duplicated(subset=['pedido_id']).any()

# Regla 3: Monto total positivo
def regla_monto_positivo(df):
    return (df['monto_total'] > 0).all()

# SLO: nulls_cliente_id < 1%
# Procedimiento: Si falla critical → bloqueo Bronze→Silver, alerta a Steward, corrección en 24h
```

---

### 3.6. Workflow Acceso a Regulado

1. **Solicitud:** Marketing completa formulario (dataset, justificación, alcance temporal).
2. **Validación automática:** Sistema detecta clasificación Regulado → requiere aprobación doble.
3. **Owner aprueba:** Gerente Marketing (owner de `gold.clientes_perfil_360`) revisa y aprueba.
4. **Seguridad aprueba:** CISO valida que justificación cumple "need-to-know".
5. **Custodian provisiona:** Equipo Infra crea rol con RBAC, aplica dynamic masking en email/teléfono.
6. **Auditoría:** Log registra acceso otorgado (quién, cuándo, por qué, hasta cuándo).
7. **Revisión:** Acceso se revisa automáticamente en 90 días (renovar o revocar).

---

## Parte 4: Entregables del Ejercicio

1. **Tabla de roles** completada para los 5 datasets.
2. **Clasificaciones justificadas**.
3. **Matriz RACI completa** para cambio de esquema.
4. **Diagrama de lineage** (puede ser texto estructurado o visual).
5. **3 reglas de calidad** en pseudocódigo/Python.
6. **Workflow de acceso** con 6-7 pasos detallados.

---

## Evaluación (Sugerida)

- Correcta asignación de roles (considerando negocio y técnico): 20%
- Clasificación fundamentada: 20%
- RACI coherente (R/A/C/I bien distribuidos): 20%
- Lineage completo y preciso: 15%
- Reglas de calidad ejecutables y SLO realista: 15%
- Workflow de acceso con controles adecuados: 10%

---

**Tiempo estimado:** 2-3 horas

**Recomendación:** Trabajar en equipos de 2-3 personas, luego peer review entre equipos.
