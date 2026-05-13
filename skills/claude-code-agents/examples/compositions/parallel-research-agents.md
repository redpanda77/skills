# Composition: parallel research agents

**Intent:** split independent questions so each agent returns a tight summary; parent synthesizes.

## Example prompt pattern

> Research authentication, billing, and notifications **in parallel** using separate subagents. Each should return at most 15 bullets and the top 8 file paths.

## Guardrails

- Ensure paths are **disjoint** enough to avoid duplicated heavy reads.
- Cap verbosity per agent (`maxTurns`, prompt caps).
- Remember: many large summaries can still **bloat the parent** — require structured, bounded responses.

Official pattern: [Run parallel research](https://code.claude.com/docs/en/sub-agents#run-parallel-research).
