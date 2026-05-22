# Troubleshooting

## Onboarding Did Not Create Files

Rerun:

```bash
./scripts/onboard
```

Choose "both" when asked whether to generate configured files, docs-only guidance, or both.

## I Chose The Wrong Runtime

Rerun onboarding. Existing local files will be backed up before replacement.

## QMD Is Not Installed

Run:

```bash
./scripts/qmd-setup
./scripts/qmd-update
```

Oak will still create a local manifest and index. Install or configure a dedicated QMD runtime later if you use one.

## Privacy Audit Fails

Read the reported file and line. If the match is real private data, move it into `workspace/`, `local/`, or `.oak/`. If the match is a local blocked term file, make sure it is in an ignored path and not part of the scan.

## Connector Feels Too Broad

Disable it in `local/connectors.toml`, revoke access in the provider, then rerun `./scripts/doctor`.

## How To Add A Domain

Create:

```text
workspace/domains/<domain-name>/README.md
```

Add only the context needed for that domain. Use a domain worker when the task is narrow.

## How To Add A Connector Later

1. Read `docs/connectors.md`.
2. Decide the minimum permissions.
3. Enable it in your runtime.
4. Record the choice in `local/connectors.toml`.
5. Test read-only or draft-only behavior first.
