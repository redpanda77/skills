---
name: audit-orchestration
description: How to orchestrate the 5 parallel audit subagents. Use in Phase 1 of the documenting-codebase workflow.
---

# Audit Orchestration

## Overview
In Phase 1, spawn 5 parallel audit subagents. Each subagent analyzes a specific part of the codebase and returns a structured report. The main agent synthesizes all 5 reports into a unified audit.

## How to Spawn

Spawn all 5 in parallel using the `Agent` tool:

```json
{
  "subagent_type": "claude",
  "description": "Audit tech stack",
  "prompt": "Execute the tech stack audit for this codebase.\n\nStep 1: Read exactly:\n- package.json (or requirements.txt, Cargo.toml, go.mod)\n- Dockerfile and docker-compose.yml if present\n- .github/workflows/ for CI/CD\n- Any config files (biome.json, tsconfig.json, etc.)\n\nStep 2: Produce a structured report following the format in `references/audit/tech-stack.md`.\n\nStep 3: Return the report as a single markdown block.\n\nStop after producing the report. Do not write any files to disk."
}
```

Repeat for each of the 5 audit scopes:

1. **tech-stack** — `references/audit/tech-stack.md`
2. **architecture** — `references/audit/architecture.md`
3. **testing** — `references/audit/testing.md`
4. **api-database** — `references/audit/api-database.md`
5. **devops** — `references/audit/devops.md`

## Synthesis

After all 5 subagents return, synthesize their reports into a unified audit:

```markdown
## Unified Audit Report

### Existing Docs
| Doc | Status | Stale? |
|-----|--------|--------|

### Gaps Found
| Doc | Why Missing | Priority |
|-----|-------------|----------|

### Stale Docs
| Doc | What's Wrong | Action |
|-----|--------------|--------|

### Audit Sources
- Tech Stack: [summary]
- Architecture: [summary]
- Testing: [summary]
- API & Database: [summary]
- DevOps: [summary]
```

## Rules

- Spawn all 5 in parallel, not sequentially.
- Each subagent only produces a report — it does NOT write files.
- The main agent synthesizes and decides what to create.
- If a subagent can't find its scope, it reports "No [scope] found" instead of failing.
- If GitNexus is unavailable, the subagent falls back to manual analysis.
