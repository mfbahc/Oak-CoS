# Connectors

Connectors are recommended ways for Oak to work with the context you already use: calendar events, email, files, transcripts, team messages, and local notes. Every connector is opt-in and skippable.

Default rule: no emails, messages, calendar invites, file shares, posts, browser submissions, or external updates unless the user explicitly asks Oak to take that exact action.

## Recommended Onboarding

For the full Oak experience, set up or document these during onboarding:

- QMD/local search for private local memory
- Calendar for schedule review and meeting prep
- Gmail or email for inbox triage, follow-ups, and draft replies
- Drive for selected documents, sheets, slides, and briefs
- Granola or transcript import for meeting notes
- Slack for team context, summaries, and drafts

Start in read-only or draft-only mode. If a user skips a connector, Oak should still create a useful local workspace and make it easy to add the connector later.

## Day 1 With Or Without Connectors

Day 1 can include Google Drive, Calendar, Gmail/email, transcripts, Slack, and QMD/local search if the user grants access in the runtime.

If the user is not ready to grant access, use local files only:

- run onboarding
- run QMD/local search setup
- create the first domain or project
- add private notes under `workspace/`
- leave outside accounts disconnected until the user chooses otherwise

## Advanced

Use these only after you understand the safety rules:

- browser automation
- WhatsApp or Telegram bridges
- Discord posting workflows
- scheduled jobs or crons, after choosing an always-on host
- connector writes or sends

Scheduled jobs should write local artifacts only unless you explicitly enable a specific external delivery action. They also need an awake, online host; laptops that sleep or shut down should use manual/on-demand routines unless an always-on device or hosted scheduler is configured.

## Three Separate States

These are different:

- Documented: Oak includes setup instructions for the connector.
- Selected in config: onboarding wrote a preference into `local/connectors.toml`.
- Actually connected in the runtime: you granted access in Codex, Claude, or another tool.

A connector is not active just because it is documented or selected in config.

## Verify The Runtime Surface

Connector state is runtime-specific. Codex App, Codex CLI, Claude CLI, Claude Desktop, cloud routines, local scheduled jobs, and hosted runners may not share the same connector surface.

After web OAuth or browser-based authorization, restart or refresh the runtime before relying on the connector. Then verify actual availability in the target runtime with one of:

- the runtime's connector list or MCP list
- a read-only smoke request
- the provider's connected-apps page plus a same-runtime test

Do not write "connected" into durable state until the runtime that will use the connector has been checked. If a connector is selected but not verified, record it as "selected, verification pending."

## Connector-Backed Prepopulation

When read-only connectors are verified, Oak may use email, calendar, Drive, transcripts, Slack, or local search to infer candidate domains/projects. Treat the inferred structure as a draft. The user must be able to rename, remove, add, and correct domains before Oak writes local project/domain files.

If a connector is unavailable, skipped, or stale, fall back to conversational intake and local files.

## Email Identity And Attachments

Email setup must record account identity, allowed read/manage actions, prohibited outbound actions, and technical no-send guardrails where the runtime supports them. Prompt instructions are not enough if a send-capable tool exists.

Email connectors may expose message bodies but not attachments. If a message references an attachment Oak cannot see, save the file to Drive or another readable source, or place it in a local workspace folder before ingestion.

## Delivery Channels

Verify delivery before promising it. Email may only support drafts in some runtimes. Slack or Drive may be better supported. Discord and personal messaging apps may require manual relay or runtime-specific verification. If delivery cannot be verified, write a local artifact and report the limitation.

## Messaging Apps

Telegram and WhatsApp are manual-import/read-only only in the public starter. Do not use browser automation, desktop app automation, or send-capable tokens to read personal messaging. A future one-way bridge must expose no send, reply, forward, react, delete, or mutation endpoint.

## Capability Table

| Connector | Stage | Enables | Permissions it may require | Default safety mode | Setup | Opt out or disable |
| --- | --- | --- | --- | --- | --- | --- |
| QMD/local search | Recommended onboarding | private local search | local file index | enabled locally | run `./scripts/qmd-setup` | remove `.oak/qmd/` |
| Local filesystem | Recommended onboarding | selected private folders and artifacts | folder access | selected folders only | choose folders explicitly | remove folder from config |
| Google Calendar | Recommended onboarding | agenda review, holds, reminders, meeting prep | read events, optional create/update | read/draft only | connect calendar, confirm calendar list | revoke access and disable in local config |
| Gmail | Recommended onboarding | inbox triage, draft replies, follow-up review | read mail, create drafts, manage labels if approved; send denied by default | read/manage/draft only; no-send by default | connect account in chosen runtime, confirm scopes and account identity | remove connector access and set `enabled = false` |
| Google Drive | Recommended onboarding | retrieve docs, sheets, slides, briefs | read files, optional create/update | read-only initially | connect Drive, restrict folders when possible | revoke access and disable |
| Granola | Recommended onboarding | transcript ingestion and meeting notes | read/export transcripts | manual import initially | export or connect with explicit consent | stop imports and remove tokens |
| Slack | Recommended onboarding | team context, drafts, thread summaries | read channels/DMs, optional send | read/draft only | connect workspace, limit channels | revoke app access and disable |
| GitHub | Recommended when relevant | issues, PRs, code context | read repos, optional write | read-only initially | connect GitHub, choose repos | revoke token and disable |
| Linear | Recommended when relevant | product/project tracking | read workspace, optional write | read-only initially | connect Linear, choose team | revoke access and disable |
| Discord | Advanced | selected community/team context and manual relay | selected channel access; posting requires separate verification | manual relay or draft only | connect selected servers/channels and verify access policy | revoke access and disable |
| Browser automation | Advanced | authenticated web workflows | browser/session access | disabled by default | enable per task, confirm target | close session and disable |
| WhatsApp | Advanced | selected manual conversation imports | user-provided export files only | manual import/read-only only | place exports in an ignored local inbox | remove exports and disable |
| Telegram | Advanced | selected manual conversation imports | user-provided export files only | manual import/read-only only | place exports in an ignored local inbox | remove exports and disable |

## Setup Principles

- Add connectors deliberately and explain what each one enables.
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
- account or sender identity when relevant

If those details are missing, Oak should draft locally instead of sending.
