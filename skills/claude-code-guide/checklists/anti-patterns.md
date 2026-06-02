# Anti-patterns

## Kitchen-sink agent

**Symptom:** one agent “does everything” with all tools and a vague description.

**Fix:** split by **role** + **tool policy**; narrow `description`.

## Novel-length `description`

**Symptom:** description duplicates entire body prompt.

**Fix:** router text ≤ ~3–5 sentences with triggers + output contract; move detail to body.

## Reviewer with write tools

**Symptom:** reviewer can `Edit` “to fix issues” without explicit user ask.

**Fix:** read-only tool set unless the user wants an implementer.

## `PreToolUse` + `"*"` in agent hooks

**Symptom:** slow, noisy, brittle guardrails on every tool call.

**Fix:** tighten matchers (`Bash`, `Write|Edit`, specific MCP tools).

## Preloading every skill “just in case”

**Symptom:** huge context, slow starts, conflicting guidance.

**Fix:** preload **only** conventions the role always needs; leave the rest discoverable.

## Chaining through subagents

**Symptom:** expecting subagent A to spawn subagent B.

**Fix:** chain from **main** or collapse into one agent with clearer steps.

## Using agents for deterministic CI policy

**Symptom:** “always block X” implemented only inside an agent prompt.

**Fix:** use **hooks** or CI; agents are probabilistic workers.

## Ignoring plugin limitations

**Symptom:** `hooks` / `mcpServers` silently missing on plugin agents.

**Fix:** copy to `.claude/agents/` or adjust session permissions consciously.
