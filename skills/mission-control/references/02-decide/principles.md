# Core Principles

## 1. The Router Decides the Workflow

The router is the workflow authority. The model runs the router and executes its command.

## 2. Scripts = Deterministic Only

Scripts verify: tests pass, files exist, schema valid, no tampering. They do NOT decide quality.

## 3. Judge = Subagent Only

The judge is a real Claude Code subagent (`.md` file in `.claude/agents/`). It is NOT a script.

## 4. State Hierarchy: Judge JSON → Deterministic Evidence → Router

Judge JSON is authoritative. A passed judge overrides a failed precheck. A failed judge overrides a passed precheck.

## 5. Judges Use Bounded Context Packs

Judges read bounded, typed context packs — not raw artifact dumps. The context pack is the evidence surface. The judge does not browse the repository for context.

## 6. Judge Output Is Authoritative

No script rewrites, normalizes, or migrates judge artifacts.

## 7. Judge Contracts Must Be Complete

Every judge writes JSON with `verdict`, `confidence`, `principle_scores`, `threshold`, `must_fix`, `should_fix`, `evidence`, `concerns`.

## 8. No Qualitative Heuristics in Scripts

There is no such thing as a "lightweight heuristic" that stays in scripts. A heuristic belongs to the judge.

## 9. Always Use Skills for Setup

- `write-a-skill` — for creating skills
- `claude-code-hooks` — for designing hooks
- `writing-claude-md` — for producing `AGENTS.md` and `CLAUDE.md`

## 10. Subagent Frontmatter Is Critical

Every `.md` file in `.claude/agents/` needs YAML frontmatter with `name`, `description`, and optional `tools`, `skills`, etc.

## 11. Commands Are Thin Shims

A command loads a skill; the skill owns all logic. Never duplicate skill logic in a command.

## 12. Always Create a System Skill

Every setup must produce a system skill in `.claude/skills/`. Hard gate — do not skip.

## 13. Stop Hook Blocks Premature Exit

Claude cannot stop until `done-check.sh` passes or a real blocker exists.

## 14. Subagents Are Bounded Workers

Every subagent declares its read surfaces, write surfaces, forbidden write surfaces, and return format.

## 15. AGENTS.md Is a Map, Not a Manual

Keep it under 120 lines. Point to deeper docs. Do not write a 2000-line encyclopedia.

## 16. Nested AGENTS.md for Divergent Conventions

Create nested files where conventions diverge. Score each area 0.0–1.0. Where score >= 0.70, create a nested file. 30–60 lines. Three sections: Conventions, Commands, Hard Rules.

## 17. Phased Implementation — MVP First

Build in phases, not all at once. Each phase is user-approved before proceeding.

## 18. User Alignment Before Implementation

User must approve what will be created, what rules will be enforced, and what "good" means.

## 19. Setup-Time vs Runtime Instructions

- **Setup time** — how to configure the harness (mission-control skill)
- **Runtime** — how to do the actual work (AGENTS.md, CLAUDE.md)

Do not conflate them.

## 20. Skills Preloaded Through Subagent Frontmatter

Subagents load skills via `skills:` field in YAML frontmatter. This is the primary way to give subagents durable domain knowledge.

## 21. Context Efficiency

Judge JSON must be efficient: omit absence, avoid duplicate shapes, prefer counts over lists, drill down by pointer.

## 22. First Principles Document

Create `documentation/first-principles.md` as the durable contract. All control files must preserve it.

## 23. Subagent Read Contracts Are Reusable

Place shared read/skip lists and subagent contracts in `.claude/agent-contracts/`. Subagents load their contract before reading anything else. This is the agent contract, not the context pack.

## 24. The Model Reads Bounded Packs, Not Raw Artifacts

The model reads the rendered prompt, the typed context pack, and only the files explicitly named in the prompt. It does not browse raw artifacts or use the repository as a knowledge base. Scripts produce compact typed summaries; the model reads the bounded evidence surface.

## 25. Invoke Skills, Never Write Manually

- Invoke `write-a-skill` for skill creation
- Invoke `claude-code-hooks` for hook design
- Invoke `writing-claude-md` for `AGENTS.md` and `CLAUDE.md`
