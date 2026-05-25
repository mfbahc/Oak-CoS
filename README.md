# Oak

## What is this?

Oak is a connector-aware Chief of Staff workspace that runs from a private local folder. You open this folder with an AI tool such as Codex or Claude, run a short setup, connect the sources you choose, and Oak helps you organize notes, prepare briefs, track follow-ups, and work with focused assistants called workers. The public repo contains the reusable Oak system; your durable private state stays in local folders that are ignored by git.

## What does it do?

Oak can help you:

- prepare a daily brief from local notes plus selected context such as Calendar, email, Drive, transcripts, tasks, projects, and domains
- prep for meetings with decisions, questions, risks, and follow-ups
- triage inbox or message context into drafts and next actions
- turn transcripts into decisions, commitments, and open questions
- keep project, domain, and task notes organized
- run weekly reviews, evening wraps, and coaching-style check-ins
- launch narrow workers for research, calendar prep, projects, writing, or admin

Oak is most useful when it can see the context you already work in: Calendar, email, Drive, transcripts, Slack, and local notes. Onboarding includes these connectors as recommended setup choices. You can skip any connector, and connector-backed work starts read-only or draft-only unless you explicitly approve a write, send, share, or calendar change.

Oak's personality is customizable. Onboarding offers practical soul-style templates such as Executive Chief of Staff, Research Analyst, Personal Admin, and Executive Coach, plus `Custom / build my own` for users who want to define their own tone, boundaries, decision posture, and challenge style. The templates live in `core/personality-templates/` and are rendered into the private local file `workspace/context/assistant-identity.md`.

The assistant does not need to be named Oak. Onboarding asks what personal name you want for your Chief of Staff; Oak is the project name and default only.

Use your own first project on day one. Run the synthetic demo later only when you want to test that the package works.

**Skills, connectors, and routines:**

| Area | What it means | Day-one status | Full docs |
| --- | --- | --- | --- |
| Skills | focused instructions for work such as daily briefs, meeting prep, inbox triage, first-project setup, transcript ingest, reading queues, briefing refreshes, and Oak updates | included as local scaffolds | [docs/skills-and-plugins.md](docs/skills-and-plugins.md) |
| Connectors | recommended setup for outside context such as Gmail, Calendar, Drive, Slack, or Granola | skippable; read-only or draft-only by default | [docs/connectors.md](docs/connectors.md) |
| Routines | reusable prompts for repeated work such as morning brief, evening wrap, meeting prep, and weekly review | copied locally; not background jobs | [docs/routines.md](docs/routines.md) |
| Capabilities | what is implemented, scaffolded, connector-backed, or future/private | labeled explicitly | [docs/capability-matrix.md](docs/capability-matrix.md) |

**Included skills:**

| Skill | What it does |
| --- | --- |
| Board Brief | Builds a decision-oriented board, investor, lender, or project briefing. |
| Board Briefing Refresh | Refreshes a board or governance briefing from new materials, emails, trackers, and transcripts. |
| Coaching | Runs optional executive-coaching style check-ins on priorities, energy, decisions, and commitments. |
| Daily Brief | Prepares a concise day plan from tasks, observations, calendar, inbox, Drive, transcripts, and project notes. |
| First Domain/Project Setup | Creates a user's first local Oak domain or project workspace. |
| Inbox Triage | Reviews inbox context into priorities, drafts, and next actions without sending by default. |
| Ingest | Turns provided notes or artifacts into structured local memory and follow-ups. |
| Initial Inbox Scan | Infers domains, projects, and optional writing-style patterns from read-only email context. |
| Meeting Prep | Prepares objectives, context, questions, risks, and follow-ups for an upcoming meeting. |
| Meeting Transcript Ingest | Preserves a raw meeting transcript and extracts decisions, commitments, questions, and durable updates. |
| Oak Update | Checks for and applies safe public-core updates while preserving private workspace state. |
| Onboard | Guides runtime, personality, connector, project, and routine setup. |
| Reading Queue | Keeps review folders current, marks items read, and moves superseded versions out of the active queue. |
| Research Memo | Produces a source-grounded research memo with citations and open questions. |
| Retro | Runs a weekly or periodic review of commitments, decisions, patterns, and improvements. |
| Task Tracking | Maintains tasks, stale commitments, waiting items, and follow-up status. |

See [skills/README.md](skills/README.md) for the browsable skills library.

## How do I install it?

**Which path should I choose?**

| Choose this path | Best when | What happens |
| --- | --- | --- |
| Ask an AI agent to install Oak from GitHub | you want Codex or Claude to do the setup in plain English | the agent clones the repo locally, runs onboarding, and shows you where to start |
| Use Terminal | you are comfortable copying commands | run onboarding and QMD setup yourself |
| Open an already-downloaded folder | you downloaded a zip or already cloned the repo | the agent uses the local folder and runs setup there |

Important sharing rule: ignored private folders are safe from normal git sharing, but they are still inside a live working folder on your machine. Never zip or share a live working folder. Share through git/GitHub after release checks, or run `./scripts/export-public` and share the clean export archive it creates.

Feedback rule: GitHub issues are the right place for public bug reports or setup notes. Issue text and screenshots are public, so do not paste private workspace files, `.oak/`, `local/`, email/calendar content, secrets, or unsanitized logs. Describe the symptom, command, runtime, and what you expected.

Pick a dedicated folder before setup. Good default: `~/Documents/oak-cos`. Do not clone Oak inside an existing Claude, Codex, OpenClaw, or other assistant workspace unless you are intentionally migrating it. Folder name and assistant name are separate: the folder can be `oak-cos` while the assistant can be any personal name you choose.

Path A, easiest: give this to Codex or Claude.

```text
Please install Oak from https://github.com/mfbahc/Oak-CoS.git. Clone it into a new dedicated folder I can find again, such as ~/Documents/oak-cos, then enter that folder. Do not reuse an existing Claude, Codex, OpenClaw, or other assistant workspace unless I explicitly ask to migrate it. Read README.md, run ./scripts/onboard, and explain each choice in plain English before changing anything. Onboarding will ask what personal name I want for the assistant. Use the recommended defaults when I am unsure. Recommend useful connectors during onboarding, especially Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search, but let me skip any connector. Keep connector-backed work read-only or draft-only unless I explicitly approve a specific write, send, share, or calendar change. After onboarding, run ./scripts/qmd-setup and show me .oak/START_HERE.md.
```

Path B, if you are comfortable with Terminal:

```bash
git clone https://github.com/mfbahc/Oak-CoS.git oak-cos
cd oak-cos
./scripts/onboard
./scripts/qmd-setup
```

Path C, if you already downloaded or cloned the folder, open it in Codex or Claude and paste:

```text
Please help me set up Oak in this folder. First confirm this is a dedicated Oak folder, not an existing Claude, Codex, OpenClaw, or other assistant workspace unless I explicitly want migration. Start by reading README.md. Then run ./scripts/onboard and explain each choice in plain English before changing anything. Onboarding will ask what personal name I want for the assistant. Use the recommended defaults when I am unsure. Recommend useful connectors during onboarding, especially Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search, but let me skip any connector. Keep connector-backed work read-only or draft-only unless I explicitly approve a specific write, send, share, or calendar change. After onboarding, run ./scripts/qmd-setup and show me .oak/START_HERE.md.
```

## How do I launch it the first time?

If you started in Codex App or Claude Desktop, keep using that same chat and paste the launch prompt from `.oak/START_HERE.md`.

If you are using Terminal, run:

```bash
./scripts/onboard
./scripts/qmd-setup
```

Then open `.oak/START_HERE.md`. It tells you which launch prompt to use for your runtime.

The first real thing to ask Oak is:

```text
Help me set up my first Oak domain or project. Ask me only for the minimum information needed, create the local workspace files, and then prepare my first daily brief. Use the local workspace plus any selected read-only connector context that is already available, especially Calendar, email, Google Drive, transcripts, and Slack. If a connector is not available yet, continue from local context and note what would improve after connection. Do not send, share, post, invite, archive, label, delete, or change external systems unless I explicitly approve that exact action.
```

You can still run the synthetic demo later:

```bash
./scripts/demo
```

The demo is for testing Oak. It is not the recommended first user experience.


If you are using Codex App, open this folder in Codex and paste:

```text
You are Oak in Codex App. The Oak root is this workspace. Read AGENTS.md first, then read workspace/context/assistant-identity.md if it exists. Use docs/codex.md only as needed. Use QMD/local search before broad scans. Treat manifests as maps. Keep private state in workspace/, local/, or .oak/. Do not send or publish externally unless I explicitly ask for the exact action. Give me a short status and ask what I want to work on.
```

If you are using Codex CLI, run `codex` from this folder and paste the Codex CLI prompt from `.oak/launch-prompts.md`.

If you are using Claude CLI, run `claude` from this folder and paste the Claude CLI prompt from `.oak/launch-prompts.md`.

If you are using Claude Desktop, add this folder as a project or accessible folder, read `docs/claude-desktop.md`, then paste the Claude Desktop prompt from `.oak/launch-prompts.md`.

## What should I see after setup?

After onboarding, Oak creates private local folders:

```text
workspace/   your private notes, tasks, templates, routines, and artifacts
local/       your machine-specific profile and connector settings
.oak/        launch prompts, setup notes, QMD index, backups, and release reports
```

Open `.oak/START_HERE.md` first. Then ask Oak:

```text
Help me set up my first Oak domain or project. Ask me only for the minimum information needed, create the local workspace files, and then prepare my first daily brief. Use the local workspace plus any selected read-only connector context that is already available, especially Calendar, email, Google Drive, transcripts, and Slack. If a connector is not available yet, continue from local context and note what would improve after connection. Do not send, share, post, invite, archive, label, delete, or change external systems unless I explicitly approve that exact action.
```

Oak should create a small local domain or project workspace, produce a first daily brief from local and selected read-only connected context, and explain where your private notes go. It should not send emails, post messages, change calendars, share files, or contact outside services unless you explicitly approve that exact action.

## Privacy In Plain English

Oak has two parts:

- Public core: the reusable files in this repo, such as `README.md`, `docs/`, `core/`, `scripts/`, `config/`, and `examples/`.
- Private local workspace: the generated `workspace/`, `local/`, and `.oak/` folders on your machine.

Put your real notes, tasks, reflections, connector choices, and working files in the private local workspace. Do not put private information in the public core if you plan to share or update the repo.

## Runtime Support

| Runtime | Best for | Startup file | Beginner guide |
| --- | --- | --- | --- |
| Codex App | people who want to open the folder and ask Codex to help | `AGENTS.md` | [docs/codex.md](docs/codex.md) |
| Codex CLI | people comfortable using Terminal with Codex | `AGENTS.md` | [docs/codex-cli.md](docs/codex-cli.md) |
| Claude CLI | people comfortable using Terminal with Claude | `CLAUDE.md` | [docs/claude-cli.md](docs/claude-cli.md) |
| Claude Desktop | people who prefer a desktop app and project instructions | `CLAUDE.md` or project instructions | [docs/claude-desktop.md](docs/claude-desktop.md) |

Read [docs/prompt-bible.md](docs/prompt-bible.md) for the full prompt set.

## Daily Operating Model

Most users run one main Oak instance and launch workers only for narrow jobs.

The main instance:

- keeps the operating picture
- decides what context is needed
- delegates to workers when a domain needs focus
- merges handoffs back into local state only when authorized

Workers:

- read only what the task needs
- use QMD/local search first
- return a short handoff with sources, findings, proposed updates, and blockers
- avoid durable state changes unless explicitly authorized

Oak should treat current tasks, latest observations, and source-backed project notes as the operating state. Old daily briefs and historical exports are evidence, not the current truth, when newer state conflicts with them. See [docs/operating-state.md](docs/operating-state.md).

## Connectors Are Recommended But Skippable

Recommended onboarding: prepare the connectors that make Oak useful for real work, especially Calendar, Gmail/email, Google Drive, Granola/transcripts, Slack, and QMD/local search.

Skippable path: if you are not ready to grant access, leave any connector unconfigured. Oak can still work from local files, your first domain/project, and generated templates.

Advanced: use browser automation, WhatsApp/Telegram bridges, or scheduled jobs only after you understand the safety rules.

A connector can be documented in Oak, selected in `local/connectors.toml`, and still not actually connected in your AI runtime. Oak treats those as separate states. Nothing external is active until you configure it in the runtime and grant access.

After web OAuth or browser connector auth, restart or refresh the runtime and verify a read-only request before relying on that connector. Different runtimes may expose different connector surfaces.

Inbox scanning is a useful first connector workflow. Oak can do a read-only inbox scan to suggest domains and projects. During that flow, Oak should ask whether you want it to learn your writing style from sent emails. If you say yes, it can sample enough sent emails inside the mailbox/date/account scope you choose to separate casual and formal patterns. It must not send, archive, label, delete, forward, or reply to email unless you explicitly approve the exact action.

## Routines Are Templates

Routines are templates for repeated work, not background jobs. Onboarding can create local routine files for daily briefs, evening wraps, meeting prep, transcript ingest, weekly reviews, QMD refreshes, stale-task reviews, connector health checks, and domain tracker refreshes.

Scheduled jobs are opt-in. Onboarding asks whether you have an always-on device or hosted runner. A laptop or desktop that sleeps, shuts down, or loses network access will not run cron-style routines reliably, so use manual/on-demand routines unless you configure an always-on Mac, server, NAS, or cloud scheduler.

Scheduled jobs should write local artifacts only unless you explicitly enable a specific external delivery action.

## QMD And Local Search

Run:

```bash
./scripts/qmd-setup
./scripts/qmd-update
```

The setup creates a local QMD-compatible manifest and JSON index under `.oak/qmd/`. If a `qmd` binary is available, Oak registers a named collection, runs a status check, and performs a smoke search. If not, the local JSON index remains the fallback search path.

## Executive Coaching

Oak includes an optional executive-coaching lens. It is not therapy and does not claim clinical authority. It helps with priorities, energy, commitments, difficult conversations, retros, and quarterly planning.

Use the coaching launch prompt in [docs/prompt-bible.md](docs/prompt-bible.md) or the skill in [core/skills/coaching/SKILL.md](core/skills/coaching/SKILL.md). Coaching notes belong in your ignored `workspace/` tree.

## Updating Oak

Public core updates are designed to be safe. The simplest path is to ask your running Oak instance:

```text
Check for Oak updates.
```

Oak should run:

```bash
./scripts/update --check-only
```

If updates are available, tell Oak:

```text
Update Oak.
```

Oak should run:

```bash
./scripts/update --apply
```

The update flow is the same in Codex App, Codex CLI, Claude CLI, and Claude Desktop. After an update, restart or refresh the current AI session so it reloads the updated public core instructions and skills.

Release notes live in [docs/changelog.md](docs/changelog.md). Check that file after updating if you want the short version of what changed.

Manual equivalent:

```bash
git pull
./scripts/upgrade --dry-run
./scripts/upgrade
./scripts/doctor
```

Upgrade rules:

- never overwrite private workspace files without a backup
- keep local config ignored
- run migrations idempotently
- explain dry-run changes before applying them
- keep user-created extensions outside the public core unless the user chooses otherwise

See [docs/upgrades.md](docs/upgrades.md).

## Validation

Run these in a live onboarded workspace:

```bash
./scripts/doctor
./scripts/qmd-update
./scripts/privacy-audit
./scripts/upgrade --dry-run
```

`./scripts/doctor` is safe to run after onboarding. It validates the demo path
inside a temporary copy and should not overwrite `.oak/`, `local/`, or
`workspace/` setup files. Do not run `./scripts/onboard --demo` inside a real
workspace unless you intentionally want to replace local setup with synthetic
demo values.

Before public release:

```bash
./scripts/perf-benchmark
./scripts/export-public
./scripts/release-check
```

`./scripts/export-public` creates an ignored `.oak/export/oak-public-.../` folder and matching zip archive that excludes `.git`, `.oak`, `local`, `workspace`, caches, backups, and generated private state. Use that package when you need a clean shareable zip instead of publishing through git.

Maintainers should add local blocked terms to `.oak/release-check-blocklist.txt` or pass a blocklist with `./scripts/privacy-audit --blocklist path/to/file`. That file is ignored and must not be committed.

## Public Release Checklist

Before release:

- onboarding works from a fresh clone
- runtime docs cover Codex App, Codex CLI, Claude CLI, and Claude Desktop
- prompt bible is complete
- QMD setup runs
- connector docs state permissions, safe defaults, setup, opt-out, and disable steps
- demo material is synthetic
- privacy audit passes with a local release blocklist
- README and docs have been reviewed for generic AI phrases and private references
- no generated `workspace/`, `local/`, or `.oak/` files are committed

The full checklist is in [docs/public-release-checklist.md](docs/public-release-checklist.md).
