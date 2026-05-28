# Setup — zero to running vault

For a user with nothing. End state: a working Tolaria vault with folder structure, type-definition files, `AGENTS.md`, `CLAUDE.md`, and the skill itself accessible from the vault.

## Step 0 — Confirm intent

Ask if not already clear:

> Where should the vault live?
> - `~/Documents/Wiki` (Recommended)
> - `~/Documents/Tolaria`
> - `~/Notes`
> - Custom path

Then ask one identity question:

> Tell me in one line who you are and what this vault is for. (Freeform — used at the top of CLAUDE.md.)

Optional, AskUserQuestion (multiSelect):

> Install opinionated extras now? You can add them later.
> - Daily-note template (Recommended)
> - Sample seed notes (one of each type, for learning)
> - Integration watcher pattern (example shell script)
> - None — bare vault only

## Step 1 — Create the folder structure

Standard layout. Adapt to user need but keep the core folders.

```bash
VAULT="$HOME/Documents/Wiki"   # or whatever the user chose
mkdir -p "$VAULT"/{meetings/{data,design,engineering,stakeholder,general},initiatives,features,research,decisions,people,daily,Raw/archive,summaries,logs,attachments,views}
```

Folder roles:

| Folder | Purpose |
|--------|---------|
| `meetings/` | Processed meeting notes, subfoldered by category |
| `initiatives/` | Epic-level ongoing work |
| `features/` | Specific feature specs |
| `research/` | Reference research with external sources |
| `decisions/` | ADRs and product calls |
| `people/` | One note per person (team, stakeholders, contacts) |
| `daily/` | Daily standup notes |
| `Raw/` | Inbox — unprocessed source material |
| `Raw/archive/` | Processed Raw originals, preserved for audit |
| `summaries/` | Daily/weekly/topic summaries |
| `logs/` | Maintenance log (append-only) |
| `attachments/` | Binary assets (images, PDFs) |
| `views/` | Tolaria saved views (`*.yml`) |

Sub-categorization of `meetings/` is optional — use it if the user expects regular meetings across distinct domains; collapse to a flat `meetings/` if not. Confirm via AskUserQuestion if unsure.

## Step 2 — Write type-definition files at the vault root

Tolaria uses regular notes at the vault root as type definitions. Set `type: Type` in frontmatter. Get the full set from `templates.md`. Always include:

- `note.md`
- `meeting.md`
- `decision.md`
- `initiative.md`
- `feature.md`
- `research.md`
- `raw.md`
- `person.md`
- `summary.md`
- `type.md` (definition of the Type type itself)

Write all of them at once with the templates from `templates.md`.

## Step 3 — Write `AGENTS.md`

Tool-agnostic vault mechanics (file format, frontmatter conventions, view rules). Use the template from `templates.md` § "AGENTS.md template". Customize only the top description line if needed.

## Step 4 — Write `CLAUDE.md`

Behavioral contract for Claude Code in this vault. Use the template from `templates.md` § "CLAUDE.md template". Fill in:

- Identity line from Step 0
- Confidentiality default (ask if not stated — default "everything in `stakeholder/` is confidential by default")
- `@AGENTS.md` import at the bottom

Keep it under 80 lines. The template is already lean — resist adding to it during setup.

## Step 5 — Make the skill discoverable from inside the vault (optional)

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

## Step 6 — Optional extras (only if user opted in)

### Daily-note template

Write `daily/_template.md` from `templates.md` § "Daily note template". Users can copy it as the starting point for `daily/YYYY-MM-DD.md`.

### Sample seed notes

Write one note of each type with realistic-but-generic content (e.g., a fake meeting, an example initiative). Useful for learning the conventions. List them with `seed-` prefix or in a `_examples/` folder the user can later delete.

### Integration watcher

If the user has a meeting recorder, transcript folder, or other external source, point them at `references/integrations.md` and offer to scaffold a watcher script. Don't install anything that runs in the background without explicit consent.

## Step 7 — Initialize git (recommended, ask)

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

## Step 8 — Append the maintenance log entry

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
$([ -d "$VAULT/.claude/skills/tolaria-wiki" ] && echo "- Project-local tolaria-wiki skill")

EOF
```

## Step 9 — Confirm and hand back

Tell the user:

1. Where the vault is.
2. What was created (counts: N folders, N type files, N skill files if project-local).
3. Three things they can try:
   - "Create a meeting note for today's standup" (authoring workflow)
   - "Process Raw/<file>" (maintenance workflow)
   - "What types are available?" (lookup → `types-reference.md`)
4. If they have a meeting recorder: point at `references/integrations.md`.

## Decisions to never make autonomously

- **Where the vault lives** — always ask.
- **Whether to install background scripts** — always ask.
- **Whether to overwrite an existing `CLAUDE.md` or `AGENTS.md`** — if file exists, ask before overwriting.
- **Whether to init git** — ask.
