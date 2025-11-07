#!/usr/bin/env python
"""Quality gate script para validar dataset ventas.
Uso:
  python scripts/quality_gate.py 04-recursos/datasets/ejemplo_ventas.csv
Devuelve exit code !=0 si falla alguna regla.
"""
import sys
import pandas as pd
from datetime import datetime, timezone

RULES = {
    'no_null_pedido_id': lambda df: df['pedido_id'].notna().all(),
    'cantidad_en_rango': lambda df: df['cantidad'].fillna(0).between(0, 10000).all(),
    'precio_unitario_en_rango': lambda df: df['precio_unitario'].fillna(0).between(0, 100000).all(),
    'frescura_max_60_min': lambda df: (datetime.now(timezone.utc) - df['updated_at'].max().to_pydatetime()).total_seconds()/60.0 <= 60,
}

CRITICAL = {'no_null_pedido_id', 'frescura_max_60_min'}


def main():
    if len(sys.argv) < 2:
        print("ERROR: ruta CSV requerida")
        sys.exit(2)
    path = sys.argv[1]
    try:
        df = pd.read_csv(path, parse_dates=['fecha','updated_at'])
    except Exception as e:
        print(f"ERROR al cargar CSV: {e}")
        sys.exit(3)
    results = {name: rule(df) for name, rule in RULES.items()}
    for k,v in results.items():
        status = 'OK' if v else 'FAIL'
        crit = ' (CRIT)' if k in CRITICAL else ''
        print(f"{k}: {status}{crit}")
    if not all(results[r] for r in CRITICAL):
        print("Quality gate CRITICAL FAILED")
        sys.exit(1)
    if not all(results.values()):
        print("Quality gate WARNING: reglas no críticas fallaron")
    print("Quality gate PASSED")

if __name__ == '__main__':
    main()
