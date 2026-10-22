# Research freshness, six-hour checks and monthly review

Owner: [E09-04 #70](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/70). Status: operating procedure proposed for independent acceptance. Recurring coordinator and reviewer: **Unassigned**. Human review assignments remain unassigned. The six-hour access/change monitor below implements Andrew’s 2026-10-22 cadence decision after its workflow is merged.

## Purpose and governing inputs

Keep each recommendation traceable to the exact program, applicant route, claim and source observation that support it. The monthly review finds work requiring investigation; it does not renew provider evidence or establish eligibility by running on a calendar.

This procedure consumes the [provider intake workflow](../templates/provider-research.md), its [structured-record mapping](../data/README.md), the [research method](research-methodology.md), and the [authorization process](workflow-and-authorization.md). The full E09-01 input acceptance remains tracked in [#67](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/67); its initial delivered examples are not a substitute for that acceptance. E09-04's final acceptance must link the accepted input and this procedure's independent review.

The upstream [source policy at research `daac1dae7348c8f4f1011c85979068c8ba6c1489`](https://github.com/Pick-Your-AI/pick-your-ai-research/blob/daac1dae7348c8f4f1011c85979068c8ba6c1489/research/T0-configuration/catalog-data-sources.md), read 2026-10-19, distinguishes retained version facts from current-state claims. Apply that distinction without adding an arbitrary evidence lifetime:

- A permitted historical observation keeps its source, date, round and limits. A newer round does not rewrite what the earlier one offered.
- Current availability, prices, eligibility, quotas, account conditions and governing terms need applicable current evidence before a current recommendation or action.
- An explicit validity end can disqualify a claim for current use. Elapsed time alone does not disprove an immutable fact.
- A changed disclosure or reuse restriction needs its own review, including any affected historical publication; retaining history does not override that restriction.

## Register and observation convention

The unique program record remains in [opportunities.json](../data/opportunities.json). The URL/membership index remains in [research-freshness.json](../data/research-freshness.json). Detailed observations and decisions belong in a dated [freshness review record](../templates/freshness-review.md) linked from the owning issue. This adds no opportunity identity or lifecycle stage.

Use one observation for one source, claim and applicable scope. A shared URL can support several programs or claims; checking one section does not refresh the others.

| Information | Required treatment |
| --- | --- |
| Program and claim identity | Existing opportunity ID and issue; exact field or quoted/paraphrased claim; provider/program/round/version and applicable jurisdiction, route, account, product and intended use. |
| Retrieval attempt | Actual date/time if available, requested URL, final URL after redirects, outcome and access limit. Distinguish success with relevant content, irrelevant/partial content, sign-in wall, access error and not attempted. HTTP success alone proves no claim. |
| Successful source check | Preserve the actual successful access date and the precise content inspected. A record-only review, linked endpoint, failed attempt or synthetic exercise cannot advance `last_verified`. |
| Prior observation | Link the prior immutable record/revision and retain its original wording, scope and dates. Add the new observation and resulting decision; do not erase a closed round or source conflict. |
| Current consequence | State which claim remains supported, becomes disputed, is known unavailable/ineligible for this use, or is Not Verified. An application-page failure need not erase a separately supported membership price. |
| Unresolved fields | Name missing applicant facts, uninspected endpoints, uncertain account agreements, unknown limits and required decisions. Null is unknown, not zero, no restriction or no deadline. |
| Next verification | Record an event-based basis and next research action. Set an internal date only when actually chosen under applicable authorization. Keep owner/reviewer unassigned until accepted. |
| Independent decision | Actual reviewer identity, exact reviewed revision, sources actually read, accepted scope, corrections and limitations. Do not attribute a later repository review as a new provider retrieval. |

Keep the latest observation's access result distinct from the latest *successful* check. For example, after a previously successful source becomes unavailable, retain the old successful date, add the failed attempt/result, and mark affected current claims Not Verified. If access was never attempted, preserve null attempt and verification dates.

Update the canonical opportunity and required pipeline/freshness memberships together only when a reviewed observation justifies a change. Preserve unrelated rows and concurrent owners. A dated audit is a snapshot, so later legitimate changes do not require rewriting its original counts.

## Authorized automated source checks

Andrew authorized rechecking sources every 4–6 hours and whenever something changes on 2026-10-22. The implementation chooses **six hours**, recorded in `check_policy.interval_hours` in the [register](../data/research-freshness.json). This operational interval supersedes the previously unresolved automation cadence; the immutable dated readbacks retain what was unknown at their cutoffs. Monthly program review and before-reliance claim review still apply.

The [source-freshness workflow](../.github/workflows/source-freshness.yml) executes on standard GitHub-hosted Ubuntu runners at **00:23, 06:23, 12:23 and 18:23 UTC** (`23 */6 * * *`). Main-branch changes under `data/`, `research/`, `templates/`, the research procedure documents and checker/workflow/test files trigger an immediate full recheck. Pull requests run offline tests, validation and a no-network plan only. Maintainers can use **Actions → Check source freshness → Run workflow** on main when notified of an external change. Provider websites have no webhook here: polling detects their changes; a known change warrants the manual trigger rather than waiting for cron. Event runs check all entries even if not due yet.

The [checker](../scripts/check_source_freshness.py) emits `freshness-report.json`, linked as a run artifact, with per-source outcomes, redirect chains, response hashes, change flags and precise UTC timestamps. It reads the `source-freshness` artifact from the latest successful canonical main-branch run of this workflow (push, schedule or manual event only); PR/fork artifacts are excluded as a comparison baseline. An absent baseline means a first observation, never “unchanged.” A failed baseline download or invalid report fails the run instead of claiming a comparison. Reports are retained **seven days**, so old run observations remain available without a growing commit history. No raw page bodies are published. The job writes no commits, issues, PRs, Projects or canonical research decisions.

Timestamp rules:

- `last_checked_at` is the actual completion of an automated public check or robots preflight, including blocked/failed access; it is not a successful claim review.
- `next_check_at = last_checked_at + 6 hours`, using timezone-aware UTC arithmetic. An entry with no previous attempt is immediately due at plan generation time. A run-budget skip preserves the old last attempt and due time, or remains immediately due.
- `content_checked_at` and `content_final_url` retain the last comparable public response separately from a failed latest attempt. Redirect and byte-hash changes flag investigation; dynamic content may change without a material claim changing. HTTP 304 reuses only the prior matching-resource digest.
- `last_verified`, `next_verification_date`, deadlines, histories, program dispositions and pipeline evidence remain untouched. Human review still determines whether a source supports its precise cited claim. Neither HTTP 200 nor an unchanged byte hash establishes eligibility, terms or current application admission.

Public retrieval uses an identified agent, at least two seconds between requests (also honoring longer supported robots delays), cached per-origin robots checks, conditional GET when available, bounded redirects, a 2 MB body limit, a 30-second absolute per-request deadline, a 35-minute collection budget and a 45-minute job timeout. It does not execute scripts, load subresources, authenticate, submit forms, retry 403/429 or solve challenges. Robots denial/unavailable policy and supported crawl delays over 60 seconds prevent target retrieval. Only public HTTPS on port 443 is accepted; every connection resolves and pins a public address while verifying TLS for the original hostname. Redirect destinations are checked independently. A partial or blocked response preserves the prior comparable digest without calling it unchanged.

The run summary gives outcome/change counts; download the JSON for exact URLs, next due times and access limitations. Blocked/dead/changed results require the canonical researcher’s event-based review before reliance; a budget-exhausted run fails visibly and retains a partial report. No individual review commitment is assigned by the monitor.

This public repository uses standard GitHub-hosted runners: **no runner compute charge**, server, model or paid API is required under [GitHub’s public-repository pricing](https://docs.github.com/en/billing/concepts/product-billing/github-actions). Report artifacts have short retention; any account-level storage billing follows GitHub’s separate storage allowance. No cache or raw-source archive is created. GitHub schedules are best effort: they may be delayed/dropped, and public-repository schedules can be disabled after 60 days without repository activity ([schedule limitations](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)). This is a six-hour intended cadence, not a guaranteed six-hour service-level bound. Check the latest successful run when relying on monitoring. The schedule starts only after merge to main; creating its PR does not activate cron.

## Recheck triggers and resulting action

| Trigger | Review action and boundary |
| --- | --- |
| Six-hour automated/public change check | Record access, redirects and comparable content changes; keep claim-verification fields unchanged and route material findings for human review. |
| Monthly program review | Read every registered program, including retained declined/ineligible or closed records. Identify missing or changed evidence; a historical record need not be actively pursued. |
| Current recommendation, outreach, application, acceptance, activation or renewal | Read the applicable current program, eligibility, restrictions and intake sources for the specific applicant and action. Confirm any actual terms and authority separately. |
| Reopened or new round, redirect, closure or changed provider terms | Compare exact program/round identity and applicability. Preserve the prior outcome. Opening an intake does not qualify the project or approve pursuit. |
| Contradictory source or changed price, quota, rights or benefit | Preserve both observations, normalize scope, and follow the research method's source hierarchy. Leave unresolved material claims disputed/Not Verified; do not choose a financially convenient interpretation. |
| Applicant/entity, fiscal sponsor, account, monetization or use-case change | Reassess each affected route and restriction. A sponsor's status or nonprofit recognition does not establish academic eligibility, account entitlement or provider admission. |
| Explicit deadline/validity, renewal, expiry or reporting event | Check the actual governing round/agreement and dates. Keep expired current eligibility separate from retained historical evidence and any outstanding obligations. |
| Failed or incomplete access | Retain permitted dated findings, record the precise failure, and remove unsupported current claims. Route a new public-source check or authorized account review; do not infer hidden terms. |

## Four distinct kinds of date

1. **Source event/publication/effective date:** when the publisher says the fact or terms apply, at the stated precision.
2. **Source access date:** when that content was actually inspected; retain attempted and successful dates separately.
3. **Analysis/review date:** when a researcher or reviewer assessed the record. It never silently replaces a source date.
4. **Application deadline or internal action date:** separate fields and meanings. An external deadline needs the exact program/round and official source. An internal date needs an actual selected action and applicable authority.

For an external cutoff, retain the published local date, time and timezone and, only when unambiguous, its UTC conversion. If only a date is published, preserve date-only precision. If the cutoff is in the submitting organization's local time but its timezone is unknown, leave UTC null. Do not use the researcher's timezone, midnight or the next monthly meeting as a substitute. Unknown deadlines remain null; “rolling” needs source evidence and does not imply unlimited availability.

## Monthly review agenda and output

1. Pin the repository/register revision and read the live issue, Project, prerequisite and PR state. Record the retrieval cutoff and pagination/access limits. Identify active writers before proposing updates.
2. Inventory all programs and their governing, program and application endpoints. List missing successful checks, failed attempts, unresolved claims, closed or changed rounds, and explicitly dated obligations.
3. Select bounded source checks from those findings, prioritizing an actual decision or deadline. Record each attempted source independently using the review template. No bulk date advancement is permitted.
4. Reassess affected claims and all three applicant routes, value assumptions and obligations. Separate cash, potential avoided cost and realized support. Preserve the established ineligible/Not Pursuing outcome unless new applicable evidence changes it.
5. Obtain independent review of material findings, exact restrictions, significant deadlines and any recommended next action. Resolve corrections before changing qualification or recommending an externally consequential action.
6. Reconcile justified program/pipeline/freshness changes and read back actual issue/Project updates. Report unavailable mutation or access capabilities precisely; a local file is not proof that remote fields changed.
7. Publish the dated review summary, accepted decisions, outstanding questions, owners who actually accepted work, and next event-based actions. Link it from the existing issue/dashboard rather than silently scheduling new work.

Any existing scheduled task retains its own recorded authority, scope and owner. Before changing or adding a schedule, inspect the actual task and applicable user authorization; do not duplicate a monitor or invent a person's recurring commitment. A schedule can prompt research, but it cannot certify a provider source it did not retrieve.

## First readback

The [2026-10-19 record audit](research-freshness-readback-2026-10-19.md) and its [machine-readable snapshot](../data/audits/freshness-readback-2026-10-19.json) inspect accepted sustainability revision `cad980ecc8e43a472ebe63c4360f94846d175a96`. They identify all 39 program memberships, 17 endpoints without a recorded successful check, existing source observations, unresolved fields and the recorded deadline precision. They do not refresh all 72 external sources or declare records stale merely because time passed.

## Independent walkthrough

The following are deliberately **synthetic process cases**, not provider observations, actual rounds or live register updates. A reviewer must work through the expected results and record the exact procedure revision in the owning issue or PR. Do not populate a provider's access date from these cases.

| Case and supplied evidence | Required result | Check that must fail acceptance |
| --- | --- | --- |
| Reopened round: retained synthetic round A is closed; a newly inspected official notice explicitly opens synthetic round B with a date-only cutoff. Applicant facts and B's full terms are unknown. | Retain A closed. Add B's actual observation in the exercise; current intake may be recorded open for B only. Keep applicant qualification and action gate unresolved; keep cutoff time/timezone/UTC null. | Reopening by elapsed time, erasing A, inferring eligibility from intake, or inventing midnight/UTC. |
| Conflicting terms: a general synthetic overview promises unrestricted credits, while an equally applicable current governing agreement excludes benchmark publication. | Preserve both sources and deciding scope. The governing restriction blocks the proposed public-benchmark use; another unrelated use is not automatically excluded. If agreement applicability is itself unknown, keep that use unresolved. | Counting excluded credits as usable value, discarding the restriction, or extending a decision to a different account/use. |
| Unavailable page: a synthetic form was checked earlier, but the current attempt returns an access error; a separate program page still loads. | Keep the earlier successful form date, append the failed attempt/result, and mark current form requirements Not Verified. Retain only the separately supported program-page claims. | Refreshing the form's verification date from the error, successful homepage, review date or link discovery. |

## Applicability, value and acceptance

Priority recommendation: **P2**. This foundational operating work prevents unsupported qualification and supports the existing pipeline; no source-backed immediate deadline for the process has been identified. Recommended disposition: adopt the procedure after exact independent review and accepted E09-01 intake, then use its actual readback findings to select bounded source investigations.

This is an operating process, so a provider application round, award amount, currency and program eligibility are Not applicable to the process itself. It is used separately for the present community, a fiscal-sponsored project and an independently recognized 501(c)(3); it establishes none of those applicant facts. All benefit types use the same traceability convention, with the actual provider's reporting, branding, publication, privacy, portability, renewal, overage and independence conditions retained where applicable.

The concrete public-benefit use is to keep this repository's support recommendations reproducible and prevent unsupported current eligibility or value from entering the six repositories' funding decisions. No cash or avoided-cost amount is assigned to the process. Effort can be estimated from observed records reviewed, sources attempted and actual elapsed work in a completed review; there is no supported hours-per-source or recurring staffing commitment yet.

Final E09-04 acceptance must link the exact delivered procedure, first readback, independent walkthrough and accepted E09-01 input. Any remaining source/applicant questions stay with their canonical investigations. Completing this operating process establishes no application, award, receipt, activation or organization-wide legal authority.
