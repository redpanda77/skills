# Setup — zero to running vault

**When to read this:** When the user wants to create a new Tolaria vault from scratch. This is the master procedure. Read `references/templates.md` for copy-paste templates after understanding the setup steps.

## Step 0 — Read the checklist

Before starting, read `references/setup/checklist.md`. It is the single source of truth for the setup process.

## Step 1 — Confirm intent

Ask if not already clear:

> Where should the vault live?
> - `~/Documents/Wiki` (Recommended)
> - `~/Documents/Tolaria`
> - `~/Notes`
> - Custom path

Then ask one identity question:

> Tell me in one line who you are and what this vault is for. (Freeform — used at the top of CLAUDE.md.)

Then ask methodology (single choice):

> Which organizational philosophy fits your work?
> - Default (meetings, initiatives, features, research) — recommended for teams and project work
> - PARA (Projects, Areas, Resources, Archives) — recommended for personal productivity
> - Zettelkasten (Fleeting, Literature, Permanent, Index) — recommended for research and writing
> - LYT (Maps of Content, notes, sources, people, projects) — recommended for knowledge work
> - Custom — define your own types during setup

See `references/setup/methodology-modes.md` for details on each mode.

Optional, AskUserQuestion (multiSelect):

> Install opinionated extras now? You can add them later.
> - Daily-note template (Recommended)
> - Sample seed notes (one of each type, for learning)
> - Integration watcher pattern (example shell script)
> - None — bare vault only

## Step 2 — Create the folder structure

Standard layout. Adapt to user need but keep the core folders.

```bash
VAULT="$HOME/Documents/Wiki"   # or whatever the user chose
mkdir -p "$VAULT"/{notes,Raw/archive,summaries,logs,attachments,views,system,archive}
```

Methodology-specific folders (e.g., `meetings/`, `initiatives/`, `features/` for Team/Work; `projects/`, `areas/`, `resources/` for PARA; `fleeting/`, `literature/`, `permanent/` for Zettelkasten) come from `references/setup/methodology-modes.md`. Always add `system/` and `archive/`.

For Custom mode, create folders based on the types the user defines during setup.

Core folder roles:

| Folder | Purpose |
|--------|---------|
| `notes/` | Default folder for structured notes (when no type-specific folder exists) |
| `Raw/` | Inbox — unprocessed source material |
| `Raw/archive/` | Processed Raw originals, preserved for audit |
| `summaries/` | Daily/weekly/topic summaries |
| `logs/` | Maintenance log (append-only) |
| `attachments/` | Binary assets (images, PDFs) |
| `views/` | Tolaria saved views (`*.yml`) |
| `system/` | Vault system documentation (VAULT.md, README.md, CHANGELOG.md) |
| `archive/` | Archived notes (status=Archived or >1 year old) |

**No notes at root.** Only type-definition files and system docs live at root. All notes go in their typed folders.

**Folder size limit:** If a folder has >50 files, create subfolders by year or subcategory. See `references/operations/naming.md`.

## Step 3 — Write type-definition files at the vault root

Tolaria uses regular notes at the vault root as type definitions. Set `type: Type` in frontmatter. Get the full set from `templates.md`. Always include:

- `note.md` (base type for all notes)
- `raw.md` (unprocessed source material)
- `type.md` (definition of the Type system itself)
- `summary.md` (generated summaries)

Methodology-specific types (e.g., `meeting.md`, `initiative.md`, `decision.md`, `feature.md`, `research.md`, `person.md` for Team/Work; `project.md`, `area.md`, `resource.md` for PARA; `fleeting.md`, `literature.md`, `permanent.md` for Zettelkasten) come from `templates.md` § "Methodology-specific type-definition files".

Write all of them at once with the templates from `templates.md`.

## Step 4 — Write `AGENTS.md`

Tool-agnostic vault mechanics (file format, frontmatter conventions, view rules, folder structure). Use the template from `templates.md` § "AGENTS.md template". Customize:

- Top description line
- Folder structure (if using PARA/Zettelkasten/LYT)
- Methodology mode (if applicable)

## Step 5 — Write `CLAUDE.md`

Behavioral contract for Claude Code in this vault. Use the template from `templates.md` § "CLAUDE.md template". Fill in:

- Identity line from Step 1
- Confidentiality default (ask if not stated — default "everything in `stakeholder/` is confidential by default")
- Methodology mode (if applicable)
- `@AGENTS.md` import at the bottom

Keep it under 80 lines. The template is already lean — resist adding to it during setup.

## Step 6 — Write `system/VAULT.md`

This is the vault's system document. It is the single source of truth for this vault's conventions, structure, and maintenance rules. Use the template from `references/setup/templates.md` § "VAULT.md template". Fill in:

- Vault name and purpose (from Step 1 identity line)
- Folder layout (from Step 2)
- Naming conventions (from `references/operations/naming.md`)
- Methodology mode (if applicable)
- Maintenance schedule (weekly health checks, monthly audits)
- Automation rules (auto-process enabled, context pack size)

This document is read by the agent before every operation on this vault. Keep it accurate and up to date.

## Step 7 — Write `system/README.md` (optional)

Human-readable quickstart for the vault. One page explaining what the vault is for, how to navigate it, and where to find things. This is for human readers, not agents.

## Step 8 — Make the skill discoverable from inside the vault (optional)

Two options, ask the user:

> How should this vault find the tolaria-wiki skill?
> - User-global only (Recommended) — skill installed at `~/.claude/skills/tolaria-wiki/`, available in every directory on this machine
> - Project-local copy too — copy skill into `<vault>/.claude/skills/tolaria-wiki/` so the vault is fully portable (you can move it to another machine and the skill goes with it)

If project-local:

```bash
mkdir -p "$VAULT/.claude/skills"
cp -R "$HOME/.claude/skills/tolaria-wiki" "$VAULT/.claude/skills/tolaria-wiki"
```

Then add a `## Project-local skills` section to `CLAUDE.md` listing the skill (see `templates.md`).

## Step 9 — Optional extras (only if user opted in)

### Daily-note template

Write `daily/_template.md` from `templates.md` § "Daily note template". Users can copy it as the starting point for `daily/YYYY-MM-DD.md`.

### Sample seed notes

Write one note of each type with realistic-but-generic content (e.g., a fake meeting, an example initiative). Useful for learning the conventions. List them with `seed-` prefix or in a `_examples/` folder the user can later delete.

### Integration watcher

If the user has a meeting recorder, transcript folder, or other external source, point them at `references/operations/integrations.md` and offer to scaffold a watcher script. Don't install anything that runs in the background without explicit consent.

## Step 10 — Initialize git (recommended, ask)

> Initialize git for this vault?
> - Yes — recommended for backup and history (Recommended)
> - No

If yes:

```bash
cd "$VAULT"
git init
cat > .gitignore <<'EOF'
.DS_Store
.obsidian/workspace*
.tolaria/cache/
attachments/*.tmp
CLAUDE.local.md
EOF
git add -A
git commit -m "Initialize Tolaria vault"
```

## Step 11 — Append the maintenance log entry

```bash
cat >> "$VAULT/logs/maintenance-log.md" <<EOF
---
type: Note
date: $(date +%Y-%m-%d)
---

# Maintenance Log

## $(date +%Y-%m-%d) — Vault bootstrap

### Created
- Folder structure
- Type definitions at vault root
- AGENTS.md
- CLAUDE.md
- system/VAULT.md
- system/README.md
$([ -d "$VAULT/.claude/skills/tolaria-wiki" ] && echo "- Project-local tolaria-wiki skill")

EOF
```

## Step 12 — Confirm and hand back

Tell the user:

1. Where the vault is.
2. What was created (counts: N folders, N type files, N system docs, N skill files if project-local).
3. Three things they can try:
   - "Create a meeting note for today's standup" (authoring workflow)
   - "Process Raw/<file>" (maintenance workflow)
   - "What types are available?" (lookup → `references/operations/types.md`)
4. Point them at `system/VAULT.md` for the vault's conventions and `references/setup/checklist.md` for the full setup checklist.

## Decisions to never make autonomously

- **Where the vault lives** — always ask.
- **Which methodology mode** — always ask.
- **Whether to install background scripts** — always ask.
- **Whether to overwrite an existing `CLAUDE.md` or `AGENTS.md`** — if file exists, ask before overwriting.
- **Whether to init git** — ask.
