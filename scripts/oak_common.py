#!/usr/bin/env python3
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0-public"
RELEASE_TIME_TARGET_SECONDS = 30.0

PRIVATE_DIRS = {"workspace", "local", ".oak"}
ALWAYS_SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
}

SCRIPT_NAMES = [
    "onboard",
    "doctor",
    "qmd-setup",
    "qmd-update",
    "privacy-audit",
    "demo",
    "upgrade",
    "release-check",
    "export-public",
    "eval-onboarding",
    "generate-large-fixture",
    "perf-benchmark",
    "docs-list",
]

REQUIRED_PATHS = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "docs/onboarding.md",
    "docs/architecture.md",
    "docs/context-management.md",
    "docs/connectors.md",
    "docs/skills-and-plugins.md",
    "docs/privacy.md",
    "docs/worker-patterns.md",
    "docs/coaching.md",
    "docs/codex.md",
    "docs/codex-cli.md",
    "docs/claude.md",
    "docs/claude-cli.md",
    "docs/claude-desktop.md",
    "docs/prompt-bible.md",
    "docs/upgrades.md",
    "docs/routines.md",
    "docs/evaluation.md",
    "docs/release-readiness.md",
    "docs/capability-matrix.md",
    "docs/onboarding-issues-release-gate.md",
    "docs/changelog.md",
    "docs/public-release-checklist.md",
    "core/roles/executive-coach.md",
    "core/skills/coaching/SKILL.md",
    "core/skills/inbox-triage/SKILL.md",
    "core/skills/meeting-prep/SKILL.md",
    "core/skills/task-tracking/SKILL.md",
    "core/skills/initial-inbox-scan/SKILL.md",
    "core/skills/first-domain-project-setup/SKILL.md",
    "core/connectors/qmd.md",
    "core/routines/daily-brief.md",
    "core/templates/first-domain-project.md",
    "core/templates/assistant-profile.md",
    "core/personality-templates/README.md",
    "core/personality-templates/executive-chief-of-staff.md",
    "core/personality-templates/research-analyst.md",
    "core/personality-templates/engineering-lead.md",
    "core/personality-templates/personal-admin.md",
    "core/personality-templates/investor-board-support.md",
    "core/personality-templates/founder-operator.md",
    "core/personality-templates/legal-compliance-conservative.md",
    "core/personality-templates/creative-strategist.md",
    "core/personality-templates/executive-coach.md",
    "core/personality-templates/custom-build-my-own.md",
    "core/templates/meeting-prep.md",
    "core/templates/transcript-ingest.md",
    "core/templates/inbox-triage.md",
    "core/templates/writing-style-profile.md",
    "core/templates/decision-memo.md",
    "config/sample.profile.toml",
    "config/sample.connectors.toml",
    "config/sample.context.toml",
    "eval/fixtures/synthetic-profile.json",
    "eval/fixtures/expected-release-checks.json",
    "eval/fixtures/beginner-onboarding-answers.txt",
    "scripts/perf-benchmark",
    "examples/synthetic-user/README.md",
    "workspace.template/context/manifest.md",
    "migrations/001-initial-structure.md",
]

RUNTIMES = [
    "Codex App",
    "Codex CLI",
    "Claude CLI",
    "Claude Desktop",
    "Multiple / not sure yet",
]

GENERATION_MODES = [
    "both",
    "configured files",
    "docs-only guidance",
]

PERSONALITIES = [
    "Executive Chief of Staff",
    "Research Analyst",
    "Engineering Lead",
    "Personal Admin",
    "Investor / Board Support",
    "Founder Operator",
    "Legal/Compliance Conservative",
    "Creative Strategist",
    "Executive Coach",
    "Custom / build my own",
]

DOMAINS = [
    "Work / company",
    "Investing",
    "Board / advisory",
    "Personal admin",
    "Family / household",
    "Health / fitness",
    "Creative projects",
    "Engineering / software",
    "Other custom domains",
]

CADENCE = [
    "daily brief",
    "evening wrap",
    "weekly review",
    "monthly audit",
    "quarterly planning",
    "reminders/follow-ups",
    "meeting prep",
    "inbox triage",
    "task review",
]

AUTOMATION_HOSTS = [
    "Manual/on-demand only (no scheduled jobs yet)",
    "This laptop or desktop is only sometimes on",
    "Always-on Mac, desktop, server, or NAS",
    "Cloud runner or hosted scheduler",
    "Not sure yet",
]

STORAGE_MODELS = [
    "Local folder only; I will handle backup separately",
    "Drive/iCloud/Dropbox backup with a separate local runtime folder for scheduled jobs",
    "Always-on local runtime folder with optional backup sync",
    "Not sure yet; keep scheduled jobs manual for now",
]

DELIVERY_CHANNELS = [
    "Local artifact only",
    "Drive file/archive",
    "Slack channel or DM after capability verification",
    "Email draft only",
    "Discord or messaging app manual relay only",
    "Not sure yet",
]

CONNECTORS = [
    {
        "key": "gmail",
        "label": "Gmail",
        "enables": "inbox triage and draft replies",
        "permissions": "read mail, create drafts, manage labels if approved; send is denied by default",
        "default_mode": "read/manage/draft only; no-send by default",
    },
    {
        "key": "google_drive",
        "label": "Google Drive",
        "enables": "document, sheet, and slide retrieval",
        "permissions": "read files, optional create/update",
        "default_mode": "read-only initially",
    },
    {
        "key": "google_calendar",
        "label": "Google Calendar",
        "enables": "agenda review, holds, reminders, and meeting prep",
        "permissions": "read events, optional create/update",
        "default_mode": "read/draft only",
    },
    {
        "key": "granola",
        "label": "Granola",
        "enables": "meeting transcript ingestion",
        "permissions": "read/export transcripts",
        "default_mode": "manual import initially",
    },
    {
        "key": "slack",
        "label": "Slack",
        "enables": "team context, summaries, and drafts",
        "permissions": "read channels/DMs, optional send",
        "default_mode": "read/draft only",
    },
    {
        "key": "discord",
        "label": "Discord",
        "enables": "selected community or team context and manual relay",
        "permissions": "selected channel access; posting must be separately verified",
        "default_mode": "manual relay or draft only",
    },
    {
        "key": "whatsapp",
        "label": "WhatsApp",
        "enables": "manual import of selected conversation exports",
        "permissions": "user-provided export files only in the public starter",
        "default_mode": "manual import/read-only only",
    },
    {
        "key": "telegram",
        "label": "Telegram",
        "enables": "manual import of selected conversation exports",
        "permissions": "user-provided export files only in the public starter",
        "default_mode": "manual import/read-only only",
    },
    {
        "key": "github",
        "label": "GitHub",
        "enables": "repo, issue, and PR support",
        "permissions": "read repos, optional write",
        "default_mode": "read-only initially",
    },
    {
        "key": "linear",
        "label": "Linear",
        "enables": "product and project tracking",
        "permissions": "read workspace, optional write",
        "default_mode": "read-only initially",
    },
    {
        "key": "browser",
        "label": "Browser automation",
        "enables": "authenticated web workflows",
        "permissions": "browser/session access",
        "default_mode": "disabled by default",
    },
    {
        "key": "local_filesystem",
        "label": "Local filesystem",
        "enables": "selected private folders and artifacts",
        "permissions": "folder access",
        "default_mode": "selected folders only",
    },
    {
        "key": "qmd",
        "label": "QMD/local search",
        "enables": "local memory and search",
        "permissions": "local file index",
        "default_mode": "enabled",
    },
]

RUNTIME_DOCS = {
    "Codex App": "docs/codex.md",
    "Codex CLI": "docs/codex-cli.md",
    "Claude CLI": "docs/claude-cli.md",
    "Claude Desktop": "docs/claude-desktop.md",
}

RUNTIME_INSTRUCTION_FILES = {
    "Codex App": "AGENTS.md",
    "Codex CLI": "AGENTS.md",
    "Claude CLI": "CLAUDE.md",
    "Claude Desktop": "CLAUDE.md or project instructions",
}

RUNTIME_PROMPTS = {
    "Codex App": "You are {assistant} in Codex App. The Oak root is this workspace. Read AGENTS.md first, then read workspace/context/assistant-identity.md if it exists. Use docs/codex.md only as needed. Use QMD/local search before broad scans. Treat manifests as maps. Keep private state in workspace/, local/, or .oak/. Do not send or publish externally unless I explicitly ask for the exact action. Give me a short status and ask what I want to work on.",
    "Codex CLI": "You are {assistant} in Codex CLI. The Oak root is the current repo. Read AGENTS.md first, then read workspace/context/assistant-identity.md if it exists. Use docs/codex-cli.md only as needed. Use QMD/local search before broad scans. Keep context tight. Do not send emails, messages, invites, file shares, posts, or external updates unless I explicitly ask for that exact action. Report a short status before large work.",
    "Claude CLI": "You are {assistant} in Claude CLI. The Oak root is the current repo. Read CLAUDE.md first, then read workspace/context/assistant-identity.md if it exists. Use docs/claude-cli.md only as needed. Treat context manifests as manifests, not expansion instructions. Use QMD/local search before broad scans. Keep user state local. Do not take external actions unless I explicitly ask for the exact action. Start with a concise status.",
    "Claude Desktop": "You are {assistant} in Claude Desktop. The Oak root is the project folder I added. Read CLAUDE.md or the project instructions first, then read workspace/context/assistant-identity.md if it exists. Use docs/claude-desktop.md only as needed. Use QMD/local search before broad scans. Treat manifests as maps. Keep private state local. Do not send, share, post, invite, or publish externally unless I explicitly ask for that exact action. Start with a concise status and any file-access limits you see.",
}

APP_ONBOARDING_PROMPT = "Please install Oak from https://github.com/mfbahc/Oak-CoS.git if it is not already cloned locally. Clone it into a local folder I can find again, such as ~/Documents/oak-cos, then enter that folder. If the Oak folder is already open, use the current folder. Read README.md, run ./scripts/onboard, and explain each choice in plain English before changing anything. Use the recommended defaults when I am unsure. Recommend useful connectors during onboarding, especially Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search, but let me skip any connector. Keep connector-backed work read-only or draft-only unless I explicitly approve a specific write, send, share, or calendar change. After onboarding, run ./scripts/qmd-setup and show me .oak/START_HERE.md."

FIRST_DOMAIN_PROMPT = "Help me set up my first Oak domain or project. Ask me only for the minimum information needed, create the local workspace files, and then prepare my first daily brief. Use the local workspace plus any selected read-only connector context that is already available, especially Calendar, email, Google Drive, transcripts, and Slack. If a connector is not available yet, continue from local context and note what would improve after connection. Do not send, share, post, invite, archive, label, delete, or change external systems unless I explicitly approve that exact action."

ROUTINES = [
    "daily-brief",
    "evening-wrap",
    "weekly-review",
    "monthly-audit",
    "qmd-refresh",
    "stale-task-review",
    "connector-health-check",
    "domain-tracker-refresh",
]

LOCAL_TEMPLATE_NAMES = [
    "first-domain-project.md",
    "daily-brief.md",
    "meeting-prep.md",
    "transcript-ingest.md",
    "meeting-notes.md",
    "inbox-triage.md",
    "writing-style-profile.md",
    "weekly-retro.md",
    "board-project-brief.md",
    "decision-memo.md",
    "relationship-note.md",
    "travel-logistics-plan.md",
    "domain-tracker.md",
    "coaching-checkin.md",
    "quarterly-review.md",
]


def now_stamp() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def root_path(*parts: str) -> Path:
    return ROOT.joinpath(*parts)


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def backup_existing(path: Path) -> Path | None:
    if not path.exists():
        return None
    backup_root = root_path(".oak", "backups", now_stamp())
    ensure_dir(backup_root)
    target = backup_root / rel(path).replace("/", "__")
    if path.is_dir():
        shutil.copytree(path, target)
    else:
        ensure_dir(target.parent)
        shutil.copy2(path, target)
    return target


def write_text(path: Path, content: str, *, backup: bool = True) -> None:
    ensure_dir(path.parent)
    if path.exists():
        existing = path.read_text(encoding="utf-8")
        if existing == content:
            return
        if backup:
            backup_existing(path)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: object, *, backup: bool = True) -> None:
    write_text(path, json.dumps(payload, indent=2, sort_keys=True) + "\n", backup=backup)


def copy_template_tree(src: Path, dst: Path) -> list[str]:
    copied: list[str] = []
    for current, dirs, files in os.walk(src):
        dirs.sort()
        files.sort()
        current_path = Path(current)
        rel_dir = current_path.relative_to(src)
        for filename in files:
            src_file = current_path / filename
            dst_file = dst / rel_dir / filename
            if dst_file.exists():
                continue
            ensure_dir(dst_file.parent)
            shutil.copy2(src_file, dst_file)
            copied.append(rel(dst_file))
    return copied


def toml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def toml_array(values: Iterable[str]) -> str:
    return "[" + ", ".join(toml_quote(v) for v in values) + "]"


def is_text_file(path: Path) -> bool:
    try:
        data = path.read_bytes()[:4096]
    except OSError:
        return False
    if b"\x00" in data:
        return False
    return True


def iter_repo_files(*, include_generated: bool = False) -> Iterable[Path]:
    for current, dirs, files in os.walk(ROOT):
        current_path = Path(current)
        rel_parts = current_path.relative_to(ROOT).parts
        if rel_parts:
            first = rel_parts[0]
            if first in ALWAYS_SKIP_DIRS:
                dirs[:] = []
                continue
            if not include_generated and first in PRIVATE_DIRS:
                dirs[:] = []
                continue
        dirs[:] = sorted(
            d
            for d in dirs
            if d not in ALWAYS_SKIP_DIRS
            and (include_generated or d not in PRIVATE_DIRS)
        )
        for filename in sorted(files):
            yield current_path / filename


def markdown_title(path: Path, fallback: str | None = None) -> str:
    try:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except OSError:
        pass
    return fallback or path.stem.replace("-", " ").title()


def extract_headings(path: Path) -> list[str]:
    headings: list[str] = []
    try:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("#"):
                headings.append(line.strip())
    except OSError:
        return []
    return headings[:12]


def public_markdown_files() -> list[Path]:
    return [
        p
        for p in iter_repo_files(include_generated=False)
        if p.suffix.lower() in {".md", ".toml", ".json", ".txt"} and is_text_file(p)
    ]


def build_qmd_index() -> dict[str, object]:
    entries: list[dict[str, object]] = []
    candidates: list[Path] = []
    for base in ["docs", "core", "examples", "workspace"]:
        root = root_path(base)
        if root.exists():
            candidates.extend(p for p in root.rglob("*") if p.is_file() and is_text_file(p))

    for path in sorted(candidates):
        relative = rel(path)
        if relative.startswith(("local/", ".oak/")):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        snippet = " ".join(text.split())[:360]
        entries.append(
            {
                "path": relative,
                "title": markdown_title(path),
                "headings": extract_headings(path),
                "bytes": path.stat().st_size,
                "snippet": snippet,
            }
        )

    return {
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "oak_version": VERSION,
        "rule": "This is a search manifest. Do not open every listed file.",
        "entries": entries,
    }


def local_search(query: str, *, limit: int = 5) -> list[dict[str, object]]:
    query_terms = [term.lower() for term in re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]+", query)]
    phrase = query.strip().lower()
    index = build_qmd_index()
    scored: list[tuple[int, dict[str, object]]] = []
    for entry in index["entries"]:
        haystack = " ".join(
            [
                str(entry.get("path", "")),
                str(entry.get("title", "")),
                " ".join(entry.get("headings", [])),
                str(entry.get("snippet", "")),
            ]
        ).lower()
        score = sum(1 for term in query_terms if term in haystack)
        if phrase and phrase in haystack:
            score += 10
        if score:
            scored.append((score, entry))
    scored.sort(key=lambda item: (-item[0], str(item[1].get("path", ""))))
    return [entry for _, entry in scored[:limit]]


def render_personality_template(profile: dict[str, object]) -> str:
    template_name = str(profile.get("personality_template", "Custom / build my own"))
    template_path = root_path("core", "personality-templates", f"{slugify(template_name)}.md")
    if not template_path.exists():
        template_path = root_path("core", "personality-templates", "custom-build-my-own.md")
    text = template_path.read_text(encoding="utf-8", errors="ignore")
    replacements = {
        "{{ASSISTANT_NAME}}": str(profile.get("assistant_name", "Oak")),
        "{{OWNER_NAME}}": str(profile.get("owner_name", "the user")),
        "{{RELATIONSHIP}}": str(profile.get("relationship", "chief of staff")),
        "{{ROLE}}": str(profile.get("role", "planning, briefing, and follow-up partner")),
        "{{WORK_STYLE}}": str(profile.get("work_style", "")),
        "{{BOUNDARIES}}": str(profile.get("boundaries", "")),
    }
    for needle, value in replacements.items():
        text = text.replace(needle, value)
    return text.strip()


def run_command(args: list[str], *, timeout: float = 10.0) -> tuple[int, str, float]:
    start = time.perf_counter()
    try:
        result = subprocess.run(
            args,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
        )
        return result.returncode, result.stdout, time.perf_counter() - start
    except subprocess.TimeoutExpired as exc:
        output = exc.stdout if isinstance(exc.stdout, str) else ""
        return 124, output + "\ncommand timed out", time.perf_counter() - start


def sanitize_output(text: str) -> str:
    text = text.replace(str(ROOT), "<oak-root>")
    home = str(Path.home())
    if home != "/":
        text = text.replace(home, "<home>")
    return text


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "first-project"


def render_launch_prompts(profile: dict[str, object]) -> str:
    assistant = str(profile.get("assistant_name", "Oak"))
    targets = list(profile.get("runtime_targets", [])) or []
    runtime_targets = ", ".join(targets) or "not selected"
    sections = [
        "# Local Launch Prompts",
        "",
        f"Assistant: {assistant}",
        f"Runtime targets: {runtime_targets}",
        "",
        "These prompts are generated local state. Keep them private if you customize them.",
        "",
        "## Guided App Onboarding",
        "",
        APP_ONBOARDING_PROMPT,
        "",
        "## Universal",
        "",
        f"You are {assistant}, my connector-aware Chief of Staff running from a private local workspace. Operate from this Oak workspace. First read the runtime instruction file for this environment, then read workspace/context/assistant-identity.md if it exists, then follow the startup discipline. Treat context manifests as manifests, not instructions to open every linked file. Use QMD/local search before broad file scans. Keep context tight. Use selected read-only connectors when they are available and useful. Do not send emails, messages, calendar invites, file shares, posts, or external updates unless I explicitly instruct that exact action. Keep durable user state local unless I choose another destination. Start by giving me a concise status and asking what I want to work on.",
        "",
    ]
    for target in targets:
        if target in RUNTIME_PROMPTS:
            sections.extend(
                [
                    f"## {target}",
                    "",
                    RUNTIME_PROMPTS[target].format(assistant=assistant),
                    "",
                    f"- Instruction file: {RUNTIME_INSTRUCTION_FILES[target]}",
                    f"- Runtime guide: {RUNTIME_DOCS[target]}",
                    "",
                ]
            )
    sections.extend(
        [
            "## Worker",
            "",
            "You are an Oak worker for [DOMAIN/TASK]. Do not run the full startup. Read only the core Oak instructions needed for identity, privacy, context discipline, and worker rules. Use QMD/local search first. Open at most the files needed for this task. Produce a concise handoff with sources read, findings, recommended updates, and blockers. Do not update durable state unless I explicitly authorize it.",
            "",
            "## Safe Mode",
            "",
            f"You are {assistant} in safe mode. Do not use connectors, browser automation, external tools, or broad file scans. Read only the runtime instruction file and files I name. Do not write durable state unless I approve the exact path and content. Help me inspect, recover, or reason locally.",
            "",
            "## First Domain Or Project",
            "",
            FIRST_DOMAIN_PROMPT,
            "",
        ]
    )
    return "\n".join(sections)


def render_runtime_next_steps(profile: dict[str, object]) -> str:
    targets = list(profile.get("runtime_targets", [])) or []
    lines = ["# Runtime Next Steps", ""]
    for target in targets:
        if target in RUNTIME_DOCS:
            lines.extend(
                [
                    f"## {target}",
                    "",
                    f"1. Read `{RUNTIME_INSTRUCTION_FILES[target]}`.",
                    f"2. Read `{RUNTIME_DOCS[target]}`.",
                    "3. Open `.oak/launch-prompts.md` and use the matching launch prompt.",
                    "4. Run `./scripts/doctor` before using private context.",
                    "",
                ]
            )
    return "\n".join(lines)


def render_onboarding_safety(profile: dict[str, object], selected_keys: list[str]) -> str:
    selected = ", ".join(selected_keys) if selected_keys else "none"
    targets = ", ".join(profile.get("runtime_targets", [])) or "not selected"
    storage = str(profile.get("storage_model", "not selected"))
    delivery = str(profile.get("delivery_channel", "not selected"))
    automation_host = str(profile.get("automation_host", "not selected"))
    email_boundaries = str(profile.get("email_boundaries", "No email send approval has been granted."))
    inference = str(profile.get("context_inference", "Ask before inferring domains/projects from connected context."))
    return f"""# Onboarding Safety Notes

These notes are generated local state. Keep them private if you customize them.

## Runtime And Connector Verification

- Selected runtimes: {targets}
- Selected connectors in config: {selected}
- Documented, selected in config, and actually connected in the runtime are different states.
- After web OAuth or connector authorization, restart or refresh the runtime before relying on the connector.
- Verify connector availability in each runtime that will use it. Codex App, Codex CLI, Claude CLI, Claude Desktop, cloud routines, local scheduled jobs, and hosted runners may expose different tools.
- Do not write "connected" into durable state until the target runtime has been checked with its own connector list or a read-only smoke test.

## Value First

Use the first session for useful work: create the first project/domain, prepare a first brief, and only add infrastructure after it helps that work.

## Identity And User Context

- Assistant identity, role, voice, relationship, and working style belong in `workspace/context/assistant-identity.md`.
- User facts, preferences, accounts, and learned patterns belong in `workspace/context/user-profile.md` or other private workspace files.
- Do not mix assistant personality with user memory.

## Storage And Runtime Path

Selected storage model: {storage}

Drive, iCloud, Dropbox, and similar folders can be useful backup locations. Unattended scheduled jobs should run from a reliable local or hosted runtime path, not directly from a file-provider folder that may sleep, prompt, or be offline.

## Automation Host And Scheduling

Automation host: {automation_host}

Scheduled jobs need an awake, online host or hosted runner. Scheduled wrappers should have timeouts, logs, visible failure, no waiting for interactive prompts, and local artifacts as the default output.

## Delivery Channel Checks

Preferred delivery channel: {delivery}

Before promising delivery, verify the actual runtime capability. Email may only support drafts in some runtimes. Slack or Drive may be better supported. Discord and personal messaging apps should be treated as manual relay unless the runtime-specific delivery path is verified.

## Email Identity And No-Send Boundaries

{email_boundaries}

For every email account, record account identity, allowed read/manage actions, prohibited outbound actions, and any technical no-send guardrails. Behavioral instructions are not enough when a send-capable tool exists.

## Attachments And Drive

Email connectors may expose message bodies without attachment files. If an email mentions an attachment that Oak cannot see, save the file to Drive or another readable source, or place it in a local workspace folder before asking Oak to ingest it.

## Messaging Apps

Telegram and WhatsApp are manual-import/read-only only in the public starter. Do not use browser automation, desktop app automation, or send-capable tokens to read personal messaging.

## Domain And Project Reconciliation

{inference}

If connected context or local wiki/source notes suggest active projects, create or flag matching `workspace/projects/` and `workspace/domains/` files so briefs do not miss them.

## QMD And Context Refresh

Run QMD setup/update from the runtime root Oak will actually use. If local state changes during a long-running session, refresh search indexes and restart or refresh the runtime before relying on old in-session context.

## Existing Settings

If Oak edits runtime settings later, read the full settings file first, preserve existing rules, change only the intended field, and verify counts or key sections before and after.

## Migration From Another Assistant

Keep the old system running until Oak has produced verified useful output for the same job. Retire old automations only after the new path has passed smoke tests and at least a short real-world trial.
"""


def render_onboarding_resume(profile: dict[str, object], selected_keys: list[str]) -> str:
    first_project = str(profile.get("first_project", "your first project"))
    selected = ", ".join(selected_keys) if selected_keys else "none"
    return f"""# Resume Oak Onboarding

Use this if setup pauses, connector auth requires a restart, or you return in a later session.

## Paste This Prompt

```text
Please resume Oak onboarding in this folder. Read `.oak/onboarding.checkpoint.json`, `.oak/onboarding-review.md`, `.oak/START_HERE.md`, and `workspace/context/onboarding-safety.md`. Verify which connectors are actually available in this runtime before claiming they are connected. Continue with `{first_project}` and prepare the next useful local brief or setup step. Do not send, post, share, invite, archive, label, delete, or change external systems unless I explicitly approve that exact action.
```

## Current Checkpoint

- First project/domain: {first_project}
- Selected connectors in config: {selected}
- Runtime targets: {', '.join(profile.get("runtime_targets", []))}

If connector auth happened in a browser, restart or refresh the runtime before relying on those connectors.
"""


def render_start_here(profile: dict[str, object], selected_keys: list[str]) -> str:
    assistant = str(profile.get("assistant_name", "Oak"))
    targets = list(profile.get("runtime_targets", [])) or []
    first_target = targets[0] if targets else "your selected runtime"
    selected = ", ".join(selected_keys) if selected_keys else "none"
    first_project = str(profile.get("first_project", "your first project"))
    return f"""# Start Here

Oak setup created private local files for {assistant}.

## What Was Created

- `workspace/` for your private notes, tasks, routines, templates, and artifacts.
- `local/` for your local profile and connector preferences.
- `.oak/launch-prompts.md` for copy/paste launch prompts.
- `.oak/onboarding-resume.md` for pause/resume after auth, restart, or a later session.
- `.oak/qmd/` after QMD setup for local search files.

These folders are ignored by git. They are meant to stay on your machine.

## What To Open Next

1. Open `.oak/launch-prompts.md`.
2. Find the section for `{first_target}`.
3. Paste that prompt into your AI tool.
4. Ask Oak to continue setting up `{first_project}`.
5. Read `workspace/context/onboarding-safety.md` before connecting accounts or scheduling routines.

## First Thing To Ask Oak

```text
{FIRST_DOMAIN_PROMPT}
```

Oak created a starter file for this at `workspace/projects/{slugify(first_project)}/README.md`.
It also created a starter brief at `workspace/artifacts/daily-briefs/{slugify(first_project)}-first-brief.md`.

## Routine Scheduling

Automation host: {profile.get("automation_host", "not selected")}

Scheduled routines only run reliably when the chosen host is awake, online, and allowed to run background jobs. If Oak is on a laptop or desktop that sleeps, shuts down, or loses network access, treat routines as manual/on-demand unless you configure an always-on Mac, server, NAS, or cloud runner.

## Where Private Notes Go

- Tasks: `workspace/tasks.md`
- Project notes: `workspace/projects/`
- Domain notes: `workspace/domains/`
- Generated briefs and drafts: `workspace/artifacts/`
- Private templates and routines: `workspace/templates/` and `workspace/routines/`

Do not put private information in `docs/`, `core/`, `config/`, `examples/`, or `scripts/` if you plan to share or update the public repo.

## Connectors

Selected in local config: {selected}

This does not mean any outside account is connected. A connector is only active after you configure it in Codex, Claude, or another runtime and grant access there.

Recommended next step: connect the useful context sources you selected, especially Calendar, email, Drive, transcripts/Granola, Slack, and QMD/local search. If you are not ready, skip any connector and keep working locally.

## Safety Rule

Oak should not send emails, post messages, create calendar events, share files, submit browser forms, or update outside systems unless you explicitly approve that exact action.
"""


def render_connector_setup(selected_keys: list[str]) -> str:
    selected = set(selected_keys) | {"qmd"}
    lines = [
        "# Connector Setup",
        "",
        "Connectors are recommended when they match your real workflow, and every connector is skippable. Start in read-only or draft-only mode.",
        "",
        "Documented, selected in config, and actually connected are three different states. A connector is not active until you connect it in the runtime and grant access.",
        "",
    ]
    for connector in CONNECTORS:
        state = "selected" if connector["key"] in selected else "not selected"
        lines.extend(
            [
                f"## {connector['label']} ({state})",
                "",
                f"- Enables: {connector['enables']}",
                f"- May require: {connector['permissions']}",
                f"- Default mode: {connector['default_mode']}",
                "- Setup: enable the connector in your chosen runtime, confirm scopes, then test a read-only request.",
                "- Opt out: leave disabled in `local/connectors.toml` and do not connect the provider.",
                "- Disable later: revoke provider access and set `enabled = false` in `local/connectors.toml`.",
                "",
            ]
        )
    return "\n".join(lines)


def render_routine_file(name: str) -> str:
    title = name.replace("-", " ").title()
    cadence = {
        "daily-brief": "daily",
        "evening-wrap": "daily",
        "weekly-review": "weekly",
        "monthly-audit": "monthly",
        "qmd-refresh": "daily or weekly",
        "stale-task-review": "weekly",
        "connector-health-check": "weekly",
        "domain-tracker-refresh": "weekly",
    }.get(name, "as needed")
    return f"""# {title}

Cadence: {cadence}
Default output: local note or draft artifact only.

Scheduling note: this routine only runs automatically if an awake, networked host or hosted scheduler is configured. Otherwise run it manually.

## Safety

- Do not send, share, post, invite, or write to external systems by default.
- Use QMD/local search before opening files.
- Write outputs under `workspace/artifacts/` unless the user chooses another local path.
- Ask before using connectors or changing durable state.

## Suggested Prompt

Run the {title.lower()} routine using the local workspace and selected read-only connector context. Report sources read, findings, proposed updates, and blockers. Do not take external actions.
"""


def section(title: str) -> None:
    print(f"\n== {title} ==")
