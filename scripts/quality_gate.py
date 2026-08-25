#!/usr/bin/env python
"""Quality gate script para validar dataset ventas.

Uso:
  python scripts/quality_gate.py 04-recursos/datasets/ejemplo_ventas.csv
  python scripts/quality_gate.py 04-recursos/datasets/ejemplo_ventas.csv --check-freshness

Devuelve exit code !=0 si falla alguna regla crítica.

Nota: las reglas de STATIC_RULES validan esquema/rango y tienen sentido
contra un dataset fijo (por ejemplo, el CSV de ejemplo versionado en el
repo). La regla de FRESHNESS_RULES compara 'updated_at' contra la hora
actual, así que solo tiene sentido contra datos vivos de un pipeline en
producción: contra un CSV estático fallará siempre por diseño, por lo
que se ejecuta solo si se pasa --check-freshness explícitamente.
"""
import sys
import argparse
import pandas as pd
from datetime import datetime, timezone

STATIC_RULES = {
    'no_null_pedido_id': lambda df: df['pedido_id'].notna().all(),
    'cantidad_en_rango': lambda df: df['cantidad'].fillna(0).between(0, 10000).all(),
    'precio_unitario_en_rango': lambda df: df['precio_unitario'].fillna(0).between(0, 100000).all(),
}

FRESHNESS_RULES = {
    'frescura_max_60_min': lambda df: (datetime.now(timezone.utc) - df['updated_at'].max().to_pydatetime()).total_seconds()/60.0 <= 60,
}

CRITICAL = {'no_null_pedido_id', 'frescura_max_60_min'}


def main():
    parser = argparse.ArgumentParser(description="Quality gate para dataset de ventas")
    parser.add_argument("csv_path", help="Ruta al CSV a validar")
    parser.add_argument(
        "--check-freshness",
        action="store_true",
        help="Incluye la regla de frescura (solo tiene sentido contra datos vivos, no un fixture estático)",
    )
    args = parser.parse_args()

    rules = dict(STATIC_RULES)
    if args.check_freshness:
        rules.update(FRESHNESS_RULES)

    try:
        df = pd.read_csv(args.csv_path, parse_dates=['fecha', 'updated_at'])
    except Exception as e:
        print(f"ERROR al cargar CSV: {e}")
        sys.exit(3)

    results = {name: rule(df) for name, rule in rules.items()}
    for k, v in results.items():
        status = 'OK' if v else 'FAIL'
        crit = ' (CRIT)' if k in CRITICAL else ''
        print(f"{k}: {status}{crit}")

    critical_evaluated = CRITICAL & set(results)
    if not all(results[r] for r in critical_evaluated):
        print("Quality gate CRITICAL FAILED")
        sys.exit(1)
    if not all(results.values()):
        print("Quality gate WARNING: reglas no críticas fallaron")
    print("Quality gate PASSED")

if __name__ == '__main__':
    main()
