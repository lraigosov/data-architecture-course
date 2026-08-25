"""Smoke tests: imports y dependencias básicas funcionan."""
import importlib.util


def test_quality_rules_importable():
    import quality_rules as qr
    import pandas as pd

    df = pd.DataFrame({"a": [1, 2, None, 4], "b": [10, 10, 11, 11]})
    assert 0.0 <= qr.null_rate(df) <= 1.0
    assert 0.0 <= qr.duplicate_rate(df) <= 1.0
    assert isinstance(qr.psi([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]), float)


def test_cost_metrics_importable():
    import cost_metrics as cm

    finops = cm.summarize_finops(
        total_cost_usd=150.0,
        num_queries=30,
        cost_tooling=20.0,
        cost_staff=50.0,
        cost_infra_gov=10.0,
        total_platform_cost=500.0,
        cluster_usage_hours=[
            {"active_hours": 40, "idle_hours": 5},
            {"active_hours": 35, "idle_hours": 10},
        ],
    )
    assert 0.0 <= finops["fin_waste_pct"] <= 1.0


def test_event_emitter_importable_without_network():
    import event_emitter as ee

    # No invocamos emit_* aquí: harían una conexión real a localhost:5000
    # si openlineage-python está instalado. Solo verificamos que el
    # módulo define las funciones esperadas.
    emit_funcs = [f for f in dir(ee) if f.startswith("emit_")]
    assert {"emit_start", "emit_complete", "emit_fail"} <= set(emit_funcs)


def test_networkx_graph_basico():
    import networkx as nx

    graph = nx.DiGraph()
    graph.add_edge("bronze.sales_orders_raw", "silver.orders_clean")
    graph.add_edge("silver.orders_clean", "gold.sales_metrics")
    assert list(graph.nodes()) == [
        "bronze.sales_orders_raw",
        "silver.orders_clean",
        "gold.sales_metrics",
    ]


def test_matplotlib_optional():
    if importlib.util.find_spec("matplotlib") is None:
        return
    import matplotlib

    assert matplotlib.__version__
