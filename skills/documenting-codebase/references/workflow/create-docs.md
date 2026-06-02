---
name: doc-create-docs
description: How to create individual docs in parallel. Use in Phase 3 of the documenting-codebase workflow.
---

# Create Docs (Phase 3)

## Overview
After planning what docs to create (Phase 2), spawn parallel subagents to write each doc. Up to 4 subagents in parallel.

## How to Spawn

For each doc in the plan, spawn a subagent with a self-contained prompt:

```json
{
  "subagent_type": "claude",
  "description": "Create ARCHITECTURE.md",
  "prompt": "Execute the doc creation task for ARCHITECTURE.md.\n\nStep 1: Read exactly:\n- references/doc-types/architecture.md (the guide)\n- references/templates/architecture.md (the template)\n- The relevant audit report for this scope\n\nStep 2: Write ARCHITECTURE.md at the repo root with the following content:\n[template content, customized with real data from the audit]\n\nStep 3: Return confirmation that the file was written.\n\nStop after writing the file."
}
```

## Parallel Limits

- **Max 4 subagents in parallel** for doc creation.
- If more than 4 docs need to be created, batch them: create 4, then the next 4, etc.
- Group related docs together (e.g., API.md and DATABASE.md can be created in parallel).

## Doc Creation Order

Recommended order:

1. First batch (foundation):
   - `TECH_STACK.md`
   - `GETTING_STARTED.md`
   - `ARCHITECTURE.md`
   - `STRUCTURE.md`

2. Second batch (workflow):
   - `CONVENTIONS.md`
   - `TESTING.md`
   - `DEVELOPMENT.md`

3. Third batch (specific):
   - `API.md`
   - `DATABASE.md`
   - `DEPLOYMENT.md`
   - `TROUBLESHOOTING.md`
   - `DESIGN.md`

## Rules

- Each subagent writes exactly one doc.
- The subagent loads the doc-type guide and template from references.
- The subagent customizes the template with real data from the audit report.
- Do not create a doc if the audit report shows no corresponding code exists.
- After all docs are written, update `docs/index.md` to catalog them.
