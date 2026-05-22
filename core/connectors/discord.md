# Discord Connector Spec

Status: optional integration.

## Use For

Selected community or team context and manual relay.

## Permissions

May require selected server/channel access. Posting or delivery must be separately verified in the target runtime.

## Default Safety Mode

Manual relay or draft only.

## Setup

Connect selected servers or channels only. Verify access policy before use.

## Disable

Revoke access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not post, message, auto-submit terminal input, or change access policy without explicit approval and runtime verification.
