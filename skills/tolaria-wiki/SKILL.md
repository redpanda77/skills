---
name: tolaria-wiki
description: Set up, author in, and maintain a Tolaria knowledge vault (folder of Markdown + YAML frontmatter forming a personal knowledge graph). Use when the user wants to create a new Tolaria vault from scratch; create any vault note (Meeting, Decision, Initiative, Feature, Research, Person, Note, Raw); process raw notes; import meeting recordings or transcripts; generate daily / weekly / topic summaries; or set up integrations with external sources (recorders, transcript folders, Slack exports, Jira/Linear, etc.). Tolaria is a folder-of-markdown vault format — github.com/refactoringhq/tolaria. Works on a fresh machine with no prior setup.
---

# Tolaria Wiki — zero to running

Single self-contained skill for everything Tolaria. Three workflows, autodetected from the user's request.

## What is Tolaria?

A Tolaria vault is a folder of Markdown files with YAML frontmatter. Each file is one note. Frontmatter properties define type, status, dates, and relationships. Relationships use `[[wikilinks]]`. Saved views live in `views/*.yml`. That's it — no database, no proprietary format, plain files you can read with any editor and version with git.

The skill works whether or not the user has the Tolaria app installed. The format is the contract; the app is one viewer.

## Detect the situation

Before doing anything, check the working directory:

```bash
test -f AGENTS.md && grep -l "tolaria" AGENTS.md && echo "vault-exists"
test -f CLAUDE.md && echo "has-claude-md"
test -d meetings && test -d initiatives && echo "looks-like-vault"
```

Then route:

| Situation | Workflow | Reference |
|-----------|----------|-----------|
| No vault, user wants to start one | **Setup** | `references/setup.md` |
| Vault exists, user wants to create/file a note | **Authoring** | `references/authoring.md` |
| Vault exists, user wants to process raw, import recordings, generate summaries | **Maintenance** | `references/maintenance.md` |
| User asks about types, frontmatter, naming, folder routing | Lookup | `references/types-reference.md` |
| User asks about file format details (YAML, H1, views, underscore keys) | Lookup | `references/tolaria-format.md` |
| User wants to connect an external source (recorder, transcripts, Slack) | Integrations | `references/integrations.md` |

## Universal rules (always apply)

These hold in every workflow. Don't repeat them in references — enforce them everywhere.

- **One Markdown note per file.** Filenames `kebab-case.md`.
- **YAML frontmatter** between `---` fences at the top of every note.
- **First H1 in the body is the display title.** Do not also set `title:` in frontmatter on new notes (legacy support only).
- **`type:`** is required on every note. Set it exactly as defined (Meeting, Decision, Initiative, Feature, Research, Note, Raw, Person, Summary, Type).
- **`[[wikilinks]]`** for cross-references — never markdown links inside the vault.
- **Quoted wikilinks for scalar frontmatter values** (`owner: "[[name]]"`), **YAML lists for multi-value** (`attendees: [- "[[a]]", - "[[b]]"]`).
- **Dates** as `YYYY-MM-DD`.
- **Underscore-prefixed frontmatter keys** (`_icon`, `_color`, `_organized`) are Tolaria-managed app state. Never touch unless explicitly editing config.
- **Never delete a note.** Move to an `archive/` subfolder or change status to `Archived` / `Stale`.
- **Never invent** dates, attendees, decisions, quotes, or facts. Flag uncertainty and ask.
- **Treat confidential material as confidential by default** — anything marked `confidential: true` in frontmatter, anything in folders the user designates as such. Never summarize or share outside the vault without explicit ask in the current message.

## When to use AskUserQuestion

- During **setup**: confirm vault location, identity, confidentiality default, whether to install opinionated extras (daily note template, integration watchers).
- During **authoring**: type ambiguous (Note vs Research vs Initiative), meeting category unclear, owner missing on an action item.
- During **maintenance**: source-to-destination routing unclear, action items lack owners.

Default to proceeding autonomously when context is unambiguous. Cap at 5 questions per session.

## What this skill does NOT do

- Does not write CLAUDE.md instruction files for *coding* projects — for that, the user should use a CLAUDE.md authoring skill if available. This skill ships a Tolaria-specific CLAUDE.md template inside `references/templates.md`.
- Does not transcribe audio or extract text from PDFs. Treats those as upstream — see `references/integrations.md` for the contract.
- Does not deploy or sync anywhere. Vault is local files. Sync is the user's choice (git, iCloud, Dropbox, Syncthing).

## References

- `references/setup.md` — create a vault from nothing
- `references/authoring.md` — create, classify, file, cross-link any note
- `references/maintenance.md` — process raw, import recordings, generate summaries, log
- `references/types-reference.md` — every type, frontmatter schema, folder routing, naming
- `references/tolaria-format.md` — file format rules (YAML, H1, wikilinks, views, underscore keys)
- `references/integrations.md` — pattern for plugging in external sources (recorders, transcripts, Slack, Jira/Linear)
- `references/templates.md` — copy-paste templates for AGENTS.md, CLAUDE.md, type definitions, daily note
