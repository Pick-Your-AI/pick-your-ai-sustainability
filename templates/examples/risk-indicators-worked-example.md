# Worked risk-indicator cases — synthetic, not project exposure

These cases exercise the [method](../../docs/risk-indicators.md) and
[register](../risk-register.md). **Every donor, receipt, workload, contract,
amount, date, observation and scenario below is synthetic.** They represent no
actual award, applicant status, financial position, provider commitment, accepted
risk appetite or hardware/runtime result. Identifiers prefixed `SYN-` belong only
to these examples and are not external evidence locators.

The purpose is to make denominator, coverage and authority mistakes observable.
The examples specify expected results for independent arithmetic and method
review; their publication is not approval of a real risk record.

## A. Cash, commitments, resources and custody

Synthetic scope: one recipient, gross cash received during
`[2026-01-01T00:00:00Z, 2026-02-01T00:00:00Z)`, complete receipt inventory and
known distinct funding groups. There is no FX policy.

| Synthetic input | Category | Quantity | Treatment |
| --- | --- | ---: | --- |
| SYN-R1, group A | Received cash | USD 600 | Eligible USD flow. |
| SYN-R2, group B | Received cash | USD 400 | Eligible USD flow. |
| SYN-C1, group A | Outstanding conditional commitment | USD 500 | Separate commitment observation; not received cash. |
| SYN-K1, provider C | Published maximum credit face value | USD 6,000 | Neither cash nor proven usable resources or realized avoided cost. |
| SYN-L1, provider D | Quoted purchase value of loaned equipment | USD 800 | Not cash or owned equipment; actual custody/return obligations need separate review. |
| SYN-R3, group E | Received cash | EUR 50 | Separate EUR population; no conversion into USD. |

The complete USD received-flow denominator is `600 + 400 = USD 1,000`. Its
largest group contributes USD 600, so the exact concentration is `600/1000 =
3/5 = 60%`. The independently complete EUR population has `50/50 = 1 = 100%`.
Those are two separate observations, not an average or combined-currency result.
Neither percentage is labelled acceptable or unacceptable.

The amount `600 + 400 + 500 + 6000 + 800 = 8300` is a deliberately **invalid
cross-category sum** and is not reported as support or concentration. No avoided
cost is calculated: the example has no actual consumption, suitable alternative,
eligible rate or counterfactual-spending evidence.

If SYN-R1 is paid through intermediary F on behalf of ultimate funder A, retain
F and A as separate identity fields on the same receipt. The denominator remains
USD 1,000, not USD 1,600. An intermediary view and an ultimate-source view can each
be calculated only with the evidence needed for that view. If A's identity is
unavailable, the ultimate-source concentration becomes Unknown even though the
cash quantity is known. Do not guess that F and A are independent donors.

If the two initially distinct groups are later proved to share a relevant funding
source under the declared grouping rule, create a new dated observation with
`1000/1000 = 100%` and preserve the original 60% observation with its earlier
grouping assumption. Until the grouping dispute is resolved, the whole-group
concentration is Unknown.

## B. Missing, zero, negative and incomplete inputs

Each row is a separate synthetic observation, not a mutation of actual evidence.

| Case | Inputs and coverage | Expected result |
| --- | --- | --- |
| SYN-B1 incomplete amount | One known USD 600 receipt; a second eligible receipt exists but its amount is unavailable. One of two amounts is known. | **Unknown** whole-population concentration. Known subtotal USD 600 and amount coverage `1/2` stay visible. Do not report `600/600 = 100%` as the population result or presume the missing amount is zero. |
| SYN-B2 unknown population | One known USD 600 receipt, but no evidence the receipt list is complete. | **Unknown**; expected population and coverage denominator are also Unknown. A known row count cannot bound unseen receipts. |
| SYN-B3 complete empty flow | Complete independent evidence establishes no received cash in the declared interval. | **Not applicable — complete zero received-flow denominator**. No division and no 0% result. Other dependence indicators remain applicable. |
| SYN-B4 missing ledger | No receipt list or completeness evidence is available. | **Unknown**, not the complete-empty case. |
| SYN-B5 negative gross receipt | A row proposes USD −20 as a gross receipt without changing the declared category. | **Invalid input**. Preserve the row and request its proper refund/return classification; do not subtract it or silently remove it from a population. |
| SYN-B6 unit mismatch | USD 600 and EUR 400 are proposed as one denominator without an accepted conversion method. | **Invalid input** for that combined calculation; retain separate currency observations. |
| SYN-B7 conflicting source | Two retained documents claim USD 400 and USD 450 for the same receipt, with no accepted correction. | **Unknown** dependent concentration. Preserve both sources and the receipt identity; do not choose the amount that improves the ratio. |

These states concern the calculation, not the seriousness of the exposure. In
particular, “Not applicable cash concentration” can coexist with severe in-kind
dependence or no viable operating resource.

## C. Essential workload dependence and unserved need

Synthetic scope: a complete accepted list of three equally counted essential
workloads. “Viable” below is an explicit synthetic fact for this example, not an
assessment of any real provider or resource.

| Workload | Evidenced viable provider alternatives | Classification |
| --- | --- | --- |
| SYN-W1, reproducible validation | P | Exactly one. |
| SYN-W2, public documentation | Q and R, independently qualified for the same requirements | Multiple. |
| SYN-W3, bounded model evaluation | None | Unserved. |

Single-provider dependence is `1/3` of workloads; unserved need is separately
`1/3`; multiple-provider coverage is `1/3`. Retain the fractions. If displaying
two decimal places, each is approximately 33.33%, a rounded display only.
No combined “two thirds safe” claim follows. The metric does not weight workload
importance, compute hours or cash value.

Now suppose SYN-W3's classification is unavailable. The entire dependence ratio
is **Unknown**, with two of three workloads classified, one known single-provider
workload, one known multi-provider workload and one unresolved workload. It is
not `1/2` over the classified subset. If the list of essential workloads itself
is incomplete, the population denominator is Unknown as well.

If a fourth workload SYN-W4 also has only P, a separately complete four-workload
observation has `2/4 = 1/2` single-provider dependence and names P for both rows.
If Q and R are later found to require the same sole upstream resource, reassess
their independence rather than counting two commercial labels automatically.
Nominal credit dollars, GPU hours and token quotas cannot repair that evidence.

## D. Expiry and restricted balances

Synthetic expiry scope: three activated benefits, as of 2026-01-01T00:00:00Z;
the explicitly chosen half-open inspection horizon ends 2026-02-01T00:00:00Z and is not an
approved risk threshold or provider application deadline.

| Benefit | Contractual expiry in this synthetic scenario | Continuation |
| --- | --- | --- |
| SYN-E1 | 2026-01-15T00:00:00Z, inside horizon | Unresolved. |
| SYN-E2 | 2026-03-01T00:00:00Z, outside horizon | Unresolved. |
| SYN-E3 | Unknown | Unknown. |

Report **one confirmed expiring benefit with unresolved continuation**, two of
three expiry dates known, and one unknown-date row. The complete expiring share
is **Unknown**; `1/3` would imply the third benefit had been classified. If a
separately retained new observation establishes E3 expires outside the horizon
and resolves every required classification, that new observation can report
`1/3`. The original Unknown remains historical.

Boundary controls use separate synthetic records: an unresolved expiry exactly
at 2026-01-01T00:00:00Z is included, while one exactly at
2026-02-01T00:00:00Z is outside. An expiry immediately before the as-of instant
belongs to the separate already-expired list. No implicit date-only timezone
conversion changes those instants.

For a separate synthetic restricted-balance observation, suppose an accepted
accounting basis identifies USD 300 restricted cash within a complete USD 1,000
cash balance at a single as-of instant. Its share is `300/1000 = 3/10 = 30%`.
An additional USD 200 obligation is a separate obligation, not a reason to
replace the numerator with USD 500. Eligible use and available-to-spend amounts
still require their own evidence. If any balance's restriction is unclassified,
the share is Unknown. A complete zero cash balance is Not applicable.

## E. Action and authority records

The following are synthetic findings showing how to complete the register without
inventing a real assignee or exception authority. No action described here has
been performed.

| Field | SYN-RISK-1: publication veto | SYN-RISK-2: single-person operation |
| --- | --- | --- |
| Use case / observation | Public validation report; a synthetic proposed support clause requires sponsor approval before publishing unfavorable findings. | Critical operation SYN-OP1; an accepted synthetic primary exists, but no continuity arrangement is evidenced. |
| Evidence and material question | SYN-TERM-1, proposed clause; potential conflict with the declared independent-findings boundary. No numerical concentration result waives it. | SYN-ROSTER-1 and missing handoff/access evidence; availability of a runbook alone does not prove continuity. |
| Current control | Agreement unaccepted in this scenario. | Primary responsibility only; no tested handoff claimed. |
| Recommendation | Withhold support-acceptance recommendation pending the actual neutrality/authority disposition; no contract is rejected or signed by the template. | Record unresolved continuity and request an actually accepted continuity arrangement. |
| Concrete action | Obtain the exact proposed term and an independent clause-level decision; establish a compliant revised term or decline recommendation if the accepted policy requires it. | Identify an authorized willing alternate or service, arrange the necessary scoped access and verify the stated handoff procedure. |
| Decision authority role | Authorized neutrality-policy and agreement reviewer; actual mandate and person **Unknown / Unassigned**. | Authorized operations/account role; actual mandate and person **Unknown / Unassigned**. |
| Dependency | E01.08 accepted policy and E09.02 action authority; actual agreement and rights evidence. | Accepted critical-operation inventory, account permissions and the actual continuity acceptance. |
| Exit condition | Identified actual term and independent decision demonstrate the stated publication boundary is preserved, or an evidenced decline closes the intake finding without activating the benefit. | Accepted named arrangement, scoped access and observed handoff evidence satisfy the declared operation's continuity requirements. |
| Actual decision / action / review date | Pending / unperformed / not assigned. | Pending / unperformed / not assigned. |

For a complete synthetic three-operation inventory, suppose SYN-OP1 lacks
continuity, SYN-OP2 has neither primary nor continuity, and SYN-OP3 has both.
The distinct affected-operation numerator is two, not three: `2/3`. Keep the
separate counts of one missing primary and two missing continuity arrangements
without double-counting SYN-OP2 in the union. If any arrangement is unknown,
withhold the whole-population share and retain the known findings.

Portability and overage findings use the same action structure. For example,
unknown export permission cannot be replaced by an assumed migration cost, and
an alert cannot be described as a hard spend cap. A proposed engineering task
estimate of two hours would remain an estimate requiring its actual task basis;
this example supplies no such estimate or authority to activate a service.

## F. Review and reporting controls

Before a real register is accepted, the reviewer must check population and
grouping completeness, units and categories, source conflicts and permissions,
all mandatory risk topics, actual role mandates, actionable exit conditions and
the separate threshold/exception approval gate. Recompute the actual arithmetic
from the retained inputs; a successful repository validator cannot establish
these facts.

A later threshold proposal must state its evidence, scope, consequences,
alternatives, policy/budget dependencies and real authorized decision. No
threshold is proposed in these cases. Do not import any synthetic value, date,
identity or result into `data/opportunities.json`, the budget, an actual risk
dashboard or an application. The cases are evidence of a reviewable method,
with actual project scores and organizational facts still unavailable.
