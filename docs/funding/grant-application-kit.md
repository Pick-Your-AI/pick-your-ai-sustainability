# Grant application kit

Issue [#23 / E02-05](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/23) · Prepared **2026-10-19 UTC** · **Findings independently accepted; application kit remains a draft**.

This is the canonical reusable application index and drafting pack. Its source baseline is accepted main [`bfa30ca5`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/tree/bfa30ca5754e2068b06f7ff5fbf846cb39c6972b). It combines existing project material, a concrete proposed work package, provider adaptation instructions and the evidence still needed for an actual application. It is **P1 foundational work**, with numerical opportunity score, application intake and provider deadline **Not applicable to the kit itself**. It is not a new funding program or an application.

**Current disposition:** the reusable evidence-and-Unknown drafting method and all eleven research criteria have [independently accepted findings](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/23#issuecomment-6275839960); actual application readiness remains unresolved. Budget [#20](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/20) has independently accepted findings but undelivered [PR #102](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/102). The measurement design in [#22](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/22) is accepted and delivered. Neither dependency supplies an adopted financial request, measured public benefit or an eligible applicant.

## 1. Canonical packet index

Use the source document for each claim. When preparing a particular application, record its exact commit or document version in one manifest; do not copy live figures into several maintained documents. These relative links navigate this checkout. The immutable baseline above identifies the versions inspected for this kit.

| Application component | Canonical material | What it can support and what remains unresolved |
| --- | --- | --- |
| Project overview and mission | [Existing grant narrative](../grant-narrative-draft.md), [charter](../charter.md), [program boundaries](../../README.md#current-boundaries) | Public project direction and proposed benefits. Charter adoption, charitable qualification, actual reach and achieved impact are separate. |
| Applicant and representation | [Entity, asset and administrative baseline](../nonprofit/entity-baseline.md), [structure comparison](../nonprofit/structure-decision-brief.md), [host comparison](../nonprofit/fiscal-sponsorship-comparison.md) | Public project references and actual Unknowns. An account name, repository permission or researched host is not a verified applicant, asset owner or signer. |
| Need and receiving work | [Accepted N01–N09 needs assessment](needs-assessment.md), with [actual findings review](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/96#pullrequestreview-5571462106) | The defined technical/operating questions, existing capabilities and unmeasured costs. Historical execution receipts retain their own dates and scopes; they are not current bills or a complete capacity forecast. |
| Budget and justification | [Guide at `b24176fb`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/b24176fb5ad81a4b8722effed48bd6c002254173/docs/funding/operating-budget.md), [canonical JSON at the same revision](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/b24176fb5ad81a4b8722effed48bd6c002254173/data/budget/operating-budget.json), [accepted substantive review](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/102#pullrequestreview-5572495606) | The reviewed planning method and explicit unknown inputs. The substantive acceptance is at `236d7644`; the inspected two-file `b24176fb` continuation records that acceptance without changing arithmetic. These files are not yet on this kit's main baseline. Keep #20 delivery pending and replace these navigation links with the actual accepted-main receipt when delivered, preserving this history. |
| Outcomes and evaluation | [Public-benefit measurement plan](public-benefit-measurement-plan.md), [observation template](../../templates/public-benefit-observation.md), [synthetic example](../../templates/examples/public-benefit-observation-synthetic.md) | Accepted measurement design, [reviewed at `971cd166`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/103#pullrequestreview-5572379791) and [delivered at `16a0f2c9`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/commit/16a0f2c9dea0e502d6a092e3b25dfdf7c4d0846c). Baselines and observed outcomes remain Unknown; the proposed targets are not achieved results. |
| Program-specific evidence | [Opportunity register](../../data/opportunities.json), [pipeline](../funding-pipeline.md), [NLnet assessment](../../data/opportunities/nlnet-programs.json), [Secure Open Source Fund assessment](../../data/opportunities/github-secure-open-source-fund.json) | Reuse the exact existing opportunity ID, round, disposition, source observations and unresolved eligibility. A kit does not advance a provider stage or reopen a closed/ineligible route. |
| Rights, neutrality and restrictions | [Award mechanisms and restrictions](award-mechanisms-and-restrictions.md), [vendor-neutrality draft](../policies/vendor-neutrality-and-sponsorship-ethics-draft.md), [IP/stewardship #17](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/17) | Existing research and draft controls. Verify rights and actual agreement terms for the selected work; do not assert blanket ownership or license compatibility for every repository, asset or AI-assisted contribution. |
| Exact application and later reporting | [Concrete action record](../../templates/application-approval.md), [financial controls draft](../operations/financial-controls-draft.md), [operations/reporting](../operations-and-reporting.md), [benefit/obligation report](../../templates/award-report.md) | Reuse the existing identity, evidence, scope, actual decision and execution fields. Engineering authorization remains effective. No blank form or kit review appoints a financial representative or establishes an external submission. |

The older [budget assumptions](../budget-assumptions.md) remain historical planning input; they are not a replacement for #20's calculator and cannot supply a full grant budget. Never add an alternative ceiling to the allocation it bounds, count shared resources twice, treat unknown actuals as zero, or translate synthetic product prices into community operating expense.

## 2. Reusable project narrative

The existing narrative remains the longer source draft. The following concise version is a reusable **draft**, to be checked against the selected source manifest before external use:

> Pick Your AI publishes project source and research to help people examine AI system choices. Its proposed public benefits include clearer evidence, explicit uncertainty, reproducibility, interoperability and accessible decision support. The project includes research, web and mobile application work and contributor tools. Particular artifacts may be prototypes or use synthetic inputs; each achievement must be tied to its own reviewed source and result. A proposed funded package would improve a defined part of this work. Applicant identity, eligibility, request size, beneficiary baseline and measured improvement remain to be established.

For a real provider form, replace the final two sentences with the actual selected work, supported applicant facts and request. Do not remove the prototype/synthetic qualification while retaining claims based on those artifacts. A published source, passing automated check, merged PR or prepared research instrument is evidence of that output, not proof of adoption, human learning, charitable status, revenue, an operational service or complete device coverage.

Use three explicit labels in every working draft:

| Label | Required treatment |
| --- | --- |
| **Observed** | Identify the exact artifact, source/result date, method, actual reviewer and claim boundary. A reader must be able to distinguish original execution from a later source review. |
| **Proposed** | Identify the future work, receiving issue, intended output and how it will be measured. A target, estimated effort or planned benefit stays proposed until separately observed. |
| **Unknown** | State the missing fact and the evidence needed. Do not replace the unknown with plausible prose, a zero, an assumed institution or an absent person's name. |

A claim manifest can use: **claim ID; draft section; exact claim; label; source revision and path; original result if any; scope/date; rights/disclosure finding; reviewer and actual finding; correction or remaining question**. No complete manifest for a submitted application exists yet.

## 3. Concrete proposed work package

**Illustrative proposal: traceable evidence for one bounded comparison cohort.** This is a proposed package, not an approved research study, selected data acquisition or accomplished outcome.

The public-benefit hypothesis is that a person or reviewer can distinguish a result's evidence grade, recover its material conditions, and recognize when a comparison must remain Unknown. The selected cohort, actual user need and impact baseline are unresolved. This package consumes N07 (evidence admission) and N08 (independent review) in the accepted needs assessment. It keeps [Website #15](https://github.com/Pick-Your-AI/pick-your-ai-website/issues/15) and the canonical Research evidence/admission policy as the receiving owners; it creates no second catalog or replacement source policy.

| Proposed output | Concrete acceptance evidence | Outcome link and present limit |
| --- | --- | --- |
| Freeze a finite cohort and an evidence manifest | Named receiving issue, exact source/data versions, rights finding, claim population and exclusions before evaluation | PB-03 traceability. Actual cohort and source permissions are Unknown. |
| Prepare evidence cards or admission records with explicit gaps | Every in-scope claim links its source conditions and grade; inaccessible or unsupported claims remain visibly qualified and tracked | PB-03. The denominator is all unique in-scope claims actually audited, including failed retrievals. Report coverage of the declared audit population separately. |
| Supply a reproducible bounded fixture or method | Exact input/environment, expected result or prospectively chosen tolerance, complete original outcome and independent replay finding | PB-04. A synthetic contract replay remains separate from empirical hardware reproduction. Blocked/unrun work is disclosed separately. |
| Correct consequential evidence or access defects | Original finding, scoped correction and relevant review/retest; retain failed originals and pending work | PB-07. No numerical improvement is claimed before observation. |
| Publish the cleared method and result | Public-safe source/rubric and a scoped review; no confidential source or participant data | Provides reusable evidence. It does not establish an effect on users or a whole-service accessibility claim. |

Use the accepted measurement plan's exact units, denominator and missingness rules. Do not add unlike PB measures into a single impact score. PB-01/PB-02/PB-05 require a suitable actual human-task protocol before claiming a learning, selection or accessibility outcome. Ordinary assistive technology is not moderator help. An observed assisted success does not become an unassisted target success.

[Research #63](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/63) retains its participant protocol and unresolved operational records. This example neither selects its optional task module nor authorizes participant contact, trials, recordings or use of private notes. A source-only audit can proceed within existing engineering scope.

### Funding-request paragraph to complete for a selected program

> We propose [specific work package and receiving issue] over [supported period]. We request [benefit type, amount/currency or finite resource units] for [eligible activities tied to the canonical need IDs]. The budget is generated from [exact accepted budget revision and recorded scenario inputs]; uncovered costs, existing support and restrictions are [supported findings or Unknown]. We will deliver [versioned outputs] and evaluate [selected PB measures and their declared populations]. Existing results are limited to [exact observed evidence]; [remaining benefits] are proposed. [Actual applicant and verified representative] will be responsible for [the particular obligations supported by the reviewed terms].

This is deliberately incomplete. Unknown amount, period, applicant, workload or evidence cannot be resolved by substituting attractive text. For planning-only funding, adapt the outputs to actual eligible planning activities; do not relabel product development as planning.

## 4. Budget, support value and effort

The selected application must consume one frozen #20 input set and its reproducible calculator output. Record currency, period, scenario and source dates; distinguish proposed amounts from actual expense. State whether the result is partial because inputs remain Unknown. The accepted planning model does not establish a complete organization budget, actual balances, an adopted scenario or spending authority.

Prepare a resource-to-output crosswalk: **Need ID → specific output → existing capacity → incremental eligible units/period → dated rate → cash cost → covered benefit → uncovered cost/fees/taxes → obligation/expiry → evidence and owner**. Quantities, rates and effort stay Unknown until supported. #21 retains compute-demand modeling; a funding narrative cannot manufacture a finite GPU cohort, undisclosed publisher run or missing equipment inventory.

Report each support class separately:

- **Cash requested, awarded and received:** different amounts/stages with their own evidence.
- **Credits, discounts and service units:** advertised maxima differ from usable eligibility, activation, covered products and actual usage.
- **Equipment or professional help:** distinguish ownership, loan, access and services; include support, return and other actual duties where applicable.
- **Realized avoided cost:** requires the same necessary resource, an evidenced purchase counterfactual and actual eligible coverage. Do not add credit face value, displaced purchase value and donated time as if they were three cash receipts.

Use actual task decomposition for effort: evidence preparation, technical delivery, independent review, provider form work, mandatory participation, reporting and closeout. Record hours only when estimated with an explicit method or observed with a stated clock. Neither source-code volume nor the length of this kit is an effort estimate. Overall preparation/operating hours and incremental support value remain **Unknown**.

## 5. Provider adaptation examples

These are concrete examples of how the same packet changes by provider. They do not select a program or replace the canonical owner. Current public pages were inspected **2026-10-19**; recheck the actual call and form before external use, retaining this dated observation.

| Existing record / benefit | Current intake observation and actual applicant status | Required adaptation |
| --- | --- | --- |
| **NLNET-CODESUPPLY**; related **NLNET-RESTACK** and **NLNET-NGI0-COMMONS** in [#25](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/25). Technical-development grant research. | The common form shows **3 November 2026, 12:00 CET** (11:00 UTC). Its generic deadline does not qualify any project. The accepted record leaves CodeSupply eligibility Unknown, excludes the ordinary AI-builder scope from Restack absent the recorded exception evidence, and retains Commons as closed intake. | Select the exact eligible fund/work first. Adapt the summary, task/effort/rate breakdown, related-work comparison, challenges, ecosystem and contributor experience to the live form. State other funding truthfully. Preserve required open-source rights and the fund's geographic conditions. Apply the separate AI instructions below. [G1, G2] |
| **NSF-PESOSE-26-506**, [#30](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/30). Research/ecosystem grant. | The next listed deadline after this review is **2 March 2027**, 17:00 in the submitting organization's local time. The actual organization/timezone, program admission, PI/team eligibility and registration remain Unknown; a universal UTC time is not justified. | Select a supported track and eligible lead. Use the due-date PAPPG and solicitation, including current product/testing/user/contributor evidence and team qualifications. Track 1 funds planning; Tracks 1/2 have experiential requirements with a conditional prior-participation waiver. Check required sections, limits, security/governance/evaluation content and the prohibition on voluntary committed cost sharing. No team appointment, registration or matching pledge is inferred. [G3] |
| **GITHUB-SECURE-OSS-FUND**, [#26](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/26). Maintainer funding plus security education/services. | The FAQ describes rolling applications; an actual selection date is Unknown. The accepted program research leaves this project's applicant eligibility Unknown. | Identify actual maintainers, project license/governance, demonstrated adoption and a bounded security-improvement plan. Verify the applicant's stated personal/regional conditions privately. Map participation and later check-ins to actual availability. The FAQ's total is **20 hours** including the initial program and both follow-ups, not three additive versions of one commitment. Keep cash tranches, tools and contingent credits separate. Do not promise use of an AI tool or paid service that the project's authorization excludes. [G4] |

The deadline observations are provider deadlines, not internal work reservations. A rolling form does not establish continuous selection, an award or immediately available cash. These examples introduce no duplicate opportunity records and refresh no unrelated source observations.

### AI provenance and responsible authorship

NLnet's form uses broad language discouraging AI-generated proposals; its linked policy expressly describes disclosed assistance for drafting, translation and summarization. Read both together. Its application provenance log requires **model, prompt dates/times, prompts and unedited outputs**. Its development rules separately require responsible human contribution and rights/quality checks; purely generated outcomes must not be represented as payable human work. This kit does not establish such a contributor or an exception. [G1, G2]

**Actual kit provenance:** ChatGPT (GPT-6 Astra Pro) assisted this project's source review, organization and drafting on 2026-10-19. The proposed boilerplate and work-package example are AI-assisted drafts. The [recorded independent in-session engineering review](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/23#issuecomment-6275839960) is not evidence of a distinct human author, an applicant's own words, institutional review or an absent person's endorsement. No external model delegation, provider application or AI service activation was performed for this kit.

For each later adaptation, preserve the real prompts/interactions and unedited outputs as they occur, identify subsequent edits and the actual responsible reviewer, and follow the provider's current disclosure mechanism. A reconstructed summary is not a substitute for a required complete prompt log. **A complete application provenance export and responsible applicant review have not been supplied by this kit.** If the required record is unavailable, record that gap and do not claim compliance. Never conceal assistance by deleting its history.

Keep confidential applicant data, participant material, credentials and private financial documents out of public prompt logs and repositories. Prepare from public or rights-cleared material; resolve an actual provider disclosure/privacy conflict before including sensitive information in an application. This statement does not select a private custodian, storage product or retention period.

## 6. Applicant routes and agreement conditions

| Route | Kit-level finding | Evidence required for a particular representation |
| --- | --- | --- |
| Present community | Public source and project descriptions exist; the legal applicant, jurisdiction, actual representative and eligibility remain Unknown. | Program-specific admission for the actual person/entity, supported identity and a valid mandate for the particular action. GitHub organization metadata is insufficient. |
| Fiscal-sponsored project | An assessment of possible hosts is available; an actual executed relationship is not established here. | Accepted host/project agreement, permitted applicant/beneficiary roles, custody, fees, rights, exit conditions and the provider's treatment of that arrangement. Do not claim the host's status as the project's own. |
| Independently recognized 501(c)(3) | Recognition is a stated intended route, not a verified current fact. | Actual entity/recognition/current standing and every additional program condition, including the appropriate representative. Recognition alone would not establish all program eligibility. |

For the selected offer, complete the following agreement crosswalk from actual clauses. At present, all selected-offer findings are **Unknown** because no offer or applicant has been selected.

| Condition | Required application/acceptance record |
| --- | --- |
| Permitted use and benefit | Eligible work, products, costs, period, beneficiary and payment/activation conditions; distinguish grants, credits, reimbursement, loans and equity. |
| Reporting and staffing | Actual outputs, cadence, deadline/timezone, participation and accountable people; a draft title is not an appointment. |
| Branding and communications | Exact required acknowledgment and permitted marks/public statements. A donation cannot purchase a favorable result or implied project endorsement. |
| Publication and intellectual property | Rights to code/data/text/assets, actual license terms, benchmark/publication restrictions and any confidentiality; a source URL alone is not redistribution permission. |
| Privacy and custody | Minimum required data, actual recipient/controller/access/retention/deletion arrangements, consent or other applicable basis, and permitted public projection. |
| Portability and exit | Exportable artifacts, access after termination, asset title or return, restricted funds, deletion duties and supported exit costs. |
| Renewal and overage | Actual start/expiry, renewal or recurring charge, uncovered fees/taxes, stop mechanism and responsibility. An alert or planning ceiling is not proof of a hard spending cap. |
| Independence and conflicts | Actual reviewer interests and recusal where needed; retain impartial methods/results and ordinary repository decision authority. No exclusivity, veto or sponsor ranking benefit is inferred. |

Use the existing action record for the exact form, representations, attachments and commitments. Standing project engineering authorization still covers its established scope; this kit adds no permission request for that work. It supplies none of the unverified real-world identities, authority or evidence needed for an external representation.

## 7. Private attachments and reproducible versioning

The public kit contains only draft language, public sources, synthetic examples and unresolved questions. **Do not put signatures, banking/payment details, tax identifiers, identity documents, confidential applications, private donor lists, participant notes or access-bearing custody URLs in GitHub, CI logs or public artifacts.** No such attachments are needed to review this drafting method.

Use the existing action record's public projection and private-custody sections for a real packet. Actual custodian, access and retention arrangements must be established for that packet; none is invented here. Public evidence references must reveal only the permitted verification result, with sensitive originals remaining in their actual approved custody. Do not publish hashes of low-entropy private identifiers as a substitute for safe redaction.

For each concrete draft version, retain:

1. Opportunity ID, exact call/form version, source-check date, applicant route and the affected receiving issue.
2. Narrative/manifest revision, exact budget inputs/output, measurement instrument, rights findings and attachment inventory.
3. Actual independent findings, corrected draft and residual Unknowns; preserve rejected and superseded versions with their original scope.
4. Any applicable existing/exact external-action decision and its limits, followed by the actual attempt/result only if execution occurs.
5. Award, receipt, activation, use and obligations as separate later records. An application receipt is not an award and a grant is not usable until its actual conditions are satisfied.

## 8. Source observations and conflict history

| Source | Date checked and scope used |
| --- | --- |
| **G1** — [NLnet application form](https://nlnet.nl/propose/) | 2026-10-19: visible call date/time, form structure, fund selection, general rights/geographic conditions and AI-disclosure route. No field was entered; the form's existence is not eligibility. |
| **G2** — [NLnet generative-AI policy](https://nlnet.nl/foundation/policies/generativeAI/) | 2026-10-19: displayed version 1.1, valid from 2026-01-26; application disclosure/provenance and distinct development responsibility. No grandfathered arrangement or compliance is inferred. |
| **G3** — [NSF 26-506 solicitation](https://www.nsf.gov/funding/opportunities/pesose-pathways-enable-secure-open-source-ecosystems/nsf26-506/solicitation) and [program page](https://www.nsf.gov/funding/opportunities/pesose-pathways-enable-secure-open-source-ecosystems) | 2026-10-19: current solicitation/next deadline, applicant and track-specific preparation boundaries. Neither page identifies an eligible PYA lead, team or registration. |
| **G4** — [GitHub Secure Open Source Fund FAQ](https://github.com/open-source/github-secure-open-source-fund) | 2026-10-19: rolling intake, maintainer/project requirements, participation and distinct benefits. No application, interview, account or award was initiated. |

The live NLnet form and policy have different levels of detail; the policy's disclosed-assistance provision does not erase its human-responsibility conditions or the canonical fund-specific fit findings. The NSF September 2026 date is past at this review; it is not presented as an upcoming deadline. GitHub's instruction-hours description and its full participation total concern different scopes; the total is not supplemented by the same instruction hours again.

Budget PR #102's older description still says review is pending, but its actual substantive review and the two-file acceptance amendment establish the narrower accepted-findings state. This kit preserves the separate undelivered status. The measurement plan's proposed thresholds remain proposed even though its research design is accepted. These reconciliations do not rewrite the earlier source/review records.

Independent source review of the first kit at `9622c29f` found that its PB-03 sentence could use the entire declared population as the success denominator. The corrected sentence follows the accepted plan: all unique in-scope claims actually audited, including failed retrievals, with population coverage reported separately. This was a source-reading correction; no audit observations or experimental result were produced.

The [actual findings acceptance](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/23#issuecomment-6275839960), recorded at **2026-10-19 19:47:12 UTC**, covers the corrected source [`048ca3b0698d382e838d271d210c01125c46a331`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/commit/048ca3b0698d382e838d271d210c01125c46a331), tree `687b36e4add763898a0cc58b752de6d167c36e4a`, and all eleven research criteria. This later acceptance-metadata amendment changes no program interpretation, arithmetic, outcome definition or proposed work. The review is independent within the current AI engineering session; normal delivery, the undelivered budget dependency and real human/applicant evidence remain separate.

Delivery reconciliation recovered the [project controller's actual settings readback](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/10#issuecomment-6270502471): at approximately **2026-10-19 15:06 UTC**, automatic code and security reviews were saved OFF for Sustainability and Website and read back unchecked. Its [subsequent ordinary delivery record](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/10#issuecomment-6270961156) retained that state. Earlier versions of this kit cited only the prior automatic approval rejection because this newer evidence had not yet been recovered by the kit author. The controller's recorded action resolves that reported integration condition; it is not a claim that the kit author personally inspected or changed settings. Ordinary reviewed source delivery remains separate.

Direct primary pages were successfully read. One broad search also returned unrelated results; those results were excluded. This review accessed public sources only and did not inspect a private provider account, application, billing record or administrative document. Source access, local validation, independent research acceptance, project delivery and real-world eligibility are different observations.

## 9. Remaining questions, review and delivery

| Remaining item | Concrete resolution; current state |
| --- | --- |
| #20 hard dependency | Preserve actual planning acceptance and complete ordinary delivery of the canonical budget. **Undelivered** at this inspection; no total or adopted request is copied into this kit. |
| Selected program and applicant | Choose only after the canonical program-specific fit and actual route facts support it. **Unknown**; no default grant, host, person or entity is selected. |
| Finite work, resources and budget | Pin the actual receiving scope, admissible inputs, period and calculator scenario with the receiving owner. **Proposed example only**. |
| Outcomes and participant scope | Select applicable measures prospectively; establish actual baselines/protocol/custody where needed. **No measured outcome or participant operation claimed**. |
| Complete AI provenance and responsible applicant review | Preserve actual complete records and the real review required by the selected provider. **Not supplied for an application**. |
| Exact-source independent kit findings | **Accepted** at corrected `048ca3b0` by [the substantive findings review](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/23#issuecomment-6275839960), covering the entire kit, source interpretations, dependency state, usable draft/crosswalks and all eleven criteria. This acceptance-metadata amendment and ordinary delivery remain traceable separately. |
| Ordinary kit delivery | Source publication and PR/main delivery remain separate. The earlier [automatic approval rejection](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/14#issuecomment-6269247598) is reconciled with the later [actual saved-OFF controller receipt](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/10#issuecomment-6270502471). Proceed through the ordinary reviewed PR path; no alternate PR-opening route or external model task is used. |

### Literal issue acceptance map

| #23 criterion | Reviewable result |
| --- | --- |
| 1. Achievements evidenced, proposed or Unknown | Canonical index, three claim labels, bounded narrative and concrete proposed package |
| 2. Budget and outcomes consume accepted canonical artifacts | Exact #20 method/review/acceptance amendment with delivery pending; accepted #22 plan and instruments; no copied financial totals |
| 3. Provider customization, AI provenance, independent review | Three provider adaptations, actual AI-assisted draft attribution, required real provenance and reviewer instructions |
| 4. No confidential signatures or banking material | Public/private handling boundaries and existing concrete-action template |
| 5. Current primary sources, dates, failures/conflicts | G1–G4 and explicit form/policy, deadline, participation and stale-review reconciliation |
| 6. Program, intake and deadline | Kit Not applicable with reason; dated provider examples and unresolved actual applicant timezone/selection |
| 7. Benefit and three entity routes | Internal drafting benefit, separate support classes and community/host/recognized-entity table |
| 8. Restrictions and operating conditions | Agreement crosswalk covering reporting, branding, rights, privacy, portability, renewal/overage and independence |
| 9. Public benefit and defensible value/effort | Finite proposed evidence cohort, N07/N08 and PB-03/PB-04/PB-07 mapping; no invented cash, usage, hours or outcomes |
| 10. Canonical deliverable, records, questions and disposition | This index, README navigation, existing program IDs, P1 recommendation and explicit remaining questions; no duplicate opportunity |
| 11. Actual independent findings acceptance | **Accepted at `048ca3b0`** in [the exact-source review](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/23#issuecomment-6275839960) on 2026-10-19. The actual PB-03 correction and residual delivery/applicant limits are retained above; validation is not substituted for findings acceptance. |

Successful local consistency checks can verify links and data preservation. The substantive findings acceptance above is a separate actual review. Validation cannot supply #20 delivery, provider/applicant facts, an actual application, support, or outcome evidence. Keep #23 open for its actual outstanding dependency and ordinary delivery rather than closing it from the existence of a draft.
