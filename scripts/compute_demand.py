#!/usr/bin/env python3
"""Offline, exact-rational demand and coverage planning; no provider operations."""

from __future__ import annotations

import argparse
import copy
from datetime import date
from fractions import Fraction
import json
from pathlib import Path
import re


DEFAULT = Path(__file__).resolve().parents[1] / "data/budget/compute-demand-model.json"
CLASSES = {"research": "N06", "product_hosting": "N01", "ci_testing": "N03",
           "public_demonstration": "N06"}
KINDS = {"unknown", "proposal", "planning_estimate", "measured", "synthetic"}
RATE_KEYS = {
    "api": {"uncached_input_tokens", "cached_input_tokens", "output_tokens"},
    "embedding": {"embedding_tokens"},
    "accelerator": {"accelerator_hours"},
    "ci": {"ci_minutes"},
    "storage": {"gib_months"},
    "egress": {"egress_gib"},
}
INPUT_KEYS = {
    "api": {"request_dimensions", "max_attempts_per_request", "input_tokens_per_attempt",
            "cached_input_tokens_per_attempt", "output_tokens_per_attempt", "cache_eligible"},
    "embedding": {"items", "tokens_per_item", "max_attempts_per_item"},
    "accelerator": {"jobs", "accelerators_per_job", "timing_mode", "seconds_per_job",
                    "work_units_per_job", "units_per_second", "work_unit", "minimum_memory_gib"},
    "ci": {"jobs", "minutes_per_job"},
    "storage": {"gib", "months"},
    "egress": {"gib"},
}
LIMIT_KEYS = {"requests", "tokens", "accelerator_hours", "ci_minutes", "storage_gib",
              "egress_gib", "available_memory_gib"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, name):
    require(type(value) is str and bool(value.strip()), f"{name}: nonblank text required")
    return value


def keys(value, expected, name):
    require(type(value) is dict and set(value) == expected, f"{name}: exact fields required")


def number(value, name, *, integer=False, positive=False):
    if value is None:
        return None
    if integer:
        require(type(value) is int, f"{name}: integer or null required")
        result = Fraction(value)
    else:
        require(type(value) is str and len(value) <= 100 and
                re.fullmatch(r"(?:0|[1-9][0-9]*)(?:\.[0-9]+)?", value) is not None,
                f"{name}: exact nonnegative decimal string or null required")
        result = Fraction(value)
    require(result > 0 if positive else result >= 0, f"{name}: invalid sign/zero")
    return result


def tri(value, name):
    require(value is None or type(value) is bool, f"{name}: boolean or null required")
    return value


def refs(value, sources, name, *, required=False):
    require(type(value) is list and all(type(v) is str and v in sources for v in value)
            and len(value) == len(set(value)), f"{name}: unique known source IDs required")
    require(not required or bool(value), f"{name}: provenance required")


def evidence(value, sources, name):
    keys(value, {"kind", "source_refs", "note"}, name)
    require(value["kind"] in KINDS, f"{name}: evidence kind")
    text(value["note"], name + ".note")
    refs(value["source_refs"], sources, name, required=value["kind"] != "unknown")


def product(*values):
    # A missing quantity stays missing even with a known zero multiplier.
    if any(value is None for value in values):
        return None
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def exact(value):
    return None if value is None else str(value)


def cents(value):
    """Nonnegative USD amount, rounded half upward exactly once per component."""
    require(value >= 0, "USD cost must be nonnegative")
    value *= 100
    return (2 * value.numerator + value.denominator) // (2 * value.denominator)


def quantities(component, sensitivity):
    kind, inputs = component["kind"], component["inputs"]
    keys(inputs, INPUT_KEYS[kind], component["id"] + ".inputs")
    n = lambda key, **kw: number(inputs[key], key, **kw)
    result = {}
    if kind == "api":
        dimensions = inputs["request_dimensions"]
        require(type(dimensions) is dict and bool(dimensions), "nonempty request dimensions")
        for name in dimensions:
            text(name, "request dimension")
        logical = product(*(number(v, k, integer=True) for k, v in dimensions.items()))
        # An optional sensitivity changes the number of requests, never the rate.
        logical = product(logical, sensitivity)
        require(logical is None or logical.denominator == 1,
                "request sensitivity must yield whole logical requests")
        attempts = product(logical, n("max_attempts_per_request", integer=True, positive=True))
        input_tokens = n("input_tokens_per_attempt", integer=True)
        cached = n("cached_input_tokens_per_attempt", integer=True)
        output_tokens = n("output_tokens_per_attempt", integer=True)
        require(input_tokens is None or cached is None or cached <= input_tokens,
                "cached input is a subset of total input")
        eligible = tri(inputs["cache_eligible"], "cache_eligible")
        if eligible is False or cached == 0:
            billed_cached = Fraction(0)
            billed_uncached = input_tokens
        elif eligible is True and input_tokens is not None and cached is not None:
            billed_cached, billed_uncached = cached, input_tokens - cached
        else:
            billed_cached = billed_uncached = None
        result = {"logical_requests": logical, "max_attempts": attempts,
                  "input_tokens_total": product(attempts, input_tokens),
                  "uncached_input_tokens": product(attempts, billed_uncached),
                  "cached_input_tokens": product(attempts, billed_cached),
                  "output_tokens": product(attempts, output_tokens)}
    elif kind == "embedding":
        items = product(n("items", integer=True), sensitivity)
        require(items is None or items.denominator == 1, "whole embedding items")
        attempts = product(items, n("max_attempts_per_item", integer=True, positive=True))
        require(attempts is None or attempts.denominator == 1, "whole embedding attempts")
        result = {"max_attempts": attempts,
                  "embedding_tokens": product(attempts, n("tokens_per_item", integer=True))}
    elif kind == "accelerator":
        require(inputs["timing_mode"] in {"duration", "throughput"}, "timing mode")
        duration = n("seconds_per_job")
        units = n("work_units_per_job")
        throughput = n("units_per_second", positive=True)
        text(inputs["work_unit"], "work_unit")
        if inputs["timing_mode"] == "duration":
            require(units is None and throughput is None, "unused throughput fields must be null")
        else:
            require(duration is None, "unused duration must be null")
            duration = None if units is None or throughput is None else units / throughput
        jobs = product(n("jobs", integer=True), sensitivity)
        require(jobs is None or jobs.denominator == 1, "whole accelerator jobs")
        seconds = product(jobs, duration, n("accelerators_per_job", integer=True, positive=True))
        result = {"jobs": jobs, "seconds_per_job": duration,
                  "accelerator_hours": None if seconds is None else seconds / 3600,
                  "minimum_memory_gib": n("minimum_memory_gib")}
    elif kind == "ci":
        jobs = product(n("jobs", integer=True), sensitivity)
        require(jobs is None or jobs.denominator == 1, "whole CI jobs")
        result = {"jobs": jobs, "ci_minutes": product(jobs, n("minutes_per_job"))}
    elif kind == "storage":
        # Storage duration and footprint are explicit; traffic is not a storage model.
        result = {"storage_gib": n("gib"), "gib_months": product(n("gib"), n("months"))}
    else:
        result = {"egress_gib": product(n("gib"), sensitivity)}
    return result


def price(component, quantity, sources):
    pricing = component["pricing"]
    keys(pricing, {"currency", "billing_mode", "mode_eligible", "rates", "source_refs"}, "pricing")
    currency = pricing["currency"]
    require(currency is None or type(currency) is str and re.fullmatch(r"[A-Z]{3}", currency),
            "currency: ISO-style code or null; no conversion is performed")
    require(pricing["billing_mode"] in {"standard", "batch", "unknown"}, "billing mode")
    eligible = tri(pricing["mode_eligible"], "mode_eligible")
    keys(pricing["rates"], RATE_KEYS[component["kind"]], "rates")
    rates = {k: number(v, k) for k, v in pricing["rates"].items()}
    refs(pricing["source_refs"], sources, "pricing", required=any(v is not None for v in rates.values()))
    terms = {}
    for key, rate in rates.items():
        amount = quantity[key]
        # Exact known zero usage has zero metered cost; missing usage never does.
        terms[key] = Fraction(0) if amount == 0 else product(amount, rate)
        if terms[key] is not None and component["kind"] in {"api", "embedding"}:
            terms[key] /= 1_000_000
    total = (sum(terms.values(), Fraction(0)) if all(v is not None for v in terms.values())
             and currency is not None and eligible is True and pricing["billing_mode"] != "unknown" else None)
    return currency, total, {k: exact(v) for k, v in terms.items()}


def capacity(component, quantity, sources):
    limits = component["limits"]
    keys(limits, {"period_matches", "values", "source_refs", "note"}, "limits")
    matches = tri(limits["period_matches"], "period_matches")
    keys(limits["values"], LIMIT_KEYS, "limit values")
    values = {k: number(v, k) for k, v in limits["values"].items()}
    refs(limits["source_refs"], sources, "limits", required=any(v is not None for v in values.values()))
    text(limits["note"], "limits note")
    used = {k: v for k, v in quantity.items() if k in LIMIT_KEYS}
    if component["kind"] in {"api", "embedding"}:
        used["requests"] = quantity["max_attempts"]
        used["tokens"] = (product(Fraction(1), quantity["embedding_tokens"])
                          if component["kind"] == "embedding" else
                          None if quantity["input_tokens_total"] is None or quantity["output_tokens"] is None
                          else quantity["input_tokens_total"] + quantity["output_tokens"])
    if "minimum_memory_gib" in quantity:
        used["available_memory_gib"] = quantity["minimum_memory_gib"]
    return {key: {"demand": exact(value), "limit": exact(values[key]),
                  "status": "unknown" if matches is not True or value is None or values[key] is None
                  else "exceeds" if value > values[key] else "within"}
            for key, value in used.items()}


def support(component, cost, currency, sources):
    offer = component["support"]
    realized = component["realization"]
    output = {"face_value": None, "potential_useful_coverage": None,
              "uncovered_list_exposure": None, "gross_avoided_cash": None,
              "incremental_cash": None, "net_avoided_cash": None}
    if offer is None:
        require(realized is None, "realization needs an identified support record")
        return output
    keys(offer, {"currency", "face_value", "eligible", "activated", "eligible_spend_limit",
                 "before_expiry_spend_limit", "source_refs", "note"}, "support")
    require(offer["currency"] is None or type(offer["currency"]) is str and
            re.fullmatch(r"[A-Z]{3}", offer["currency"]), "support currency")
    eligible = tri(offer["eligible"], "support eligible")
    active = tri(offer["activated"], "support activated")
    face = number(offer["face_value"], "face_value")
    eligible_cap = number(offer["eligible_spend_limit"], "eligible_spend_limit")
    expiry_cap = number(offer["before_expiry_spend_limit"], "before_expiry_spend_limit")
    text(offer["note"], "support note")
    refs(offer["source_refs"], sources, "support", required=any(v is not None for v in (face, eligible_cap, expiry_cap)))
    output["face_value"] = {"currency": offer["currency"], "amount": exact(face)}
    same_currency = currency is not None and offer["currency"] == currency
    coverage = None
    if same_currency and eligible is False:
        coverage = Fraction(0)
    elif same_currency and eligible is True and all(v is not None for v in (cost, face, eligible_cap, expiry_cap)):
        coverage = min(cost, face, eligible_cap, expiry_cap)
    output["potential_useful_coverage"] = exact(coverage)
    output["uncovered_list_exposure"] = exact(None if cost is None or coverage is None else cost - coverage)
    if realized is not None:
        keys(realized, {"currency", "completed", "evidence_kind", "necessary_counterfactual_cash", "actual_covered_cash",
                        "incremental_cash", "source_refs", "note"}, "realization")
        require(realized["evidence_kind"] in {"unknown", "measured", "synthetic"}, "realization evidence kind")
        completed = tri(realized["completed"], "realization completed")
        counterfactual = number(realized["necessary_counterfactual_cash"], "necessary_counterfactual_cash")
        covered = number(realized["actual_covered_cash"], "actual_covered_cash")
        incremental = number(realized["incremental_cash"], "incremental_cash")
        require(covered is None or all(cap is None or covered <= cap for cap in
                                      (face, eligible_cap, expiry_cap)),
                "actual covered cash exceeds the stated support caps")
        refs(realized["source_refs"], sources, "realization", required=True)
        text(realized["note"], "realization note")
        require(realized["currency"] is None or type(realized["currency"]) is str and
                re.fullmatch(r"[A-Z]{3}", realized["currency"]), "realization currency")
        if (same_currency and realized["currency"] == currency and eligible is True and active is True
                and completed is True and realized["evidence_kind"] in {"measured", "synthetic"}
                and all(v is not None for v in (counterfactual, covered, incremental))):
            gross = min(counterfactual, covered)
            output.update(gross_avoided_cash=exact(gross), incremental_cash=exact(incremental),
                          net_avoided_cash=exact(gross - incremental))
            output["realization_evidence_kind"] = realized["evidence_kind"]
    return output


def cash_quote(component, sources):
    """A separately sourced payable quote; never substitute computed list value."""
    quote = component.get("cash_quote")
    if quote is None:
        return None
    keys(quote, {"currency", "amount", "complete_for_period", "evidence_kind", "source_refs", "note"}, "cash quote")
    require(quote["currency"] is None or type(quote["currency"]) is str and
            re.fullmatch(r"[A-Z]{3}", quote["currency"]), "cash quote currency")
    amount = number(quote["amount"], "cash quote amount")
    complete = tri(quote["complete_for_period"], "cash quote completeness")
    require(quote["evidence_kind"] in KINDS, "cash quote evidence kind")
    refs(quote["source_refs"], sources, "cash quote", required=amount is not None)
    text(quote["note"], "cash quote note")
    return {"currency": quote["currency"], "amount": exact(amount),
            "complete_for_period": complete, "evidence_kind": quote["evidence_kind"]}


def calculate(document):
    require(document.get("schema_version") == 1 and type(document.get("schema_version")) is int,
            "schema_version must be integer 1")
    require(type(document.get("sources")) is list and bool(document["sources"]), "sources required")
    source_ids = set()
    for source in document["sources"]:
        identifier = text(source["id"], "source id")
        require(identifier not in source_ids, "duplicate source id")
        source_ids.add(identifier)
        for key in ("url", "reviewed_on", "classification", "finding"):
            text(source[key], "source " + key)
    require(type(document.get("scenarios")) is list and bool(document["scenarios"]), "scenarios required")
    scenarios, seen_scenarios = [], set()
    for scenario in document["scenarios"]:
        sid = text(scenario["id"], "scenario id")
        require(sid not in seen_scenarios, "duplicate scenario id")
        seen_scenarios.add(sid)
        evidence(scenario["evidence"], source_ids, sid)
        keys(scenario["period"], {"unit", "count", "start", "end"}, "period")
        require(scenario["period"]["unit"] in {"month", "study", "run"}, "period unit")
        require(number(scenario["period"]["count"], "period count", integer=True, positive=True) is not None,
                "period count required")
        for key in ("start", "end"):
            value = scenario["period"][key]
            require(value is None or type(value) is str and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value),
                    "period date or null")
            if value is not None:
                date.fromisoformat(value)
        start, end = scenario["period"]["start"], scenario["period"]["end"]
        require(start is None or end is None or start <= end, "period end precedes start")
        complete = tri(scenario["resource_inventory_complete"], "resource inventory")
        sensitivity = number(scenario["traffic_multiplier"], "traffic multiplier")
        require(sensitivity is not None, "explicit traffic multiplier required")
        require(type(scenario["workloads"]) is list and bool(scenario["workloads"]), "workloads required")
        rows, seen_workloads, seen_components, seen_scopes = [], set(), set(), set()
        for workload in scenario["workloads"]:
            wid, wclass = text(workload["id"], "workload id"), workload["class"]
            require(wid not in seen_workloads and wclass in CLASSES, "unique workload and known class required")
            seen_workloads.add(wid)
            require(workload["need_id"] == CLASSES[wclass], "workload need/scope mismatch")
            text(workload["scope_note"], "scope note")
            require(type(workload["components"]) is list and bool(workload["components"]), "components required")
            for component in workload["components"]:
                cid, scope = text(component["id"], "component id"), text(component["scope_key"], "scope key")
                require(cid not in seen_components and scope.casefold().strip() not in seen_scopes,
                        "duplicate component or physical billing scope")
                seen_components.add(cid); seen_scopes.add(scope.casefold().strip())
                require(component["kind"] in RATE_KEYS, "resource kind")
                evidence(component["evidence"], source_ids, cid)
                quantity = quantities(component, sensitivity)
                currency, cost, terms = price(component, quantity, source_ids)
                rows.append({"workload_id": wid, "class": wclass, "need_id": workload["need_id"],
                             "component_id": cid, "scope_key": scope, "kind": component["kind"],
                             "evidence_kind": component["evidence"]["kind"],
                             "quantities": {k: exact(v) for k, v in quantity.items()},
                             "currency": currency, "metered_list_cost": exact(cost),
                             "price_terms": terms, "limits": capacity(component, quantity, source_ids),
                             "support": support(component, cost, currency, source_ids),
                             "payable_cash_quote": cash_quote(component, source_ids)})
        groups = {}
        for wclass in sorted({r["class"] for r in rows}):
            selected = [r for r in rows if r["class"] == wclass]
            totals = {}
            for row in selected:
                if row["currency"] is not None and row["metered_list_cost"] is not None:
                    totals[row["currency"]] = totals.get(row["currency"], Fraction(0)) + Fraction(row["metered_list_cost"])
            class_complete = complete is True and all(r["currency"] is not None and
                                                     r["metered_list_cost"] is not None for r in selected)
            groups[wclass] = {"known_metered_subtotals": {k: exact(v) for k, v in sorted(totals.items())},
                              "complete_metered_totals": {k: exact(v) for k, v in sorted(totals.items())}
                              if class_complete else None,
                              "component_count": len(selected)}
        research = [r for r in rows if r["class"] == "research"]
        period_admissible = (bool(research) and complete is True and scenario["period"]["unit"] == "month"
                      and scenario["period"]["count"] == 1
                      and scenario["evidence"]["kind"] in {"planning_estimate", "measured"}
                      and all(r["evidence_kind"] in {"planning_estimate", "measured"} for r in research))
        metered_admissible = period_admissible and all(r["currency"] == "USD" and
                                                     r["metered_list_cost"] is not None for r in research)
        cash_admissible = period_admissible and all(r["payable_cash_quote"] is not None and
            r["payable_cash_quote"]["complete_for_period"] is True and
            r["payable_cash_quote"]["evidence_kind"] in {"planning_estimate", "measured"} and
            r["payable_cash_quote"]["currency"] == "USD" and
            r["payable_cash_quote"]["amount"] is not None for r in research)
        scenarios.append({"id": sid, "evidence_kind": scenario["evidence"]["kind"],
                          "period": copy.deepcopy(scenario["period"]), "traffic_multiplier": exact(sensitivity),
                          "resource_inventory_complete": complete, "components": rows, "by_class": groups,
                          "budget_handoff": {
                              "research_monthly_metered_cost_cents": sum(cents(Fraction(r["metered_list_cost"]))
                                                                        for r in research) if metered_admissible else None,
                              "research_monthly_cash_cost_cents": sum(cents(Fraction(r["payable_cash_quote"]["amount"]))
                                                                     for r in research) if cash_admissible else None,
                              "unit": "USD cents per one relative month, per-component half-up rounding",
                              "scope": "N06 research only; excludes N01 hosting, N03 CI and public demonstrations",
                              "limitation": "Metered list cost and separately sourced complete payable cash quotes are distinct. The exact source, period, billing scope and quote need independent admission before #20 use. No actual cash or funding inferred."}})
    return {"arithmetic": "Exact nonnegative decimal inputs; rational-string outputs, no FX conversion.",
            "actual_project_spending": None, "actual_project_support_received": None,
            "scenarios": scenarios}


def load(path):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key: " + key)
            result[key] = value
        return result

    def reject(value):
        raise ValueError("JSON floats/nonfinite values are forbidden; use decimal strings: " + value)

    return json.loads(Path(path).read_text(encoding="utf-8"), object_pairs_hook=pairs,
                      parse_float=reject, parse_constant=reject)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT)
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--check", action="store_true")
    action.add_argument("--write", action="store_true")
    args = parser.parse_args()
    document = load(args.input)
    result = calculate(document)
    if args.check:
        # Serialized comparison also distinguishes bool and integer aliases.
        require(json.dumps(document.get("calculated"), sort_keys=True) == json.dumps(result, sort_keys=True),
                "committed calculated output differs")
        print("Compute-demand model: exact calculated output matches.")
    elif args.write:
        document["calculated"] = result
        args.input.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
