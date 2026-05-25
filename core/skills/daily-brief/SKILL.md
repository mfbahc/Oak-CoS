---
name: daily-brief
description: Prepare a concise daily brief from local workspace context plus selected read-only connector context such as calendar, Drive, email, transcripts, tasks, project notes, and observations.
---

# Daily Brief

Use QMD/local search before opening files. Include selected read-only connector context when available.

Read only the files needed for today:

- calendar summary or exported agenda
- `workspace/tasks.md`
- relevant project notes
- recent observations

## Source Precedence

When sources conflict, current task status plus latest observations override `workspace/context/` notes and old briefs. Treat older morning briefs, historical exports, and transcripts as evidence, not current state, unless a newer durable note confirms they remain live.

Before listing urgent work, run a contradiction check:

- completed task versus active-context claim;
- user-confirmed or manually sent item versus missing connector evidence;
- old morning brief versus evening note or newer observation;
- stale tracker, reading queue, or board-pack version versus newer source;
- connector result whose sync time is older than the claim.

If the check finds conflict, present it as a "state conflict" with the evidence instead of resurrecting the item as a live task.

Return:

- schedule
- decisions needed
- commitments due
- risks
- suggested focus
- any domain/project reconciliation gaps, such as important context without a matching project file
- optional drafts, clearly marked

Do not send messages, change calendar items, or update durable state unless the user explicitly authorizes it.
