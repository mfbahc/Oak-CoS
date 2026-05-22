# Connectors

Connectors are optional ways for Oak to work with outside accounts or tools. You do not need any connector on day one.

Default rule: no emails, messages, calendar invites, file shares, posts, browser submissions, or external updates unless the user explicitly asks Oak to take that exact action.

## Day 1

Use local files only:

- run onboarding
- run QMD/local search setup
- generate the synthetic demo brief
- add private notes under `workspace/`
- leave Gmail, Calendar, Drive, Slack, Granola, browser automation, and messaging bridges disconnected

## Later

When local Oak feels useful, consider adding one connector at a time:

- Calendar for schedule review and meeting prep
- Gmail for inbox triage and draft replies
- Drive for selected documents, sheets, and slides
- Granola for transcript import
- Slack for team context and draft replies

Start in read-only or draft-only mode.

## Advanced

Use these only after you understand the safety rules:

- browser automation
- WhatsApp or Telegram bridges
- Discord posting workflows
- scheduled jobs or crons
- connector writes or sends

Scheduled jobs should write local artifacts only unless you explicitly enable a specific external delivery action.

## Three Separate States

These are different:

- Documented: Oak includes setup instructions for the connector.
- Selected in config: onboarding wrote a preference into `local/connectors.toml`.
- Actually connected in the runtime: you granted access in Codex, Claude, or another tool.

A connector is not active just because it is documented or selected in config.

## Capability Table

| Connector | Stage | Enables | Permissions it may require | Default safety mode | Setup | Opt out or disable |
| --- | --- | --- | --- | --- | --- | --- |
| QMD/local search | Day 1 | private local search | local file index | enabled locally | run `./scripts/qmd-setup` | remove `.oak/qmd/` |
| Local filesystem | Day 1 | selected private folders and artifacts | folder access | selected folders only | choose folders explicitly | remove folder from config |
| Google Calendar | Later | agenda review, holds, reminders, meeting prep | read events, optional create/update | read/draft only | connect calendar, confirm calendar list | revoke access and disable in local config |
| Gmail | Later | inbox triage, draft replies, follow-up review | read mail, create drafts, optional send | read/draft only | connect account in chosen runtime, confirm scopes | remove connector access and set `enabled = false` |
| Google Drive | Later | retrieve docs, sheets, slides, briefs | read files, optional create/update | read-only initially | connect Drive, restrict folders when possible | revoke access and disable |
| Granola | Later | transcript ingestion and meeting notes | read/export transcripts | manual import initially | export or connect with explicit consent | stop imports and remove tokens |
| Slack | Later | team context, drafts, thread summaries | read channels/DMs, optional send | read/draft only | connect workspace, limit channels | revoke app access and disable |
| GitHub | Later | issues, PRs, code context | read repos, optional write | read-only initially | connect GitHub, choose repos | revoke token and disable |
| Linear | Later | product/project tracking | read workspace, optional write | read-only initially | connect Linear, choose team | revoke access and disable |
| Discord | Advanced | community/team coordination | read channels, optional send | read/draft only | connect selected servers/channels | revoke access and disable |
| Browser automation | Advanced | authenticated web workflows | browser/session access | disabled by default | enable per task, confirm target | close session and disable |
| WhatsApp | Advanced | personal/team messaging | message bridge access | disabled by default | configure bridge only if needed | remove bridge and disable |
| Telegram | Advanced | personal/team messaging | bot or account bridge access | disabled by default | configure bridge only if needed | revoke token and disable |

## Setup Principles

- Add one connector at a time.
- Prefer limited scopes and selected folders/channels/calendars.
- Keep credentials out of the repo.
- Store machine-specific settings in `local/`.
- Test read-only behavior before enabling writes.
- Revoke provider access when you disable a connector.

## External Actions

When a task might contact another person or publish anything, Oak should stop and ask for confirmation with:

- exact action
- recipient or destination
- content
- connector or tool

If those details are missing, Oak should draft locally instead of sending.
