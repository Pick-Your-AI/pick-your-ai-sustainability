# Hugging Face Community GPU Grants — qualification and Space proposal

Canonical issue: [E05-02 / #47](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/47) · Parent: [E05 / #6](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/6)

Existing opportunity: `HF-COMMUNITY-GPU` in [the register](../../data/opportunities.json)

Source inspection: **2026-10-19 UTC** · Repository baseline: **`cad980ecc8e43a472ebe63c4360f94846d175a96`**

Status: **Accepted bounded findings; research Done** · Researcher: ChatGPT research agent, session `eccc026f8bdd` · Independent findings acceptance: [in-session root review 5571037132](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/88#pullrequestreview-5571037132) at **2026-10-19 11:45:48 UTC**, reviewed source **`ccec8d108171b95e4536ec42b7fe79dbdfe77024`** (tree **`38a916c562eee24aa56b77bd9e952ba4c4caecb0`**).

The actual review includes the independent Apple-agent source assessment and accepts this deferred-application finding. Its primary-source and six-PDF inspections retain their original reviewers, dates and scopes; this acceptance-metadata follow-up performs no new provider inspection. The substantive COMMENT uses the shared CompleteDotTech GitHub account and is not a separate-account APPROVED vote. Current-main composition, metadata review, configured checks and delivery are recorded separately in [PR #88](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/88).

## Recommendation

**Defer a grant application; retain P2 research priority and an unscored opportunity.** The first useful proposed deliverable is a static public explanation of AI evidence and uncertainty. It needs no server-side inference. A later GPU request should identify a working Space, a demonstrated limitation of that version, and the smallest justified GPU workload. None of the inspected project records establishes that Space, workload, account, award or operating owner.

The Community GPU Grant is a documented selection route for a Space's hardware upgrade. It is not an entitlement to general API credits, an award to Pick Your AI, or evidence that a paid account prerequisite will be waived. The program documentation provides no project-specific allocation or award agreement. [S1, S2]

This memo records an independently accepted qualification finding with explicit Unknowns. The bounded research outcome is accepted while an application remains deferred. It does not create a Space/account, authorize expenditure, appoint an operator, submit an application or certify legal eligibility. The [entity baseline](../../docs/nonprofit/entity-baseline.md) and [authorization procedure](../../docs/workflow-and-authorization.md) retain the actual applicant and commitment boundaries.

## Duplicate and ownership check

On 2026-10-19, repository text/register searches and organization-wide GitHub issue searches for `Hugging Face`, `Community GPU` and `ZeroGPU` returned this unique program record and #47, its parent, adjacent compute work, and existing technical/source research. The three issue searches returned 9, 3 and 1 matches respectively. They are bounded search results, not an exhaustive inventory of external accounts or grants. No competing canonical deliverable or open sustainability PR was found at the preparation check.

The full #47 body and comments had no prior claim; the [root coordination claim](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/47#issuecomment-6265818809) records this four-file scope. #48 owns broader GPU route comparison and #50 consumes accepted restrictions; neither is completed here. Only `HF-COMMUNITY-GPU`, its pipeline projection and freshness membership are reconciled. No new provider record, assignee or native dependency is created.

## Current program and product boundaries

| Route | Published boundary, inspected 2026-10-19 | Consequence for this proposal |
| --- | --- | --- |
| **Community GPU Grant** | The application is documented inside an existing Space's hardware settings, below sleep settings; selection concerns an innovative Space needing upgrade support. [S1] | Actual form fields/access, selection, hardware, duration, monetary cap, geography and renewal are Unknown. No general inference subsidy is established. |
| **Static Space** | Static HTML is served without running compute and can be created without a paid plan. [S3] | Appropriate first proposed delivery; publishing would still require an actual account and a separate deployment action. |
| **Ordinary CPU/GPU compute Space** | Current Overview requires PRO for new personal Gradio/Docker compute Spaces, or Team/Enterprise for organizations. CPU Basic's lack of hourly charge does not remove that creation condition. [S2] | Do not label a new ordinary CPU Space a universally free fallback or purchase a plan to qualify a speculative grant. |
| **ZeroGPU** | A separate shared, dynamically allocated service. Eligible free personal accounts with verified email and age over 30 days may host two Gradio ZeroGPU Spaces; organizational hosting requires Team/Enterprise. Its documented free-account daily allowance is five GPU minutes, with quota resetting 24 hours after first use. Default task duration is 60 seconds. [S4] | Account eligibility, actual queue availability and workload compatibility remain untested. These limits do not describe a Community GPU Grant. Do not multiply allowances through extra identities. |
| **Inference Endpoints** | Pricing describes the ordinary active-subscription/card route and minute-based compute metering. Hub billing also permits approved organizational AWS/Google Cloud marketplace subscriptions to replace card billing. [S5, S6] | Actual project subscription/payment route is **Unknown**. This separate paid product receives no Endpoint or general API credit award from the grant documentation. |

Current ZeroGPU documentation lists Gradio-only compatibility and a default half RTX Pro 6000 Blackwell allocation with 48 GB VRAM; the full 96 GB option consumes twice the quota. These are published product specifications, not measured available memory, grant hardware or a guarantee that a selected runtime works. No inference, queue, timing or memory experiment was performed. [S4]

The new-compute creation requirement and ZeroGPU exception are both explicit in current Overview; they are not conflicting universal promises of free compute. This memo uses no historical announcement as current eligibility evidence. The live Terms, Privacy Policy and Content Policy display older effective dates, recorded below; their retrieval date is not a new effective date. [S2, S7–S9]

## Concrete public-benefit proposal

**Proposed artifact: a static AI evidence walkthrough.** A visitor compares three clearly synthetic cards showing a documented capability, an estimate, and an unresolved claim. Each card explains provenance, version/scope, access date, uncertainty and permitted reuse; a local download retains those labels and links. No real provider result, price, benchmark score or participant observation is fabricated. There is no visitor text submission, model invocation, account login, analytics integration or secret-bearing configuration in the proposed first version.

This addresses [Research #41](https://github.com/Pick-Your-AI/pick-your-ai-research/issues/41)'s actual user decision: where component facts come from, whether they may be reused, and how uncertainty/freshness is communicated. Its [canonical source policy at `daac1dae`](https://github.com/Pick-Your-AI/pick-your-ai-research/blob/daac1dae7348c8f4f1011c85979068c8ba6c1489/research/T0-configuration/catalog-data-sources.md) distinguishes source checking, independent reproduction and per-source rights. The proposal illustrates those distinctions without promoting pending policy supplements, changing frozen v1 or copying third-party catalogs. Any later implementation and receiving acceptance remain with the affected repository owners.

Static Spaces support ordinary HTML and optional frontend build steps, so the proposed output can remain a versioned static bundle with a local/offline copy. [S3] Suggested acceptance for that future implementation is a keyboard-operable walkthrough, persistent evidence labels in the download, correct synthetic notices, and a reproducible build from its pinned source. These are proposed engineering checks, not completed tests, measured accessibility or a participant study.

**GPU extension remains conditional.** A later proposal could demonstrate one explicitly selected, rights-cleared model/configuration using a finite synthetic input set, bounded concurrency/output and a visible stop path. Before asking for hardware, retain its pinned model/runtime, baseline result, peak-memory measurement method, requested accelerator, measured per-run duration, expected visits and finite demonstration window. Those values are presently Unknown; assigning a GPU from a catalog alone would not establish need. If the static walkthrough already serves the educational goal, pursue no GPU upgrade for it.

[Leaderboard #25](https://github.com/Pick-Your-AI/pick-your-ai-leaderboard/issues/25) is a separate production hosting decision. Its inspected issue retains the accepted static/service topology and unresolved actual operator/account evidence. A public demo Space neither replaces that topology nor establishes its service owner, database, budget, deployed source installation or operating acceptance. The [needs assessment](../../docs/needs-assessment.md) remains the canonical cross-repository map. Proposed public usefulness is not evidence of achieved charitable impact or actual demand.

## Eligibility: three separate routes

The grant paragraphs do not state a 501(c)(3) prerequisite or a fiscal-sponsor exception. Absence of such wording is not affirmative admission. General account Terms require an eligible natural person or registered legal entity and authority when acting for an organization; the actual applicant and account route must be matched before use. [S1, S7]

| Applicant route | Present assessment | Exact unresolved evidence |
| --- | --- | --- |
| Current community | **Unknown for the actual project.** A public community description is insufficient. | Actual account holder and authority, existing Space, supported location, incremental hardware need, current form and provider selection; any required plan or grant waiver. |
| Fiscal-sponsored project | **Unknown.** A sponsor's status or account is not automatically the project's. | Actual sponsor agreement and applicant/beneficiary identity, permitted account/control arrangement, payment responsibility, and provider acceptance of that specific route. |
| Independently recognized 501(c)(3) | **Unknown.** Intended recognition is not actual recognition or grant entitlement. | Real entity/status and representative, account/plan eligibility, suitable Space, supported jurisdiction, workload and program decision. |

These are qualification questions, not new prerequisites to complete public desk research. The entity baseline retains the administrative Unknowns; this memo does not assign people or request their private records. Do not infer eligibility from repository publicity, contribution volume, nonprofit intent, a fiscal-host comparison or a free product tier.

## Restrictions, obligations and exit

| Topic | Current finding and proposed treatment |
| --- | --- |
| Grant scope, expiry and renewal | Selected hardware/capacity, award length, expiry behavior, renewal method, reporting cadence and grant-specific deadline are **Unknown** in the reviewed public grant description. No recurring or open-ended award is inferred. Obtain the actual conditions only if a later application is warranted. [S1] |
| Billing and overage | Upgraded Spaces bill while starting/running even without visitors; pause or CPU Basic stops upgrade billing. Paid subscriptions renew and compute is billed separately. A grant's coverage of plan fees, storage, replicas or post-award usage is Unknown. A future receiving plan must verify covered meters and prevent unintended paid continuation; an alert alone is not a hard spending cap. [S1, S6] |
| Public content and publication rights | The Terms give Hugging Face a service-related content license and users a perpetual public-repository license through its services; existing open-source notices still govern. Grant-specific publication/benchmark permission and any applicant-specific agreement remain unverified. Use only material whose actual rights permit the intended publication. [S7] |
| Privacy and data use | The Privacy Policy covers account, communication, device and usage data, service improvement/research uses, stated sharing grounds and international processing; retention is purpose-dependent. A static app with no input collection does not make hosting anonymous or establish zero retention. The proposal excludes private prompts, identities, credentials and source data requiring restricted access. [S8] |
| Branding, reporting and independence | Hugging Face reserves its marks; a grant-specific acknowledgement, publicity obligation, exclusivity or editorial veto was not established. Treat each as Unknown pending actual terms. Proposed project conditions are accurate support disclosure, preserved negative results and no sponsor control of findings; these are our recommendations, not published provider promises. [S7] |
| Content and resource conduct | Platform policy restricts privacy/IP violations, abuse, metric manipulation and bypassing resource restrictions. Keep the demonstration rights-cleared and finite; no grant application should rely on proxying, duplicate identities or unrelated workloads. [S9] |
| Persistence and portability | Runtime disk is ephemeral; attached storage is a separate capability. Keep the static source and permitted output in the owning repository rather than using runtime disk as the only evidence copy. Any paid storage, model files and later runtime dependencies need their own export/rights/cost check. Public copies may survive account deletion. [S10, S7] |
| Geography and account transfer | General Terms require prior written consent to assign agreement rights/obligations and compliance with applicable export/sanctions rules. Code portability does not establish account or award transfer. Signed documents and Supplemental Terms can take precedence; actual applicant geography and grant conditions remain Unknown. [S7] |
| Supplemental product scope | The April 28, 2025 Supplemental Terms preamble incorporates the general Terms and other binding documents and takes precedence over conflicting general Terms. Hub Premium Features includes Spaces hardware upgrades, storage fees and PRO, describes monthly pay-as-you-go billing, and incorporates the DPA specifically for Spaces hardware upgrades. These published product conditions do not establish a Community GPU award or a waiver of charges. Actual award/form/private agreements remain Unknown. [S11, S12] |
| Conditional data-processing agreement | The DPA applies to personal data processed for a customer under the applicable service agreement. Customer lawful-basis and security duties remain; specified sensitive data requires prior written consent. It authorizes listed subprocessors with a 30-day objection route for additions and describes international transfer mechanisms. Section 10 governs request/end-of-service deletion, with a latest 180-day deadline after expiry/termination unless law requires storage; a charged copy request must be made at least 30 days beforehand. These are conditional published terms, not zero retention, observed compliance or an actual project data configuration. [S16, pp. 1, 4–10] |

The other linked PDFs cover **separate products**. Enterprise Hub and Enterprise Plus describe order-form terms, annual renewal and 60-day non-renewal notice; their Section 5 overrides expressly exclude self-serve purchases. Inference Services covers Serverless Providers and Dedicated Endpoints: its Endpoint-specific personal-data restriction requires express written agreement for an exception, and its PostHog/EU analytics clause is also Endpoint-specific. Neither the enterprise purchase terms nor those Endpoint clauses define a Spaces grant or the proposed static demo. [S13–S15] The synthetic no-input proposal remains appropriate without claiming that all hosting data falls outside the provider's policies.

## Intake, value and next action

The public application route is documented, but this research did not identify or access a Pick Your AI Space's settings or an applicant-specific form. Therefore the exact application URL remains `null`; required fields, attachments, review timing, geographic limits and the actual decision remain Unknown. No deadline is published in the inspected grant paragraphs. This is **Unknown**, not a fabricated rolling deadline or an assigned internal due date. [S1]

Record **Verified for program research** and **Done research**, retaining **Unknown applicant eligibility**, **P2**, and `null` for all eight weighted factors, total score, currency, usable value and numerical effort. The actual findings acceptance meets the [Verified transition](../../docs/operations-and-reporting.md#evidence-for-transitions); it does not establish a Qualified applicant or an authorized application. The supplied weights remain 20/20/15/10/10/10/10/5; the eligibility and evidence gates precede scoring. P2 reflects a relevant documented educational-demo route with unresolved need, terms and eligibility, not an estimated success probability.

A defensible later valuation would use covered eligible runtime by hardware/meter, the contemporaneous applicable rate and currency, award window, existing free access, uncovered account/storage/overage costs and evidence of what the project would otherwise buy. Hardware support is not cash. With neither a covered workload nor a purchase counterfactual, avoided cost cannot be computed. Effort needs actual estimates for a static implementation, any GPU adaptation/measurement, account/terms review, maintenance, reporting and exit. This memo supplies the task categories without inventing staff commitments or hours. Follow the [budget method](../../docs/budget-assumptions.md).

**Next authorized action:** supply this accepted bounded finding to existing #50 and retain the deferred opportunity. Link the separately reviewed current-main delivery and actual checks in #47; no repeated provider inspection or new application action is required merely to record the existing acceptance. Any later implementation can use the static proposal as a candidate, while a GPU application first needs the missing Space/need/terms evidence. There is no reason to send speculative outreach, create an account or buy hardware merely to complete this research.

## Dated source register

All public pages and PDFs below were inspected **2026-10-19 UTC**. They are provider documentation, not independent operational observations. S11 retains an earlier web-content HTTP 403 observation and a later successful exact-URL retrieval; it is now a checked source. The exact linked source, rather than a search snippet or old announcement, supports each finding.

| ID | Primary official source | Scope and access result |
| --- | --- | --- |
| S1 | [GPU Spaces](https://huggingface.co/docs/hub/en/spaces-gpus) | Read: Community GPU Grant location/selection description and upgrade billing. No award-specific terms or deadline found in those sections. |
| S2 | [Spaces Overview](https://huggingface.co/docs/hub/en/spaces-overview) | Read: current paid-plan creation requirement, explicit ZeroGPU exception and public source visibility. |
| S3 | [Static HTML Spaces](https://huggingface.co/docs/hub/en/spaces-sdks-static) | Read: no-compute hosting and static/build configuration. |
| S4 | [ZeroGPU](https://huggingface.co/docs/hub/en/spaces-zerogpu) | Read: distinct hosting eligibility, quota/account/SDK, hardware and duration limits. Not grant limits. |
| S5 | [Inference Endpoints pricing](https://huggingface.co/docs/inference-endpoints/en/pricing) | Read: dedicated product, standard subscription/card route and metering; qualified by S6's approved organization marketplace alternative. No award valuation. |
| S6 | [Hub billing](https://huggingface.co/docs/hub/en/billing) | Read: separate charges, renewal/storage exposure and approved organizational AWS/Google Cloud marketplace billing instead of a card. Actual settings Unknown. |
| S7 | [Terms of Service](https://huggingface.co/terms-of-service) | Read: displayed effective date 2022-09-15; account, content/license, marks, termination, assignment/export and agreement precedence. No actual applicant agreement assumed. |
| S8 | [Privacy Policy](https://huggingface.co/privacy) | Read: displayed effective date 2023-03-28; collection/use/sharing, retention and processing scope. |
| S9 | [Content Policy](https://huggingface.co/content-policy) | Read: displayed effective date 2025-04-10; resource conduct and privacy/IP restrictions. |
| S10 | [Spaces disk/storage](https://huggingface.co/docs/hub/en/spaces-storage) | Read: ephemeral disk and attached-volume distinction. No persistent-storage entitlement assumed. |
| S11 | [Supplemental Terms preamble](https://cdn-media.huggingface.co/landing/assets/Supplemental+Terms.pdf) | Read and visually checked: one page, displayed effective date 2025-04-28; precedence and four product links. After the earlier web-content HTTP 403, exact-URL GET returned HTTP 200 application/pdf at 11:24:38 UTC, 123,984 bytes; no grant award clause on this preamble. |
| S12 | [Hub Premium Features](https://cdn-media.huggingface.co/landing/assets/Supplemental+Terms+-+Hub+Premium+Features.pdf) | Read: displayed effective date 2025-04-28; p. 1 Sections 1–3 cover Spaces hardware/storage/PRO, fees and the Spaces hardware-upgrade DPA reference. HTTP 200; no Community GPU award terms established. |
| S13 | [Enterprise Hub](https://cdn-media.huggingface.co/landing/assets/Supplemental+Terms+-+Enterprise+Hub.pdf) | Read for scope: displayed effective date 2025-04-28; Sections 2–3 order-form term/renewal/fees and p. 3 Section 5's explicit exclusion of self-serve purchases from its overrides. HTTP 200; actual enterprise agreement Unknown. |
| S14 | [Enterprise Plus](https://cdn-media.huggingface.co/landing/assets/Supplemental+Terms+-+Enterprise+Plus.pdf) | Read for scope: displayed effective date 2025-04-28; Sections 2–3 order-form term/renewal/fees and p. 3 Section 5's same conditional override boundary. HTTP 200; no enterprise purchase assumed. |
| S15 | [Inference Services](https://cdn-media.huggingface.co/landing/assets/Supplemental+Terms+-+Inference+Services.pdf) | Read: displayed effective date 2025-04-28; Serverless/Dedicated product scope and p. 2's Endpoint-specific personal-data/analytics clauses, fees and DPA reference. HTTP 200; these clauses are not transferred to Spaces. |
| S16 | [Data Processing Agreement](https://cdn-media.huggingface.co/landing/assets/Data+Processing+Agreement.pdf) | Read: 15 pages; no standalone calendar effective date displayed—p. 1 ties effectiveness to the underlying agreement. Customer duties, sensitive-data limits, subprocessors, deletion and transfers are scoped above. HTTP 200 at 11:30:54 UTC; no actual project agreement/configuration established. |

S12–S15 were retrieved successfully at 11:26:28 UTC. The existing opportunity's source objects retain each PDF's exact URL, successful retrieval timestamp and SHA-256 digest. S11's earlier failure is retained as resolved access history, not evidence of missing current terms. The originating grant lead's earlier date is retained; this continuation adds a current scoped review, not an award or form readback. A changed program, terms, plan requirement, quota or source-access result triggers requalification before a current recommendation or external action. The repository's monthly review convention does not assert that a scheduled automation was installed.

## Acceptance map

The numbering below follows all 13 literal #47 criteria in their current order. Repeated criteria receive the same actual evidence, not invented additional deliverables.

| Criterion | Accepted research evidence and separate delivery boundary |
| --- | --- |
| 1. Primary sources/date; historical versus current | Dated S1–S16 register, displayed effective dates and historical failed versus later successful retrieval receipts. |
| 2. Application/benefit/restrictions/deadline | Product table, obligations and intake sections; award/form/deadline Unknowns. |
| 3. Three eligibility routes | Separate community, fiscal-sponsored and recognized-entity table. |
| 4. Canonical findings/disposition/scoring/questions | This memo, the unique opportunity record, P2/null rationale and next action. |
| 5. Independent review; no implied activation | [Actual findings acceptance 5571037132](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/88#pullrequestreview-5571037132) at `ccec8d108171b95e4536ec42b7fe79dbdfe77024`, submitted 2026-10-19 11:45:48 UTC. No external activity is claimed. |
| 6. Named deliverable and Space proposal | This canonical path, static proposal, conditional GPU need and grant/product distinction. |
| 7. Current sources, access failures/conflicts | Source register, reconciled compute/ZeroGPU/payment boundaries and scoped supplemental/DPA review; S11's earlier HTTP 403 is resolved by the later verified HTTP 200. |
| 8. Current program/intake/deadline or Unknown | Public settings route; unaccessed actual form and unsupported deadline kept separate. |
| 9. Benefit and three applicant routes | Hardware support distinct from cash; each route assessed without entitlement. |
| 10. Full obligation categories | Restrictions, reporting, branding, publication, privacy, portability, renewal, overage and independence table. |
| 11. Concrete use and defensible value/effort | Source-policy walkthrough, actual cross-repository boundaries and explicit unvalued methodology. |
| 12. Publish canonical record, sources and disposition | Memo and canonical register package published at `ccec8d108171b95e4536ec42b7fe79dbdfe77024` and accepted in the linked review. This metadata/current-main follow-up retains separate checks, delivery and issue readback. |
| 13. Link independent acceptance | [The actual independent COMMENT](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/88#pullrequestreview-5571037132) identifies the exact revision, primary-source/PDF review, findings and limits. Passing local checks are separate consistency evidence. |

The recorded independent source/engineering acceptance establishes this deferred research finding without asserting a legal opinion, actual account eligibility, a deployment, provider selection, grant receipt, achieved public benefit or a binding organizational decision. Final issue reconciliation must link the current receiving revision, required original checks, ordinary merge and actual-main/Project readback; this source map does not invent those later receipts.

Local checks on **2026-10-19**, using Python **3.12.14** and the repository's pinned validator dependencies: **61 unit tests passed** in **3.635 seconds**; `scripts/validate_repository.py` passed **21 JSON and 34 Markdown files with zero errors**; the diff whitespace check passed. These checks establish repository consistency, not source freshness, application qualification or independent acceptance.
