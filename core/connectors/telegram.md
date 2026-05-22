# Telegram Connector Spec

Status: optional integration, disabled by default.

## Use For

Bot or account-based messaging workflows.

## Permissions

May require bot token or account bridge access.

## Default Safety Mode

Disabled by default.

## Setup

Configure a bot or bridge only for selected chats.

## Disable

Revoke token or bridge access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not send, forward, or export messages without explicit approval.
