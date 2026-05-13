# active.md Format

```markdown
# Active Feature

feature: [feature-name or "none"]
status: [in-progress | blocked | review]
current-task: [TASK-NNN or "none"]
last-session: [YYYY-MM-DD]

# Queued
- [next-feature]
- [another-feature]
```

- `feature` is the folder name under `.plan/features/`
- Leave `feature: none` and `current-task: none` until the first feature is created
- Queued features are listed in priority order — top one activates when current feature is archived
