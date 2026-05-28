# Agent Templates

## Minimal Agent

```toml
name = "reviewer"
description = "Read-only PR reviewer."
developer_instructions = """
Review code for correctness. Do not edit files.
"""
```

## Full Agent

```toml
name = "reviewer"
description = "Read-only PR reviewer for correctness, security, regressions, and missing tests."
model = "gpt-5.4"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
nickname_candidates = ["Atlas", "Delta", "Echo"]
developer_instructions = """
Review like a senior maintainer.
Scope: correctness, security, regressions, missing tests.
Rules:
- Do not edit files.
- Return findings by severity.
"""
```

## With MCP

```toml
name = "docs_researcher"
description = "Read-only documentation researcher."
model = "gpt-5.4-mini"
sandbox_mode = "read-only"
developer_instructions = """
Use docs tools to verify APIs. Return concise answers.
"""
[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"
```

## Global Settings

```toml
[agents]
max_threads = 6
max_depth = 1
job_max_runtime_seconds = 1800
[features]
hooks = true
```

## Sandbox Modes

| Mode | Use Case |
|------|----------|
| `read-only` | Exploration, review, research |
| `workspace-write` | Implementation, bug fixes |
| `network` | External API calls |

## Recommended Patterns

- Exploration agents: `sandbox_mode = "read-only"`
- Implementation agents: `sandbox_mode = "workspace-write"`
- Avoid giving all agents write access by default.
