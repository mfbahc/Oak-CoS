# Personality Templates

These are public starter templates for Oak's local assistant identity. They are
inspired by the common SOUL.md pattern: opening, core truths, boundaries, vibe,
continuity, and closing. They are not user profiles and must not contain private facts.

During onboarding, Oak renders the selected template into:

```text
workspace/context/assistant-identity.md
```

That generated file is private local state. Users should tune that file after a
few real sessions. If a runtime expects a file named `SOUL.md`, copy the generated
assistant identity into the runtime-specific private location instead of editing
these public templates.

## How To Choose

- `executive-chief-of-staff.md`: broad operating partner and default for most users.
- `research-analyst.md`: evidence-first research, diligence, and synthesis.
- `engineering-lead.md`: software planning, implementation, review, and release work.
- `personal-admin.md`: calendar, household, inbox, logistics, and follow-through.
- `investor-board-support.md`: board packs, governance, investments, and risk framing.
- `founder-operator.md`: product, sales, hiring, fundraising, and operating cadence.
- `legal-compliance-conservative.md`: careful review and ambiguity spotting.
- `creative-strategist.md`: positioning, narrative, messaging, and exploration.
- `executive-coach.md`: reflection, commitments, energy, and leadership growth.
- `custom-build-my-own.md`: a guided blank template for building a distinct custom identity.

## Design Rules

- Keep the template predictive: a reader should be able to infer how Oak will act.
- Describe judgment and boundaries, not a long list of canned responses.
- Include anti-patterns, especially filler, sycophancy, and pretending certainty.
- Keep private examples, names, and live account details out of public templates.
