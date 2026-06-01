# redpanda77 skills

Agent skills for Claude Code and compatible agents. The flagship skill is **mission-control** — a compiler operating system for reliable, repeatable agent execution. Also includes knowledge vaults (tolaria-wiki), documentation workflows (grill-me, grill-with-docs), planning workflows (writing-plans), handoffs, skill authoring, and CLAUDE.md / AGENTS.md writing.

## Original Skills

These skills were built specifically for this repository and are not derived from other sources:

### mission-control (Flagship)

Configure Claude Code as a compiler operating system for reliable, repeatable agent execution. Compiles human intent into structured output through intermediate representations (source, graph, plans, canonical, validation, judges, output, audit), where each tier is validated and judged before moving to the next stage.

**Features:**
- Router-driven execution — the router decides what to do next, not the agent
- Deterministic scripts — scripts are mechanical only, never qualitative
- Bounded agent context — every judge and worker gets a bounded context pack
- Hash-based freshness — `content_hash != receipt_hash` means stale
- Incremental compilation — changing one artifact only re-validates affected downstream targets
- Principle-based evaluation — judges score against 5-10 named principles
- Multi-tier validation — every tier has validators and judges
- Repair system — repair planner, doctor, and escape protocol for handling failures
- Maintenance system — legacy cleanup, change management, and diagnostic resilience

### tolaria-wiki

Set up, author in, and maintain a Tolaria knowledge vault (folder of Markdown + YAML frontmatter forming a personal knowledge graph). Used for creating vault notes, processing raw notes, importing meeting recordings, and generating summaries. Tolaria is a folder-of-markdown vault format from [github.com/refactoringhq/tolaria](https://github.com/refactoringhq/tolaria).

### writing-plans

Write, structure, or audit a project improvement plan. Covers plan naming (P{NN}, K{NN}), directory layout, goal.md structure, knockout files, progress tracking, and the 7-step execution methodology (baseline, classify, map, change, verify, ledger, repeat).

**Features:**
- Progressive disclosure — plan index first, then goal, then knockouts, then methodology
- Goal.md as execution contract — defines scope, boundaries, mandatory steps, and completion criteria
- Knockouts (KOs) as independent execution slices — each KO can be validated and merged separately
- 7-step protocol — baseline, classify, map, change, verify, ledger, repeat
- Deviation tracking — blockers go in DEVIATIONS.md, not in memory
- Plan type templates — reorganization, theming, feature, and audit plans

## Attribution

This repository also includes skills derived from other sources:

### Based on [mattpocock/skills](https://github.com/mattpocock/skills)
The following skills are derived from the original `mattpocock/skills` repository with modifications and enhancements:

- **grill-me** — Interview the user before starting a feature or task using interactive multiple-choice questions. Surfaces the decisions that will meaningfully change what gets built, not what can already be inferred from the codebase.
- **grill-with-docs** — Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Stress-tests a plan against the project's language and documented decisions.
- **handoff** — Compact the current conversation into a handoff document so a fresh agent can continue this work without re-reading the full conversation. Used when context is large, switching tasks or branches, preparing for a new session, or when the user says "handoff", "save context", "resume later", or "new session".

### Based on [Anthropic Documentation](https://docs.anthropic.com/)
The following skills are derived from official Anthropic documentation and best practices for Claude Code:

- **writing-claude-md** — Write, audit, or compress a CLAUDE.md / AGENTS.md instruction file for a coding agent. Covers what to put in CLAUDE.md, why it might be ignored, and how to make Claude Code follow your conventions.
- **write-a-skill** — Create agent skills with proper structure, progressive disclosure, and bundled resources. Covers the skill format, frontmatter design, supporting files, and progressive disclosure principles.
- **claude-code-guide** — Router and condensed guide to Claude Code configuration and extension points. Tracks official documentation for memory, permission modes, settings, CLI flags, slash commands, hooks, subagents, and agent teams.
- **claude-code-hooks** — Design, review, implement, and debug Claude Code hooks. Covers settings hooks, plugin hooks, skill-scoped hooks, agent-scoped hooks, hook lifecycle, events, matchers, security, and async hooks.
- **claude-code-agents** — Design, create, review, invoke, or debug Claude Code subagents, agent teams, and the agent system architecture. Covers built-in agents, custom subagents, agent teams, file placement, frontmatter design, and the execution decision tree.
- **creating-codex-environments** — Scaffolds local Codex configuration, custom agents, hooks, and skills. Used when setting up Codex for a repo. Do not use for Claude Code or Claude Desktop setup.

## Install

Install all skills (project scope is detected automatically; use `-g` for global):

```bash
npx skills add redpanda77/skills
```

List available skills without installing:

```bash
npx skills add redpanda77/skills --list
```

Install one skill:

```bash
npx skills add redpanda77/skills --skill mission-control
```

Install globally:

```bash
npx skills add redpanda77/skills --skill mission-control -g
```

If `npx` on your Node version prefers `npm exec`, equivalent invocations use `npm exec --yes -- skills …` with the same arguments after `skills`.

## Layout

Skills live under `skills/<skill-name>/` with a `SKILL.md` (YAML frontmatter plus body). Optional folders: `references/`, `scripts/`, `assets/`.

For Claude Code, the primary location is `.agents/skills/<skill-name>/`.

## Skill Descriptions

| Skill | Source | What it does |
|---|---|---|
| `mission-control` | Original | Compiler operating system for reliable, repeatable agent execution with tiered validation and judging |
| `tolaria-wiki` | Original | Set up and maintain a Tolaria knowledge vault (folder-of-markdown personal knowledge graph) |
| `grill-me` | mattpocock | Interview the user before starting a feature using interactive multiple-choice questions |
| `grill-with-docs` | mattpocock | Challenge your plan against the domain model and update documentation inline |
| `handoff` | mattpocock | Compact the current conversation into a handoff document for a fresh agent |
| `writing-claude-md` | Anthropic | Write, audit, or compress a CLAUDE.md / AGENTS.md instruction file for a coding agent |
| `write-a-skill` | Anthropic | Create agent skills with proper structure, progressive disclosure, and bundled resources |
| `claude-code-guide` | Anthropic | Guide to Claude Code configuration: memory, permissions, settings, CLI flags, hooks, subagents |
| `claude-code-hooks` | Anthropic | Design, review, implement, and debug Claude Code hooks (settings, plugin, skill-scoped, agent-scoped) |
| `claude-code-agents` | Anthropic | Design, create, review, invoke, or debug Claude Code subagents, agent teams, and agent system architecture |
| `creating-codex-environments` | Anthropic | Scaffold local Codex configuration: custom agents, hooks, and skills |
| `writing-plans` | Original | Write, structure, or audit a project improvement plan with knockout files and 7-step methodology |

## Test before publishing

From outside this repo (or with a path to it):

```bash
npx skills add ./skills-repo --list
```

After pushing to GitHub:

```bash
npx skills add redpanda77/skills --list
npx skills add redpanda77/skills --skill mission-control -y
```

Public listing on [skills.sh](https://skills.sh) is driven by install telemetry when users run `npx skills add <owner/repo>`; there is no separate registry submission for the leaderboard.

## License

MIT — see [LICENSE](LICENSE).
