# Hook Templates

## Config Shape

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "^Bash$",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "timeout": 30,
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_validate.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

Equivalent inline TOML inside `config.toml`:

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"
[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"
```

## PreToolUse: Block Dangerous Commands

```python
#!/usr/bin/env python3
import json, re, sys
payload = json.load(sys.stdin)
command = (payload.get("tool_input") or {}).get("command", "")
dangerous = [r"\brm\s+-rf\s+/", r"\bsudo\b", r"\bchmod\s+-R\s+777\b"]
if payload.get("tool_name") == "Bash" and any(re.search(p, command) for p in dangerous):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "Blocked by policy."}}))
    sys.exit(0)
sys.exit(0)
```

## PermissionRequest: Auto-allow Safe Commands

```python
#!/usr/bin/env python3
import json, sys
payload = json.load(sys.stdin)
command = (payload.get("tool_input") or {}).get("command", "")
safe = ("git status", "git diff", "npm test", "pnpm test")
if any(command.startswith(s) for s in safe):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PermissionRequest", "decision": {"behavior": "allow"}}}))
    sys.exit(0)
sys.exit(0)
```

## Stop: Require Validation After Edits

```python
#!/usr/bin/env python3
import json, re, sys
payload = json.load(sys.stdin)
last = payload.get("last_assistant_message") or ""
edited = re.search(r"\b(updated|modified|changed|edited|implemented)\b", last, re.I)
validated = re.search(r"\b(test|lint|typecheck|validated)\b", last, re.I)
if edited and not validated:
    print(json.dumps({"decision": "block", "reason": "Run or identify the narrowest validation command, then summarize the result."}))
    sys.exit(0)
print(json.dumps({"continue": True}))
sys.exit(0)
```

## SubagentStart: Inject Context

```python
#!/usr/bin/env python3
import json, sys
payload = json.load(sys.stdin)
if payload.get("agent_type") == "reviewer":
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SubagentStart", "additionalContext": "Prioritize data loss and auth bypass. Do not report style-only issues."}}))
sys.exit(0)
```

## Hook Events

| Event | When it runs |
|-------|-------------|
| `SessionStart` | Session starts, resumes, clears, compacts |
| `PreToolUse` | Before Bash, apply_patch, MCP tools |
| `PermissionRequest` | Before approval prompt |
| `PostToolUse` | After supported tools produce output |
| `UserPromptSubmit` | When user prompt is about to be sent |
| `SubagentStart` | When a subagent starts |
| `SubagentStop` | When a subagent is about to stop |
| `Stop` | When main turn is about to stop |

## Trust Model

- Hooks are enabled by default.
- Non-managed command hooks must be reviewed and trusted before running.
- Codex records trust against the hook's hash.
- Changed hooks are marked for review and skipped until trusted again.
- Disable globally with `[features] hooks = false`.
