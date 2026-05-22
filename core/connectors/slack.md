# Slack Connector Spec

Status: optional integration.

## Use For

Team context, thread summaries, notification triage, and draft replies.

## Permissions

May require channel or DM read access and optional send.

## Default Safety Mode

Read/draft only.

## Setup

Connect the workspace, limit channels, and test read-only summaries first.

## Disable

Revoke app access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not post, react, invite, archive, or message anyone without explicit approval.
