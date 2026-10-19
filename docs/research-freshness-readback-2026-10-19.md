# First freshness register readback — 2026-10-19

Owner: [E09-04 #70](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/70). Status: prepared for independent review.

This is an **offline audit of recorded evidence**, with analysis cutoff **2026-10-19T11:17:34Z**. The input is accepted commit [cad980e](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/commit/cad980ecc8e43a472ebe63c4360f94846d175a96), tree `2dfdb6a554381d767f869ed3f33a2429d531abe1`. The [complete JSON readback](../data/audits/freshness-readback-2026-10-19.json) retains all existing claim summaries, route assessments, source observations, unresolved fields and original review identities.

The audit does not refresh the external sources, alter any program record or certify applicant eligibility. All provider states and dates below are observations **recorded in that immutable input**, not new provider findings. The separate Apple change-event handoff is identified below.

## Method and source identity

Read both exact Git objects, compare their bytes with the checkout, join all opportunity IDs to the URL index, check required program/application/source membership, and derive counts from the actual rows and source roles. An independent reader can repeat these operations using the pinned objects and compare every copied field in the JSON. The `null_fields_at_cutoff` lists enumerate top-level null opportunity fields; they do not recursively enumerate nested scoring or review fields. The existing offline repository validator checks required URL membership; it does not establish live freshness.

| Input | Git blob | SHA-256 |
| --- | --- | --- |
| [data/opportunities.json](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/cad980ecc8e43a472ebe63c4360f94846d175a96/data/opportunities.json) | `85efabeada5387e04f2ed6f7e3e9ead1d528b2da` | `50e727f3c561d6be2897c215c4322e4340aeca54ca80fa242d7127cc680d530f` |
| [data/research-freshness.json](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/blob/cad980ecc8e43a472ebe63c4360f94846d175a96/data/research-freshness.json) | `4c9067cadfd643374fd0da914a2d82ca22edb5e2` | `269aaa188f493daad76d0b197673ff348ac993bc1f21d67e1ca25999e2df9610` |

## Findings

| Recorded inventory | Count / consequence |
| --- | --- |
| Unique programs | 39 |
| Unique source/program/application URLs | 72 |
| Governing-evidence URLs, derived from source roles | 55 |
| Additional endpoints, derived from source roles | 17 |
| URLs with a recorded successful source check | 55 |
| URLs without a recorded successful source check | 17 |
| Of those, source-index entries without a structured attempt date | 16 |
| Of those, a recorded unsuccessful attempt | 1 |
| Programs affected by unverified endpoints | 18 |
| Required URL/membership gaps | 0 |
| Recorded closed-intake programs | 4 |
| Programs with a recorded external deadline | 3 |

The 55 recorded successful checks all retain 2026-10-19 dates from the input. They are not renewed by this audit. Their general source scope/state is not a complete per-claim access history; use the [review template](../templates/freshness-review.md) to capture exact applicable content and attempt outcomes when performing the next real check.

The one dated failed attempt in the source index is the AWS application workbook's HTTP 403. Its successful-verification date remains null. The other 16 unverified source-index entries have no structured attempt date/result. That absence does not establish that no attempt was recorded elsewhere, and no new access outcome is inferred.

The preserved `JETBRAINS-OSS` claim summary records that the main program landing page did not expose readable eligibility details, while the source-index row for `https://www.jetbrains.com/community/opensource/` has no structured attempt date/result. Both observations are retained. Reconcile that discrepancy in the [existing #58 investigation](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/58) without inventing an attempt timestamp, HTTP result, successful check or new provider observation.

## Endpoints requiring successful content review

| URL | Existing program IDs | Structured source-index attempt / result |
| --- | --- | --- |
| https://academicgrants.nvidia.com | NVIDIA-ACADEMIC | Unknown / No structured attempt recorded in the source index |
| https://app.coderabbit.ai | CODERABBIT-OSS-PRODUCT | Unknown / No structured attempt recorded in the source index |
| https://apply.sovereign.tech | SOVEREIGN-TECH-FUND | Unknown / No structured attempt recorded in the source index |
| https://causes.benevity.org | BENEVITY-CAUSES | Unknown / No structured attempt recorded in the source index |
| https://cloud.cerebras.ai | CEREBRAS-TRIAL | Unknown / No structured attempt recorded in the source index |
| https://console.firebase.google.com | FIREBASE-TEST-LAB | Unknown / No structured attempt recorded in the source index |
| https://console.groq.com | GROQ-FREE-PLAN | Unknown / No structured attempt recorded in the source index |
| https://developer.amd.com | AMD-DEVCLOUD | Unknown / No structured attempt recorded in the source index |
| https://github.com/sponsors | GITHUB-SPONSORS-ORG | Unknown / No structured attempt recorded in the source index |
| https://nlnet.nl/propose/ | NLNET-CODESUPPLY, NLNET-RESTACK | Unknown / No structured attempt recorded in the source index |
| https://openai.com/form/codex-for-oss/ | OPENAI-CODEX-OSS | Unknown / No structured attempt recorded in the source index |
| https://openai.smapply.org | OPENAI-RESEARCHER | Unknown / No structured attempt recorded in the source index |
| https://opensourcecreditsapplicationform.s3.us-east-2.amazonaws.com/AWS%2BOpen%2BSource%2BCredits%2BApplication%2BForm.xlsx | AWS-OSS-CREDITS | 2026-10-19 / HTTP 403 recorded during initial source research; workbook contents remain unverified |
| https://softwarefreedom.org/about/contact/ | SFLC-LEGAL | Unknown / No structured attempt recorded in the source index |
| https://spencer.smartsimple.us/ | SPENCER-SMALL-EDUCATION | Unknown / No structured attempt recorded in the source index |
| https://www.jetbrains.com/community/opensource/ | JETBRAINS-OSS | Unknown / No structured attempt recorded in the source index |
| https://www.research.gov | NSF-PESOSE-26-506 | Unknown / No structured attempt recorded in the source index |

A sign-in wall, later access error or irrelevant page must retain its own actual outcome. A readable program overview or discovered link cannot establish the unseen application fields. These are research follow-ups for existing owners, not authorized account actions.

## Every program and its unresolved intake

The JSON gives each program's exact linked source observations, claim summaries, three route assessments, action gate, named missing evidence/decisions and top-level null fields. This table is its compact index. Zero unverified endpoints means every indexed URL has a recorded check; it does not mean every current claim or applicant is qualified.

| Existing program / issue | Indexed URLs / no recorded success | Recorded application status |
| --- | --- | --- |
| [NLNET-RESTACK](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/25) | 2 / 1 | Call open; Pick Your AI scope excluded absent exception evidence |
| [NLNET-CODESUPPLY](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/25) | 4 / 1 | Call open; applicant and proposed work not qualified |
| [NLNET-NGI0-COMMONS](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/25) | 1 / 0 | Closed historical program; no new applications |
| [GITHUB-SECURE-OSS-FUND](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/26) | 1 / 0 | Rolling applications documented; no application submitted in this execution |
| [GITHUB-SPONSORS-ORG](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/33) | 4 / 1 | Organization onboarding route documented; existing account state Unknown |
| [SFC-MEMBERSHIP](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/14) | 2 / 0 | Rolling inquiry/application process; acceptance may take months |
| [SPI-ASSOCIATED-PROJECT](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/14) | 3 / 0 | Application process documented; PYA acceptance/relationship Unknown |
| [OSC-FISCAL-HOST](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/14) | 4 / 0 | Application/validation route documented; no acceptance claimed |
| [GOOGLE-NONPROFITS-US](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/31) | 1 / 0 | Eligibility route documented; no qualified applicant established |
| [SOVEREIGN-TECH-FUND](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/27) | 2 / 1 | Application portal documented; scope unsuitable absent distinct component evidence |
| [SLOAN-OSS-IN-SCIENCE](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/27) | 2 / 0 | Program LOI route documented; no current special open call |
| [NSF-PESOSE-26-506](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/30) | 3 / 1 | Active solicitation; PYA applicant route not qualified |
| [SPENCER-SMALL-EDUCATION](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/29) | 2 / 1 | Closed; no next deadline verified |
| [BENEVITY-CAUSES](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/36) | 2 / 1 | Nonprofit registration route documented; applicant validation Unknown |
| [AWS-OSS-CREDITS](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/51) | 2 / 1 | Requests invited per official page; current workbook access unverified |
| [CLOUDFLARE-ALEXANDRIA](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/52) | 2 / 0 | Current page invites sponsorship requests; no deadline published |
| [HF-COMMUNITY-GPU](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/47) | 1 / 0 | Application documented in Space hardware settings; actual applicant form not accessed |
| [CODERABBIT-OSS-PRODUCT](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/56) | 2 / 1 | No funding application; repository-app installation is the activation route |
| [JETBRAINS-OSS](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/58) | 4 / 1 | Program documented; current application requirements and form not fully verified |
| [APPLE-FEE-WAIVER](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/60) | 1 / 0 | Requests available during enrollment or before membership expiry for eligible account holder; no project deadline confirmed |
| [FASTLY-FAST-FORWARD](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/53) | 1 / 0 | Application link is present; no deadline published |
| [OPENAI-RESEARCHER](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/39) | 2 / 1 | Official page invites applications via SurveyMonkey Apply; exact cutoff Unknown |
| [OPENAI-CODEX-OSS](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/61) | 2 / 1 | Application offered on current program page |
| [ANTHROPIC-RESEARCHER](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/40) | 1 / 0 | Official application linked; monthly evaluation documented |
| [ANTHROPIC-CLAUDE-OSS](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/61) | 1 / 0 | Apply-now page exists; no deadline published |
| [GOOGLE-GEMINI-ACADEMIC](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/41) | 1 / 0 | Program named; actual intake and route not verified |
| [AZURE-NONPROFIT](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/42) | 2 / 0 | Offer documented; registration and validation required |
| [AMD-DEVCLOUD](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/48) | 2 / 1 | Current page describes registration/application for complimentary credits |
| [NVIDIA-ACADEMIC](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/48) | 2 / 1 | Closed per explicit current notice; no verified reopening date |
| [GROQ-FREE-PLAN](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/43) | 2 / 1 | Public service allowance; no research grant application verified |
| [CEREBRAS-TRIAL](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/44) | 2 / 1 | Public trial; no independent OSS/research grant verified |
| [TOGETHER-RESEARCH](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/45) | 1 / 0 | Invitation-only; route/access not confirmed |
| [FIREWORKS-STARTUP](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/46) | 1 / 0 | Applications documented for qualifying startups |
| [SAMSUNG-REMOTE-LAB](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/55) | 1 / 0 | Public developer service; not a donation program |
| [FIREBASE-TEST-LAB](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/55) | 2 / 1 | Public product allowance; no nonprofit grant required |
| [OSTIF-SECURITY](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/59) | 1 / 0 | Inquiry/scoping route documented; no automatic grant intake or deadline |
| [TAPROOT-PROBONO](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/65) | 1 / 0 | Platform signup documented; volunteer match not guaranteed |
| [SFLC-LEGAL](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/65) | 2 / 1 | Public contact route exists; capacity/intake availability not confirmed |
| [GSOC-MENTOR-ORG](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/66) | 1 / 0 | Organization registration closed; next-cycle dates not verified |

The four recorded closed intakes are `NLNET-NGI0-COMMONS`, `SPENCER-SMALL-EDUCATION`, `NVIDIA-ACADEMIC`, `GSOC-MENTOR-ORG`. None is reopened by this readback or by the monthly cadence.

Only Fireworks has a populated independent reviewer in this input. Its existing reviewed exclusion and historical Discovered stage remain attributed to the original record; this audit neither reopens that outcome nor accepts the other investigations. All recurring coordinator and reviewer assignments for this process remain Unassigned.

## Recorded deadline precision

These are retained deadline records, not newly reverified calls or a recommendation to apply. The exact round field is copied in the JSON; a null round remains unresolved even where the stable program identity includes a solicitation number.

| Existing program | Recorded local date/time | Recorded timezone | Recorded UTC | Source |
| --- | --- | --- | --- | --- |
| NLNET-RESTACK | 2026-11-03 12:00 | CET (UTC+01:00) | 2026-11-03T11:00:00Z | [recorded source](https://nlnet.nl/restack/) |
| NLNET-CODESUPPLY | 2026-11-03 12:00 | CET (UTC+01:00) | 2026-11-03T11:00:00Z | [recorded source](https://nlnet.nl/codesupply/) |
| NSF-PESOSE-26-506 | 2027-03-02 17:00 | Submitting organization local time; exact zone Unknown | Unknown | [recorded source](https://www.nsf.gov/funding/opportunities/pesose-pathways-enable-secure-open-source-ecosystems/nsf26-506/solicitation) |

The two NLnet records retain explicit CET cutoffs and UTC conversions. NSF retains a submitting-organization-local cutoff with exact timezone and UTC unresolved. The remaining 36 records retain null verified deadlines. No internal action date or next monthly meeting is substituted for a provider cutoff.

## Separate current change event

The [independent Apple source handoff](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/60#issuecomment-6265778887), read and posted on 2026-10-19, identifies a current-source boundary between legacy CTF wording and later agreement-dependent EU guidance. Its three inspected primary URLs are recorded separately in the JSON. The existing #60 author is preparing the canonical disposition. This event is outside the pinned input's 72 URLs; it does not silently refresh that snapshot, infer an applicable account agreement or establish transaction-fee savings.

## Review and next actions

Review the [procedure](research-freshness.md) and manually exercise its reopened-round, conflicting-source and unavailable-page cases. Those cases are synthetic; this audit records no actual reopened provider round. Final E09-04 acceptance needs the exact reviewed/delivered revision and #67's accepted intake input.

The immediate desk-research output is a concrete queue: 17 endpoints without a successful recorded check; four retained closed rounds; the unresolved NSF deadline timezone; the Apple term-change review; and per-claim access detail to capture when sources are actually rechecked. Prioritize checks against an actual proposed decision or validity event. Owners and action dates are assigned only when accepted/selected, and all findings remain in the existing program identities.

No application, outreach, award, receipt, activation, financial value, organization-wide authority or new automation is created by this readback.
