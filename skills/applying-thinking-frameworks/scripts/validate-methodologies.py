#!/usr/bin/env python3
"""Validate all methodology reference files have required sections."""

import os
import re
import sys
from pathlib import Path


def check_frontmatter(content):
    """Check YAML frontmatter exists."""
    return content.startswith("---")


def check_section(content, section_patterns):
    """Check if any of the section patterns exists (flexible matching)."""
    # Extract all ## headers
    headers = re.findall(r"^##\s+(.+)$", content, re.MULTILINE)
    for header in headers:
        for pattern in section_patterns:
            # Match if pattern appears anywhere in the header (case-insensitive)
            if re.search(pattern, header, re.IGNORECASE):
                return True
    return False


def check_core_principle(content):
    """Check for Core Principle as bold text."""
    return re.search(r"\*\*Core Principle:\*\*", content) is not None


def count_checklist_items(content):
    """Count checklist items."""
    items = re.findall(r"-\s*\[\s*\]", content)
    return len(items)


def count_key_questions(content):
    """Count key questions (lines starting with a quote)."""
    questions = re.findall(r'^\s*"', content, re.MULTILINE)
    return len(questions)


def count_words(content):
    """Count words in content."""
    return len(content.split())


def validate_file(filepath):
    """Validate a single methodology file."""
    with open(filepath, "r") as f:
        content = f.read()

    issues = []
    warnings = []

    # Frontmatter
    if not check_frontmatter(content):
        issues.append("Missing YAML frontmatter")

    # Overview
    if not check_section(content, ["Overview"]):
        issues.append("Missing Overview section")

    # Core Principle (bold text)
    if not check_core_principle(content):
        issues.append("Missing Core Principle (bold text)")

    # When to Use
    if not check_section(content, ["When to Use"]):
        issues.append("Missing When to Use section")

    # Process (any step-by-step section)
    process_patterns = [
        r"Process", r"Steps", r"Phases", r"Loop",
        r"Method", r"Framework", r"How to Use", r"Application",
        r"Types of", r"The Six", r"The Five", r"The OODA",
        r"Core Concepts", r"System 1 vs System 2",
        r"How to Apply", r"Applying", r"Techniques",
        r"Identifying", r"Analysis", r"Audit",
        r"Archetypes", r"Diagnosis", r"Principles",
        r"Approach", r"Procedure", r"Algorithm",
        r"Domains", r"Assessment", r"Selection",
        r"Scenario", r"Facilitation", r"Tips",
        r"Inventory", r"Loss Analysis", r"Building",
        r"Response", r"Control vs Predict", r"Outreach",
        r"Iteration", r"Direction", r"Commitments",
        r"Contingencies", r"Next Action",
    ]
    if not check_section(content, process_patterns):
        issues.append("Missing Process-like section")

    # Examples (any example section)
    example_patterns = [
        r"Examples", r"Example", r"Use Cases",
        r"Case Study", r"Case Studies",
        r"Patterns", r"Scenarios",
        r"Common System", r"System Patterns",
        r"Recommendation", r"Red Flags",
        r"Integration", r"Applications",
        r"Reference Card", r"Quick Reference",
        r"Summary", r"Illustration",
        r"Mismatches", r"Practices",
        r"Debugging", r"Test Design",
        r"Effects in", r"Career Analysis",
        r"Dependency Audit", r"Failure Modes",
        r"Why .* Works", r"Failure Categories",
        r"In Practice", r"Lindy in",
        r"Applying", r"Applying .* to",
        r"Partnership", r"Contingency",
        r"Building", r"Analysis",
        r"Control vs", r"Reasoning",
        r"Inventory", r"Loss",
        r"Outreach", r"Log",
    ]
    if not check_section(content, example_patterns):
        issues.append("Missing Examples-like section")

    # Verification Checklist
    if not check_section(content, ["Verification Checklist"]):
        issues.append("Missing Verification Checklist section")

    # Key Questions (any questions section)
    question_patterns = [
        r"Key Questions", r"Key Meta-Questions", r"Meta-Questions",
        r"Questions to Ask", r"Questions",
        r"Questions to Surface",
    ]
    if not check_section(content, question_patterns):
        issues.append("Missing Key Questions section")

    # Quality checks
    checklist_items = count_checklist_items(content)
    if checklist_items < 3:
        warnings.append(f"Only {checklist_items} checklist items (min 3)")

    key_questions = count_key_questions(content)
    if key_questions < 3:
        warnings.append(f"Only {key_questions} key questions (min 3)")

    word_count = count_words(content)
    if word_count > 3500:
        warnings.append(f"{word_count} words (max 3500)")
    if word_count < 300:
        warnings.append(f"{word_count} words (min 300)")

    return issues, warnings


def main():
    methodologies_dir = Path(__file__).parent.parent / "references" / "methodologies"

    if not methodologies_dir.exists():
        print(f"ERROR: Directory not found: {methodologies_dir}")
        sys.exit(1)

    files = sorted(methodologies_dir.glob("*.md"))

    if not files:
        print("WARNING: No methodology files found.")
        sys.exit(0)

    total_issues = 0
    total_warnings = 0
    clean_files = 0

    print(f"Validating {len(files)} methodology files...\n")

    for filepath in files:
        issues, warnings = validate_file(filepath)

        if issues or warnings:
            print(f"{filepath.name}:")
            for issue in issues:
                print(f"  ERROR: {issue}")
                total_issues += 1
            for warning in warnings:
                print(f"  WARNING: {warning}")
                total_warnings += 1
            print()
        else:
            clean_files += 1

    print(f"{'=' * 50}")
    print(f"Files checked: {len(files)}")
    print(f"Clean: {clean_files}")
    print(f"Errors: {total_issues}")
    print(f"Warnings: {total_warnings}")

    if total_issues > 0:
        print("\nFAILED: Fix errors before continuing.")
        sys.exit(1)
    else:
        print("\nPASSED: All methodology files are valid.")
        sys.exit(0)


if __name__ == "__main__":
    main()
