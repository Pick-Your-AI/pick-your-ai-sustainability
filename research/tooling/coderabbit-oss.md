# CodeRabbit OSS: coverage and activation recommendation

Owner issue: [E07-01 / #56](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/56). Canonical record: `CODERABBIT-OSS-PRODUCT` in [the opportunity register](../../data/opportunities.json). Source review date: **2026-10-19**. Research status: **In Review; independent acceptance of this revision is pending**.

## Recommendation

**Defer a new CodeRabbit activation.** The public record does not yet establish an installed, correctly scoped service or a review gap that another bot would close. Retain the existing repository CI and independent maintainer review. If an authorized operator later demonstrates an unmet need, evaluate one small, explicitly authorized internal pilot using the decision procedure below. This is a complete research recommendation with named unknowns, not an instruction to install or a claim that the service is absent.

The product and cash routes have different dispositions:

| Route | Disposition | What would change it |
| --- | --- | --- |
| Free OSS product access | Defer activation; preserve an optional pilot decision | Verify actual installation/account/configuration, authority, rights, operating capacity and an uncovered review need |
| Provider-selected cash sponsorship | Watch; no open application route or project entitlement established | A current, specific provider invitation with recipient, amount, conditions and authorized acceptance |

No application, app installation, bot invocation, configuration change, outreach, paid trial or financial commitment occurred in this research. Actual historical installation, billing and award state remain Unknown.

## Current offer and intake

The current [OSS FAQ](https://www.coderabbit.ai/oss) describes public GitHub/GitLab visibility as its OSS condition, without a grant application, approval queue or credit card. It separately describes provider-selected cash support through sponsorship/payment channels. Its marketing announcements and aggregate support pledge do not establish a Pick Your AI award, deadline or usable value.

The [GitHub installation guide](https://docs.coderabbit.ai/platforms/github-com) describes repository-owner access, organization-owner authority for organization integration, authentication and selection of repositories. The [public quickstart](https://docs.coderabbit.ai/getting-started/quickstart) describes that setup route. The public app endpoint, [app.coderabbit.ai](https://app.coderabbit.ai), exposed no readable intake fields in the public text retrieval on this review. No signed-in screen or actual grant of access was inspected. The published route is established; present account eligibility and the final consent screen are not.

A grant-round deadline is **Not applicable to the documented public-product route**. A project cash-sponsorship intake, amount, deadline, currency and reporting agreement are **Unknown**. No internal research checkpoint is an application deadline.

## Dated coverage across the six repositories

These are bounded public observations captured on **2026-10-19, approximately 11:00–11:07 UTC**. Each source root and check/status query was pinned to the listed commit. Repository star counts are contemporaneous metadata; they are not immutable commit properties. Later main changes do not alter what was inspected here.

| Repository | Inspected main commit | Stars | Root entries | Check runs |
| --- | --- | ---: | ---: | ---: |
| Apple | [`ee2b3adfc99869d71141425f31b38a0ebf3cf3bc`](https://github.com/Pick-Your-AI/pick-your-ai-apple/tree/ee2b3adfc99869d71141425f31b38a0ebf3cf3bc) | 0 | 12 | 17 |
| Android | [`875a339ec7e05046349afb9963e59285831350df`](https://github.com/Pick-Your-AI/pick-your-ai-android/tree/875a339ec7e05046349afb9963e59285831350df) | 0 | 21 | 3 |
| Leaderboard | [`abc38d5d4caab73160eddbdc9a8a346bd3c3dac3`](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/tree/abc38d5d4caab73160eddbdc9a8a346bd3c3dac3) | 0 | 24 | 5 |
| Website | [`900c14d7e5101183a930834cb5249597837efb41`](https://github.com/Pick-Your-AI/pick-your-ai-website/tree/900c14d7e5101183a930834cb5249597837efb41) | 5 | 32 | 20 |
| Research | [`daac1dae7348c8f4f1011c85979068c8ba6c1489`](https://github.com/Pick-Your-AI/pick-your-ai-research/tree/daac1dae7348c8f4f1011c85979068c8ba6c1489) | 13 | 20 | 1 |
| Sustainability | [`cad980ecc8e43a472ebe63c4360f94846d175a96`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/tree/cad980ecc8e43a472ebe63c4360f94846d175a96) | 0 | 10 | 1 |

For every row, the complete root listing had no `.coderabbit.yaml` or CodeRabbit-named entry. Every returned check run identified the `github-actions` app; no CodeRabbit check appeared. Each combined commit-status response had `total_count: 0` and an empty status array. These are attendance and configuration observations, **not a statement that all those CI jobs passed or that an installed review service is absent**.

The reproducible read pattern is:

- `GET /repos/Pick-Your-AI/{repository}` for public/unarchived state and stars.
- `GET /repos/Pick-Your-AI/{repository}/contents?ref={full_commit}` for the complete root.
- `GET /repos/Pick-Your-AI/{repository}/commits/{full_commit}/check-runs?per_page=100&filter=latest`.
- `GET /repos/Pick-Your-AI/{repository}/commits/{full_commit}/status?per_page=100`.

For example, the [frozen Sustainability root](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-sustainability/contents?ref=cad980ecc8e43a472ebe63c4360f94846d175a96), [checks](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-sustainability/commits/cad980ecc8e43a472ebe63c4360f94846d175a96/check-runs?per_page=100&filter=latest) and [statuses](https://api.github.com/repos/Pick-Your-AI/pick-your-ai-sustainability/commits/cad980ecc8e43a472ebe63c4360f94846d175a96/status?per_page=100) show the query identity. The structured record retains all six heads, counts, check IDs and source URLs. Completed list counts were below the requested page size; no additional page was omitted.

The organization-wide issue search `org:Pick-Your-AI is:issue CodeRabbit in:title,body` returned exactly [#56](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/56), parent [#8](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/8), and comparative service research [#61](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/61). The corresponding PR title/body search returned zero. Separate indexed PR searches for `reviewed-by:coderabbitai[bot]` and `commenter:coderabbitai[bot]` also returned zero, with `incomplete_results: false`. Indexed absence does not establish complete historical absence.

The public [.github root](https://github.com/Pick-Your-AI/.github/tree/01d392c1a42e93e6a11c17f4c165ad23988d376a) also had no such entry. However, [CodeRabbit's inheritance guide](https://docs.coderabbit.ai/configuration/configuration-inheritance) documents `organization/coderabbit/.coderabbit.yaml` as the central source and supports UI configuration. Applied to this organization, that location is `Pick-Your-AI/coderabbit/.coderabbit.yaml`. The [central repository API](https://api.github.com/repos/Pick-Your-AI/coderabbit) returned 404. A private or inaccessible repository and all UI settings remain Unknown. Root-file absence alone cannot resolve effective configuration.

The accepted [GitHub baseline](github-baseline.md), delivered by [#79](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/79) and accepted in [#57](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/57), supplies the existing CI/review foundation. Its [independent factual review](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/79#pullrequestreview-5570410486) accepted the corrected public-content rights assessment. This note consumes that baseline; it does not duplicate its audit, claim that source configuration proves settings or execution, or close the existing Apple/Android device and release work linked in #56.

### What is still unknown for every repository

Actual app installation and selected repositories; organization/account plan; effective repository/UI/central settings; granted permissions; code-cache and knowledge-base settings; applicable OSS allowance; account holder and operating owner; and whether any historical bot review addressed a still-relevant gap. The observed review sources are a reason to request a concrete inventory before activation, not a reason to install in order to discover the answer.

## Limits that affect useful coverage

The current [plans guide](https://docs.coderabbit.ai/management/plans) places OSS access separately from the summary-only Free plan: it describes Team features with OSS limits of **1–10 PR reviews per developer per hour**, an additional repository scope, and **100–300 files per review** after filtering. Allowances vary by community/popularity; the actual six-repository allocations are Unknown. It also requires **manual review requests for public repositories below ten stars**. Consequently five dated rows fall under that condition; Research's thirteen stars alone do not establish automatic-review configuration.

This is a material qualification to broad OSS marketing about reviews starting on the next PR. The operating guide's explicit threshold should govern the proposed setup decision until the provider clarifies any mismatch.

The [rate-limit guide](https://docs.coderabbit.ai/management/rate-limits) explains rolling event budgets and warns that a rate-limited review can produce a passing check even though no review ran. The explanatory comment is the relevant observation; an older approval can remain. A superseded review can also consume capacity without current-head feedback. Record actual reviewed commits, comments and incomplete attempts before treating the service as coverage. Batch useful changes rather than spend review events on repeated pushes.

The [pricing page](https://www.coderabbit.ai/pricing) separately describes optional usage-based paid reviews and administrator controls. A free public-repository offer is not authorization for metered reviews, paid agents or another tier. Current account billing settings and all overage exposure remain Unknown. For a later pilot, require the operator to demonstrate the intended free scope and absence of scheduled paid activation before use.

## Permissions, data, rights and continued obligations

| Area | Source finding and practical consequence |
| --- | --- |
| GitHub authority | The [installation guide](https://docs.coderabbit.ai/platforms/github-com) lists read/write access to checks, code, commit statuses, issues, PRs and workflows, alongside read-only metadata and other scopes. OAuth includes organization/team and email information. Prefer selected repositories if a pilot is authorized; the requested write authority deserves review even when ordinary review behavior does not edit workflows. Actual granted scopes are Unknown. |
| Code cache | The [cache guide](https://docs.coderabbit.ai/reference/caching) describes a default repository/dependency cache lasting at most seven days and an encryption exception for OSS projects. It documents `reviews.disable_cache: true`. This is distinct from AI-provider retention and knowledge-base storage; no claim of globally zero retention is justified. |
| Knowledge base | The [knowledge-base guide](https://docs.coderabbit.ai/knowledge-base) documents retained learnings and context, and `knowledge_base.opt_out: true` to disable/remove that stored data. It says removal is immediate and irreversible. Any later deletion is a separate authorized action with an evidence-preservation decision. No configuration was changed here. |
| Personal data | The [Privacy Policy](https://www.coderabbit.ai/privacy-policy), updated **2026-10-16**, covers account and usage information, service providers, purpose/legal retention and deletion requests. It describes US server processing and review-related embeddings. Provider privacy/security statements are documentary claims; no independent infrastructure audit was performed. |
| Processing agreement | The [DPA](https://www.coderabbit.ai/legal/dpa), incorporated by the Terms, distinguishes processing for the customer from account/usage data controlled by CodeRabbit. It covers international transfers, customer permissions, subprocessors and deletion with backup/legal exceptions. The [linked subprocessor list](https://trust.coderabbit.ai/subprocessors) exposed no readable text; actual recipient list and account-specific transfer terms remain unresolved. |
| Contract and publication | [Terms](https://www.coderabbit.ai/legal/terms-of-service), updated **2026-04-20**, require authority and data rights, describe third-party AI processing with no-code-training/zero-retention commitments, and restrict sensitive-data uses. Section 4.2 requires prior written consent to disclose service benchmark results. Sections 6 and 12 address conditional output rights and name/logo/OSS-review marketing. Section 5 describes Order Form renewals and 45-day nonrenewal notice. The actual agreement, any overrides and applicable renewal date are Unknown. |
| Portability | The [export guide](https://docs.coderabbit.ai/guides/data-export) describes Dashboard CSV exports whose ranges depend on plan/access; its metrics API requires Enterprise. Exports contain account/author identifiers and vendor estimates. This does not establish an OSS entitlement to complete review-history export, a backup, or independent time savings. Keep necessary project review decisions in the existing GitHub process. |
| Cancellation and renewal | [Subscription documentation](https://docs.coderabbit.ai/management/subscription-management) distinguishes trial, scheduled paid activation and cancellation at the end of a billing cycle; it says review history/configuration remain after cancellation. Product removal, subscription cancellation and data deletion need separate account-specific verification. No expiry or renewal promise is inferred for this project. |
| Reporting and independence | No project-specific grant reporting obligation or sponsor agreement was retrieved. A future offer must be checked for reports, branding, publicity, termination and restrictions before acceptance. Maintainers retain decisions about correctness and publication; service output and sponsorship must not determine project rankings or accepted findings. |

The proposed pilot is **internal process assessment**. Treat public comparison or benchmark publication as a separate rights decision under the cited Terms. It must not become employee/person performance scoring. Future operators must also resolve source-use rights before sending non-public code, issue context or other people's data. This research neither grants those rights nor establishes that a future applicant can meet them.

## Three applicant routes

| Applicant route | Present finding | Specific remaining gates |
| --- | --- | --- |
| Current community | **Conditionally Eligible for the documented public-product route; actual applicant qualification Unknown** | All six inspected repositories are public, but the person/entity that can accept terms, app ownership, installation and operating controls are unverified |
| Fiscal-sponsored project | **Conditional; sponsorship itself supplies no product entitlement** | Establish sponsor agreement, who controls repositories/accounts, contracting and data responsibilities, and the same public-product requirements |
| Independent 501(c)(3) | **Conditional; recognition supplies no automatic product entitlement** | Verify actual entity/authorized signer and the same account, repository, rights and operating conditions |

These are route analyses, not claims that fiscal sponsorship or 501(c)(3) recognition exists. The public program does not describe nonprofit recognition as its entry condition; no separate charitable discount or broader country entitlement was established. Geography, sanctions/contract compatibility and any account-specific requirement remain Unknown. Cash sponsorship needs its own recipient and offer analysis for all three routes.

## Concrete use case and measurement decision

The prospective public benefit is finding additional correctness, contract or security defects in changes to the open-source clients, website, research validators and leaderboard before maintainers accept them. The current snapshot demonstrates existing CI activity, not the marginal value of another reviewer. Do not replace required checks or existing reviewers based on a vendor effectiveness claim.

A future authorized pilot should be defined before activation:

1. **Identify the gap and baseline.** Select one repository and a finite cohort of eligible, ordinary PRs with a named technical owner and independent human reviewer. Record which existing tests, scanners and reviews already cover the proposed defect classes. The operator chooses the cohort and time budget from actual capacity; this note assigns no person or deadline.
2. **Capture exact attempts.** Retain PR/head, request and completion times, configuration and plan limits, actually reviewed files, findings, skipped/limited/superseded attempts and the original CI result. Separate a passing bot status from an executed review.
3. **Adjudicate usefulness.** A reviewer evaluates each distinct finding against source and reproducible evidence. Record accepted defect, duplicate/already-known issue, unsupported finding, disagreement and still-unresolved finding separately. A bot comment resolved or counted as accepted by the vendor is insufficient proof.
4. **Measure marginal effort.** Record actual integration, configuration, triage, correction, maintenance and removal time. Compare time for matched tasks or a prespecified alternating workflow, retaining uncertainty and selection bias. A small nonrandom cohort can guide an operating decision; it cannot establish a universal improvement or causal benchmark.
5. **Decide and exit.** Continue only if verified useful coverage outweighs observed burden within the selected free scope and reviewed rights. Otherwise stop through the authorized account owner, preserve project evidence, verify removed access/billing obligations and decide separately about data deletion.

No pilot observations exist in this deliverable. **Effort, usable value and all numeric scores remain null.** A defensible later valuation separates:

- actual cash received under a specific award;
- avoided expense that would otherwise have been incurred for the same useful service;
- measured maintainer time saved, reported as time unless an agreed cost basis exists; and
- integration, triage, ongoing administration, privacy/rights work and exit costs.

Free access has no assumed cash value. Do not use a paid list price, vendor-estimated review minutes, aggregate sponsorship pledge or issue count as realized benefit. Do not count the same avoided cost and saved time twice.

## Priority, review and follow-through

**P2** remains appropriate: the public offer is plausible, but an actual marginal need, operator capacity and account qualification are not yet established; there is no verified urgent external deadline. Under [the scoring rubric](../../docs/scoring-and-qualification.md), the eight weights remain 20/20/15/10/10/10/10/5. No component has been scored to substitute for the unresolved gate. Program verification, applicant qualification and permission to activate remain separate [lifecycle decisions](../../docs/operations-and-reporting.md).

The next decision is to independently accept this dated assessment. A later operator can then resolve the concrete questions below before choosing whether the optional pilot is justified:

| Question | Required evidence |
| --- | --- |
| Is there an existing installation or subscription? | Authorized account inventory: app ID/selected repositories, actual plan, scheduled billing and effective settings |
| Is another reviewer needed? | Current existing-coverage inventory and an explicit defect class or workload the pilot can test |
| Are rights and authority sufficient? | Actual contracting recipient, consent/data scope and accepted publication/branding/transfer conditions |
| Can the service be operated and exited sustainably? | Assigned operator/reviewer capacity, actual allowances, retained project records, export/removal and billing/deletion responsibilities |

Independent acceptance must name the **actual reviewed revision**, a substantive source review and the issue/PR receipt. Local schema/link checks establish consistency only. Until that acceptance is recorded, this snapshot keeps the opportunity at **Discovered** and the research work **In Review**. A later acceptance record may advance the research/Verified stage without claiming Qualified, Submitted, Awarded or Activated.

The existing [#67 intake-method owner](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/67), [#21 compute-demand work](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/21), [#58 JetBrains research](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/58), comparative [#61](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/61) and parent [#8](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/8) retain their own scope. No duplicate provider opportunity or installation task is created.

## Source access and freshness

All provider links above were inspected on **2026-10-19**. The current policy dates are distinguished from access date; undated documentation is identified by its URL and access date, not an invented version. Governing conditions are taken from current official pages rather than historical announcement totals or testimonials.

Two endpoints remain explicitly unverified: the public application exposed no readable intake fields, and the DPA-linked subprocessor page returned no readable content. A documentation `.md` route for GitHub setup returned an unsupported-content response; the complete relevant HTML guide was then read successfully. The central GitHub repository returned 404, whose access ambiguity is retained above. No login, hidden installation endpoint or private document was probed.

[The freshness register](../../data/research-freshness.json) tracks the governing URLs and the attempted endpoints. Recheck on a plan/permission/privacy/terms change, new installation evidence, changed repository visibility or thresholds, and **before any activation, billing, sponsorship or public benchmark decision**. The monthly research procedure creates no invented application due date. This record does not promise a future operator's time.
