"""Synthetic-only controls for #50; no provider or project qualification."""

import copy
from fractions import Fraction
import importlib.util
import itertools
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/support_comparison.py"
SPEC = importlib.util.spec_from_file_location("support_comparison", SCRIPT)
MODEL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODEL)


def option(coverage="20", cash="5"):
    return {
        "context": {
            "task": "synthetic-task", "period": "synthetic-period",
            "currency": "XCU", "evidence_kind": "synthetic",
        },
        "gates": {name: True for name in MODEL.GATES},
        "potential_useful_coverage": coverage,
        "incremental_implementation_cash": cash,
    }


def compare(left, right, **kwargs):
    kwargs.setdefault("common_conditions", True)
    return MODEL.compare(left, right, **kwargs)


class SupportComparisonTests(unittest.TestCase):
    def test_four_published_synthetic_cases(self):
        cases = MODEL.synthetic_demo()["cases"]
        expected = [
            ("low", "20", "20", "left_dominates"),
            ("base", "20", "70", "tradeoff"),
            ("earlier-expiry", "20", "10", "left_dominates"),
            ("unknown-schedule", "20", None, "indeterminate"),
        ]
        self.assertEqual(len(cases), len(expected))
        for case, (name, left, right, relation) in zip(cases, expected):
            with self.subTest(name=name):
                self.assertEqual(case["case"], name)
                self.assertEqual(case["left_coverage"], left)
                self.assertEqual(case["right_coverage"], right)
                self.assertEqual(case["left_cash"], "5")
                self.assertEqual(case["right_cash"], "15")
                self.assertEqual(case["comparison"]["relation"], relation)

    def test_no_coverage_minus_cash_score(self):
        result = compare(option("20", "5"), option("70", "15"))
        self.assertEqual(result["relation"], "tradeoff")
        for key in ("score", "rank", "winner", "net_support"):
            self.assertNotIn(key, result)
        self.assertIsNone(result["actual_avoided_cash"])

    def test_equal_coordinates_are_only_equivalent_on_two_dimensions(self):
        result = compare(option(), option())
        self.assertEqual(result["relation"], "equivalent_on_two_dimensions")
        self.assertEqual(result["evidence_level"], "arithmetic_only")

    def test_false_gate_excludes_even_zero_coverage(self):
        for side, gate in itertools.product((0, 1), MODEL.GATES):
            with self.subTest(side=side, gate=gate):
                values = [option("0", "0"), option("0", "0")]
                values[side]["gates"][gate] = False
                self.assertEqual(compare(*values)["relation"], "excluded")

    def test_unknown_gate_never_passes(self):
        for side, gate in itertools.product((0, 1), MODEL.GATES):
            with self.subTest(side=side, gate=gate):
                values = [option(), option()]
                values[side]["gates"][gate] = None
                self.assertEqual(compare(*values)["relation"], "indeterminate")

    def test_failed_gate_takes_priority_over_unknown_gate(self):
        left, right = option(), option()
        left["gates"][MODEL.GATES[0]] = None
        right["gates"][MODEL.GATES[1]] = False
        self.assertEqual(compare(left, right)["relation"], "excluded")

    def test_common_conditions_must_be_explicit(self):
        self.assertEqual(MODEL.compare(option(), option())["relation"], "indeterminate")
        self.assertEqual(compare(option(), option(), common_conditions=False)["relation"],
                         "incomparable")
        for invalid in (0, 1, "true", [], {}):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                compare(option(), option(), common_conditions=invalid)

    def test_unknown_context_blocks_even_when_equal(self):
        for key in ("task", "period", "currency", "evidence_kind"):
            with self.subTest(key=key):
                left, right = option(), option()
                left["context"][key] = right["context"][key] = None
                self.assertEqual(compare(left, right)["relation"], "indeterminate")
        left, right = option(), option()
        left["context"]["evidence_kind"] = right["context"]["evidence_kind"] = "unknown"
        self.assertEqual(compare(left, right)["relation"], "indeterminate")

    def test_unlike_contexts_never_compare(self):
        changes = {"task": "other-task", "period": "other-period", "currency": "USD",
                   "evidence_kind": "measured"}
        for key, value in changes.items():
            with self.subTest(key=key):
                right = option()
                right["context"][key] = value
                self.assertEqual(compare(option(), right)["relation"], "incomparable")

    def test_each_unknown_amount_remains_unknown_including_zero(self):
        for side, field in itertools.product((0, 1), MODEL.AMOUNTS):
            with self.subTest(side=side, field=field):
                values = [option("0", "0"), option("0", "0")]
                values[side][field] = None
                self.assertEqual(compare(*values)["relation"], "indeterminate")

    def test_exact_rational_and_decimal_inputs(self):
        self.assertEqual(compare(option("1/3", "0.10"), option("0.33", "1/10"))
                         ["relation"], "left_dominates")
        self.assertEqual(compare(option("2/6", "0.10"), option("1/3", "1/10"))
                         ["relation"], "equivalent_on_two_dimensions")

    def test_no_binary_float_rounding(self):
        self.assertEqual(compare(option("9007199254740993"), option("9007199254740992"))
                         ["relation"], "left_dominates")
        left = "0." + "0" * 80 + "2"
        right = "0." + "0" * 80 + "1"
        self.assertEqual(compare(option(left), option(right))["relation"], "left_dominates")

    def test_invalid_amounts_fail_instead_of_becoming_unknown(self):
        invalid = [False, True, 0, 1.0, float("inf"), float("nan"), "", "-1", "+1",
                   "1e3", "NaN", "Infinity", "1/0", "01", "1/02", ".5", "1.",
                   " 1", "1 ", "1\n", "1_000", "1//2", "1" * (MODEL.MAX_EXACT_STRING_LENGTH + 1), [], {}]
        for field, value in itertools.product(MODEL.AMOUNTS, invalid):
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                left = option()
                left[field] = value
                compare(left, option())

    def test_invalid_input_is_rejected_even_if_gate_failed(self):
        left = option("NaN")
        left["gates"][MODEL.GATES[0]] = False
        with self.assertRaises(ValueError):
            compare(left, option())

    def test_exact_top_level_and_nested_fields_required(self):
        for where in (None, "context", "gates"):
            for mode in ("missing", "extra"):
                with self.subTest(where=where, mode=mode), self.assertRaises(ValueError):
                    left = option()
                    target = left if where is None else left[where]
                    if mode == "missing":
                        del target[next(iter(target))]
                    else:
                        target["unexpected"] = "not-an-input"
                    compare(left, option())

    def test_invalid_gates_rejected_not_truthiness_coerced(self):
        for value in (0, 1, "false", "true", [], {}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                left = option()
                left["gates"][MODEL.GATES[0]] = value
                compare(left, option())

    def test_invalid_context_and_mappings_rejected(self):
        for key, value in (("task", ""), ("task", "a\nb"), ("period", " month"),
                           ("currency", "usd"), ("currency", "USD\n"),
                           ("evidence_kind", "approved"), ("task", 5)):
            with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                left = option()
                left["context"][key] = value
                compare(left, option())
        for value in (None, [], "input", 1):
            with self.subTest(value=value), self.assertRaises(ValueError):
                compare(value, option())

    def test_amount_upper_bound_and_zero_fraction(self):
        self.assertEqual(compare(option("1" * 100), option("1" * 99))["relation"],
                         "left_dominates")
        self.assertEqual(compare(option("1" * 101), option("1" * 100))["relation"],
                         "left_dominates")
        self.assertEqual(compare(option("1" * MODEL.MAX_EXACT_STRING_LENGTH), option("1"))["relation"],
                         "left_dominates")
        self.assertEqual(compare(option("0/7", "0"), option("0", "0.0"))["relation"],
                         "equivalent_on_two_dimensions")

    def test_symmetry_over_synthetic_grid(self):
        inverse = {"left_dominates": "right_dominates", "right_dominates": "left_dominates",
                   "tradeoff": "tradeoff", "equivalent_on_two_dimensions":
                   "equivalent_on_two_dimensions"}
        for a, b, c, d in itertools.product(("0", "1/3", "1", "2"), repeat=4):
            left, right = option(a, b), option(c, d)
            first = compare(left, right)["relation"]
            self.assertEqual(compare(right, left)["relation"], inverse[first])
            if first == "left_dominates":
                self.assertGreaterEqual(Fraction(a), Fraction(c))
                self.assertLessEqual(Fraction(b), Fraction(d))
                self.assertNotEqual((Fraction(a), Fraction(b)), (Fraction(c), Fraction(d)))

    def test_dominance_is_transitive_on_synthetic_grid(self):
        options = [option(str(a), str(b)) for a, b in itertools.product(range(3), repeat=2)]
        for left, middle, right in itertools.product(options, repeat=3):
            if (compare(left, middle)["relation"] == "left_dominates" and
                    compare(middle, right)["relation"] == "left_dominates"):
                self.assertEqual(compare(left, right)["relation"], "left_dominates")

    def test_inputs_unchanged(self):
        left, right = option(), option("70", "15")
        before = copy.deepcopy((left, right))
        compare(left, right)
        self.assertEqual((left, right), before)

    def test_demo_uses_no_network(self):
        with mock.patch.object(socket, "socket", side_effect=AssertionError("network forbidden")):
            result = MODEL.synthetic_demo()
        self.assertEqual(result["evidence_level"], "synthetic_arithmetic")
        for case in result["cases"]:
            self.assertIsNone(case["comparison"]["actual_avoided_cash"])

    def test_cli_only_runs_explicit_demo_without_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, str(SCRIPT), "--demo"],
                                    cwd=directory, capture_output=True, text=True, timeout=10,
                                    env={"PYTHONDONTWRITEBYTECODE": "1"})
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout), MODEL.synthetic_demo())
            self.assertEqual(list(Path(directory).iterdir()), [])
            for args in ([], ["--d"], ["--input", "not-a-real-file"]):
                rejected = subprocess.run([sys.executable, str(SCRIPT), *args],
                                          cwd=directory, capture_output=True, text=True, timeout=10,
                                          env={"PYTHONDONTWRITEBYTECODE": "1"})
                self.assertEqual(rejected.returncode, 2)
                self.assertEqual(rejected.stdout, "")

    def test_long_exact_calculator_output(self):
        # Source integration: use the real calculator from the full checkout.
        # No synthetic output is treated as a project price or realized cash.
        calculator_script = ROOT / "scripts/compute_demand.py"
        spec = importlib.util.spec_from_file_location("compute_demand", calculator_script)
        calculator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(calculator)

        decimal = "1." + "0" * 49 + "1"
        sources = {"synthetic-source"}
        quantity = calculator.quantities({
            "id": "synthetic-ci", "kind": "ci",
            "inputs": {"jobs": 1, "minutes_per_job": decimal},
        }, Fraction(1))
        currency, cost, _ = calculator.price({
            "kind": "ci", "pricing": {
                "currency": "USD", "billing_mode": "standard",
                "mode_eligible": True, "rates": {"ci_minutes": decimal},
                "source_refs": ["synthetic-source"],
            },
        }, quantity, sources)
        support = calculator.support({
            "support": {
                "currency": "USD", "face_value": "10", "eligible": True,
                "activated": False, "eligible_spend_limit": "10",
                "before_expiry_spend_limit": "10",
                "source_refs": ["synthetic-source"], "note": "Synthetic only",
            }, "realization": None,
        }, cost, currency, sources)
        value = support["potential_useful_coverage"]
        self.assertGreater(len(value), 100)
        self.assertEqual(value, str(cost))
        self.assertEqual(compare(option(value, "0"), option("1", "0"))["relation"],
                         "left_dominates")

    def test_abbreviated_demo_switch_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = subprocess.run([sys.executable, str(SCRIPT), "--d"], cwd=directory,
                               capture_output=True, text=True, timeout=10,
                               env={"PYTHONDONTWRITEBYTECODE": "1"})
            self.assertEqual(p.returncode, 2)
            self.assertEqual(p.stdout, "")
            self.assertEqual(list(Path(directory).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
