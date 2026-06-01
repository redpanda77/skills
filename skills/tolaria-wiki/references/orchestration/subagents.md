# Subagent Invocation

**When to read this:** When deciding whether to invoke a subagent or when configuring subagent thresholds. This is the operational reference for delegation.

## Main Agent vs. Subagent

The main agent (the one talking to the user) can do most work itself. Subagents are used when **isolation, scale, or safety** requires it.

| Factor | Main Agent | Subagent |
|--------|-----------|----------|
| **Context** | Full session context | Forked, isolated context |
| **Vault size** | Any | Large vaults (>100 notes) |
| **Batch size** | 1-5 notes | >5 notes (configurable) |
| **Complexity** | Simple operations | Multi-step diagnostics |
| **Error impact** | Affects main session | Isolated; main session unaffected |
| **Return** | Immediate | Structured report |

## The Three Subagents

| Subagent | Trigger | What It Does | Returns |
|----------|---------|--------------|---------|
| **Health Checker** | "Check vault health" or scheduled | Runs 5 health checks in isolation | Structured markdown report |
| **Raw Processor** | "Process raw notes" with batch > threshold | Processes unambiguous Raw notes | Processed notes + "needs human" list |
| **Summary Generator** | "Generate summary" or scheduled | Generates summaries with bounded context | Summary content + source_evidence |

## When to Invoke a Subagent

### Always Invoke Subagent

These operations **always** use a subagent:

- **Health checks on vaults >100 notes** — orphan detection requires reading the entire vault index
- **Batch processing >5 Raw notes** — prevents context overflow in the main agent
- **Topic summaries spanning >20 notes** — context pack is too large for main agent
- **Any operation the user explicitly requests to run "in the background"** — user wants to continue talking while work happens

### Main Agent Does It Directly

These operations **never** use a subagent:

- **Single note creation** — simple, bounded, immediate
- **Single Raw processing** — one file, one destination, quick
- **Quick health check** — vault <50 notes, just checking for dead links
- **Freshness check** — reading hashes, comparing, reporting
- **Any user request starting with "Quick" or "Can you just"** — user wants immediate response

### Threshold-Based Decision

For everything else, use the `subagent-threshold` setting in `system/VAULT.md`:

```
If (batch_size > subagent-threshold):
  → Invoke subagent
Else:
  → Main agent handles it
```

| Batch Size | Subagent? | Example |
|-----------|-----------|---------|
| 1-2 notes | No | "Process Raw/meeting.md" |
| 3-5 notes | Configurable | "Process all raw notes" (if threshold=5, main agent handles) |
| 6-20 notes | Yes | "Process all raw notes" (if threshold=5, subagent handles) |
| 20+ notes | Yes | "Process all raw notes from last month" |

## Invocation Procedure

### How to Invoke a Subagent

```
1. Load system/VAULT.md for configuration
2. Determine if subagent is needed (threshold check)
3. If yes:
   a. Prepare input: vault path, specific files, date range, topic
   b. Spawn subagent with `skills: [tolaria-wiki]` and `context: fork`
   c. Provide the prepared input
   d. Wait for subagent to return
   e. Receive structured output
4. If no:
   a. Main agent performs the work directly
   b. Report results immediately
```

### Subagent Input Contract

Every subagent receives:

```yaml
---
vault_path: "/path/to/vault"
operation: "health-check" | "raw-process" | "summary-generate"
parameters:
  # Operation-specific parameters
---
```

Examples:

**Health Checker Input:**
```yaml
vault_path: "/Users/me/Documents/Wiki"
operation: "health-check"
parameters:
  checks: ["orphans", "dead-links", "stale-raw", "empty-notes", "missing-fields"]
```

**Raw Processor Input:**
```yaml
vault_path: "/Users/me/Documents/Wiki"
operation: "raw-process"
parameters:
  files: ["Raw/2026-05-11-meeting.md", "Raw/2026-05-12-slack.md"]
  auto_process: true
  confidence: "high"
```

**Summary Generator Input:**
```yaml
vault_path: "/Users/me/Documents/Wiki"
operation: "summary-generate"
parameters:
  type: "daily"
  date: "2026-05-11"
```

### Subagent Output Contract

Every subagent returns a structured report:

```markdown
## Subagent Report: [Operation Name]

### Status
Completed | Partial | Failed

### Results
[Structured results specific to the operation]

### Findings
- [Finding 1]
- [Finding 2]

### Maintenance Log Entries
```markdown
## YYYY-MM-DD
### [Operation]
- [Entry 1]
- [Entry 2]
```

### Notes for Human
[Anything the subagent couldn't resolve or that needs human attention]
```

## Subagent Return Contract

After a subagent returns, the main agent:

1. **Reads the report** — structured output from subagent
2. **Presents findings to user** — summary of what the subagent found/did
3. **Asks for decisions** — if the subagent flagged items for human review
4. **Appends maintenance log entries** — if the subagent provided them
5. **Records the subagent invocation** — in maintenance log for audit

### Health Checker Return

```
Main agent receives:
- Health report with counts and severity
- Suggested fixes for each finding

Main agent does:
- Presents report to user
- Asks: "Fix all, fix selected, or just flag?"
- Records findings in maintenance log after user decides
```

### Raw Processor Return

```
Main agent receives:
- List of processed notes (paths)
- List of "needs human" notes with reasons
- Maintenance log entries to append

Main agent does:
- Reports processed notes
- Presents "needs human" notes to user
- Asks for decisions on ambiguous notes
- Appends maintenance log entries
```

### Summary Generator Return

```
Main agent receives:
- Summary content (full markdown)
- source_evidence block with hashes
- Context pack record

Main agent does:
- Displays summary to user
- Persists summary to summaries/
- Records in maintenance log
```

## Isolation Rules

Subagents run with `context: fork` for isolation:

1. **No shared state** — subagent cannot see the main agent's context
2. **No shared memory** — subagent must receive all input explicitly
3. **Bounded access** — subagent reads only the vault path provided
4. **Deterministic output** — subagent returns structured reports, not conversational responses

## Error Handling in Subagents

If a subagent fails:

1. **Report failure** — "Subagent [name] failed: [reason]"
2. **Fallback to main agent** — main agent attempts the work directly
3. **Record fallback** — note that subagent failed and main agent took over
4. **Continue** — do not block the session; report and continue

Common failure modes:

| Failure | Fallback |
|---------|----------|
| Subagent timeout | Main agent processes smaller batch |
| Subagent returns malformed output | Main agent re-reads the vault and performs the check |
| Subagent exceeds context limit | Main agent splits the work into smaller chunks |

## Configuration

Subagent invocation is controlled by `system/VAULT.md`:

```yaml
## Subagent Rules
- Subagent threshold: 5 notes
- Always use subagent for health checks: true
- Always use subagent for batch processing: true
- Always use subagent for summary generation: true
```

## Subagent Performance

| Subagent | Typical Time | Notes |
|----------|-------------|-------|
| Health Checker | 10-30s | Depends on vault size |
| Raw Processor | 5-15s per note | Faster for unambiguous notes |
| Summary Generator | 15-45s | Depends on context pack size |

If a subagent is taking longer than expected, the main agent should:
1. Report: "Subagent is still working..."
2. Offer: "Would you like me to continue, or cancel and try a smaller batch?"
