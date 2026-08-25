from datetime import datetime, timedelta, timezone

import pandas as pd
import quality_gate as qg


def _base_df(**overrides):
    data = {
        "pedido_id": [1, 2, 3],
        "cantidad": [1, 5, 10],
        "precio_unitario": [10.0, 20.0, 30.0],
        "updated_at": [pd.Timestamp.now(tz=timezone.utc)] * 3,
    }
    data.update(overrides)
    return pd.DataFrame(data)


def test_static_rules_pass_on_valid_data():
    df = _base_df()
    for name, rule in qg.STATIC_RULES.items():
        assert rule(df), f"{name} debería pasar con datos válidos"


def test_no_null_pedido_id_fails_on_null():
    df = _base_df(pedido_id=[1, None, 3])
    assert not qg.STATIC_RULES["no_null_pedido_id"](df)


def test_cantidad_en_rango_fails_out_of_range():
    df = _base_df(cantidad=[1, 5, 999999])
    assert not qg.STATIC_RULES["cantidad_en_rango"](df)


def test_freshness_rule_passes_with_recent_timestamp():
    df = _base_df(updated_at=[pd.Timestamp.now(tz=timezone.utc)] * 3)
    assert qg.FRESHNESS_RULES["frescura_max_60_min"](df)


def test_freshness_rule_fails_with_stale_timestamp():
    stale = datetime.now(timezone.utc) - timedelta(hours=2)
    df = _base_df(updated_at=[pd.Timestamp(stale)] * 3)
    assert not qg.FRESHNESS_RULES["frescura_max_60_min"](df)
