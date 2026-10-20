#!/usr/bin/env python3
"""Reproduce a dated dashboard from pinned Git bytes and retained GitHub reads.

This command is offline. It neither refreshes provider observations nor changes
registers, Project fields, lifecycle states, financial facts or assignments.
"""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_AUDIT = "data/audits/dashboard-readback-2026-10-20.json"
REPOSITORY = "Pick-Your-AI/pick-your-ai-sustainability"
GITHUB = "https://github.com/" + REPOSITORY
REPOSITORIES = tuple("Pick-Your-AI/pick-your-ai-" + name for name in (
    "leaderboard", "sustainability", "website", "research", "apple", "android",
))
DATA_PATHS = (
    "data/opportunities.json",
    "data/funding-pipeline.json",
    "data/research-freshness.json",
    "data/budget/operating-budget.json",
)
METHOD_PATHS = (
    "docs/operations-and-reporting.md",
    "docs/research-freshness.md",
    "docs/risk-indicators.md",
    "docs/needs-assessment.md",
)
STAGES = (
    "Discovered", "Verified", "Qualified", "Preparing", "Submitted",
    "Awarded", "Declined", "Activated", "Reporting",
)
PROJECTION_FIELDS = {
    "program_name": "program_name",
    "work_status": "research_status",
    "opportunity_stage": "opportunity_stage",
    "linked_github_research_issue": "owning_research_issue",
    "priority": "priority",
    "verified_deadline": "verified_deadline",
    "deadline_timezone": "deadline_timezone",
    "eligibility_status": "eligibility",
    "application_gate": "application_gate",
    "current_disposition": "disposition",
}


class DashboardError(ValueError):
    """The available evidence cannot support an unambiguous report."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DashboardError(message)


def strict_json(raw: bytes | str) -> Any:
    def pairs(entries):
        result = {}
        for key, value in entries:
            require(key not in result, "Duplicate JSON property: " + key)
            result[key] = value
        return result

    def number(value):
        result = float(value)
        require(math.isfinite(result), "Non-finite JSON number: " + value)
        return result

    def invalid(value):
        raise DashboardError("Non-finite JSON number: " + value)

    return json.loads(raw, object_pairs_hook=pairs, parse_float=number, parse_constant=invalid)


def instant(value: str) -> datetime:
    require(isinstance(value, str), "Capture time must be an explicit timestamp")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise DashboardError("Invalid capture timestamp: " + value) from exc
    require(result.tzinfo is not None, "Capture timestamp needs an explicit timezone")
    return result


def index_rows(rows: Any, key: str, label: str) -> dict[str, dict]:
    require(isinstance(rows, list), label + " must be a list")
    result = {}
    for row in rows:
        require(isinstance(row, dict), label + " contains a non-object row")
        identity = row.get(key)
        require(isinstance(identity, str) and bool(identity.strip()), label + " has a missing identity")
        require(identity not in result, label + " has duplicate identity " + identity)
        result[identity] = row
    return result


def counts(rows: list[dict], key: str) -> dict[str, int]:
    values = []
    for row in rows:
        value = row.get(key)
        require(value is None or isinstance(value, str), "Non-text category: " + key)
        values.append(value if value else "Unknown / not recorded")
    return dict(sorted(Counter(values).items()))


def complete_review_pointer(row: dict) -> bool:
    """Reference coverage, deliberately not a new substantive acceptance decision."""
    review = row.get("review") or {}
    return (
        isinstance(review, dict)
        and isinstance(review.get("reviewer"), str)
        and bool(review["reviewer"].strip())
        and isinstance(review.get("reviewed_revision"), str)
        and bool(re.fullmatch(r"[0-9a-f]{40}", review.get("reviewed_revision") or ""))
        and isinstance(review.get("review_url"), str)
        and bool(re.match(r"https://[^/]+/\S+", review.get("review_url") or ""))
    )


def load_inputs(audit: dict, root: Path, input_directory: Path | None = None) -> dict:
    require(audit.get("schema_version") == "sustainability-dashboard-readback/v1", "Unsupported dashboard audit schema")
    inputs = audit.get("inputs", {})
    require(isinstance(inputs, dict), "Audit inputs must be an object")
    require(set(inputs) == set(DATA_PATHS + METHOD_PATHS), "Audit must pin the four data and four method/needs files")
    loaded = {}
    for path, pin in inputs.items():
        require(isinstance(pin, dict), "Invalid input pin for " + path)
        require(bool(re.fullmatch(r"[0-9a-f]{40}", pin.get("revision", ""))), "Invalid source revision for " + path)
        require(bool(re.fullmatch(r"[0-9a-f]{64}", pin.get("sha256", ""))), "Invalid source digest for " + path)
        if input_directory is None:
            try:
                raw = subprocess.check_output(
                    ["git", "--no-replace-objects", "show", pin["revision"] + ":" + path],
                    cwd=root, stderr=subprocess.PIPE,
                )
            except subprocess.CalledProcessError as exc:
                raise DashboardError("Pinned Git input unavailable: " + path + "; fetch the stated revision or supply --input-directory") from exc
        else:
            resolved = (input_directory / path).resolve()
            require(resolved.is_relative_to(input_directory.resolve()), "Input path escapes supplied directory")
            raw = resolved.read_bytes()
        require(len(raw) == pin.get("bytes"), "Input byte length differs: " + path)
        require(hashlib.sha256(raw).hexdigest() == pin["sha256"], "Input SHA256 differs: " + path)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(blob == pin.get("git_blob"), "Input Git blob differs: " + path)
        if path in DATA_PATHS:
            loaded[path] = strict_json(raw)
    return loaded


def github_metrics(observation: dict, discrepancies: list[dict]) -> dict:
    start = instant(observation["capture_started_at"])
    finish = instant(observation["capture_completed_at"])
    require(start <= finish, "GitHub capture window is reversed")
    pages = observation.get("sustainability_issue_pages", [])
    rows = []
    seen = set()
    totals = set()
    complete = bool(pages)
    for page in pages:
        complete = complete and page.get("incomplete_results") is False and not page.get("error")
        total = page.get("total_count")
        complete = complete and type(total) is int and total >= 0
        if type(total) is int:
            totals.add(total)
        items = page.get("items")
        if not isinstance(items, list):
            complete = False
            discrepancies.append({"kind": "github_missing_page_response", "page": page.get("page"), "result": "Unknown; explicit item array missing"})
            continue
        for row in items:
            require(type(row.get("id")) is int and row["id"] > 0, "GitHub issue identity is missing")
            require(row["id"] not in seen, "GitHub pagination repeats issue ID " + str(row["id"]))
            require(row.get("is_pull_request") is False, "PR contaminated the issue-only population")
            require(row.get("state") in {"open", "closed"}, "Unknown GitHub issue state")
            seen.add(row["id"])
            rows.append(row)
    complete = complete and len(totals) == 1 and len(rows) == next(iter(totals), -1)
    if not complete:
        discrepancies.append({"kind": "github_issue_coverage", "observed_rows": len(rows), "reported_totals": sorted(totals), "result": "Unknown; incomplete or inconsistent pagination"})
    kinds = Counter()
    keys = set()
    for row in rows:
        key = row.get("tracking_key")
        if not key or key in keys:
            discrepancies.append({"kind": "tracking_key", "issue": row["number"], "key": key})
        keys.add(key)
        kind = "Program" if key == "PROGRAM" else "Epic" if isinstance(key, str) and re.fullmatch(r"E\d{2}", key) else "Task" if isinstance(key, str) and re.fullmatch(r"E\d{2}-\d{2}[A-Z]?", key) else "Unclassified"
        kinds[kind] += 1
    repository_counts = []
    request_keys = set()
    for row in observation.get("repository_open_counts", []):
        key = (row.get("repository"), row.get("kind"))
        require(key not in request_keys, "Duplicate repository/type count query")
        request_keys.add(key)
        require(row.get("repository") in REPOSITORIES, "Repository count outside the six-project scope")
        require(row.get("kind") in {"issue", "pull_request"}, "Untyped GitHub count")
        usable = row.get("incomplete_results") is False and type(row.get("total_count")) is int and row["total_count"] >= 0 and not row.get("error")
        sample = row.get("sample")
        if sample is not None:
            usable = usable and sample.get("state") == "open" and sample.get("is_pull_request") is (row["kind"] == "pull_request")
        if not usable:
            discrepancies.append({"kind": "repository_query_coverage", "repository": row.get("repository"), "type": row.get("kind"), "result": "Unknown"})
        repository_counts.append({**row, "count": row["total_count"] if usable else None})
    for repository in REPOSITORIES:
        for kind in ("issue", "pull_request"):
            if (repository, kind) not in request_keys:
                discrepancies.append({"kind": "missing_repository_query", "repository": repository, "type": kind, "result": "Unknown"})
                repository_counts.append({"repository": repository, "kind": kind, "count": None})
    project = observation.get("project", {})
    require(project.get("item_count") is None and project.get("status_counts") is None, "This audit has no current Project readback; do not invent Project counts")
    return {
        "capture_started_at": observation["capture_started_at"],
        "capture_completed_at": observation["capture_completed_at"],
        "atomic_snapshot": False,
        "issues": {"complete": complete, "total": len(rows) if complete else None, "by_state": counts(rows, "state") if complete else None, "by_kind": dict(sorted(kinds.items())) if complete else None, "observed_rows": len(rows), "rows": rows},
        "repositories": repository_counts,
        "project": project,
    }


def calculate(audit: dict, inputs: dict) -> dict:
    require(audit.get("schema_version") == "sustainability-dashboard-readback/v1", "Unsupported dashboard audit schema")
    require(bool(re.fullmatch(r"data/audits/[A-Za-z0-9_.-]+\.json", audit.get("audit_path", ""))), "Audit needs a repository-relative dated JSON path")
    canonical_revision = audit.get("canonical_revision", "")
    require(bool(re.fullmatch(r"[0-9a-f]{40}", canonical_revision)), "Invalid canonical data revision")
    require(all(audit["inputs"].get(path, {}).get("revision") == canonical_revision for path in DATA_PATHS), "Canonical revision does not match all four data input pins")
    opportunities = inputs[DATA_PATHS[0]]
    pipeline = inputs[DATA_PATHS[1]]
    freshness = inputs[DATA_PATHS[2]]
    budget = inputs[DATA_PATHS[3]]
    indexed = index_rows(opportunities["records"], "opportunity_id", "Opportunity register")
    projected = index_rows(pipeline["records"], "opportunity_id", "Pipeline")
    sources = index_rows(freshness["sources"], "url", "Freshness register")
    rows = [indexed[key] for key in sorted(indexed)]
    names = set()
    for row in rows:
        identity_values = [row.get(key) for key in ("provider", "program_name")]
        require(all(isinstance(value, str) and value.strip() for value in identity_values), "Program/provider identity needs nonempty strings")
        identity = tuple(" ".join(value.casefold().split()) for value in identity_values)
        require(identity not in names, "Repeated provider/program identity; consolidate rounds or resolve distinct identity before counting: " + row["opportunity_id"])
        names.add(identity)
    discrepancies = []
    for name, declared, actual in (
        ("opportunities.records_count", opportunities.get("records_count"), len(rows)),
        ("pipeline.record_count", pipeline.get("record_count"), len(projected)),
        ("freshness.source_count", freshness.get("source_count"), len(sources)),
        ("freshness.records_count", freshness.get("records_count"), len(rows)),
    ):
        if declared != actual:
            discrepancies.append({"kind": "declared_count", "field": name, "declared": declared, "actual": actual})
    for identity in sorted(set(indexed) | set(projected)):
        if identity not in indexed or identity not in projected:
            discrepancies.append({"kind": "projection_identity", "opportunity_id": identity, "canonical": identity in indexed, "pipeline": identity in projected})
            continue
        for left, right in PROJECTION_FIELDS.items():
            if indexed[identity].get(left) != projected[identity].get(right):
                discrepancies.append({"kind": "projection_value", "opportunity_id": identity, "field": left, "canonical": indexed[identity].get(left), "pipeline": projected[identity].get(right)})
    canonical_urls = {url for row in rows for url in row.get("source_urls", [])}
    discovery_urls = set()
    for row in rows:
        for entry in row.get("discovery_sources", []):
            if isinstance(entry, dict) and isinstance(entry.get("url"), str):
                discovery_urls.add(entry["url"])
            else:
                discrepancies.append({"kind": "unclassified_discovery_source", "opportunity_id": row["opportunity_id"]})
    referenced = canonical_urls | discovery_urls
    for url in sorted(referenced - sources.keys()):
        discrepancies.append({"kind": "untracked_reference", "url": url})
    for url, source in sources.items():
        for identity in source.get("opportunity_ids", []):
            if identity not in indexed:
                discrepancies.append({"kind": "unknown_source_membership", "url": url, "opportunity_id": identity})
    without_date = [source for source in sources.values() if source.get("last_verified") is None]
    without_review = [row["opportunity_id"] for row in rows if not complete_review_pointer(row)]
    stages = counts(rows, "opportunity_stage")
    for stage in STAGES:
        stages.setdefault(stage, 0)
    deadlines = [{key: row.get(key) for key in ("opportunity_id", "program_name", "verified_deadline", "deadline_local_time", "deadline_timezone", "deadline_utc", "deadline_source_url", "application_gate")} for row in rows if row.get("verified_deadline") is not None]
    github = github_metrics(audit["github"], discrepancies)
    return {
        "schema_version": "sustainability-dashboard-report/v1",
        "audit_id": audit["audit_id"],
        "audit_path": audit["audit_path"],
        "source_revision": audit["canonical_revision"],
        "inputs": audit["inputs"],
        "definitions": audit["definitions"],
        "github": github,
        "work": {"program_records": len(rows), "by_status": counts(rows, "work_status"), "by_priority": counts(rows, "priority"), "complete_review_pointer_count": len(rows) - len(without_review), "missing_review_pointer_ids": without_review, "unassigned_research_owner_ids": [row["opportunity_id"] for row in rows if row.get("assigned_owner") is None], "distinct_owning_issue_urls": sorted({row["linked_github_research_issue"] for row in rows if row.get("linked_github_research_issue")})},
        "opportunity_stages": stages,
        "program_gates": [{key: row.get(key) for key in ("opportunity_id", "program_name", "round", "work_status", "opportunity_stage", "linked_github_research_issue", "application_gate", "eligibility_status", "current_disposition", "available_before_incorporation", "available_through_fiscal_sponsorship", "available_after_501c3_recognition", "assigned_owner")} for row in rows],
        "freshness": {"tracked_urls": len(sources), "canonical_source_urls": len(canonical_urls), "additional_discovery_urls": len(discovery_urls - canonical_urls), "referenced_source_or_discovery_urls": len(referenced), "tracked_urls_outside_references": len(sources.keys() - referenced), "recorded_successful_check_dates": dict(sorted(Counter(source["last_verified"] for source in sources.values() if source.get("last_verified") is not None).items())), "without_successful_check_count": len(without_date), "without_successful_check": sorted(without_date, key=lambda x: x["url"]), "stale_source_count": None, "stale_scope": "Unknown: no arbitrary age threshold or complete claim-specific current-action validity population is supplied. A recorded successful date is not current availability or full endpoint acceptance."},
        "deadlines": deadlines,
        "resources": {"confirmed_awards": None, "cash_received_by_currency": None, "activated_benefits": None, "realized_avoided_cost_by_currency": None, "actual_expenditure_by_currency": None, "complete_population": None, "reason": "Canonical research records are not a complete event-level financial/operating ledger; no actual recipient/fund/currency/period and complete population is established.", "recorded_pipeline_totals": pipeline.get("funding_totals"), "recorded_budget_actuals": budget.get("actuals"), "recorded_execution_activity": pipeline.get("known_execution_activity"), "non_null_award_evidence_ids": [row["opportunity_id"] for row in rows if row.get("award_evidence") is not None], "non_null_activation_evidence_ids": [row["opportunity_id"] for row in rows if row.get("activation_evidence") is not None]},
        "obligations": {"confirmed_open_count": None, "overdue_count": None, "complete_population": None, "operating_owner": "Unassigned", "recurring_coordinator": "Unassigned", "recurring_reviewer": "Unassigned", "reason": "A program's published restrictions or reporting text does not establish an actual accepted agreement, due trigger, responsible role or complete obligation ledger."},
        "needs_and_risks": {"actual_needs_population_complete": None, "funded_coverage": None, "cash_concentration": None, "essential_resource_dependence": None, "expiring_support": None, "restricted_fund_exposure": None, "exit_cost": None, "ownership_continuity": None, "reason": "Planning needs and proposed budget scenarios are not accepted actual workload, receipt, liability or critical-operation populations. No risk appetite or numeric threshold is adopted."},
        "discrepancies": discrepancies,
    }


def cell(value: Any) -> str:
    if value is None:
        return "Unknown"
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def table(headers: list[str], rows: list[list[Any]]) -> str:
    return "\n".join(["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |", *("| " + " | ".join(cell(item) for item in row) + " |" for row in rows)])


def render_markdown(report: dict) -> str:
    work, github = report["work"], report["github"]
    freshness, resources = report["freshness"], report["resources"]
    parts = [
        "# Sustainability dashboard",
        f"Owner issue: [E09-06 / #72]({GITHUB}/issues/72). Initial populated report `{report['audit_id']}`. Priority **P2**: evidence-based operating visibility for the existing six repositories.",
        f"**GitHub observation window: {github['capture_started_at']} through {github['capture_completed_at']}.** These are actual bounded reads, not an atomic snapshot or a live counter. Canonical register revision: [`{report['source_revision']}`]({GITHUB}/commit/{report['source_revision']}). Later changes do not rewrite this dated report.",
        "Research progress, program lifecycle and actual received support are separate measures. This report performs no provider check, application, account action, financial transaction or Project mutation. Its generic internal reporting process has no provider intake, award amount or external application deadline: **Not applicable**. Actual eligibility, usable value and review effort remain Unknown unless the cited owning record establishes their specific scope.",
        "## 1. Research work and GitHub visibility",
        table(["Canonical-register measure", "Value", "Exact rule / scope"], [
            ["Distinct program/channel records", work["program_records"], "One canonical opportunity_id; alias/round fields create no extra observation."],
            *[["Research status: " + status, count, "Literal work_status; independent of lifecycle or issue closure."] for status, count in work["by_status"].items()],
            ["Complete recorded review pointers", work["complete_review_pointer_count"], "Top-level review has reviewer, full revision and URL. Reference coverage, not a new acceptance decision."],
            ["Missing complete review pointers", len(work["missing_review_pointer_ids"]), "Absence remains visible; nested mechanism reviews do not accept the program owner's research."],
            ["Unassigned canonical research owners", len(work["unassigned_research_owner_ids"]), "assigned_owner is null. Other values remain research-only; none appoints an operator."],
            ["Distinct owning research issues", len(work["distinct_owning_issue_urls"]), "Distinct linked_github_research_issue URLs; several programs may share one research issue."],
        ]),
        table(["Actual Sustainability issue population", "Count"], [["All issue IDs (PRs excluded)", github["issues"]["total"]], *([["State: " + k, v] for k, v in github["issues"]["by_state"].items()] if github["issues"]["by_state"] is not None else [["State totals", None]]), *([["Tracking kind: " + k, v] for k, v in github["issues"]["by_kind"].items()] if github["issues"]["by_kind"] is not None else [["Tracking kinds", None]])]),
        "Issue closure is not independently accepted research, and issue state is not a Project status. The retained paginated responses contain the actual IDs, states and tracking keys. The older 39-record/30-issue link audit is historical and is not reused as this report's population.",
    ]
    repositories = sorted({row["repository"] for row in github["repositories"]})
    count_map = {(row["repository"], row["kind"]): row["count"] for row in github["repositories"]}
    parts += [
        table(["Repository", "Open issues", "Open PRs"], [[f"[{repo.split('/')[-1]}](https://github.com/{repo})", count_map.get((repo, "issue")), count_map.get((repo, "pull_request"))] for repo in repositories]),
        "Repository totals use the exact typed search response total_count with incomplete_results=false, not the single returned sample. Each repository/type is its own scope. These broader project totals are not the Sustainability program denominator.",
        f"**[Project 7]({github['project']['url']}): current item count and status distribution Unknown.** The actual request was rejected by the connected tool's allowed-route check before Projects data was returned. This says nothing about the server's privacy, existence or item population. Historical Project audit files are not a substitute for a current readback.",
        "**Missing review references:** " + ", ".join("`" + identity + "`" for identity in work["missing_review_pointer_ids"]) + ".",
        "## 2. Opportunity lifecycle and unresolved applicant gates",
        table(["Recorded lifecycle", "Program records"], [[stage, report["opportunity_stages"][stage]] for stage in (*STAGES, *sorted(set(report["opportunity_stages"]) - set(STAGES)))]),
        "The zero later-stage counts describe this complete register, not the world's actual application, award or account history. An accepted research result may remain Discovered or Not Pursuing. No free-text eligibility classifier infers an applicant decision. The following exact action-gate text exposes unresolved authority, scope and eligibility; all three route fields are retained separately in the reproducible JSON output and the pinned canonical record.",
        table(["Canonical identity / owning issue", "Research / lifecycle", "Recorded application gate"], [[f"[`{row['opportunity_id']}`]({row['linked_github_research_issue']})", f"{row['work_status']} / {row['opportunity_stage']}", row["application_gate"]] for row in report["program_gates"]]),
        "The present community, fiscal-sponsored route and independently recognized nonprofit route must be reviewed separately under their actual program conditions. A host's classification or another route's result cannot fill an Unknown. Published restrictions on ranking, benchmark publication, data/privacy, portability, branding, overage, renewal and independence remain with each canonical assessment and the accepted operating/risk methods.",
        "### Recorded external deadlines",
        table(["Program", "Published date", "Local time", "Published timezone", "Recorded UTC", "Source"], [[row["opportunity_id"], row["verified_deadline"], row["deadline_local_time"], row["deadline_timezone"], row["deadline_utc"], row["deadline_source_url"]] for row in report["deadlines"]]),
        "These are dated source claims with the stated precision. No timezone, midnight, UTC conversion, next round or internal commitment is inferred. The NSF organization-local cutoff retains Unknown UTC. A deadline alone does not establish eligible scope or permission to act.",
        "## 3. Source evidence and current-action rechecks",
        table(["URL population", "Count", "Counting rule"], [
            ["Tracked source/endpoint URLs", freshness["tracked_urls"], "Unique exact URL in research-freshness.sources."],
            ["Canonical source_urls", freshness["canonical_source_urls"], "Distinct canonical source_urls across program records."],
            ["Additional discovery URLs", freshness["additional_discovery_urls"], "Explicit discovery_sources.url values outside canonical source_urls."],
            ["Referenced source/discovery union", freshness["referenced_source_or_discovery_urls"], "Union of the preceding reference sets, deduplicated."],
            ["Tracked URLs outside that union", freshness["tracked_urls_outside_references"], "Membership difference, not a count of failed or unverified checks."],
            ["No recorded successful-check date", freshness["without_successful_check_count"], "last_verified is null; original attempts and access limits remain intact."],
            *[["Recorded check date: " + date, count, "Observation-date coverage only; no current-availability or full-form claim."] for date, count in freshness["recorded_successful_check_dates"].items()],
            ["Stale current claims", None, freshness["stale_scope"]],
        ]),
        "A failed or partial latest attempt does not erase an older successful observation. Its affected current claim can remain Not Verified even when a date exists. The builder advances no dates and adopts no elapsed-time expiry rule. Recheck applicable sources before a current recommendation, agreement, application, activation or renewal; preserve historical announcements, redirects, inaccessible forms and conflicting terms.",
        table(["No successful check recorded: exact URL", "Roles", "Recorded scope / access state"], [[row["url"], ", ".join(row.get("source_roles", [])), row.get("state")] for row in freshness["without_successful_check"]]),
        "## 4. Resource realization and obligations",
        table(["Actual resource or obligation measure", "Value", "Reason"], [[name, None, reason] for name, reason in [
            ("Confirmed awards", resources["reason"]),
            ("Cash received, separately by currency/fund/custodian/period", "No complete evidenced receipt population. Award ceilings, commitments and credits are excluded."),
            ("Activated noncash capacity / hardware custody", "No complete identity-bound entitlement/delivery population. A loan is not donated ownership."),
            ("Realized avoided cost, separately by currency and use", "No complete actual-use and counterfactual-purchase evidence; unused face value is excluded."),
            ("Actual expenditures and restricted balances", "Planning scenarios do not establish expenditure, eligible balance, settlement or liabilities."),
            ("Open or overdue actual obligations", report["obligations"]["reason"]),
        ]]),
        "Unknown is not zero. Different currencies, cash and credits, loan list prices, commitments and avoided costs are never summed. Empty or absent actual ledgers do not prove no awards, no liabilities or no activity. Source JSON output retains the original funding_totals and budget actuals fields without treating an unqualified aggregate as received support.",
        "### Historical execution scope retained",
        "```json\n" + json.dumps(resources["recorded_execution_activity"], indent=2, ensure_ascii=False) + "\n```",
        "The recorded execution values above belong only to their explicitly stated earlier scope. They do not refresh historical account, award, submission, expenditure or reporting facts at this report's GitHub cutoff.",
        "Use the accepted [operating procedure](operations-and-reporting.md), [benefit record](../templates/benefit-obligation-record.md) and [report](../templates/award-report.md) for actual clause/version, recipient, covered authority, period/trigger, planned versus delivered scope, review, confirmed dispatch and provider acceptance. A report draft or acknowledgment does not close an obligation. Unknown due triggers remain Unknown. No operating owner or recurring appointment is created here.",
        "## 5. Unresolved needs, risks and maintenance",
        table(["Population or risk", "Current result", "Remaining evidence"], [[name, None, need] for name, need in [
            ("Complete actual workload / funded-needs coverage", "Accepted need, denominator, useful quantity, actual received resource and remaining gap; the needs map remains planning context."),
            ("Cash concentration / restricted-fund exposure", "Same currency/category/custodian/period with eligible numerator, denominator and complete population."),
            ("Essential-resource and single-provider dependence", "Evidenced essential workload population and viable alternatives, including dependencies and actual exit conditions."),
            ("Expiry, renewal and exit cost", "Actual accepted terms, verified controls, confirmed expiry/return/export and supported migration effort."),
            ("Critical-operation ownership continuity", "Accepted primary and continuity arrangement for a complete critical-operation inventory. Research assignments are insufficient."),
        ]]),
        "Per the accepted risk method, missing coverage gives Unknown; a complete evidenced zero denominator would be Not applicable with its population evidence. Neither is a low-risk score. Material sponsor influence, publication limits, exclusivity, overage and data/portability terms need their own independent disposition. This report adopts no numerical risk appetite or financial commitment.",
        "**Recurring coordinator and independent reviewer: Unassigned.** The [monthly review template](../templates/dashboard-review.md) requires accepted responsibility, exact source revisions, actual GitHub pagination/visibility, scoped resource evidence, discrepancy reconciliation and a second person's recomputation. Existing authorized engineering work can continue; no new schedule or external action is installed.",
        "## Reconciliation and reproducibility",
        "**Discrepancies: " + str(len(report["discrepancies"])) + ".** " + ("Review required; counts retain their stated scope and no conflicting value is silently repaired." if report["discrepancies"] else "The compared canonical/projection fields and retained GitHub population reconcile within the explicit visibility and actual-resource limits."),
        "```json\n" + json.dumps(report["discrepancies"], indent=2, ensure_ascii=False) + "\n```",
        f"The [dated audit](../{report['audit_path']}) retains the actual GitHub response projections, observation window, unavailable-Project result and exact input hashes. It stores no fabricated operating events. The offline builder verifies every byte length, Git blob and SHA256 before calculating; it reads the stated Git objects, never silently substitutes newer worktree files.",
        "```sh\npython3 scripts/build_dashboard.py --audit " + report["audit_path"] + " --format markdown --check docs/dashboard.md\npython3 scripts/build_dashboard.py --audit " + report["audit_path"] + " --format json\n```",
        "A source archive may supply --input-directory only with the exact eight pinned files; every hash must still match. Reproduction needs no network. If Git objects are missing, fetch the explicitly named public revision before reproducing; the builder fails rather than using an unrelated version. A later monthly report gets a new dated audit and preserves this one.",
        table(["Input path", "Revision", "SHA256"], [[path, f"[`{pin['revision'][:12]}`]({GITHUB}/blob/{pin['revision']}/{path})", "`" + pin["sha256"] + "`"] for path, pin in sorted(report["inputs"].items())]),
        "### Definition inputs and review record",
        table(["Input", "Exact scope and acceptance"], [[row["name"], row["acceptance"]] for row in report["definitions"]]),
        f"Independent initial-report recomputation and final delivery are recorded in [#72]({GITHUB}/issues/72). Local tests validate calculation boundaries and reproducibility; they are not provider research or independent findings acceptance. The recommendation is to use this P2 reporting method within its explicit coverage, and to resolve actual resource/role/Project visibility gaps before claiming support or assigning recurring work.",
    ]
    return "\n\n".join(parts) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", type=Path, default=ROOT / DEFAULT_AUDIT)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--input-directory", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args(argv)
    try:
        require(not (args.output and args.check), "Choose --output or --check")
        audit = strict_json(args.audit.read_bytes())
        report = calculate(audit, load_inputs(audit, args.root, args.input_directory))
        rendered = render_markdown(report) if args.format == "markdown" else json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        if args.check:
            require(args.check.read_text() == rendered, "Dashboard differs from the exact retained inputs")
            print("PASS: exact dated dashboard reproduced; no source refresh or operating fact inferred.")
        elif args.output:
            args.output.write_text(rendered)
        else:
            sys.stdout.write(rendered)
        return 0
    except (DashboardError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
