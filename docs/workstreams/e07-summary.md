# E07 — Code quality, security and development tools (provisional synthesis)

**Owning epic:** [#8](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/issues/8). **Prepared:** 2026-11-17 from accepted [`main` `f19d1a7141ca`](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/commit/f19d1a7141cafffd5b6d1b5c2ce4f8a922619fa1) and current review statuses. This is research about support, **not** a deployed SDK, completed third-party audit, accessibility certification, paid license or review of confidential vulnerabilities.

## Support-screen decision

**P1 coordination:** retain existing free, publicly reviewable tests and security controls until a specific uncovered need and responsible maintainer are established. Outsourced audits, grant-backed audits, accessibility user testing, generic static tools and developer-subscription concessions serve different purposes and may impose different disclosure/retention costs.

| Child | Current disposition | What remains |
| --- | --- | --- |
| Closed #56–#58 / #60 | [CodeRabbit OSS](../../research/tooling/coderabbit-oss.md), [GitHub baseline](../../research/tooling/github-baseline.md), JetBrains and [Apple fee-waiver](../../research/tooling/apple-fee-waiver.md) research are separate documented packages | Do not equate access to a tool with a live installed security control, actual device result or eligibility |
| Open #59 | [PR #160](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/160) proposes independent security versus accessibility support research | Current `OSTIF-SECURITY` record exists; reconcile that single identity and source limits, obtain independent findings review; no audit/quote/sponsor awarded |
| Open #61 | [PR #155](https://github.com/Pick-Your-AI/pick-your-ai-sustainability/pull/155) restores a bounded support-stack comparison | Existing `OPENAI-CODEX-OSS` and `ANTHROPIC-CLAUDE-OSS` records remain separate from personal account eligibility; reconcile source and disposition only after receiving review |

## Handling accepted-main data

At the 2026-11-17 readback, `OSTIF-SECURITY`, `OPENAI-CODEX-OSS` and `ANTHROPIC-CLAUDE-OSS` already exist in [opportunities](../../data/opportunities.json), each with a matching pipeline row and tracked source URLs. Their historical `work_status: Blocked` is **not** evidence that the newly reopened research is completed or the provider is unavailable; issue readiness and historical register snapshots require deliberate reconciliation. Update [pipeline](../../data/funding-pipeline.json) and [freshness](../../data/research-freshness.json) only with exactly supported, rights-safe source evidence.

**Disposition:** *In progress; #59 and #61 are pending independent review and safe integrated research.* No new security findings, real participant data, account credentials or third-party service communications may be published under this synthesis. Do not close #8 until those children and this final revision are accepted.
