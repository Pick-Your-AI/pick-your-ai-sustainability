"""Independent arithmetic controls and counterexamples; no service or GPU use."""

import copy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("compute_demand", ROOT / "scripts/compute_demand.py")
MODEL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODEL)
DOCUMENT = MODEL.load(ROOT / "data/budget/compute-demand-model.json")


class ComputeDemandTests(unittest.TestCase):
    def setUp(self):
        self.document = copy.deepcopy(DOCUMENT)
        self.document["scenarios"] = [next(s for s in self.document["scenarios"]
                                           if s["id"] == "synthetic-base")]

    @property
    def scenario(self):
        return self.document["scenarios"][0]

    def component(self, identifier="synthetic-api"):
        return next(c for w in self.scenario["workloads"] for c in w["components"]
                    if c["id"] == identifier)

    def result(self):
        return MODEL.calculate(self.document)["scenarios"][0]

    def row(self, identifier="synthetic-api"):
        return next(r for r in self.result()["components"] if r["component_id"] == identifier)

    def admit_mock_cash_inputs(self):
        # Exercise the shape of a separately admitted quote in memory only.
        # These altered control labels are never persisted as real project evidence.
        self.scenario["evidence"]["kind"] = "planning_estimate"
        for workload in self.scenario["workloads"]:
            for component in workload["components"]:
                component["evidence"]["kind"] = "planning_estimate"
                if component["cash_quote"] is not None:
                    component["cash_quote"]["evidence_kind"] = "planning_estimate"

    def test_committed_snapshot_and_unmeasured_classes_remain_unknown(self):
        result = MODEL.calculate(DOCUMENT)
        self.assertEqual(result, DOCUMENT["calculated"])
        self.assertIsNone(result["actual_project_spending"])
        self.assertIsNone(result["actual_project_support_received"])
        current = result["scenarios"][0]
        self.assertEqual(set(current["by_class"]),
                         {"research", "product_hosting", "ci_testing", "public_demonstration"})
        for group in current["by_class"].values():
            self.assertEqual(group["known_metered_subtotals"], {})
            self.assertIsNone(group["complete_metered_totals"])
        self.assertTrue(all(r["metered_list_cost"] is None for r in current["components"]))
        self.assertIsNone(current["budget_handoff"]["research_monthly_cash_cost_cents"])

    def test_two_route_proposal_has_exact_slots_attempts_and_unknown_tokens(self):
        proposal = MODEL.calculate(DOCUMENT)["scenarios"][1]
        self.assertEqual(proposal["period"]["unit"], "study")
        self.assertEqual(len(proposal["components"]), 2)
        for row in proposal["components"]:
            self.assertEqual(row["quantities"]["logical_requests"], "144")
            self.assertEqual(row["quantities"]["max_attempts"], "288")
            self.assertIsNone(row["quantities"]["input_tokens_total"])
            self.assertIsNone(row["metered_list_cost"])
        self.assertEqual(sum(Fraction(r["quantities"]["max_attempts"])
                             for r in proposal["components"]), 576)
        self.assertIsNone(proposal["budget_handoff"]["research_monthly_cash_cost_cents"])

    def test_cached_input_is_a_subset_and_prices_are_per_million(self):
        row = self.row()
        self.assertEqual(row["quantities"], {
            "logical_requests": "1000", "max_attempts": "2000",
            "input_tokens_total": "2000000", "uncached_input_tokens": "1200000",
            "cached_input_tokens": "800000", "output_tokens": "400000"})
        self.assertEqual(row["price_terms"], {
            "uncached_input_tokens": "12/5", "cached_input_tokens": "2/5", "output_tokens": "8/5"})
        self.assertEqual(row["metered_list_cost"], "22/5")

    def test_accelerator_ci_storage_egress_and_embedding_units_are_distinct(self):
        gpu = self.row("synthetic-accelerator")
        self.assertEqual(gpu["quantities"]["seconds_per_job"], "900")
        self.assertEqual(gpu["quantities"]["accelerator_hours"], "2")
        self.assertEqual(gpu["metered_list_cost"], "5")
        self.assertEqual(self.row("synthetic-ci")["quantities"]["ci_minutes"], "50")
        self.assertEqual(self.row("synthetic-hosting-storage")["quantities"]["gib_months"], "50")
        self.assertEqual(self.row("synthetic-hosting-egress")["metered_list_cost"], "1/2")
        self.assertEqual(self.row("synthetic-demo-embedding")["metered_list_cost"], "1/10000")
        self.assertEqual(self.result()["by_class"]["research"]["complete_metered_totals"], {"USD": "47/5"})

    def test_sensitivities_change_work_not_storage_or_rates(self):
        results = {s["id"]: s for s in MODEL.calculate(DOCUMENT)["scenarios"]}
        for name, cost in (("low", "47/10"), ("base", "47/5"), ("high", "94/5")):
            result = results["synthetic-" + name]
            self.assertEqual(result["by_class"]["research"]["complete_metered_totals"], {"USD": cost})
            storage = next(r for r in result["components"] if r["kind"] == "storage")
            self.assertEqual(storage["quantities"]["gib_months"], "50")
            self.assertIsNone(result["budget_handoff"]["research_monthly_cash_cost_cents"])

    def test_unknown_quantity_survives_zero_rate_and_zero_sensitivity(self):
        api = self.component()
        api["inputs"]["request_dimensions"]["requests_per_period"] = None
        self.scenario["traffic_multiplier"] = "0"
        api["pricing"]["rates"] = dict.fromkeys(api["pricing"]["rates"], "0")
        self.assertIsNone(self.row()["quantities"]["max_attempts"])
        self.assertIsNone(self.row()["metered_list_cost"])

    def test_explicit_zero_usage_has_zero_metered_cost_without_a_rate(self):
        api = self.component()
        api["inputs"]["request_dimensions"]["requests_per_period"] = 0
        api["pricing"]["rates"] = dict.fromkeys(api["pricing"]["rates"], None)
        self.assertEqual(self.row()["metered_list_cost"], "0")
        api["pricing"]["currency"] = None
        self.assertIsNone(self.row()["metered_list_cost"])

    def test_cache_ineligible_uses_full_input_and_unknown_eligibility_stays_unknown(self):
        self.component()["inputs"]["cache_eligible"] = False
        row = self.row()
        self.assertEqual(row["quantities"]["uncached_input_tokens"], "2000000")
        self.assertEqual(row["quantities"]["cached_input_tokens"], "0")
        self.assertEqual(row["metered_list_cost"], "28/5")
        self.component()["inputs"]["cache_eligible"] = None
        self.assertEqual(self.row()["quantities"]["input_tokens_total"], "2000000")
        self.assertIsNone(self.row()["metered_list_cost"])

    def test_cache_cannot_exceed_total_input(self):
        self.component()["inputs"]["cached_input_tokens_per_attempt"] = 1001
        with self.assertRaisesRegex(ValueError, "subset"):
            self.result()

    def test_batch_price_needs_eligibility_and_does_not_reduce_token_count(self):
        pricing = self.component()["pricing"]
        pricing.update(billing_mode="batch", mode_eligible=None)
        self.assertIsNone(self.row()["metered_list_cost"])
        pricing["mode_eligible"] = True
        pricing["rates"]["output_tokens"] = "2"
        self.assertEqual(self.row()["quantities"]["output_tokens"], "400000")
        self.assertEqual(self.row()["metered_list_cost"], "18/5")

    def test_integer_counts_reject_boolean_float_and_negative_aliases(self):
        for invalid in (True, False, 1.0, "2", -1):
            with self.subTest(invalid=invalid):
                self.component()["inputs"]["max_attempts_per_request"] = invalid
                with self.assertRaises(ValueError):
                    self.result()

    def test_rates_reject_nonfinite_sign_whitespace_and_numeric_aliases(self):
        for invalid in (True, 0, 0.5, "NaN", "Infinity", "-1", " 1", "1 ", "1e3", "01"):
            with self.subTest(invalid=invalid):
                self.component()["pricing"]["rates"]["output_tokens"] = invalid
                with self.assertRaises(ValueError):
                    self.result()

    def test_input_parser_rejects_duplicate_keys_floats_and_nonfinite_tokens(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            for raw in ('{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}', '{"x":1.0}', '{"x":1e999}'):
                with self.subTest(raw=raw):
                    path.write_text(raw)
                    with self.assertRaises(ValueError):
                        MODEL.load(path)
            path.write_text('{"x":"0.10","unknown":null}')
            self.assertEqual(MODEL.load(path), {"x": "0.10", "unknown": None})

    def test_unknown_and_zero_throughput_cannot_create_free_accelerator_hours(self):
        inputs = self.component("synthetic-accelerator")["inputs"]
        inputs["units_per_second"] = None
        self.assertIsNone(self.row("synthetic-accelerator")["quantities"]["accelerator_hours"])
        inputs["units_per_second"] = "0"
        with self.assertRaisesRegex(ValueError, "sign/zero"):
            self.result()

    def test_explicit_duration_is_an_alternative_to_throughput(self):
        inputs = self.component("synthetic-accelerator")["inputs"]
        inputs.update(timing_mode="duration", seconds_per_job="7200", work_units_per_job=None, units_per_second=None)
        self.assertEqual(self.row("synthetic-accelerator")["quantities"]["accelerator_hours"], "16")
        inputs["units_per_second"] = "2"
        with self.assertRaisesRegex(ValueError, "unused throughput"):
            self.result()

    def test_fractional_discrete_jobs_are_rejected_instead_of_rounded(self):
        self.component()["inputs"]["request_dimensions"]["requests_per_period"] = 1001
        self.scenario["traffic_multiplier"] = "0.5"
        with self.assertRaisesRegex(ValueError, "whole logical"):
            self.result()

    def test_embedding_retry_ceiling_cannot_make_fractional_logical_items_valid(self):
        inputs = self.component("synthetic-demo-embedding")["inputs"]
        inputs.update(items=1, max_attempts_per_item=2)
        self.scenario["traffic_multiplier"] = "0.5"
        with self.assertRaisesRegex(ValueError, "whole embedding items"):
            self.result()
        inputs["items"] = 2
        quantities = self.row("synthetic-demo-embedding")["quantities"]
        self.assertEqual(quantities["max_attempts"], "2")
        self.assertEqual(quantities["embedding_tokens"], "200")
        inputs["items"] = None
        quantities = self.row("synthetic-demo-embedding")["quantities"]
        self.assertIsNone(quantities["max_attempts"])
        self.assertIsNone(quantities["embedding_tokens"])

    def test_quota_windows_and_memory_limits_are_separate_admission_constraints(self):
        row = self.row()
        self.assertEqual(row["limits"]["requests"]["status"], "exceeds")
        self.assertEqual(row["limits"]["tokens"]["status"], "within")
        self.component()["limits"]["period_matches"] = False
        self.assertEqual(self.row()["limits"]["requests"]["status"], "unknown")
        self.component("synthetic-accelerator")["limits"]["values"]["available_memory_gib"] = "8"
        gpu = self.row("synthetic-accelerator")
        self.assertEqual(gpu["limits"]["available_memory_gib"]["status"], "exceeds")
        self.assertEqual(gpu["quantities"]["accelerator_hours"], "2")

    def test_face_value_useful_coverage_and_avoided_cash_are_never_equated(self):
        support = self.row()["support"]
        self.assertEqual(support["face_value"], {"currency": "USD", "amount": "10"})
        self.assertEqual(support["potential_useful_coverage"], "2")
        self.assertEqual(support["uncovered_list_exposure"], "12/5")
        self.assertIsNone(support["gross_avoided_cash"])
        self.assertIsNone(support["net_avoided_cash"])
        self.component()["support"]["before_expiry_spend_limit"] = None
        self.assertIsNone(self.row()["support"]["potential_useful_coverage"])

    def test_ineligibility_and_expiry_zero_have_scoped_zero_coverage(self):
        self.component()["support"]["eligible"] = False
        self.assertEqual(self.row()["support"]["potential_useful_coverage"], "0")
        self.component()["support"].update(eligible=True, before_expiry_spend_limit="0")
        self.assertEqual(self.row()["support"]["potential_useful_coverage"], "0")

    def test_mixed_currencies_stay_separate_and_credit_fx_is_not_invented(self):
        self.component("synthetic-accelerator")["pricing"]["currency"] = "EUR"
        self.assertEqual(self.result()["by_class"]["research"]["complete_metered_totals"], {"EUR": "5", "USD": "22/5"})
        self.component()["support"]["currency"] = "EUR"
        self.assertIsNone(self.row()["support"]["potential_useful_coverage"])

    def test_avoided_cash_needs_completed_activated_evidence_and_preserves_net_loss(self):
        api = self.component()
        api["realization"] = {"currency":"USD", "completed":True, "evidence_kind":"synthetic",
                              "necessary_counterfactual_cash":"5", "actual_covered_cash":"1.5",
                              "incremental_cash":"3", "source_refs":["SYN"], "note":"Synthetic actual-style control only."}
        self.assertIsNone(self.row()["support"]["gross_avoided_cash"])
        api["support"]["activated"] = True
        support = self.row()["support"]
        self.assertEqual(support["gross_avoided_cash"], "3/2")
        self.assertEqual(support["net_avoided_cash"], "-3/2")
        self.assertEqual(support["realization_evidence_kind"], "synthetic")
        api["realization"]["completed"] = None
        self.assertIsNone(self.row()["support"]["gross_avoided_cash"])

    def test_actual_covered_value_cannot_exceed_retained_support_caps(self):
        self.component()["realization"] = {"currency":"USD", "completed":True, "evidence_kind":"synthetic",
            "necessary_counterfactual_cash":"100", "actual_covered_cash":"99", "incremental_cash":"0",
            "source_refs":["SYN"], "note":"Contradictory control must fail."}
        with self.assertRaisesRegex(ValueError, "support caps"):
            self.result()

    def test_duplicate_ids_and_shared_scope_aliases_cannot_double_count(self):
        extra = copy.deepcopy(self.component())
        self.scenario["workloads"][0]["components"].append(extra)
        with self.assertRaisesRegex(ValueError, "duplicate component"):
            self.result()
        extra["id"] = "different-name"
        extra["scope_key"] = " SYNTHETIC-API "
        with self.assertRaisesRegex(ValueError, "physical billing scope"):
            self.result()

    def test_mismatched_needs_and_missing_provenance_fail_closed(self):
        self.scenario["workloads"][0]["need_id"] = "N01"
        with self.assertRaisesRegex(ValueError, "need/scope"):
            self.result()
        self.scenario["workloads"][0]["need_id"] = "N06"
        self.component()["pricing"]["source_refs"] = []
        with self.assertRaisesRegex(ValueError, "provenance"):
            self.result()

    def test_incomplete_inventory_has_known_subtotals_but_no_complete_total(self):
        self.scenario["resource_inventory_complete"] = False
        group = self.result()["by_class"]["research"]
        self.assertEqual(group["known_metered_subtotals"], {"USD": "47/5"})
        self.assertIsNone(group["complete_metered_totals"])

    def test_cash_handoff_uses_separate_quotes_and_excludes_hosting_ci_and_demo(self):
        self.admit_mock_cash_inputs()
        handoff = self.result()["budget_handoff"]
        self.assertEqual(handoff["research_monthly_metered_cost_cents"], 940)
        self.assertEqual(handoff["research_monthly_cash_cost_cents"], 750)
        self.component()["cash_quote"] = None
        self.assertIsNone(self.result()["budget_handoff"]["research_monthly_cash_cost_cents"])
        self.assertEqual(self.result()["budget_handoff"]["research_monthly_metered_cost_cents"], 940)

    def test_partial_quote_mixed_currency_or_study_cannot_be_monthly_cash(self):
        self.admit_mock_cash_inputs()
        quote = self.component()["cash_quote"]
        quote["complete_for_period"] = None
        self.assertIsNone(self.result()["budget_handoff"]["research_monthly_cash_cost_cents"])
        quote.update(complete_for_period=True, currency="EUR")
        self.assertIsNone(self.result()["budget_handoff"]["research_monthly_cash_cost_cents"])
        quote["currency"] = "USD"
        self.scenario["period"]["unit"] = "study"
        self.assertIsNone(self.result()["budget_handoff"]["research_monthly_cash_cost_cents"])
        self.scenario["period"].update(unit="month", count=2)
        self.assertIsNone(self.result()["budget_handoff"]["research_monthly_cash_cost_cents"])

    def test_usd_rounding_is_half_up_per_component_not_binary_or_aggregate(self):
        self.admit_mock_cash_inputs()
        self.component()["cash_quote"]["amount"] = "0.005"
        self.component("synthetic-accelerator")["cash_quote"]["amount"] = "0.005"
        self.assertEqual(self.result()["budget_handoff"]["research_monthly_cash_cost_cents"], 2)
        self.component()["cash_quote"]["amount"] = "0.004"
        self.assertEqual(self.result()["budget_handoff"]["research_monthly_cash_cost_cents"], 1)

    def test_exact_input_field_sets_reject_silent_unit_typos(self):
        self.component("synthetic-ci")["inputs"]["hours_per_job"] = "5"
        with self.assertRaisesRegex(ValueError, "exact fields"):
            self.result()

    def test_period_dates_are_real_and_ordered_without_inventing_unknown_dates(self):
        self.scenario["period"].update(start="2026-02-30", end=None)
        with self.assertRaises(ValueError):
            self.result()
        self.scenario["period"].update(start="2026-03-01", end="2026-02-28")
        with self.assertRaisesRegex(ValueError, "precedes"):
            self.result()
        self.scenario["period"].update(start="2026-03-01", end=None)
        self.assertIsNone(self.result()["period"]["end"])


if __name__ == "__main__":
    unittest.main()
