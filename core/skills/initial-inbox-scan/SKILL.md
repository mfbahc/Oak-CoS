---
name: initial-inbox-scan
description: Use for a read-only first inbox scan that suggests Oak domains/projects and can learn a local writing style profile from opt-in sent-email sampling.
---

# Initial Inbox Scan

Use this when the user runs initial email triage or asks Oak to inspect inbox context.

## Default Mode

Read-only and local-only.

## What It Can Do

- triage recent inbox themes
- suggest Oak domains or projects
- identify recurring people, topics, waiting items, and commitments
- draft local setup suggestions
- ask whether the user wants Oak to learn writing style from sent emails
- review sent emails inside the chosen mailbox/date/account scope
- write a proposed local writing style profile under `workspace/`

## Writing Style Profile

Writing style means how the user writes.

When the user opts in, sample sent emails in batches until the profile is stable enough to draft from. No per-message approval is needed inside the chosen scope. If the profile remains uncertain, ask whether to widen the scope.

Separate at least two modes:

- casual writing for friends, close colleagues, quick replies, and lightweight follow-ups
- formal writing for customers, executives, investors, board/advisory contacts, legal/compliance, or high-stakes threads

For each mode, look for:

- greeting and sign-off patterns
- sentence length
- directness
- formality
- common phrases
- level of detail
- follow-up style
- how the user says no, asks for decisions, and closes loops

Store any profile locally. Do not copy private email content into public files.

## Never Without Send Approval

Do not send or change email state unless the user explicitly approves the exact action.

- send, reply, forward, archive, delete, label, or move email
- mark messages read or unread
- inspect all mailboxes broadly
- learn from sent mail unless the user opted into writing-style sampling
- sample outside the stated mailbox/date/account scope
- copy private email content into public files

## Output

Return:

- sources or scopes reviewed
- suggested domains/projects
- recurring commitments or waiting items
- draft writing style profile with casual and formal patterns separated
- recommended next local files to create
- blockers or permissions still needed
