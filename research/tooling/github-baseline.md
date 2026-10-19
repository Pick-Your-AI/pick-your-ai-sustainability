# GitHub developer and security baseline

Owning issue: [E07-02 / #57](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/57). Parent: [E07 / #8](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/8).

**Status:** source-checked research draft; independent acceptance of this deliverable is pending. **Official sources reviewed:** 2026-10-19. **Repository/settings refresh:** 2026-10-19, 10:08–10:09 UTC. This refresh extends the earlier 08:09–08:14 UTC inventory. Each observation is bounded to its revision or read time, not a continuing assertion about a moving branch.

**Recommended disposition:** P1 foundational work: verify and use existing public-repository capabilities before requesting overlapping donated tooling. The [scoring rubric](../../docs/scoring-and-qualification.md) makes a numeric opportunity score **Not applicable** to this baseline. There is no grant, award probability or cash amount to score. Realized avoided cost and implementation effort remain **Unknown**. Implementation owner and independent reviewer are **Unassigned** throughout this document; existing issue ownership is unchanged.

## Scope and evidence boundaries

The inventory covers six delivery/research repositories and the organization's `.github` repository. All seven were public and unarchived in direct repository reads. This is a bounded inventory: the earlier repository-list query returned no results despite successful direct reads, so it does not prove that these are every repository in the organization.

Four claims must remain separate:

1. **Available:** current GitHub documentation permits the capability for the repository/account type.
2. **Configured:** a frozen source file or settings read shows a configuration.
3. **Executed:** a linked run reports a result for an exact revision. A success does not prove complete coverage, enforcement or incident readiness.
4. **Independently qualified operation:** an appropriate reviewer accepts the actual feature, negative/recovery evidence, permissions and ongoing responsibilities. No whole-repository operational qualification is established by this baseline.

Repository trees and run receipts support the middle two claims. Published provider descriptions support availability. Unknown administrative settings remain Unknown rather than being labeled disabled. Neither research nor publication changes settings, grants rights, appoints people, authorizes spending, submits an application or activates a benefit.

## Standard capabilities and cost boundaries

These are service capabilities, not selective funding awards. Their application process, application deadline and award stage are **Not applicable**. Use remains subject to account permissions, acceptable use, supported languages/ecosystems and product terms.

| Capability | Current published baseline | Cost or qualification boundary |
| --- | --- | --- |
| Actions execution | Standard GitHub-hosted runners are free for public repositories. | Larger runners are charged even for public repositories. Self-hosting has infrastructure/maintenance costs even where GitHub runner usage is free. The 2,000-minute Free allowance is not a cap on free public standard-runner execution. [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) |
| Actions storage | Free organizations: 500 MB artifact allowance; Team: 2 GB. Artifact storage shares the Packages allowance. Cache is separately 10 GB per repository. | Extra storage is not unlimited free capacity. Cache above 10 GB is billable when a higher cache limit is configured. Current published overage rates are USD 0.25/GB-month for shared storage and USD 0.07/GB-month for cache; actual plan, usage and budgets are Unknown. [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) |
| Hosted-runner limits | Free: 20 concurrent jobs, at most five macOS. Team: 60 jobs, still at most five macOS. Hosted jobs have a six-hour execution limit. | Account-specific increases are Unknown. A Team benefit alone would not raise the documented standard macOS concurrency cap. [Actions limits](https://docs.github.com/en/actions/reference/limits) |
| Dependency protection | Dependency graph, SPDX SBOM export, Dependabot alerts/security updates/version updates, and public-repository dependency review are available without purchasing Advanced Security. | Availability does not establish settings, ecosystem coverage, complete snapshots or remediation. [Security features](https://docs.github.com/en/code-security/getting-started/github-security-features) |
| Merge-time dependency review | Public repositories can run the dependency-review action. | Its failed check blocks merging only when the applicable branch protection/rules require it. A passing job or review UI alone is insufficient. [Dependency review](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review) |
| Code and secret scanning | Public repositories have no-cost code-scanning, secret-scanning and push-protection capabilities. Security policies and public-repository advisories are also available. | Product-default wording is not repository-specific readback. Personal push protection and repository protection are distinct. Premium features are not all included. [Security features](https://docs.github.com/en/code-security/getting-started/github-security-features), [Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) |
| Repository controls | Public repositories on Free organizations can use branch/tag rulesets. | Rule changes require appropriate permission. Organization-wide and push rules have separate plan boundaries. Classic branch protection and rulesets can apply together. [Rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets) |
| Packages | Public packages are free. Container Registry storage/bandwidth is currently free, with at least one month's notice before a policy change. | Private packages have separate quotas/overages; Actions artifacts share the storage pool. No actual package usage or invoice was verified. [Packages billing](https://docs.github.com/en/billing/concepts/product-billing/github-packages) |
| Codespaces | Organizations have no included free quota. Personal Free accounts receive 120 core-hours and 15 GB-month monthly. | Personal capacity is not a transferable organization pool; compute/storage overages and billing ownership matter. No organization-sponsored Codespaces use was established. [Codespaces billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces) |
| Private-repository security | Code Security and Secret Protection are separate products on qualifying paid plans. | Free public-repository features or a donated Team plan do not imply those private-repository products are included. [Advanced Security](https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security) |

These are published allowance/rate facts, not an invoice forecast. Current GitHub plan, payment method, budgets, consumed allowance, paid seats, vendor subscriptions and installed integrations were not inspected. Consequently no zero-total-cost or available-credit claim is made.

## Frozen repository inventory

Each linked tree is the exact inspected `main` revision. Source observations below use these revisions. Settings and workflow-run collections are time-stamped live observations and are not frozen by a source commit.

| Repository | Exact revision | License metadata |
| --- | --- | --- |
| [Apple](https://github.com/Pick-Your-AI/pick-your-ai-apple/tree/76f84345eb4b5451af4385e8207fa7f8719ccc0a) | `76f84345eb4b5451af4385e8207fa7f8719ccc0a` | MIT recognized |
| [Android](https://github.com/Pick-Your-AI/pick-your-ai-android/tree/56cc178e38f1fc0914db273468301e3431daef64) | `56cc178e38f1fc0914db273468301e3431daef64` | MIT recognized |
| [Leaderboard](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/tree/24c0140466cfa1454723adfba04ff030646821c5) | `24c0140466cfa1454723adfba04ff030646821c5` | MIT recognized |
| [Website](https://github.com/Pick-Your-AI/pick-your-ai-website/tree/414d63a31df00afb10cafe13c9694b180af0ab65) | `414d63a31df00afb10cafe13c9694b180af0ab65` | MIT recognized |
| [Research](https://github.com/Pick-Your-AI/pick-your-ai-research/tree/99f82fb0fe4bf3bb5c4a302994c7089fdf5cea1d) | `99f82fb0fe4bf3bb5c4a302994c7089fdf5cea1d` | MIT recognized |
| [Sustainability](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/tree/e73024a31ea0568af0abac479a21f7f1c39ac15f) | `e73024a31ea0568af0abac479a21f7f1c39ac15f` | No recognized license |
| [Organization `.github`](https://github.com/Pick-Your-AI/.github/tree/01d392c1a42e93e6a11c17f4c165ad23988d376a) | `01d392c1a42e93e6a11c17f4c165ad23988d376a` | No recognized license |

License metadata is an inventory result, not a legal conclusion about every file, dependency, dataset or contribution. Existing licensing/stewardship research remains in [E01-07 / #17](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/17).

### Repository-by-feature configuration

“Absent” below means absent from the complete inspected source tree, not disabled in account settings. “Unknown” native settings apply to every row as detailed in the next section.

| Repository | CI and artifact configuration | Dependency protection | Scanning and reporting evidence |
| --- | --- | --- | --- |
| Apple | Nine [workflows](https://github.com/Pick-Your-AI/pick-your-ai-apple/tree/76f84345eb4b5451af4385e8207fa7f8719ccc0a/.github/workflows), standard Ubuntu and `macos-15`; uploaded evidence commonly retained 14 days. | [Dependency review](https://github.com/Pick-Your-AI/pick-your-ai-apple/blob/76f84345eb4b5451af4385e8207fa7f8719ccc0a/.github/workflows/dependency-review.yml) covers vulnerable dependencies, licenses and snapshot completeness. No Dependabot configuration found. | No checked-in CodeQL workflow or SECURITY.md found. Native code/secret settings Unknown. |
| Android | Two [workflows](https://github.com/Pick-Your-AI/pick-your-ai-android/tree/56cc178e38f1fc0914db273468301e3431daef64/.github/workflows), standard `ubuntu-24.04`; seven-day artifacts. | Core/preview checks include dependency locking, strict Gradle verification and runtime SBOM generation. No Dependabot configuration or dependency-review action found. | [Secrets workflow](https://github.com/Pick-Your-AI/pick-your-ai-android/blob/56cc178e38f1fc0914db273468301e3431daef64/.github/workflows/secrets.yml) runs the standalone pinned scanner. No checked-in CodeQL workflow or SECURITY.md found. Native secret protection remains Unknown. |
| Leaderboard | Five [workflows](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/tree/24c0140466cfa1454723adfba04ff030646821c5/.github/workflows), standard Ubuntu; browser/recovery artifacts retained seven days. | [Dependabot](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/blob/24c0140466cfa1454723adfba04ff030646821c5/.github/dependabot.yml) schedules weekly npm/Actions updates. No dependency-review action found. | Runtime CI includes checksum-verified Gitleaks and scanner self-tests. [SECURITY.md](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/blob/24c0140466cfa1454723adfba04ff030646821c5/SECURITY.md) records private-reporting activation/readback on October 18; this is historical evidence, not today's settings read. No checked-in CodeQL workflow found. |
| Website | Three [workflows](https://github.com/Pick-Your-AI/pick-your-ai-website/tree/414d63a31df00afb10cafe13c9694b180af0ab65/.github/workflows), standard Ubuntu; seven-/14-day evidence retention. | [CI](https://github.com/Pick-Your-AI/pick-your-ai-website/blob/414d63a31df00afb10cafe13c9694b180af0ab65/.github/workflows/ci.yml) includes audit, dependency-review, build/tests/accessibility checks; weekly npm/Actions [Dependabot](https://github.com/Pick-Your-AI/pick-your-ai-website/blob/414d63a31df00afb10cafe13c9694b180af0ab65/.github/dependabot.yml). | [SECURITY.md](https://github.com/Pick-Your-AI/pick-your-ai-website/blob/414d63a31df00afb10cafe13c9694b180af0ab65/SECURITY.md) exists. Its legacy repository reporting URL and described response target are source statements, not verified reporting delivery or a new commitment. No checked-in CodeQL workflow found. |
| Research | Two [workflows](https://github.com/Pick-Your-AI/pick-your-ai-research/tree/99f82fb0fe4bf3bb5c4a302994c7089fdf5cea1d/.github/workflows): research validation and MR09 estimator validation on standard Ubuntu. | No Dependabot configuration or dependency-review action found. | [SECURITY.md](https://github.com/Pick-Your-AI/pick-your-ai-research/blob/99f82fb0fe4bf3bb5c4a302994c7089fdf5cea1d/SECURITY.md) describes private reporting; availability/delivery not freshly tested. No checked-in CodeQL workflow found. |
| Sustainability | Two [workflows](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/tree/e73024a31ea0568af0abac479a21f7f1c39ac15f/.github/workflows): read-only evidence validation and separately gated native-relationship execution on standard Ubuntu. | Validation dependencies are pinned; no Dependabot configuration or dependency-review action found. | No checked-in CodeQL workflow or SECURITY.md found. Native-relationship execution is an administrative workflow, not security/research acceptance. |
| Organization `.github` | One [Early Contributors workflow](https://github.com/Pick-Your-AI/.github/blob/01d392c1a42e93e6a11c17f4c165ad23988d376a/.github/workflows/early-contributors.yml) on standard Ubuntu. | No Dependabot configuration or dependency-review action found. | No checked-in CodeQL workflow or SECURITY.md found. Organization policy text does not prove another repository's live settings. |

### Branch protection and rulesets

Both the branch metadata and every returned ruleset were inspected. A `protected: true` branch is not by itself proof of required CI checks. Conversely, missing status-check rules in a ruleset collection do not rule out classic branch protection.

| Repository | Fresh setting evidence | Required-check finding |
| --- | --- | --- |
| Apple | [Main branch](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-apple/branches/main); [four active rulesets](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-apple/rulesets) | Contributor/review controls present; branch response has empty required-check contexts and no inspected ruleset requires status checks. |
| Android | [Main branch](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-android/branches/main); [four active rulesets](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-android/rulesets) | Contributor/review controls present; branch response has empty required-check contexts and no inspected ruleset requires status checks. |
| Leaderboard | [Main branch](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-leaderboard/branches/main); [four active rulesets](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-leaderboard/rulesets) | **Classic protection requires `checks` and `validate` for everyone**, with GitHub Actions app ID 15368. The rulesets themselves contain no status-check requirement. Do not report this as an absent CI gate. |
| Website | [Main branch](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-website/branches/main); [five active rulesets](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-website/rulesets) | [Main-protection ruleset](https://github.com/Pick-Your-AI/pick-your-ai-website/rules/25248541) requires `ci-required`, GitHub Actions integration 15368. Classic contexts are empty; the ruleset supplies the gate. |
| Research | [Main branch](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-research/branches/main); [five active rulesets](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-research/rulesets) | Branch/review controls present; branch response has empty required-check contexts and no inspected ruleset requires status checks. |
| Sustainability | [Main branch](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-sustainability/branches/main); [rulesets](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-sustainability/rulesets) | `protected: false`, no returned rulesets or required-check contexts. The written contribution/review policy still applies; it is not equivalent to enforcement. |
| Organization `.github` | [Main branch](https://api.github.com/repos/Pick-Your-AI/.github/branches/main); [four active rulesets](https://api.github.com/repos/Pick-Your-AI/.github/rulesets) | Contributor/review controls present; branch response has empty required-check contexts and no inspected ruleset requires status checks. |

These reads do not exercise bypass behavior or establish that every failing change is blocked. They preserve the distinction between configured checks, observed failures and independently accepted enforcement.

### Bounded execution receipts

The following were read at 10:09 UTC. Run links identify their own exact heads and can subsequently change status. A successful workflow is not a clean security audit.

| Repository | Receipt and boundary |
| --- | --- |
| Apple | [Contract preparation](https://github.com/Pick-Your-AI/pick-your-ai-apple/actions/runs/39233366235) succeeded at the inventory head. Six native/Swift workflows were still queued; do not call that head fully green. Earlier [dependency-review success](https://github.com/Pick-Your-AI/pick-your-ai-apple/actions/runs/39218320169) is historical execution evidence, not a new run for this head. |
| Android | [Core verification](https://github.com/Pick-Your-AI/pick-your-ai-android/actions/runs/39234376226) and [secret scanning](https://github.com/Pick-Your-AI/pick-your-ai-android/actions/runs/39234376320) succeeded at the inventory head. Scanner success does not prove GitHub-native protection, vulnerability response or credential rotation. |
| Leaderboard | [Runtime](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/actions/runs/39234720091), [isolated recovery](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/actions/runs/39234719998) and [plan validation](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/actions/runs/39234720055) succeeded at the inventory head; [browser checks](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/actions/runs/39234720076) were in progress. |
| Website | [CI](https://github.com/Pick-Your-AI/pick-your-ai-website/actions/runs/39234422398) and [live E2E](https://github.com/Pick-Your-AI/pick-your-ai-website/actions/runs/39234893551) succeeded at the inventory head. Deployment results do not establish third-party hosting prices or subscription ownership. |
| Research | [Research validation](https://github.com/Pick-Your-AI/pick-your-ai-research/actions/runs/39228992051) succeeded at the inventory head. This does not independently accept all research findings. |
| Sustainability | [Evidence validation](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/actions/runs/39233924756) succeeded at the inventory head. It checks local consistency, not source freshness or applicant qualification. |
| Organization `.github` | The head-filtered [run collection](https://api.github.com/repos/Pick-Your-AI/.github/actions/runs?head_sha=01d392c1a42e93e6a11c17f4c165ad23988d376a&per_page=100) returned no runs for this head. Workflow presence and earlier execution are not a successful current-head receipt. |

## Administrative Unknowns and access limitations

For **each of the seven repositories**, these current settings remain Unknown:

- Code-scanning default setup, complete analysis coverage, alert state and disposition. No checked-in CodeQL action was found; default setup can exist without a checked-in workflow.
- GitHub-native secret-scanning alerts, repository push protection, exceptions and contributor-level push protection.
- Dependabot alert/security-update settings and actual coverage. A version-update configuration is not proof that security alerts/updates are enabled or effective.
- Current private vulnerability reporting, notification delivery and accepted responder capacity. Repository policy text is not a fresh readback or delivery test.
- Effective Actions allowlist, fork-workflow restrictions and complete organization/enterprise policy inheritance.

Direct repository responses omitted `security_and_analysis`. The earlier connector pass rejected code-scanning default-setup and Actions workflow-settings URLs as unsupported; those are tool/access limitations, not evidence of disabled features. No administrative permission was expanded to resolve them. A later authorized read should record the exact repository, setting, timestamp and result, without copying secret values or private findings into public artifacts.

## Applicant routes and adjacent benefits

The [program README](../../README.md#current-boundaries) does not establish the community's legal entity, recognized status, sponsor or authorized signer. Current facts must not be replaced by intended future structure.

| Route | Standard public-repository capabilities | Separate nonprofit-plan comparison |
| --- | --- | --- |
| Present community | Charity recognition is unnecessary for the public-repository baseline. Product/permission/license conditions still apply; configuration and operation remain separately evidenced. | Actual qualification is **Not established**. A community without registered nonprofit status would not meet the program's published registered-organization condition. |
| Fiscal-sponsored project | The same public-repository baseline is available without treating the sponsor's status as the project's own. | **Unknown.** The reviewed terms do not establish that a sponsor's benefit transfers to a separately owned project organization. Sponsor agreement, beneficiary account and provider acceptance require verification. |
| Independently recognized 501(c)(3) | Recognition does not add evidence that a feature is configured, effective or free of overages. | A **conditional route**, not established eligibility: actual recognition, jurisdiction, mission restrictions, authorized organization administrator and provider approval must be verified. |

[GitHub for Nonprofits](https://github.com/solutions/industry/nonprofits) advertises free Team or a 25% Enterprise Cloud discount for verified qualifying organizations. The discount still involves paid Enterprise service. The [current quickstart](https://docs.github.com/en/nonprofit/quickstart) describes owner/administrator authorization, nonprofit documents, portal application, validation and later activation. No application was made. The portal returned no readable body in the source audit; authenticated intake fields, a fixed deadline and renewal/reporting schedule remain **Unknown**. No incremental Team need or benefit value has yet been demonstrated for this public-repository baseline.

This comparison is retained to prevent overclaiming standard benefits, not to promote a new nonprofit-plan opportunity. No new structured program record is introduced. If that distinct program is later pursued, first perform duplicate checking and create/reconcile its unique record under the [research method](../../docs/research-methodology.md). Existing `GITHUB-SECURE-OSS-FUND` and `GITHUB-SPONSORS-ORG` records in [the opportunity register](../../data/opportunities.json) remain owned by [#26](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/26) and [#33](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/33). This baseline neither duplicates nor completes those outcomes.

Other individual benefits are also separate: [Education](https://docs.github.com/en/education/about-github-education/github-education-for-students/about-github-education-for-students) requires the relevant verified academic status; free [Copilot Pro for maintainers](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-teachers-and-os-maintainers) depends on being a qualifying popular-project maintainer and is reevaluated monthly. Neither is established for a person here or transferable merely because one of the three legal structures owns public repositories. Account eligibility, activation, paid-review subscriptions and future quota remain Unknown.

## Restrictions, obligations and historical reconciliation

| Topic | Finding and remaining boundary |
| --- | --- |
| Licensing | [CodeQL CLI terms](https://github.com/github/codeql-cli-binaries/blob/main/LICENSE.md), read on 2026-10-19 at license blob `e872708522ded4e4155f3f8799ec7451a63176ad`, distinguish OSI-licensed codebases and automated analysis hosted/maintained on GitHub from other uses. Public visibility alone is insufficient. Clarify the sustainability and `.github` license positions before any CLI proposal; this research neither grants permission nor changes rights. |
| Permissions and independence | The [organization contribution policy](https://github.com/Pick-Your-AI/.github/blob/01d392c1a42e93e6a11c17f4c165ad23988d376a/CONTRIBUTING.md) restricts workflows to `actions/*` and approved OAuth apps. A CodeQL action proposal must check the actual allowlist and obtain any required authority; no silent permission expansion is implied. Preserve independent research conclusions and existing review/merge rules. |
| Branding and reporting | No new sponsor branding, exclusivity or grant-reporting commitment is established by documenting standard capabilities. Special-program obligations and nonprofit renewal/reporting remain unverified and must be reviewed separately before acceptance. |
| Privacy and publication | GitHub's published Terms (effective 2026-04-27; reread 2026-10-19) describe [D.4](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#d-user-generated-content) rights for GitHub and affiliates to use public content for AI/ML development, improvement and training, beyond viewing/forking. The [J.3](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service#j-ai-features-training-and-your-data) opt-out concerns AI Inputs/Outputs; it does not narrow D.4–D.8 or cover stored public-repository content. J.1 limits J.3 to individual licenses; customer/volume agreements govern their AI data use separately. Section E separately protects private-repository content. The project's governing agreement/settings remain Unknown; this is source analysis, not a project-specific legal conclusion. Keep confidential/security-sensitive material out of public evidence; citation does not authorize redistribution. |
| Portability | [CodeQL supports SARIF output](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli); the dependency graph supports SPDX export. Export formats help preserve results but do not migrate CI, rules, issues, identity, response ownership or billing automatically. Migration cost remains Unknown. |
| Renewal and overage | Standard capabilities have no application-round expiry established here, but product limits and terms can change. Artifact/cache retention, payment settings and budgets need ongoing ownership. No recurring review commitment, automatic renewal purchase or spending authority is created. |
| Historical nonprofit conflict | The [2024-10-23 announcement](https://github.blog/changelog/2024-10-23-announcing-github-for-nonprofits/) gave a blanket religious-affiliation exclusion; the current quickstart specifically identifies religious/faith-based organizations in India. Retain the conflict and consult current qualification terms; do not reproduce the old wording as universally current eligibility. This is source comparison, not a legal opinion. |
| Historical repository state | Android's earlier October 18 `protected: false`/empty-rulesets observation is superseded for current state by this dated read, not erased. Sustainability's earlier `b6c2f9c0a630efbb5ca57c0bde2f491e0cbcf9be` main had no workflows; the current inventory head contains both workflows. PR #73's initial program draft is no longer evidence that main lacks them. |
| Ruleset-only inference | Leaderboard's absence of a required-status-check rule in its four rulesets does not contradict the classic `checks`/`validate` requirements returned by its main branch. Website's gate instead comes from its ruleset. Read both surfaces before declaring a gap. |

## Actual use cases, overlaps and existing technical work

Public benefit comes from reproducible client builds, dependency inventories, accessible public interfaces and traceable research, with safe contribution paths. Existing standard-runner CI, dependency review, npm/Gradle checks and standalone Gitleaks already cover parts of that need. A donor request should identify the remaining accepted gap rather than price the same capability twice. The Android scanner is documented as a standalone MIT Gitleaks tool, not evidence of a paid scanner service. Existing automated review activity likewise does not establish a paid account, transferable license or available future quota.

| Existing work | Useful baseline input and remaining outcome | Owner for new work |
| --- | --- | --- |
| [Apple #30](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/30), open | Native CI exists; required-status enforcement and complete receiving evidence remain distinct from a successful job. | Unassigned |
| [Apple #103](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/103), open | Extend existing dependency review into accepted inventory, reporting, urgent-patch and rotation evidence. Do not infer response readiness from a scan. | Unassigned |
| [Android #59](https://github.com/Pick-Your-AI/pick-your-ai-android/issues/59), open | Existing core/preview checks supply configuration/execution evidence; required-check and full CI acceptance remain in this issue. | Unassigned |
| [Android #69](https://github.com/Pick-Your-AI/pick-your-ai-android/issues/69), open | Consume locking, verification, SBOM and scanner evidence; reporting, actionable triage, inventory traceability and urgent-update drills remain separate criteria. | Unassigned |
| [Leaderboard #34](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/issues/34), open | Classic required checks and existing CI are evidenced. Its actual fork-origin PR acceptance remains unchecked; do not invent a missing required-check gate. | Unassigned |
| [Apple #107](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/107) and [Android #107](https://github.com/Pick-Your-AI/pick-your-ai-android/issues/107), open | Hosted CI does not qualify physical devices, OS/lifecycle behavior or release readiness. These remain the canonical testing work. | Unassigned |
| [Sustainability #57](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/57) | Retain the administrative Unknowns, licensing questions, missing source configurations and sustainability enforcement discrepancy as baseline findings. Route any authorized implementation through the affected repository after checking its current issues/ownership; no duplicate implementation issue is created here. | Unassigned |

[Apple #24](https://github.com/Pick-Your-AI/pick-your-ai-apple/issues/24) is closed. Although #57 links it as context, it must not be presented as an unresolved account-decision task. The separate sustainability validation contribution is already reflected in current main; this document does not take ownership of its workflow/tests.

**Valuation method if later needed:** document an accepted workload and measured monthly usage; identify a genuinely otherwise-purchased alternative and its current quote; subtract uncovered usage, implementation, migration and maintenance costs. Keep any resulting avoided-cost estimate separate from cash. Without those inputs, value and effort stay Unknown rather than assigning a retail-price multiple to nominal free capacity. No verified deadline justifies P0; P1 follows the foundational-work rule.

## Remaining questions and acceptance record

The source date applies to the linked official product documentation and historical announcement, not to independent applicant qualification. Frozen repository files, API settings observations, and exact run receipts are identified separately. Recheck governing sources and actual account state before any activation, paid use or external representation.

1. Can an authorized reviewer obtain the missing administrative settings and effective allowlist readbacks without exposing private security findings? This is the remaining enabled-state evidence gap.
2. What plan, seats, integrations, actual usage, budget and paid-license inventory does the organization have? Which proposed donated tools add an accepted capability rather than overlap existing coverage?
3. Who will accept implementation/security-response ownership, evaluate source/configuration gaps and verify negative/recovery behavior in the existing technical issues? No person or deadline is assigned here.
4. If a nonprofit-plan comparison becomes an actual opportunity, what applicant/account, authority, recognition or sponsor relationship and incremental need are accepted? Full intake, renewal and private terms remain unverified.
5. Who independently accepts this exact baseline revision and its explicit Unknowns? Record the reviewer, reviewed revision, scope, conflicts, decision, limitations and review link in #57. Local validation or an automated source check alone does not satisfy acceptance.

| Acceptance item | Current record |
| --- | --- |
| Canonical deliverable | This file is the proposed baseline. Publication and a revision link must be verified separately. |
| Evidence and three routes | Source-linked product facts, dated repository matrix, route distinctions, costs, restrictions, conflicts and Unknowns are recorded above. |
| Program record | Not applicable to standard service capabilities; existing Secure OSS/Sponsors records are preserved. No new nonprofit-plan opportunity is promoted. |
| Priority and numeric score | P1 foundational; numeric score Not applicable. Cash award Not applicable; realized avoided cost and effort Unknown. |
| Independent reviewer / acceptance | Unassigned / Pending; no acceptance URL or reviewed revision is fabricated. |
| Application, award, activation or operational qualification | None established by this research. Prior account/program enrollment is Unknown. |
| Deadline / next-action date | No application deadline for this standard baseline; implementation and review dates Unassigned. |

Issue #57 remains open until the actual findings revision is published and independently accepted under the repository process. Unknown settings or applicant facts must not silently become qualified operation, eligibility, funding or activation claims when that review occurs.
