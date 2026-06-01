# Automation Configuration

**When to read this:** When setting up a new vault, or when you want to change what automation does automatically. This is the configuration reference for the automation system.

## Where configuration lives

Automation settings are stored in `system/VAULT.md` under the `Automation Rules` section. Every agent reads `system/VAULT.md` before every operation, so these settings are always current.

```yaml
## Automation Rules
- Auto-process unambiguous Raw notes: enabled
- Context pack size: max 30 notes
- Auto-link suggestions: enabled
- Archive after: status=Archived or >1 year old
- Health check schedule: weekly
- Summary generation schedule: daily
- Raw stale threshold: 30 days
- Subagent threshold: 5 notes
- Auto-process confidence: high
```

## Configuration Schema

### Core Switches

| Setting | Default | Values | What It Controls |
|---------|---------|--------|----------------|
| `auto-process` | `enabled` | `enabled` / `disabled` | Whether unambiguous Raw notes are processed automatically |
| `auto-link-suggestions` | `enabled` | `enabled` / `disabled` | Whether the agent suggests related notes when creating a new note |
| `health-check-schedule` | `weekly` | `daily` / `weekly` / `manual` | How often health checks run automatically |
| `summary-generation-schedule` | `daily` | `daily` / `weekly` / `manual` | How often summaries are generated automatically |

### Thresholds and Limits

| Setting | Default | Range | What It Controls |
|---------|---------|-------|----------------|
| `context-pack-max` | `30` | `10-50` | Maximum notes in a context pack |
| `subagent-threshold` | `5` | `1-20` | Batch size above which a subagent is invoked |
| `raw-stale-threshold` | `30` | `7-90` | Days after which unprocessed Raw is flagged as stale |
| `auto-process-confidence` | `high` | `high` / `medium` | How confident the agent must be to auto-process (high = stricter, medium = more permissive) |

### Confidence Levels

| Level | What Auto-Processes | What Requires Human |
|-------|-------------------|-------------------|
| **High** | Clear category, clear destination, all required fields inferable, no contradictions | Anything ambiguous, voice memos, screenshots, confidential material |
| **Medium** | Clear category, likely destination, most fields inferable | Contradictions, multiple plausible destinations, missing critical fields |

## How to Change Configuration

1. Edit `system/VAULT.md` in the `Automation Rules` section.
2. The agent reads this before every operation — changes take effect immediately.
3. Record the change in `logs/maintenance-log.md`:

```markdown
## YYYY-MM-DD
### Automation Config Changed
- Changed `auto-process` from `enabled` to `disabled`
- Changed `health-check-schedule` from `weekly` to `manual`
```

## What Happens When a Setting Is Missing

If `system/VAULT.md` is missing or the `Automation Rules` section is absent, the agent uses **defaults** for all settings. It does not ask the user to configure automation before proceeding.

| Setting Missing | Behavior |
|-----------------|----------|
| `auto-process` missing | Defaults to `enabled` |
| `auto-link-suggestions` missing | Defaults to `enabled` |
| `health-check-schedule` missing | Defaults to `weekly` |
| `summary-generation-schedule` missing | Defaults to `daily` |
| `context-pack-max` missing | Defaults to `30` |
| `subagent-threshold` missing | Defaults to `5` |
| `raw-stale-threshold` missing | Defaults to `30` |
| `auto-process-confidence` missing | Defaults to `high` |

## What Cannot Be Configured

These are hardcoded and never change:

- **Raw notes are immutable.** Even if `auto-process` is enabled, a Processed Raw is never re-edited.
- **Never delete without confirmation.** Even with `auto-process` enabled, the agent never deletes notes.
- **Context packs are mandatory.** Even if `auto-process` is disabled, context packs are always generated for multi-note operations.
- **Audit trail is append-only.** Every automated operation is recorded, regardless of settings.

## Per-Vault vs. Global Settings

All automation settings are **per-vault**, stored in `system/VAULT.md`. There is no global override. If a user has multiple vaults, each has its own automation rules.

## Configuration Verification

After changing automation settings, run a quick verification:

1. Create a test Raw note with clear category and content.
2. Ask the agent to process Raw notes.
3. Verify the behavior matches the setting (auto-processed or held for human).
4. Record the verification result in the maintenance log.
