# Opportunity evidence register

This register contains **42 distinct program/channel records**: 14 nonprofit and funding records and 28 compute, software, hardware and professional-service records. The records distinguish seed evidence from individually accepted research findings. Published source facts have been checked; no record is asserted to be a qualified or authorized application.

The canonical data is [opportunities.json](opportunities.json), with [schema](opportunities.schema.json). Stable `owning_research_key` values connect records to GitHub research work; the original 39 owning issue URLs were matched to the independent live 72-issue snapshot. Three later infrastructure records reuse the separately read existing E06-03 / #53 issue; no additional issue or Project item is inferred from that historical audit. The native workflow has read back the declared 71 parent and 43 blocker relationships, and the persisted Project field audit has passed for all 72 issues. Independent relationship verification and saved view checks are reported in the [execution report](../docs/execution-report.md).

A shared owning key means one comparative research package evaluates different programs. It does not create duplicate provider tasks. Closed programs and scope exclusions are retained so future research does not revive them as current offers. The Cloudflare historical OSS name and Project Alexandria use one record.

## Funding and nonprofit records

| Program | Owning key | Opportunity disposition |
|---|---|---|
| Restack | E03-01 | Not Pursuing for ordinary AI-builder scope |
| CodeSupply | E03-01 | Research; blocked from application pending scope, contributor and authority evidence |
| NGI Zero Commons Fund | E03-01 | Not Pursuing — closed |
| Secure Open Source Fund | E03-02 | Rolling applications documented; no application submitted in this execution |
| Sponsors for organizations | E04-01 | Organization onboarding route documented; existing account state Unknown |
| Member-project fiscal sponsorship | E01-04 | Rolling inquiry/application process; acceptance may take months |
| Associated project fiscal hosting | E01-04 | Application process documented; PYA acceptance/relationship Unknown |
| Fiscal hosting for open-source projects | E01-04 | Application/validation route documented; no acceptance claimed |
| Google for Nonprofits — United States | E03-07 | Eligibility route documented; no qualified applicant established |
| Sovereign Tech Fund | E03-03 | Not Pursuing for ordinary builder scope; research only for a real foundational component |
| Open Source in Science | E03-03 | Program LOI route documented; no current special open call |
| PESOSE (NSF 26-506) | E03-06 | Active solicitation; PYA applicant route not qualified |
| Small Research Grants on Education | E03-05 | Watch for a verified reopening; do not apply |
| Causes Portal / workplace giving channel | E04-04 | Nonprofit registration route documented; applicant validation Unknown |

## How to interpret fields

- `source_review_status` describes source consistency. `applicant_qualification_status` and the three eligibility-phase fields describe unresolved or conditional applicant gates.
- `work_status` belongs to the owning research issue. `opportunity_stage`, `current_disposition`, `application_outcome`, `award_status`, `activation_status` and `reporting_status` describe different decisions or evidence.
- `priority` is a justified research/record priority. A closed opportunity can have a lower priority than the broader package containing it. Every numeric component of `scoring` remains null until actual eligibility, effort and net-value facts exist.
- `required_application_evidence` contains only explicit published requirements captured so far. It is incomplete unless the record explicitly says otherwise. `internal_application_review_controls` are our own review needs.
- External deadlines are source-backed and timezone-specific. No internal due dates or named contributors are assigned.
- Headline dollars, euros, credits, service access and volunteer time are not added together as realized support. Currency remains unknown when the reviewed source did not establish it separately.

## Template, citations and lifecycle

Use [the fill-in record template](../templates/opportunity-record.json). It intentionally starts with unresolved values and is not a publishable opportunity as-is. Before adding a record, fill every schema-required property, including the existing owning research key, at least one official `source_urls` entry, `source_review_status`, the program identity and a justified priority; remove `template_only`. Preserve unknown applicant facts instead of manufacturing eligibility or scores.

`source_refs` contains durable official URLs, not browser-session identifiers or positional claim indices. Distinct application and registration endpoints are tracked by the freshness register, including unresolved access attempts. Identifying a link does not verify its current form contents.

Source facts checked does not mean the canonical program/intake assessment has received independent acceptance. Seed records retain Discovered under the clarified [transition rules](../docs/operations-and-reporting.md); individually accepted assessments record their own actual lifecycle evidence. The [Fireworks startup exclusion](../research/compute/fireworks-support.md) has independently accepted bounded findings and completed research, while preserving its historical stage after the failed applicant gate and its Not Pursuing disposition. Other records retain their individual accepted or unresolved research/review states. Verified, Qualified and externally authorized actions have separate evidence requirements.

## Additional infrastructure comparison

The [E06-03 comparison](../research/infrastructure/additional-programs.md) updates Fastly and adds distinct Netlify OSS, Buildkite OSS-pricing and historical DigitalOcean OSS-credit records under existing [#53](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/53). Azure retains its separate accepted record without modification. The complete comparison is In Review; earlier bounded source checks do not establish its independent acceptance. It preserves current hosting/public CI, explicit applicant and intake Unknowns, null values/scores and a separate disposition for each candidate. The historical DigitalOcean route is retained without asserting provider-wide closure.
