---
source_urls:
  - https://code.claude.com/docs/en/sub-agents#common-patterns
last_reviewed: 2026-05-13
---

# Agent patterns

Durable shapes — adapt names/tools to the repo.

## Research agent

**Use for:** large codebase exploration.

**Good tools:** `Read`, `Glob`, `Grep`.

**Usually avoid:** `Edit`, `Write`, destructive `Bash`.

**Return:** concise findings, **file paths**, risks, next steps — not raw file dumps.

## Reviewer agent

**Use for:** independent audit after changes.

**Variants:** code, security, performance, tests, migrations.

**Return:** issues by **severity**, **evidence** (paths + snippets), suggested fix, likely false positives called out.

## Debugger agent

**Use for:** noisy logs, failing tests, stack traces, repro searches.

**Return:** likely root cause, evidence, **minimal** fix, tests/commands to verify.

## Implementer agent

**Use only when** edits are expected and scoped.

**Good for:** narrow features, codemods, repetitive project edits.

**Avoid for:** vague product direction, high-risk migrations without review gates, “figure out what I want” tasks.

## Validator agent

**Use for:** checking outputs, SQL, migrations, generated artifacts, plans.

Often **read-only**; commonly **paired after** an implementer in a chain.
