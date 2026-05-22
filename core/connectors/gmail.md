# Gmail Connector Spec

Status: optional integration.

## Use For

Inbox triage, follow-up review, and draft replies.

## Permissions

May require read mail, create drafts, and optional send.

## Default Safety Mode

Read/draft only.

## Setup

Connect Gmail in the chosen runtime, confirm scopes, and test read-only triage first.

## Disable

Revoke provider access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not send, archive, label, delete, or forward messages without explicit approval.
