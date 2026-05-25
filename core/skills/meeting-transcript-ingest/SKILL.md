---
name: meeting-transcript-ingest
description: Ingest meeting transcripts into raw artifacts, structured notes, follow-ups, and optional external-ready summaries.
---

# Meeting Transcript Ingest

Treat transcripts as private local context unless the user explicitly asks for an external-ready summary.

## Source Order

1. Use the transcript source the user named or attached.
2. If the user says to use a local cache or local transcript store, use that source before connector summaries.
3. If both raw transcript and AI summary exist, preserve the raw transcript and treat the summary as secondary context.
4. If the transcript source is incomplete, say what is missing and continue only if there is enough source-grounded content.

## Read, Draft, Write Ladder

1. Read or preserve the source transcript and any authorized read-only context.
2. Draft structured notes and proposed durable updates.
3. Write local notes, tasks, or wiki updates only when the user has authorized routine ingestion or approves the proposed updates.
4. Create or send external-ready notes only when the user asks for that exact output.

## Standard Procedure

1. Save or link the raw source under an appropriate private artifact folder.
2. Preserve source metadata: meeting title, date, participants if known, source path/link, and attribution caveats.
3. Extract:
   - decisions
   - commitments
   - open questions
   - risks
   - follow-ups with owner/date when stated
   - facts that should update project or domain memory
4. Propose durable updates before writing them unless the user has already authorized routine ingestion.
5. Update the relevant private notes/tasks/wiki only after authorization or established local routine rules.
6. Refresh local search/QMD after meaningful durable writes.

## External-Ready Notes

Create external-ready notes only when the user asks. Remove internal provenance such as private tooling, local cache details, and assistant workflow notes. Keep claims grounded in the transcript and distinguish facts, decisions, next steps, and open questions.

## Stop When

- the raw source is preserved or linked;
- structured notes exist;
- proposed or authorized durable updates are complete;
- follow-ups are captured;
- local search is refreshed or the refresh failure is logged.
