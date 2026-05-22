# Privacy

Oak keeps durable private state local. It can use selected connector context such as Google Drive, Calendar, email, transcripts, or Slack, but public files contain only generic guidance, placeholders, and synthetic examples. Private user data belongs in ignored local paths unless the user explicitly chooses a connected destination.

## Public Files Must Not Contain

- private names
- private emails
- private domains
- private filesystem paths
- real meeting transcripts
- real board materials
- private project names
- copied private artifacts
- private coaching history
- non-synthetic examples

## Ignored Private Paths

```text
workspace/
local/
.oak/
```

## Technical Guardrails

Behavioral instructions are not enough for outbound actions when a runtime exposes send-capable tools. Where the runtime supports it, configure technical deny/no-send guardrails for:

- email send, forward, autoreply, or draft-send
- Slack or chat posting
- calendar creates, updates, cancellations, and invites
- Drive shares, deletes, moves, renames, and permission changes
- git commit, push, release, or publish actions
- browser form submissions

Outbound approval must include the exact action, destination, account identity, and content. If those details are missing, draft locally.

## Settings Preservation

When editing runtime settings, read the full file first, modify only the intended field, and write back the complete file. Never write a partial settings file that drops existing permission rules. Verify key counts or sections before and after.

## Storage Choices

Cloud-synced folders can be useful backups, but unattended scheduled jobs should use a reliable local or hosted runtime path. If backup sync is used, make freshness visible and do not make a cloud file-provider prompt part of the scheduled-job critical path.

## Privacy Audit

Run:

```bash
./scripts/privacy-audit
```

Before public release, run:

```bash
./scripts/privacy-audit --release --include-generated
```

Release mode requires a local blocked-term file in `.oak/`, `local/`, or an explicit `--blocklist` path.

Add a local blocklist when validating a release:

```bash
mkdir -p .oak
$EDITOR .oak/release-check-blocklist.txt
./scripts/privacy-audit
```

The blocklist file is ignored by git. Add private names, emails, domains, organization names, and filesystem paths that must never appear in public files.

You can also pass a blocklist directly:

```bash
./scripts/privacy-audit --blocklist path/to/blocklist.txt
```

## Coaching Data

Coaching notes are sensitive. Keep check-ins, reflections, values work, difficult-conversation notes, and quarterly reviews under `workspace/` unless the user explicitly chooses another private location.

## Demo Data

All shipped demo data must be synthetic and clearly labeled as synthetic.
