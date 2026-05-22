# Google Drive Connector Spec

Status: optional integration.

## Use For

Finding and reading documents, sheets, and slides selected by the user.

## Permissions

May require read files and optional create/update.

## Default Safety Mode

Read-only initially.

## Setup

Connect Drive in the chosen runtime and limit folders when possible.

## Disable

Revoke provider access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not share, move, delete, rename, or edit files without explicit approval.
