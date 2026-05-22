# Google Calendar Connector Spec

Status: optional integration.

## Use For

Agenda review, meeting prep, reminders, and proposed holds.

## Permissions

May require read events and optional create/update.

## Default Safety Mode

Read/draft only.

## Setup

Connect Calendar in the chosen runtime, choose calendars, and test read-only agenda review.

## Disable

Revoke provider access and set `enabled = false` in `local/connectors.toml`.

## Never Without Approval

Do not create, update, cancel, or invite anyone without explicit approval.
