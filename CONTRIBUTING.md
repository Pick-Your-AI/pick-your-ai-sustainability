# Contributing

The [organization-wide contribution rules](https://github.com/Pick-Your-AI/.github/blob/main/CONTRIBUTING.md) remain canonical for access, branches, credentials, reviews and merges. This guide adds the funding research workflow.

## Repository lead maintainers

**Designated joint lead maintainers:** [@CompleteDotTech](https://github.com/CompleteDotTech) and [@appletechie](https://github.com/appletechie) (Apple Teckie). Both are review contacts for repository changes and volunteer coordination. [`.github/CODEOWNERS`](.github/CODEOWNERS) routes review requests to both accounts.

The organization-wide [team and review rules](https://github.com/Pick-Your-AI/.github/blob/main/CONTRIBUTING.md) govern permissions. GitHub's effective grants and branch protections must be read back separately; CODEOWNERS and this declaration do not grant Admin rights or bypass independent review. The [configuration tracking issue](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/143) remains open until both leads have the intended permissions and policy enforcement is verified.

Repository leadership is **not** authorization to represent a nonprofit, approve fiscal transactions, execute agreements, submit grant applications, or solicit sponsorship. Those roles and approvals follow the [program charter](docs/charter.md) and remain independently governed.

Volunteer recruitment and coordination for organization members belong in the **private `internal-discussion` repository**, not the public organization profile repository. Research deliverables and implementation issues remain in this repository and [Project #7](https://github.com/orgs/Pick-Your-AI/projects/7).


1. Read the live issue, its parent, native prerequisites, assignees, comments, deliverable path and existing pull requests.
2. Search the repository, organization and opportunity register for the same provider/program/round or outcome. Extend an existing record when it is the same work; preserve declined and ineligible history.
3. Record primary-source findings, dates, scope, eligibility, restrictions, value assumptions and unknowns using [the method](docs/research-methodology.md).
4. Preserve the canonical technical research, device testing, deployment and market-research issues. A request for donated resources can consume their outputs without moving their implementation here.
5. Submit a pull request with the exact issue and changed records. Use partial references until every criterion and required handoff has been independently accepted.
6. Read the resulting issue and Project state after changes. A local manifest or successful API response alone is insufficient evidence of complete triage.

A contributor may offer ownership; an issue or plan does not assign an absent person. A reviewer must identify the exact reviewed revision and scope, declare material conflicts, and preserve unresolved legal, financial and operating facts. A draft, a schema check, a second agent's analysis or an automated test does not establish a legal opinion or an organization's binding approval.

Small steps belong in the issue checklist. Separate outcomes belong in native sub-issues. Use native dependencies only for an actual prerequisite output; ordinary evidence links need no execution-order edge.

Keep credentials, banking details, private donor identities, confidential applications and security findings out of public artifacts. Follow the affected repository's security policy. Third-party material retains its own rights; citation or a public URL does not authorize copying or redistribution. Repository license and intellectual-property stewardship questions are owned by E01.07.

## Local validation

Use Python 3.12 and an isolated virtual environment. From the repository root:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-validation.txt
python -m unittest discover -s tests -v
python scripts/validate_repository.py
```

The validator reads local files only. It parses repository JSON, validates the opportunity register against its Draft 2020-12 schema (including URI/date formats), checks required template fields while allowing blank placeholders, and reconciles unique IDs, counts, pipeline projections and source/program/application URL coverage. Update the pipeline and freshness membership when updating a canonical opportunity. Counts, lifecycle stages, scores, dates and ownership are not frozen to the initial draft.

JSON floating-point tokens must stay finite and preserve their original decimal
value in the reader's shortest decimal readback. Whole-valued floats must also
retain the exact integer. Excess precision or nonzero underflow is rejected at
the original parsing boundary, before schema limits and pipeline comparisons;
it cannot silently become a matching score or zero. Ordinary decimals such as
`0.10`, equivalent exponent spellings, signed zero and exact integer values
remain supported. Original file bytes are never rewritten. This checks the
reader's numeric representation, not the accuracy or evidential basis of a score.

URI format checks require a complete match of the original JSON string.
Python's [`$` regular-expression anchor](https://docs.python.org/3.12/library/re.html#regular-expression-syntax)
can match before a final newline (checked 2026-10-19); that prefix alone does
not validate the complete URI value. Literal trailing newlines are rejected in
canonical URI fields, freshness source URLs and filled template values.
Permitted percent-encoded content such as `%0A` retains its existing syntax
treatment, and original strings and file bytes are preserved without trimming.

Markdown links and images are parsed as CommonMark, including reference links and tables. Relative and repository-root paths must exist inside the checkout. Code examples, external URLs and fragments are not checked; this is not a live-source freshness check or a heading-anchor/HTML-link checker. Local virtual environments, Git metadata, dependency directories and bytecode caches are excluded. External JSON Schema references are refused instead of fetched.

The [validation workflow](.github/workflows/validate.yml) runs the same commands for pull requests to any target branch (including stacked contributions) and pushes to `main`, with only `contents: read` permission. It uses immutable releases of [checkout v7.0.1](https://github.com/actions/checkout/releases/tag/v7.0.1) and [setup-python v7.0.0](https://github.com/actions/setup-python/releases/tag/v7.0.0). Direct dependencies are pinned to official PyPI releases: [jsonschema 4.26.0](https://pypi.org/project/jsonschema/4.26.0/), [markdown-it-py 4.0.0](https://pypi.org/project/markdown-it-py/4.0.0/), [rfc3986-validator 0.1.1](https://pypi.org/project/rfc3986-validator/0.1.1/), and [PyYAML 6.0.3](https://pypi.org/project/PyYAML/6.0.3/). Reverify the official tag-to-commit mapping when updating action pins.

Passing checks establishes local consistency, not independent research acceptance, current provider availability, applicant qualification or permission to apply. The separate native-relationship workflow retains its existing scope and authorization gates.
