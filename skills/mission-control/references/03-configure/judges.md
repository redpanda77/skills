# Judges Setup

How to create judge subagents.

## What judges are

Judges evaluate qualitative quality. They are the sole authority for:
- Content quality, naturalness, semantic fit
- Intent satisfaction
- Architecture consistency beyond lint
- Security beyond static analysis

## Judge vs validator

**Rule:** Could a non-expert with a regex pass this check?
- **Yes** → Validator script.
- **No** → Judge subagent.

## Types

| Type | Evaluates | Principles |
|---|---|---|
| Single judge | All dimensions | 5-10 principles |
| Multi-judge | One domain each | 5-10 principles per judge |

## Rules

- Judge evaluates principles independently (0.0–1.0).
- Task passes only when every principle scores >= threshold.
- `must_fix` items are tagged with the violated principle.
- No Python script pre-packages context for the judge.
- Judge output is authoritative. No script rewrites it.
- The worker spawns the judge subagent via the `Agent` tool.
- The hook does NOT spawn the judge. It checks for the judge's verdict file.

## See also

- `references/07-agents/README.md` — agent design overview
- `references/07-agents/agent-design.md` — frontmatter schema, categories, read/write scope
- `references/07-agents/worker-class-contracts.md` — scoped evidence language for each worker class
- `references/07-agents/agent-invocation.md` — how to invoke judge subagents via the `Agent` tool
- `references/07-agents/agent-manifest.md` — the `AGENT_MANIFEST.json` registry
