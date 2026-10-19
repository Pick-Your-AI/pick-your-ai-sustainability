# Cerebras trial and research-support assessment

Owning issue: [E05-01F / #44](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/44) · Parent: [E05-01 / #38](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/38) · Canonical opportunity: `CEREBRAS-TRIAL`.

Prepared **2026-10-19 UTC** against accepted sustainability revision `cad980ecc8e43a472ebe63c4360f94846d175a96`. **Research status: prepared for independent findings review. Priority: P3. Recommended disposition: Not Pursuing for the proposed independent evaluation under the inspected terms.** The applicant remains **Unknown**, and the historical opportunity stage remains **Discovered** under the [failed-gate rule](../../docs/operations-and-reporting.md#evidence-for-transitions). No provider account, payment method, application, outreach, inference request, purchase, award or activation was created by this research.

The receiving composition also preserves accepted revision `52c439c056beed504ee1d0ec2e904213f507e456`, including the Apple/Together assessments and freshness procedure. Their source/review dates and the original 39-program/72-source audit retain their own scope.

## Decision and public-benefit use

The proposed use is a small, reproducible evaluation of source-handling and numerical-response behavior for [research #41](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/41). It could reveal integration mistakes before wider comparisons and provide transparent evidence for readers choosing AI services. This is a proposed benefit, not a measured outcome. [Leaderboard #25](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/issues/25) retains its own contributor-ranking work; this assessment neither changes its scores nor turns trial access into a contribution metric.

**The current use gate fails.** The published Terms of Service expressly include inference-as-a-service APIs in their scope and prohibit using the service for benchmarking or competitive analysis. This assessment treats the proposed independent evaluation as within that restriction; the issue's label “smoke test” does not remove it. The inference documentation's policy link redirects to the company policy index that links those terms. No applicable exception or superseding project agreement was established. [S5, S8]

Pricing advertises development, evaluation and experimentation while retaining applicable terms. That statement supplies no exception for this proposed independent benchmark. [S2] Accordingly, the **current executable request budget is zero and the paid-spend budget is zero**. The conditional calculation below answers the issue's affordability question without running the evaluation. Reconsideration requires evidence of permitted use, the actual applicable terms, a qualified account/applicant route and the remaining controls below. A legal interpretation or provider exception is not supplied by this engineering review.

## Current offer, intake and conflicting documentation

| Question | Dated finding and qualification |
| --- | --- |
| Benefit type and duration | A new-account Shared Inference trial offers a one-time **$5 credit for 30 days after grant** once a payment method is verified. It is neither a recurring free tier nor a cash grant. Actual account eligibility, grant date, balance and expiry are Unknown. [S1] |
| Payment and continuation | Published pricing says trial access stops after exhaustion or expiry; paid access requires a separate choice to buy credits. A verified payment method alone is not evidence of automatic paid enrollment. Promotional credits have no cash value and are not transferable. [S2] |
| Intake | The official endpoint is [cloud.cerebras.ai](https://cloud.cerebras.ai). Public retrieval exposed no form content, so exact current fields, accepted payment methods, country checks, existing-account treatment and any account-specific agreement remain Unknown. Documentation establishes the advertised route, not a completed application. [S1–S3] |
| Deadline | No dated trial application round was established. Rate/billing documentation describes **30 days from grant**, while pricing uses **activation**. Those labels are not silently equated: the actual start, expiry, calendar deadline and timezone remain Unknown without an account-specific record. No current independent-research grant deadline is established; the separate historical RFP is closed, as recorded below. [S1–S3, S10] |
| Model and rate limits | For the prospective `gpt-oss-120b` route, the current trial table lists **5 requests/minute, 30,000 uncached tokens/minute, 90,000 total tokens/minute, and 1,000,000 tokens/hour and/day**. Limits are organization-level and model-specific; the actual console can impose different limits. [S1] |
| Material conflict | The model Markdown still has prose labeled “Free tier” with **30 RPM / 60,000 input TPM**, while its own structured model component says **Free Trial, 5 RPM / 30,000 TPM**. The latter agrees with the explicit current rate-limit page. Do not infer an enduring free tier or use the larger numbers; unresolved account limits prevent execution. [S1, S4] |
| Model identity and prices | The public model record names `gpt-oss-120b` and displays Developer prices of **$0.35 per million input tokens and $0.75 per million output tokens**. These are inputs to a conditional estimate, not a verified trial-debit quote. No immutable served-weight revision or separately explicit offer currency was established. [S4] |

These findings extend the original source lead; they do not erase its 2026-10-19 observation. The policy pages identify **27 August 2024** as their effective/update date and were inspected on **19 October 2026**. An older effective date on a currently linked page is different from a historical promotion. Account-specific or later terms still need verification before any future reliance. [S5, S6, S8]

## Three separate applicant routes

The accepted [entity baseline](../../docs/nonprofit/entity-baseline.md) records the project's actual legal identity, jurisdiction, recognition, host relationship and external signatory authority as unresolved. Repository access and the intention to pursue charitable recognition do not supply these facts.

| Route | Applicant assessment | Evidence needed before reconsideration |
| --- | --- | --- |
| Present community / before incorporation | **Unknown.** The advertised trial is not evidence that this project's actual account or representative qualifies. The proposed use gate fails independently. | Real account holder and permitted jurisdiction, new-account/trial status, lawful payment-method authority, applicable terms and permitted use. |
| Fiscal-sponsored project | **Unknown.** No executed host relationship or provider acceptance of a host/project arrangement was established. | Actual host agreement, precise applicant/beneficiary and account/payer roles, authorized representative, provider treatment and the same use/account gates. |
| Independently recognized 501(c)(3) | **Unknown.** Actual recognition is not established, and recognition would not itself establish a special Cerebras benefit or remove the use restriction. | Verified entity/status and representative, a real qualifying account, and evidence for any claimed nonprofit-specific route plus all applicable conditions. |

No current applicant is declared Ineligible solely because these facts are missing. **Not Pursuing** is the supported decision for this proposed use under the inspected evidence. No scholarship, fiscal-host exemption, automatic nonprofit entitlement, approved payer or named operating owner is inferred.

## Conditional no-spend evaluation budget

This is a **non-executed engineering design**, retained so a future permitted-use decision has a concrete scope. It does not authorize requests or claim that a trial is available. Existing offline contract checks remain useful without a provider account.

### Original synthetic cases

Use this exact common instruction with each case: **“Use only the supplied synthetic facts. Return one JSON object matching the requested keys. Do not infer missing facts or execute tools.”** The case text and expected objects below are original planning material. They include no personal, confidential, customer or third-party benchmark dataset.

| ID | Case text appended to the common instruction | Expected object |
| --- | --- | --- |
| C1 | Available memory is unknown. Return `memory_bytes`. | `{"memory_bytes":null}` |
| C2 | Provider A's stated license is unknown, and the supplied facts contain no verified license record. Return `license_verified` to indicate whether such a record was supplied, without deciding the license or permission itself. | `{"license_verified":false}` |
| C3 | Input costs 2 units per million tokens; output costs 8. Usage is 1000 input and 250 output tokens. Return `cost_units`. | `{"cost_units":0.004}` |
| C4 | A source record requires revision `rev-a`; the supplied receipt is for `rev-b`. Return `revision_matches`. | `{"revision_matches":false}` |
| C5 | A measurement reports 0 bytes. Return `memory_bytes` without replacing a measured zero with missing data. | `{"memory_bytes":0}` |
| C6 | There are 2 copies of a 300-byte object and 1 copy of a 400-byte object. Return `total_bytes`. | `{"total_bytes":1000}` |
| C7 | A source was checked on 2026-10-19 but its event date was not given. Return `checked_on` and `event_on`. | `{"checked_on":"2026-10-19","event_on":null}` |
| C8 | A supplier claims a 99% score; there is no independently reviewed measurement. Return `independently_verified`. | `{"independently_verified":false}` |

Run order, **only after a future admissible plan**, would be C1–C8 once, then C1–C8 again: **16 total attempts**, including errors or any manually authorized retry. Concurrency is one; wait at least 30 seconds between starts; disable automatic retries and tool calls. Do not multiply accounts, projects or credentials to extend limits. Two repetitions test basic response consistency, not statistical quality or broad model fitness.

### Quantity and cost calculation

The plan ceiling is **1,024 input tokens per attempt including the complete wrapper**, and **256 completion tokens per attempt**, with reasoning effort `low`. The reasoning documentation says reasoning tokens count within `max_completion_tokens` and completion usage; they must not be added as an unbudgeted allowance. [S7]

| Quantity | Exact arithmetic | Limit / interpretation |
| --- | --- | --- |
| Total input ceiling | 16 × 1,024 | 16,384 tokens |
| Total completion ceiling | 16 × 256 | 4,096 tokens, including reasoning |
| Input cost at displayed rate | 16,384 × 0.35 / 1,000,000 | 0.0057344 displayed dollar units |
| Completion cost at displayed rate | 4,096 × 0.75 / 1,000,000 | 0.003072 displayed dollar units |
| Conditional modeled debit | 0.0057344 + 0.003072 | **0.0088064 displayed dollar units** |
| Additional plan ceiling | Hard stop on any uncertain billing state or cumulative debit reaching 0.10 | A prospective trial-credit ceiling, not an enforceable provider setting verified here |
| Current executable / paid budget | Inspected use gate fails; no applicable exception established | **0 requests / 0 paid spend** |

The arithmetic fits inside the advertised 5-unit headline **only if** the credit and prices use the same billing currency, those rates actually apply to the trial, every attempt meets the token caps, and no additional billable component exists. These assumptions remain unverified, so the calculation is neither a guaranteed charge nor a usable-value estimate. No cache discount is assumed. Exact provider tokenization, request reservation and account quota must be established before execution; the plan cannot enforce an input cap using an unverified counter. The small total is below the published hourly/day ceilings but does not prove available shared capacity. [S1, S4]

A future admissible run must first freeze the case bytes/order, model identifier and available revision metadata, request parameters, tokenizer/accounting evidence, applicable terms, actual remaining trial balance/expiry and rate limits. Stop for a price/term/model change, unknown debit, exhausted credit, an unexpected paid state, a failed token-bound check or a rate-limit response. Preserve every attempt and terminal outcome; a rerun consumes the same total-attempt allowance unless a new plan is reviewed. Report truncation and malformed outputs as failures. No throughput ranking, universal accuracy claim or resource-estimate record follows from these cases.

## Obligations, privacy, publication and exit

| Area | Assessment and unresolved evidence |
| --- | --- |
| Publication and independence | The use restriction is the decisive gate above. Any future arrangement must preserve publication of unfavorable results, source transparency and sponsor disclosure without provider scoring/veto rights. These are internal requirements, not an exception already granted. Model/output rights remain dependent on the applicable third-party model terms. [S5] |
| Privacy | The public privacy policy says inference inputs/outputs are not retained. It also describes separate personal/account/usage data and purpose-based log retention; that is not proof that all metadata disappears immediately. Actual account agreements, processors, residency and any DPA were not verified. This design permits only the original synthetic text above. [S6] |
| Branding and reporting | No grant agreement or award-specific reporting, logo, publicity or endorsement requirement was established. Those fields remain Unknown for any future arrangement; no absence of conditions is inferred. A receipt must identify the actual obligations before acceptance. |
| Renewal and overage | There is no recurring free allowance. Billing documentation says auto-recharge is off by default and separately enabled for paid access. An unseen existing account must be checked; a documented default is not its actual state. No purchase or auto-recharge setting was changed. [S1, S3] |
| Portability and exit | Keep original prompts, response/usage records, model/parameter metadata and permitted result notes in portable project files if a future run is admitted. No grant of weights, immutable model pin, transferable credits or continuing capacity is inferred. Billing documentation distinguishes key/project removal from account deletion and says account deletion requires support; no deletion request was sent. [S2–S4] |
| Costs and effort | Actual cash, avoided cost, remaining credit and staffing effort are **Unknown**. The 16-attempt plan estimates conditional usage only. There is no evidenced paid counterfactual, operating commitment or maintenance-hours estimate, so headline credits are not recorded as savings or revenue. |

## Distinct research/OSS funding discovery

**Result: a historical formal research RFP is documented and closed; three separate current program leads are documented, but no presently admitted independent-research grant route or applicable benchmark-use exception is established.** Independent review found the following material sources beyond the initial pricing/document-index search. These program identities and conditions remain separate from the trial.

| Distinct program / source | Evidence and disposition for this assessment |
| --- | --- |
| **Inference Research Grant RFP**, announced 10 December 2024 [S10] | **Closed historical call.** It offered selected PIs up to **$50,000 USD in inference credits**, required full-time faculty at an accredited PhD-awarding institution and a separate sponsored-research agreement, and included model/quality/safety evaluation. The stated deadline was **31 January 2025, 11:59 p.m. PT**; a separate notice says no applications from **17 February 2025**. Preserve both statements. Its proposed public-research/university agreement is not an exception granted to this project or to the present trial. No reopening is evidenced. |
| **Early Access Program for Builders** [S11] | Current page advertises selected builders, private-preview models, credits and demos. **Documented lead; fit, selection, amount, complete agreement and permitted independent evaluation Unknown.** The linked Microsoft form returned no content in the independent public read. |
| **Cerebras Sponsorships** [S12] | Current page offers event-related discussions about speakers, workshops and credits. **Documented event lead; no actual PYA event, award, terms or benchmark permission established.** The linked Typeform returned no content in the independent public read. An invented event is not an admissible funding strategy. |
| **Ambassador Program** [S13] | Current page describes local community/promotional duties, credits and event support. **Documented advocacy/event lead; Not Pursuing for this independent-evaluation use.** No actual ambassador, operating commitment, selection, amount or applicable agreement is established. The linked Microsoft form returned no content. Advocacy duties cannot be represented as unconditional independent-research funding. |

The historical RFP's explicitly **USD** headline belongs only to that closed call. It does not establish the trial's currency, remaining balance or usable value. No verified faculty/PI/institutional agreement, event commitment or ambassador role was established for any of the three applicant routes. The current leads need their own full terms, rights and fit review if a genuinely applicable use is later proposed; no application, event, promotion or provider contact was initiated.

The initial 2026-10-19 domain-filtered queries were `site:cerebras.ai ("research" OR "open source") ("grant" OR "credits" OR "sponsorship")` and `site:inference-docs.cerebras.ai "research" "program"`. Results included unrelated domains and missed the material pages above. That initial result is not evidence of global absence. The corrected discovery rests on the actual primary pages and individually recorded form-access limits; no other private or future arrangement is ruled out. Research-oriented tutorials and open-model availability do not themselves establish a grant.

The existing unique `CEREBRAS-TRIAL` opportunity is retained, with the four distinct related discovery leads recorded separately inside its assessment metadata. Their headlines are not trial benefits, qualified pipeline opportunities or awards. Their actual source/form URLs are retained, rather than inventing a grant endpoint or a duplicate trial. The organization-wide issue/PR duplicate check on 2026-10-19 found the existing #44 and its parent/related research references; it found no Cerebras PR before the public work claim. This is a dated coordination result, not a permanent guarantee.

### Remaining questions; no outreach sent

1. Has a genuinely applicable independent-research intake reopened or become available? Recheck the closed RFP or a distinct new lead and obtain the actual active intake, complete terms, eligible applicant/use, award/expiry conditions and deadline. The documented builder/event/advocacy leads are not automatic substitutes.
2. Would the exact independent evaluation and publication be permitted under the actual applicable agreement? Record any explicit exception and its scope without relabeling the work to evade a restriction.
3. Which actual entity/account/representative, jurisdiction and payment method qualify, and is a new-account trial genuinely available? Verify the three routes independently.
4. What currency, model revision, trial debit rates, reasoning/token accounting, quota, remaining balance and expiry apply to that account?
5. What publication, model/output rights, branding, reporting, data handling, exit and continuing-cost obligations would apply?

These are prepared evidence questions, not messages to a provider or requests for a commitment. The next action is independent acceptance of this assessment. Reopen the opportunity only on material new governing/program evidence or a separately reviewed permitted use. Monthly source maintenance and pre-action checks retain the [freshness procedure](../../docs/research-freshness.md); no artificial application date or operating owner is assigned.

## Sources, access and confidence

All source accesses below occurred on **2026-10-19 UTC**. URLs are durable source references, not session identifiers. Confidence is high in the attributed published statements; actual intake/account facts, applicable exceptions and usable value remain unverified.

| ID | Primary source | Inspection scope and access result |
| --- | --- | --- |
| S1 | [Rate limits](https://inference-docs.cerebras.ai/support/rate-limits) | Current trial, model quotas and reservation behavior; full relevant table/text read. |
| S2 | [Pricing](https://www.cerebras.ai/pricing) | Trial conditions and separate paid continuation. Extracted page did not expose its numerical model-price table; model rates above come from S4. |
| S3 | [Account & Billing](https://inference-docs.cerebras.ai/console/account-billing) | Published account, credit, auto-recharge and deletion procedures; no signed-in account inspected. |
| S4 | [OpenAI GPT OSS model Markdown](https://inference-docs.cerebras.ai/models/openai-oss.md) | HTML retrieval exposed navigation only and the web Markdown fetch failed. The advertised public Markdown was then retrieved successfully: 19,369 bytes, SHA-256 `ec19fdfa0659856b8ea5606551f0567032157a04f8f69a0206bc1f2fae5f8440`. Both the conflicting prose and structured trial/pricing component were read; no MDX was executed. |
| S5 | [Terms of Service](https://www.cerebras.ai/terms-of-service) | API scope and use/publication restrictions; current linked text has effective date 27 August 2024. This is not a substitute for unseen account-specific agreements. |
| S6 | [Privacy Policy](https://www.cerebras.ai/privacy-policy) | Relevant data, retention and transfer provisions, updated 27 August 2024; no private contract or residency validation. |
| S7 | [Reasoning](https://inference-docs.cerebras.ai/capabilities/reasoning) | The `gpt-oss-120b` effort controls and completion/reasoning budget statements. |
| S8 | [Policy index](https://www.cerebras.ai/policies) | The [inference policy link](https://inference-docs.cerebras.ai/support/policies) redirects here; it links S5/S6 and separately dated other-product terms. An older software EULA is not used as a substitute for API terms. |
| S9 | [Complete public documentation index](https://inference-docs.cerebras.ai/llms.txt) | All 133 returned lines inspected for a distinct program/intake lead; linked pages are not thereby all reviewed. |
| S10 | [Inference Research Grant RFP](https://www.cerebras.ai/blog/grantfrp) | Historical 2024–2025 call; current page explicitly records closure. |
| S11 | [Early Access Program](https://www.cerebras.ai/early-access) | Current public builder lead; complete page read, application fields and full agreement remain unverified. |
| S12 | [Sponsorships](https://www.cerebras.ai/sponsorships) | Current public event lead; complete page read, no event or support award established. |
| S13 | [Ambassador Program](https://www.cerebras.ai/ambassadors) | Current public duties/benefits read; no current selection, amount or accepted operating agreement. |
| A1 | [Cloud intake endpoint](https://cloud.cerebras.ai) | Public retrieval returned no form content. Access was attempted; successful current form/account verification remains null in the freshness register. |
| A2 | [Early-access form](https://forms.cloud.microsoft/r/zUw2W8LEiY) | Linked from S11; independent public retrieval on 2026-10-19 returned zero content lines. Current fields and availability Not Verified. |
| A3 | [Event sponsorship form](https://form.typeform.com/to/TUK3flkj) | Linked from S12; independent public retrieval on 2026-10-19 returned zero content lines. Current fields and availability Not Verified. |
| A4 | [Ambassador form](https://forms.cloud.microsoft/r/fXi2GLpDGQ) | Linked from S13; independent public retrieval on 2026-10-19 returned zero content lines. Current fields and availability Not Verified. |

The register preserves the original trial facts, adds these dated sources and the model-document conflict, and updates only this opportunity and its pipeline projection. Stage **Discovered** is retained after the failed use gate; **P3** reflects that exclusion and the small temporary benefit. All eight weighted ratings, total score, usable value and currency remain null: a 20/20/15/10/10/10/10/5 rubric does not justify invented inputs or converting a promotional ceiling into cash.

## Acceptance map

Criterion numbers follow the thirteen literal checkboxes in #44. This document prepares their evidence; the actual independent review and accepted revision must be linked in the issue before research completion.

| Criteria | Evidence / remaining boundary |
| --- | --- |
| C1 and C7: primary sources, dates, historical/access/conflict labels | Source table, separate policy effective/access dates, failed form/model extraction and explicit quota conflict. |
| C2 and C8: program, intake, benefit, restrictions and deadline | Offer/intake table and source-backed decision; unresolved form, account, grant intake and calendar dates stay Unknown with reasons. |
| C3 and C9: three eligibility routes | Separate route table using the accepted entity baseline; no actual eligible applicant asserted. |
| C4, C6 and C12: canonical assessment, disposition, budget, discovery, records, priority and questions | This file, the unique opportunity and matching pipeline/freshness records, exact conditional arithmetic and original cases, bounded discovery and evidence questions. |
| C10: obligations, reporting, branding, publication, privacy, portability, renewal, overage and independence | Obligations table and decisive use gate; no award-specific obligation or legal exception fabricated. |
| C11: concrete public use, defensible value/effort, cash versus avoided cost | Proposed research #41 use; original synthetic plan; actual value and effort remain Unknown without a counterfactual or commitment. |
| C5 and C13: independent acceptance of actual findings | **Pending exact-revision independent findings review and publication.** Schema/tests alone do not satisfy this. Review must address the use gate, conflict, conditional budget, bounded funding search and applicant Unknowns. |

Research acceptance can complete this investigated **Not Pursuing** outcome without creating an application, award, account, operating arrangement or broader parent completion. Existing technical, legal, financial and administrative issues retain their own scope.
