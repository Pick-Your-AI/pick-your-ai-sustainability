# Monthly sustainability dashboard review

Owner issue: [E09-06 / #72](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/72). Use with the [populated dashboard](../docs/dashboard.md), [operations procedure](../docs/operations-and-reporting.md), [freshness method](../docs/research-freshness.md) and [risk definitions](../docs/risk-indicators.md).

This is an unfilled maintenance record. A monthly cadence is a proposed review procedure, not an installed automation, a source expiry rule, a deadline or a contributor appointment. **Recurring coordinator and independent reviewer: Unassigned.** Existing authorized engineering work can continue within its covered scope. Actual applications, agreements, financial activity and operating responsibilities require their own accepted authority.

## 1. Accept the bounded review responsibility

| Field | Recorded value |
| --- | --- |
| Reporting period and actual observation window, including timezone | Unknown / not recorded |
| Coordinator, accepted scope and availability | Unassigned |
| Independent reviewer and accepted review scope | Unassigned |
| Source cutoff, canonical full revision and immutable report identity | Unknown / not recorded |
| Repository PR / issue and exact review revision | Unknown / not recorded |
| Actual operating roles affected by this report | Unknown; research assignments are insufficient |

Record acceptance of the reporting work before treating a person as a recurring owner. An unfilled role remains a visible maintenance gap; it does not invalidate another person's existing engineering authorization.

## 2. Retain the exact inputs and actual observations

Create a **new dated audit**, keeping the earlier report's audit and review history intact. Retain all eight source files' paths, full Git revisions, Git blob IDs, byte lengths and SHA256 digests. The four canonical data inputs must share the declared canonical revision. Method inputs may have separately stated revisions and must have actual accepted findings/delivery links. If any definition is still pending, say so and do not claim whole-report acceptance.

Record actual GitHub request URLs, the observation start and completion timestamps, every returned issue ID/state, page and total, response completeness and errors. Exclude PRs from the issue population. Retain typed issue and PR totals separately for each of the six repositories. A one-item search sample is not its total. Prove page coverage and unique identities; changing counts during pagination require reconciliation or an explicit Unknown. Search observations are bounded reads, not an atomic snapshot.

Read Project fields only through an available authorized capability. If unavailable, preserve the actual error and the resulting visibility limit. A connector route rejection does not establish server privacy, absence or zero items. Do not substitute an old Project audit, issue state or assignee count for current Project data.

Provider research is a separate scope: keep original publication, successful check, latest attempt and review dates. If a current action requires a recheck, follow the freshness procedure and preserve the actual access result, affected claim/program/round/jurisdiction and unresolved conflict. Do not refresh all dates because a dashboard ran.

## 3. Recompute and reconcile separate populations

| Section | Required calculation and review |
| --- | --- |
| Research work | Count distinct canonical program IDs once. Compare the pipeline projection to the canonical register. Keep literal work statuses, review-pointer coverage, research assignments and GitHub issue states separate. Aliases and repeated rounds add no program count. |
| Opportunity lifecycle | Retain each program's literal stage, exact action gate and all three applicant routes. A Done research record may remain Discovered. Missing applicant/authority facts remain Unknown. |
| Sources and deadlines | Separate tracked URL identities, program memberships, reference unions, additional endpoints and missing successful dates. No age-only stale count. Preserve date-only or organization-local precision; unknown timezone means no invented UTC. |
| Resource realization | Establish the actual event population, recipient, fund/custodian, currency, period and evidence before computing anything. Separate cash received, commitments, usable noncash units, actual avoided cost and expenditure. Never combine currencies, unused credit value or loan prices. |
| Obligations | Use actual accepted terms, due-rule/trigger, complete scope, accepted responsible role, planned/delivered evidence and independent review. A draft, dispatch or acknowledgment is not automatically provider acceptance or closeout. |
| Unresolved needs and risks | Distinguish planning from an accepted actual workload/critical-operation population. Apply each accepted risk definition to its own complete numerator and denominator. Unknown coverage is Unknown; a complete evidenced zero denominator is Not applicable with its scope, not low risk. |

The initial builder deliberately leaves actual financial, benefits, obligation and risk totals Unknown because those complete populations do not exist in its inputs. Do not replace null with zero or populate a total from a provider maximum. Adding a new actual ledger or a risk calculation requires a reviewed implementation and tests for its population, category, unit, currency, period and incomplete-evidence boundaries.

| Discrepancy or limitation | Exact source / affected metric | Resolution or retained Unknown | Reviewer disposition |
| --- | --- | --- | --- |
| Not recorded | Unknown | Unknown | Unassigned |

Repair a canonical error through its owning review path, then create a new fixed report revision. Otherwise preserve the conflict and its effect on the count. Do not silently edit history, research status, a source observation or a Project field to make totals agree.

## 4. Reproduce and independently accept the actual report

With the stated Git objects available, run the offline builder against the **new audit path**, then retain the generated JSON and Markdown identities. A source archive can use `--input-directory` with all eight exact pinned files; their byte lengths and hashes must still match. Missing Git objects require an explicit fetch of the cited public revisions before the offline command. Never substitute newer worktree files.

```sh
python3 scripts/build_dashboard.py --audit data/audits/NEW-DATED-AUDIT.json --format json
python3 scripts/build_dashboard.py --audit data/audits/NEW-DATED-AUDIT.json --format markdown --output docs/dashboard.md
python3 scripts/build_dashboard.py --audit data/audits/NEW-DATED-AUDIT.json --format markdown --check docs/dashboard.md
```

`NEW-DATED-AUDIT.json` is a placeholder, not an existing source or a completed command. The independent reviewer must recompute the actual populated report, inspect all response coverage and joins, and reason through missing versus zero populations, currencies, repeat rounds, negated review text, source-date scope, deadlines and unassigned roles. A passing schema check or test suite is not findings acceptance.

| Completion evidence | Value |
| --- | --- |
| Audit and generated output byte lengths / SHA256 | Unknown / not recorded |
| Exact independent recomputation, discrepancies and limitations accepted | Pending |
| Independent review URL and complete reviewed revision | Unknown / not recorded |
| Accepted-main revision, delivery receipt and preservation of prior audits | Pending |
| Remaining questions, prioritized follow-ups and accepted owners | Unknown / Unassigned |
| Next review date accepted by responsible contributors | Unknown / not assigned |

Publish a concrete source-linked report and record the actual accepted revision and independent review in #72. The reporting result establishes operating visibility within its evidence scope; it does not establish submission, award, receipt, activation, financial authority or a legal/operating appointment.
