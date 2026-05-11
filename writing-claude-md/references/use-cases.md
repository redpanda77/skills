# Templates per use case

CLAUDE.md isn't only for coding. Each use case has a different shape. Pick the one that matches discovery + classification.

---

## 1. `coding-single` — one app/package

See [[template]] for the full production-ready coding template (`references/template.md`). 5 sections: Commands, Architecture, Hard Rules, Workflow, Human-Approval / Out-of-Scope.

Length target: 60–120 lines.

---

## 2. `coding-monorepo` — multiple packages

Thin root + nested files. See `nested-decisions.md`.

Root template (target < 80 lines):

```markdown
# Monorepo: <NAME>

<one-line description>. <N> packages: list them.

## Universal commands

- `<cmd>`: Install all deps
- `<cmd>`: Run all tests
- `<cmd>`: Run all linters
- `<cmd>`: Build all

## Packages

- `apps/web` — see `apps/web/CLAUDE.md`
- `apps/api` — see `apps/api/CLAUDE.md`
- `packages/ui` — shared components, see `packages/ui/CLAUDE.md`
- `infra/` — Terraform, see `infra/CLAUDE.md`

## Hard rules (universal)

- IMPORTANT: Never commit `.env`.
- All packages use <package-manager>, never mix.
- Commits use <conventional/semantic> format.

## Workflow

- Make minimal changes — do not refactor unrelated code.
- Separate commits per logical change.
- Ask before changing files outside the package you're working in.

## Human approval required

YOU MUST get confirmation before:
- Deploying any package
- Running migrations
- Modifying `/infra/`
- Cross-package refactors

## Out of scope

- `/generated/`
- `/legacy/`
- Anything outside the package you were asked to work in (without explicit ask)
```

---

## 3. `writing` — book, blog, content

```markdown
# Writing project: <NAME>

<one-line: what you're writing and for whom>

## Voice

- <voice description from interview>
- Audience: <audience>
- Tone: <tone markers>

## Style

- <e.g., short sentences, declarative>
- <e.g., first-person>
- <e.g., no filler — never open with "Great question" or "Of course">
- <e.g., active voice>
- <e.g., specific examples over abstractions>

## Words I never use

- <comma-separated list>

## Format

- <e.g., H2 for sections, no H3 unless > 3 paragraphs under it>
- <e.g., one idea per paragraph>
- <e.g., lists for parallel items, prose for sequences>

## Workflow

- Only change what I specifically asked you to change.
- After editing, summarize: what changed, what's untouched, what needs my attention.
- Match my voice exactly. Do not default to your own patterns.
- If you suggest a structural change, propose it first — don't apply it.

## Hard rules

- IMPORTANT: Never claim facts, statistics, dates, or quotes you aren't sure about. Flag uncertainty.
- Never add emojis unless I explicitly ask.
- Never use em-dashes / Oxford commas / <user preference>.
- Never end paragraphs with "In conclusion" / "Ultimately" / <user preference>.

## Out of scope

- `_drafts/archive/` — don't touch
- `_published/` — never edit; create new drafts to revise
```

Target length: 40–80 lines.

---

## 4. `research` / knowledge-base / vault

```markdown
# Knowledge base: <NAME>

<one-line: what this vault is for, e.g., "Careem Food PM wiki for Gonzalo">

## Structure

- `meetings/` — meeting notes (frontmatter: type=Meeting)
- `initiatives/` — ongoing initiatives (frontmatter: type=Initiative)
- `decisions/` — recorded decisions (frontmatter: type=Decision)
- `Raw/` — inbox, unprocessed
- `summaries/` — daily/weekly summaries
- `daily/` — standup notes

## Conventions

- Every note has YAML frontmatter with `type` and `date`.
- Cross-link with `[[wikilinks]]`, not markdown links.
- File names use kebab-case.
- Dates in frontmatter: `YYYY-MM-DD`.

## Workflow

- When adding a new note, place it in the correct folder per `type`.
- When processing a Raw note: create structured note, update Raw status to Processed, move to `Raw/archive/`.
- Never delete original meeting transcripts or source recordings.
- Append to `logs/maintenance-log.md` after any structural change.

## Hard rules

- IMPORTANT: Never modify notes in `_published/` or `_archive/` without explicit ask.
- Never invent dates, attendees, or decisions.
- Never delete a note — move to `_archive/` instead.

## When to ask

- Note category unclear → ask before filing.
- Action items lack owners → ask.

## Out of scope

- `attachments/` — binary files
- `.obsidian/` / `.tolaria/` — tool config
```

Target length: 40–80 lines.

---

## 5. `pm` — product management

```markdown
# PM workspace: <NAME>

<role + scope, e.g., "Careem Food PM, focus on ranking & search">

## What I work on

- <area 1>
- <area 2>
- <area 3>

## Stakeholders

- <name> (<role>) — <relationship>
- <name> (<role>) — <relationship>

## Workflow

- When summarizing meetings: group by category (Data, Engineering, Design, Stakeholder).
- Extract action items with owners. Flag missing owners.
- List decisions made and blockers identified explicitly.
- Reference initiatives by `[[wikilink]]`.

## Hard rules

- IMPORTANT: Never share or summarize content from notes marked `confidential: true` outside the vault.
- Never invent attendees or quotes.
- Treat "stakeholder", "exec", "leadership" notes as confidential by default.

## Communication style

- Direct, no filler.
- Recommendations come with explicit tradeoffs.
- For exec-bound material: 1-paragraph TL;DR up front.

## Out of scope

- `confidential/` — never read or summarize without explicit ask
```

Target length: 40–80 lines.

---

## 6. `marketing` — campaigns, brand

```markdown
# Marketing: <BRAND/PROJECT>

<one-line>

## Brand voice

- <markers from interview>
- Audience: <audience>
- Channels: <channels>

## Style

- Open with the strongest claim, not a setup.
- Concrete > abstract. Use specific numbers, names, examples.
- Cut filler ("just", "really", "very", "in order to").
- One idea per sentence.

## Words we never use

- <forbidden list>

## Approvals

YOU MUST get explicit approval before:
- Publishing or scheduling any post
- Sending any email
- Posting to social
- Modifying landing-page copy in production

## Hard rules

- IMPORTANT: Never claim metrics, statistics, or testimonials you cannot verify.
- Never use stock phrases that violate the brand voice (see "Words we never use").
- Never write in the voice of a named person without their content.

## Out of scope

- `_archive/` — old campaigns
- `legal/` — legal review docs
```

Target length: 40–80 lines.

---

## 7. `mixed` — code + content

Combine the relevant sections from the coding template and the content/writing/PM template.

Pattern:
- Start with the code-side (Commands, Architecture, Hard Rules, Workflow) — these are higher-risk.
- Add a `## Content` section with voice/style/forbidden words.
- Out-of-scope covers both code (`generated/`, `infra/`) and content (`_drafts/archive/`).

Target length: 60–100 lines. If both halves are deep, split into root + `content/CLAUDE.md` nested.

---

## Cross-cutting (every template)

Every template should include — adapted to the use case:

- **Workflow** section with "ask before big changes", "summarize what changed".
- **Hard rules** with at least one `IMPORTANT:`.
- **Out of scope** — what to never touch.
- **Approval requirements** if any irreversible / external-effect actions exist.
