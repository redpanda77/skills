# Agent Manifest

The `AGENT_MANIFEST.json` is the canonical registry of all agents. It is the single source of truth for what agents exist, what categories they belong to, what they write, and how they are invoked.

## Why it matters

Without a manifest, agents drift. Files appear in `.claude/agents/` that are not part of the runtime contract. Routers reference agents that do not exist. Hooks authorize writes for agents that are not registered. The manifest prevents this by making every agent explicit.

## Schema

```json
{
  "schema_version": "agent_manifest_v1",
  "categories": {
    "planning_worker": "Model-authored planning worker invoked by the router to produce tier hypotheses and plans.",
    "artifact_worker": "Model-authored artifact worker invoked by the router to produce canonical content units.",
    "repair_worker": "Model-authored repair worker invoked by the router to patch one failed canonical unit.",
    "judge_worker": "Real LLM judge invoked through Claude Code agents; reads one context pack and writes one judgment file.",
    "audit_worker": "Read-only verification or blocked-state analysis worker.",
    "escape_worker": "Write-capable control-layer repair worker used only after Escape Protocol.",
    "deprecated": "Retired stub retained only to reject accidental invocation."
  },
  "agents": [
    {
      "name": "example-worker",
      "category": "artifact_worker",
      "normal_runtime": true,
      "writes": [
        "out/build/canonical/{unit}.json"
      ],
      "router_actions": [
        "delegate_example"
      ],
      "claude_agent": ".claude/agents/example-worker.md",
      "claude_invocation": "@\"example-worker (agent)\""
    }
  ]
}
```

## Top-level fields

| Field | Purpose | Required |
|-------|---------|----------|
| `schema_version` | Manifest format version | Yes |
| `categories` | Human-readable category definitions | Yes |
| `agents` | Array of agent definitions | Yes |

## Agent entry fields

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Unique identifier, matches `subagent_type` | `lesson-repair-worker` |
| `category` | Worker class for scope validation | `repair_worker` |
| `normal_runtime` | Whether this agent is part of the normal pipeline | `true` |
| `writes` | List of paths the agent is allowed to write | `["out/build/canonical/{unit}.json"]` |
| `router_actions` | Router actions that may invoke this agent | `["delegate_lesson_repair"]` |
| `claude_agent` | Path to the agent definition file | `.claude/agents/lesson-repair-worker.md` |
| `claude_invocation` | How to invoke this agent in Claude Code | `@"lesson-repair-worker (agent)"` |
| `note` | Optional note (used for deprecated agents) | `Deprecated. Reject all invocations.` |

## Category definitions

The manifest must define every category used by its agents:

| Category | Description |
|----------|-------------|
| `planning_worker` | Produces plans, grouping, or sequencing hypotheses |
| `artifact_worker` | Produces canonical content units |
| `repair_worker` | Patches one failed canonical unit |
| `judge_worker` | Evaluates quality against principles |
| `audit_worker` | Read-only verification or blocked-state analysis |
| `escape_worker` | Repairs control-layer files only during Escape Protocol |
| `deprecated` | Retired stub, rejects accidental invocation |

## Rules

- If an agent is not in `AGENT_MANIFEST.json`, it is not part of the runtime contract
- The manifest is the canonical registry: routers, hooks, and tests all reference it
- `name` must match the `subagent_type` used in the `Agent` tool invocation
- `category` must match one of the defined categories
- `writes` are the authorized write paths; hooks may use this for boundary enforcement
- `router_actions` are the actions the router may emit to invoke this agent
- `normal_runtime: false` means the agent is only used for audit, escape, or maintenance
- Deprecated agents should have empty `writes` and `router_actions`, with a `note` explaining why

## Using the manifest

### Router

The router reads the manifest to validate that a `requires_worker` value references a real agent:

```python
manifest = load_manifest(".claude/agents/AGENT_MANIFEST.json")
if action["requires_worker"] not in manifest.agent_names:
    raise RouterError(f"Unknown agent: {action['requires_worker']}")
```

### Hooks

Hooks may read the manifest to enforce write boundaries:

```python
agent = manifest.get_agent(subagent_type)
allowed_writes = agent["writes"]
```

### Tests

Tests should verify:

- Every `.claude/agents/*.md` file is listed in the manifest
- Every manifest entry has a corresponding `.md` file
- Every `router_action` in the manifest is referenced by at least one router
- No two agents have the same `name`
- Every agent's `category` is defined in the manifest's `categories` block

## Maintenance

When adding a new agent:

1. Write the agent `.md` file in `.claude/agents/`
2. Add the agent entry to `AGENT_MANIFEST.json`
3. Add the router action to the relevant router script
4. Update the authorization sidecar template if needed
5. Run tests to verify the manifest is consistent

When retiring an agent:

1. Set `normal_runtime` to `false`
2. Clear `writes` and `router_actions`
3. Add a `note` explaining the deprecation
4. Do not delete the agent file until all references are gone

## Rules

- The manifest is the single source of truth for agent inventory
- Every agent must be in the manifest
- Every agent in the manifest must have a `.md` file
- The manifest is not a prompt library — it is a runtime registry
- Changes to the manifest require updating all dependent surfaces (router, hooks, tests)
