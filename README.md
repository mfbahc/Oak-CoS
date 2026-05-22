# Oak

## What is this?

Oak is a local-first Chief of Staff workspace. You open this folder with an AI tool such as Codex or Claude, run a short setup, and Oak helps you organize notes, prepare briefs, track follow-ups, and work with focused assistants called workers. The public repo contains the reusable Oak system; your private information stays in local folders that are ignored by git.

## What does it do?

Oak can help you:

- prepare a daily brief from local notes, tasks, projects, and domains
- prep for meetings with decisions, questions, risks, and follow-ups
- triage inbox or message context into drafts and next actions
- turn transcripts into decisions, commitments, and open questions
- keep project, domain, and task notes organized
- run weekly reviews, evening wraps, and coaching-style check-ins
- launch narrow workers for research, calendar prep, projects, writing, or admin

Day one can be completely local. You do not need to connect Gmail, Calendar, Drive, Slack, Granola, or any outside account to try Oak.

Use your own first project on day one. Run the synthetic demo later only when you want to test that the package works.

**Skills, connectors, and routines:**

| Area | What it means | Day-one status | Full docs |
| --- | --- | --- | --- |
| Skills | focused instructions for work such as daily briefs, meeting prep, inbox triage, first-project setup, and transcript ingest | included as local scaffolds | [docs/skills-and-plugins.md](docs/skills-and-plugins.md) |
| Connectors | optional access to outside accounts such as Gmail, Calendar, Drive, Slack, or Granola | not required and not active | [docs/connectors.md](docs/connectors.md) |
| Routines | reusable prompts for repeated work such as morning brief, evening wrap, meeting prep, and weekly review | copied locally; not background jobs | [docs/routines.md](docs/routines.md) |
| Capabilities | what is implemented, scaffolded, connector-backed, or future/private | labeled explicitly | [docs/capability-matrix.md](docs/capability-matrix.md) |

## How do I install it?

**Which path should I choose?**

| Choose this path | Best when | What happens |
| --- | --- | --- |
| Open the folder in Codex App or Claude Desktop | you want the AI app to guide setup in plain English | paste the onboarding prompt below and let the app walk you through choices |
| Use Terminal | you are comfortable copying commands | run onboarding and QMD setup yourself |
| Use an AI tool to explain Terminal steps | you want help but still want to see each command | ask Codex or Claude to explain and ask before running commands |

Important sharing rule: ignored private folders are safe from normal git sharing, but they are still inside a live working folder on your machine. Never zip or share a live working folder. Share through git/GitHub after release checks, or run `./scripts/export-public` and share the clean export archive it creates.

Path A, easiest: open the folder in an AI app.

1. Download it.
2. Open or unzip the folder.
3. Keep the folder somewhere you can find again, such as Documents.
4. Open the folder in Codex App or Claude Desktop.
5. Paste this:

```text
Please help me set up Oak. Start by reading README.md. Then run ./scripts/onboard and explain each choice in plain English before changing anything. Use the recommended defaults when I am unsure. Do not connect Gmail, Calendar, Drive, Slack, or any outside account. After onboarding, run ./scripts/qmd-setup and show me .oak/START_HERE.md.
```

Path B, if you are comfortable with Terminal:

```bash
git clone https://github.com/mfbahc/Oak-CoS.git oak
cd oak
./scripts/onboard
./scripts/qmd-setup
```

Path C, if you want an AI tool to explain each terminal step, open this folder in Codex or Claude and ask:

```text
Please walk me through Oak setup. Explain what each command does, then ask before running it. Keep setup local-only and stop before connecting outside accounts.
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
Help me set up my first Oak domain or project. Ask me only for the minimum information needed, create the local workspace files, and then prepare my first daily brief from that local context. Do not connect or use any outside accounts.
```

You can still run the synthetic demo later:

```bash
./scripts/demo
```

The demo is for testing Oak. It is not the recommended first user experience.


If you are using Codex App, open this folder in Codex and paste:

```text
You are Oak in Codex App. The Oak root is this workspace. Read AGENTS.md first, then use docs/codex.md only as needed. Use QMD/local search before broad scans. Treat manifests as maps. Keep private state in workspace/, local/, or .oak/. Do not send or publish externally unless I explicitly ask for the exact action. Give me a short status and ask what I want to work on.
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
Help me set up my first Oak domain or project. Ask me only for the minimum information needed, create the local workspace files, and then prepare my first daily brief from that local context. Do not connect or use any outside accounts.
```

Oak should create a small local domain or project workspace, produce a first local daily brief from that context, and explain where your private notes go. It should not send emails, post messages, change calendars, share files, or contact outside services unless you explicitly approve that exact action.

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

## Connectors Are Optional

Day 1: use local files, your first domain/project, and generated templates. No outside account is needed.

Later: connect Calendar, Gmail, Drive, Granola, or Slack when you are ready.

Advanced: use browser automation, WhatsApp/Telegram bridges, or scheduled jobs only after you understand the safety rules.

A connector can be documented in Oak, selected in `local/connectors.toml`, and still not actually connected in your AI runtime. Oak treats those as separate states. Nothing external is active until you configure it in the runtime and grant access.

Inbox scanning is also optional. When you are ready, Oak can do a read-only inbox scan to suggest domains and projects. During that flow, Oak should ask whether you want it to learn your writing style from sent emails. If you say yes, it can sample enough sent emails inside the mailbox/date/account scope you choose to separate casual and formal patterns. It must not send, archive, label, delete, forward, or reply to email unless you explicitly approve the exact action.

## Routines Are Templates

Routines are templates for repeated work, not background jobs. Onboarding can create local routine files for daily briefs, evening wraps, meeting prep, transcript ingest, weekly reviews, QMD refreshes, stale-task reviews, connector health checks, and domain tracker refreshes.

Scheduled jobs are opt-in. They should write local artifacts only unless you explicitly enable a specific external delivery action.

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

Public core updates are designed to be safe:

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

Run these before sharing or depending on a fresh clone:

```bash
./scripts/doctor
./scripts/onboard --demo
./scripts/qmd-setup
./scripts/privacy-audit
./scripts/perf-benchmark
./scripts/demo
./scripts/upgrade --dry-run
```

Before public release:

```bash
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
