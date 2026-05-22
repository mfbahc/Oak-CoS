# Upgrades

Oak is designed so public core updates do not overwrite private workspace state.

## Standard Flow

```bash
git pull
./scripts/upgrade --dry-run
./scripts/upgrade
./scripts/doctor
```

## Rules

- Core files are versioned public files.
- Private user files live in ignored paths.
- Upgrade scripts are idempotent.
- Dry run explains intended changes.
- Existing private files are never overwritten without a backup.
- Local config stays ignored.

## What Upgrade Checks

- required ignored directories exist when local state exists
- migrations listed in `migrations/` are known
- local version and migration metadata exists under `.oak/`
- backups are created before local metadata changes
- workspace template changes are not forced onto private workspaces

## Migration State

Oak records applied migrations in `.oak/version.json`. Public migrations must be idempotent: running the same migration twice should not duplicate sections, remove custom files, or rewrite private content without a backup.

## Customizations

Put private customizations under:

```text
workspace/extensions/
```

If you want to contribute a generic customization to the public core, remove private context, replace user-specific names with placeholders, run the privacy audit with a local blocklist, and review the change manually.
