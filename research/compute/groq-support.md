# Groq — conditional free-plan evaluation and separate support discovery

Canonical issue: [E05-01E / #43](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/43)

Canonical record: `GROQ-FREE-PLAN` in the [opportunity register](../../data/opportunities.json)

Sources inspected: **2026-10-19**

Status: **Source-backed assessment; independent findings acceptance pending**

Groq is a trademark of Groq LLC and/or its affiliates. This independently prepared
assessment is not affiliated with or endorsed by Groq, and no sponsorship is
claimed. [S13]

## Recommended disposition

Retain **P2: conditional small evaluation option; defer activation and publication**.
The public allowance could support a bounded interface and evidence-capture check
using wholly authored synthetic inputs. It is neither cash nor an awarded grant,
reserved capacity, a research allocation, or proof of usable savings. No Groq
account, agreement, application, payment method, API call, model run, benchmark,
provider contact, or activation was performed for this assessment.

Two gates matter before any later use. First, determine the actual customer,
applicable agreement and permitted scope: the current Services Agreement's
restriction on developing or improving similar or competing offerings needs
specific review for an AI planning/evaluation project. Second, confirm the
account's actual free-plan model entitlement and quotas. A published model alias
and a documentation table do not establish either gate. The service-specific
terms link also redirected to website terms during this review. Do not treat
that different document as the missing service terms. [S1, S4–S6]

Keep **formal support discovery separate**. Groq and NSF document a NAIRR pilot
contribution, but the current intake, available capacity, applicant conditions
and deadline were not established here. The observed portal access failure is
retained below. This is a qualified lead for the parent
[compute assessment #38](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/38),
not a second award record or a direct Groq sponsorship application. [S15–S17]

## Current offer, intake and historical distinctions

| Question | Evidence-backed assessment |
| --- | --- |
| Benefit type | Public rate-limited API service allowance; no cash amount or awarded credits. The existing stable record remains `GROQ-FREE-PLAN`. [S1–S2] |
| Entry point | The public console redirected to `/home` and displayed sign-in/continuation terms. No authenticated account, registration fields or private offer was inspected. [S3] |
| Application state | A service entry point is available; a complete direct research-grant or OSS-sponsorship intake was not verified in the bounded search. This is not a claim that none exists. |
| Deadline | No dated submission round was found for ordinary free-plan entry. `verified_deadline`, time and timezone stay null; this means no verified deadline, not a guaranteed perpetual offer. NAIRR's current deadline is Unknown. |
| Payment boundary | The documented Developer upgrade requires a payment method and introduces usage billing. Do not add a card or select a paid tier under this plan. The actual account tier and historic commitments remain Unknown. [S2] |
| Model choice | The current catalog lists `openai/gpt-oss-20b` and `openai/gpt-oss-120b` as Production. Model-specific entitlement and terms still require review. The provider's hosted implementation claims are not an independently measured identity or performance result. [S9–S11] |
| Historical model changes | Free/developer access to `llama-3.1-8b-instant` and `llama-3.3-70b-versatile` ended on 2026-08-16; committed-spend enterprise customers were excepted. Do not reuse their historical free-tier quota assumptions. [S12] |
| Continuity | Deprecation may require migration, and some aliases may be automatically upgraded. Freeze actual response identity and stop on a changed/retired model rather than silently comparing a replacement. [S12] |

### Published limits and the unresolved plan-label ambiguity

The retrieved rate-limit page contains both **Free Plan Limits** and **Developer
Plan Limits** controls. Its displayed table gives these values, while adjacent
prose calls the limits below base Developer limits. The extracted page does not
establish the active tab. Preserve that conflict; treat these as conservative
**provisional planning ceilings**, not a verified entitlement for a particular
free account. The model catalog's separate Developer limits are not substituted
for the values below. [S1, S9]

| Displayed model | Requests/minute | Requests/day | Tokens/minute | Tokens/day |
| --- | ---: | ---: | ---: | ---: |
| `openai/gpt-oss-20b` | 30 | 1,000 | 8,000 | 200,000 |
| `openai/gpt-oss-120b` | 30 | 1,000 | 8,000 | 200,000 |

The limits are organization-wide, and the first applicable limit wins. Some
organizations have separate input/output token limits. Exact account settings,
other workloads and remaining allowance therefore control admission; do not
multiply allowances through users or organizations. A 429 or unexpected limit
ends the proposed session and preserves the response, including `Retry-After`.
No retry, second account or paid upgrade is part of this plan. [S1, S7]

## Three applicant routes

The accepted [entity baseline](../../docs/nonprofit/entity-baseline.md) leaves the
actual legal entity, jurisdiction, sponsor, tax recognition, account owner and
signing authority unestablished. A GitHub organization is not evidence of those
facts. This assessment applies published conditions to possible routes; it does
not select an entity or give a legal eligibility opinion.

| Route | General service fit | Actual Pick Your AI eligibility and needed evidence |
| --- | --- | --- |
| Current community project | Service terms contemplate an individual or entity customer; nonprofit incorporation is not a stated free-plan prerequisite. | **Unknown / conditional.** Identify the adult customer, country and authority, intended developer/business use, applicable agreements and model terms. Resolve the competing-offerings scope before accepting terms or sending inputs. |
| Fiscal-sponsored project | No public sponsorship-specific entitlement or exception was established. | **Unknown.** Identify which party contracts, owns the account/data and bears obligations; obtain the actual sponsor arrangement and provider applicability decision. A sponsor's status cannot transfer eligibility by assumption. |
| Independent 501(c)(3) | Recognition does not itself create an allocation or exempt service restrictions. | **Unknown / conditional.** Verify the real entity, authority, location and use. Recognition alone does not answer account, model, privacy, export or scope requirements. |

The Services Agreement requires an adult customer and authorized use, covers
developer/business rather than consumer use, and restricts competing offerings
in §6.3(e). Model terms apply separately. The legal framework warns that an
existing offline agreement may govern. These are reasons to inspect the actual
agreement and intended use, not to assert that this project is eligible or
ineligible without those facts. [S4–S6]

## Obligations, independence and exit

| Area | Current finding and decision consequence |
| --- | --- |
| Permitted use and input rights | Review the actual service/model terms and AUP for the exact workload. Use only wholly authored benign synthetic material in the proposed plan. Public availability of third-party text is not a redistribution or provider-processing license. [S5, S7] |
| Data handling | Groq documents request metadata retention and conditional input/output retention, including reliability/abuse exceptions of up to 30 days unless legally extended. ZDR is documented as available to customers, with feature tradeoffs; no account setting was verified. Retained customer data is described as stored in US GCP buckets, not proof of every inference location. [S8] |
| Training | The agreement states a customer-permission/instruction boundary for training on customer data. This is a published contractual statement, not an independent audit of the service or an account-specific promise. [S5] |
| Publication | Benchmark-publication permission was not affirmatively established. No matching benchmark clause in the inspected agreement is not permission. Keep performance comparisons unpublished until scope, model rights, confidentiality and actual terms are resolved. Record observations honestly and preserve adverse results. |
| Branding and sponsor influence | Nominative word use requires attribution; truthful comparisons need a clear nearby nonaffiliation disclaimer. Logos require permission. Do not imply endorsement, sponsorship or an award. Keep methodology, rankings and negative findings independent of support; any eventual benefit needs a factual disclosure. [S13] |
| Reporting and renewal | No grant reporting calendar, fixed award term or renewal process was verified for this public allowance. Read any actual support offer before acceptance; no absence-of-obligations claim follows from a missing offer. |
| Overage | The plan has no payment method addition or paid fallback. Unexpected billing or an upgraded account is a stop condition. Applicable private orders and existing account obligations remain Unknown. [S2, S4] |
| Portability | Keep provider-neutral inputs, expected structures, exact configuration, hashes and failure records. Hosted aliases do not pin weights, serving numerics or a recoverable service implementation. Preserve unsupported/unknown identity instead of inventing a comparable snapshot. [S9–S12] |
| Retention and exit | Maintain the project's own rights-compatible evidence; minimize personal/account identifiers. Before actual use, settle deletion/export and post-termination obligations in the applicable agreement. No perpetual free capacity, output availability or service continuity is assumed. |

The [sponsorship ethics draft](../../docs/sponsorship-ethics-draft.md) and
[workflow controls](../../docs/workflow-and-authorization.md) remain proposals
where their own status says so. This note does not appoint a signer, data owner,
reviewer, account administrator or grant recipient.

## Bounded evaluation design — not executed

The [needs assessment](../../docs/needs-assessment.md) relates inference access
to source-aware configuration/evaluation work in
[Research #36](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/36)
and [Research #41](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/41).
The concrete proposed use is a small request/response and evidence-capture smoke
check: can the selected hosted aliases produce short responses that a future
adapter can record without losing identity, malformed results or failures?
Its public benefit would be a reproducible account of integration limitations
for people assessing AI stacks. It is not a model-quality ranking, load test,
context-capacity test, empirical calibration, or fulfillment of another issue's
hardware, dataset, statistical or receiving-owner criterion.

### Admission before a later run

1. An actually authorized account owner confirms customer identity, applicable
   terms, country, model rights, publication scope and independent data handling.
   Resolve §6.3(e) and the service-specific-terms redirect with the appropriate
   qualified decision or provider clarification. No outreach is performed here.
2. Read the actual free account's allowed models, daily/minute/input/output
   ceilings, remaining budget, tier and other organization use. Document the
   current source/model dates. No model or trial activation is implied by this
   source assessment.
3. Freeze the complete authored prompt set, expected response structures, exact
   request parameters, tokenizer/version and input token accounting, including
   all message/template overhead. Confirm that the completion bound covers all
   generated reasoning as well as visible output; the chat reference does not
   separately spell out that accounting boundary. If it cannot be established,
   leave this plan unexecuted rather than treating the arithmetic as a hard cap.
4. Record who will retain evidence, review adverse results and decide whether
   further work is justified. No person or schedule is assigned by this note.

### Proposed workload and stop rules

| Design item | Fixed proposal |
| --- | --- |
| Inputs | Six wholly authored benign task families: scalar extraction, small JSON formatting, explicit unknown-field handling, unit-label preservation, source-label preservation and a short explanation. No private user data, scraped catalog or externally licensed benchmark corpus. |
| Models and attempts | The two Production aliases above; ten attempts per family per model: **6 × 10 × 2 = 120 total attempts**, 60 per model. Failed attempts consume the same budget; no replacement run. |
| Token envelope | At most **512 input tokens** including overhead and requested **128 generated tokens** per attempt. Conditional on the verified accounting gate: **640 per attempt; 38,400 per model; 76,800 in total**. These are design calculations, not measured consumption. |
| Pacing | Concurrency one, at least 30 seconds between request starts, at most two starts in any rolling minute across both models. The ideal 120-attempt window is about an hour; timeouts, quota stops or unavailable models can end it sooner. No completion-time promise. |
| Parameters | One completion, non-streaming text, `reasoning_effort=low`, explicit token cap; no tools, search, code execution, files, batches, fine-tuning or automatic fallback. Pin all other accepted parameters in the eventual manifest. [S14] |
| Admission per request | Reserve the full ceiling before starting. Stop before a request would exceed the stricter actual organization/day/minute/input/output budget. Preserve the whole run's daily allowance; do not rely on a midnight reset. |
| Failure handling | Stop on 429, authorization/tier changes, missing token accounting, unexpected billing, unsafe/unlicensed content, changed model identity or an unbounded request. Record timeout and malformed/truncated outputs as outcomes; do not expand token caps to improve results. |
| Evidence | Preserve the authored manifest and SHA-256, request ID/time, actual alias/fingerprint when available, client/config versions, recorded usage, response/error and rights-compatible raw hash, quota headers and stop reason. Unknown backend revision stays Unknown. Never store credentials. |
| Review and exit | Compare only the predefined shape/identity outcomes. A small or truncated result set cannot support broad quality claims. Complete a source/rights review before releasing even a narrow comparison; archive evidence and close the session without paid continuation. |

The deliberately small completion cap may yield truncation or no usable visible
answer on a reasoning model. That is a recorded limitation of this proposed
smoke check, not evidence of a model defect. The public API describes supported
reasoning effort and warns that deterministic reproduction is not guaranteed.
No hidden-reasoning capture or inference of a precise serving revision is needed
for this plan. [S14]

## Formal support discovery

Groq's **2024-05-06** announcement describes its NAIRR pilot participation.
The current NSF NAIRR page retains a Groq contribution of access for up to ten
research teams inside a section expressly describing **pilot commitments**.
This establishes a historical provider/resource lead, not ten currently vacant
places, a current award, a direct open Groq grant or project eligibility.
The linked NAIRR portal returned a robots access block during this review;
no form or account was inspected and no alternate access route was attempted.
[S15–S17]

The next discovery question is whether the current NAIRR intake has an applicable
Groq resource and accepts the actual project's investigator, institution,
jurisdiction and proposed use. Intake deadline/timezone, capacity, eligibility,
review criteria, reporting, publication, data handling, attribution and renewal
are all **Unknown** until current governing evidence is obtained. A fiscal
sponsor or 501(c)(3) cannot be presumed to satisfy those conditions.

The bounded search covered current official Groq documentation, legal and
program/news pages, current NSF NAIRR material, the known console entry point,
and the repository/organization's Groq issue and PR matches. The only matching
research owner was #43, with parent #38 and epic #6; no Groq PR duplicate was
found before the 11:11 UTC claim. `groq.com/community/` redirected to the home
page. These observations limit the search; they do not establish the worldwide
absence of a support program. Preserve this lead here until current evidence
supports a distinct program record and duplicate review. [S18]

## Value, effort and prioritization

| Scoring factor | Treatment under the existing rubric |
| --- | --- |
| Mission fit, 20% | Plausible bounded integration use identified above; receiving work and actual demand remain uncommitted. Rating null. |
| Eligibility, 20% | Actual customer, applicable terms and scope unresolved; hard gate. Rating null. |
| Net usable value, 15% | No actual covered workload, existing entitlement or purchase displacement demonstrated. Rating null. |
| Likelihood evidence, 10% | Public entry point is not an acceptance probability; NAIRR intake unknown. Rating null. |
| Timing, 10% | No verified application deadline or approved internal run date. Rating null. |
| Effort, 10% | Terms/account review, prompt/token accounting, evidence capture and review/exit are real work; no measured estimate or assigned capacity. Rating null. |
| Independence risk, 10% | Competing-use/publication and branding terms need resolution; no sponsor influence accepted. Rating null. |
| Strategic value, 5% | A portable small integration check may help; it establishes no durable compute supply. Rating null. |

Keep weighted total, currency, usable value and realized avoided cost **null**.
The free allowance has no demonstrated cash receipt or displaced purchase.
A future estimate must subtract uncovered usage, integration, terms/privacy
review, maintenance, evidence retention and exit cost from an evidenced eligible
workload, under the [budget rules](../../docs/budget-assumptions.md). Do not price
the proposed token budget at paid rates and call the result funding acquired.

**P2** is a qualitative research priority, not an application rank or urgency
created by a guessed deadline. Current stage stays **Discovered** and applicant
qualification **Unknown** until actual independent assessment acceptance and
the separate lifecycle conditions are recorded. No Qualified, Approved to apply,
Submitted, Awarded or Activated transition is made by this draft.

## Source ledger and recheck rules

All access observations below are from **2026-10-19**. Dates embedded in the
sources are separate historical facts. Links are primary provider/government
evidence; only short factual paraphrases are retained, not a copied provider
catalog or a private form.

| ID | Primary source | Observation and scope |
| --- | --- | --- |
| S1 | [Rate limits](https://console.groq.com/docs/rate-limits) | Organization/model limits; displayed table and plan-label conflict retained. Actual account limits not read. |
| S2 | [Billing FAQ](https://console.groq.com/docs/billing-faqs) | Public free/developer upgrade and billing boundary; no private account checked. |
| S3 | [Console entry](https://console.groq.com) | Redirected to public `/home`; sign-in/continuation surface only. No registration or form completion. |
| S4 | [Contractual framework](https://console.groq.com/docs/legal/contractual-framework-overview) | Current public framework, including possible existing offline agreements. |
| S5 | [Services Agreement](https://console.groq.com/docs/legal/services-agreement) | Last modified 2026-06-22; inspected use, customer/model/data and scope provisions. Actual applicability remains unverified. |
| S6 | [Legal index](https://console.groq.com/docs/legal) and [service-specific link](https://groq.com/groq-service-specific-terms) | Linked service-specific URL redirected to [website terms](https://groq.com/terms-of-use); a distinct current service-specific document was not obtained. |
| S7 | [Acceptable Use Policy](https://console.groq.com/docs/legal/ai-policy) | Effective 2025-10-15; permitted use and quota protections. No project compliance certification. |
| S8 | [Your Data](https://console.groq.com/docs/your-data) | Published retention/ZDR and storage statements; no account setting or independent service audit. |
| S9 | [Model catalog](https://console.groq.com/docs/models) | Current Production/Preview distinctions and hosted aliases; no actual entitlement or measurement. |
| S10 | [GPT-OSS 20B](https://console.groq.com/docs/model/openai/gpt-oss-20b) | Vendor model/hosting description, separately from actual usage. |
| S11 | [GPT-OSS 120B](https://console.groq.com/docs/model/openai/gpt-oss-120b) | Same bounded model-specific scope; no weight/license acceptance inferred. |
| S12 | [Deprecations](https://console.groq.com/docs/deprecations) | Current lifecycle and dated historical access changes. |
| S13 | [Trademark policy](https://groq.com/trademark-policy) | Effective 2025-10-24; truthful references versus logos/endorsement. |
| S14 | [API reference](https://console.groq.com/docs/api-reference) | Chat fields, effort and generated-token cap; explicit hidden-reasoning accounting still a preflight question. No API invocation. |
| S15 | [Groq NAIRR announcement](https://groq.com/newsroom/groq-is-selected-to-provide-access-to-worlds-fastest-ai-inference-engine-for-the-national-ai-research-resource-nairr-pilot) | Historical 2024-05-06 announcement, not current intake evidence. |
| S16 | [NSF NAIRR](https://www.nsf.gov/focus-areas/si/nairr) | Current page preserving pilot contribution description; current Groq allocation/intake unverified. |
| S17 | [NAIRR portal](https://nairrpilot.org/) | Attempt blocked by robots; successful verification date stays null. No form, deadline or account inspected. |
| S18 | [Groq community path](https://groq.com/community/) | Redirected to homepage; no application route established from the redirect. |

Recheck at the existing monthly research review and before any reliance,
registration, agreement, run, publication or application; also on a changed
catalog/quota, redirect, terms conflict, billing change, NAIRR intake update or
account/entity decision. No new scheduled loop or internal date is created.

## Acceptance and handoff

This assessment supplies the canonical note, current/historical source ledger,
three-route analysis, bounded unexecuted plan, formal-support discovery result,
restrictions, null-value/scoring rationale and disposition required by #43.
The corresponding opportunity/pipeline/freshness changes belong to this same
record. All other programs, owners and actual applicant facts remain separate.

An independent reviewer must accept the **actual findings at an exact source
revision**, including the documented unknowns and conditional disposition,
before the research acceptance criteria are checked. Record that real review
and its scope in the canonical issue/record; a passing link/schema check alone
does not satisfy it. This draft does not claim that acceptance has occurred.
Research acceptance may complete #43 while account eligibility, any experiment,
application, award and activation remain unperformed and unestablished.
