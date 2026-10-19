#!/usr/bin/env python3
"""Recalculate the twelve-month planning budget offline, using integer cents.

Unknown inputs propagate to complete totals. Known subtotals, contingent support
and a reserve stock remain separate; this calculator never authorizes spending.
"""

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data/budget/operating-budget.json"
SCHEMA = "pya-operating-budget/v1"
MONTHS = 12
COST_MODES = {
    "website_domain": "monthly",
    "ci_incremental": "scaled_monthly",
    "research_compute": "scaled_monthly",
    "evidence_licensing": "monthly",
    "mobile_equipment": "one_time",
    "security_accessibility": "one_time",
    "project_coordination": "monthly",
    "route_admin_extras": "monthly",
    "taxes": "monthly",
    "processor_fees": "monthly",
    "migration_exit": "one_time",
    "independent_formation_other": "independent_one_time",
}
FUNDING_KEYS = (
    "external_unrestricted_cash_receipts",
    "external_restricted_cash_receipts",
    "contingent_cash_awards",
    "credit_face_value",
    "evidenced_avoided_cost",
)
PATH_IDS = {"community", "osc", "sfc", "spi", "independent_1023", "independent_1023_ez"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, location, *, nullable=True, maximum=None):
    if value is None and nullable:
        return
    require(type(value) is int and value >= 0,
            f"{location}: expected nonnegative integer, not a boolean or float")
    require(maximum is None or value <= maximum, f"{location}: exceeds {maximum}")


def series(values, location):
    require(isinstance(values, list) and len(values) == MONTHS,
            f"{location}: expected exactly twelve monthly values")
    for i, value in enumerate(values, 1):
        integer(value, f"{location}[month {i}]")


def one_time(amount, month):
    # A positive amount with unknown timing cannot be placed in this horizon.
    if amount == 0:
        return [0] * MONTHS
    if month is None:
        return [None] * MONTHS
    return [amount if i == month else 0 for i in range(1, MONTHS + 1)]


def rounded(numerator, denominator=10000):
    """Nonnegative rational to cents: nearest integer, exact half rounded up."""
    return (2 * numerator + denominator) // (2 * denominator)


def scaled(value, basis_points):
    return None if value is None else rounded(value * basis_points)


def complete_sum(values):
    return None if any(value is None for value in values) else sum(values)


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON property: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"non-finite JSON number: {value}")


def load_budget(path):
    return json.loads(path.read_text(encoding="utf-8"),
                      object_pairs_hook=reject_duplicate_keys,
                      parse_constant=reject_nonfinite)


def validate(document):
    require(isinstance(document, dict) and document.get("schema_version") == SCHEMA,
            f"expected schema_version {SCHEMA}")
    parameters = document["parameters"]
    require(parameters["currency"] == "USD", "v1 calculates USD cents only; do not mix currencies")
    require(type(parameters["months"]) is int and parameters["months"] == MONTHS,
            "budget horizon must be twelve months")
    start = parameters["start_month"]
    require(start is None or (isinstance(start, str) and
            re.fullmatch(r"[0-9]{4}-(?:0[1-9]|1[0-2])", start) and not start.startswith("0000-")),
            "start_month must be null or YYYY-MM")
    integer(parameters["contingency_bps"], "contingency_bps", maximum=10000)
    integer(parameters["reserve_months"], "reserve_months", maximum=MONTHS)
    integer(parameters["formation_month"], "formation_month", maximum=MONTHS)
    require(parameters["formation_month"] != 0, "formation_month must be 1..12 or null")
    require(parameters["selected_legal_path"] is None or
            parameters["selected_legal_path"] in PATH_IDS, "unknown legal path")

    hosting = document["hosting"]
    for key in ("vm_count", "vm_unit_monthly_cents", "database_count",
                "database_unit_monthly_cents", "backup_bps_of_vm_cost",
                "export_monthly_cents", "same_scope_ceiling_monthly_cents"):
        integer(hosting[key], f"hosting.{key}", nullable=False)
    require(hosting["backup_bps_of_vm_cost"] <= 10000, "backup proportion exceeds 100%")

    source_ids = {source["id"] for source in document["sources"]}
    require(len(source_ids) == len(document["sources"]), "duplicate source ID")
    costs = document["cost_inputs"]
    require(isinstance(costs, list), "cost_inputs must be a list")
    ids = [cost["id"] for cost in costs]
    require(len(ids) == len(set(ids)) and set(ids) == set(COST_MODES),
            "cost IDs must contain every v1 scope exactly once; no duplicate hosting line")
    scopes = [cost["exclusive_scope"] for cost in costs]
    require(len(scopes) == len(set(scopes)), "duplicate exclusive cost scope")
    require("leaderboard_hosting" not in scopes, "N01 hosting is already priced once")
    for cost in costs:
        name = cost["id"]
        mode = COST_MODES[name]
        require(cost["mode"] == mode, f"{name}: unexpected cost mode")
        require(cost["evidence_class"] in {"unmeasured", "engineering_estimate", "quote", "synthetic"},
                f"{name}: input is a planning assumption, not an actual-expense claim")
        require(isinstance(cost["source_refs"], list) and cost["source_refs"] and
                all(ref in source_ids for ref in cost["source_refs"]), f"{name}: missing source provenance")
        if mode.endswith("one_time"):
            integer(cost["amount_cents"], f"{name}.amount_cents")
            integer(cost["month"], f"{name}.month", maximum=MONTHS)
            require(cost["month"] != 0, f"{name}: month must be 1..12 or null")
            known = cost["amount_cents"] is not None
        else:
            series(cost["monthly_cents"], name)
            known = any(value is not None for value in cost["monthly_cents"])
        require(not known or cost["evidence_class"] != "unmeasured",
                f"{name}: populated estimate needs an explicit evidence class")
        if name == "research_compute" and known and cost["evidence_class"] != "synthetic":
            handoff = document["compute_handoff"]
            require(isinstance(handoff["source_revision"], str) and
                    re.fullmatch(r"[0-9a-f]{40}", handoff["source_revision"]),
                    "research_compute: an exact #21 source revision is required")
            mapping = handoff["field_and_scope_mapping"]
            require(isinstance(mapping, str) and bool(mapping.strip()),
                    "research_compute: #21 units and scope mapping must be nonblank text")

    paths = document["legal_paths"]
    require(len(paths) == len(PATH_IDS) and {path["id"] for path in paths} == PATH_IDS,
            "legal alternatives must each appear exactly once")
    for path in paths:
        integer(path["host_fee_bps"], f"{path['id']}.host_fee_bps", maximum=10000)
        integer(path["federal_application_fee_cents"], f"{path['id']}.federal_application_fee_cents")
    scenarios = document["scenarios"]
    require(len(scenarios) == 3 and {s["id"] for s in scenarios} == {"lean", "expected", "stress"},
            "exactly lean, expected and stress scenarios are required")
    for scenario in scenarios:
        integer(scenario["workload_multiplier_bps"], "workload multiplier", nullable=False)
        require(scenario["hosting_profile"] in {"planned", "same_scope_ceiling"},
                "unknown hosting profile")
    require(set(document["funding_inputs"]) == set(FUNDING_KEYS), "funding measures must remain separate")
    for key in FUNDING_KEYS:
        series(document["funding_inputs"][key], f"funding.{key}")


def calculate(document):
    validate(document)
    parameters = document["parameters"]
    hosting = document["hosting"]
    chosen = parameters["selected_legal_path"]
    path = next((item for item in document["legal_paths"] if item["id"] == chosen), None)
    results = []
    for scenario in document["scenarios"]:
        amounts = {}
        one_time_ids = {"federal_application_fee"}
        if scenario["hosting_profile"] == "planned":
            vm = hosting["vm_count"] * hosting["vm_unit_monthly_cents"]
            amounts.update({
                "hosting_vms": [vm] * MONTHS,
                "hosting_databases": [hosting["database_count"] * hosting["database_unit_monthly_cents"]] * MONTHS,
                "hosting_backups": [rounded(vm * hosting["backup_bps_of_vm_cost"])] * MONTHS,
                "hosting_exports": [hosting["export_monthly_cents"]] * MONTHS,
            })
        else:
            amounts["hosting_same_scope_ceiling"] = [hosting["same_scope_ceiling_monthly_cents"]] * MONTHS
        for cost in document["cost_inputs"]:
            name, mode = cost["id"], cost["mode"]
            if mode.endswith("one_time"):
                one_time_ids.add(name)
                values = one_time(cost["amount_cents"], cost["month"])
                if mode == "independent_one_time":
                    values = ([None] * MONTHS if chosen is None else values
                              if chosen.startswith("independent_") else [0] * MONTHS)
            else:
                values = list(cost["monthly_cents"])
                if mode == "scaled_monthly":
                    values = [scaled(value, scenario["workload_multiplier_bps"]) for value in values]
            amounts[name] = values

        federal = None if path is None else path["federal_application_fee_cents"]
        amounts["federal_application_fee"] = one_time(federal, parameters["formation_month"])
        fee_bps = None if path is None else path["host_fee_bps"]
        funding = document["funding_inputs"]
        amounts["host_administration_fee"] = []
        for i in range(MONTHS):
            gross = complete_sum([funding["external_unrestricted_cash_receipts"][i],
                                  funding["external_restricted_cash_receipts"][i]])
            fee = (0 if fee_bps == 0 else None if fee_bps is None or gross is None
                   else rounded(gross * fee_bps))
            amounts["host_administration_fee"].append(fee)

        months = []
        for i in range(MONTHS):
            line_items = {name: values[i] for name, values in amounts.items()}
            missing = [name for name, value in line_items.items() if value is None]
            subtotal = sum(value for value in line_items.values() if value is not None)
            total = None if missing else subtotal
            contingency = (None if total is None or parameters["contingency_bps"] is None
                           else rounded(total * parameters["contingency_bps"]))
            months.append({
                "month": i + 1,
                "cash_costs_cents": line_items,
                "known_cost_subtotal_cents": subtotal,
                "missing_cost_ids": missing,
                "complete_cash_cost_cents": total,
                "contingency_allowance_cents": contingency,
                "cash_requirement_with_contingency_cents": complete_sum([total, contingency]),
                "funding_measures_cents": {key: funding[key][i] for key in FUNDING_KEYS},
            })
        recurring_total = complete_sum([value for name, values in amounts.items()
                                        if name not in one_time_ids for value in values])
        reserve = (None if recurring_total is None or parameters["reserve_months"] is None
                   else rounded(recurring_total * parameters["reserve_months"], MONTHS))
        results.append({
            "scenario": scenario["id"],
            "legal_path_hypothesis": chosen,
            "monthly": months,
            "annual": {
                "known_cost_subtotal_cents": sum(m["known_cost_subtotal_cents"] for m in months),
                "complete_cash_cost_cents": complete_sum([m["complete_cash_cost_cents"] for m in months]),
                "contingency_allowance_cents": complete_sum([m["contingency_allowance_cents"] for m in months]),
                "cash_requirement_with_contingency_cents": complete_sum([m["cash_requirement_with_contingency_cents"] for m in months]),
                "liquidity_reserve_target_cents": reserve,
                "funding_measures_cents": {key: complete_sum(funding[key]) for key in FUNDING_KEYS},
            },
        })
    return {"currency": "USD", "money_unit": "integer cents", "actual_available_cash_cents": None,
            "status": "Planning only; complete totals remain null when a required input is unknown",
            "scenarios": results}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="verify the committed derived snapshot")
    mode.add_argument("--write", action="store_true", help="replace only calculated outputs in the input file")
    args = parser.parse_args(argv)
    try:
        document = load_budget(args.input)
        calculated = calculate(document)
        if args.check:
            require(json.dumps(document.get("calculated"), sort_keys=True) ==
                    json.dumps(calculated, sort_keys=True),
                    "derived budget is stale or has wrong value types; recalculate with --write")
            print("PASS: three scenarios, twelve months each; exact integer-cent outputs reproduced")
        elif args.write:
            document["calculated"] = calculated
            args.input.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        else:
            print(json.dumps(calculated, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
