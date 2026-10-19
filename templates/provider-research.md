# Provider research record

Opportunity ID: [stable ID]  
Provider / specific program / round: [exact identity and aliases]  
Canonical issue: [GitHub URL]  
Research state / opportunity stage / application gate: [separate values]  
Researcher / independent reviewer: [actual identities or Unassigned]

## Decision and project fit

Which specific support could address which evidenced need? Link receiving repository/issues and describe one independently reviewable public-benefit output. Record existing capabilities and why incremental support is useful.

## Duplicate search

Record searched provider/program aliases, existing issue/register matches and date. If extending prior research, preserve its identity, old rounds and outcomes.

1. Search provider and specific program names, aliases and previous rounds in the [opportunity register](../data/opportunities.json), repository issues and organization issues. Record the actual search scope, date and matches; a search not performed is still unknown.
2. Reuse the stable opportunity ID and owning issue for the same program. A renamed program or repeat round is not automatically a new opportunity. Preserve earlier outcomes and source dates; use a separate record only when the independently reviewable research outcome is genuinely distinct, as described in the [method](../docs/research-methodology.md).
3. Resolve possible duplicates before creating a live record. A missing search result is not evidence that a provider or program does not exist.

## Sources and program status

| Claim | Official URL and publisher | Round/version and scope | Actual access date/result | Evidence description | Finding / limitation |
| --- | --- | --- | --- | --- | --- |
| Program exists | | | | | |
| Applications open/closed/rolling/invitation-only/unknown | | | | | |
| Applicant/eligibility terms | | | | | |
| Benefit and restrictions | | | | | |
| Application process and deadline | | | | | |

Distinguish primary/public documentation, vendor assertions, independent evidence with its method, and estimates with their assumptions. These are evidence descriptions, not a new verification scale. Identify historical rounds, failed access and conflicting terms explicitly. The date this Markdown file was edited is not a source-access date.

## Eligibility by route

| Route | Assessment | Governing evidence | Missing condition and native dependency |
| --- | --- | --- | --- |
| Current project | Unknown | | |
| Fiscal-sponsored | Unknown | | |
| Independent 501(c)(3) | Unknown | | |

Record actual jurisdiction, legal entity, recognition, account, revenue/traction, license and other requirements. Fiscal sponsorship does not imply program admission.

## Benefit and obligations

Support type; amount/capacity; currency; estimated usable value and method; rate limits/quotas; expiry; region/model/account restrictions; privacy; benchmark/publication rights; attribution; exclusivity; reporting; renewal; overage; maintenance/custody/return; portability and exit plan. Unknown is valid. Do not substitute maximum advertised value for actual use.

## Recommendation and review

Eligibility gate; factor ratings/evidence and score if defensible; priority/rationale; next research action; required decision; proposed authorization scope; independent review record. Record dates only when sourced or explicitly selected as internal actions.

## Acceptance

The owning issue's concrete deliverable, criteria and definition of done govern completion. Reviewer records exact revision, reviewed sources, accepted findings, unresolved questions and affected-owner handoff. Research completion is separate from submission, award and activation.

## From the desk note to a structured record

Start with the [JSON template](opportunity-record.json), following the [register guidance](../data/README.md) and [schema](../data/opportunities.schema.json). Keep incomplete work as a clearly marked draft outside the live register when required identity, source, owning key or justified priority is missing. Do not fill these gaps with a fictional URL, issue, score or date merely to pass validation. Unknowns in the note map to explicit `null`, `Not Verified` or `Unknown` values where the field permits them, with the reason preserved in the note.

| Desk-note information | Structured fields and treatment |
| --- | --- |
| Provider, specific program, aliases, round and canonical issue | `opportunity_id`, `provider`, `program_name`, `program_aliases`, `round`, `owning_research_key`, `linked_github_research_issue`; reuse the canonical identity after duplicate search. |
| Search actually performed | `duplicate_search.searched_at`, `aliases_checked`, `canonical_match`; describe scope and unresolved matches in the note. Null/empty search fields mean not established, not no duplicate. |
| Official program and application endpoints | `official_program_url`, `official_application_url`, `source_urls`, `source_refs`; use durable URLs. An unknown application endpoint can remain null; identifying a link is not inspecting its form. |
| Source-access date, scope, evidence description and limitations | `sources` entries retain the actual source dates and claim scope; `last_verified` and `source_review_status` must not imply a later source check or independent acceptance. Keep per-claim details in the linked note. |
| Current intake and all three eligibility routes | `application_status`, `available_before_incorporation`, `available_through_fiscal_sponsorship`, `available_after_501c3_recognition`, `eligibility_status`, `eligibility_jurisdiction`, `legal_entity_requirements`, `eligibility_conditions`; assess each route independently. |
| Deadline and usable benefit | `verified_deadline`, `deadline_timezone`, `deadline_source_url`, `benefit_amount_or_capacity`, `currency`, `estimated_usable_value`, `valuation_method`; unknown numbers/dates stay null, not zero or a guessed date. |
| Need, obligations and missing evidence | `fit_with_pick_your_ai`, `restrictions_and_obligations`, `required_application_evidence`, `required_contacts_or_decisions`; link the evidenced receiving need. Empty lists mean nothing established yet unless completeness is explicitly supported. |
| Research disposition and next action | `work_status`, `opportunity_stage`, `priority`, `scoring`, `next_action`, `next_action_date`; explain priority independently of an unscored opportunity. Assign a date only from verified terms or an explicit internal scheduling decision. |
| People, acceptance and external-action gates | `assigned_owner`, `independent_reviewer`, `review`, `application_gate`, `application_outcome`, `award_evidence`, `activation_status`, `activation_evidence`, `reporting_status`, `reporting_obligations`; source checking, schema success and a draft do not assign people or authorize an action. |

Use the [outreach draft](outreach-draft.md) only to prepare an unsent request. Keep recipient, representation, evidence, commitments and exact-text approval unresolved until established under the [authorization workflow](../docs/workflow-and-authorization.md). An empty obligations list does not establish that an offer has no obligations.

The [synthetic worked example](examples/provider-research-worked-example.md) and its [JSON fixture](examples/opportunity-record.synthetic.json) demonstrate this mapping without provider research or outreach. Never copy their synthetic identity, priority or URLs into the live registers. For a real record, remove `template_only` only after completing the required fields with justified facts; update the pipeline projection and freshness URL membership together. Run the [local checks](../CONTRIBUTING.md#local-validation) before requesting review. Use partial issue references until the owning issue's complete acceptance criteria and required handoffs have actually been met.

## Current workflow review

The [dated intake workflow review](../docs/provider-intake-review.md) maps this
canonical template and its worked example to all 13 original E09-01 criteria.
It records the exact reviewed source and current canonical requirement basis,
including the unavailable separate original brief. Final independent acceptance
and delivery remain linked through the owning issue; this navigation link grants
no provider eligibility, source-use permission or authority to send a request.
