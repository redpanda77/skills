# redpanda77 skills

Agent skills for Claude Code and compatible agents. The flagship skill is **mission-control** — a compiler operating system for reliable, repeatable agent execution. Also includes knowledge vaults (tolaria-wiki), interviewing and planning workflows (grill), planning workflows (writing-plans), handoffs, skill authoring, skill repository management, and CLAUDE.md / AGENTS.md writing.

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

- **grill** — Interview and stress-test the user before building. Two modes: pre-build interview (surfaces scope decisions via interactive questions) and plan stress-test (challenges a plan against the domain model, sharpens terminology, and updates CONTEXT.md/ADRs inline).
- **handoff** — Compact the current conversation into a handoff document so a fresh agent can continue this work without re-reading the full conversation. Used when context is large, switching tasks or branches, preparing for a new session, or when the user says "handoff", "save context", "resume later", or "new session".

### Based on [cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills)
The following skill is derived from the `cc-thinking-skills` repository by T.J. Boudreaux, which collects 39 structured thinking methodologies and mental models. These were consolidated into a single unified skill with a routing layer and validation framework:

- **applying-thinking-frameworks** — Apply structured thinking methodologies (first principles, systems thinking, 5 whys, etc.) to solve problems, make decisions, and analyze systems. Routes to the right mental model based on domain and problem type. Integrates grilling and document exploration for clarifying questions before framework application.

### Based on [Anthropic Documentation](https://docs.anthropic.com/)
The following skills are derived from official Anthropic documentation and best practices for Claude Code:

- **writing-claude-md** — Write, audit, or compress a CLAUDE.md / AGENTS.md instruction file for a coding agent. Covers what to put in CLAUDE.md, why it might be ignored, and how to make Claude Code follow your conventions.
- **write-a-skill** — Create agent skills with proper structure, progressive disclosure, and bundled resources. Covers the skill format, frontmatter design, supporting files, and progressive disclosure principles.
- **claude-code-guide** — Unified router and guide to Claude Code (CLI, Agent SDK, API). Routes to product features (memory, permissions, settings, CLI), custom agents (subagents, teams, frontmatter, patterns), and hooks (events, matchers, automation, security).
- **creating-codex-environments** — Scaffolds local Codex configuration, custom agents, hooks, and skills. Used when setting up Codex for a repo. Do not use for Claude Code or Claude Desktop setup.
- **skill-repo-manager** — Manage a skill repository using the `npx skills` CLI. Covers installing, listing, updating, removing, and publishing skills. Includes the skill format specification, directory structure, and publishing best practices.

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
| `grill` | mattpocock | Interview and stress-test the user before building. Pre-build interview + plan stress-test modes |
| `handoff` | mattpocock | Compact the current conversation into a handoff document for a fresh agent |
| `writing-claude-md` | Anthropic | Write, audit, or compress a CLAUDE.md / AGENTS.md instruction file for a coding agent |
| `write-a-skill` | Anthropic | Create agent skills with proper structure, progressive disclosure, and bundled resources |
| `claude-code-guide` | Anthropic | Unified router for Claude Code (CLI, Agent SDK, API). Covers product features, custom agents, and hooks |
| `creating-codex-environments` | Anthropic | Scaffold local Codex configuration: custom agents, hooks, and skills |
| `applying-thinking-frameworks` | cc-thinking-skills | Apply structured thinking methodologies (first principles, systems thinking, 5 whys, etc.) to solve problems and make decisions. Routes to the right mental model based on domain and problem type |
| `writing-plans` | Original | Write, structure, or audit a project improvement plan with knockout files and 7-step methodology |
| `skill-repo-manager` | Original | Manage a skill repository using the `npx skills` CLI. Covers installing, listing, updating, and publishing skills |

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
