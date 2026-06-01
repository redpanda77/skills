# Agent Invocation

How the `Agent` tool works, the handoff protocol, and the parent/worker boundary.

## The Agent tool

Use the `Agent` tool for every subagent invocation. A generic prompt that says "you are X" is not the same thing: it does not load the custom system prompt, tool restrictions, or agent-scoped contract.

```json
{
  "subagent_type": "example-worker",
  "description": "Short routed task summary",
  "prompt": "Execute the routed task for level N. Step 1: read exactly ... Step 2: write exactly ... Step 3: return WORKER_RECEIPT only."
}
```

### Required fields

| Field | Purpose | Example |
|-------|---------|---------|
| `subagent_type` | Exact agent name from `AGENT_MANIFEST.json` | `lesson-repair-worker` |
| `description` | Short UI summary only (not the contract) | `Repair lesson L005` |
| `prompt` | The worker's bounded task contract | Self-contained handoff |

### Rules

- `subagent_type` must match the exact `name` in `AGENT_MANIFEST.json`
- `description` is a UI label, not the work contract
- `prompt` is the actual task contract — it must be self-contained
- The prompt must name: level (if applicable), target, read scope, write scope, output schema, stop condition
- The prompt must not ask the worker to inspect router state, hooks, authorization sidecars, agent files, or source code

## Prompt pattern

A good handoff prompt is self-contained and bounded:

```text
Execute the routed task for level {level}.

Step 1: Read exactly:
- {context_pack_path}
- {target_artifact_path} (only if needed for overwrite mechanics)

Step 2: Write exactly:
- {output_path}

Step 3: Return WORKER_RECEIPT JSON with:
  status, agent, artifact_path, summary, assumptions

Stop after one artifact write or one blocker receipt.
Do not inspect router state, hooks, or authorization sidecars.
```

### What the prompt must contain

- **Level/target** — the scope identifier
- **Read scope** — exact files the worker must read
- **Write scope** — exact output path
- **Output schema** — what the worker must produce (e.g., `WORKER_RECEIPT`)
- **Stop condition** — when to stop (one write, one blocker receipt)
- **Hook awareness** — "The rendered prompt's listed files are the authorized files. If a listed read is blocked, return `blocked_upstream` naming authorization/renderer scope."

### What the prompt must NOT contain

- Requests to inspect router state, hooks, or authorization sidecars
- Requests to browse raw artifacts, source code, or plans
- Requests to run validators or simulate validator logic
- Permission to create scratch files or one-off scripts

## The handoff protocol

The chain is:

```
1. Router produces a card (status, run, requires_worker, target, then)
2. Parent reads the card
3. Parent invokes the exact named subagent with the exact handoff prompt
4. Parent does NOT pre-read worker prompts, context packs, or target artifacts
5. Worker reads its own context packs and writes its target
6. Worker returns WORKER_RECEIPT JSON
7. Parent reads the receipt (not the artifact) to verify completion
8. Parent runs the `then` router check if present
```

### Parent boundaries

The parent orchestrator must:

- Execute the returned `run` field exactly once
- For `requires_worker`, invoke the exact named subagent with the exact routed handoff
- For deterministic `ready` actions, run the routed command, then run the `then` router check
- Not read worker prompts, context packs, authorization sidecars, raw artifacts, or target outputs to prepare delegation
- Not inspect the artifact to verify the worker — it reads the receipt
- Not run validators during the worker's execution — validators run after the worker returns

### Worker boundaries

The worker must:

- Read exactly the files listed by the rendered repair prompt
- Not browse raw artifacts, plans, diagnostics, or sibling files unless the prompt lists them
- Not inspect router state, hooks, or authorization sidecars
- Not create scratch files or one-off scripts
- Return `blocked_upstream` if listed evidence is insufficient
- Return `WORKER_RECEIPT` JSON as the only output besides the artifact

## Operator role

The top-level agent is the operator, not a general coding agent. During a skill session:

1. Treat the router as workflow authority
2. Execute the returned `run` field exactly once
3. For `requires_worker`, invoke the exact named subagent with the exact routed handoff
4. The `then` field is the official continuation checkpoint
5. Judge JSON is first-class state. Python scripts are not qualitative judges.
6. Generated artifacts are evidence and protected state, not normal repair targets
7. Agents do not update router state. State is derived by official refresh scripts

## Hard stops

- Do not manually patch protected generated artifacts: plans, canonical units, ledgers, judge JSON, runtime state, or export files
- Do not create repo-root scratch scripts or one-off repair scripts
- Do not rerun the same failing validator, worker, or prompt render with unchanged inputs
- Do not paste full artifacts, context packs, or validator logs unless explicitly requested
- Do not mutate a closed scope unless the user asks for the reopen flow
- Do not edit hooks or settings during normal execution; this requires Escape Protocol

## Hook blocks

A hook block means the attempted tool call is off-protocol or underspecified. Do not work around it with `cat`, inline Python, direct writes, broader reads, settings relaxation, hook edits, or manual artifact edits. Stop, read the hook message, and fix the route, rendered prompt, context pack, or subagent handoff.

## Context rule

Workers use official rendered prompts and bounded context packs. Context-pack `source_paths` are provenance for renderers, not worker read lists. If required context is missing, fix the renderer or prompt; do not browse raw generated artifacts to compensate.

## Headless invocation

When a non-Claude-Code operator must run a real judge, render the official prompt/context first and invoke the matching agent explicitly:

```bash
claude -p "$(cat out/traces/worker_prompts/judge_prompt.md)" \
  --agent judge-worker-name \
  --output-format json
```

Do not use `--bare` unless the agent definition is passed inline with `--agents`; bare mode does not auto-discover `.claude/agents/`.

## Rules

- The parent is the operator, not the worker
- The parent does not pre-read worker context packs — the worker reads them
- The parent does not run validators — the parent runs the router, which decides whether to validate
- The parent does not construct delegation by reading worker prompts — it uses the router card
- The `then` field is the official continuation checkpoint
- A generic agent with a prompt is not a custom subagent — always use `subagent_type`
- If an agent is not in `AGENT_MANIFEST.json`, it is not part of the runtime contract
