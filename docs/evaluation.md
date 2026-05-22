# Evaluation

Oak ships with a local release gate and synthetic fixtures so maintainers can test the public repo without private data.

## Main Gate

```bash
./scripts/release-check
```

This runs:

- script compilation
- demo onboarding
- scripted non-demo beginner onboarding from `eval/fixtures/beginner-onboarding-answers.txt`
- QMD/local search setup
- synthetic large-workspace search performance
- performance benchmarking with min/p50/p95/max metrics
- generated prompt validation
- privacy release audit
- clean public export creation and privacy scan
- ignored-state checks
- demo generation
- onboarding rerun safety
- upgrade idempotence
- QMD smoke search when the QMD binary is available
- fresh-copy and clean-export simulation

## Fixtures

Synthetic fixtures live in:

```text
eval/fixtures/
examples/synthetic-user/
```

They use placeholder data only.

`scripts/generate-large-fixture` creates ignored synthetic files under `workspace/perf-large-fixture/` so release-check can time QMD/local indexing without private data.

## Performance Target

Run:

```bash
./scripts/perf-benchmark
```

This writes ignored local reports:

```text
.oak/perf/perf-report.json
.oak/perf/perf-report.md
```

The benchmark reports min, p50, p95, and max for:

- scripted beginner onboarding eval
- QMD setup over a 180-file synthetic local workspace
- QMD update over that fixture
- repeated local searches
- public export creation

Hard failures are reserved for obvious breakage:

- beginner onboarding eval max > 10 seconds
- QMD update on 180 synthetic files max > 10 seconds
- local search p95 > 2 seconds
- export-public max > 10 seconds
- full release-check > 30 seconds

These are not optimization targets. They are guardrails for hangs, runaway scans, or broken packaging.

## Local Baselines

To refresh a local baseline after intentional product growth:

```bash
./scripts/perf-benchmark --refresh-baseline
```

Baseline comparisons are warnings only. A warning means “look at the change,” not “delete useful docs/templates until the number shrinks.” If a metric grows because Oak gained useful public templates, skills, docs, or examples, document the reason in release notes rather than weakening the product.
