# Project-local skills as the deep-reference layer

CLAUDE.md is the **always-loaded** layer. It must stay short (60–120 lines). When a project needs deep reference content — type schemas, framework conventions, domain-specific workflows, filing rules — the right home is a **project-local skill** at `.claude/skills/<name>/`, not CLAUDE.md.

This document covers **whether** to extract and **what** to extract. It does **not** cover how to author a skill — for that, **delegate** to one of the dedicated skill-authoring skills (see "How to actually create the skill" below).

## The pattern

```
project/
├── CLAUDE.md                         # behavioral contract + skill registry
├── AGENTS.md                         # tool-agnostic mechanics
└── .claude/
    └── skills/
        ├── <domain-skill-1>/         # on-demand deep reference
        └── <domain-skill-2>/
```

CLAUDE.md:
- Hard rules (always-on)
- Workflow preferences (always-on)
- Out-of-scope (always-on)
- **A "Project-local skills" section** that lists local skills by name with one-line triggers
- `@AGENTS.md` import

Each project-local skill owns one domain. CLAUDE.md doesn't repeat what's inside it.

## When to extract — the 2-of-N test

Extract content out of CLAUDE.md into a new `.claude/skills/<name>/` skill if **two or more** are true:

- Content is reference material (tables, schemas, lifecycles) — not behavioral rules.
- Content is only relevant for a subset of tasks (filing notes, writing migrations, generating reports).
- Content is over ~30 lines on its own.
- Multiple existing rules in CLAUDE.md duplicate parts of it.
- Content would benefit from progressive disclosure inside it (its own `references/`).
- Content has a clear trigger surface (specific verbs / file types / folders).

If only one is true → keep in CLAUDE.md (or a single `agent_docs/X.md` pointer file).
If none are true → the content probably isn't reference, it's a rule. Stays in CLAUDE.md.

## What stays in CLAUDE.md after extraction

- **A "Project-local skills" section** listing the new skill by name with its trigger phrase.
- Any **hard rules** the skill cannot enforce on its own (e.g., "Never modify `_archive/`").
- A pointer line at the bottom of the section: "If a task touches one of these domains and Claude isn't using the skill, run `/memory` to verify it loaded."

## CLAUDE.md "Project-local skills" section template

```markdown
## Project-local skills

These skills activate automatically based on your request. They live in `.claude/skills/`.

- **<skill-name>** — Use when <trigger>. Covers <one-line scope>.
- **<skill-name>** — Use when <trigger>. Covers <one-line scope>.

If a task touches one of these domains and Claude isn't using the skill, run `/memory` to verify it's loaded.
```

## Naming a project-local skill

- kebab-case
- Verb-led where possible (`wiki-author`, `db-migrate`, `report-generate`) or noun-scoped (`careem-pm`, `auth-conventions`)
- Match the trigger surface — the name should suggest *when* it fires

## How to actually create the skill — DELEGATE

**Do not write the skill inline from this skill.** Skill authoring is a separate domain with its own progressive disclosure. Hand off to one of these (in preference order):

| Skill | Use when |
|-------|----------|
| `write-a-skill` | Default first choice — most complete skill-authoring guide |
| `skill-creator` | Alternative; from anthropic-skills |
| `plugin-dev:skill-development` | If the skill is part of a plugin |
| `find-skills` | If unsure which skill-authoring skill applies |

**Read these only when actually creating an extracted skill, not during audit or compression.** During audit/compression, the only output is *"this content should become a skill called `<name>`"* — the authoring happens in a separate step.

### Handoff procedure

When the extraction is approved (user confirms or you're in a flow that proceeds automatically):

1. State the handoff: "I'll use `write-a-skill` to create `.claude/skills/<name>/`."
2. Invoke the skill with:
   - The proposed skill name (kebab-case).
   - A trigger-rich description draft based on the extraction analysis.
   - The cluster of content being extracted (paste verbatim).
   - The target location: `<project-root>/.claude/skills/<name>/`.
3. After the skill returns, update CLAUDE.md's "Project-local skills" section to list the new skill.
4. Verify with `/memory` in a fresh session.

The skill-authoring skill handles `SKILL.md` structure, progressive disclosure into `references/`, frontmatter format, anti-patterns, and tests. Don't duplicate that knowledge here.

## Anti-patterns (extraction-specific)

These are anti-patterns *of the extraction decision*. Anti-patterns of skill *authoring* live in the skill-authoring skills, not here.

- **Skill that duplicates CLAUDE.md.** If a skill's `SKILL.md` repeats hard rules already in CLAUDE.md — delete from one. CLAUDE.md is always-on; rules go there. Skills carry the *how*, not the *what's forbidden*.
- **Skill with no trigger.** If you can't write a one-line `Use when …` description, the content probably isn't a skill — it's documentation. Make it a plain `agent_docs/X.md` instead and reference with progressive disclosure.
- **Hard rules buried in a skill.** Rules that must apply to *every* session (security, confidentiality, never-delete) belong in CLAUDE.md, not a skill — skills only fire when triggered.
- **Skill that duplicates an existing skill.** Before creating, check the registered skills list. If there's already a skill that covers this trigger surface, extend or reference it instead of creating a new one.

## Where to put what — placement table

| Content | Home | Why |
|---------|------|-----|
| "Never commit secrets" | CLAUDE.md hard rules | Always-on, security |
| "Use `[[wikilinks]]` not markdown links" | CLAUDE.md hard rules | Always-on, universal |
| Frontmatter schema per note type | `.claude/skills/<author-skill>/references/types.md` | Reference, triggers on filing |
| Raw → archive workflow | `.claude/skills/<maintain-skill>/SKILL.md` | Procedure, triggers on maintenance verb |
| Vault file format (YAML, H1 conventions) | `AGENTS.md` | Tool-agnostic, applies to any AI tool |
| Owner / role / focus areas | CLAUDE.md identity (3 lines max) | Always-on context, short |
| Team roster | `people/_roster.md` (regular note) | Data, stale-risk, queryable on demand |
| Folder ASCII tree | Delete — Claude can `ls` | Discoverable |
| How to write a `SKILL.md` | `write-a-skill` / `skill-creator` (existing skills) | Not our domain — delegate |
