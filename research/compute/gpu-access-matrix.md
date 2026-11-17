# GPU evaluation access: public-source route screen

**Owning issue:** [#48 / E05-03](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/48) · **Source review:** 2026-11-17 (public official pages, unauthenticated) · **Research status:** conditional source screen pending independent acceptance, canonical register reconciliation and actual-workload qualification. **No applications or credentialed API calls were made.**

## Decision

For short, separately approved GPU evaluation workloads, **AMD Developer Cloud** is the most direct conditional *individual-developer* lead, subject to the applicant, credit terms, third-party billing and rights review. **Hugging Face Spaces community GPU grants** are only a conditional fit for a public Space demonstration, not a replacement for an arbitrary benchmark VM. **NVIDIA Academic Grant** explicitly says it is not accepting new applications; preserve its historical route without treating the visible proposal controls as an open intake. **Google Cloud Research Credits** and **AWS Cloud Credit for Research** are two additional documented programs, but neither establishes a route for an unaffiliated applicant; both involve institutional researcher eligibility. These are research dispositions, **not qualified applicant statuses or actual resource allocations**.

No specific provider has approved Pick Your AI, any project representative, any fiscal sponsor, or any academic collaboration. Numeric scores and net usable value remain **Unknown** until eligibility and verifiable cost/workload/usage evidence exist. P2 reflects comparison priority, not a positive eligibility result.

## Provider and hardware route matrix

| Route | Official offer / intended use | Status observed 2026-11-17 | Conditional fit / principal disqualifier | Current disposition |
| --- | --- | --- | --- | --- |
| AMD Developer Cloud / AMD AI Developer Program | AMD Instinct MI300X hosted cloud; enrolled eligible developers may receive **$100 credit with a generally 30-day expiry**, subject to confirmation and discretion. Requires a third-party account; a valid payment method can create overage exposure. | Official product and member terms published; application/award not tested. Another AMD general cloud-access page still describes **25 hours / approximately $50 and 10 days**. Treat this as conflicting first-party product-path terms and require an actual current offer notice before using any amount. | Relevant for ROCm / MI300X-compatible, bounded inference or reproducibility tests; requires developer qualification, acceptable storage/transfer terms and an approved zero-overage plan. | **Conditional research lead**; no eligible applicant or credit known. |
| NVIDIA Academic Grant Program | Competitive research support including GPU cloud/hardware/software, on topics and platform requirements stated by NVIDIA. | Official program page says **not accepting new applications**, despite containing historical calls and submit links. | Applicant must be full-time faculty at an accredited institution awarding PhD research degrees. A partner mentioned in a proposal is not an actual qualified PI. | **Defer / intake closed**. No current award route evidenced. |
| Hugging Face Spaces community GPU | Community grants may help qualifying public Spaces with upgraded GPU hardware. Ordinary GPU Space hardware has published hourly pricing; a grant is discretionary. | Official Spaces documentation provides a grant request within Space settings, not an unconditional entitlement. | Valid for a public Space demonstrator with compatible runtime, quotas and data rights. It is **not** unrestricted, researcher-controlled GPU VM time, and paid replicas/upgrades can incur charges. | **Conditional public-demo route**; not counted as free benchmark cluster capacity. |
| Google Cloud academic research credits | Official application describes research credits, a proposal and estimated cost/calculator; Google advertises a research-credit program for eligible researchers. | Public application page shows an intake form; submission not attempted. The offer states activation/expiry and noncommercial academic-use conditions. | Restricted to faculty, PhD students and postdoctoral researchers at accredited higher-education institutions or eligible nonprofit research institutions in approved countries. A general nonprofit or fiscal sponsor is not presumed to qualify. The official application asks for an actual **billing-account ID**; credits must be activated **within 60 days of the start date** and do not retroactively cover work already run or charged to a different account. Starting a pilot before activation can create payable cash. The application and program FAQ differ as to whether the 365-day expiry runs from redemption or issuance; use the actual award notice. Credit eligibility does not guarantee a specific GPU SKU or quota. | **Institutional-partner-dependent lead**; no applicant, quota or credits verified. |
| AWS Cloud Credit for Research | AWS promotional research credits for bounded proofs of concept, benchmark comparisons, reproducible tools and tutorials; EC2 use under the program is limited to on-demand and Spot. | Official program describes **rolling review**, typical **90–120-day cycles** and research-institution eligibility. | Full-time faculty/staff or graduate researchers at accredited research institutions; requires institutional email and AWS account. The [AWS Promotional Credit Terms](https://aws.amazon.com/awscredits/) require prior written consent to disclose the credit (§8) and restrict disclosure of information learned through the service (§11). Do not publish named award details or measured AWS benchmark results without reviewing both provisions and obtaining any required written consent. No unsponsored community entitlement is established; actual GPU instance/quota and award remain unknown. | **Institutional-partner-dependent lead**; not available to count in current usable capacity. |

**Offer conflicts and time bounds:** AMD's program-specific [$100/30-day member terms](https://developer.amd.com/resources/) and [AMD Developer Cloud FAQ](https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html) conflict with the [general cloud comparison's 25h/~$50/10-day description](https://www.amd.com/en/developer/resources/cloud-access.html). Neither is a usable credit without confirming the exact applicant offer, account region, hardware class, terms and expiry. Do not substitute an old promotional figure or advertise a guaranteed grant.

## Three legal/applicant situations (separate determinations)

| Route | Present independent community | Actual fiscally sponsored project | Independently recognized 501(c)(3) |
| --- | --- | --- | --- |
| AMD | Individual qualifying developer **may apply**; organizational status does not itself confer a credit | A qualified developer could potentially apply in the supported manner; fiscal sponsorship alone is not approval | Same developer-program criteria; tax exemption alone not an entitlement |
| NVIDIA | No eligible faculty member/academic institution established; intake currently closed | A real qualified faculty PI and accredited institution would still be required; intake closed | Nonprofit status alone does not meet faculty/institution rule; intake closed |
| Hugging Face | Public Space grant may be requested if an actual Space meets criteria; not yet demonstrated | Same Space-specific criteria, with actual control and rights to be documented | Same Space criteria; nonprofit status not a guaranteed grant |
| Google | No qualified academic/eligible research-institution applicant documented | A qualifying applicant/institution relationship would need direct verification; sponsor status alone insufficient | Eligible nonprofit **research institution** may be covered under specific terms, but ordinary 501(c)(3) status is not enough |
| AWS | No accredited-research-institution researcher or institutional account evidenced | Partner would need qualifying institutional researcher, account and authorization | Nonprofit status is not itself eligibility under the published academic-researcher definition |

For every row: applicant identity, country, legal authority, data rights, quota, payment method, grant decision, useful time, actual utilization, overage treatment and publication permissions are **Unknown unless stated as an explicit published condition**. Do not list any unconfirmed organization or individual as an applicant. A historical program page is not a current award.

## Concrete research use case and acceptance gates

The proposed bounded use is **reproducible, vendor-neutral comparisons of model deployment and inference**: pin a public model/quantization and software build; define prompt/task fixtures with rights, input/output retention and privacy rules; collect latency, throughput, memory, stability, cost and limitations; publish both favorable and unfavorable results. Preserve each provider's hardware/driver/library constraints rather than treating MI300X, H100, ZeroGPU and generic EC2/GCE GPU instances as interchangeable.

The accepted [compute demand method](../../docs/funding/compute-demand-model.md) and its [structured inputs](../../data/budget/compute-demand-model.json) specify the framework, **not** a confirmed benchmark workload, account, provider entitlement or cash spending baseline. Before any real use:

1. Obtain explicit approval for provider-specific scope, actual applicant/control and rights; external accounts, card enrollment and provider applications are **out of scope** for this research contribution.
2. Define an offline fixture list, model licenses, exact GPU class, required VRAM, framework/driver, hours, storage and permitted publication. Confirm the offer allows the precise benchmark outputs and data policy.
3. Verify live account eligibility and quota via an authorized operator only after the separate organizational and financial gates. If credit can bill after expiration, require a verified no-overage control or classify as **not presently usable**.
4. Preselect teardown/export/backup criteria. On AMD, official documentation states powered-off instances can still be charged and credits do not generally cover storage/backup; running out of credit can destroy access and data.
5. Only then form a ranking for [#50](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/50). **Do not rank Unknown as zero or use the advertised maximum as net benefit.**

Conditional usable-support calculation for a future authorized operator (not an observation):

`usable_hours = min(approved_eligible_hours, available_quota_hours, eligible_credit / verified_effective_hourly_rate, planned_runnable_hours_before_expiry)`

`potential_reference_coverage = eligible_usable_hours * verified_reference_price_of_equivalent_eligible_workload`

**This expression is potential reference-priced coverage, not actual avoided cash.** A zero-spend counterfactual (for example existing free capacity) cannot generate cash savings. Under the accepted [#50 value method](usable-support-ranking.md#6-value-equations-and-unknown-propagation), only after actual supported utilization, a **necessary counterfactual cash purchase** `B`, actual covered cash `A`, and incremental cash `I` are evidenced may a realized estimate use `gross_avoided_cash = min(B, A)` and `net_avoided_cash = min(B, A) - I`. Actual project avoided cash remains **Unknown**, not reference hours × price minus an imagined cash cost.

The calculation must retain Unknowns as Unknown, enforce zero-overage and explicitly separate **cash**, **restricted credit** and **avoidable expense**. It is invalid when hardware class, rate, quota or rights cannot be compared. The credit has no cash resale value and should not be represented as donations received.

## Restrictions and controls requiring receiving review

- **Privacy and security:** No production data, credentials, donor identities or private user prompts in grant applications or public fixtures. Provider/cloud data retention and processing terms require separate legal/security inspection. Use only synthetic or rights-cleared samples.
- **Licenses and benchmark/publication rights:** A published provider page does not grant all model, benchmark, dataset or trademark rights. Check program conditions and model licenses before tests; record negative findings without sponsor editorial control.
- **Payments and renewal:** No card entry or subscription in this research. Confirm zero-cost enrollment, trial expiry, storage and egress fees, stop vs destroy semantics, overage and project ownership with the actual account owner before operations.
- **Migration/exit:** Preserve local environment/container specs, assets and evidence metadata; never depend on a temporary VM as the sole artifact store. Do not claim successful provisioning, model execution or zero charges.
- **Independence and governance:** An ineligible or inactive program remains useful as an explicit negative outcome. No favoritism, application, sponsorship agreement, nonprofit authority, partner commitment or cloud-resource acceptance is implicit.

## Evidence ledger (official public-source page reads, 2026-11-17)

| Ref | Publisher, URL | What was inspected / evidence limit |
| --- | --- | --- |
| A1 | AMD, https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html | Developer cloud, $100 program-linked credit, expiry, third-party billing, ownership/teardown conditions; not an applicant decision |
| A2 | AMD AI Developer Program, https://developer.amd.com/resources/ | Member-program credit conditions and 30-day term; must reconcile other official AMD page |
| A3 | AMD cloud overview, https://www.amd.com/en/developer/resources/cloud-access.html | Conflicting 25-hour/$50/10-day description; exact offer uncertain |
| N1 | NVIDIA, https://www.nvidia.com/en-us/industries/higher-education-research/academic-grant-program/ | Faculty eligibility, proposed resources, explicit closed intake; visible historical links not treated as open |
| H1 | Hugging Face, https://huggingface.co/docs/hub/en/spaces-gpus | Space hardware and discretionary community GPU grant; not unrestricted VM access |
| G1 | Google for Education, https://edu.google.com/programs/credits/research/ | Academic/nonprofit research institution criteria and noncommercial research-credit form; no application or quota |
| W1 | AWS, https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/ | Rolling application, institutional researcher definitions, EC2 and credit conditions; no award |
| W2 | AWS FAQ, https://aws.amazon.com/government-education/research-and-technical-computing/cloud-credit-for-research/faqs/ | Institutional email/account prerequisites and excluded general workloads |
| W3 | AWS Promotional Credit Terms, https://aws.amazon.com/awscredits/ | §8 credit-disclosure consent; §11 confidentiality of information learned through service; public research does not substitute for consent |
| G2 | Google billing FAQ, https://support.google.com/google-cloud-higher-ed/answer/10724373 | Account-specific credit use, nonretroactive charges and activation controls |
| G3 | Google program FAQ, https://support.google.com/google-cloud-higher-ed/answer/10723679 | Published expiry trigger discrepancy; actual award notice controls |

These sources are checked **as of the indicated date only**; they may change and should be rechecked before any actual decision. Only first-party published terms were read, with no account authentication, third-party SDK invocation, benchmarking, payment or registration.

## Outstanding work and handoff for #48 and #50

- **Canonical structured integration:** deduplicate against current `data/opportunities.json`; add/adjust a unique program record only if the exact scheme and provider identity warrant it; serialize `data/funding-pipeline.json`, `data/research-freshness.json` and their documentation projections. None was changed in this document-only recovery.
- **Review/acceptance:** independent reviewer must check each literal issue criterion and the current sources, identify the reviewed commit, and decide whether documentation-only research is sufficient. The historical local source described in #48 remains separately preserved; this is a new publicly reproducible version, not a claim to have recovered its private bytes.
- **Missing facts:** no actual PI, fiscal sponsor, cloud subscription, operator, authorized benchmark dataset, capacity, price, quota or credit award is verified. Eligibility and usable cost remain Unknown; a specific matching program may be screened out without becoming an application.
- **No completion claim:** this note supplies five sourced routes and a comparison method but does **not** close #48 or unblock #50 until structured reconciliation and independent acceptance are completed.