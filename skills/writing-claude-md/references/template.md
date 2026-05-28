# Production-ready template

## Full template (~70 lines)

Copy this and fill in. Delete sections that don't apply.

```markdown
# Project: <NAME>

<one-line description: stack, purpose, who it's for>

## Commands

- `<cmd>`: Start dev server
- `<cmd>`: Run unit tests
- `<cmd>`: Run e2e tests
- `<cmd>`: Type check
- `<cmd>`: Lint + format (auto-fix where safe)
- `<cmd>`: Run db migrations
- `<cmd>`: Build for production

## Architecture

- `/app` — Next.js App Router pages and layouts
- `/components/ui` — shared UI primitives
- `/lib` — utilities and shared logic
- `/lib/auth` — authentication (see `lib/auth/CLAUDE.md`)
- `/prisma` — schema and migrations
- `/app/api` — API routes

## Hard rules

- **IMPORTANT**: Never commit `.env` files or any credentials.
- **IMPORTANT**: All API handlers under `/app/api` must validate input with Zod schemas.
- Use named exports. No default exports.
- No `any` types without a `// reason:` comment on the next line.
- All database access goes through `/lib/db`. Never import Prisma directly from a component or API route.
- Use the logger (`lib/log.ts`). No `console.log` in committed code.

## Workflow

- Make minimal changes — do not refactor unrelated code.
- Ask before changing content I've already created.
- Create separate commits per logical change.
- When unsure between two approaches, explain both and let me choose.
- Ask clarifying questions before starting complex or ambiguous tasks.
- After completing a task: list files changed, files intentionally not touched, follow-up needed.

## Human approval required (full stop)

YOU MUST get explicit in-session confirmation before:

- Deploying to any environment
- Running migrations on any database
- Modifying anything under `/infra/`
- Modifying `lib/payments/` (billing — human review required)
- Sending any email or external API call
- Executing any command with irreversible external side effects

## Out of scope

- `/generated/` — auto-generated, never edit by hand.
- `/legacy/` — deprecated, do not touch unless explicitly asked.
- `CHANGELOG.md` — maintained by the release pipeline.

## Pointers

- Building & deploying: `agent_docs/building.md`
- Testing patterns: `agent_docs/testing.md`
- Auth flow: `lib/auth/CLAUDE.md`
- API conventions: `app/api/CLAUDE.md`
```

## Compressed variant (~14 lines)

For mature repos with strong auto-memory:

```markdown
# Project: <NAME>

Stack: <stack>. Build: `<cmd>`. Test: `<cmd>`. Lint: `<cmd>`.

Architecture: see `agent_docs/architecture.md`.

- IMPORTANT: Never commit `.env`. Never modify `/infra/` or `lib/payments/` without explicit approval.
- All db access via `/lib/db`. Use the logger, not console.log. Named exports only.
- Make minimal changes. Don't refactor unrelated code. Ask before big edits. Separate commits per logical change.
- Human approval required: deploys, migrations, infra, payments, external APIs.
- Out of scope: `/generated/`, `/legacy/`, `CHANGELOG.md`.
```

## Karpathy's four rules (drop-in for the Workflow section)

```
- Ask, don't assume — if something is unclear, ask before writing a single line.
- Simplest solution first — implement the simplest thing that could work. No abstractions that weren't requested.
- Don't touch unrelated code — if a file is not directly part of the current task, do not modify it. Ever.
- Flag uncertainty explicitly — if you're not confident, say so before proceeding.
```
