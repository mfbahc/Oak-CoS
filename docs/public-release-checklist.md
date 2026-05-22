# Public Release Checklist

Use this before sharing Oak publicly.

## Required Checks

- [ ] Fresh clone can run `./scripts/onboard --demo`.
- [ ] `./scripts/doctor` passes.
- [ ] `./scripts/qmd-setup` passes.
- [ ] `./scripts/privacy-audit` passes.
- [ ] `./scripts/demo` passes.
- [ ] `./scripts/upgrade --dry-run` passes.
- [ ] `./scripts/perf-benchmark` passes and writes `.oak/perf/perf-report.md`.
- [ ] `./scripts/export-public` creates a clean folder and zip archive.
- [ ] The clean export does not contain `.git`, `.oak`, `local`, `workspace`, caches, backups, or generated release reports.
- [ ] `./scripts/release-check` passes.
- [ ] Runtime docs cover Codex App, Codex CLI, Claude CLI, and Claude Desktop.
- [ ] Prompt bible includes all required launch prompts.
- [ ] Connector docs include permissions, default safety mode, setup, opt-out, and disable steps.
- [ ] Executive coaching is included and clearly bounded.
- [ ] Demo files are synthetic.
- [ ] No generated `workspace/`, `local/`, or `.oak/` files are staged.
- [ ] A local release blocklist was used for maintainer-specific private terms.
- [ ] Customer-facing writing was reviewed for empty hype, generic AI phrases, and repeated structure.

Do not zip or share a live working folder. Ignored private folders are safe from normal git sharing, but manual archives can include private local state. Use git/GitHub after release checks, or share the archive from `./scripts/export-public`.

## Manual Runtime Checks

- [ ] Codex App can read `AGENTS.md`.
- [ ] Codex CLI can start from repo root and follow `AGENTS.md`.
- [ ] Claude CLI can read `CLAUDE.md`.
- [ ] Claude Desktop can use project instructions or `CLAUDE.md`.
- [ ] Each runtime can explain the external-action safety rule.
- [ ] Each runtime can run or follow the demo flow.
