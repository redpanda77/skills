---
name: codebase-map-context-fork
description: Use when producing a structured map of a feature area or module tree in isolation. Returns a bounded map, not a wall of code.
context: fork
---

# Codebase map (forked)

## Goal

Produce a **navigable map** of a subsystem: entrypoints, modules, and dependencies.

## Method

1. Identify top-level folders and public entry APIs.
2. Use search to find imports/callers of the focal symbol or route.
3. Read only representative files per module.

## Output

- `Scope`
- `Entrypoints`
- `Modules` (1–3 bullets each)
- `Data boundaries`
- `Unknowns / assumptions`
