# Mission Control Master Checklist

The complete checklist for setting up a Mission Control harness.

Follow this in order. Do not skip steps. Do not start Phase N until Phase N-1 is complete.

---

## Phase 0: Self-Setup (Read this skill)

- [ ] Read `SKILL.md` — understand the 5-phase workflow
- [ ] Read `references/00-introduction/README.md` — what is this and why you need it
- [ ] Read `references/00-introduction/philosophy.md` — the harness mindset
- [ ] Read `references/00-introduction/terminology.md` — key terms
- [ ] Read `references/CHECKLIST.md` — this file (master checklist)

---

## Phase 1: Discover (Understand the project)

- [ ] Read `references/01-discover/README.md`
- [ ] Read `references/01-discover/folder-structure.md` — what the harnessed project looks like
- [ ] Audit current project: what exists, what's missing, what's broken
- [ ] Pick tier: Minimal (<30min) / Standard (30m-2h) / Strict (2h+)
- [ ] Pick layout: Inline (files in repo) / External (agent-control/ outside)
- [ ] Record: `PROJECT_TYPE`, `TIER`, `LAYOUT`

---

## Phase 2: Decide (Choose the harness design)

- [ ] Read `references/02-decide/README.md`
- [ ] Read `references/02-decide/principles.md` — 25 non-negotiable rules
- [ ] Read `references/02-decide/setup-router.md` — pick workflow type
- [ ] Read `references/02-decide/judge-vs-validation.md` — what goes to judge vs validators
- [ ] Read `references/02-decide/judge-principles.md` — how to design principles
- [ ] Read `references/02-decide/implementation-plan.md` — the 6-phase implementation plan
- [ ] Decide: judge needed? hook level? nested files? principle count?
- [ ] Record: `JUDGE_NEEDED`, `HOOK_LEVEL`, `PRINCIPLE_COUNT`, `NESTED_FILES_NEEDED`

---

## Phase 3: Configure (Build the harness)

### 3.1 Intent
- [ ] Read `references/03-configure/agents.md`
- [ ] Read `references/03-configure/frontmatter.md` — how to write YAML frontmatter
- [ ] Write `AGENTS.md` — map of the project (use `writing-claude-md` skill)
- [ ] Write `CLAUDE.md` — behavioral contract (use `writing-claude-md` skill)
- [ ] Write `PLAN.md` — task list with acceptance criteria and closure contracts
- [ ] Write `CLOSED_TASKS.md` — closed-task registry
- [ ] Write `validation-manifest.json` — machine-readable registry

### 3.2 Validation
- [ ] Read `references/03-configure/validators.md`
- [ ] Write `done-check.sh` — THE completion authority
- [ ] Write `validate-global.sh` — tests, lint, typecheck
- [ ] Write `validate-closed-tasks.sh` — regression tests (Tier 2+)
- [ ] Write `validate-no-blockers.sh` — open task detection
- [ ] Write `validate-no-tampering.sh` — tampering detection (Tier 2+)
- [ ] Write `close-task-check.sh` — single-task promotion check

### 3.3 Constraints (Hooks)
- [ ] Read `references/03-configure/hooks.md`
- [ ] Install `stop-if-not-done.sh` — blocks premature exit (use `claude-code-hooks` skill)
- [ ] Install `block-dangerous.sh` — blocks destructive commands
- [ ] Install `protect-control-files.sh` — blocks editing control files (Tier 2+)
- [ ] Install `session-start-reminder.sh` — re-injects rules
- [ ] Install `post-edit-reminder.sh` — reminds to validate (optional)
- [ ] Wire hooks in `.claude/settings.json` (use `claude-code-hooks` skill)

### 3.4 Feedback (Judge)
- [ ] Read `references/03-configure/judges.md`
- [ ] Design principles — `references/02-decide/judge-principles.md`
- [ ] Create judge subagent(s) — use `Agent` tool with YAML frontmatter
- [ ] Write judge principles file — `.mission-control/judge-principles.md`

### 3.5 Memory (Skills)
- [ ] Read `references/03-configure/skills.md`
- [ ] Create system skill (use `write-a-skill` skill)
- [ ] Create domain skills (use `write-a-skill` skill)

### 3.6 Commands
- [ ] Create slash commands in `.claude/commands/`
  - `/close-task` — closure workflow
  - `/run-judge` — spawn judge subagent
  - `/mc-status` — show current state
  - `/mc-recovery` — recover after context loss
  - `/session-start` — initialize new session
  - `/handoff` — pass context to next agent

### 3.7 Project Structure
- [ ] Create `.mission-control/` directory with `state.json`
- [ ] Create `.claude/` directory with hooks, agents, commands, skills, rules
- [ ] Verify all files exist
- [ ] Record what was created

---

## Phase 4: Test (Verify the harness)

- [ ] Read `references/04-test/README.md`
- [ ] Run `done-check.sh` — must pass on current code
- [ ] Run each hook — verify blocking works
- [ ] Run judge on sample output — verify JSON and scores
- [ ] Run closed-task regression — verify no false failures
- [ ] Read `references/04-test/common-mistakes.md` — check for anti-patterns

---

## Phase 5: Operate (Run the harness)

- [ ] Read `references/05-operate/README.md`
- [ ] Start session — hook reminds you of protocol
- [ ] Pick task from `PLAN.md` — work on it
- [ ] Run `done-check.sh` — it decides if you're done
- [ ] Spawn judge subagent — scores the work
- [ ] Run `/close-task` — closure workflow updates registries
- [ ] State tracked in `.mission-control/state.json`
- [ ] If crash: read `references/05-operate/run-recovery.md`

---

## Key Rules

- Scripts are the completion authority. `done-check.sh` decides when work is done.
- Scripts = deterministic only. Judge = qualitative only. No overlap.
- The judge is always a subagent (`.claude/agents/*.md`), never a script.
- Always invoke `writing-claude-md` to write `CLAUDE.md`. Never write it directly.
- Always create a system skill. Hard gate — do not skip.
- Hooks via `claude-code-hooks` skill. Do not write them manually.
- Skills via `write-a-skill` skill. Do not write them manually.
