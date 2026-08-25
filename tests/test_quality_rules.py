import pytest
import pandas as pd
from curso_helpers import quality_rules as qr


def test_null_rate_basic():
    df = pd.DataFrame({"a": [1, None, 3, None]})
    assert qr.null_rate(df) == 0.5


def test_null_rate_no_nulls():
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert qr.null_rate(df) == 0.0


def test_duplicate_rate_basic():
    df = pd.DataFrame({"a": [1, 1, 2, 3]})
    assert qr.duplicate_rate(df) == 0.25


def test_psi_identical_distributions_is_near_zero():
    reference = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert abs(qr.psi(reference, reference)) < 1e-6


def test_psi_empty_inputs_return_zero():
    assert qr.psi([], [1, 2, 3]) == 0.0
    assert qr.psi([1, 2, 3], []) == 0.0


def test_evaluate_rules_pass_and_fail():
    df = pd.DataFrame({"a": [1, 2, 3, None]})
    result = qr.evaluate_rules(df, {"max_null_rate": 0.5})
    assert result["results"]["max_null_rate"]

    result = qr.evaluate_rules(df, {"max_null_rate": 0.1})
    assert not result["results"]["max_null_rate"]


def test_ks_pvalue_with_scipy():
    reference = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    current = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    p = qr.ks_pvalue(reference, current)
    assert p == pytest.approx(1.0)


def test_ks_pvalue_without_scipy_raises_instead_of_faking_a_pvalue(monkeypatch):
    """Sin SciPy, debe fallar explícitamente, no inventar un pseudo-p-value."""
    monkeypatch.setattr(qr, "ks_2samp", None)
    with pytest.raises(ImportError):
        qr.ks_pvalue([1, 2, 3], [4, 5, 6])
