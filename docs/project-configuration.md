# GitHub Project configuration and readback

**Draft for review. Actual field values, all nine saved views, the complete editable-field catalog, the required labels and all four milestones are verified.**

[Project](https://github.com/orgs/Pick-Your-AI/projects/7) · [Repository](https://github.com/Pick-Your-AI/pick-your-ai-sustainability) · [Program #1](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/1) · [PR #73](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/73)

## Verified actual fields

The live Project table was reloaded and captured at **2026-10-19 06:55:24 UTC** in five disjoint issue cohorts. All **72 rows**, **1,152 field comparisons**, **504 required blank cells**, and **70 blank deadline cells** passed; no discrepancy remained. The [captured cells](../data/audits/project-field-readback.json) and [validation](../data/audits/project-field-validation.json) are separate from labels and issue-body text.

| Actual field | Compared rows | Interpretation |
|---|---:|---|
| Status | 72 / 72 | Work delivery state; all 72 GitHub issues remain open. |
| Opportunity stage | 72 / 72 | Discovered for 35 opportunity work items; Not applicable for 37 program/epic/foundation items. |
| Priority | 72 / 72 | P1: 37; P2: 32; P3: 3. No P0 unsupported by an urgent viable deadline or serious blocker. |
| Workstream | 72 / 72 | Program or one of the nine declared workstreams. |
| Record type | 72 / 72 | Program: 1; Epic: 9; Foundation: 27; Opportunity: 35. |
| Eligibility phase | 72 / 72 | Unknown: 63; Immediate: 7 internal foundation tasks; 501c3: 2 blocked investigations. |
| Eligibility | 72 / 72 | Not applicable: 37; Unknown: 34; Ineligible: 1. No opportunity is represented as immediately eligible. |
| Effort | 72 / 72 | Unknown until a defensible effort assessment exists. |
| Resource category | 72 / 72 | The single primary resource category; may differ from additional applicable labels. |
| Confidence | 72 / 72 | Not verified means the full research assessment is unaccepted; source-lead access is recorded separately. |
| Support type | 72 / 72 | Cash, Credit, Hardware, Software, Service or Mixed according to actual issue scope. |
| Provider | 72 / 72 | Provider or research subject from the issue scope; not a claimed sponsor relationship. |
| Program | 72 / 72 | Specific program or scoped comparison subject; not a newly asserted award brand. |
| Dependencies and decision blockers | 72 / 72 | Dependency and action-qualification text; does not replace the native graph. |
| Deadline | 72 / 72 | #25: 2026-11-03; #30: 2027-03-02. Other 70 cells blank; exact timezones remain in sourced records. |
| Source verified | 72 / 72 | 2026-10-19 initial source inspection, not acceptance of research or qualification of the applicant. |

The additional blank checks cover Assignees, Currency, Independent reviewer, Estimated value, Score, Next action date and Next verification: 72 blank cells each. Unknown financial or scheduling information is not recorded as zero or invented as a date.

## Verified field catalog and project settings

The settings readback completed at **2026-10-19 07:49:18 UTC**. It contains **23 editable field definitions: 21 custom fields plus GitHub’s native Status and Sub-issues progress settings**. Native Title, Assignees and Parent issue columns are also used in the Project but are not custom fields. All required data types and options are present, every existing single-select value is supported, and the rendered option lists match the parsed catalog. See the [field settings evidence](../data/audits/project-field-catalog-readback.json) and [independent catalog comparison](../data/audits/catalog-validation.json).

The Project is public, uses the requested name and description, and defaults new issues to `Pick-Your-AI/pick-your-ai-sustainability`. Its README separates research acceptance, applicant eligibility, authorization and achieved support.

| Editable field | Actual type | Actual options | Default |
|---|---|---|---|
| Status | Single select | Backlog, Ready, In Progress, In Review, Blocked, Done, Not Pursuing | Backlog |
| Sub-issues progress | Sub-issues progress | Segmented bar; numerical values shown | None |
| Opportunity stage | Single select | Not applicable, Discovered, Verified, Qualified, Preparing, Submitted, Awarded, Declined, Activated, Reporting | None |
| Priority | Single select | P0, P1, P2, P3 | P2 |
| Workstream | Single select | Program, 01 Nonprofit, 02 Readiness, 03 Grants, 04 Sponsorship, 05 Inference, 06 Infrastructure, 07 Tools and security, 08 Partnerships, 09 Operations | Program |
| Record type | Single select | Program, Epic, Foundation, Opportunity | Foundation |
| Eligibility phase | Single select | Immediate, Fiscal sponsor, 501c3, Unknown, Not applicable | None |
| Eligibility | Single select | Eligible, Conditionally eligible, Unknown, Ineligible, Not applicable | None |
| Effort | Single select | S, M, L, Unknown | None |
| Resource category | Single select | Funding, Inference, Hardware, Software, Security, Nonprofit, Sponsorship, Partnership, Operations | None |
| Confidence | Single select | High, Medium, Low, Not verified | None |
| Support type | Single select | Cash, Credit, Hardware, Software, Service, Mixed, Not applicable | None |
| Provider | Text | Not applicable | None |
| Program | Text | Not applicable | None |
| Currency | Text | Not applicable | None |
| Independent reviewer | Text | Not applicable | None |
| Decision blockers | Text | Not applicable | None |
| Estimated usable value | Number | Not applicable | None |
| Score | Number | Not applicable | None |
| Deadline | Date | Not applicable | None |
| Next action | Date | Not applicable | None |
| Source verified | Date | Not applicable | None |
| Next verification | Date | Not applicable | None |

The four nonempty single-select defaults are Status = Backlog, Priority = P2, Workstream = Program and Record type = Foundation. They are starting values for triage; they do not qualify an opportunity, name a contributor or assign a date. All 72 existing issues were populated individually and verified separately. Assignees remains the authoritative native owner field. Independent reviewer is a text field for the actual reviewer/evidence reference and is not a substitute for GitHub approval.

## Status and outcome conventions

Work statuses are Backlog, Ready, In Progress, In Review, Blocked, Done and Not Pursuing. The verified snapshot contains **10 Backlog, 35 Ready, 26 Blocked and one In Review**. No research issue was closed or represented as accepted merely because this program was configured.

Opportunity stages are Discovered, Verified, Qualified, Preparing, Submitted, Awarded, Declined, Activated and Reporting. Program/foundation work uses Not applicable. Under the [transition rules](operations-and-reporting.md), Verified requires an independently accepted program/intake assessment. Checked source facts alone do not move an unfinished seed assessment out of Discovered. Qualification and permission for an external action remain later gates.

The sole In Review item is [Fireworks #46](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/46), whose [canonical exclusion draft](../research/compute/fireworks-support.md) preserves Ineligible and Not Pursuing. It is not an actionable startup-credit application.

## Verified saved views

All nine named views were saved and reloaded, with exact membership confirmed at **2026-10-19 07:42:06 UTC**. They use **Table** layout, no grouping and no displayed hierarchy. Native parent/sub-issue relationships remain present and are exposed through the relevant parent/progress columns. The [saved-view readback](../data/audits/project-view-readback.json) and [comparison results](../data/audits/project-field-validation.json) record the actual filters, issue identities, visible columns and sort settings.

| Saved view | Verified issue count | Sort order | Purpose |
|---|---:|---|---|
| [Overview](https://github.com/orgs/Pick-Your-AI/projects/7/views/1) | 10 | Workstream (ascending) | Program and epics with native progress, priority and workstream. |
| [Research Backlog](https://github.com/orgs/Pick-Your-AI/projects/7/views/2) | 61 | Priority (ascending) | Open research and internal preparation, including all eight provider investigations. |
| [Funding Pipeline](https://github.com/orgs/Pick-Your-AI/projects/7/views/3) | 0 | Priority (ascending) | Qualified/preparing/submitted cash or mixed opportunities that pass eligibility and work-status gates. |
| [In-Kind Support](https://github.com/orgs/Pick-Your-AI/projects/7/views/4) | 24 | Priority (ascending) | Credit, hardware, software, service and mixed research opportunities, excluding confirmed ineligible items. |
| [Nonprofit Readiness](https://github.com/orgs/Pick-Your-AI/projects/7/views/5) | 16 | Priority (ascending) | Formation, fiscal hosting, governance, budget and readiness work. |
| [Deadlines](https://github.com/orgs/Pick-Your-AI/projects/7/views/6) | 2 | Deadline (ascending) | Confirmed dates on or after today; sourced timezone details remain in the owning issue/record. |
| [Ready for Review](https://github.com/orgs/Pick-Your-AI/projects/7/views/7) | 1 | Priority (ascending) | In Review findings awaiting independent acceptance. |
| [Outreach & Applications](https://github.com/orgs/Pick-Your-AI/projects/7/views/8) | 0 | Priority (ascending) | Preparing/submitted work passing the saved eligibility/status filter; action authority is recorded separately. |
| [Awards & Reporting](https://github.com/orgs/Pick-Your-AI/projects/7/views/9) | 0 | Next action (ascending) | Awarded/activated/reporting stages supported by actual evidence. |

Research Backlog membership was collected by scrolling the actual saved table. In-Kind Support and Nonprofit Readiness used the saved base-filter counts plus complete, disjoint UI filter cohorts; their saved base filters were restored and reloaded. The cohorts introduce no extra saved views or changes to issue fields. Empty qualified/outreach/award views are the expected result at this evidence cutoff.

### Visible columns

| Saved view | Actual visible columns |
|---|---|
| Overview | Title, Status, Sub-issues progress, Priority, Workstream, Record type |
| Research Backlog | Title, Status, Parent issue, Priority, Workstream, Eligibility, Source verified, Eligibility phase, Decision blockers |
| Funding Pipeline | Title, Status, Opportunity stage, Priority, Eligibility, Provider, Program, Currency, Estimated usable value, Deadline, Support type, Score, Next action |
| In-Kind Support | Title, Status, Opportunity stage, Priority, Eligibility phase, Eligibility, Support type, Provider, Resource category, Program, Decision blockers |
| Nonprofit Readiness | Title, Status, Parent issue, Priority, Eligibility phase, Independent reviewer, Decision blockers, Sub-issues progress, Workstream |
| Deadlines | Title, Status, Priority, Eligibility, Provider, Program, Deadline, Eligibility phase, Decision blockers |
| Ready for Review | Title, Status, Priority, Eligibility, Confidence, Independent reviewer, Source verified, Opportunity stage, Decision blockers |
| Outreach & Applications | Title, Assignees, Status, Opportunity stage, Priority, Eligibility, Provider, Program, Decision blockers, Deadline, Next action |
| Awards & Reporting | Title, Assignees, Status, Opportunity stage, Support type, Provider, Program, Currency, Estimated usable value, Next action, Next verification |

### Saved filters

**Overview**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue record-type:Program,Epic`

**Research Backlog**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue record-type:Foundation,Opportunity status:Backlog,Ready,"In Progress",Blocked`

**Funding Pipeline**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue record-type:Opportunity support-type:Cash,Mixed opportunity-stage:Qualified,Preparing,Submitted eligibility:Eligible,"Conditionally eligible" -status:Blocked,"Not Pursuing"`

**In-Kind Support**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue record-type:Opportunity support-type:Credit,Hardware,Software,Service,Mixed -eligibility:Ineligible`

**Nonprofit Readiness**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue workstream:"01 Nonprofit","02 Readiness"`

**Deadlines**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue deadline:>=@today`

**Ready for Review**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue status:"In Review"`

**Outreach & Applications**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue opportunity-stage:Preparing,Submitted eligibility:Eligible,"Conditionally eligible" -status:Blocked,"Not Pursuing"`

**Awards & Reporting**

`repo:Pick-Your-AI/pick-your-ai-sustainability is:issue opportunity-stage:Awarded,Activated,Reporting`

A saved filter cannot confer authority to contact a provider or submit an application. The Preparing and Submitted stage conventions require the separate evidence described in [Workflow and authorization](workflow-and-authorization.md); the view exposes their recorded state rather than automatically approving an action.

The Deadlines filter is relative to today and is sorted by Deadline ascending. At this cutoff it contains [#25](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/25), dated 2026-11-03, and [#30](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/30), dated 2027-03-02. Future view counts will change as dated evidence and accepted work states change; this audit records the present persisted state.

## Labels, milestones and native relationships

The complete two-page [label catalog](../data/audits/label-catalog-readback.json) contains **36 unique labels: all 26 required taxonomy labels and 10 retained general-purpose labels**. The unused `priority:P0` and `eligibility:fiscal-sponsor` both exist. Every required label’s current issue count matches the independent issue readback; 24 taxonomy labels are currently applied. The remaining labels are available without forcing an unsupported assignment.

| Family | Required labels |
|---|---|
| Type | `type:epic`, `type:research`, `type:grant`, `type:legal`, `type:outreach`, `type:operations` |
| Priority | `priority:P0`, `priority:P1`, `priority:P2`, `priority:P3` |
| Category | `category:funding`, `category:inference`, `category:hardware`, `category:software`, `category:security`, `category:nonprofit`, `category:sponsorship`, `category:partnership` |
| Eligibility | `eligibility:immediate`, `eligibility:fiscal-sponsor`, `eligibility:501c3`, `eligibility:unknown` |
| Readiness | `ready:research`, `ready:review`, `blocked:dependency`, `blocked:decision` |

The complete [milestone catalog](../data/audits/milestone-catalog-readback.json) contains four open milestones, all without due dates and all with zero closed issues. Counts match the live issue assignments.

| Milestone | Open issues | Purpose |
|---|---:|---|
| [M1 — Foundation evidence](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/milestone/1) | 24 | Accepted administrative, legal-readiness, needs, budget and operating evidence. |
| [M2 — Support qualification](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/milestone/2) | 48 | Source-backed program research and qualification, including exclusions. |
| [M3 — Authorized pursuit](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/milestone/3) | 0 | Future explicitly authorized outreach or submission; no current commitment. |
| [M4 — Activation and accountability](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/milestone/4) | 0 | Future evidenced benefits, obligations, reporting and exit. |

Milestone completion describes the accepted outcome of its work; it does not imply legal recognition, an application or acquired funding. Native parent/sub-issue links and blocked-by relationships are independently recorded in the [dependency register](dependency-register.md); Project grouping and text fields do not substitute for those relationships.

## Review and handoff

- Configuration verification is complete for the recorded cutoffs; compare future changes against the saved field, view and catalog evidence.
- Record the actual final PR head and changed-file readback at handoff. Keep the PR unmerged until the organization’s genuine independent approval requirement is satisfied.

The final screenshot was unavailable after the browser connection stopped responding. The complete field, view, label and milestone evidence above had already been captured and persisted; this report claims no screenshot verification.
