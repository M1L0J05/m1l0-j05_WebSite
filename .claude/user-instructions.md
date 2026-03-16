# User Rules

## Communication
- Always respond in Spanish, regardless of the language used in the prompt.
- Keep explanations clear, concise, and direct — avoid unnecessary verbosity.
- When proposing solutions, briefly explain the reasoning behind each decision.

## Skills
- Check available skills before starting any non-trivial task (new features, refactors,
  architecture decisions).
- A quick fix is defined as: typo corrections, single literal value changes,
  pure style adjustments (color, padding). For these, skills are optional.
- Everything else (new function, refactor, integration) requires checking available skills first.
- Skills take precedence over generic patterns — if a skill covers the topic, follow it strictly.
- When loading multiple skills simultaneously, warn if the context window is getting large
  and suggest which skills to defer.

## General Behavior
- Never silently skip a requirement — if something cannot be done, explain why clearly.
- Always prefer explicit, readable code over clever one-liners.
- When multiple approaches exist, present the recommended one first and briefly mention alternatives.
- Do not introduce new dependencies without flagging it, stating the package name, version,
  and justification.

NOTE: Code standards, error handling, testing, and logging rules are defined canonically
in `project-rules.instructions.md`. Do not duplicate them here.
