"""Funciones FinOps para métricas de costo y eficiencia."""
from typing import List, Dict


def cost_per_critical_query(total_cost_usd: float, num_queries: int) -> float:
    return total_cost_usd / num_queries if num_queries else 0.0


def governance_cost_ratio(cost_tooling: float, cost_staff: float, cost_infra_gov: float, total_platform_cost: float) -> float:
    gov = cost_tooling + cost_staff + cost_infra_gov
    return gov / total_platform_cost if total_platform_cost else 0.0


def waste_pct(cluster_usage_hours: List[Dict[str, float]]) -> float:
    """cluster_usage_hours: lista de dicts {"active_hours": x, "idle_hours": y}"""
    total_active = sum(item.get("active_hours", 0) for item in cluster_usage_hours)
    total_idle = sum(item.get("idle_hours", 0) for item in cluster_usage_hours)
    total = total_active + total_idle
    return total_idle / total if total else 0.0


def summarize_finops(total_cost_usd: float, num_queries: int, cost_tooling: float, cost_staff: float, cost_infra_gov: float, total_platform_cost: float, cluster_usage_hours: List[Dict[str, float]]):
    return {
        "fin_cost_per_critical_query": cost_per_critical_query(total_cost_usd, num_queries),
        "fin_cost_governance_ratio": governance_cost_ratio(cost_tooling, cost_staff, cost_infra_gov, total_platform_cost),
        "fin_waste_pct": waste_pct(cluster_usage_hours)
    }
