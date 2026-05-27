# Operating State

Oak maintains a current operating picture from small durable notes, not from old briefs or complete file scans.

## What Goes Where

| State | Default path | Purpose |
| --- | --- | --- |
| Active tasks and commitments | `workspace/tasks.md` | What is due, waiting, delegated, blocked, or done. |
| Current actions | `workspace/context/current-actions.md` | Live sign / check / flag / wait posture that should not be reconstructed from old chats. |
| Dated observations | `workspace/observations/` | What happened on a date and what changed. |
| Stable knowledge | `workspace/wiki/` | Reusable facts that should survive beyond one day. |
| Project or domain state | `workspace/projects/`, `workspace/domains/` | The current state for a workstream. |
| Active context map | `workspace/context/manifest.md` and optional active notes | A routing map, not permission to expand every file. |
| Artifacts | `workspace/artifacts/` | Drafts, briefs, PDFs, source captures, and outputs. |

## Source Precedence

When sources conflict, use this order:

1. The user's current instruction.
2. Current actions for live sign / check / flag / wait posture.
3. Current task status, latest dated observations, and latest source-backed project or domain notes.
4. Stable wiki pages that have not been superseded.
5. Active context manifests as routing aids.
6. Historical briefs, old morning notes, old exports, and old transcripts as evidence only.

Do not resurrect a completed task just because an older brief or context file still mentions it.

## Contradiction Check

Before surfacing urgent work, check for:

- a completed task conflicting with an active-context claim;
- a user-confirmed or manually sent item that is missing from connector search;
- an old morning brief conflicting with evening notes or newer observations;
- a stale tracker, board pack, or reading-queue version when a newer source exists;
- connector results whose sync time is older than the claim being made.
- an urgent recommendation missing from current actions when it is a live sign / check / flag / wait item.

If there is a conflict, label it as a state conflict and cite the sources instead of presenting it as a live task.

## Read, Draft, Write Ladder

Use the smallest action that solves the problem:

1. Read: inspect local/QMD context and authorized read-only connectors.
2. Draft: produce a proposed brief, email, task update, or state change.
3. Write locally: update durable local state only when the workflow authorizes it or the user approves it.
4. Act externally: send, share, post, invite, archive, label, delete, or edit external systems only after explicit approval for that exact action.

This ladder applies even when a connector is available. Connector access is not approval to act.
