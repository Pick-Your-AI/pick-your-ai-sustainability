#!/usr/bin/env python3
"""Validate local sustainability evidence and Markdown targets without network access."""

import argparse
import json
import math
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError
from markdown_it import MarkdownIt
from referencing import Registry
from referencing.exceptions import Unresolvable
from rfc3986_validator import validate_rfc3986


FORMAT_CHECKER = FormatChecker(["date"])


@FORMAT_CHECKER.checks("uri")
def is_uri(value):
    # Explicitly register the pinned implementation: optional extras must not
    # silently decide whether URI checks run in a particular Python environment.
    return not isinstance(value, str) or validate_rfc3986(value, rule="URI") is not None


REQUIRED_FILES = (
    "data/opportunities.json",
    "data/opportunities.schema.json",
    "templates/opportunity-record.json",
    "data/research-freshness.json",
    "data/funding-pipeline.json",
)
# Pipeline fields are a projection of the canonical register, not separate facts.
PIPELINE_FIELDS = {
    "program_name": "program_name",
    "source_review_status": "source_review_status",
    "owning_research_issue": "linked_github_research_issue",
    "research_status": "work_status",
    "opportunity_stage": "opportunity_stage",
    "disposition": "current_disposition",
    "eligibility": "eligibility_status",
    "application_gate": "application_gate",
    "application_outcome": "application_outcome",
    "award_status": "award_status",
    "activation_status": "activation_status",
    "reporting_status": "reporting_status",
    "verified_deadline": "verified_deadline",
    "deadline_timezone": "deadline_timezone",
    "priority": "priority",
    "score": "score",
    "next_action": "next_action",
}
EXCLUDED_DIRS = {".git", ".venv", "venv", "node_modules", "__pycache__"}


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON property: {key}")
        result[key] = value
    return result


def no_nonfinite(value):
    raise ValueError(f"non-finite JSON number: {value}")


def finite_float(value):
    number = float(value)
    if not math.isfinite(number):
        no_nonfinite(value)
    return number


def repository_files(root):
    """Walk source files, never following directory symlinks or dependency trees."""
    for directory, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in EXCLUDED_DIRS)
        for name in sorted(files):
            path = Path(directory) / name
            if path.suffix.lower() in {".json", ".md"}:
                yield path


def schema_validator(schema, root_schema=None):
    # An explicit empty registry forbids automatic external $ref retrieval.
    validator = Draft202012Validator(
        schema if root_schema is None else root_schema,
        format_checker=FORMAT_CHECKER, registry=Registry()
    )
    return validator if root_schema is None else validator.evolve(schema=schema)


def error_location(location, error):
    return location + "".join("[" + str(part) + "]" for part in error.path)


def schema_errors(value, schema, location):
    try:
        return [
            f"{error_location(location, error)}: {error.message}"
            for error in schema_validator(schema).iter_errors(value)
        ]
    except Unresolvable as error:
        return [f"{location}: unresolved schema reference (network retrieval disabled): {error}"]


def template_errors(value, schema, root_schema):
    """Require the schema's fields while allowing deliberate blank placeholders."""
    location = "templates/opportunity-record.json"
    errors = []
    try:
        for error in schema_validator(schema, root_schema).iter_errors(value):
            object_shape = isinstance(error.schema, dict) and (
                "properties" in error.schema or "required" in error.schema
                or error.schema.get("type") == "object"
            )
            blank = error.instance is None or error.instance == "" or error.instance == []
            if blank and not object_shape:
                continue
            errors.append(f"{error_location(location, error)}: {error.message}")
    except Unresolvable as error:
        errors.append(f"{location}: unresolved schema reference (network retrieval disabled): {error}")
    return errors


def same_json_value(left, right):
    """JSON booleans are not numbers, although Python equates False with 0."""
    if type(left) in (int, float) and type(right) in (int, float):
        return left == right
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(same_json_value(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(same_json_value(a, b) for a, b in zip(left, right))
    return left == right


def indexed_rows(rows, key, location, errors):
    if not isinstance(rows, list):
        errors.append(f"{location}: expected an array")
        return {}
    result = {}
    for position, row in enumerate(rows):
        value = row.get(key) if isinstance(row, dict) else None
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{location}[{position}]: expected nonempty {key}")
        elif value in result:
            errors.append(f"{location}[{position}]: duplicate {key} {value}")
        else:
            result[value] = row
    return result


def check_count(document, key, count, location, errors):
    if type(document.get(key)) is not int or document[key] != count:
        errors.append(f"{location}[{key}]: expected {count}, found {document.get(key)!r}")


def required_urls(record):
    urls = {url for url in record.get("source_urls", []) if isinstance(url, str)}
    for field in ("official_program_url", "official_application_url", "application_url"):
        url = record.get(field)
        if isinstance(url, str) and url:
            urls.add(url)
    return urls


def validate_registers(documents):
    errors = []
    for path in REQUIRED_FILES:
        if not isinstance(documents.get(path), dict):
            errors.append(f"{path}: required JSON object is missing or invalid")
    if errors:
        return errors
    register, schema, template, freshness, pipeline = (documents[p] for p in REQUIRED_FILES)
    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as error:
        return [f"data/opportunities.schema.json: invalid schema: {error.message}"]
    errors.extend(schema_errors(register, schema, "data/opportunities.json"))
    records_schema = schema.get("properties", {}).get("records", {})
    item_schema = records_schema.get("items") if isinstance(records_schema, dict) else None
    if not isinstance(item_schema, dict):
        errors.append("data/opportunities.schema.json: records.items must describe the record template")
    else:
        errors.extend(template_errors(template, item_schema, schema))

    records = indexed_rows(register.get("records"), "opportunity_id", "opportunities.records", errors)
    projections = indexed_rows(pipeline.get("records"), "opportunity_id", "pipeline.records", errors)
    sources = indexed_rows(freshness.get("sources"), "url", "freshness.sources", errors)
    check_count(register, "records_count", len(records), "opportunities", errors)
    check_count(pipeline, "record_count", len(projections), "pipeline", errors)
    check_count(freshness, "records_count", len(records), "freshness", errors)
    check_count(freshness, "source_count", len(sources), "freshness", errors)
    for missing in sorted(records.keys() - projections.keys()):
        errors.append(f"pipeline: missing opportunity {missing}")
    for extra in sorted(projections.keys() - records.keys()):
        errors.append(f"pipeline: unknown opportunity {extra}")
    for identity in sorted(records.keys() & projections.keys()):
        for target, canonical in PIPELINE_FIELDS.items():
            if target not in projections[identity] or not same_json_value(
                projections[identity][target], records[identity].get(canonical)
            ):
                errors.append(f"pipeline[{identity}][{target}]: differs from opportunities[{canonical}]")

    memberships = {}
    for url, source in sources.items():
        errors.extend(schema_errors(url, {"type": "string", "format": "uri"}, "freshness.url"))
        ids = source.get("opportunity_ids")
        if not isinstance(ids, list) or any(not isinstance(identity, str) for identity in ids):
            errors.append(f"freshness[{url}]: opportunity_ids must be an array of strings")
            continue
        memberships[url] = set(ids)
        if len(ids) != len(memberships[url]):
            errors.append(f"freshness[{url}]: duplicate opportunity membership")
        for identity in sorted(memberships[url] - records.keys()):
            errors.append(f"freshness[{url}]: unknown opportunity {identity}")
    for identity, record in records.items():
        if not isinstance(record.get("source_urls"), list):
            continue  # Already reported by the schema; avoid cascading type errors.
        for url in sorted(required_urls(record)):
            if url not in sources:
                errors.append(f"freshness: missing source/program/application URL for {identity}: {url}")
            elif identity not in memberships.get(url, set()):
                errors.append(f"freshness[{url}]: missing opportunity membership {identity}")
    return errors


def markdown_urls(tokens):
    for token in tokens:
        if token.type == "link_open":
            yield token.attrGet("href")
        elif token.type == "image":
            yield token.attrGet("src")
        if token.children:
            yield from markdown_urls(token.children)


def validate_links(root, path, text):
    """Check parsed Markdown link/image paths; do not fetch URLs or validate anchors."""
    errors = []
    parser = MarkdownIt("commonmark").enable("table")
    for url in markdown_urls(parser.parse(text)):
        if not url:
            continue
        try:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            decoded = unquote(parts.path)
            target = (root / decoded.lstrip("/") if decoded.startswith("/") else path.parent / decoded).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: local link leaves repository: {url}")
            elif not target.exists():
                errors.append(f"{path.relative_to(root)}: missing local link target: {url}")
        except (ValueError, OSError, RuntimeError) as error:
            errors.append(f"{path.relative_to(root)}: invalid local link {url!r}: {error}")
    return errors


def validate_repository(root):
    root = Path(root).resolve()
    errors, documents = [], {}
    json_count = markdown_count = 0
    for path in repository_files(root):
        relative = path.relative_to(root).as_posix()
        try:
            if not path.resolve().is_relative_to(root):
                errors.append(f"{relative}: source symlink leaves repository")
                continue
            content = path.read_text(encoding="utf-8")
            if path.suffix.lower() == ".json":
                json_count += 1
                documents[relative] = json.loads(
                    content, object_pairs_hook=no_duplicate_keys, parse_constant=no_nonfinite,
                    parse_float=finite_float
                )
            else:
                markdown_count += 1
                errors.extend(validate_links(root, path, content))
        except (ValueError, OSError, RuntimeError) as error:
            errors.append(f"{relative}: {error}")
    errors.extend(validate_registers(documents))
    return errors, {"json_files": json_count, "markdown_files": markdown_count}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors, counts = validate_repository(args.root)
    for error in errors:
        print(f"ERROR: {error}")
    print(f"{'FAIL' if errors else 'PASS'}: {counts['json_files']} JSON files, "
          f"{counts['markdown_files']} Markdown files; {len(errors)} errors. "
          "Local consistency only; no source freshness or research acceptance claimed.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
