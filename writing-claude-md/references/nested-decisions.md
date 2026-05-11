# Nested CLAUDE.md decisions

Subdirectory CLAUDE.md files load **on demand** when Claude reads/edits files in that subtree. They are the primary mechanism for keeping context clean in large repos.

## When to create a nested CLAUDE.md

Create one if **two or more** of these are true for the folder:

- Conventions diverge from the rest of the repo (e.g., Python in a TS monorepo, Terraform alongside app code).
- The folder owns sensitive logic (auth, payments, PII, billing).
- There are folder-specific "do not touch" rules.
- There are folder-specific commands (e.g., a separate test runner, deployment script).
- The folder has its own team / owner.
- The root file would grow past target if these rules were added there.

## When NOT to create one

- Folder follows the same conventions as the rest of the repo.
- Folder is small (< 10 files) and shallow.
- Rules would fit in 5 lines or fewer — put them in the root with a `### <folder>` subsection.
- Folder is purely generated, vendored, or read-only (use root "Out of scope" instead).

## Decision tree (run per top-level folder)

```
For each top-level folder:
  Has divergent conventions?         → +1
  Owns sensitive/high-risk logic?    → +1
  Has its own commands/tooling?      → +1
  Owned by a different team?         → +1
  Adding to root would exceed budget?→ +1

  Score >= 2  → recommend nested CLAUDE.md
  Score == 1  → mention in root with a short `### <folder>` subsection
  Score == 0  → nothing
```

## Coding monorepo — typical layout

```
repo/
├── CLAUDE.md                       # thin root, < 80 lines
├── apps/
│   ├── web/CLAUDE.md               # Next.js conventions
│   └── api/CLAUDE.md               # endpoint conventions, auth middleware
├── packages/
│   ├── ui/CLAUDE.md                # component library conventions
│   └── shared/CLAUDE.md            # type / util conventions
└── infra/CLAUDE.md                 # Terraform + approval rules
```

## Non-code project — typical layout

For a knowledge base / PM vault (e.g., Tolaria-style):

```
vault/
├── CLAUDE.md                       # voice, frontmatter convention, wikilink rule, naming
├── meetings/CLAUDE.md              # how to format meeting notes (only if conventions differ)
├── initiatives/CLAUDE.md           # how to format initiatives (only if conventions differ)
└── Raw/CLAUDE.md                   # how to process inbox items
```

In practice, knowledge bases often need **only the root** + maybe one nested file for the inbox/processing folder.

## What goes in a nested file

Three sections, very tight:

```markdown
# <Folder name>

<one-line purpose>

## Conventions

- <rule 1>
- <rule 2>

## Commands (if any)

- `<cmd>`: …

## Hard rules

- IMPORTANT: <folder-specific never>
- <folder-specific approval requirement>
```

Keep nested files **30–60 lines**. If you need more, split further or move common rules up to the root.

## Don't duplicate

If a nested rule already exists in the root, **don't repeat it** in the nested file. Root rules apply everywhere; nested files add specifics on top.

## Verification

After writing nested files, in the next session, `cd` into the relevant folder and run `/memory` to confirm the nested file loads.
