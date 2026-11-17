# External security and accessibility review support

**Owning issue:** [#59 / E07-04](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/59). **Source review date:** 2026-11-17. **Status:** new public-source research draft, pending independently accepted findings and shared-register reconciliation. No program application, account creation, payment, third-party API calls, external audits, or production changes.

## Decision and scope

**P1 research priority, not eligibility.** Retain OSTIF as a conditional *funded security review* lead, and separately assess Knowbility programs for *web accessibility improvement and disability-user feedback*. The published security-audit offer is **not a guaranteed free audit**. Automated accessibility tooling does **not** substitute for human testing or a security assessment. Do not claim present applicant qualification, professional engagement, sponsorship, award, avoided cost, authorized representative, or review success.

The program's scoring weights (20/20/15/10/10/10/10/5) cannot produce a defensible numerical score before actual eligibility and scope, commitments, net value and effort are verified. **Numeric score: Not scored.** **Cash received, credit value, funded time, maintainer effort, deadline for most routes: Unknown.**

## Provider-specific prospectus

| Program | Observed official scope and intake | Restriction and disposition |
| --- | --- | --- |
| [OSTIF — Get an Audit](https://ostif.org/get-an-audit/) | OSTIF scopes security review, chooses an independent audit team, manages remediation and coordinates public reporting. It describes potential sponsor underwriting and an illustrative **$30,000–$200,000** audit range. An inquiry/intake exists; no fixed deadline was verified. | **Conditional P1**: actual project, audit scope, sponsor funding, SOW, reviewer capacity and responsible maintainer are Unknown. This is not a no-cost entitlement, funding approval, contractual quote, security certification or permission to disclose findings. |
| [Knowbility — Accessibility Internet Rally (AIR)](https://knowbility.org/programs/air) | AIR 2027 pairs an approved nonprofit/community client with mentored volunteer web teams to create or improve an accessible website. Official client registration is **$150**, with **2026-12-21** deadline and a 2027 delivery cycle. | **Conditional web-accessibility project, not an audit**: matching, fee authorization, site fit, actual eligible client, participation, quality and final deliverable are unverified. Under the [published AIR participant commitments](https://knowbility.org/programs/air/rally-rules#participant-commitments), paying the fee but missing orientation prevents matching; a matched client must provide a domain, hosting, content and a project representative who meets the team at least every other week. None of those inputs or staff commitments is evidenced for this project. Not a free service, not a native mobile accessibility assessment and not a security pen test. |
| [Knowbility — AccessWorks](https://knowbility.org/services/accessworks) | Published service includes disability-user usability testing, participant recruitment and **mobile-app** testing, with a **client inquiry for a tailored quote and statement of work**. No public flat fee or guaranteed booking is shown. | **Specialist testing lead; intake route documented, terms Unknown.** A particular project must request a scoped quote and SOW in a separately authorized action; no free seat, stipend, applicant-specific eligibility, availability, consent/data handling or price is verified. |
| [Google OSS-Fuzz](https://github.com/google/oss-fuzz/blob/master/docs/faq.md) | Selective continuous fuzzing service; accepts established OSS projects with meaningful security exposure or ecosystem dependency. | **Engineering support, not an independent human audit or accessibility service.** No evidence Pick Your AI meets OSS-Fuzz thresholds. Account/application and onboarding not attempted. |
| [Deque axe-core](https://www.deque.com/axe/axe-core/) | Free open-source library of automated *web* accessibility rules. | **No external review or grant.** Automation catches only some barriers; manual keyboard, screen-reader and real-user evaluation remain necessary. No native-mobile conformance claim. |

**Avoid overlap:** The existing [GitHub security/tooling baseline](../tooling/github-baseline.md) is accepted research on public-repo capabilities, not evidence that anyone has conducted an external audit. Technical security remediation belongs to the owning software repositories, not this fundraising issue.

## Three applicant routes

| Route | Unincorporated community | Actual fiscal sponsor | Recognized 501(c)(3) |
| --- | --- | --- | --- |
| OSTIF | Potential public FOSS project inquiry; specific acceptance and sponsor funding Unknown | Project scope/ownership and sponsor permission require separate proof; no automatic grant | Recognition does not confer acceptance, funding or an auditor |
| AIR | Community groups are advertised client category; actual contracting representative and ability to pay remain unverified | Sponsor authority and program acceptance Unknown | Stated nonprofit category may fit, but approval, matching and fee remain separate |
| AccessWorks | Tailored-quote inquiry path documented; eligibility, fee, scope and capacity Unknown | Same restrictions; specific contracting representative Unknown | Same restrictions; nonprofit recognition alone does not book a service |
| OSS-Fuzz | Technical maturity/exposure govern, nonprofit status not decisive | Same technical criteria | Same technical criteria |
| axe-core | Open-source tool, no provider enrollment required | Same | Same |

For every route, the legal entity/individual applicant, fiscal-sponsor agreement, signer, operating jurisdiction, licensing, fee approval, organization account, project readiness and third-party access are **Unknown** until evidenced. A charity label is not legal authority. No applications, grants, paid audits, volunteer assignments or test results occurred.

## Review scope A — security and supply-chain

**Proposed reproducible public-benefit use case:** anchor a candidate release-boundary assessment to the public [Apple issue #24](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/24), [Apple issue #107](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/107) and [Android issue #107](https://github.com/Pick-Your-AI/pick-your-ai-android/issues/107) as receiving tasks, rather than presuming a deployed service. A suggested **synthetic** check is to feed a malformed, rights-cleared model-result record to a locally selected parser/ingestion entry point and verify explicit rejection and no unintended data persistence. The exact code path, accepted source SHA, fixture, threat model and expected output must first be pinned with the technical owner. No such exercise or external audit has been run; the issue links establish receiving candidates, not that those features already exist.

Before any real audit, technical owners must identify: exact repository and signed/accepted revision, active components and dependency inventory, threat model, data flows and trust boundaries, untrusted input handling, existing static/CI/scanning evidence, rights-cleared synthetic examples, current disclosure route, responsible maintainer and remediation timeline. Ask for independent assessment of applicable authentication, authorization, package integrity, unsafe deserialization and injection risks **only where those features exist**.

**Required output:** bounded SOW/RFP, scoped test strategy, confidentiality and disclosure window, risk-based findings, agreed fixes, added regression tests, independent retest and authorized public report after remediation. OSTIF's standard process includes scoping, auditor selection, remediation and reporting; none of those steps has been executed in this campaign.

## Review scope B — accessibility and participation

**Proposed concrete public-benefit use case:** design separate, **not-yet-executed** tasks for the public [Apple #107](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/107) and [Android #107](https://github.com/Pick-Your-AI/pick-your-ai-android/issues/107) receiving issues: launch the eventual native research/comparison screen with synthetic results, select one result by assistive technology, inspect its evidence/limitations and return to the list without losing focus or spoken context. For the candidate website journey, use a rights-cleared synthetic comparison and verify keyboard/screen-reader interpretation of labels, validation errors, and result provenance. Pin a specific accepted source SHA, actual screen/entry point, WCAG version, device/assistive-tech pair and observable success/failure for **each** distinct platform before issuing an SOW. These are proposed scopes, not assertions that a screen, route, fixture or participant already exists. No owners are newly assigned.

- Pre-check labels, focus, keyboard-only navigation, errors, contrast, live regions and results explanations with appropriate web accessibility automation, while treating all untested user experience as **Unknown**.
- Specify actual browser/assistive-technology combinations, user tasks, success measures and accessible feedback mechanisms. An axe-core pass is not an accessibility certification.
- Consent, participant protection, data retention and any incentives for real-user research need separate permission. **No sensitive participant or security data may be posted publicly**; no live study is authorized.
- A fee-bearing AIR website build can potentially address an access gap, but it is neither an independent audit nor a free specialist panel. AccessWorks may offer specialist user feedback subject to independently confirmed terms.

**Required output:** versioned task/scenario inventory, reviewed WCAG standard and scope, sanitized barrier findings, fixes with regression tests, independent manual retest and a separately accepted report. No accessibility score or compliance status is inferred here.

## Restrictions, obligations, value and exit criteria

| Dimension | Evidence and explicit unresolved gate |
| --- | --- |
| Intake & deadline | OSTIF current intake description, no verified fixed date; AIR 2027 published deadline 2026-12-21; AccessWorks quote/date Unknown |
| Funding and cost | OSTIF price range is illustrative *cost*, not funding committed or project value. AIR $150 is a *fee* requiring authorization; no payment is permitted here. Actual hours, quote, overages, sponsor underwriting, renewals and avoided cost Unknown |
| Reporting & publication | Require independent severity judgment, disclosure channel, responsible fix owner and mutually agreed public-report rights; never publish unpatched exploit details in a PR |
| Branding & independence | Sponsor acknowledgments and trademark use need written permission; no sponsor veto of unfavorable findings or required exclusive vendor placement |
| Privacy | Only synthetic inputs in offline experiments; any external engagement handling user or donor information requires separate privacy, counsel and security review |
| IP, portability & continuity | Preserve tool-agnostic test fixtures, audited commit and artifact ownership; license rights/retention and repeat audits must be negotiated, not assumed |
| Use case and ranking | Preserve Unknown numeric score, avoided expense and qualifying applicant until a valid scoped procurement-style comparison and actual maintainer capacity exist |

No provider benefit may be counted as received cash or avoided cost, and the published fee/price range must not become a fake grant-value score.

## Unsent inquiry briefs (for a separately authorized operator)

**Security:** attach only an approved public repository/release link, existing checks and a sanitized scope. Ask OSTIF what objective project-acceptance criteria, sponsor underwriting, timeline, confidentiality, disclosure and ownership terms would apply. Do not transmit private infrastructure, vulnerabilities, credentials or a budget commitment.

**Accessibility:** describe an actual public web journey and distinction between an AIR site project and AccessWorks professional testing. Ask about client acceptance, fee, participation capacity, WCAG criteria, rights, retention and accessibility deliverables. Do not register, sign agreements, pay, recruit or share participant identities.

## Source ledger and remaining acceptance

Source pages were inspected unauthenticated on **2026-11-17**; this is a public-documentation evidence level, **not** provider confirmation for the project.

- S1 OSTIF, [Get an Audit](https://ostif.org/get-an-audit/) — costs, sponsor sourcing, audit/RFP, remediation and release.
- S2 OSTIF, [Sponsorship](https://ostif.org/sponsorship/) — sponsor workflow and public reports.
- S3 Knowbility, [AIR 2027](https://knowbility.org/programs/air) — client categories, $150 client registration, deadline and schedule.
- S4 Knowbility, [AccessWorks and accessibility support](https://knowbility.org/) — disability-user testing offering; price/subsidy not established.
- S5 Google, [OSS-Fuzz eligibility](https://github.com/google/oss-fuzz/blob/master/docs/faq.md) — mature/security-critical project criteria.
- S6 Deque, [axe-core](https://www.deque.com/axe/axe-core/) and [manual testing distinction](https://www.deque.com/axe/devtools/) — automated rule checks versus manual review.
- S7 [Accepted GitHub baseline](../tooling/github-baseline.md) and [research methodology](../../docs/research-methodology.md) — prior repository work and evidence gates.

**Open:** review this exact revision independently against #59's literal criteria; reconcile only the existing **OSTIF** program identity with current shared opportunity register and pipeline/freshness projections under separate safety review; confirm sources again when actual application action is authorized. No duplicated OSTIF record is introduced. Keep #59 open until canonical document, appropriate structured record, independent findings acceptance, and applicable current-head CI/merge are all complete.
