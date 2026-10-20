# Compute and API demand model

Issue [#21 / E02-03](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/21) · Prepared **2026-10-20** · P1 foundational planning method.

The [canonical model](../../data/budget/compute-demand-model.json) and
[offline calculator](../../scripts/compute_demand.py) turn explicit workload
assumptions into separately typed API, accelerator, CI, storage and egress
quantities. They retain provider list value, potentially useful support,
separately sourced payable cash quotes and evidenced avoided cash as different
measures. Unknown inputs stay Unknown. The output is a planning contract, not a
measurement of project traffic, an adopted budget or permission to run a study.

The concrete purpose is to size a finite, reproducible request for resources
against the accepted [N01–N09 needs ledger](needs-assessment.md), provide the
missing research-only interface to the accepted [#20 budget](operating-budget.md),
and let #48/#49/#50 compare proposed resource routes without adding advertised
credits to available cash. This issue owns the model; implementation, physical
device work and empirical measurements remain in their existing repositories.

## What the five initial scenarios establish

| Scenario ID | Evidence and horizon | Reproducible result | Remaining unknowns |
| --- | --- | --- | --- |
| `unmeasured-current` | Accepted requirement inventory; one relative month, with no selected calendar dates | Separate research, product hosting, CI/testing and public demonstration rows; every material measured quantity and complete cost remains null | Actual traffic, tokens, throughput, resource inventory, account rights, quotas, rates, taxes, payable quotes and support |
| `evaluation-proposal-49` | Dated, unaccepted and unexecuted #49 handoff; one study | Per route: 12 families × 2 wordings × 2 instruction packages × 3 repetitions = **144 logical slots**. At most two total attempts per slot = **288 attempts per route**, **576 across the two proposed route ceilings** | Route admission, models, token maxima, account limits, per-attempt time, prices and resource authorization |
| `synthetic-low` | Invented control, 0.5× traffic | Research reference cost **USD 4.70**, with all other classes separate | No project estimate or provider offer is established |
| `synthetic-base` | Invented control, 1× traffic | Research reference cost **USD 9.40**; independent invented payable quotes total USD 7.50 but cannot enter the real budget handoff | No project estimate or provider offer is established |
| `synthetic-high` | Invented control, 2× traffic | Research reference cost **USD 18.80**, with unchanged explicit storage footprint/duration | No project estimate or provider offer is established |

The controls are arithmetic examples, with no assigned probability or claim
that “base” is expected demand. They do not describe a provider's current prices.
The current project scenario is incomplete, and every initial monthly cash
handoff is null. All three synthetic scenarios remain excluded from that
handoff even though their reference costs can be calculated.

The [#49 handoff](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/21#issuecomment-6277987585)
reports frozen proposal `b6450a387e8f6d5c1c598aa3e2e7f8c362efa773`. This model
consumes only its explicitly stated cardinalities and retry bound. It does not
claim acceptance or inspect/execute the proposed study. A transport-only retry
is a second actual attempt, not another scored logical slot. The upper bound
charges a full per-attempt token envelope to every possible retry, rather than
assuming failed attempts are free. An expected-value forecast would require a
separate measured retry distribution and actual billing terms.

## Workload identity, scope and horizon

Every scenario has one declared period (`month`, `study` or `run`), a positive
period count, optional valid ordered calendar dates, explicit evidence and a
resource-inventory completeness flag. A study is not silently divided into
monthly cost, and a two-month aggregate is not an admitted one-month input.
Null dates remain null. A calendar date alone does not prove a service deadline
or establish when an unapproved study will occur.

Each workload has a stable ID and one class. Components have separate stable
IDs and physical billing scope keys. Duplicate IDs or case/whitespace aliases
of a scope key within one scenario are rejected. Alternative scenarios may
reuse the same IDs because they are alternatives, never concurrent totals.
The reviewer must still detect semantic overlaps that use different names.

| Workload class | Accepted need and receiving boundary |
| --- | --- |
| `research` | N06 empirical model/resource research; the only class eligible for the #20 research-compute handoff |
| `product_hosting` | N01 service resources; quantitative demand does not add a second charge to the existing N01 hosting envelope |
| `ci_testing` | N03 CI and evidence retention; keep standard entitlement, incremental paid usage, runner minutes and wall time distinct |
| `public_demonstration` | A distinct N06-related demonstration purpose; excluded from research-compute handoff, even if it uses the same model/provider |

Shared hardware, one CI invocation or one stored artifact belongs to one
physical scope. Allocate an evidenced share once or retain the shared scope
separately; do not copy its full cost into multiple workload rows. N01's existing
planned hosting allocations and its alternative all-in ceiling remain in #20.
No amount in the current demand model is added to those allocations.

## Exact units and calculations

Count inputs are nonnegative JSON integers, with booleans rejected. Attempt
ceilings and accelerator counts must be positive when known. Rates and
continuous quantities are exact nonnegative decimal **strings**, such as
`"0.10"`; null means Unknown. The reader rejects duplicate keys, JSON floats,
nonfinite values, numeric aliases, signs and ambiguous decimal spellings.
Exact field sets reject mistakes such as supplying hours to a minutes field.

All arithmetic uses rational numbers, and output quantities/amounts are rational
strings: `"3/2"` means exactly 1.5 in the field's stated unit. It is not a string
to add lexically or a binary floating-point approximation. A receiver can parse
it with Python's standard-library `Fraction`. Rates and source values are not
rounded during the calculations. Different currencies are grouped separately;
there is no exchange-rate conversion or combined money total.

| Component | Quantity formula and rate basis |
| --- | --- |
| `api` | Logical requests = product of explicit request-dimension counts × traffic multiplier. Maximum attempts = logical requests × maximum total attempts per request. Token quantities multiply each per-attempt bound by that maximum. Rates are currency units **per 1,000,000 tokens**, independently for uncached input, cached input and output. |
| `embedding` | Items × maximum total attempts per item × traffic multiplier × tokens per item. Rate is currency units **per 1,000,000 embedding tokens**; these are not generation/output tokens. |
| `accelerator` | Jobs × seconds per job × accelerators per job ÷ 3,600. Rate is currency units **per accelerator-hour**. Seconds per job is either supplied directly or work units per job ÷ measured/hypothesized units per second, never both. |
| `ci` | Jobs × minutes per job × traffic multiplier. Rate is currency units per **runner-minute** for the explicitly selected runner class. Concurrency affects wall time and admission, not this aggregate minute count. |
| `storage` | GiB footprint × explicit duration in months. Rate is currency units per **GiB-month**. Traffic multiplier does not silently change storage footprint or retention. |
| `egress` | GiB × traffic multiplier. Rate is currency units per **GiB transferred**. Bytes/GiB conversion, free allowances and region-specific billing require their own qualified input. |

For accelerator throughput, `units_per_second` describes the **whole timed job
using the stated accelerator count**, not a per-device rate multiplied again.
`work_unit` must identify the measured unit and workload. Minimum memory and
available memory are per accelerator; adding device VRAM does not establish
that a model fits one device. The model does not derive VRAM from parameter
count, infer throughput from advertised hardware or claim scheduler feasibility.
Hardware/runtime/model/context/cache/concurrency evidence remains with the
canonical technical research.

A missing quantity stays missing even with a zero rate or traffic multiplier.
An explicitly known zero quantity can have zero metered cost at an unknown
rate, within the named usage-only scope; missing currency or billing eligibility
still prevents a qualified monetary total. This does not assert that an account
has no fixed charges. Unknown throughput is not infinite throughput, zero
accelerator use or a free workload. A sensitivity producing fractional requests
or jobs is rejected so the author must choose and justify a discrete count.

### Caching, batching, quotas and substitution

Cached tokens are a **subset** of total input tokens. Cached input cannot exceed
total input, and both cannot be charged again as independent full input totals.
When cache eligibility is false, all input uses the uncached rate. When it is
unknown and caching could matter, the metered cost remains Unknown. A cache hit
must use actual eligible token boundaries; a guessed percentage is an explicit
hypothesis, not an observed provider cache result.

Batching selects an independently sourced rate/mode and requires explicit
eligibility. It does not automatically reduce tokens, logical requests or
accelerator time. Change workload/timing inputs only when a finite measured or
clearly hypothetical batching model supports the change. Record batch latency,
job deadlines, queue and data-retention limits before adopting that route.

Capacity checks compare the same demand unit and period with the explicitly
mapped cap. API token caps here use **input plus output**; a provider's different
quota definition needs a qualified mapping. A per-minute or per-day quota
cannot be substituted for a study/month cap: `period_matches` remains null/false
until the mapping is established. Unknown demand or cap yields `unknown`;
excess yields `exceeds`, not silently truncated demand. Burst/concurrency,
per-request context, minimum memory and actual execution admission can still
block a plan whose period-level arithmetic fits.

Provider substitution must preserve or explicitly revise the admitted model,
tokenizer, output envelope, workload, latency, memory, throughput, evaluation
meaning, account rights and rate period. A cheaper headline rate alone does not
prove substitutability, equivalent findings or sufficient resource coverage.

## Reference value, useful support and actual cash

`metered_list_cost` is a reference calculation at the supplied rates. A complete
resource inventory with complete rate/eligibility/currency inputs yields
`complete_metered_totals` **by class and currency**. An incomplete inventory has
only explicitly labeled known subtotals, even if every represented row is
priced. Neither is an invoice or available cash.

Support is a separate record. Its face value retains its own currency. Potential
useful coverage is the minimum of reference cost, face value, an evidenced
eligible-spend cap and an evidenced pre-expiry-spend cap, only when eligibility
and the same currency are established. The caps require a traceable derivation
from the actual products, quota windows, available capacity, workload schedule,
expiry and account terms. The synthetic caps are explicitly invented controls;
they are not derived from a real provider contract. A missing cap stays Unknown.
Ineligibility or an explicit zero pre-expiry cap can establish zero coverage
within this defined scope. Cross-currency coverage remains Unknown.

Potential coverage does not require activation and therefore is not a received
benefit. `uncovered_list_exposure` is the remaining reference-priced exposure,
not a cash invoice or authorized overage. An alert, model cap or positive credit
balance is not an account-enforced spending limit. Taxes, regions, uncredited
products, capacity gaps, support, transfer, migration and post-credit renewal
can remain uncovered. Retain their unknown costs and a feasible stop/exit plan.

Realized avoided cash requires a distinct, sourced completed record, actual
activation/eligibility, matching currency and all three amounts: necessary
counterfactual purchase, actual covered cash expenditure and incremental cash
costs. Covered expenditure cannot exceed the retained support caps. Gross
avoided cash is the smaller of necessary counterfactual cash and actual covered
cash; net effect subtracts the incremental cost and may be **negative**.
Unknown amounts or completion/activation leave the result Unknown. A synthetic
realization control is labeled synthetic in its output, never an actual project
receipt. No such realized record is asserted in the canonical initial data.

An independent payable `cash_quote` is separately supplied for each billing
scope and period. It needs its own evidence class, currency, complete-period
coverage, amount and source references, including the actual treatment of
discounts, support, fees, taxes and excluded charges. A list calculation or
nominal credit is never silently substituted for that quote. Evidence labels
and nonempty references establish input shape, not the truth of a quote; an
independent reviewer must inspect the linked scope and actual source.

## Exact downstream contract

Select an actual scenario by `id`, then retain its array index when recording
JSON pointers. Alternative sensitivities must not be added together. The initial
`unmeasured-current` scenario is index 0; the following paths use `s` as the
chosen scenario index and `c` as a component index.

| Consumer | Output pointer and required mapping |
| --- | --- |
| #49 finite evaluation proposal | `/calculated/scenarios/1/components/0/quantities/logical_requests` = `144`; `/max_attempts` = `288` within that same quantities object. Component 1 has the second route ceiling. Preserve study scope, maximum-attempt semantics and the unaccepted/unexecuted source attribution. |
| API sizing in #48/#49/#50 | `/calculated/scenarios/s/components/c/quantities` exposes total input, cached/uncached input, output or embedding tokens separately; no model/tokenizer/price is selected by this interface. |
| Accelerator sizing | The same quantities object provides `accelerator_hours`, `minimum_memory_gib` and the exact time basis; source runtime/model/hardware/measurement protocol must accompany a non-synthetic value. |
| Quota/expiry admission | Each component's `/limits` and `/support` retain the exact mapped cap, period and Unknown/exceeds result. Useful coverage is a bounded hypothesis, not an account entitlement or receipt. |
| #20 metered reference comparison | `/calculated/scenarios/s/budget_handoff/research_monthly_metered_cost_cents` is the separately labeled N06 research-only reference price. **Do not insert it into a cash cell.** |
| #20 payable planning input | `/calculated/scenarios/s/budget_handoff/research_monthly_cash_cost_cents` uses only separately sourced complete payable quotes for one relative month, USD currency, a complete resource inventory and nonsynthetic planning/measured evidence. Every initial value is null. |

The USD export rounds each nonnegative component to integer cents, exact halves
upward, then sums components. It does not round a floating-point aggregate.
Other currencies retain exact rational amounts and cannot enter #20's USD cells.
The research-only export excludes N01 hosting, N03 CI and demonstrations even
when their own values are known. A partial/missing cash quote, mixed currency,
synthetic/proposal class, incomplete inventory, study/run horizon or multiple
months prevents the monthly cash export.

Before entering any future value into #20, record the **actual accepted #21
commit** in `compute_handoff.source_revision` and the exact output pointer,
scenario/horizon, currency, original rates/quotes and exclusive scope mapping
in `compute_handoff.field_and_scope_mapping`. Reconcile every monthly research
cell to the qualified quote/usage evidence. A one-month value is not automatically
repeated twelve times. Preserve #20's evidence class and its unfilled actuals.
If the demand has already been sensitivity-adjusted here, do not apply #20's
variable-cost multiplier a second time. The accepted budget is unchanged by
this delivery, and its current research-compute cells remain unset.

## Sources, legal routes and operating restrictions

The canonical `sources` array records primary project URLs, review date,
classification and findings. `research.input_pins` retains the byte lengths,
Git blobs and SHA256 values of the accepted needs, budget and budget-interface
script at exact main `7cae962c58c02e7f28b45f38193668897adbc1e4`.
The earlier #19 acceptance and current #20 contract are distinguished from the
historical, unaccepted #49 proposal and invented numeric controls. No live
provider prices or refreshed program terms are claimed, and no access failure
has been converted to evidence of availability. The original grant-source
leads in #21 remain separate provider research; they are not rates for this model.

Provider intake, application and a funding deadline are **Not applicable** to
this internal planning-method deliverable. Actual resource/account/contract
dates remain Unknown. The present community has unverified applicant, account
and billing authority; a sponsored project needs its actual host agreement and
account/credit permissions; an independent 501(c)(3) needs actual recognition
and separately qualified program terms. None of these routes is established by
choosing a scenario or observing a public repository.

Restrictions on eligible workloads, private data, branding, reporting,
publication, portability, renewal, overage and organizational independence
must be recorded from actual terms before valuing or using support. Retain
sponsor-neutral findings and original source rights. Do not place private
credentials, billing records, donor information, participant data or payloads
in this public model. Use qualified redacted aggregate evidence and its actual
custody path when inputs later become available. Future resource, billing,
review and finance roles remain Unassigned; this implementation does not appoint
an operator or make an external commitment.

## Reproduce and review

From the repository root with Python 3.12:

```sh
python scripts/compute_demand.py --check
python scripts/compute_demand.py
python -m unittest discover -s tests -p test_compute_demand.py -v
```

`--check` compares the exact committed calculation, including JSON types.
The default action prints output without changing inputs. To explore a scenario,
copy the canonical file, change explicit inputs and provenance, then run:

```sh
python scripts/compute_demand.py --input /tmp/demand-scenario.json --write
python scripts/compute_demand.py --input /tmp/demand-scenario.json --check
```

`--write` changes only that supplied file's `calculated` section. These commands
perform no network, provider/account, model download, GPU workload or experiment
operation. The normal existing test workflow discovers the new test module;
no workflow or dependency change is needed. Tests include independent literal
arithmetic and counterexamples for unit scaling, scope duplication, Unknowns,
rates/currencies, cache/batch eligibility, retry ceilings, throughput, memory,
quota-window mismatch, support caps, actual-versus-potential coverage and
separately sourced cash. Test-only admission labels stay inside isolated copies.

An independent reviewer should recompute the complete initial scenarios,
compare every copied source/interface and evaluate all limitations, rather
than treat successful validation as findings acceptance. The actual reviewed
revision, test originals, CI and accepted-main delivery must be linked in #21
as those distinct events occur.

| #21 criterion | Concrete evidence in this deliverable |
| --- | --- |
| Independent workload classes and traceable assumptions | Four named classes, unique billing scopes, source IDs/pins, explicit horizons and separate unknown/proposal/synthetic evidence |
| API and accelerator units never conflated | Six typed component formulas; per-million token and per-accelerator-hour rate bases; independent literal arithmetic controls |
| List value, useful coverage and genuine avoided cost separate | Distinct reference price, face/capped potential support, complete payable quote and completed realization records |
| Unknown throughput or traffic never called measured demand | Null current inputs, explicit evidence kinds, no zero coercion, unexecuted proposal and synthetic controls labeled throughout |
| Primary sources, dates and historical/access qualifications | Immutable accepted project sources, dated #49 handoff, original input pins and no invented live-provider verification |
| Program/intake/deadline or reasoned N/A | Internal method has no provider intake; actual account, proposal and support dates remain Unknown |
| Benefit type and three applicant routes | Internal public-benefit planning purpose and separate community/sponsored/independent route gates |
| Restrictions and operating conditions | Explicit quota/expiry/privacy/rights/renewal/overage/portability and independence boundaries; no active resource or standing-role claim |
| Concrete use, defensible value/effort and cash distinction | Exact #20/#48/#49/#50 contracts, reproducible rational arithmetic, unknown real value/effort and distinct reference/cash measures |
| Canonical delivery, sources, questions, priority and disposition | Canonical JSON, calculator, focused tests, this guide, P1 rationale and explicit missing-input/admission questions |
| Independent acceptance of actual findings | Actual independent source/arithmetic review and delivery must be linked in #21; the model alone cannot self-approve its findings |
