# Operating costs and resource needs

Issue [#19 / E02-01](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/19) · Source inspection: **2026-10-19** · Status: **findings prepared for independent review**.

This is the canonical cost-and-need baseline for the six Pick Your AI repositories.
The recommendation is to accept the documented capabilities, proposed needs and
explicit Unknowns as the input to the operating budget and individual support
investigations. It is **P1 foundational work**; a numerical opportunity score is
Not applicable. No complete operating total, received donation, applicant
qualification or authority to activate a service is established.

The inspection found public source and execution evidence, but no invoices,
statements, provider billing readbacks, equipment ownership records or complete
subscription inventory. **Actual expenditure, account balances, awarded support
and currently usable donated capacity remain Unknown, not zero.** This is a
limit of the inspected evidence, not a claim that no spending, equipment,
agreement or donation exists. The accepted [entity baseline](../nonprofit/entity-baseline.md)
separately preserves the unverified owner, administrator, payer, custodian and
signatory facts. A contributor's repository access is not evidence of those roles.

## Evidence classes and accounting boundary

| Class | What can be recorded here | Current finding |
| --- | --- | --- |
| Actual expense | A dated paid or accrued amount, currency, covered period, exact resource and accounting evidence | **Unknown** for every need below; public prices and a successful job are insufficient |
| Proposed spend | An explicit engineering estimate or allocation, with its scope and assumptions | The leaderboard's USD 112.70/month estimate and alternative USD 200/month design ceiling; all other amounts Unknown [L1] |
| Donated service or resource | An actual award/acceptance, usable units, recipient, restrictions and expiry; distinguish a loan from a gift | **Unknown**; no award or activation receipt was inspected |
| Documented no-cost capability | A current provider entitlement for a defined usage class, with limits and actual project applicability kept separate | Standard GitHub-hosted Actions usage in public repositories is documented as free; account storage and paid features still need inspection [G1] |
| Observed capability | A source configuration or an actual, bounded execution receipt | The repository-specific records below; this class makes no claim about who paid or owns the equipment |
| Unmeasured need | A canonical technical outcome with resource quantity, availability or cost still unresolved | The gaps and required meters below; a useful outcome is not a purchase order |

Cash, promised cash, credit face value, activated service units, loaned assets and
realized avoided cost are different measures. No unit price is multiplied by an
invented demand. A credit's headline value is not income or avoided expenditure.
Avoided cost requires an accepted workload, actual eligible coverage and evidence
that the same necessary resource would otherwise have been purchased. Contributor
time, application effort and continuing operating effort remain **Unknown hours**.

## Canonical need ledger

Each ID is local to this funding ledger. It points to existing technical ownership;
it creates no replacement implementation, service owner or device acceptance gate.
For every row, actual paid amount/currency, payer, contract start, renewal/expiry,
unused entitlement and current account limit are **Unknown unless explicitly
stated**. A unit is a field to measure, not a forecast.

| Need | Existing capability and canonical receiving scope | Concrete remaining resource question | Required meters and monetary status |
| --- | --- | --- | --- |
| N01 — Leaderboard operation | The accepted hosting plan selects separate staging/production application and database resources, with backup/export work. It remains subject to [leaderboard #25](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/issues/25) and its existing deployment/security/operations work. [L1] | Obtain an actual account-specific quote and operating/billing evidence for that architecture before valuing compatible support. A generic cloud credit is not automatically compatible hosting. | VM and database months by environment/region; backup and independent export storage/operations; transfer and taxes where applicable. **Proposed USD 112.70/month**, alternative USD 200 ceiling; actual expense Unknown. |
| N02 — Existing public website and domain | The website documents a static distribution for Apache on GoDaddy cPanel, without a production Node process. Its quality issues [#19](https://github.com/Pick-Your-AI/pick-your-ai-website/issues/19) and [#25](https://github.com/Pick-Your-AI/pick-your-ai-website/issues/25) have actual accepted completion records. [W1–W3] | Establish current hosting/domain terms, payer, renewal and any unmet capacity need. Preserve the existing deployment contract. A donated replacement needs a separately justified migration and exit plan; do not recreate completed quality work. | Hosting/domain periods, storage, transfer, deployment volume and any actual increment beyond existing entitlement. **All amounts Unknown.** |
| N03 — Shared CI, validation and evidence retention | Public workflow sources already define research, website and native qualification jobs. Actual mobile receipts demonstrate available hosted execution for their recorded scopes. [R1, W3, A1–A3, D1–D2] | Measure actual job usage, queue/resource restrictions, retained artifacts and account billing before seeking additional runners or storage. Test failures and pending acceptance do not themselves demonstrate a lack of compute. | Runs by runner class, duration, concurrency, cache/artifact byte-time, retention and egress if charged. Standard public hosted usage has a documented no-cost baseline [G1]; **actual account charges/paid additions Unknown**. |
| N04 — Apple build, device and release qualification | Ordinary toolchain pin: Xcode 16.4/16F6. Separate submission lane: Xcode 26.3/17C529, iOS/device and simulator SDK 26.2, minimum OS 17.0. The accepted historical pin receipt records actual hosted simulator/build work. [A1–A3] | Inventory owned/loaned Macs and representative physical devices, and map any shortage to the existing [device matrix #107](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/107) and [store-policy #113](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/113) scope. Current package, simulator and SDK work does not prove physical coverage, membership or store submission. | Compatible Mac hours, exact OS/SDK/device cases and physical device-days; acquisition/loan, maintenance, shipping, return and membership terms separately. **All amounts and owned inventory Unknown.** |
| N05 — Android build and installed-device qualification | One exact hosted source passed 5,565 core/JVM and 432 simulated preview tests. A later exact installed receipt has launch and acknowledged-save/force-stop passes, a rotation initial-guard failure and deletion not run. [D1–D2] | Preserve the actual partial installed evidence. Finish the canonical source/qualification work and inventory physical-device/test-lab gaps against [Android #107](https://github.com/Pick-Your-AI/pick-your-ai-android/issues/107). Do not buy a duplicate emulator solution merely because a behavioral guard failed. | Runner/emulator hours by exact image, KVM/hypervisor availability, device/API/ABI cases and physical device-days; acquisition/loan/support costs separately. **All amounts and owned inventory Unknown.** |
| N06 — Empirical model/resource research | [Research #61](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/61) retains empirical work across context/cache precision/concurrency and peak/error comparisons. Existing protocols and partial observations are source material, not the missing complete dataset. [R2] | Define a finite model/runtime/protocol cohort, admissible source/weights and safe hardware envelope, then identify actual available capacity. [#21](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/21) owns the reusable demand model. | Model/runtime identities, prompt/output tokens or sequences, repetitions, GPU type/VRAM and accelerator-hours, CPU/RAM, storage/transfer and cleanup. **Usage and money Unknown**; no new job or model download is authorized by this ledger. |
| N07 — Public evidence and source admission | The research source policy and website's [real-data admission #15](https://github.com/Pick-Your-AI/pick-your-ai-website/issues/15) retain exact source/use and artifact boundaries. [Research #62](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/62) still needs publisher identity/budget/task pins; it has not selected a replication. [R2–R3] | Obtain the missing source permissions, evaluated-version disclosures and exact publishable artifact scope. Credits cannot reconstruct an undisclosed publisher run or make a source eligible for redistribution. | Eligible datasets/artifacts and permitted storage/retention/transfer; review effort and any legitimate license fee only after actual terms. **Amounts Unknown; no replication compute selected for the #62 gap.** |
| N08 — Security, accessibility and independent review | Existing website quality and mobile/source checks provide bounded evidence. The leaderboard and other repositories keep their existing security and operating requirements. [L1, W3, A3, D1] | Select a specific uncovered audit, physical accessibility check or operating exercise, with deliverables and permission scope. Preserve completed automated checks; do not value a second tool as automatically useful. | Defined review scope, specialist hours, device/user sessions and remediation follow-up. Existing free capabilities first; **effort, fees and incremental value Unknown**. |
| N09 — Governance, finance and administration | The accepted entity/asset baseline documents observed public references and unresolved legal, financial and representative facts. [S1] | Establish appropriate private evidence custody, actual subscriptions/obligations, jurisdiction and qualified professional scope. [#20](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/20) owns the full budget; [#24](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/24) owns financial-control procedures. | Accounting periods/transactions, applicable filings/renewals, professional hours, actual software seats and custody costs. **Amounts, due dates and appointed custodians Unknown.** |

### What the execution records establish

The Android installed result is from run **39241000776**, job **118023567630**,
tested commit `8c1a9ec663fb082289394b256ba65f1c5d49533f`. Launch and
acknowledged-save/force-stop passed;
rotation failed before its main assertions, and deletion was not executed. The
independent receipt records ACL restoration. Those facts neither establish the
whole supported-device matrix nor justify replacing an unresolved test result
with a presumed resource shortage. The earlier 5,565/432 counts belong to the
different exact source in D1. No native job was run for this needs assessment.

The Apple historical receipt A3 is similarly attributed to its original source
and execution: it is evidence that a pinned hosted path worked, not a new test of
the current checkout. The current ordinary and submission pins are separate;
funding requests must state which lane and exact receiving test need capacity.
Five local Swift packages and SDK system SQLite are documented, so their presence
does not establish paid third-party package subscriptions. [A1–A3]

GitHub's current billing documentation says standard GitHub-hosted Actions usage
in public repositories is free; larger runners are charged. Artifact/cache
storage and account settings have separate limits and billing rules. This makes
the existing public workflow path a baseline to inspect, not proof of a zero
invoice, unlimited retention, donated hardware or free external AI review. No
account billing settings were accessed. [G1]

## The single quantified planning component

The following is a transcription and arithmetic check of the accepted leaderboard
engineering estimate, inspected **2026-10-19**. Currency is **USD** and the unit
is **per month for both environments together**. It is not a fresh provider
quote, paid reservation, complete organization budget or approved expenditure. [L1]

| Included component | Planning calculation | USD/month |
| --- | --- | ---: |
| Two application VMs | 2 × 24.00 | 48.00 |
| Two managed databases | 2 × 15.15 | 30.30 |
| VM backup allowance | 30% × 48.00 | 14.40 |
| Independent export allowance | Explicit planning allowance, not a vendor quote | 20.00 |
| **Proposed combined allocation** | 48.00 + 30.30 + 14.40 + 20.00 | **112.70** |
| **Alternative design ceiling for that same scope** | A planning bound, not another expense | **200.00** |

The original [budget assumptions](../budget-assumptions.md) retain their explicitly
constant-scope annual scenario. It must not become twelve months of actual spend.
The ceiling is not a provider-enforced cap, and the estimate does not resolve
taxes, actual account rates, usage growth, renewal or post-credit exposure.

The same hosting source rejects an automatic Cloudflare-proxied substitution for
its current long-request-target contract. Therefore Project Alexandria credits
cannot be valued against N01 just by matching the word “hosting.” The separate
[Cloudflare investigation #52](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/52)
must identify a compatible incremental use. Existing static website hosting is
also an established architecture, not an unassigned blank destination. [L1, W1]

## Preventing double counting

1. Treat the USD 112.70 allocation and USD 200 ceiling as alternative descriptions
   of one scope. Do not add the ceiling, its headroom or an annualized version to
   the monthly allocation.
2. Count one actual CI invocation and one retained artifact once, even when its
   result is referenced by several repositories or reviews. Distinct executed
   jobs still have distinct meters; sharing a source does not merge their bills.
3. Separate app storage, VM backups and application-consistent exports by their
   actual coverage. Do not charge bundled storage again as an assumed add-on, or
   claim that one backup product proves every recovery requirement.
4. Evaluate purchase, loan, hosted access and reimbursement as alternatives for
   the same device/compute need. Include actual support/return costs if known;
   do not add a credit's face value to the covered resource's avoided cost.
5. Keep [Research #39](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/39)
   user-Build cost semantics separate from the community's operating expenses.
   Synthetic catalog prices, source-code volume and issue counts are not demand,
   revenue, beneficiaries or achieved impact.

## Applicant routes and conditions on support

This ledger is **not a provider program**, so its application form, intake status,
award deadline and opportunity stage are **Not applicable**. No new program row
belongs in `data/opportunities.json`. Actual contract expiry, tax/filing due dates,
application deadlines and financial start periods are **Unknown** until the
corresponding agreement, jurisdiction or program is qualified. Existing sponsor
and fiscal-host leads in #19 are not requalified by this needs inventory. [S1–S2]

| Route | Bounded finding | Benefit and authority boundary |
| --- | --- | --- |
| Present community | Public repositories and technical needs are observed; exact legal applicant, payer and owned resources remain Unknown. | Cash, credits, equipment and professional help are possible benefit classes, not achieved benefits. Ordinary project engineering may continue under the user's delegation; external representations need actual facts. |
| Fiscal-sponsored project | No executed sponsor/host relationship is established in the accepted baseline. | Do not transfer a host's status, credits or account rights to this project by assumption. Establish actual applicant/beneficiary, fees, custody, permitted uses and exit terms before valuing that route. |
| Independently recognized 501(c)(3) | Recognition is an intended route, not a verified current condition. | Recognition alone would not establish every provider's admission, geography, account or use restrictions. Program-specific eligibility and award/activation remain separate records. |

The following are required fields for a **particular proposed support arrangement**,
not findings that any obligation already exists:

| Condition | Evidence needed before a value or commitment claim |
| --- | --- |
| Use and overage | Exact credited products/units, workload eligibility, existing entitlement, uncovered charges/taxes, actual limits and a feasible stop mechanism; an alert or planning ceiling is not automatically a hard cap. |
| Renewal and portability | Start/expiry, renewal or automatic billing terms, exportable source/data/artifacts, migration effort and who can continue or terminate the resource. Credit expiry is not the same as data retention. |
| Privacy and source rights | Authorized data class, credentials kept private, provider processing/retention terms and exact publication/redistribution rights. A public repository license does not license every external asset or private input. |
| Reporting and branding | Actual report cadence, required acknowledgements, logo rights and workload evidence; no promotional promise, trademark permission or report deadline is inferred from a program name. |
| Independence and publication | Preserve impartial evaluation and publishable methods/results within applicable rights. Do not trade ranking, findings or repository decision authority for a donation. Any benchmark restriction must be assessed for the exact intended study. |
| Equipment or professional help | Title versus loan, delivery/taxes, damage/return/support duties, qualified scope, conflicts and permitted disclosure; no absent person is assigned a role. |

These questions consume the existing [authorization](../workflow-and-authorization.md),
[operations](../operations-and-reporting.md) and [sponsor ethics](../sponsorship-ethics-draft.md)
work. They do not introduce another permission requirement for reversible,
authorized repository engineering or claim legal acceptance of an agreement.

## Concrete handoff and next actions

For each request, prepare a record containing **Need ID; receiving issue and exact
technical artifact; finite output/cohort; existing capacity; unmet units and
period; rate/currency/source date; credit-covered and uncovered portions; actual
operator/payer/custodian if verified; expiry/renewal; privacy/source-use scope;
exit/stop procedure; and exact independent receiving decision**. Leave unverified
fields Unknown. No request, application or account change has been sent by this
assessment.

- **#20 budget:** consume N01's explicitly proposed amount and the other rows'
  Unknowns. Obtain actual private expenditure/commitment evidence before filling
  actuals; select a real budget start and scenario rather than summing blanks.
- **#21 demand:** produce finite resource meters for the selected research and
  development outputs. Existing successful jobs are a starting capability, not
  a forecast of future API/GPU use.
- **#52 and other provider owners:** demonstrate an incremental compatible need,
  actual applicant path and applicable terms before assigning credit value.
  Standard public CI and existing website deployment must be considered first.
- **Actual evidence custodian, currently unverified:** privately reconcile
  invoices, subscription terms, devices and any support already received. A
  public receipt should state verified scope/date without publishing credentials,
  banking details, private account identifiers or confidential agreements.

## Sources and inspection scope

All records below were personally read on **2026-10-19**. Immutable repository
sources preserve the inspected revision even if main advances. Actual execution
is attributed to its original receipt; no current native/provider execution,
invoice audit or physical inventory was performed. The current official GitHub
policy was opened directly; no historical promotion or search snippet supplies a
financial amount here.

| ID | Source and pinned scope |
| --- | --- |
| L1 | [Leaderboard hosting architecture at `73715b48`](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/blob/73715b4850fc0df4a2afbdd877ad2b2644f1d769/docs/hosting-architecture.md): accepted engineering topology, dated price observations, allowances and remaining provisioning limits. |
| W1 | Website [architecture](https://github.com/Pick-Your-AI/pick-your-ai-website/blob/bbed6ca4c62352c0724dd04ea01ffcd3b8490d61/docs/ARCHITECTURE.md) and [deployment contract](https://github.com/Pick-Your-AI/pick-your-ai-website/blob/bbed6ca4c62352c0724dd04ea01ffcd3b8490d61/docs/DEPLOYMENT_CONTRACT.md): existing static Apache/cPanel target and distribution boundary. |
| W2 | [Website README at `bbed6ca4`](https://github.com/Pick-Your-AI/pick-your-ai-website/blob/bbed6ca4c62352c0724dd04ea01ffcd3b8490d61/README.md): synthetic/current product boundary; not an invoice. |
| W3 | Website [CI at `bbed6ca4`](https://github.com/Pick-Your-AI/pick-your-ai-website/blob/bbed6ca4c62352c0724dd04ea01ffcd3b8490d61/.github/workflows/ci.yml) and actual issue [#19](https://github.com/Pick-Your-AI/pick-your-ai-website/issues/19)/[#25](https://github.com/Pick-Your-AI/pick-your-ai-website/issues/25) completion records: quality capability, with original source/CI/deployment scopes preserved. |
| A1 | Apple [ordinary toolchain](https://github.com/Pick-Your-AI/pick-your-ai-apple/blob/63df6b24b7bee4272bdcc8e75ad679202089110b/App/toolchain.json), [submission toolchain](https://github.com/Pick-Your-AI/pick-your-ai-apple/blob/63df6b24b7bee4272bdcc8e75ad679202089110b/App/submission-toolchain.json) and [submission SDK](https://github.com/Pick-Your-AI/pick-your-ai-apple/blob/63df6b24b7bee4272bdcc8e75ad679202089110b/App/submission-sdk.json): exact distinct declared pins. |
| A2 | [Apple submission workflow at `63df6b24`](https://github.com/Pick-Your-AI/pick-your-ai-apple/blob/63df6b24b7bee4272bdcc8e75ad679202089110b/.github/workflows/submission-sdk.yml): separate hosted SDK qualification, not a paid membership or store upload. |
| A3 | [Apple toolchain validation note at `63df6b24`](https://github.com/Pick-Your-AI/pick-your-ai-apple/blob/63df6b24b7bee4272bdcc8e75ad679202089110b/docs/validation/toolchain-pin.md): retained pin failure/recovery and original hosted simulator/build receipt, five local packages and system SQLite. |
| D1 | [Android actual #557 receiving receipt `6266171670`](https://github.com/Pick-Your-AI/pick-your-ai-android/pull/557#issuecomment-6266171670): exact `c2bfd35209ff9315f4d596809f50eae4f8214ebb`, tree `70c5a9995dcbf2ee301ee8a51931a1fd03bf80d3`; 5,565 core and 432 simulated preview cases. |
| D2 | [Android actual #467 installed receipt `6266220712`](https://github.com/Pick-Your-AI/pick-your-ai-android/pull/467#issuecomment-6266220712): exact original run/job/source, two passes, rotation guard failure, deletion not run and restored ACL; no physical-device claim. |
| R1 | [Research validation workflow at `9382507e`](https://github.com/Pick-Your-AI/pick-your-ai-research/blob/9382507e2a9df97126cb75461600880cd0f6239a/.github/workflows/research-validation.yml): current public Python validation configuration, not a GPU job or funding receipt. |
| R2 | Live Research [#61](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/61) and [#62](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/62): literal remaining empirical and publisher-disclosure scope at inspection. |
| R3 | [Research source policy at `9382507e`](https://github.com/Pick-Your-AI/pick-your-ai-research/blob/9382507e2a9df97126cb75461600880cd0f6239a/research/T0-configuration/catalog-data-sources.md) and [website #15](https://github.com/Pick-Your-AI/pick-your-ai-website/issues/15): canonical source/admission ownership; no universal publishing permission inferred. |
| S1 | [Accepted entity baseline at `395da058`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/395da05868f3169548893ea239f9fc327fcdc8c8/docs/nonprofit/entity-baseline.md) and its [#11 completion](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/11): actual applicant/owner/payer facts remain qualified Unknowns. |
| S2 | [Initial needs map](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/395da05868f3169548893ea239f9fc327fcdc8c8/docs/needs-assessment.md), [budget assumptions](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/395da05868f3169548893ea239f9fc327fcdc8c8/docs/budget-assumptions.md) and live #19/#20/#21/#24/#68: original scope and later independent outcomes remain separate. |
| G1 | [GitHub Actions billing documentation](https://docs.github.com/en/billing/concepts/product-billing/github-actions), current official page read 2026-10-19: standard public hosted usage, larger-runner distinction and separate storage/account billing boundaries. |

No conflicting invoice or account record was available to reconcile. A source
file can establish a selected architecture while its actual service/account
status remains Unknown; these are different claims. An initial attempted research
memory-note URL returned 404 because it was the wrong path; the actual issue #61
and its canonical `research/market/sizing-validation.md` reference were used.
That lookup failure says nothing about resource availability. The original
sponsor/fiscal-host seed URLs are leads only in this assessment, not refreshed
program or price findings.

## Acceptance map and remaining facts

| #19 criterion | Reviewable result |
| --- | --- |
| Distinct actual/proposed/donated/no-cost classes | Evidence table, actual Unknowns and exact source/usage limits |
| Every amount sourced/dated/currency; Unknown not zero | One USD/month planning calculation at L1; all actuals and unmeasured amounts Unknown |
| Canonical requirements and double counting | N01–N09 and five explicit deduplication rules |
| Primary sources/date/history/access/conflicts | Pinned source table, current G1, historical-execution attribution and access/conflict note |
| Program/intake/deadline | Foundational ledger Not applicable with reason; actual agreement/program dates Unknown |
| Benefit and three applicant routes | Separate community, fiscal-sponsored and independent-recognition assessments |
| Restrictions and operating conditions | Support-condition table with publication, privacy, portability, renewal/overage, reporting/branding and independence |
| Concrete use and defensible value/effort | Finite receiving outcomes/meters; cash/credit/avoided-cost distinctions; no invented value or hours |
| Canonical delivery, records, questions, priority/disposition | This file and explicit budget/demand/provider/evidence handoffs; P1, no irrelevant opportunity row |
| Independent findings acceptance | **Pending exact-revision independent review and delivery; link the actual review in #19.** Local checks do not establish this acceptance. |

The unresolved facts are the actual financial/asset inventory and each request's
finite volume, terms, custodian and incremental value. They remain prerequisites
to the particular valuation or external representation that needs them. They do
not prevent reviewing this requested evidence-and-Unknown baseline, and its
acceptance does not complete the budget, demand model, technical device matrix,
empirical study or support acquisition.

Local validation on 2026-10-19 used Python 3.12.14 with the repository's existing
pinned dependencies: **61 tests passed in 3.177 seconds**, and the repository
validator passed **21 JSON and 36 Markdown files with zero errors**. These are
local consistency checks, not source acceptance or native/provider execution.
