# ADR Format

Architecture Decision Records capture decisions that are hard to reverse, surprising without context, and the result of a real trade-off.

## File naming

`docs/adr/NNNN-short-title-in-kebab-case.md`

Number sequentially. Don't reuse numbers. Pad to 4 digits.

## Template

```markdown
# NNNN — Title (imperative: "Use X for Y", "Store Z as W")

**Date:** YYYY-MM-DD  
**Status:** Accepted | Superseded by [NNNN](./NNNN-title.md)

## Context

The situation that forced a decision. What were the constraints, pressures, and requirements? What problem were we solving? Keep it factual — no judgment.

## Decision

What we decided to do, stated plainly. One paragraph.

## Alternatives considered

| Option | Why rejected |
|--------|-------------|
| Option A | ... |
| Option B | ... |

## Consequences

What becomes easier. What becomes harder. What we are explicitly accepting as a downside.
```

## Rules

- **Past tense is wrong.** Write in present tense: "We use X", not "We used X" or "We will use X".
- **No implementation detail** that will rot. "We use event sourcing" is durable. "We use Kafka 3.4.1" is not.
- **One decision per ADR.** If you find yourself writing "and also", split it.
- **Supersede, don't delete.** When a decision is reversed, update the old ADR's status to `Superseded by [NNNN]` and write a new one explaining the change.
- **Keep consequences honest.** The downside column is the most valuable part for future readers. If you can't think of a downside, you haven't thought hard enough.

## Example

```markdown
# 0003 — Use optimistic locking for Order updates

**Date:** 2024-11-14  
**Status:** Accepted

## Context

Multiple services can attempt to update an Order concurrently (customer cancellation, restaurant confirmation, delivery assignment). We needed a concurrency strategy that doesn't require distributed locks or serialisable transactions.

## Decision

We use optimistic locking on the Order aggregate with a version field. Any update increments the version. A concurrent write that presents a stale version is rejected with a 409 and the caller retries.

## Alternatives considered

| Option | Why rejected |
|--------|-------------|
| Pessimistic locking | Requires held locks across service boundaries; unacceptable latency and deadlock risk |
| Last-write-wins | Silently discards updates; unsafe for order state transitions |

## Consequences

- Callers must implement retry logic for 409 responses.
- Version field must be included in all Order read projections.
- Simpler infrastructure — no distributed lock service required.
```
