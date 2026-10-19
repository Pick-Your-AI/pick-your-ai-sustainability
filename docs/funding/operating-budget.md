# Twelve-month operating budget

Issue [#20 / E02-02](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/20) · Prepared **2026-10-19** · **Draft findings for independent acceptance**.

The [canonical budget](../../data/budget/operating-budget.json) is a populated,
recalculable planning model for all six repositories. It consumes the accepted
[#19 needs baseline](needs-assessment.md), delivered at
[`2c06977b`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/commit/2c06977bdb59ec1fdf687e3e177c12dcc8a62cce).
It records twelve relative months for lean, expected and stress sensitivities,
the available dated hosting inputs, and explicit nulls for every unmeasured
material cost. A complete operating total cannot be inferred from the known
hosting subtotal. The start month, actual entity, financial roles, balances,
spending authority and support received remain Unknown.

The recommendation is to accept this **P1 foundational planning method and its
bounded findings**, then populate the missing inputs from the canonical cost,
demand and legal-route work before representing an adopted budget or funding
request. A numeric opportunity score is Not applicable. This internal planning
tool has no provider intake, award deadline or benefit activation. Candidate
host and filing routes have their own qualification processes; their actual
project dates and outcomes remain Unknown.

## What the initial scenarios actually establish

| Scenario | Variable-cost sensitivity | N01 hosting choice | Known monthly subtotal | Known annual subtotal | Complete annual cost |
| --- | --- | --- | ---: | ---: | --- |
| Lean | 0.5 × a future qualified base CI/research cash estimate | Dated planned configuration | USD 112.70 | USD 1,352.40 | Unknown |
| Expected | 1 × the same future base estimate | Dated planned configuration | USD 112.70 | USD 1,352.40 | Unknown |
| Stress | 2 × the same future base estimate | Alternative design ceiling for that scope | USD 200.00 | USD 2,400.00 | Unknown |

The factors are editable **sensitivity hypotheses**, with no empirical demand
calibration, assigned probability, contributor commitment or adopted forecast.
“Expected” is a scenario name. Unknown base usage cost stays Unknown after any
multiplier, including zero. Fixed costs are not halved merely because the lean
scenario has a lower workload factor. A forecast already adjusted by #21 must
not be scaled a second time.

The [pinned leaderboard engineering plan](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/blob/73715b4850fc0df4a2afbdd877ad2b2644f1d769/docs/hosting-architecture.md)
supplies the only currently priced operating scope: two VMs at USD 24, two
databases at USD 15.15, a backup allocation of 30% of VM cost and a provisional
USD 20 export allocation, per month. Thus `48 + 30.30 + 14.40 + 20 = 112.70`.
This covers staging and production together. The USD 200 all-in ceiling replaces
all four components plus N01 usage, monitoring, taxes, temporary restore overlap
and contingency in stress. Those additional charges remain an explicit unknown
`hosting_extras` input in planned profiles; their separate line is zero in stress
solely because the ceiling already includes that scope. Non-N01 taxes remain
separate in every scenario. The ceiling is never an additional expense or a
hard cap on a later invoice. A quote exceeding it needs a revised engineering
allocation; the stress label does not establish a measured worst case. These are dated
engineering allocations, with an actual quote, billing scope and invoice still
needed. The initial [assumption worksheet](../budget-assumptions.md) remains
historical input and is not charged again.

## Cost coverage and exclusivity

Each input has one stable ID, an exclusive scope, the accepted need IDs it
serves, an evidence class and source references. The calculator requires all
thirteen cost scopes exactly once and refuses duplicate IDs/scopes or a second
N01 hosting envelope. A reviewer must still detect semantic overlap in a quote;
a program cannot prove that two differently described services are distinct.

| Cost input | Accepted need | Required evidence before a non-synthetic value |
| --- | --- | --- |
| Planned-hosting extras | N01 only | Usage, monitoring, taxes and temporary restore overlap excluded from the four planned components; already included in the all-in ceiling |
| Website/domain | N02 | Existing invoice/term, renewal, payer and incremental need |
| Incremental CI/storage | N03 | Priced usage beyond applicable existing no-cost capabilities; exclude N01/N06 |
| Research compute | N06 | Exact #21 source revision, monthly USD-cent field and workload/rate/scope mapping |
| Evidence/licensing | N07 | Accepted source or publishing need and actual usage rights |
| Shared mobile equipment | N04/N05 | One asset/loan/support inventory and finite device coverage; shared items counted once |
| Security/accessibility services | N08 | Finite accepted professional-review scope and estimate |
| Project coordination | N09 | Actual prospective contracted need; no invented person, hours or commitment |
| Route administration extras | N09 | Only services excluded from the selected host's included administration |
| Other taxes | N02–N09 | Jurisdiction, tax base and amounts excluded from other gross quotes; N01 taxes must use hosting extras |
| Processor fees | N09 | Incoming/outgoing method, currency and country; exclude host administration |
| Migration/exit | Applicable needs | One incremental portability/return scope, excluding N01 exports/restore overlap and asset costs already included |
| Other independent formation | N09 | State/local/setup and preparation costs excluding the selected federal application fee |

All initial amounts in this table are **null**. A one-time cost with a known
month appears only there. With a known month and unknown amount, only that month
is unknown; with unknown timing, the calculator cannot assign the cost to the
twelve-month horizon. It never invents a purchase or filing date. An explicit
known zero is allowed only with a declared evidence class; the supplied zero
controls are synthetic tests, not statements about the project's expenses.

[#21 owns the compute-demand model](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/21#issuecomment-6263808333).
The [integration handoff](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/21#issuecomment-6267557657)
requests its exact revision and field/unit/scope mapping. This calculator does
not duplicate token, throughput, GPU-hour, rate or credit-coverage conversion.
Admission requires a forty-character hexadecimal source revision and nonblank
mapping text; booleans, numbers, containers and whitespace are rejected. This
checks the record's shape. A reviewer must inspect the pinned source to confirm
the named fields, units, time horizon, currency and scope actually support the
estimate; a string alone cannot establish that evidence.
Its compute cells stay unset until that output is qualified. The accepted
ledger is sufficient to review a model with explicit missing inputs; missing
usage evidence prevents a complete budget, not publication of the planning tool.

## Legal-route counterfactuals

`parameters.selected_legal_path` is initially null. Choosing a path in a private
scenario copy is a hypothesis and does not change the actual entity or record a
host relationship. Only one route can be selected at a time.

| Family and selectable path | Conditional fee input | Project-specific boundary |
| --- | --- | --- |
| Present community: `community` | No host or federal filing line within this counterfactual | Account authority, administrative capacity, taxes and all actual eligibility remain Unknown |
| Fiscal host: `osc` | Published 10% of external funds entering the hosted project | Acceptance and actual fee base unverified; OSC's legal route remains distinct from independent charitable recognition |
| Fiscal sponsor: `sfc` | Published 10% of revenue Conservancy processes | Software-freedom, licensing, community/maturity and negotiated agreement remain separate gates |
| Fiscal sponsor: `spi` | Published 5% of donated amounts, with attributable transaction costs separate | Current SPI-specific HOWTO supplies this input; actual project terms remain unverified |
| Independent candidate: `independent_1023` | 2026 federal application fee USD 600 once, if scheduled | Actual form selection, eligibility, entity, filing date, other costs and recognition Unknown |
| Independent candidate: `independent_1023_ez` | 2026 federal application fee USD 275 once, if scheduled | Full eligibility worksheet required; not an automatic route for this project |

The [OSC fee page](https://docs.oscollective.org/welcome-and-introduction-to-osc/fees.md)
also distinguishes third-party processing from its host fee and states there
are no additional OSC setup, minimum-balance or recurring fees. Do not create a
second charge for included host services. OSC [identifies itself](https://oscollective.org/about/)
as a 501(c)(6) fiscal host; this is distinct from charitable 501(c)(3) recognition.
The [SFC application page](https://sfconservancy.org/projects/apply/)
describes rolling initial inquiry followed by review and agreement negotiation;
hosting facilitates fundraising and does not provide an award. The
[SPI service terms](https://www.spi-inc.org/projects/services/) require documented,
approved expenses and normally an SPI officer's contract signature. Typical
accounting is covered, while extraordinary project-specific costs may need a
separate estimate. SPI's own current [association HOWTO](https://www.spi-inc.org/projects/associated-project-howto/)
states that joining/remaining associated has no fee and that 5% of donated
amounts is deducted for overhead; attributable transaction costs are separate.

The federal alternatives come from **Revenue Procedure 2026-5, Appendix A** in
the [official 2026 bulletin](https://www.irs.gov/irb/2026-01_IRB), reached through
the [current IRS fee index](https://www.irs.gov/charities-non-profits/user-fees-for-tax-exempt-and-government-entities-division).
The [Form 1023-EZ instructions](https://www.irs.gov/instructions/i1023ez), revised
January 2025, require its eligibility worksheet. The fees exclude state/local
filings and professional preparation and must be rechecked before a filing or
later-year budget. Full and streamlined fees are mutually exclusive.

This is a parameterized financial comparison, not completion of
[#14 host suitability](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/14)
or the legal formation/recognition work. The present community, a hosted project
and an independently recognized organization retain separate actual eligibility
assessments, all Unknown here. There is no actual filing, application, charitable
deductibility, acceptance or awarded support implied by selecting a scenario.

## Cash, support, controls and independence

The five monthly funding measures remain separate: external unrestricted cash
receipts, external restricted cash receipts, contingent cash awards, credit
face value and evidenced avoided cost. Each has its own strict annual sum.
An award notice is not a receipt; restricted cash is not freely spendable cash;
a credit is not a refund or income. Avoided cost needs a qualified necessary
workload, eligible actual coverage and evidence of the purchase it displaced.
None of the last three measures is added to cash, used as an expense offset or
included in an available-cash figure. Actual available cash remains null.

The separate `host_fee_inputs.monthly_base_cents` records the qualifying fee
base under the selected host's actual scope: OSC's external incoming funds,
SFC's processed revenue or SPI's donated amount. It requires its own evidence
class and nonblank scope mapping, starts null, and is never added to funding
receipts. Total cash, balances, internal transfers, awards and credits cannot
silently substitute for that base. A known host rate applies to the explicit
base; an unknown rate or base prevents a complete fee estimate. The monthly
rounding convention is a planning approximation, not a reconstruction of the
host's per-transaction ledger. Confirm actual transaction rounding, restrictions
and fee allocation before treating a projected expense as chargeable to funds.

OSC's application-linked [public agreement](https://docs.google.com/document/u/1/d/e/2PACX-1vQbiyK2Fe0jLdh4vb9BfHY4bJ1LCo4Qvy0jg9P29ZkiC8y_vKJ_1fNgIbV0p6UdvbcT8Ql1gVto8bf9/pub),
Exhibit A, instead describes 10% of all deposited funds regardless of source.
This differs from the operational fee page's internal-transfer exclusion. The
external-incoming base is a conditional planning hypothesis; neither source is
silently declared controlling for an actual PYA agreement. Written reconciliation
belongs in the host inquiry before adopting that fee base.

Contingency and liquidity reserves are separate optional policies, both unset.
Contingency is a proposed allowance on a complete monthly expense total, excluding
the all-in N01 ceiling when selected because that ceiling already includes its
own contingency. The explicit `contingency_base_cents` exposes that exclusion;
the embedded N01 allowance is not assigned an invented amount. The additional
allowance is reported separately before the combined planning requirement. A liquidity
reserve is a **cash stock** based on a selected number of average recurring-cost
months. One-time equipment and application/formation costs are excluded from
that recurring base. The stock is not charged every month, added to income or
presented as money already held. An accountant/authorized owner must determine
the actual tax, restricted-fund, gross-versus-net, reserve and fee treatment.

| Condition | Budget consequence and unresolved evidence |
| --- | --- |
| Restricted use and reporting | Preserve award/host restrictions, fee allocation and actual reporting dates separately; no deadline is fabricated |
| Branding and publication rights | No support receipt grants editorial control or publication permission; preserve canonical source/IP and sponsor-neutrality decisions |
| Privacy and evidence retention | Publish aggregate, redacted provenance; private account/bank/donor records stay out of this repository |
| Portability and assets | Price an actual exit/return scope and inspect host asset-transfer restrictions; do not treat held or loaned assets as unrestricted cash |
| Renewal, expiry and overage | Record actual terms, quotas, billing cadence and post-credit continuity before valuing support; no default free renewal or hard spending cap |
| Independence and operating effort | Keep service/custodian/signatory roles and real maintenance hours explicit; no invented contributor commitment or sponsor influence over findings |

These controls consume the accepted [financial-control procedure](../operations/financial-controls-draft.md)
and [authorization workflow](../workflow-and-authorization.md). The budget itself
does not approve spending, sign a contract or assign a person to a standing role.

## Reproduce and change a scenario

The [calculator](../../scripts/operating_budget.py) uses Python's standard library
and performs no network, provider, model or account operations. Money inputs are
nonnegative integer **USD cents**; basis points are integer fractions of 10,000.
Do not mix currencies or substitute a headline credit value for a cash cost.
It rounds nonnegative rational amounts to the nearest cent, with exact halves
upward, at each line and month. Annual values sum those monthly results.

From the repository root:

```sh
python scripts/operating_budget.py --check
python scripts/operating_budget.py
python -m unittest discover -s tests -p test_operating_budget.py -v
```

The first command verifies the committed derived snapshot, including numeric
types. The second prints the calculated scenarios without changing inputs.
For a hypothetical case, copy the JSON to a private working file, change only
documented parameters/costs with explicit provenance, and run:

```sh
python scripts/operating_budget.py --input /tmp/my-budget-case.json --write
python scripts/operating_budget.py --input /tmp/my-budget-case.json --check
```

`--write` recalculates the `calculated` section in that supplied file. It does not
approve the inputs. The tests independently cover the supplied subtotal,
half-cent rounding, single-count equipment/filings, alternative hosting/routes,
restricted-fund and support separation, missing costs/timing/rates, reserve
stock, duplicate scopes, bool/float aliases and #21 provenance requirements.
The ordinary repository suite also runs these tests, so stale derived outputs
fail the existing configured check without a new workflow.

## Source status, review and remaining decisions

The JSON `sources` array records every inspected primary source, exact project
revision, date, evidence class and finding. The hosting plan and initial
worksheet are historical engineering inputs; neither is a refreshed vendor
quote. The IRS bulletin is the current 2026 fee procedure, while its linked
instructions have their own revision date. The first attempted IRS fee URL with
an extra `charitable-organizations` path failed; the successful official index
above and its actual linked bulletin supplied the fee findings. Unrelated
search results were ignored. The initial services-only inspection left SPI's
percentage unverified; the subsequent current SPI HOWTO supplied direct 5%
donation-overhead evidence. This is improved source coverage, not a claim that
the provider changed its fees. SFC's comparative SPI quote is not the fee basis.

The remaining facts are exact invoices/assets/account entitlements; qualified
base demand from #21; selected route, form and timing; actual fees/taxes and
excluded costs; restricted-fund conditions; and an authorized choice of reserve,
contingency and sensitivity assumptions. The model does not estimate unknown
effort or attach a fabricated numerical support value. Its concrete benefit is
a reproducible funding baseline tied to N01–N09, with visible missing inputs and
no duplicate technical implementation or duplicate provider opportunity record.

| #20 acceptance criterion | Reviewable evidence |
| --- | --- |
| Assumptions versus actuals; Unknown inputs unset | Separate evidence classes, `actuals`, null parameters and complete totals |
| Cash, contingent awards and avoided cost separate | Five independent monthly/annual funding measures; no available-cash inference |
| No arbitrary contributors or authorization | Unassigned roles and null actual spending; selected route is a hypothesis |
| Monthly/annual reproduction and no double counting | Exact-cent calculator, committed 3 × 12 outputs, exclusive scopes and regression controls |
| Current primary sources and dates/history/failures | Pinned source array and source-status qualifications above |
| Program/intake/deadline or reasoned N/A | Internal planning method N/A; candidate route processes and actual dates distinguished |
| Benefit and three legal routes | Internal planning use and separate community/hosted/independent counterfactuals |
| Restrictions and operating conditions | Cash/control table, source rights, host terms and unknown operating inputs |
| Concrete public-benefit use, value and effort | N01–N09 receiving scopes, explicit arithmetic, Unknown complete value/hours |
| Canonical delivery, references, questions, priority/disposition | Canonical JSON, calculator, this guide, P1 recommendation and explicit downstream handoffs |
| Independent actual findings acceptance | Pending exact-revision review; local tests alone do not establish it |
