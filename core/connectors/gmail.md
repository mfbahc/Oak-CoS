# Gmail Connector Spec

Status: optional integration.

## Use For

Inbox triage, follow-up review, and draft replies.

## Permissions

May require read mail, create drafts, and optional send.

## Default Safety Mode

Read/manage/draft only. No-send by default.

## Setup

Connect Gmail in the chosen runtime, confirm scopes, record account identity, restart or refresh after browser auth, and test read-only triage first.

Email connectors may expose message bodies without attachment files. Save important attachments to Drive or another readable source before ingestion.

## Disable

Revoke provider access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not send, reply, forward, archive, label, delete, or move messages without explicit approval. Use technical no-send or deny guardrails where supported.
