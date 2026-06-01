# Router

The orchestration brain that decides the next legal action.

## Purpose

Prevent agent improvisation. The model runs the router, reads its output, and executes the router's command. The model does not decide the workflow by reasoning.

## What it is

- A deterministic script (`router_core.py`, `curriculum_next.py`) that reads the current state
- Outputs a single command: what to do next, what agent to invoke, what files to read
- The router's output is the current workflow authority

## Router Output Contract

```json
{
  "action": "delegate | validate | repair | render | accept",
  "target": "artifact_id",
  "requires_worker": "agent_name",
  "prompt_path": "path/to/rendered_prompt.md",
  "context_pack_path": "path/to/context_pack.json",
  "can_stop": false,
  "then": "observation_command"
}
```

## Rules

- The router decides exactly one action per invocation
- The model executes exactly one routed action per turn
- The `then` field is an observation/check command, not permission to continue
- The model does not chain multiple router actions in one invocation
- Do not choose work from memory, stale docs, or visible files
- If blocked, run the doctor or repair plan, then follow the next legal action

## Loop Risk

If the router would re-delegate the same worker with unchanged upstream files, classify it as `loop_risk` and escalate to Escape Protocol instead of repeating the worker. The hook blocks `loop_risk` re-delegation.

## Commit Reset Boundary

After a canonical unit commit succeeds, the system should refresh compact state, record the latest state path and next router command, then stop. The next unit starts in a fresh interactive context.

## Skip Closed, Select Next Unfinished

When a scope closes, normal continuation must skip it and select the next unfinished scope through the start router. The closed scope is immutable unless explicitly reopened.

## Failure Mode

If the router is broken:
- Agents wander, skip steps, or loop
- The same failing action is repeated with unchanged inputs
- Off-route work happens without authority
- The pipeline stalls with no legal next action

## The Doctor

When the router cannot find a legal next action and the state is not a simple `loop_risk`, the Doctor is the diagnostic script that identifies the root cause and prescribes the repair layer.

The Doctor is not a repair worker. It diagnoses only. The router decides what to do with the diagnosis.

Doctor output:
```json
{
  "diagnosis": "stale_state | missing_manifest | corrupted_ledger | control_mismatch",
  "affected_targets": ["U001", "S003"],
  "prescribed_layer": "router | state | validator | renderer | prompt",
  "repair_hint": "Run refresh script, then re-run router"
}
```

Rules:
- The Doctor is deterministic, not a subagent
- The Doctor runs only when the router reports `no_legal_action`
- The Doctor does not modify state; it reads state and produces a diagnosis
- The router routes the repair based on the Doctor's prescribed layer

## Repair Authority

- Bad routing logic → router script repair
- Missing artifact detection → deterministic refresh
- Stale state → run refresh script, then re-run router
- No dead-end state: every blocked state must have one legal next route or a concise blocker report
- Blocked with no legal action → run Doctor, then route to prescribed layer
