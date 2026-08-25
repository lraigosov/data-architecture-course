import cost_metrics as cm


def test_cost_per_critical_query():
    assert cm.cost_per_critical_query(100.0, 20) == 5.0


def test_cost_per_critical_query_zero_queries():
    assert cm.cost_per_critical_query(100.0, 0) == 0.0


def test_governance_cost_ratio():
    ratio = cm.governance_cost_ratio(10.0, 20.0, 5.0, 350.0)
    assert ratio == 0.1


def test_governance_cost_ratio_zero_platform_cost():
    assert cm.governance_cost_ratio(10.0, 20.0, 5.0, 0.0) == 0.0


def test_waste_pct():
    usage = [{"active_hours": 40, "idle_hours": 10}, {"active_hours": 30, "idle_hours": 20}]
    assert cm.waste_pct(usage) == 0.3


def test_waste_pct_no_hours():
    assert cm.waste_pct([]) == 0.0


def test_summarize_finops():
    result = cm.summarize_finops(
        total_cost_usd=100.0,
        num_queries=10,
        cost_tooling=5.0,
        cost_staff=5.0,
        cost_infra_gov=0.0,
        total_platform_cost=100.0,
        cluster_usage_hours=[{"active_hours": 9, "idle_hours": 1}],
    )
    assert result == {
        "fin_cost_per_critical_query": 10.0,
        "fin_cost_governance_ratio": 0.1,
        "fin_waste_pct": 0.1,
    }
