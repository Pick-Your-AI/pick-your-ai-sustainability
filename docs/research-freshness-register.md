# Research freshness register

**Draft — source check dates are evidence, not a standing eligibility guarantee.** Prepared 2026-10-19. Owning work: [E09-04 #70](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/70).

The [source register](../data/research-freshness.json) tracks 102 distinct source and endpoint URLs for the 39 opportunity records: 85 governing-source URLs, including the Apple, Together, OpenAI and AWS assessments, plus 17 additional program/application endpoints. Newly identified endpoints keep `last_verified` null until their actual contents are checked. The OpenAI application endpoint records the observed public homepage separately from the unverified program-specific form. Each row records supported programs, its role, known access results and event-based recheck triggers. Next internal review dates and people assignments remain null.

## Review triggers

- Include current opportunities in the program’s monthly review procedure.
- Recheck immediately before relying on a source in an application, agreement, activation or public eligibility claim.
- Requalify a record when the official page redirects, intake opens/closes, terms change, source facts conflict, or a price/credit/quota changes.
- Compare the current statement with historical evidence instead of overwriting the historical event date.

The currently closed NVIDIA, GSoC, Spencer and NGI Zero Commons records cannot be reopened by elapsed time alone. The Gemini and Together intake uncertainties need actual new evidence. A sponsor or nonprofit recognition decision cannot automatically replace missing academic, jurisdiction or scope eligibility facts.

## Review output

Record the exact source checked, current observation, prior observation, affected claim and opportunity, reviewer evidence, and any resulting triage change. If a source is unavailable, preserve the previous access date and mark the relevant current claim Not Verified. Do not mark the record freshly verified merely because another page linked to it.

Read the [freshness policy](research-freshness.md) and [methodology](research-methodology.md). This register does not install an automation, assign a reviewer or create arbitrary dates.

## Application endpoints

Every distinct `official_program_url`, `official_application_url` and `application_url` must appear in the source register, even when a form is inaccessible, requires an account or belongs to a closed program. The AWS application workbook retains its seed HTTP 403 attempt and a null successful-verification date. The later session c3fa0109d6ff web attempt returned an internal access error without workbook bytes or a visible status; it is not recorded as another observed 403. The [AWS assessment](../research/infrastructure/aws-open-source-credits.md) separates these attempts from successfully read program and governing sources. A monthly reviewer must revisit the failed result; a program-page refresh cannot silently refresh the workbook.
