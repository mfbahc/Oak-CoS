# QMD Connector Spec

Status: implemented local search integration with fallback.

## Use For

Local search over public docs, core files, and private workspace notes.

## Permissions

Local file index only.

## Default Safety Mode

Enabled locally.

## Setup

Run:

```bash
./scripts/qmd-setup
```

If the `qmd` binary is available, Oak can register a named QMD collection and run a smoke search. If it is absent, Oak still builds `.oak/qmd/index.json` and uses the local fallback search.

## Disable

Remove `.oak/qmd/` and disable `qmd` in `local/connectors.toml`.

## Never Without Approval

Do not treat a manifest as permission to open every file.
