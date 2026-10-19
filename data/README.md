# Opportunity evidence register

This register contains **44 distinct program/channel records**: the original 41 identities, two explicit loan/equity mechanism screenings and the distinct Sloan New Media screen. The records distinguish seed evidence from individually accepted research findings. Records carry dated source observations and explicit access limits; no record is asserted to be a qualified or authorized application.

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
| [New Media](../docs/research/education-accessibility-funding-screen.md) | E03-05 | Done / Verified public findings; conditional fit, actual grantee and invitation Unknown |
| Causes Portal / workplace giving channel | E04-04 | Nonprofit registration route documented; applicant validation Unknown |
| SBA 7(a) business loans | E03-08 | Completed nonbinding screen; Not Pursuing as present charitable project funding; no borrowing commitment |
| YC standard investment deal | E03-08 | Completed nonbinding screen; Not Pursuing for the current charitable-funding shortlist; no investment or issuance |

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

## Award mechanism findings accepted

The [mechanism matrix](../docs/funding/award-mechanisms-and-restrictions.md) has [actual independent findings acceptance](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/115#pullrequestreview-5575474352) for all thirteen issue #32 criteria at 5302c991db1087383f282663f7315f42d7054522. Its fourteen original `award_mechanism_screen` values remain byte-exact; their original Pending review objects are historical. A separate `award_mechanism_review` records the later scoped acceptance without changing existing program-owner workflow or findings. The two unique financing screens are Done research, retain historical Discovered stages, P3 and nonbinding Not Pursuing decisions, and preserve their original review/status history.

In the earlier receiving snapshot, the accepted-main input was af922c0f61cb2a499f4206249ff2d079756f6bdd. At that revision, all 41 identities, every original field and all previous source-array members were preserved; only the three GSoC/Sloan source additions and the two scoped fields on fourteen records were additive. The other 27 records then remained byte-exact. The original 39-owner relationship/Project audit above and the initial85 source-preservation snapshot are historical; neither is refreshed by this composition. Actual eligibility, value, recipient, authority, instrument and operating gates remain separate.

## Education and accessibility screen

The [#29 screen](../docs/research/education-accessibility-funding-screen.md) updates the existing Spencer program and adds distinct Sloan New Media. At reviewed source 9dcd1d1e80a2037c0f5db7ab9d861132a4ac1ea2, both findings awaited independent acceptance; Spencer remained closed/P3 and New Media P2 with no actual applicant, invitation, study, award or value. The complete earlier db07 Spencer observation remains in its dated namespace. The original source preparation at 95a26ed722e8bd1bd0b3ad1b30db934f894b5b60 preserved all 40 other db07 opportunity objects exactly and did not yet contain the later E03-08 fields.

This receiving composition uses signed main bfa30ca5754e2068b06f7ff5fbf846cb39c6972b. All 42 other main opportunity objects retain their raw bytes and order, including the accepted HF record, the other thirteen E03-08 screens, their separate acceptance fields and the two financing records. Spencer keeps its exact current E03-08 screen and acceptance fields alongside the education findings; neither scope replaces the other. Sloan Open Source in Science and NSF retain their separate owners and current source additions. The current total is 44 records. The original issue/Project audits remain historical; New Media shares #29 and creates no new issue or Project field.

The [actual #29 findings acceptance](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/29#issuecomment-6275510717) now supports Done research for both records. Spencer retains historical Discovered/P3 watch because intake is closed; Sloan New Media is Verified/P2 for its accepted public program assessment. Current counts are **44 records: 29 Discovered / 15 Verified**. The original review/status values remain in each record's dated metadata history; all source, applicant, invitation and action limits remain. Ordinary source delivery and issue reconciliation are separate from this source-only acceptance continuation.
