# Synthetic provider-research desk example

This is a fictional, offline teaching fixture for [E09-01 / issue #67](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/67), not research on a real provider. It demonstrates the [provider template](../provider-research.md) and [JSON record](opportunity-record.synthetic.json). No source was accessed, no duplicate search was performed, no person was assigned, and no outreach or application was sent. These statements describe this exercise only, not the history of any real account or provider.

## Exercise inputs and identity

- Opportunity ID: `SYNTHETIC-EXAMPLE-CREDITS`.
- Provider: Synthetic Example Provider; specific program: Synthetic Example Community Credits.
- Alias supplied by the exercise: Synthetic Example Credits; round: Unknown.
- Illustrative program URL: `https://provider.example.invalid/community-credits`. This is a placeholder, not an official source. The actual application endpoint is unknown.
- Illustrative owning key: `E00-00`, which matches the schema syntax but identifies no real research issue. `linked_github_research_issue` remains null. Issue #67 owns this documentation contribution, not a provider opportunity.
- `priority` is `P2` solely as an exercise input to demonstrate a required enum. It is not a recommendation for a real opportunity; every score remains null. A real draft without a justified priority must remain outside the register.
- `template_only` and `synthetic_example` are true. The fixture belongs only in `templates/examples/`, never in the opportunity, funding-pipeline or freshness registers.

The existing schema requires an identity, owning key, program URI, at least one source URL and priority. Synthetic values satisfy those shapes for the test; they establish no corresponding real-world facts. The explicit synthetic marker is example metadata, not a new live-record lifecycle state. Do not replace missing real evidence with the exercise values.

## Decision and project fit

Hypothetical question: could API credits support a small, reproducible evaluator smoke test with public aggregate results? This is a proposed use case only. No receiving issue, demonstrated capacity, demand model, workload size, public output or incremental benefit has been established. `fit_with_pick_your_ai` preserves that limitation. A real intake would link the existing receiving issue and evidence rather than create a duplicate implementation task.

## Duplicate-search desk plan

Before a real intake, search the provider, program, alias and prior rounds in the register, repository issues and organization issues. If the alias matches the same program, extend its stable ID and owning issue rather than create another entry. Preserve closed or ineligible rounds and the original source dates. If identity is uncertain, record the ambiguity for review instead of claiming a new program.

This exercise performs none of those searches: `duplicate_search.searched_at` and `canonical_match` are null, and `aliases_checked` is empty. The supplied alias is a planned search term, not evidence of a completed search or a finding of no duplicates.

## Sources and observed application status

| Claim | Endpoint / publisher | Round and scope | Actual access date / result | Evidence description and finding |
| --- | --- | --- | --- | --- |
| Program exists | Synthetic program URL above; no real publisher | Unknown | null / Not accessed | No evidence; existence unverified |
| Current intake | Application endpoint unknown | Unknown | null / Not accessed | Unknown; no open, closed, rolling or invitation-only state inferred |
| Applicant terms | Unknown | All three routes | null / Not accessed | No evidence; entity and jurisdiction requirements unknown |
| Benefit and restrictions | Unknown | Hypothetical API credits | null / Not accessed | No verified amount, currency, usable value or obligations |
| Application process and deadline | Unknown | Unknown | null / Not accessed | Unknown; no deadline or timezone inferred |

The JSON `source_urls` array contains only the synthetic program URI because the schema requires a nonempty array. `sources` and `source_refs` are empty, `last_verified` is null and `source_review_status` is `Not Verified`. This is not a record of a source-access failure: no access was attempted.

When real evidence exists, distinguish published terms from vendor performance assertions, independent results with method and conditions, and estimates with assumptions. A provider statement would not become independent evidence by copying it into this table. Historical announcements, access failures and conflicting terms would keep their actual dates and limitations.

## Eligibility, value and obligations

| Route | Assessment | Missing evidence |
| --- | --- | --- |
| Present project before incorporation | Not Verified | Current applicant facts and program requirements |
| Fiscal-sponsored project | Not Verified | Actual sponsor relationship and program acceptance of that route |
| Independently recognized 501(c)(3) | Not Verified | Actual recognition and the specific program conditions |

`eligibility_jurisdiction` and `legal_entity_requirements` remain null. Neither incorporation, fiscal sponsorship nor recognition is assumed. No route inherits eligibility from another.

Deadline, timezone, deadline source, benefit amount, currency, estimated usable value and valuation method remain null. Null means unknown, not no deadline, free service or zero benefit. Empty restriction, application-evidence and reporting lists mean no facts established, not that the provider has no requirements. Unknown obligations include privacy, publishing rights, attribution, exclusivity, renewal, overage, portability and exit terms. No offer or agreement has been reviewed.

## Recommendation, next action and review

- Research state: Backlog; opportunity stage: Discovered; application status: Unknown.
- Next action: identify actual official program and intake terms, resolve program identity, and record the governing evidence before assessing applicant eligibility or requesting any action. This is a proposed desk-research step, not a scheduled commitment.
- `next_action_date` and `next_verification_date`: null. No internal date has been selected and no external deadline verified.
- Researcher / independent reviewer: Unassigned. Both JSON identities are null.
- Review decision: Not reviewed. Reviewer, reviewed revision and review URL remain null. The example has no accepted provider findings.
- Application gate: Not authorized. Application outcome and award status: Unknown. Award and activation evidence: null. Activation status: Not activated, within this fictional exercise only.

## Unsent outreach exercise

Outreach status: Draft only; not sent.

Using the [outreach template](../outreach-draft.md), the only proposed question is: “What are the current applicant requirements for this specific program, including any supported fiscal-sponsorship route?”

Recipient/channel: Unknown. Sender identity and permitted representation: Unknown. Approval record: None. No exact message, financial commitment, applicant authority or legal terms have been approved. Do not send this question or visit an application endpoint on the strength of the fixture or its tests. The [authorization workflow](../../docs/workflow-and-authorization.md) still governs any actual action.

## Offline verification and remaining acceptance

From the repository root, after the [validation setup](../../CONTRIBUTING.md#local-validation):

```sh
python -m unittest discover -s tests -p 'test_provider_intake.py' -v
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

The focused tests validate the fixture against the current record schema without relaxing required fields or URI/score checks; preserve the example's unknowns and action gates; and keep its identity and placeholder URLs out of live registers. Those fixed states apply only to this deliberately incomplete example, not to legitimate future progress in real records. The repository validator also checks the example's local links and JSON syntax.

Passing tests establishes structural consistency only. It does not complete #67, establish independent acceptance, research a provider, qualify an applicant or authorize outreach. The owning issue still requires independent review of the actual fields/workflow and links to the exact accepted revision and review.
