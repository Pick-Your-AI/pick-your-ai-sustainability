# Offline support-comparison controls

Refs [issue #50](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/50).
This harness implements the two-dimensional comparison in
[the accepted comparison method, section 6](../../research/compute/usable-support-ranking.md).
It does **not** supply the actual workload, applicant, quota, rate, rights, or
independent findings acceptance needed to complete that issue.

## Reproduce without services

Use the repository's Python 3.12 environment:

```sh
python -m unittest discover -s tests -p test_support_comparison.py -v
python scripts/support_comparison.py --demo
```

The CLI accepts only an explicit `--demo`. It prints four fictional cases; it
has no account, token, input-file, output-file, URL or provider option and does
not contact services or mutate repository data. The synthetic currency `XCU`
is just a label, not an exchange rate or actual award.

| Case | Coverage A / B | Incremental implementation cash A / B | Result |
| --- | --- | --- | --- |
| Low demand | 20 / 20 | 5 / 15 | A dominates on these two dimensions |
| Base demand | 20 / 70 | 5 / 15 | Tradeoff; no total ordering |
| Earlier B expiry | 20 / 10 | 5 / 15 | A dominates on these two dimensions |
| Unknown B schedule | 20 / Unknown | 5 / 15 | Indeterminate |

## Pure comparison API and evidence boundary

`compare(left, right, common_conditions=...)` consumes two dictionaries with
exact fields: `context`, `gates`, `potential_useful_coverage`, and
`incremental_implementation_cash`. Context has `task`, `period`, `currency`
(three uppercase letters), and `evidence_kind`. The evidence kinds match the
[existing demand calculator](../../scripts/compute_demand.py): `unknown`,
`proposal`, `planning_estimate`, `measured`, or `synthetic`.

The function accepts the calculator's **exact rational string output** for
potential coverage (for example `1/3`) and a **separately evidenced** incremental
implementation-cash amount. It does not duplicate demand/pricing/cap arithmetic,
convert currencies, infer cash from a credit, or calculate realized avoided
cash. Both amounts must be nonnegative bounded integer/decimal/rational strings
or `null` (at most 4096 characters, including any fraction separator, to
accommodate exact calculator output longer than 100 characters). Floats,
booleans, signs, exponents, zero denominators and whitespace
are rejected. Unknown inputs are never replaced with zero.

Each offer must explicitly provide boolean-or-null gates for `eligibility`,
`permitted_use`, `resource_fit`, `schedule_fit`, `financial_stop`, and
`independence`. False gates produce `excluded`, not a victory for the other
route. Unknown gates block comparison. Contexts must be known and identical,
including evidence kind; there is no comparison of synthetic and measured
inputs. Callers must also explicitly affirm common task, quality, rights and
other relevant conditions. Omission is indeterminate, not implicit approval.

Gate values and evidence labels are **caller assertions**, not verified facts.
Matching labels do not establish real equivalence, professional acceptance or
authority. The result is always labeled `arithmetic_only` and preserves
`actual_avoided_cash: null`. `equivalent_on_two_dimensions` is not equivalent
scientific quality or a recommendation. No scalar coverage-minus-cash score,
provider ranking, opportunity stage or real support value is emitted.

Malformed input raises `ValueError` without echoing input contents. Valid but
unknown inputs return an explicit indeterminate result. Inputs are not mutated.
The existing opportunity, pipeline, freshness and budget registers and their
schemas remain untouched. This does not resolve any publication safety hold.

## Review and integration gates

Run the full existing suite and repository validator before integration:

```sh
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

A passing test suite proves these local arithmetic and fail-closed controls,
not actual eligibility, pricing, paid-provider behavior or research acceptance.
Independent review, exact-head required CI and ordinary protected-branch merge
remain necessary. Issue #50 stays blocked until its actual evidence and #48
receiving requirements are met.
