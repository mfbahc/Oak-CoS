# Browser Automation Connector Spec

Status: optional integration, disabled by default.

## Use For

User-approved authenticated web workflows.

## Permissions

May require browser profile or session access.

## Default Safety Mode

Disabled by default.

## Setup

Enable per task, confirm target site, and keep the session observable.

## Disable

Close the session and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not submit forms, purchase, publish, message, or change account settings without explicit approval.
