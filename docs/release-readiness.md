# Release Readiness

Use this before public sharing:

```bash
./scripts/perf-benchmark
./scripts/export-public
./scripts/release-check
```

Do not manually zip or share a live working folder. Ignored private folders are safe from normal git sharing, but a manual zip can still include `.oak/`, `local/`, `workspace/`, caches, backups, and release reports. Use git/GitHub after the release gate passes, or share the clean archive from `./scripts/export-public`.

Release mode requires a local blocked-term file. Create one under an ignored path:

```bash
mkdir -p .oak
$EDITOR .oak/release-check-blocklist.txt
```

Include private names, organization names, domains, emails, project names, and filesystem paths that must never appear in public files.

The release gate writes local reports to:

```text
.oak/perf/perf-report.md
.oak/perf/perf-report.json
.oak/release/release-readiness-report.md
.oak/release/release-check.json
```

These reports are ignored by git.

## Publishable Definition

Oak is publishable when:

- `./scripts/release-check` passes
- generated local state is ignored
- runtime launch prompts are generated for all supported runtimes
- QMD/local search finds synthetic fixtures
- performance metrics are reported with min/p50/p95/max for onboarding, QMD, local search, and export
- connector and skill docs distinguish implemented public scaffolds from optional integrations
- `./scripts/export-public` creates a clean folder and archive with no `.git`, `.oak`, `local`, `workspace`, caches, backups, or generated private state
- privacy release audit passes with the maintainer-local blocklist
- fresh-copy and clean-export simulations pass from zero local state

## Performance Guardrails

Release checks use hard failures only for obvious breakage:

- beginner onboarding eval max > 10 seconds
- QMD update on 180 synthetic files max > 10 seconds
- local search p95 > 2 seconds
- export-public max > 10 seconds
- full release-check > 30 seconds

Baseline comparisons are warnings only. They help maintainers notice local regressions without punishing useful product growth or slower machines.

Refresh the local baseline after an intentional change:

```bash
./scripts/perf-benchmark --refresh-baseline
```

Do not delete useful docs, templates, routines, skills, or examples just to reduce file count, zip size, or timing metrics. If the product surface grew for a good reason, keep it and note the reason in the release review.
