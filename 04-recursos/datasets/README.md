# Datasets Sintéticos para Ejercicios Transversales

Este directorio contiene datasets sintéticos educativos. No incluyen PII ni datos reales y poseen anomalías intencionales para practicar: calidad, contratos, modelado dimensional, streaming, migración y gobernanza. El dataset anterior `ejemplo_ventas.csv` se mantiene como ejemplo básico; los nuevos datasets estructuran los ejercicios 2025.

## 1. sales_orders.csv
**Campos:** `order_id, customer_id, order_date, product_id, quantity, unit_price, total_amount, status`

**Anomalías Intencionales:**
- `order_id` duplicado.
- `unit_price` negativo.
- `total_amount` inconsistente (≠ `quantity * unit_price`).
- Fechas fuera de rango (antes 2018 o después 2025-12-31).
- `status` incoherente (CANCELLED con monto positivo).

**Usos en Notebooks:** Junior 01 (detección inicial), Junior 06 (perfilado y reglas), Modelado (fact/dimensión, contratos), Dimensional avanzado (referencia métricas).

## 2. streaming_events.csv
**Campos:** `event_id, user_id, event_type, event_ts, device_type, region, value`

**Anomalías Intencionales:**
- Timestamps fuera de orden.
- Eventos duplicados.
- Regiones nulas.
- Sesgo fuerte en distribución de `event_type`.

**Usos en Notebooks:** Mid 15 (features offline/online, FinOps, ROI), futuro drift/latencia.

## 3. customers_dim.csv
**Campos:** `customer_id, name, segment, country, signup_date, is_active`

**Anomalías Intencionales:**
- Filas duplicadas.
- `segment` nulo.
- Fechas fuera de rango (antes 2015, después 2025-12-31).
- `is_active=true` con `signup_date` nula.

**Usos en Notebooks:** Senior 04 (migración & KPI), Junior 05 (SCD Tipo 2 histórico), evaluación governance.

## 4. ejemplo_ventas.csv (legacy)
Dataset básico de ventas multi-país utilizado originalmente para ejemplos de métricas simples. Conservado para ejercicios introductorios rápidos.

## Rutas y Carga
Los notebooks intentan primero la ruta relativa (`../04-recursos/datasets/<archivo>.csv`) y luego la raíz (`04-recursos/datasets/<archivo>.csv`) para soportar ejecución desde carpetas distintas.

Ejemplo carga genérica:
```python
import pandas as pd, pathlib
path = pathlib.Path('04-recursos/datasets/sales_orders.csv')
df = pd.read_csv(path)
```

## Reglas de Calidad Sugeridas Comunes
| Campo | Regla | Severidad |
|-------|-------|-----------|
| order_id | not null & único | Alta |
| unit_price | unit_price >= 0 | Alta |
| total_amount | total_amount == quantity * unit_price | Media |
| event_ts | parseable y dentro de ventana | Alta |
| segment | segment in conjunto permitido | Media |
| signup_date | dentro de rango válido | Media |
| is_active | si is_active entonces signup_date no nula | Media |

## Métricas Transversales
- Duplicados por clave natural.
- Frescura (max timestamp vs now).
- % registros válidos por regla (para Data Quality Score).
- Distribución por categorías (segment, region, status).

## Consideraciones FinOps
- `sales_orders.csv`: compresión columnar reduce costo y mejora scans.
- `streaming_events.csv`: evaluar costo de mantener store online; posible estrategia micro-batch si latencia < 1–5 min aceptable.
- `customers_dim.csv`: SCD2 aumenta filas; impacto marginal en costo global pero crítico para auditoría.

## Advertencias
- No usar para benchmarking de performance real.
- Distribuciones artificiales; no representan estacionalidad.
- Ajustar reglas si se añaden atributos nuevos.

## Próximas Extensiones Planeadas
- Dataset producto con atributos cambiantes (SKU, categoría, precio histórico).
- Dataset fraude para features complejas y monitoreo de drift.

---
Última actualización: 2025-11-23.
