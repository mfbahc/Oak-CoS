# Skill Authoring

Skills are routing and procedure, not documentation. They share the model context window with the user request, runtime instructions, local state, connector results, and source material.

This repo follows the same discipline used in compact public skill libraries: short trigger metadata, terse operational bodies, and scripts for repeatable mechanics.

## Rules

1. The `description` is routing metadata. Keep it short, generic, and trigger-focused.
2. The body is operational procedure. Cut history, rationale essays, broad examples, and source dumps.
3. Default to one screen. Move optional detail to a reference file only when the skill genuinely needs it.
4. Put deterministic repeated commands in scripts instead of prose.
5. Do not duplicate rules already in `AGENTS.md`, `docs/operating-state.md`, or connector docs.
6. Do not add private facts, user-specific paths, or project names to public skills.
7. Run `./scripts/validate-skills` after editing skills.

## Budgets

- Description target: <= 30 words.
- Description hard gate: <= 35 words.
- Body target: <= 700 words.
- Body hard gate: <= 900 words.
- File hard gate: <= 140 lines.

If a skill needs more than that, split procedure from mechanics: keep `SKILL.md` short and add a script or narrowly named reference.

## Shape

```text
frontmatter
one-line purpose
source order
standard procedure
write / act gates
stopping condition
```

If a section does not change what the agent does, cut it.
