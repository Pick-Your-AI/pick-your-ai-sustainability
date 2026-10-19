# Sustainability and independence risk indicators

Owner issue: E09.05. Status: draft definitions. No numerical risk appetite, financial commitment or donor relationship is adopted.

| Indicator | Definition | Unknown handling and decision |
| --- | --- | --- |
| Cash concentration | Largest source's received or separately committed cash / total cash in the same category, currency and period | Do not mix received and pledged amounts; no denominator means Unknown |
| Essential-resource dependence | Essential workloads with one viable resource provider / evidenced essential workloads | A missing needs inventory is Unknown, not zero dependence |
| Expiring support | Activated benefits with a confirmed expiry and unresolved continuation | Unverified dates remain visible outside the confirmed-expiry count |
| Restricted-fund exposure | Obligations and restricted cash tracked against eligible planned use | Scope and currency must match; accounting review sets treatment |
| Exit cost | Evidence-based effort, data export, replacement resource and transition cost | Unmeasured cost remains an estimate with assumptions |
| Sponsor influence | Terms affecting publication, ranking, compatibility, competing vendors or editorial control | A material restriction blocks acceptance pending independent disposition |
| Overage and renewal | Resource controls, actual limits and renewal authority | Credit face value alone does not establish controlled use |
| Ownership continuity | Critical operations without an accepted primary and continuity arrangement | A role description is not an assigned person |

Keep received cash, committed cash and realized avoided costs separate. Published maximum credit capacity is not realized support. Loaned hardware is not owned hardware. Count distinct programs and providers consistently; an intermediary and ultimate funding source must not silently count twice.

Each risk record names evidence, affected use case, exposure, current control, proposed mitigation, decision role, dependency, exit condition and review date. Record actual reviewers and accepted decisions only.

E01.08 owns the sponsor-neutrality policy; E02.02 owns the budget assumptions. Existing [monetization research](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/54) and [source-use research](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/60) remain canonical inputs. Their research completion does not certify a sponsor agreement, legal interpretation or production neutrality result.

## Methodology offered for independent acceptance — 2026-10-19

This dated section develops the complete original draft above, which remains
unchanged as history. It offers a reproducible indicator method, a
[risk-register template](../templates/risk-register.md) and
[worked synthetic cases](../templates/examples/risk-indicators-worked-example.md)
for [E09.05 / #71](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/71).
It does not populate actual project exposure, adopt a numerical risk appetite or
appoint organizational decision makers. Independent methodology acceptance and
normal reviewed delivery are still pending for this revision.

The concrete use case is to identify whether support for the existing public
research, builder clients, website, validation and resource-testing work could
make their operation or published findings dependent on a funding source. The
[needs assessment](needs-assessment.md) is an initial planning map, not a complete
accepted workload inventory. An apparent lack of recorded dependency therefore
cannot establish independence. This method supplies an accountable way to record
that gap before a support decision.

### 1. Declare the population before calculating

Every observation must declare all of the following:

| Field | Required meaning |
| --- | --- |
| Observation identity | Stable record ID, method revision, review date and exact retained input revision or document hash; a later correction creates a dated observation rather than replacing history. |
| Applicant and custodian | The actual recipient or operating entity, its route, and any fiscal custodian. Unknown status or authority remains explicit. Separate organizations' balances cannot silently become one denominator. |
| Time | A flow uses a stated half-open interval `[start, end)` and timezone; a stock uses a stated as-of instant. Source capture time, transaction time, contractual expiry and review time remain separate. |
| Unit and category | Currency, workload count, operation count, contract count, engineering hours or another stated native unit. Received cash, outstanding commitments, resource usage and realized avoided cost are different categories. |
| Eligibility rule | Explain which records belong to this population and why; retain excluded, disputed and unclassified rows with reasons. Select a consistent accounting or operational basis before comparing periods. |
| Grouping | Define the actual funding source or resource provider identity and document any common-control grouping. A payout intermediary and ultimate funder are different identity fields, not two receipts. Unresolved grouping can prevent a concentration conclusion. |
| Coverage | Record the expected population, examined records, known eligible records, unresolved rows and missing quantities. An observed subset is not a complete population merely because every examined row parsed. |
| Evidence | Identify the actual agreements, receipts, usage records, accepted needs, control settings or role decisions that support inclusion and quantity. Record source locator, version, review date, claim grade, permissions and material conflicts. |

Currency conversion requires a separately accepted rate source, date and method;
there is no implicit FX conversion. Distinct resource units cannot be added into
one usable-credit total. A provider's published maximum is a source claim, not
evidence of an award, activation, actual consumption or a controlled bill.

The existing [research method](research-methodology.md) separates primary facts,
publisher claims, estimates and unknowns. Retaining a hash establishes which
bytes were used, not their accuracy, completeness, rights or continuing effect.
Public records should retain safe evidence locators and permitted summaries;
private donor identities, contracts, credentials and banking information need
their own authorized storage and disclosure handling.

### 2. Result states and denominator rules

Use these states for each indicator, independently of any later risk decision:

| State | Use and required output |
| --- | --- |
| Calculated | The eligible population, grouping and required quantities are complete and consistent. Retain numerator, positive denominator, units, exact fraction and any explicitly rounded display. This is a measurement under a declared method, not an acceptable-risk badge. |
| Unknown | A required input, identity grouping, classification, quantity or denominator is unavailable or disputed. Retain known subtotals and coverage, but withhold the whole-population ratio. A known subtotal is not a lower-risk result. |
| Not applicable | Evidence establishes that this indicator has no eligible population in the stated scope, or a complete population has a zero denominator. State the reason and evidence; do not divide by zero or display zero percent. A different indicator can still expose a serious gap. |
| Invalid input | The proposed calculation contradicts its declared type, unit, category or scope, or uses impossible values such as a negative gross cash receipt. Preserve the rejected input and correction request. Do not silently drop it and recalculate a more favorable result. |

This refines the original draft's shorthand “no denominator means Unknown”:
missing or unverified is **Unknown**; an evidenced, complete zero is **Not
applicable**, with the reason visible. Neither state is a pass. Absence of a
register is not evidence of a complete zero population.

If two sources conflict, retain both and withhold any result that depends on
choosing between them until a qualified disposition resolves the conflict.
Explicit assumptions may support a separately labelled scenario; they do not
fill missing actual observations. Do not rank an incomplete observation against
a complete one as though coverage were equal. Comparisons also require compatible
scope, units, category, grouping and method revisions.

### 3. Indicator definitions

#### Cash donor concentration

For each recipient, currency and reporting interval, let `R(g)` be the sum of
evidenced **gross cash received** from funding-source group `g`. Let `D` be the
sum of those receipts over the complete eligible population. Report
`max(R(g)) / D` only when `D > 0` and the population and grouping are complete.
The unit is a share of received cash; retain each contributing cash amount.

This measures dependence of cash inflows, not available balance, recognized
income, net revenue or accounting treatment. Refunds, returns, fees and restricted
amounts must remain separately visible; a qualified accounting decision is
required before using a different financial measure. Do not infer usable funds
from this gross-flow ratio.

An optional **outstanding committed cash** observation uses a separately defined
as-of stock, enforceability/conditions, recipient, currency and eligible due
window. It excludes already received amounts from the outstanding amount and
never adds that stock to received flows. A pledge without evidence of its status
is unresolved. Credits, discounts, in-kind services and equipment loans never
enter either cash numerator or denominator.

Use one receipt identity once. If a fiscal sponsor transfers money from an
ultimate funder, retain both identities and show the chosen grouping basis.
Separate intermediary and ultimate-source views may be useful, but they are two
views of the same receipts. Missing ultimate-source evidence makes that view
Unknown; it does not authorize an invented relationship or duplicate amount.

#### Essential-resource dependence

Start with a versioned, accepted list of essential workloads for the reporting
scope. For each workload, identify independently evidenced viable provider
alternatives under the same actual requirements: capacity, account eligibility,
location, permissions, required interfaces, data handling and continuity.
Marketing availability or an advertised free quota alone does not prove viability.

Report the count of essential workloads with **exactly one** viable provider
divided by the complete eligible workload count. This is an unweighted share of
workloads, not a share of compute, budget or user impact. Keep the identities of
the sole providers; several sole-provider workloads may all depend on the same
provider. Common infrastructure or contractual dependence must not be mistaken
for independent alternatives.

Also report separate counts for **no viable provider**, multiple viable providers
and unknown classification. No viable provider is an unserved requirement, not
evidence of low dependence. An unknown workload or incomplete essential-needs
inventory withholds the overall share; it remains in the coverage statement.
If a capacity-weighted measure is later proposed, it needs its own accepted
weights, native units and complete input evidence. It cannot be inferred from
this count or from nominal credit dollars.

#### Expiring support and renewal uncertainty

For a stated as-of instant, identify the complete population of actually activated
benefits, separated by support type. Declare an inspection horizon explicitly;
choosing that horizon is a planning convention, not a contractual deadline or
an approved risk threshold. Use `[as_of, horizon_end)`, with the end later than
the as-of instant: an expiry exactly at the start is included, and one exactly
at the end is outside. Count benefits whose evidenced expiry falls within
that horizon and whose continuation is unresolved. Separately list already
expired benefits strictly before the as-of instant still supporting work,
benefits outside the horizon, unknown
expiry dates and unverified continuation terms.

The confirmed count remains useful when other dates are unknown, but it is not
the complete expiring population. A fraction uses the same activated-benefit
population only when every required date and continuation classification is
known. Application deadlines, credit expiration, contract renewal and hardware
return dates remain separate fields. A prior award, historical announcement or
usual annual cadence is not evidence of current renewal.

#### Restricted funds and obligations

An optional restricted-cash share uses evidenced restricted cash balance over
total cash balance at the same as-of instant, currency, recipient/custodian and
accepted accounting basis. It is a stock measure, separate from the received
cash concentration flow. Unclassified restrictions or balances make the share
Unknown; a complete zero cash balance is Not applicable.

Record outstanding obligations, eligible planned uses, dates and counterparties
beside that share, not as an extra amount in its denominator. Match each proposed
use to the actual restriction and the accepted budget. A restricted balance is
not proof the project can pay a particular bill. The missing E02.02 valuation and
budget decisions listed below remain gates; this method adopts no financial
recognition, restricted-fund accounting policy or amount.

#### Sponsor influence and organizational independence

Use a clause-level register, with categorical findings and actual evidence rather
than an invented numerical score. It must cover exclusivity, treatment of
competitors, ranking or compatibility influence, publication approval or veto,
benchmark disclosure, attribution/branding, intellectual-property or data terms,
privacy, audit/reporting duties and termination consequences.

The [charter](charter.md) and [ethics draft](sponsorship-ethics-draft.md) identify
independent findings and no purchased rankings as the proposed program boundary.
A proposed term that conflicts with that boundary is a reason to withhold the
support-acceptance recommendation and request a real independent disposition.
No aggregate concentration percentage can waive it. E01.08 still owns the final
neutrality policy and any actual exception process; this method supplies neither
an organization's signature nor a legal interpretation of a specific agreement.

#### Overage, renewal and uncontrolled obligation

For each activated or proposed benefit, record the actual billing account,
eligible services and usage units, verified spend controls, renewal mode, price
or quote basis, notice requirements, termination mechanism and authorized
decision maker. Distinguish an observed hard limit from an alert or a proposed
control; record the last verification and evidence of the setting.

An unknown price, cap, renewal term or permission is Unknown, not zero liability.
A finite credit balance does not establish a spending cap or authority to pay
overages. Missing control or authority blocks a recommendation to activate the
affected branch until the actual authorization workflow resolves it. This is an
intake decision, not an attempt to terminate or modify a live service.

#### Portability, custody and exit cost

Record the affected workload, export rights and format, retained data and
deletion obligations, transfer or return duties, alternative resource, transition
steps and restoration criteria. Loan custody, shipping, maintenance, insurance
and return conditions remain distinct from ownership and purchase value.

Estimate effort only from an identified task breakdown, measured or justified
unit rate, quantities and uncertainty; preserve engineering hours separately from
elapsed lead time and each currency amount. A replacement must meet the same
operational and rights requirements before it is called viable. Missing export
permission, replacement qualification or task data makes the relevant estimate
Unknown. Do not present an untested migration plan as demonstrated recoverability.

#### Single-person operational dependence

Start with the complete accepted inventory of critical operations and their
required access and continuity arrangements. Count operations lacking either
an actually accepted primary responsibility or an evidenced continuity
arrangement, divided by the complete operation count. Report missing-primary,
missing-continuity and unknown rows separately; an operation meeting both missing
conditions is counted once in the numerator.

An accepted arrangement names actual people or an authorized service, scope,
access, handoff and verification evidence. A job title, GitHub assignee, prepared
runbook or proposed backup does not prove availability or succession. An absent
operation inventory or unknown arrangements make the whole share Unknown.
Record the action and decision role without appointing an absent person.

### 4. Risk decisions, actions and exit evidence

There is no red/yellow/green threshold, combined risk score, numerical appetite,
minimum donor count or financial commitment in this method. The separate
[opportunity rubric](scoring-and-qualification.md) retains its own purpose and
eligibility gate; a foundation method has no manufactured opportunity score.

If a threshold is proposed later, its record must contain the exact indicator and
scope, complete supporting observations, uncertainty and coverage, the proposed
boundary and rationale, alternatives, likely decision consequences, dependency
on the accepted needs/budget/neutrality inputs, decision authority role and
evidence of an actual accepted mandate. Record a real review decision and its
effective scope before using it. A proposed threshold remains proposed even if
its arithmetic is valid. A reviewer of this method does not thereby approve a
future threshold or appoint its decision maker.

Every risk considered material in an actual review must have a stated reason,
affected use case, current control, proposed action, decision authority role,
actual assignee only if accepted, dependency, and falsifiable exit condition.
An action such as “diversify” is insufficient: identify the particular workload,
alternative qualification or permission evidence required to close the finding.
Unknown materiality stays unresolved instead of receiving a favorable color.

The [register](../templates/risk-register.md) separates observation, recommended
disposition, actual decision and completed action. Keep declined and resolved
records and their original evidence. A changed contract, provider, workload or
input revision requires a new observation and review of affected conclusions;
it does not silently refresh every prior result. Review dates or reminders must
be actually assigned, not inferred from an application cadence.

### 5. Current input and decision register

This table records gaps observed on 2026-10-19 at Sustainability
`015300e6834940d537c933de3490bb5d3a707cd8`. These are source and decision gaps,
not measured exposure scores. No row appoints a person or changes a native issue
edge. The explicit unresolved-input branch in criterion 6 allows this methodology
to be reviewed while the two prerequisite decisions remain open.

| Input / gap | Available evidence and limit | Action and decision authority role | Dependency and exit condition |
| --- | --- | --- | --- |
| E01.08 neutrality policy | The current ethics draft supplies review questions. The canonical `docs/policies/vendor-neutrality-and-sponsorship-ethics-draft.md` required by #18 is absent at this revision; no adopted exception or materiality policy is inferred. | Preserve clause-level concerns; the authorized neutrality-policy reviewer must decide actual policy and any permitted exception process. No individual is appointed here. | [#18](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/18); exit requires its accepted, identified policy and an actual affected-term disposition where needed. |
| E02.02 budget and valuation | `docs/budget-assumptions.md` is a partial planning worksheet. Its illustrative allocations are not current expenditure or a complete risk denominator; `data/budget/operating-budget.json` is absent at this revision. | Consume the existing budget owner's actual delivered output; the authorized budget/custody role must settle scope and valuation before financial exposure is calculated. | [#20 and its 12:15 owner checkpoint](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/20#issuecomment-6266988438); exit requires the accepted budget revision and the needed units, categories, quantities and authority. This method does not duplicate that calculator. |
| Complete essential-workload and resource qualification inputs | The initial needs map is useful context, not a complete accepted inventory or proof that an advertised resource can serve a workload. | Request the actual inventory and per-resource qualification from their existing owners; use Unknown until complete. | [#50](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/50) and the affected technical owners; exit requires identifiable workloads, operational requirements and evidenced alternatives. |
| Activated-benefit, cash and operating-authority evidence | This method has no actual complete receipt ledger, activated-benefit inventory, accepted critical-operation roster or agreement-specific authority record. | The custodian and operations decision roles must supply authorized evidence and review access; no cash amount, donor identity, activation or volunteer commitment is invented. | [#69](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/69), [authorization workflow](workflow-and-authorization.md) and the relevant account/financial owners; exit requires the specific complete population and actual decisions for the intended indicator. |

The register's recommended disposition is **accept the bounded methodology after
independent review; keep actual exposure and unresolved policy/valuation decisions
unscored**. P2 remains the issue's foundation priority: the method supports
independent public-benefit work before reliance grows. Effort and financial value
remain Unknown; no monetary value is needed to justify documenting this control.

### 6. Applicant routes, terms and program applicability

This is an internal operating-method deliverable, not a funding program or offer.
Its own benefit type, application process and provider deadline are **Not
applicable for that reason**. It creates no opportunity record in
`data/opportunities.json`; actual investigated programs must continue to use their
unique canonical record and source review. No application, receipt, award,
activation or reporting completion is claimed.

| Route | Required assessment before actual exposure or action |
| --- | --- |
| Present community | Identify the actual recipient, contracting/billing account, custody and accepted action authority. Those organizational facts remain unverified here; an open-source repository is not proof of a legal recipient or an authorized payment decision. |
| Fiscal-sponsored project | Separately establish the actual sponsor arrangement, restrictions, account control, retained responsibilities and ultimate-funder/intermediary mapping. No sponsor or agreement is assumed; do not merge its balances or authority into another route. |
| Independently recognized 501(c)(3) | Separately verify the actual entity/status and the specific program and action requirements. Recognition is not asserted, and would not by itself establish a particular offer, agreement, account permission or qualified resource. |

For every actual opportunity, assess the applicable restrictions, reporting,
branding, publication and data rights, privacy, portability, custody, renewal,
overage and independence terms against that route. Record Unknown or Not
applicable with a reason for each field. Recheck current governing terms before
action; historical source inspection does not establish current eligibility.
These are intake requirements under the repository method, not legal advice or
an eligibility finding about a provider.

### 7. Exact source scope and review date

Primary project inputs were inspected on **2026-10-19**. The following are
repository requirements and proposals, not independently measured risk data or
fresh provider-term investigations. No external provider site, private agreement,
bank account or applicant-status document was accessed for this method. There is
therefore no claimed provider access failure or newly verified provider deadline.

| Source | Exact revision / blob and actual read scope |
| --- | --- |
| Sustainability issue #71 | [Live original requirements](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/71), read before authorship; all thirteen criteria retained below. The current methodology claim is [6267037801](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/71#issuecomment-6267037801). |
| Program charter | [015300e / docs/charter.md](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/015300e6834940d537c933de3490bb5d3a707cd8/docs/charter.md), blob `adc2e809704590133f481048eecbc4b888938bf7`; complete 2,879 bytes. Draft authority and independence boundaries remain draft. |
| Budget, ethics and needs | At the same revision: [budget](budget-assumptions.md) `1ef8bb337d89f8da6f0269cc284f268321afda21` (3,199 bytes), [ethics](sponsorship-ethics-draft.md) `4f2d95f68e2f9f2b999796784cc89107ce56f22f` (2,396), [needs](needs-assessment.md) `f78028794e2f6b27be90dae8d6e8eecafe7d1c24` (3,416); all read completely. Their proposals and missing inputs retain the limits above. |
| Operating and research methods | At the same revision: [workflow](workflow-and-authorization.md) `f73b05c18e9c69ec493b27f002e2b13244a29f9a` (2,948 bytes), [qualification](scoring-and-qualification.md) `9cae800d5abe1f55cdee4d017a614756070d7d9a` (3,241), [method](research-methodology.md) `1e4dce39cf654af8c587a4f2dd3ddae8e5f921a5` (3,904), and complete [CONTRIBUTING](../CONTRIBUTING.md). No action authority is inferred from research acceptance. |
| Research #54 monetization input | [9382507 / research/market/monetization.md](https://github.com/Pick-Your-AI/pick-your-ai-research/blob/9382507e2a9df97126cb75461600880cd0f6239a/research/market/monetization.md), blob `3baf64e0aca6c9190bc6012fde5cc62e3fe9baf8`, 44,237 bytes retained. Actual read for this method covers sections 1–5, including the explicitly hypothetical incentive analysis and proposed independence controls; no full-note, legal or vendor-source re-audit is claimed. Its dated source observations remain historical. |
| Research evidence method | [9382507 / docs/RESEARCH_METHOD.md](https://github.com/Pick-Your-AI/pick-your-ai-research/blob/9382507e2a9df97126cb75461600880cd0f6239a/docs/RESEARCH_METHOD.md), blob `96a77c2a8bafe4caad5676ad80e02a915ea10de9`, complete 3,565 bytes; exact claim/source/conditions and unknown handling. [#60 source use](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/60) remains an existing authority boundary, not a newly performed rights review here. |

### 8. Literal criterion map and remaining acceptance

The original issue wording is preserved. “Offered” identifies actual method and
example content for review; it does not claim that publication or independent
acceptance has already occurred.

| # | Exact original criterion | Concrete offered outcome or remaining gate |
| --- | --- | --- |
| 1 | Indicators define units, eligible numerator/denominator, coverage, source evidence and treatment of unknown or zero denominators. | Sections 1–3, the register and synthetic complete/incomplete/zero/conflicting-input cases. |
| 2 | Cash donor concentration and usable in-kind dependency remain separate, with no headline-credit valuation treated as cash. | Separate received-cash, committed-cash and workload indicators; synthetic credits, loans, currencies and custody examples. |
| 3 | The register includes sponsor influence, exclusivity, publishing rights, portability, renewal, overage and single-person operational dependence. | Mandatory register topic review and the clause, control, exit and continuity definitions. |
| 4 | No numerical red/yellow threshold, risk appetite or financial commitment is silently adopted; proposed thresholds show evidence and an approval gate. | Section 4 and the register's distinct proposal/actual-decision fields; none adopted. |
| 5 | Each material risk records an action, decision authority role, dependency and exit condition without inventing an assignee. | Required action/authority/dependency/exit fields and worked findings with unassigned people. |
| 6 | The E01.08 neutrality policy and E02.02 budget scope are consumed or unresolved threshold/valuation decisions remain explicit; an independent reviewer accepts the methodology. | Available drafts consumed, exact absent inputs and active #20 owner retained in section 5. Independent acceptance of this unresolved-input branch is pending. |
| 7 | Identify current primary official sources and record the review date; label historical announcements, access failures and conflicting terms. | Section 7 pins the actual dated primary project inputs and read scopes; section 2 preserves disputes. No new external program investigation is claimed. |
| 8 | Verify the program, current intake/application process and deadline, or explicitly record Unknown / Not applicable with a reason. | Section 6 records internal-method Not applicable; actual program fields remain in their own intake records. |
| 9 | Document the benefit type and separately assess the present community, a fiscal-sponsored project and an independently recognized 501(c)(3). | Section 6 distinguishes all three routes and unverified organizational facts; no actual benefit or entity is asserted. |
| 10 | Evaluate restrictions, reporting, branding, publication rights, privacy, portability, renewal, overage and organizational independence as applicable. | Sections 3 and 6 plus the required topic table; actual agreement-specific conclusions remain unavailable. |
| 11 | Establish a concrete repository/public-benefit use case; estimate value and effort only with a defensible method and distinguish cash from avoided cost. | The public research/client/validation use case, native-unit cost/effort method, separate avoided cost and explicit current Unknowns. |
| 12 | Publish the canonical deliverable, structured program record where relevant, source references, remaining questions, priority rationale and recommended disposition. | Canonical method, register and worked examples prepared; no program record applies. Normal reviewed publication and delivery remain pending. |
| 13 | Obtain and link independent acceptance of the actual findings. A schema check or initial source lead alone does not meet this criterion. | Pending actual independent source/method acceptance at the concrete revision. Validation and example arithmetic alone cannot fill this row. |

After genuine independent acceptance, record the actual review URL, source
revision, scope and unresolved conditions. Reconcile issue and Project metadata
only against that actual delivered outcome. Do not close E01.08/E02.02, fill real
exposures with synthetic values or turn a method decision into authority to
apply, accept funds, activate resources or change a provider agreement.
