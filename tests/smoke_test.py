"""Smoke test básico para helpers y dependencias.
Ejecutar: python tests/smoke_test.py
Salida esperada: métricas calculadas y confirmación de imports.
"""
from importlib import import_module
import sys

# Resultado acumulado
RESULTS = {}

# 1. Probar import quality_rules y métricas simples
try:
    qr = import_module("04-recursos.helpers.quality_rules".replace("/",".").replace("-","_"))
except ModuleNotFoundError:
    # Ajuste de ruta: helpers están en 04-recursos/helpers => usar paquete relativo añadible al path
    import pathlib
    root = pathlib.Path(__file__).resolve().parents[1]
    helpers_path = root / "04-recursos" / "helpers"
    sys.path.append(str(helpers_path))
    import quality_rules as qr

try:
    import pandas as pd
    df = pd.DataFrame({"a":[1,2,None,4], "b":[10,10,11,11]})
    null_r = qr.null_rate(df)
    dup_r = qr.duplicate_rate(df)
    psi_val = qr.psi([1,2,3,4,5],[1,2,3,4,6])
    RESULTS['quality'] = {"null_rate": null_r, "duplicate_rate": dup_r, "psi_sample": psi_val}
except Exception as e:
    RESULTS['quality_error'] = str(e)

# 2. Probar cost_metrics
try:
    try:
        cm = import_module("04-recursos.helpers.cost_metrics".replace("/",".").replace("-","_"))
    except ModuleNotFoundError:
        import cost_metrics as cm
    finops = cm.summarize_finops(
        total_cost_usd=150.0,
        num_queries=30,
        cost_tooling=20.0,
        cost_staff=50.0,
        cost_infra_gov=10.0,
        total_platform_cost=500.0,
        cluster_usage_hours=[{"active_hours":40, "idle_hours":5},{"active_hours":35,"idle_hours":10}]
    )
    RESULTS['finops'] = finops
except Exception as e:
    RESULTS['finops_error'] = str(e)

# 3. Probar event_emitter (sin emitir red)
try:
    try:
        ee = import_module("04-recursos.helpers.event_emitter".replace("/",".").replace("-","_"))
    except ModuleNotFoundError:
        import event_emitter as ee
    # Validar funciones disponibles
    RESULTS['event_emitter_funcs'] = [f for f in dir(ee) if f.startswith('emit_')]
    # No llamamos emit_* para evitar conexión HTTP.
except Exception as e:
    RESULTS['event_emitter_error'] = str(e)

# 4. Probar networkx (creación grafo mínima)
try:
    import networkx as nx
    G = nx.DiGraph()
    G.add_edge('bronze.sales_orders_raw','silver.orders_clean')
    G.add_edge('silver.orders_clean','gold.sales_metrics')
    RESULTS['networkx_nodes'] = list(G.nodes())
    RESULTS['networkx_edges'] = list(G.edges())
except Exception as e:
    RESULTS['networkx_error'] = str(e)

# 5. Verificar import opcional matplotlib (solo si presente)
try:
    import importlib.util
    if importlib.util.find_spec('matplotlib'):
        import matplotlib
        RESULTS['matplotlib_version'] = matplotlib.__version__
    else:
        RESULTS['matplotlib_version'] = 'not_installed'
except Exception as e:
    RESULTS['matplotlib_error'] = str(e)

# 6. Resumen y checks simples
def assert_range(name, value, min_v, max_v):
    if not (min_v <= value <= max_v):
        raise AssertionError(f"Metric {name}={value} fuera de rango [{min_v},{max_v}]")

try:
    if 'quality' in RESULTS:
        assert_range('null_rate', RESULTS['quality']['null_rate'], 0.0, 1.0)
        assert_range('duplicate_rate', RESULTS['quality']['duplicate_rate'], 0.0, 1.0)
    if 'finops' in RESULTS:
        assert_range('fin_waste_pct', RESULTS['finops']['fin_waste_pct'], 0.0, 1.0)
except Exception as e:
    RESULTS['asserts_error'] = str(e)

print("=== SMOKE TEST RESULTS ===")
for k,v in RESULTS.items():
    print(f"{k}: {v}")

# Exit code 0 si no hay errores clave
errors = [k for k in RESULTS if k.endswith('_error') or k=='asserts_error']
if errors:
    print('\nErrores detectados:', errors)
    sys.exit(1)
else:
    print('\nSmoke test OK')
