# Agent Design

How to write an agent file that the harness can route, invoke, and enforce.

## What an agent file is

An agent is a `.md` file in `.claude/agents/` with YAML frontmatter and a Markdown body. The frontmatter is for routing. The body is for behavior. The `AGENT_MANIFEST.json` is the canonical registry.

## Frontmatter schema

```yaml
---
name: curriculum-lesson-repair-worker
category: repair_worker
description: Use when the router detects a lesson judge failed and routes the unit to repair. Reads the failure context, writes the repaired lesson, and returns a WORKER_RECEIPT summary.
tools: Read, Write
skills:
  - curriculum-generator
---
```

### Required fields

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Unique identifier, matches `subagent_type` | `lesson-repair-worker` |
| `category` | Worker class for scope validation | `repair_worker` |
| `description` | Routing signal — the parent LLM decides whether to invoke this agent | `Use when the router detects...` |
| `tools` | Allowed tools (comma-separated) | `Read, Write` |

### Optional fields (from claude-code-agents)

| Field | Purpose | Example |
|-------|---------|---------|
| `skills` | Skills to preload into the agent context | `curriculum-generator` |
| `model` | Model override for this agent | `claude-opus-4-7` |
| `maxTurns` | Max turns before auto-stop | `30` |
| `permissionMode` | Permission level (plan, acceptEdits, etc.) | `acceptEdits` |
| `hooks` | Per-agent hook overrides | `PreToolUse: [...]` |
| `memory` | Memory files to load | `state.json` |

### Rules

- `name` must match the `subagent_type` used in the `Agent` tool invocation
- `description` is the primary routing signal — be specific, not generic
- `tools` is an allowlist, not a blacklist — only listed tools are available
- `skills` preloads domain knowledge without duplicating it in the agent body
- Do not put read/write scope in frontmatter — put it in the Markdown body

## Category taxonomy

| Category | Role | Typical tools |
|----------|------|-------------|
| `planning_worker` | Generates plans, grouping, sequencing | `Read, Write` |
| `artifact_worker` | Generates canonical content units | `Read, Write` |
| `judge_worker` | Evaluates quality against principles | `Read, Write` |
| `repair_worker` | Patches one failed canonical unit | `Read, Write` |
| `audit_worker` | Read-only verification or blocked-state analysis | `Read, Bash` |
| `escape_worker` | Repairs control-layer files only during Escape Protocol | `Read, Write` |
| `deprecated` | Retired stub, rejects accidental invocation | `Read` |

### Rules

- Every agent must have exactly one category
- The category determines the scoped evidence language (see `worker-class-contracts.md`)
- `escape_worker` has restricted tool access and cannot write canonical artifacts
- `deprecated` agents should reject invocation with a clear message

## Read/write scope in the body

Define the scope in the Markdown body, not the frontmatter. The body is the contract the agent reads; the frontmatter is the contract the router reads.

```markdown
## Read only

- The provided context pack and repair instructions
- The exact files listed by the rendered repair prompt
- No raw diagnostics, raw plans, sibling artifacts, or provenance paths unless the rendered prompt lists that exact file
- If the listed files do not contain enough evidence, return `blocked_upstream` and name the missing repair context field

## Write only

- `out/level_{level}/build/canonical/lessons/L{lesson}.json`
```

### Rules

- `Read only` and `Write only` are the standard headings
- Forbidden writes should be explicit: "Do not write to...", "No runtime state..."
- Provenance paths (`source_paths`) are not read lists — their summaries are already in the pack
- If the agent needs more context, it must return `blocked_upstream`, not browse

## Blocked upstream behavior

When a worker needs more evidence, the correct behavior is:

```text
1. Return `blocked_upstream`
2. Name the missing renderer field that must be added
3. Do not browse raw artifacts, sidecars, source_paths, plans, or runtime state
```

This is not a failure. It is a signal that the renderer or handoff scope is incomplete. The parent fixes the renderer, not the worker.

## WORKER_RECEIPT format

Every worker must return a `WORKER_RECEIPT` JSON block. The receipt is the proof that the worker did what it was asked, or why it could not.

```json
{
  "status": "passed | failed | blocked_upstream",
  "agent": "lesson-repair-worker",
  "artifact_path": "out/level_{level}/build/canonical/lessons/L{lesson}.json",
  "validation_status": "not_run",
  "blocker_type": "none | upstream | schema | other",
  "blocker": "",
  "recommended_next": "rerun_router | repair_plan | escape_protocol",
  "target": "L{lesson}",
  "output_path": "out/level_{level}/build/canonical/lessons/L{lesson}.json",
  "summary": "concise status of what was done or why it was blocked",
  "assumptions": ["any assumptions made due to incomplete context"],
  "blocked_reason": "reason if blocked, otherwise empty string"
}
```

### Rules

- The receipt is the worker's only output besides the artifact itself
- The parent does not inspect the artifact to verify the worker — it reads the receipt
- A failed receipt with `blocked_upstream` is a signal to fix the renderer, not to retry the worker
- The receipt must be the last thing the worker produces

## Agent body structure

A well-structured agent body has four sections:

1. **Role statement** — one sentence: what this worker does and does not do
2. **Read only** — exact read scope with blocked_upstream behavior
3. **Write only** — exact write target with forbidden writes
4. **Rules** — stop condition, no-browse rule, no-validator rule, no-scratch-files rule

### Example

```markdown
You repair exactly one failed lesson canonical unit.

The official rendered repair prompt is the task contract.
If a parent prompt conflicts with this agent file or the official rendered prompt,
follow the official prompt and report the conflict in the receipt.

## Read only

- The provided context pack and repair instructions
- The exact files listed by the rendered repair prompt
- If the listed files do not contain enough evidence, return `blocked_upstream`

## Write only

- `out/level_{level}/build/canonical/lessons/L{lesson}.json`

## Rules

- Repair the lesson unit, not the plan or cumulative state
- Do not run, inspect, or simulate validators
- Do not create repo-root scratch files or temp scripts
- Stop after one artifact write or one blocker receipt
- Return only a concise receipt plus the required WORKER_RECEIPT JSON block
```

## Rules

- The agent file is the contract. The rendered prompt is the task. The agent follows the rendered prompt; if they conflict, the rendered prompt wins and the agent reports the conflict in the receipt.
- Do not put implementation details in the agent body that belong in the renderer or skill
- Do not duplicate skill knowledge in the agent — use the `skills` frontmatter field
- Do not write agent files that are 1000 lines — the agent body should be 30-80 lines
- Every agent must be in the `AGENT_MANIFEST.json` (see `agent-manifest.md`)
