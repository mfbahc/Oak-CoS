# Synthetic Transcript Ingest

This example is synthetic. It shows the expected output shape after ingesting a meeting transcript.

## Source

- Meeting: Example Strategy Call
- Date: 2026-01-12
- Source: `workspace/artifacts/example-strategy/2026-01-12/raw-transcript.txt`
- Caveat: Transcript text may contain speaker attribution errors.

## Decisions

- Use a narrow pilot before expanding the workflow to all teams.
- Keep the initial data import read-only until access controls are confirmed.

## Commitments

| Owner | Commitment | Due |
| --- | --- | --- |
| Alex | Draft the pilot access request. | 2026-01-14 |
| Jordan | Confirm which source systems are in scope. | 2026-01-15 |

## Open Questions

- Which workspace should be treated as the source of truth during the pilot?
- Who approves external sharing once the summary is ready?

## Proposed Durable Updates

- Add a task for the pilot access request.
- Update the project page with the read-only access constraint.
- Refresh local search after the updates are written.
