---
name: skill-process
description: Full implementation checklist for creating, modifying, or reviewing a skill. Reference when the user asks to implement or change a skill.
---

# Implementation Checklist

When user asks to create, modify, or review a skill, you MUST work through this checklist in order. Do not skip steps. Mark each item as done before proceeding.

## 1. Read & Decide

Before writing anything, read the relevant references and make decisions:

- [ ] **Read `references/principles.md`** — Confirm the 8 core principles apply to this skill
- [ ] **Read `references/frontmatter.md`** — Know the naming and description rules
- [ ] **Decide scope:** What is the use case?
  - Workflow / process → sequential or iterative pattern (read `references/patterns/`)
  - MCP integration → read `references/invocation.md` for tool-first vs problem-first
  - Domain expertise → domain-specific pattern (read `references/patterns/`)
  - Multi-service → multi-MCP or context-aware pattern (read `references/patterns/`)
- [ ] **Decide invocation mode:**
  - Auto-triggered → description must match user queries (read `references/invocation.md`)
  - Slash command → user explicitly invokes with `/skill-name`
  - User-invocable → user requests by name
  - Disable model invocation → never auto-trigger; only explicit invocation
- [ ] **Decide subagent needs:**
  - Does it delegate work to other agents? → read `references/subagents.md`
  - Does it need `context: fork` for isolation?
  - Does it preload skills into subagents?
  - Does it need `paths:` restrictions?
- [ ] **Decide arguments:**
  - Does the skill need user input? → read `references/arguments.md`
  - What `$variables` will be used?
- [ ] **Decide permissions:**
  - Which tools does it need? → read `references/permissions.md`
  - Should `allowed-tools` be restricted?
  - What are the side effects?
- [ ] **Decide distribution:**
  - Plugin, personal, project, or bundled? → read `references/distribution.md`
  - Where will the skill live?

## 2. Scaffold

Create the skeleton based on decisions:

- [ ] **Create folder** in kebab-case matching the skill name
- [ ] **Write `SKILL.md`** with frontmatter (name, description, optional arguments/allowed-tools)
- [ ] **Verify frontmatter:**
  - `name:` is kebab-case, max 64 chars, no reserved words, matches folder name
  - `name:` uses gerund form if possible: `processing-pdfs`, `analyzing-data`
  - `description:` is `[What it does]. Use when [triggers].` Under 1024 chars.
  - `description:` is in third person: "Processes Excel files" not "I can help you process Excel files"
  - No XML tags `< >` anywhere in frontmatter
  - No time-sensitive data (version numbers, percentages)
- [ ] **Create `references/` directory** if deep docs, examples, or schemas are needed
- [ ] **Create `scripts/` directory** if deterministic validation is needed

## 3. Write Content

Fill in the SKILL.md body and references:

- [ ] **Write core workflow in SKILL.md** — Keep under 100 lines
- [ ] **Apply principles:**
  - Every line prevents a specific mistake
  - Imperatives over prose
  - High-priority rules in first 40 lines
  - Negative rules included
  - No secrets anywhere
  - Don't duplicate linter, CI, or auto-memory
- [ ] **Move deep content to references:**
  - Detailed schemas → `references/<topic>.md`
  - Examples → `references/examples/<name>.md`
  - Troubleshooting → `references/troubleshooting.md`
  - Rationale → `references/principles.md` (already exists)
- [ ] **Add error handling and escape hatches** in SKILL.md
- [ ] **Add validation gates** if using sequential or iterative patterns
- [ ] **Provide utility scripts** for deterministic operations (see references/files-structure.md)
- [ ] **List dependencies** if scripts need packages (see references/files-structure.md)
- [ ] **Use forward slashes** in all file paths (see references/principles.md)
- [ ] **Provide a default approach** — one clear method, not a menu of options (see references/principles.md)

## 4. Validate Structure

- [ ] **Check file layout:** `SKILL.md`, `references/`, `scripts/` (no `README.md` inside skill folder)
- [ ] **Check references depth:** One level only (no `references/sub/dir/file.md`)
- [ ] **Check line counts:**
  - SKILL.md under 100 lines (ideally 60–80)
  - Global skill under 30 lines
  - Monorepo root skill under 80 lines
- [ ] **Check for secrets:** Search for API keys, tokens, passwords, internal URLs
- [ ] **Check for time-sensitive data:** Remove version numbers, percentages, dates

## 5. Test

- [ ] **Create evaluations first:** Build 3 scenarios that test real gaps before shipping (see references/testing.md)
- [ ] **Triggering test:** Verify skill loads on 3–5 relevant queries
- [ ] **Negative trigger test:** Verify skill does NOT load on 3–5 unrelated queries
- [ ] **Functional test:** Walk through each step, verify expected output
- [ ] **Edge case test:** Missing input, MCP failure, empty result, permission denied
- [ ] **Paraphrase test:** Test variations of trigger phrases
- [ ] **Model test:** Test with all models you plan to use (Haiku, Sonnet, Opus) (see references/testing.md)

## 6. Review & Deliver

Final check before presenting to user:

- [ ] Name is kebab-case, no reserved words, matches folder name
- [ ] Description under 1024 chars with "Use when..." triggers
- [ ] No XML tags in frontmatter
- [ ] No README.md inside skill folder
- [ ] No secrets anywhere
- [ ] Under line target for scope
- [ ] Every line prevents a specific mistake
- [ ] Negative rules included
- [ ] References one level deep
- [ ] No time-sensitive data
- [ ] Permissions are restricted to minimum necessary
- [ ] Error handling covers common failures
- [ ] Subagent configuration is correct (if applicable)
- [ ] Arguments are declared and used correctly (if applicable)
- [ ] Distribution method is documented (if applicable)
- [ ] **MCP tool references use fully qualified names** if applicable: `ServerName:tool_name` (see references/files-structure.md)
- [ ] **Scripts handle errors explicitly** — solve, do not punt (see references/files-structure.md)
- [ ] **No "voodoo constants"** — all values are justified and documented (see references/files-structure.md)
