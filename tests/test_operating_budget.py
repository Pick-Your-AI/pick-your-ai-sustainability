"""Independent arithmetic and failure controls for the planning budget."""

import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("operating_budget", ROOT / "scripts/operating_budget.py")
BUDGET = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BUDGET)


class OperatingBudgetTests(unittest.TestCase):
    def setUp(self):
        self.document = BUDGET.load_budget(ROOT / "data/budget/operating-budget.json")

    def cost(self, name):
        return next(row for row in self.document["cost_inputs"] if row["id"] == name)

    def scenario(self, name="expected"):
        return next(row for row in BUDGET.calculate(self.document)["scenarios"]
                    if row["scenario"] == name)

    def fully_priced_synthetic(self):
        # These explicit zeros belong only to a counterfactual control; never
        # write this control over the public project's unmeasured baseline.
        self.document["parameters"].update(selected_legal_path="community",
                                            contingency_bps=0, reserve_months=0)
        for row in self.document["cost_inputs"]:
            row["evidence_class"] = "synthetic"
            if row["mode"].endswith("one_time"):
                row.update(amount_cents=0, month=None)
            else:
                row["monthly_cents"] = [0] * 12
        for key in BUDGET.FUNDING_KEYS:
            self.document["funding_inputs"][key] = [0] * 12
        self.document["host_fee_inputs"].update(monthly_base_cents=[0] * 12,
            evidence_class="synthetic", scope_mapping="Synthetic qualifying fee base for the selected host only")

    def test_committed_outputs_reproduce_without_mutating_source_inputs(self):
        original = copy.deepcopy(self.document)
        result = BUDGET.calculate(self.document)
        self.assertEqual(self.document, original)
        self.assertEqual(result, self.document["calculated"])
        self.assertEqual(len(result["scenarios"]), 3)
        self.assertTrue(all(len(row["monthly"]) == 12 for row in result["scenarios"]))

    def test_real_baseline_keeps_unknowns_and_partial_totals_distinct(self):
        for name, expected in [("lean", 135240), ("expected", 135240), ("stress", 240000)]:
            annual = self.scenario(name)["annual"]
            self.assertEqual(annual["known_cost_subtotal_cents"], expected)
            for key in ("complete_cash_cost_cents", "contingency_allowance_cents",
                        "cash_requirement_with_contingency_cents", "liquidity_reserve_target_cents"):
                self.assertIsNone(annual[key])
            self.assertTrue(all(value is None for value in annual["funding_measures_cents"].values()))
        self.assertIsNone(BUDGET.calculate(self.document)["actual_available_cash_cents"])
        self.assertTrue(all(value is None for value in self.document["actuals"].values()))

    def test_same_scope_ceiling_replaces_all_four_hosting_components(self):
        self.fully_priced_synthetic()
        planned = self.scenario()["monthly"][0]["cash_costs_cents"]
        stress = self.scenario("stress")["monthly"][0]["cash_costs_cents"]
        self.assertEqual({k: v for k, v in planned.items() if k.startswith("hosting_")},
                         {"hosting_vms": 4800, "hosting_databases": 3030,
                          "hosting_backups": 1440, "hosting_exports": 2000,
                          "hosting_extras": 0})
        self.assertEqual({k: v for k, v in stress.items() if k.startswith("hosting_")},
                         {"hosting_same_scope_ceiling": 20000, "hosting_extras": 0})
        self.assertEqual(self.scenario("stress")["annual"]["complete_cash_cost_cents"], 240000)

    def test_n01_extras_are_in_planned_cost_but_already_inside_all_in_ceiling(self):
        self.fully_priced_synthetic()
        self.cost("hosting_extras")["monthly_cents"] = [1000] * 12
        self.cost("taxes")["monthly_cents"] = [300] * 12
        for name in ("lean", "expected"):
            result = self.scenario(name)
            self.assertEqual(result["monthly"][0]["complete_cash_cost_cents"], 12570)
            self.assertEqual(result["annual"]["complete_cash_cost_cents"], 150840)
        stress = self.scenario("stress")
        self.assertEqual(stress["monthly"][0]["cash_costs_cents"]["hosting_extras"], 0)
        self.assertEqual(stress["monthly"][0]["cash_costs_cents"]["taxes"], 300)
        self.assertEqual(stress["annual"]["complete_cash_cost_cents"], 243600)

    def test_unknown_n01_extras_only_invalidate_planned_profile(self):
        self.fully_priced_synthetic()
        self.cost("hosting_extras")["monthly_cents"][0] = None
        self.assertIsNone(self.scenario()["monthly"][0]["complete_cash_cost_cents"])
        self.assertEqual(self.scenario("stress")["annual"]["complete_cash_cost_cents"], 240000)
        self.cost("taxes")["monthly_cents"][0] = None
        self.assertIsNone(self.scenario("stress")["annual"]["complete_cash_cost_cents"])

    def test_tax_and_hosting_extras_need_scopes_cannot_be_interchanged(self):
        for name, needs in (("taxes", ["N01"]), ("hosting_extras", ["N02"])):
            with self.subTest(cost=name):
                original = self.cost(name)["need_ids"]
                self.cost(name)["need_ids"] = needs
                with self.assertRaisesRegex(ValueError, "N01"):
                    BUDGET.calculate(self.document)
                self.cost(name)["need_ids"] = original

    def test_all_in_ceiling_is_excluded_from_additional_contingency_base(self):
        self.fully_priced_synthetic()
        self.document["parameters"]["contingency_bps"] = 1000
        self.cost("hosting_extras")["monthly_cents"] = [1000] * 12
        self.cost("taxes")["monthly_cents"] = [300] * 12
        expected = self.scenario()["monthly"][0]
        self.assertEqual(expected["contingency_base_cents"], 12570)
        self.assertEqual(expected["contingency_allowance_cents"], 1257)
        stress = self.scenario("stress")["monthly"][0]
        self.assertEqual(stress["contingency_base_cents"], 300)
        self.assertEqual(stress["contingency_allowance_cents"], 30)
        self.assertEqual(stress["cash_requirement_with_contingency_cents"], 20330)

    def test_fractional_cent_scale_rounds_once_per_line_and_month(self):
        self.fully_priced_synthetic()
        self.cost("research_compute")["monthly_cents"] = [1] * 12
        for name, month, annual in [("lean", 1, 135252), ("expected", 1, 135252), ("stress", 2, 240024)]:
            result = self.scenario(name)
            self.assertEqual(result["monthly"][0]["cash_costs_cents"]["research_compute"], month)
            self.assertEqual(result["annual"]["complete_cash_cost_cents"], annual)
        self.assertEqual(BUDGET.rounded(4999), 0)
        self.assertEqual(BUDGET.rounded(5000), 1)
        self.assertEqual(BUDGET.rounded(14999), 1)
        self.assertEqual(BUDGET.rounded(15000), 2)

    def test_unknown_variable_cost_is_not_zero_even_at_zero_scale(self):
        self.fully_priced_synthetic()
        self.cost("research_compute")["monthly_cents"][5] = None
        self.document["scenarios"][0]["workload_multiplier_bps"] = 0
        result = self.scenario("lean")
        self.assertIsNone(result["monthly"][5]["cash_costs_cents"]["research_compute"])
        self.assertIsNone(result["annual"]["complete_cash_cost_cents"])

    def test_one_time_equipment_is_counted_once_across_platforms(self):
        self.fully_priced_synthetic()
        self.cost("mobile_equipment").update(amount_cents=12345, month=7)
        result = self.scenario()
        self.assertEqual([row["cash_costs_cents"]["mobile_equipment"] for row in result["monthly"]],
                         [0] * 6 + [12345] + [0] * 5)
        self.assertEqual(result["annual"]["complete_cash_cost_cents"], 147585)

    def test_unknown_one_time_timing_is_not_assigned_an_arbitrary_month(self):
        self.fully_priced_synthetic()
        self.cost("mobile_equipment").update(amount_cents=12345, month=None)
        result = self.scenario()
        self.assertTrue(all(row["cash_costs_cents"]["mobile_equipment"] is None for row in result["monthly"]))
        self.assertIsNone(result["annual"]["complete_cash_cost_cents"])
        self.cost("mobile_equipment").update(amount_cents=None, month=7)
        self.assertEqual([row["cash_costs_cents"]["mobile_equipment"] for row in self.scenario()["monthly"]],
                         [0] * 6 + [None] + [0] * 5)

    def test_mutually_exclusive_federal_candidates_and_actual_filing_gate(self):
        self.fully_priced_synthetic()
        for path, fee in [("independent_1023_ez", 27500), ("independent_1023", 60000)]:
            self.document["parameters"].update(selected_legal_path=path, formation_month=3)
            result = self.scenario()
            self.assertEqual(result["annual"]["complete_cash_cost_cents"], 135240 + fee)
            self.assertEqual([row["cash_costs_cents"]["federal_application_fee"] for row in result["monthly"]],
                             [0, 0, fee] + [0] * 9)
        self.document["parameters"]["formation_month"] = None
        self.assertIsNone(self.scenario()["annual"]["complete_cash_cost_cents"])

    def test_hosted_routes_exclude_independent_formation_costs(self):
        self.fully_priced_synthetic()
        self.cost("independent_formation_other").update(amount_cents=99999, month=2)
        for path in ("community", "osc", "sfc"):
            self.document["parameters"]["selected_legal_path"] = path
            result = self.scenario()
            self.assertEqual(result["annual"]["complete_cash_cost_cents"], 135240)
            self.assertTrue(all(row["cash_costs_cents"]["independent_formation_other"] == 0
                                for row in result["monthly"]))

    def test_host_fee_uses_processed_cash_not_awards_credits_or_avoided_cost(self):
        self.fully_priced_synthetic()
        self.document["parameters"]["selected_legal_path"] = "osc"
        funding = self.document["funding_inputs"]
        funding["external_unrestricted_cash_receipts"][0] = 10000
        funding["external_restricted_cash_receipts"][0] = 5000
        self.document["host_fee_inputs"]["monthly_base_cents"][0] = 15000
        for name in ("contingent_cash_awards", "credit_face_value", "evidenced_avoided_cost"):
            funding[name][0] = 9000000
        result = self.scenario()
        self.assertEqual(result["monthly"][0]["cash_costs_cents"]["host_administration_fee"], 1500)
        self.assertEqual(result["annual"]["complete_cash_cost_cents"], 136740)
        self.assertEqual(result["annual"]["funding_measures_cents"]["external_restricted_cash_receipts"], 5000)
        self.assertEqual(result["annual"]["funding_measures_cents"]["credit_face_value"], 9000000)
        self.assertIsNone(BUDGET.calculate(self.document)["actual_available_cash_cents"])

    def test_unknown_fee_or_fee_base_prevents_a_complete_cost(self):
        self.fully_priced_synthetic()
        self.document["parameters"]["selected_legal_path"] = "spi"
        next(path for path in self.document["legal_paths"] if path["id"] == "spi")["host_fee_bps"] = None
        self.assertIsNone(self.scenario()["annual"]["complete_cash_cost_cents"])
        self.document["parameters"]["selected_legal_path"] = "osc"
        self.document["host_fee_inputs"]["monthly_base_cents"][0] = None
        self.document["funding_inputs"]["external_restricted_cash_receipts"][0] = None
        self.assertIsNone(self.scenario()["monthly"][0]["cash_costs_cents"]["host_administration_fee"])
        self.assertIsNone(self.scenario()["annual"]["funding_measures_cents"]["external_restricted_cash_receipts"])

    def test_spi_current_donation_fee_uses_only_explicit_qualifying_base(self):
        self.fully_priced_synthetic()
        self.document["parameters"]["selected_legal_path"] = "spi"
        self.document["host_fee_inputs"]["monthly_base_cents"][0] = 10000
        self.document["funding_inputs"]["external_unrestricted_cash_receipts"][0] = 900000
        result = self.scenario()
        self.assertEqual(result["monthly"][0]["cash_costs_cents"]["host_administration_fee"], 500)
        self.assertEqual(result["annual"]["complete_cash_cost_cents"], 135740)
        self.assertNotIn("host_fee_base", result["annual"]["funding_measures_cents"])
        self.assertEqual(result["annual"]["funding_measures_cents"]["external_unrestricted_cash_receipts"], 900000)

    def test_fee_base_needs_evidence_and_nonblank_mapping(self):
        self.document["host_fee_inputs"]["monthly_base_cents"][0] = 0
        with self.assertRaisesRegex(ValueError, "evidence class"):
            BUDGET.calculate(self.document)
        self.document["host_fee_inputs"]["evidence_class"] = "synthetic"
        for invalid in (True, 17, [], {}, "", " \t\n"):
            with self.subTest(mapping=invalid):
                self.document["host_fee_inputs"]["scope_mapping"] = invalid
                with self.assertRaisesRegex(ValueError, "mapping"):
                    BUDGET.calculate(self.document)

    def test_contingency_and_reserve_are_distinct_from_baseline_expense(self):
        self.fully_priced_synthetic()
        self.document["parameters"].update(contingency_bps=1000, reserve_months=2)
        self.cost("mobile_equipment").update(amount_cents=10000, month=1)
        result = self.scenario()
        self.assertEqual(result["annual"]["complete_cash_cost_cents"], 145240)
        self.assertEqual(result["annual"]["contingency_allowance_cents"], 14524)
        self.assertEqual(result["annual"]["cash_requirement_with_contingency_cents"], 159764)
        self.assertEqual(result["annual"]["liquidity_reserve_target_cents"], 22540)

    def test_duplicate_missing_or_overlapping_scopes_are_rejected(self):
        for change in ("duplicate", "missing", "same_scope", "hosting"):
            with self.subTest(change=change):
                original = copy.deepcopy(self.document)
                if change == "duplicate":
                    self.document["cost_inputs"].append(copy.deepcopy(self.document["cost_inputs"][0]))
                elif change == "missing":
                    self.document["cost_inputs"].pop()
                elif change == "same_scope":
                    self.document["cost_inputs"][1]["exclusive_scope"] = self.document["cost_inputs"][0]["exclusive_scope"]
                else:
                    self.document["cost_inputs"][0]["exclusive_scope"] = "leaderboard_hosting"
                with self.assertRaises(ValueError):
                    BUDGET.calculate(self.document)
                self.document = original

    def test_booleans_floats_negative_and_wrong_monthly_shapes_are_rejected(self):
        for invalid in (True, False, 1.0, -1, "100", float("inf")):
            with self.subTest(value=repr(invalid)):
                self.cost("website_domain")["monthly_cents"][0] = invalid
                with self.assertRaises(ValueError):
                    BUDGET.calculate(self.document)
        self.cost("website_domain")["monthly_cents"] = [None] * 11
        with self.assertRaises(ValueError):
            BUDGET.calculate(self.document)

    def test_unmeasured_values_cannot_be_silently_populated(self):
        self.cost("website_domain")["monthly_cents"][0] = 0
        with self.assertRaisesRegex(ValueError, "evidence class"):
            BUDGET.calculate(self.document)

    def test_nonsynthetic_compute_needs_exact_upstream_scope_and_revision(self):
        row = self.cost("research_compute")
        row.update(evidence_class="engineering_estimate", monthly_cents=[100] * 12)
        with self.assertRaisesRegex(ValueError, "revision"):
            BUDGET.calculate(self.document)
        self.document["compute_handoff"]["source_revision"] = "a" * 40
        with self.assertRaisesRegex(ValueError, "mapping"):
            BUDGET.calculate(self.document)
        self.document["compute_handoff"]["field_and_scope_mapping"] = "Synthetic test-only USD-cent field; research scope only"
        self.assertEqual(self.scenario()["monthly"][0]["cash_costs_cents"]["research_compute"], 100)

    def test_compute_mapping_requires_nonblank_text_not_truthiness(self):
        self.cost("research_compute").update(evidence_class="engineering_estimate", monthly_cents=[100] * 12)
        self.document["compute_handoff"]["source_revision"] = "a" * 40
        for invalid in (True, 17, ["field"], {"field": "cost"}, "", " \t\n"):
            with self.subTest(mapping=invalid):
                self.document["compute_handoff"]["field_and_scope_mapping"] = invalid
                with self.assertRaisesRegex(ValueError, "mapping"):
                    BUDGET.calculate(self.document)

    def test_json_duplicate_and_nonfinite_values_fail_before_calculation(self):
        for source in ('{"amount":1,"amount":2}', '{"amount":NaN}', '{"amount":Infinity}'):
            with self.subTest(source=source), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "bad.json"
                path.write_text(source)
                with self.assertRaises(ValueError):
                    BUDGET.load_budget(path)

    def test_committed_snapshot_cannot_spoof_integer_types(self):
        for invalid in (True, 1.0):
            with self.subTest(value=invalid), tempfile.TemporaryDirectory() as directory:
                self.document["calculated"]["scenarios"][0]["monthly"][0]["month"] = invalid
                path = Path(directory) / "budget.json"
                path.write_text(json.dumps(self.document))
                with contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(BUDGET.main(["--input", str(path), "--check"]), 1)

    def test_invalid_calendar_route_and_policy_parameters_fail(self):
        for field, invalid in (("start_month", "0000-01"), ("start_month", "2026-13"),
                               ("formation_month", 0), ("formation_month", 13),
                               ("reserve_months", True), ("contingency_bps", 10001),
                               ("selected_legal_path", "all_hosts"), ("currency", "EUR")):
            with self.subTest(field=field, invalid=invalid):
                original = self.document["parameters"][field]
                self.document["parameters"][field] = invalid
                with self.assertRaises(ValueError):
                    BUDGET.calculate(self.document)
                self.document["parameters"][field] = original


if __name__ == "__main__":
    unittest.main()
