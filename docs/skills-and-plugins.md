# Skills And Plugins

Oak treats skills as focused instruction packs and plugins/connectors as access to outside tools or data.

Public agent ecosystems commonly use small skill folders with a `SKILL.md` entrypoint, optional supporting files, and short descriptions that help the model decide when to load the skill. Oak follows that shape in `core/skills/` while keeping private user skills in ignored extension folders.

## Implemented Public Skills

The public repo currently includes safe scaffolds for:

- coaching
- daily brief
- first domain/project setup
- transcript ingest
- weekly retro
- onboarding
- inbox triage
- initial inbox scan and writing style profile
- meeting prep
- task tracking
- board or project brief
- board briefing refresh
- reading queue maintenance
- meeting transcript ingest
- Oak update checks and safe public-core upgrades
- research memo

These skills use the local workspace plus selected connectors. Connector-backed work is opt-in, recommended when useful, and starts in read-only or draft-only mode.

## Design Rules

- Keep skill entry files short.
- Put detailed references in supporting files only when needed.
- State when the skill should be used.
- State what the skill must not do.
- Avoid granting broad tool access by default.
- Review third-party skills before installing them.
- Prefer read-only connectors until a write action is explicitly needed.

## Recommended Optional Categories

The following are useful categories for future private or public skills. Some are represented by templates or connector specs, but not every category is a complete automation:

- calendar management
- document summarization
- file organization
- light relationship memory
- repo/code support
- personal admin
- travel/logistics
- reminders and follow-ups
- difficult-conversation prep
- quarterly planning

## Local Extension Layout

Private skills belong under:

```text
workspace/extensions/skills/
```

Public, scrubbed skills intended for reuse can be proposed under:

```text
core/skills/
```

## References For Maintainers

- OpenAI Codex plugin and skill concepts: <https://openai.com/academy/codex-plugins-and-skills/>
- Claude Code skills structure: <https://code.claude.com/docs/en/skills>
- Generic skill folder patterns from public agent frameworks.

Use these as design references only. Do not copy private or proprietary workflows into Oak.
