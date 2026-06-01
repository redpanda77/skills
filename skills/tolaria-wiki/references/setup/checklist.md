# Tolaria Wiki Master Checklist

The complete checklist for setting up a Tolaria vault. Follow this in order. Do not skip steps.

---

## Phase 0: Self-Setup (Read this skill)

- [ ] Read `SKILL.md` — understand the 3 workflows and the pipeline
- [ ] Read `references/principles.md` — the 12 non-negotiable principles
- [ ] Read `references/architecture.md` — the pipeline, layers, and contracts
- [ ] Read `references/setup/checklist.md` — this file (master checklist)

---

## Phase 1: Discover (Understand the project)

- [ ] Read `references/operations/types.md` — every type, schema, and routing
- [ ] Read `references/operations/format.md` — file format rules
- [ ] Audit current state: does a vault already exist? What exists? What's missing?
- [ ] Pick methodology: Default (generic notes) or PARA / Zettelkasten / LYT / Team-Work (see `references/setup/methodology-modes.md`)
- [ ] Record: `VAULT_PATH`, `IDENTITY`, `METHODOLOGY`

---

## Phase 2: Setup (Create the vault)

- [ ] Read `references/setup/setup.md` — detailed setup procedure
- [ ] Confirm vault location (ask user if not already set)
- [ ] Confirm identity line (ask user)
- [ ] Confirm optional extras (daily-note template, sample seed notes, integration watcher)
- [ ] Create folder structure (`mkdir -p` command)
- [ ] Write type-definition files at vault root (10 files from `templates.md`)
- [ ] Write `AGENTS.md` (from `templates.md`)
- [ ] Write `CLAUDE.md` (from `templates.md`, fill in identity and confidentiality)
- [ ] Optionally: copy skill locally to `<vault>/.claude/skills/`
- [ ] Optionally: write daily-note template, sample seed notes
- [ ] Optionally: scaffold integration watcher script
- [ ] Optionally: initialize git
- [ ] Append maintenance log entry: vault bootstrap
- [ ] Confirm and hand back to user

---

## Phase 3: Configure (Type system and contracts)

- [ ] Read `references/operations/types.md` § "Status lifecycles"
- [ ] Verify all 10 type-definition files are present and correct
- [ ] Verify `AGENTS.md` is present and imports correctly
- [ ] Verify `CLAUDE.md` is present and under 80 lines
- [ ] Test: create one note of each type to verify filing works
- [ ] Test: verify cross-linking works (create a note with `related_to:` links to other notes)
- [ ] Test: verify Raw processing works (create a Raw, process it, verify it moves to archive)
- [ ] Test: verify summary generation works (create daily summary)
- [ ] Record: types tested, cross-links verified, Raw pipeline verified

---

## Phase 4: Operate (Daily use)

- [ ] Read `references/operations/authoring.md` — create, classify, file, cross-link
- [ ] Read `references/operations/maintenance.md` — process raw, import, generate summaries
- [ ] Read `references/operations/integrations.md` — connect external sources
- [ ] Read `references/orchestration/automation.md` — deterministic refresh, auto-process, context packs
- [ ] Read `references/operations/health.md` — vault health checks
- [ ] Read `references/operations/maintenance.md` § "Audit" — source traceability, receipts, hash-based freshness
- [ ] Create a note (test authoring workflow)
- [ ] Process a Raw note (test maintenance workflow)
- [ ] Generate a daily summary (test summary workflow)
- [ ] Run a health check (test health workflow)
- [ ] Verify automation: auto-process unambiguous Raw, auto-link suggestions

---

## Phase 5: Maintenance (Keep the vault healthy)

- [ ] Read `references/operations/health.md` — health check procedure
- [ ] Read `references/operations/maintenance.md` § "Audit" — audit trail and freshness
- [ ] Read `references/operations/maintenance.md` § "Stale Raw" and "What to refuse"
- [ ] Weekly: run health check (orphans, dead links, stale Raw, empty notes)
- [ ] Weekly: process any unprocessed Raw notes
- [ ] Weekly: check for stale summaries (compare source_evidence hashes)
- [ ] Monthly: review methodology alignment — is the folder structure still right?
- [ ] Monthly: verify no notes are missing `type:` or `status:`
- [ ] After changes: run targeted health check on affected areas

---

## Key Rules

- The vault is a graph, not a folder hierarchy. Folders are for browsing; the graph is the truth.
- State is derived from the vault. Re-read indexes before acting.
- Raw sources are immutable. The wiki is a maintained layer.
- Context is bounded. Never read the entire vault.
- Automation is deterministic. Scripts expose evidence; models decide.
- The audit trail is append-only. Never rewrite history.
- Human curates, LLM maintains. The human approves; the LLM executes.
- Never delete, only archive.
- Confidentiality is opt-out, not opt-in.
