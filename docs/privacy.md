# Privacy

Oak is local-first. Public files contain only generic guidance, placeholders, and synthetic examples. Private user data belongs in ignored local paths.

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
