# Anthropic external-researcher API access assessment

Opportunity **ANTHROPIC-RESEARCHER / E05-01B**. Canonical issue: [#40](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/40). Research state: **Done**; opportunity stage: **Verified**; actual applicant eligibility: **Unknown**. Research author: current CompleteDotTech-delegated project session (fb637); independent program/intake findings were accepted in [review 5571407286](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/93#pullrequestreview-5571407286).

## Decision and concrete project fit

**Retain P2 as a potential research route; do not treat the project as qualified or the headline credits as available funding.** A defensible proposed question is whether a model reports uncertainty accurately when a technical recommendation lacks supporting evidence. That is a possible safety/alignment framing for the provider to evaluate, not a finding that Anthropic considers this project high priority. General product comparison alone does not establish fit.

Proposed public-benefit output: an original, reproducible uncertainty-evaluation corpus and analysis for the existing [research comparison work](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/41), with a reusable evidence-reporting method for [Leaderboard #25](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/issues/25). Keep implementation and publication in those canonical repositories. The proposal does not assert that their issue acceptance or an actual study is complete.

The proposed protocol uses 120 original technical scenarios, each in complete-evidence and missing-evidence variants, with three repetitions: **720 requests per selected model**. This is a planning calculation, not a measured workload or executed benchmark. Before execution, freeze ground truth and scoring rules for unsupported factual assertions, appropriate abstention and citation provenance; independently adjudicate a sample; retain model/version, prompt, output and failure provenance. Use ordinary non-sensitive synthetic inputs, no safeguard circumvention, no human-subject recruitment and no third-party confidential material. Do not infer production latency or reliability from a subsidized service tier.

## Source observations and prior evidence

Sources were actually inspected on **2026-10-19**. Dates below distinguish document versions from retrieval. These are publisher statements and a researcher’s scoped assessment; no account or provider decision was inspected.

| Source | Version and actual observation |
| --- | --- |
| [A1: Researcher program](https://support.claude.com/en/articles/9125743-what-is-the-external-researcher-access-program) | Help article dated 2026-03-16; full program/process/FAQ retrieved. |
| [A2: Public application](https://forms.gle/pZYC8f6qYqSKvRWn9) → [actual form](https://docs.google.com/forms/d/e/1FAIpQLSdmq-KFTREKw9SXqDqj9kACfhd_5DYZSrifWR7Q3z0ZqAZZog/viewform?usp=send_form) | Undated live form; public HTTP 200 and visible field text read. The search reader failed, but a direct public retrieval succeeded; neither error is treated as a closed intake. |
| [A3: Commercial terms](https://www.anthropic.com/legal/commercial-terms) | Effective 2025-06-17; API scope, content, restrictions, publicity, fees and termination read. |
| [A4: Credit terms](https://www.anthropic.com/legal/credit-terms) | Effective 2024-03-04; usage/promotional credit distinctions read. |
| [A5: Commercial retention](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) | Article dated 2026-07-01; retention exceptions and covered-model caveat read. |
| [A6: Privacy policy](https://www.anthropic.com/legal/privacy) | Effective 2026-09-10; form/contact information is distinct from business-customer content governed by customer agreements. |
| [A7: Published next usage policy](https://www.anthropic.com/legal/aup), [prior policy](https://www.anthropic.com/legal/archive/22742366-2ef0-4c7a-a833-6523f10d3944), [change announcement](https://www.anthropic.com/news/2026-usage-policy-update) | Live page is effective **2026-11-12**, after this review; prior version says 2025-09-15. The 2026-10-08 announcement confirms the future effective date. |
| [A8: Region-policy redirect](https://www.anthropic.com/supported-countries) → [published policy](https://www.anthropic.com/legal/supported-regions) | Live destination also says effective 2026-11-12. Preserve that date; do not silently apply a future version to an October applicant. |
| [A9: Claude for Open Source](https://claude.com/contact-sales/claude-for-oss) | Undated live subscription offer inspected only to distinguish the separate program. |

The [prior register at 395da058](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/395da05868f3169548893ea239f9fc327fcdc8c8/data/opportunities.json) remains the immutable source-lead history. This assessment adds inspected intake and governing terms; it does not rewrite a prior applicant outcome. Organization issue-title searches for Anthropic and Gemini, the 39-record register and owning issue/comments were checked on 19 October. The Anthropic title search returned #40; the distinct ANTHROPIC-CLAUDE-OSS record remains with [#61](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/61), not merged into this opportunity.

## Current intake, benefit and deadline

A1 describes selected safety/alignment research, standard publicly offered API models, monthly assessment on the first Monday, and a typical successful allocation of **$1,000 in API credits**, with exceptional larger allocations possible. It excludes consumer web credits and nonpublic-model access; it provides no usage-policy exemption. Silence is not an approval. The guidance recommends one Console organization for a research program; this is not proof that a particular organization exists or that every team arrangement is mandatory. No submission deadline or guaranteed response date is established. The monthly review cadence is not a cutoff, renewal promise or internal due date.

A2 visibly requests contact/email, optional organization, referral status, Console organization ID, researcher/team expertise (under 200 words), research/request rationale (under 300), requested allocation, and a public scholarly or GitHub profile. It asks about tolerance for lower-priority capacity, and has optional context and US tax/accounting questions. These field observations establish intake requirements, not a submitted application. The form treats the proposal as nonconfidential; its terms link is the commercial agreement and its privacy link is A6. Its displayed deletion-contact text and linked mail destination differ, so verify a contact before using it. Google sign-in is offered for saving progress; a JavaScript notice appeared in the static response, so interactive submission behavior was not tested.

## Eligibility by applicant route

| Route | Finding and missing evidence |
| --- | --- |
| Current community or individual | **Unknown for the actual applicant.** The form accommodates an individual and optional organization, but no investigator expertise, eligible location, account authority or provider-accepted safety question is established. Non-incorporation alone is not a sourced exclusion. |
| Fiscal-sponsored project | **Unknown.** Sponsorship is not an independent admission criterion in the inspected material. Confirm the researcher, sponsor authority, account holder, permitted collaboration and applicable jurisdiction; do not transfer credits across entities by assumption. |
| Independent 501(c)(3) | **Unknown.** Recognition is neither an established prerequisite nor a substitute for research fit, investigator capability, account and regional conditions. No recognition or organizational account is claimed. |

The public region-policy version transition remains explicit. Before any actual use, the account holder must establish the policy applicable on that date, their location/entity scope and permitted collaborators. The project’s actual jurisdiction remains Unknown. No new native dependency is invented; the owning issue identifies no hard prerequisite to completing this research.

## Terms, usefulness and operating boundaries

| Topic | Evidence and consequence |
| --- | --- |
| API rights and independence | A3 assigns output rights as between the parties, disclaims training on customer content, requires authority to bind an entity, and restricts competing-service/model development and reverse engineering. Output accuracy still needs evaluation. This proposed evaluation is not a competing-model training plan; that distinction is a research inference, not provider permission. |
| Publicity and publication | A3 permits customer-name/logo identification with an opt-out route and asks good-faith consideration of marketing requests. It establishes no general project endorsement. Program-specific acknowledgment, embargo, publication review, reporting and renewal terms remain **Unknown** pending the actual offer. Reject editorial influence over methodology or unfavorable findings as an internal project condition. |
| Credit expiry and overage | A4 makes credits noncash, nonrefundable and nontransferable. Purchased credits generally expire after one year; promotional credits expire as specified when issued, otherwise after one year. Account closure forfeits credits. Optional automatic reload can charge a payment method. The actual research-credit classification, issue date, expiry, balance and reload state are unverified. |
| API data and retention | A5 describes ordinary deletion within 30 days, with service, agreement, policy-enforcement and legal exceptions. Files, feedback and covered models can differ; flagged data can be retained longer. No zero-retention agreement or settings are established. A6's handling of contact/proposal data is not the API customer-content rule. |
| Scope and service continuity | A1 and A2 do not promise a service-level guarantee or fixed model/rate allocation; lower-priority capacity may affect availability. A3 permits suspension/termination under stated conditions. Record these differences in experiments and retain local permitted original inputs/results; credits and account entitlement are not portable. |
| Separate subscription route | A9 offers selected OSS contributors six months of Claude Max 20x, with specific end-of-benefit subscription behavior. That is separate from researcher API credit. This assessment changes no subscription or OSS eligibility record. |

For policy handling, the planned benign protocol should remain inside applicable ordinary-use rules. The inspected prior usage policy includes intellectual-property and unauthorized-access prohibitions; the announced November policy is a separate future observation. A research label does not authorize prohibited prompts or make policy exceptions automatic.

## Valuation, effort and next decision

Keep cash value, estimated avoided cost, every scoring factor and total **null**. A headline allocation has no proved useful value without an approved applicant, eligible service, sufficiently useful capacity and real demand. Proposed avoided-cost method: sum only eligible requests actually needed and used before expiry at the applicable input/output rates, bounded by usable awarded credit, then subtract onboarding, paid fallback and maintenance. Do not count labor or purchases the project would not otherwise undertake as realized savings.

Planning effort consists of original-case preparation, independent scoring review, an account/terms decision, bounded pilot, execution and published analysis. Estimate hours only from observed preparation and pilot work; no staff assignment, recurring effort or funded work has been established. Existing repository tests and synthetic fixtures remain useful without provider credit and are not empirical model evidence.

Before considering an application, establish a responsible investigator, documented research expertise and public profile; confirm the specific safety question and valid regional/account route; determine publication, expiry, classification, data and service-priority terms; and adopt an affordable stopping rule. The unsent research question is: **Does evidence-aware prompting reduce unsupported certainty while preserving useful answers on a preregistered corpus of original technical scenarios?** A provider would need to judge that question’s priority. No application draft contains fabricated affiliations or a promised result.

## Review and acceptance

This is the canonical program/intake assessment for #40, with its unique structured record, pipeline and source memberships. [Independent findings review 5571407286](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/93#pullrequestreview-5571407286), submitted on 2026-10-19 at 12:17:48 UTC, accepts all thirteen literal criteria at exact source `1fab45ebe2051b599d823f5e2d1e1fc00b476d74` / tree `8aa9cda4e001d12829c1c3a0d549f28075ed99c4`. The independently performed Research review and complementary Apple source/form review are explicitly attributed in that public COMMENT. This establishes **Done / Verified** for the canonical program/intake research under the pipeline definition. Actual applicant eligibility, institutional/provider agreement, financial value and account behavior remain Unknown; research acceptance does not establish application, award, spending, activation or empirical results. Final metadata/integration review, normal merge and distinct accepted-main validation remain delivery steps in the PR; the findings receipt is not relabeled as a review or execution of a later revision.
