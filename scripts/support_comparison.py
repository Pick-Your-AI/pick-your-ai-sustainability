#!/usr/bin/env python3
"""Offline two-dimensional comparison of supplied #50 assumptions, not ranking.

Consumes exact potential_useful_coverage outputs from compute_demand.py and a
separately evidenced incremental implementation cash amount. Does not compute
credit eligibility, prices, realized avoided cash, or authority to operate.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import re
from typing import Any


GATES = ("eligibility", "permitted_use", "resource_fit", "schedule_fit",
         "financial_stop", "independence")
AMOUNTS = ("potential_useful_coverage", "incremental_implementation_cash")
CONTEXT = {"task", "period", "currency", "evidence_kind"}
EVIDENCE_KINDS = {"unknown", "proposal", "planning_estimate", "measured", "synthetic"}
NUMBER = re.compile(r"(?:0|[1-9][0-9]*)(?:\.[0-9]+|/[1-9][0-9]*)?")


def _fields(value: Any, expected: set[str], label: str) -> None:
    if type(value) is not dict or set(value) != expected:
        raise ValueError(f"{label}: exact fields required")


def _tri(value: Any, label: str) -> None:
    if value is not None and type(value) is not bool:
        raise ValueError(f"{label}: boolean or null required")


def _amount(value: Any, label: str) -> Fraction | None:
    if value is None:
        return None
    # Accept the accepted calculator's rational string output, never a float.
    if (type(value) is not str or len(value) > 100 or
            NUMBER.fullmatch(value) is None):
        raise ValueError(f"{label}: bounded exact nonnegative string or null required")
    return Fraction(value)


def _validate(offer: Any) -> tuple[Fraction | None, Fraction | None]:
    _fields(offer, {"context", "gates", *AMOUNTS}, "offer")
    _fields(offer["context"], CONTEXT, "context")
    _fields(offer["gates"], set(GATES), "gates")
    for name in GATES:
        _tri(offer["gates"][name], "gate")
    for name, value in offer["context"].items():
        if value is None:
            continue
        if (type(value) is not str or not 1 <= len(value) <= 200 or
                value != value.strip() or any(ord(ch) < 32 or ord(ch) == 127 for ch in value)):
            raise ValueError("context: bounded nonblank text without controls required")
        if name == "currency" and re.fullmatch(r"[A-Z]{3}", value) is None:
            raise ValueError("currency: three uppercase letters or null required")
        if name == "evidence_kind" and value not in EVIDENCE_KINDS:
            raise ValueError("evidence_kind: known classification or null required")
    return tuple(_amount(offer[name], name) for name in AMOUNTS)


def compare(left: dict[str, Any], right: dict[str, Any], *,
            common_conditions: bool | None = None) -> dict[str, Any]:
    """Compare coverage (higher) and incremental cash (lower), without netting.

All gates and the common-task/quality/rights assumption must be explicitly true.
A declared gate is an input assumption, not verification of an applicant or term.
An excluded route never makes its counterpart a winner. Unknown is not zero.
"""
    left_values, right_values = _validate(left), _validate(right)
    _tri(common_conditions, "common_conditions")

    def result(relation: str, reasons: list[str]) -> dict[str, Any]:
        return {"relation": relation, "reasons": reasons,
                "evidence_level": "arithmetic_only", "actual_avoided_cash": None}

    failed, unknown = [], []
    for side, offer in (("left", left), ("right", right)):
        for name in GATES:
            value = offer["gates"][name]
            if value is False:
                failed.append(f"{side}:{name}:false")
            elif value is None:
                unknown.append(f"{side}:{name}:unknown")
    if failed:
        return result("excluded", failed)
    if common_conditions is False:
        return result("incomparable", ["common_conditions:false"])
    if common_conditions is None:
        unknown.append("common_conditions:unknown")
    for side, offer in (("left", left), ("right", right)):
        if any(value is None for value in offer["context"].values()):
            unknown.append(f"{side}:context:unknown")
        elif offer["context"]["evidence_kind"] == "unknown":
            unknown.append(f"{side}:evidence_kind:unknown")
    if unknown:
        return result("indeterminate", unknown)
    if left["context"] != right["context"]:
        return result("incomparable", ["context:mismatch"])
    if any(value is None for value in (*left_values, *right_values)):
        return result("indeterminate", ["amount:unknown"])
    lc, lh = left_values
    rc, rh = right_values
    if (lc, lh) == (rc, rh):
        return result("equivalent_on_two_dimensions", [])
    if lc >= rc and lh <= rh:
        return result("left_dominates", [])
    if rc >= lc and rh <= lh:
        return result("right_dominates", [])
    return result("tradeoff", [])


def synthetic_demo() -> dict[str, Any]:
    """Replay the four invented #50 section-6 coordinates; no provider data."""
    context = {"task": "synthetic-task", "period": "synthetic-period",
               "currency": "XCU", "evidence_kind": "synthetic"}

    def offer(coverage: str | None, cash: str) -> dict[str, Any]:
        return {"context": dict(context), "gates": dict.fromkeys(GATES, True),
                "potential_useful_coverage": coverage,
                "incremental_implementation_cash": cash}

    cases = []
    for name, right_coverage in (("low", "20"), ("base", "70"),
                                 ("earlier-expiry", "10"), ("unknown-schedule", None)):
        cases.append({"case": name, "left_coverage": "20", "right_coverage": right_coverage,
                      "left_cash": "5", "right_cash": "15",
                      "comparison": compare(offer("20", "5"), offer(right_coverage, "15"),
                                            common_conditions=True)})
    return {"schema_version": "support-comparison-demo/v1",
            "evidence_level": "synthetic_arithmetic", "cases": cases}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", required=True,
                        help="Print only the four fictional arithmetic controls; no files or network")
    parser.parse_args()
    print(json.dumps(synthetic_demo(), indent=2, sort_keys=True, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
