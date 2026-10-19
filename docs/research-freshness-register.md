# Research freshness register

**Draft — source check dates are evidence, not a standing eligibility guarantee.** Prepared 2026-10-19. Owning work: [E09-04 #70](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/70).

The [source register](../data/research-freshness.json) tracks 140 distinct source and endpoint URLs for the 39 opportunity records: 118 governing-source URLs, including the independently accepted Apple, Together, OpenAI, Anthropic, Google and Cerebras assessments, plus 22 additional program/application/setup endpoints. Newly identified endpoints keep `last_verified` null until their actual contents are checked. The OpenAI application endpoint records the observed public homepage separately from the unverified program-specific form. Each row records supported programs, its role, known access results and event-based recheck triggers. Next internal review dates and people assignments remain null.

## Review triggers

- Include current opportunities in the program’s monthly review procedure.
- Recheck immediately before relying on a source in an application, agreement, activation or public eligibility claim.
- Requalify a record when the official page redirects, intake opens/closes, terms change, source facts conflict, or a price/credit/quota changes.
- Compare the current statement with historical evidence instead of overwriting the historical event date.

The currently closed NVIDIA, GSoC, Spencer and NGI Zero Commons records cannot be reopened by elapsed time alone. Gemini's applicant/award gates and Together's invitation/intake ambiguity need actual new evidence. A sponsor or nonprofit recognition decision cannot automatically replace missing academic, jurisdiction or scope eligibility facts.

## Review output

Record the exact source checked, current observation, prior observation, affected claim and opportunity, reviewer evidence, and any resulting triage change. If a source is unavailable, preserve the previous access date and mark the relevant current claim Not Verified. Do not mark the record freshly verified merely because another page linked to it.

Read the [freshness policy](research-freshness.md) and [methodology](research-methodology.md). This register does not install an automation, assign a reviewer or create arbitrary dates.

## Application endpoints

Every distinct `official_program_url`, `official_application_url` and `application_url` must appear in the source register, even when a form is inaccessible, requires an account or belongs to a closed program. The AWS application workbook retains its recorded HTTP 403 attempt and a null successful-verification date. A monthly reviewer must revisit the failed result; a program-page refresh cannot silently refresh the workbook.

The independently accepted [Azure nonprofit AI assessment](../research/compute/azure-nonprofit-ai.md) adds a scoped 16-source investigation, preserving its actual registration/tutorial access failures and the Foundry overview/Product Terms inconsistency. These observations do not verify a private offer, applicant, model meter or grant balance. Unrelated source observations keep their recorded scope.

The [Cerebras assessment](../research/compute/cerebras-support.md) adds twelve actual source inspections on 2026-10-19 and separately records three content-empty related-program form attempts. It preserves the original trial source, the quota and expiry-label differences, and the cloud endpoint's unsuccessful form inspection. All four form/account verification dates remain null. The closed historical research RFP and current builder/event/ambassador leads retain separate scope; none establishes a trial entitlement or admitted independent benchmark. The accepted dated [39-program/72-source audit](research-freshness-readback-2026-10-19.md) remains its original snapshot.
