# Agents

The model execution layer: workers generate, judges evaluate.

## Two Distinct Agent Types

| Type | Role | Scope | Tools |
|------|------|-------|-------|
| **Worker** | Generates artifacts | One bounded unit | Read, Write, Edit |
| **Judge** | Evaluates quality | One concern per judge | Read |

Never collapse them. A worker that also judges its own output is unbounded. A judge that also writes is not independent.

## Workers

### Purpose

Generate one bounded artifact at a time. The rendered prompt and context pack are the worker's contract.

### Types

- **Proposal workers** — write one plan or one canonical artifact
- **Repair workers** — repair one routed target
- **Control repair workers** — patch routing/control behavior only when Escape Protocol is active

### Rules

- Read only the rendered prompt and files listed in it
- Do not browse raw generated artifacts for context
- If missing context, return `blocked_upstream` with the smallest upstream authority
- Generate one target at a time, not the whole pipeline
- Write only what the prompt asks for; respect negative contracts
- If the same failure class repeats twice, stop retrying the same worker. Treat it as an upstream graph, plan, assembler, validator, or source-governance issue

### Worker Authorization Sidecar

The prompt renderer should write a deterministic delegation metadata file (prompt path, prompt hash, allowed reads, exact artifact write path) that hooks may use to enforce worker boundaries. This is a separate concept from the delegation ledger.

### Parent Context Budget

The top-level orchestrator should retain only a compact set (router status, repair route card, current task ID, produced artifact paths, first concise validator/judge failure, latest committed state path, one concise worker receipt) and explicitly discard full artifacts, full graph JSON, full judge JSON, repeated validator logs, etc.

### Invocation Integrity

A worker is active only when the harness invokes the exact custom subagent. A generic agent with a prompt that says "you are X" is not the same thing: it does not load the custom system prompt, tool restrictions, or agent-scoped contract.

## Judges

### Purpose

Evaluate qualitative quality against principles. The judge is the sole authority for content quality, naturalness, semantic fit, and intent satisfaction.

### Types

- **Single judge** — evaluates all dimensions (5-10 principles)
- **Multi-judge** — one domain per judge when >10 principles

### Rules

- Evaluate each principle independently (0.0–1.0)
- Task passes only when every principle >= threshold
- `must_fix` items are tagged with the violated principle
- Judge output is authoritative; no script rewrites it
- The worker spawns the judge subagent via the `Agent` tool
- The hook does NOT spawn the judge; it checks for the judge's verdict file

### Verdict Format

```json
{
  "task_id": "T002",
  "verdict": "pass",
  "confidence": 0.82,
  "principle_scores": {
    "communicative_purpose_first": 0.91,
    "evidence_before_explanation": 0.75
  },
  "threshold": 0.70,
  "must_fix": [],
  "should_fix": [],
  "evidence": [],
  "concerns": []
}
```

## Failure Mode

If agents are broken:
- Workers drift into content generation during planning phases
- Judges collapse multiple concerns into vague feedback
- Scope creep: one agent tries to solve the whole project
- Agents browse raw artifacts instead of using context packs
- Generic agent invocation loses custom system prompts and tool restrictions

## Failure-to-Repair-Layer Mapping

When a worker or judge fails, route the repair to the correct layer. Do not retry the same worker with the same inputs.

| Failure | Repair Layer | Why |
|---------|-------------|-----|
| Bad canonical phrasing, examples, dialogue | Canonical worker | Content is the worker's domain |
| Bad grouping or sequence | Plan worker | Grouping is the plan's domain |
| Bad judgment (score too low) | Rerun or repair the specific judge | Judge is the sole quality authority |
| Worker cannot see needed context | Context-pack renderer or prompt | The pack is missing required context |
| Worker repeats the same failure | Router or graph (upstream) | Same input → same output. The problem is upstream |
| Judge contradicts validator | Judge wins, validator repair | Qualitative > deterministic, but validator must be fixed |
| Validator false positive | Fix validator | Do not patch the artifact to pass a broken validator |
| Oversized context pack | Fix renderer | The contract is the budget, not the trimming logic |
| Prompt/pack mismatch | Fix renderer or router | The pack shape must match what the prompt describes |
| Hook blocks valid work | Fix route, not hook | The hook is the constraint; the route is the problem |
| Control system failure | Escape Protocol | Router, hooks, validators need repair without weakening gates |

## Repair Authority

- Bad canonical phrasing, examples, dialogue → canonical repair
- Bad grouping or sequence → plan repair
- Bad judgment → rerun or repair the specific judge only through the router
- Worker cannot see needed context → repair the context-pack renderer or prompt
- Same failure repeats → route to upstream graph, plan, or control layer
- Control system failure → Escape Protocol

## See also

- `references/07-agents/README.md` — agent design overview
- `references/07-agents/agent-design.md` — frontmatter schema, categories, read/write scope
- `references/07-agents/worker-class-contracts.md` — scoped evidence language for each worker class
- `references/07-agents/skill-activation-and-hooks.md` — how skills activate hooks
- `references/07-agents/agent-invocation.md` — how to invoke agents via the `Agent` tool
- `references/07-agents/agent-manifest.md` — the `AGENT_MANIFEST.json` registry
