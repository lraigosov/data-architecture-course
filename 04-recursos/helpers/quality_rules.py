"""Funciones de métricas de calidad y drift.
Evita dependencias pesadas; SciPy opcional si disponible.
"""
from typing import Dict, Any

try:
    from scipy.stats import ks_2samp  # type: ignore
except ImportError:
    ks_2samp = None  # Fallback simple

import math


def null_rate(df, cols=None) -> float:
    """Porcentaje de nulos sobre el total de celdas en columnas indicadas."""
    if cols is None:
        cols = df.columns
    total = 0
    nulls = 0
    for c in cols:
        total += len(df[c])
        nulls += df[c].isna().sum()
    return nulls / total if total else 0.0


def duplicate_rate(df, subset=None) -> float:
    """Porcentaje de filas duplicadas según subset (lista de columnas)."""
    if subset is None:
        subset = df.columns.tolist()
    total = len(df)
    dups = df.duplicated(subset=subset).sum()
    return dups / total if total else 0.0


def psi(reference, current, bins=10) -> float:
    """Population Stability Index simplificado para listas/series numéricas."""
    if len(reference) == 0 or len(current) == 0:
        return 0.0
    low = min(min(reference), min(current))
    high = max(max(reference), max(current))
    step = (high - low) / bins if high != low else 1
    edges = [low + i * step for i in range(bins + 1)]
    ref_counts = [0] * bins
    cur_counts = [0] * bins
    for v in reference:
        idx = min(bins - 1, int((v - low) / step)) if high != low else 0
        ref_counts[idx] += 1
    for v in current:
        idx = min(bins - 1, int((v - low) / step)) if high != low else 0
        cur_counts[idx] += 1
    ref_total = sum(ref_counts)
    cur_total = sum(cur_counts)
    psi_val = 0.0
    for i in range(bins):
        r = ref_counts[i] / ref_total if ref_total else 0.000001
        c = cur_counts[i] / cur_total if cur_total else 0.000001
        psi_val += (c - r) * math.log((c + 1e-9) / (r + 1e-9))
    return psi_val


def ks_pvalue(reference, current) -> float:
    """KS test p-value si SciPy disponible; fallback aproximado: 0 si medias difieren >5%."""
    if ks_2samp is not None:
        return ks_2samp(reference, current).pvalue
    # Fallback heurístico
    ref_mean = sum(reference) / len(reference) if reference else 0
    cur_mean = sum(current) / len(current) if current else 0
    if ref_mean == 0:
        return 1.0 if cur_mean == 0 else 0.0
    diff_ratio = abs(cur_mean - ref_mean) / abs(ref_mean)
    return 0.0 if diff_ratio > 0.05 else 0.5


def evaluate_rules(df, rules: Dict[str, Any]) -> Dict[str, Any]:
    """Evalúa un diccionario de reglas simples.
    rules ejemplo:
    {
      "max_null_rate": 0.02,
      "max_duplicate_rate": 0.01,
    }
    """
    metrics = {
        "null_rate": null_rate(df),
        "duplicate_rate": duplicate_rate(df)
    }
    results = {}
    for k, v in rules.items():
        if k == "max_null_rate":
            results[k] = metrics["null_rate"] <= v
        elif k == "max_duplicate_rate":
            results[k] = metrics["duplicate_rate"] <= v
    return {"metrics": metrics, "results": results}
