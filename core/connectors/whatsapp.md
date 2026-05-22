# WhatsApp Connector Spec

Status: optional integration, disabled by default.

## Use For

Manual import of selected conversation exports.

## Permissions

User-provided export files only in the public starter.

## Default Safety Mode

Manual import/read-only only.

## Setup

Place selected exports in an ignored local inbox. Do not use browser or desktop app automation.

## Disable

Remove the bridge and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not send, reply, react, forward, delete, or use send-capable tokens.
