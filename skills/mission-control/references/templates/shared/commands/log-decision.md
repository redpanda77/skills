---
description: Record a key decision, deviation, or scope change to the session log. Run before making any change that deviates from the design docs or task plan.
argument-hint: "What changed and why — e.g. 'switching AOV metric from basket_amount to net_basket_amount_with_tax because it excludes discounts'"
---

Log a decision or deviation. $ARGUMENTS is the decision text.

## Steps

1. **Validate argument.** If $ARGUMENTS is empty, ask the user: "What decision should I log?"

2. **Read `.mission-control/state.json`.** Get `current_task` and `current_phase`.

3. **Append to `.mission-control/session-log/log.md`:**
   ```markdown
   ## [ISO timestamp] — [current_task]

   **Decision:** [ARGUMENTS]

   Phase: [current_phase]
   Task: [current_task] — [task name from PLAN.md]
   ```

4. **If the decision affects methodology, personas, dimensions, or process:**
   Tell the user: "This change may affect the operating manual skill. Consider updating `.claude/skills/[skill-name]/SKILL.md` to keep it in sync."

5. **If the decision invalidates completed tasks:**
   Tell the user: "If this change invalidates closed tasks, those tasks should be re-opened in `state.json` and their stale outputs removed before proceeding."

6. **Confirm.** Print: "Decision logged to `.mission-control/session-log/log.md`."

## Note

This command must be run **before** making the change, not after. The log is the audit trail — logging after the fact defeats the purpose.
