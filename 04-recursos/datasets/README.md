# Datasets de Ejemplo

Este directorio contiene datasets sintéticos usados en notebooks para ilustrar conceptos de observabilidad, calidad y contratos de datos.

## Lista

- `ejemplo_ventas.csv`: Ventas simples multi-país y multi-canal con algunos valores nulos para pruebas de reglas.

## Uso Rápido

```python
import pandas as pd
df = pd.read_csv('04-recursos/datasets/ejemplo_ventas.csv', parse_dates=['fecha','updated_at'])
```

## Métricas Sugeridas
- Frescura: diferencia (minutos) entre `now()` y `max(updated_at)`
- Nulls por columna
- Duplicados por `pedido_id`
- Ventas por día y canal

## Relación con Contratos
El dataset está cubierto por `../contratos-datos/contrato_dataset_bi_ventas.yaml` que define SLOs y reglas de calidad.

## CI/CD
Ejemplo de quality gate:
```bash
python scripts/quality_gate.py 04-recursos/datasets/ejemplo_ventas.csv
```
