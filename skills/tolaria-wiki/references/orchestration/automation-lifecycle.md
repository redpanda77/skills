# Automation Lifecycle

**When to read this:** When you want to understand when automation runs, how it starts and stops, what triggers it, and how it handles errors. This is the operational reference for the automation system.

## The Three Trigger Types

Automation can be triggered in three ways:

| Trigger Type | How It Happens | Examples |
|--------------|----------------|----------|
| **Explicit** | User asks directly | "Process my raw notes", "Generate today's summary", "Check vault health" |
| **Implicit** | Agent runs it automatically during another workflow | Session start deterministic refresh, pre-authoring Raw check, post-import auto-process |
| **Scheduled** | Recurring automation runs on a schedule | Weekly health check, daily summary generation |

## Explicit Triggers

### User Says: "Process my raw notes"

```
Agent:
1. Load system/VAULT.md (check auto-process setting)
2. List all unprocessed Raw notes
3. If auto-process is enabled:
   a. Auto-process unambiguous notes
   b. Hold ambiguous notes for human
4. If auto-process is disabled:
   a. List all unprocessed Raw notes
   b. Ask user which to process
5. Report: processed N, held M, skipped K
6. Record in maintenance log
```

### User Says: "Generate today's summary"

```
Agent:
1. Load system/VAULT.md (check summary-generation-schedule)
2. Check if summary already exists
3. If exists → check freshness
4. If fresh → report "Summary is fresh"
5. If stale or missing → generate context pack → generate summary
6. Record in maintenance log
```

### User Says: "Check vault health"

```
Agent:
1. Load system/VAULT.md (check health-check-schedule)
2. Run five health checks
3. Report findings with severity
4. Ask user: fix all, fix selected, or just flag?
5. Record in maintenance log
```

## Implicit Triggers

### Session Start Deterministic Refresh

Every time the agent starts a session on a vault:

```
Agent:
1. Check for unprocessed Raw notes
2. If found and auto-process is enabled:
   a. List unprocessed Raw notes
   b. Report: "Found N unprocessed Raw notes. Auto-process enabled."
   c. Process unambiguous notes
   d. Report what was processed and what needs human
3. Check for stale summaries
4. If stale summaries found:
   a. Report: "Found N stale summaries"
   b. Ask user: regenerate or skip?
```

This is the **implicit auto-refresh**. It happens before any user request, but only reports — it does not block the user.

### Pre-Authoring Raw Check

Before creating any new note:

```
Agent:
1. Check if unprocessed Raw notes exist
2. If found → report: "Found N unprocessed Raw notes. Process them first?"
3. If user says yes → process Raw
4. If user says no → proceed with authoring
```

This prevents the inbox from growing while the user creates new structured notes.

### Post-Import Auto-Process

After importing external sources (recordings, transcripts, Slack):

```
Agent:
1. Import external source as Raw note
2. If auto-process is enabled:
   a. Check if the new Raw is unambiguous
   b. If unambiguous → auto-process immediately
   c. Report: "Imported and auto-processed X.md → Y.md"
   d. If ambiguous → report: "Imported X.md. Needs human review."
3. If auto-process is disabled:
   a. Report: "Imported X.md. Added to Raw inbox."
```

## Scheduled Triggers

### Weekly Health Check

Runs automatically based on `health-check-schedule: weekly`:

```
Agent (on first session of the week):
1. Check if health check was run this week
2. If not → run health check
3. Report findings
4. Ask user: fix or flag?
```

### Daily Summary

Runs automatically based on `summary-generation-schedule: daily`:

```
Agent (on first session of the day):
1. Check if daily summary exists for today
2. If not → generate daily summary
3. Display summary to user
4. Persist to summaries/daily-YYYY-MM-DD.md
```

### Detecting Schedule

The agent does not have a persistent scheduler. It detects scheduled events by:

- Checking `logs/maintenance-log.md` for last run date
- Comparing to today's date
- If last run date < today → run the scheduled task

## The Automation Lifecycle

```
[Trigger] → [Load Config] → [Deterministic Refresh] → [Auto-Process] → [Report]
                ↓
          [Check VAULT.md]
                ↓
          [Check for unprocessed Raw]
                ↓
          [Check for stale summaries]
                ↓
          [Execute main workflow]
                ↓
          [Record in audit trail]
                ↓
          [Report to user]
```

### Start

Automation starts when a trigger fires. The agent:
1. Reads `system/VAULT.md` for configuration
2. Reads the relevant skill reference for the workflow
3. Generates a context pack

### Run

During execution:
1. Deterministic steps run automatically (listing, checking, indexing)
2. Qualitative steps stop and ask (classifying, deciding, summarizing)
3. Subagents are invoked when thresholds are exceeded

### Stop

Automation stops when:
- **Completion**: All work done successfully
- **Ambiguity**: A step requires human judgment
- **Error**: A script fails, a file is missing, a subagent times out
- **Human override**: The user says "stop" or "skip this"
- **Threshold**: Context pack exceeds max size, batch exceeds subagent threshold

### Resume

After stopping, the agent reports what was done and what remains. The user can:
- Continue: "Process the rest" → resume from where it stopped
- Skip: "Skip those" → mark as skipped in maintenance log
- Abort: "Never mind" → record partial completion in maintenance log

## Error Handling

### Context Pack Failure

If the agent cannot generate a context pack (e.g., index is too large, notes are unreadable):

1. Report the failure: "Could not generate context pack for [reason]"
2. Fallback: read the most relevant notes directly (max 5)
3. Record the fallback in maintenance log

### Subagent Timeout

If a subagent does not return within a reasonable time:

1. Report: "Subagent [name] timed out after [time]"
2. Fallback: main agent performs the work directly
3. Record the timeout and fallback in maintenance log

### Ambiguous Note

If a note cannot be classified or its destination is unclear:

1. Add to "needs human" list
2. Provide the reason: "Category is unknown", "Multiple plausible destinations", "Missing required fields"
3. Continue processing other notes
4. Report all "needs human" notes at the end

### Missing VAULT.md

If `system/VAULT.md` is missing:

1. Report: "system/VAULT.md not found. Using default automation settings."
2. Proceed with defaults
3. Suggest: "Create system/VAULT.md to configure automation."

## Recovery Rules

1. **Partial success is success.** If 8 of 10 notes were processed, report success for 8 and flag 2.
2. **Never retry silently.** If a step fails, report it and ask the user.
3. **Never lose work.** Even if automation stops, notes that were processed are recorded.
4. **Always record.** Every run, partial or complete, is recorded in the maintenance log.

## Human Override

The user can override automation at any time:

- **"Don't auto-process this note"** → The agent skips it and records the override
- **"Process everything manually"** → The agent disables auto-process for this session
- **"Stop suggesting links"** → The agent disables auto-link suggestions for this session
- **"Skip the health check"** → The agent skips the scheduled check and records it

Overrides are **session-scoped** by default. To make them persistent, update `system/VAULT.md`.
