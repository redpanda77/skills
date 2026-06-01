# 07 — Agents

How to design, implement, and invoke agents in a harnessed pipeline.

## Why this matters

An agent is only as good as its contract. Without a clear frontmatter, bounded read/write scope, and a canonical manifest, agents drift — they browse raw artifacts, write off-route files, and ignore context packs. This section documents the concrete patterns that prevent that drift.

## What you will learn

- How to write agent frontmatter that the harness can parse and route
- How to define read/write surfaces in the agent body, not the frontmatter
- How to classify agents by worker class (judge, artifact, repair, planning, escape, audit)
- How to align the agent contract with the renderer, hook, router, and skill
- How to invoke agents via the `Agent` tool with the correct `subagent_type`
- How skills activate hooks and why hooks are only active when the skill is loaded
- How to maintain an `AGENT_MANIFEST.json` as the canonical registry

## The files

- `README.md` — this file (overview)
- `agent-design.md` — frontmatter schema, categories, read/write scope, WORKER_RECEIPT
- `worker-class-contracts.md` — scoped evidence language for each worker class
- `skill-activation-and-hooks.md` — how skills activate hooks, hook scoping, curriculum example
- `agent-invocation.md` — how the `Agent` tool works, handoff protocol, parent boundaries
- `agent-manifest.md` — the `AGENT_MANIFEST.json` pattern, canonical registry

## The core invariant

```text
Scope must be explicit, typed, and worker-class appropriate.
```

## The cross-surface invariant

```text
The files a worker is told to read, the files hooks authorize,
and the files the agent base prompt expects must be the same files.
```

Any mismatch between those surfaces is a pipeline bug.

## When to read this

Read this section after you understand the system architecture (`00-introduction/system-architecture/`) and before you write your first agent. It is the bridge between "what agents are" and "how to build them correctly."
