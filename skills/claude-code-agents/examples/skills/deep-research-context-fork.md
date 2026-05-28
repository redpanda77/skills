---
name: deep-research-context-fork
description: Use when the user wants an isolated deep-dive across many files with a compact summary back to the main thread. Pair with context fork so the skill owns the workflow.
context: fork
---

# Deep research (forked)

This example skill is the **spine** of the workflow; the forked agent provides isolation.

## When to use

- auth flows spanning multiple packages
- performance regressions needing wide reads
- dependency graphs and implicit coupling

## Steps

1. Restate the question and success criteria in one paragraph.
2. Map entrypoints (`Glob`/`Grep`), then read only high-signal files.
3. Trace control/data flow; note extension points.
4. Return: summary, key paths, open questions — **not** raw logs or full files.

## Output contract

- `Summary`
- `Key files`
- `Flow`
- `Risks`
- `Next actions`
