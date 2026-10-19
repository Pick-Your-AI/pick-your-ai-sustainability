# Opportunity evidence register

This register contains **41 distinct program/channel records**: 14 nonprofit and funding records and 27 compute, software, hardware and professional-service records. The records distinguish seed evidence from individually accepted research findings. Published source facts have been checked; no record is asserted to be a qualified or authorized application.

The canonical data is [opportunities.json](opportunities.json), with [schema](opportunities.schema.json). Stable `owning_research_key` values connect records to GitHub research work; the 39 owning issue URLs have been matched to the independent live 72-issue snapshot. The native workflow has read back the declared 71 parent and 43 blocker relationships, and the persisted Project field audit has passed for all 72 issues. Independent relationship verification and saved view checks are reported in the [execution report](../docs/execution-report.md).

A shared owning key means one comparative research package evaluates different programs. It does not create duplicate provider tasks. Closed programs and scope exclusions are retained so future research does not revive them as current offers. The Cloudflare historical OSS name and Project Alexandria use one record.

## Funding and nonprofit records

| Program | Owning key | Opportunity disposition |
|---|---|---|
| Restack | E03-01 | Not Pursuing for ordinary AI-builder scope |
| CodeSupply | E03-01 | Defer application; P2 qualification research only |
| NGI Zero Commons Fund | E03-01 | Not Pursuing — closed |
| Secure Open Source Fund | E03-02 | Defer application; verify maintainer and project fit |
| [Sponsors for organizations](opportunities/github-sponsors.json) | E04-01 | Done / Verified readiness research; actual recipient, authority and payout route Unknown; setup remains on hold |
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

Source facts checked does not mean the canonical program/intake assessment has received independent acceptance. Records awaiting findings acceptance retain Discovered under the clarified [transition rules](../docs/operations-and-reporting.md). The [Fireworks startup exclusion](../research/compute/fireworks-support.md) has independently accepted bounded findings and completed research, while preserving its historical stage after the failed applicant gate and its Not Pursuing disposition. Each record retains its own research/review state and applicant gates. Verified, Qualified and externally authorized actions have separate evidence requirements.

## Hardware partner comparison

The [E06-04 assessment](../research/hardware/partner-shortlist.md) adds two distinct TechSoup RHW and Computer Aid Get Computers records under existing [#54](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/54). They are Done / Verified for program research after [complete independent findings acceptance](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/108#pullrequestreview-5573387399) at `25eb4b8e047e2adb736d6540b4588b1f3a462697`. Both retain actual overall applicant, inventory, custody, offer, value and effort Unknowns; the documented U.S. fiscal-sponsored TechSoup route is explicitly ineligible. Their shared owning issue was separately read; the original 39-record native setup audit does not extend to a new snapshot or Project item. Existing NVIDIA, AMD, Samsung and all other program rows remain unchanged. The memo distinguishes fee-based access, gifts, loans, accounting and donor-tax valuation, and includes an unsent single-station request with care and exit requirements.
