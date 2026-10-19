# Research freshness register

**Draft — source check dates are evidence, not a standing eligibility guarantee.** Prepared 2026-10-19. Owning work: [E09-04 #70](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/70).

The [source register](../data/research-freshness.json) tracks 146 distinct source and endpoint URLs for the 39 opportunity records: 127 governing-source URLs, including the independently accepted Apple, Together, OpenAI, Anthropic, Google, Azure and AWS assessments, plus 19 additional program/application/setup endpoints. Newly identified endpoints keep `last_verified` null until their actual contents are checked. The OpenAI application endpoint records the observed public homepage separately from the unverified program-specific form. Each row records supported programs, its role, known access results and event-based recheck triggers. Next internal review dates and people assignments remain null.

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

Every distinct `official_program_url`, `official_application_url` and `application_url` must appear in the source register, even when a form is inaccessible, requires an account or belongs to a closed program. The AWS application workbook retains a null successful-verification date. Its historical seed HTTP403, the author's later internal access errors without visible status, and the independent reviewer's explicit HTTP403 without bytes at approximately12:30UTC are separate observations in the [AWS assessment](../research/infrastructure/aws-open-source-credits.md) and [actual findings review](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/100#pullrequestreview-5571815080). A monthly reviewer must revisit the failed result; a program-page refresh cannot silently refresh the workbook.

The independently accepted [Azure nonprofit AI assessment](../research/compute/azure-nonprofit-ai.md) adds a scoped 16-source investigation, preserving its actual registration/tutorial access failures and the Foundry overview/Product Terms inconsistency. These observations do not verify a private offer, applicant, model meter or grant balance. Unrelated source observations keep their recorded scope.

## Cloudflare assessment

The [canonical Project Alexandria assessment](../research/infrastructure/cloudflare-project-alexandria.md) uses eleven dated sources, including the historical redirect, product terms/limits/prices and a separately attributed public page-configuration retrieval. Its complete scoped findings are independently accepted in [review 5572334688](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/104#pullrequestreview-5572334688); actual applicant, account, award and usable value remain Unknown. The published invitation/configuration does not establish complete rendered fields, applicant eligibility, an account or an award. The source register retains those distinctions; the bounded proposal and conditional free-alternative example are not measured demand or a provider execution.
