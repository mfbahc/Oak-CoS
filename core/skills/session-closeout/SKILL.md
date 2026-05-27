---
name: session-closeout
description: Wind down a session into durable local state so the next Oak session can restart cleanly.
---

# Session Closeout

Use when the user says "wind down," "update logs," "close out," "going to bed," or asks to prepare the next session.

## Procedure

1. Use the current thread as the primary source for the day's live decisions and user-confirmed actions.
2. Reconcile only today's work:
   - completed, new, stale, blocked, or waiting tasks;
   - decisions, approvals, and user-confirmed sends/actions;
   - artifacts created or delivered;
   - transcripts or source material ingested;
   - items that should not resurface.
3. Update only the narrow local files needed:
   - `workspace/tasks.md`
   - `workspace/observations/YYYY-MM-DD.md`
   - relevant project/domain/wiki notes
   - `workspace/context/current-actions.md` for live sign / check / flag / wait items
4. Write a compact closeout note under `workspace/artifacts/session-closeouts/` or the user's chosen local session folder.
5. Keep `current-actions.md` short. Add only items the user might otherwise lose track of: documents to sign, checks with colleagues, issues to flag, approvals/invoices to draft, and waiting states that affect meetings or decisions. Remove closed rows quickly.
6. Refresh local search/QMD after meaningful durable writes.

## Guardrails

- No broad inbox or file scans unless needed to resolve a specific conflict.
- No external sends, drafts, posts, calendar edits, file shares, or browser submissions.
- Keep closeout factual. It is state, not a transcript.

Stop when a new Oak session can start from durable local state without the old chat.
