# High-impact lines

Copy-paste reference. Each line has measurable impact on output quality across many projects.

## Workflow

- `Make minimal changes — do not refactor unrelated code.`
- `Create separate commits per logical change, not one giant commit.`
- `When unsure between two approaches, explain both and let me choose.`
- `Ask clarifying questions before starting any complex or ambiguous task.`
- `After completing a task: files changed, what was modified (one line per file), files intentionally not touched, follow-up needed.`

## Quality

- `IMPORTANT: run type check after every code change.`
- `Run <test-cmd> before marking any task complete.`

## Security

- `NEVER commit .env files or any credentials.`
- `YOU MUST get explicit confirmation before running migrations on any database.`
- `YOU MUST get explicit confirmation before deploying to any environment.`

## Scope

- `Only modify files, functions, and lines directly related to the current task. If you notice something elsewhere, mention it. Don't touch it.`
- `Before deleting any file, overwriting code, or dropping records, list what will be affected and ask for explicit confirmation.`

## Stack-specific examples

- `Static export only, no SSR (deployed to S3).`
- `Use named exports. No default exports.`
- `All database access through /lib/db. Never import Prisma directly from a component or API route.`
- `All API handlers validate input with Zod schemas.`
- `Use the logger (lib/log.ts). No console.log in committed code.`

## Karpathy four (drop-in block)

```
- Ask, don't assume — if something is unclear, ask before writing a single line.
- Simplest solution first — implement the simplest thing that could work. No abstractions that weren't requested.
- Don't touch unrelated code — if a file is not directly part of the current task, do not modify it. Ever.
- Flag uncertainty explicitly — if you're not confident, say so before proceeding.
```
