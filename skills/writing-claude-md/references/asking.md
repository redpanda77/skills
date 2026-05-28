# Using AskUserQuestion in this skill

Front-load decisions. Ask narrow, structured questions one at a time. Skip anything discovery already answered.

## When to use AskUserQuestion (vs. plain text question)

| Situation | Use |
|-----------|-----|
| Decision between 2–6 known options | **AskUserQuestion** |
| Yes/no with consequences | **AskUserQuestion** |
| Open-ended freeform (project name, audience description) | Plain text |
| Confirming a recommendation | **AskUserQuestion** with one option marked `(Recommended)` |
| Multi-select (which folders, which integrations) | **AskUserQuestion** with `multiSelect: true` |

## Format rules

- Recommended option goes **first** with `(Recommended)` suffix on the label.
- Each option has a short description (1 line, what it implies).
- Always include an **"Other"** affordance — users can supply custom text.
- Multi-select only when answers are genuinely independent.
- Cap at 5 questions per setup session.

## Question bank by use case

Skip any question the discovery step already answered.

### Universal (all use cases)

1. **Layer / scope** (only if ambiguous)
   > Where should this CLAUDE.md live?
   > - Project root, shared with the team (Recommended)
   > - `.claude/CLAUDE.md` (config subdir)
   > - `CLAUDE.local.md` (gitignored, personal only)

2. **Multi-tool setup** (only if you see signals for Cursor, Copilot, etc.)
   > I see signs of multiple AI tools in this repo. Want a unified setup?
   > - Yes — canonical `AGENTS.md` + thin `CLAUDE.md` (Recommended)
   > - No — Claude Code only

### Coding-specific

3. **Hard rules — top 3 "never do this"**
   > What are the top 3 "never do this" rules every new dev on this codebase learns the hard way? (Freeform.)

4. **Human approval required** (multiSelect)
   > Which actions require explicit human approval before execution?
   > - Deploying to any environment (Recommended)
   > - Running database migrations (Recommended)
   > - Modifying `infra/` or Terraform (Recommended)
   > - Modifying billing/payments code
   > - Sending email or external API calls
   > - Deleting files or dropping records
   > - None of the above

5. **Out of scope folders** (multiSelect, auto-populate from discovery)
   > Which folders should Claude **never** modify?
   > - `<generated/>` (Recommended)
   > - `<legacy/>`
   > - `<infra/>`
   > - `<vendor/>` or `<node_modules/>`
   > - None

### Writing-specific

3. **Voice**
   > Describe your voice in 1 sentence. (Freeform.)

4. **Audience**
   > Who is the audience? (Freeform.)

5. **Style markers** (multiSelect)
   > Style preferences:
   > - Short sentences (Recommended)
   > - First-person
   > - No filler / no hedging
   > - No emojis
   > - Active voice only
   > - Avoid jargon
   > - Use specific examples over abstractions

6. **Words to avoid**
   > Words or phrases Claude must never use. (Freeform comma-separated.)

### Research / PM / knowledge-base

3. **Note types** (multiSelect, auto-populate from folders found)
   > Which note types live here?
   > - Meeting notes
   > - Decisions
   > - Initiatives
   > - Daily standups
   > - Raw / inbox
   > - Research
   > - Summaries

4. **Frontmatter convention**
   > Do notes use YAML frontmatter?
   > - Yes — type, date, status (Recommended, infer from existing notes)
   > - No
   > - Mixed / unsure

5. **Wikilinks**
   > Cross-link style?
   > - `[[wikilinks]]` (Recommended for Obsidian/Tolaria)
   > - Markdown links `[text](path)`
   > - Both

### Marketing

3. **Brand voice** (multiSelect)
   > Brand voice markers:
   > - Confident, declarative (Recommended)
   > - Warm, conversational
   > - Technical, precise
   > - Playful, witty
   > - Authoritative, formal

4. **Forbidden words**
   > Words you never use in brand copy. (Freeform.)

5. **Channels** (multiSelect)
   > Channels this guides:
   > - Long-form posts
   > - Social posts (X, LinkedIn)
   > - Email
   > - Landing pages
   > - Internal comms

## Don't ask

- **Stack** if `package.json` / `pyproject.toml` / etc. exist.
- **Build commands** if you found them in `scripts:` or `Makefile`.
- **Folder names** — `ls`.
- **Project name** — `package.json` `name` or directory name.
- **Git status** — `git status`.
- **License** — `LICENSE` file.

## Iterative follow-ups

After v0 is written, offer **one** follow-up question:

> Want to run the 5-prompt adherence test against this v0?
> - Yes (Recommended)
> - No, ship it
