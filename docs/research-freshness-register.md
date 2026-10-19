# Research freshness register

**Draft — source check dates are evidence, not a standing eligibility guarantee.** Prepared 2026-10-19. Owning work: [E09-04 #70](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/70).

The [source register](../data/research-freshness.json) tracks 127 distinct source and endpoint URLs for the 39 opportunity records: 111 referenced source/discovery URLs, including the Apple, Together, OpenAI, Anthropic, Gemini and Groq assessments, plus 16 additional program/application endpoints. These are URL membership counts, not 127 successful verifications. The initial review contained 55 source URLs and 17 additional endpoints; the [Groq assessment](../research/compute/groq-support.md) adds current evidence, a separately qualified historical NAIRR lead and explicit access/redirect limits. Unverified contents keep `last_verified` null; a dated observation of a public entry point does not verify the authenticated account or complete form. The OpenAI application endpoint records the observed public homepage separately from the unverified program-specific form. Each row records supported programs, its role, known access results and event-based recheck triggers. Next internal review dates and people assignments remain null.

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
