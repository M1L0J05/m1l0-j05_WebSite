---
applyTo: "**"
description: "Project-specific rules for this Reflex full-stack application. Covers stack, code standards, error handling, documentation, git, structure, versioning, testing, and design. Always applied."
---

# Project Rules

## Stack & Skills
- This project uses the Reflex Python full-stack framework. Apply the relevant skill
  based on the task:
  - `reflex-core` — state management, event handlers, components, routing, styling,
    DuckDB integration, logging, testing patterns, and project structure.
  - `reflex-design` — visual design, aesthetics, typography, color, motion, and spatial
    composition decisions.
  - `reflex-fastapi` — custom FastAPI endpoints, Pydantic V2 schemas, webhooks,
    external integrations, JWT auth, and endpoint testing.
- Do not use patterns that conflict with the skills — if in doubt, follow the skill.
- When loading multiple skills simultaneously, warn if the context window is getting
  large and suggest which skills to defer.
- Database approach: direct connectors only — no ORM.
- For analytics and data transformations: **DuckDB** + **Polars**.
  Use the pattern defined in the skill (`duckdb.connect` with explicit close after each operation).
- For transactional databases: **asyncpg** (PostgreSQL) or **aiomysql** (MySQL) depending
  on the project. Choose at project start and document the decision in `README.md`.
- Raw SQL only — queries must be explicit, readable, and parameterized to prevent SQL injection.
- Never use SQLAlchemy ORM or any other ORM layer.

## Code Standards
- All code must be written in Python following PEP 8.
- All comments must be in Spanish — clear, detailed, and understandable by any developer
  regardless of experience level.
- Every function and class must have a docstring in Spanish describing purpose, parameters,
  return value, and side effects.
- No uncommented code blocks are allowed in any delivered output. Self-explanatory
  one-liners (simple assignments, direct returns) are exempt — any functional block
  with conditional logic, external calls, or data transformations must be commented.
- Inline comments should explain the "why", not just the "what".
- Examples that do NOT need a comment: simple assignments (`x = 0`), direct returns.
- Examples that DO need a comment: any block with conditional logic, external service
  calls, data transformations, or error handling.

- Never use `print()` statements — use Python `logging` with structured output instead.
  Follow the logging conventions defined in the `reflex-core` skill.
- All configuration values (API keys, URLs, secrets, environment-specific settings) must
  be loaded from environment variables via `.env`. Never hardcode them.

## Error Handling
- All async event handlers and API endpoints must handle exceptions explicitly —
  never use bare `except:` clauses.
- Database operations must always include explicit rollback logic using the connector's
  transaction API directly — no ORM transaction managers. Example with asyncpg:
  `async with conn.transaction(): ...` wraps the block and rolls back automatically on exception.
- API endpoints must return structured error responses (never raw exceptions to the client).
- Use custom exception classes for domain-specific errors, defined in a central `exceptions.py`.

## Documentation
- Every change (new feature, bug fix, refactor) must be accompanied by updated or newly
  created documentation in Spanish.
- Documentation must be structured with headings, bullet lists, and code examples.
- Maintain a `docs/` directory with at least:
  - `README.md` — project overview, setup instructions, and architecture summary in Spanish.
  - `CHANGELOG.md` — log of all changes with semantic versioning (v1.0.0, v1.1.0),
    date, description, and impact.
  - One `.md` file per major module or feature area.
- Documentation must be updated in the same task/commit as the code change — never deferred.
- No merge or task completion is valid if the corresponding documentation has not been updated.

## Git & Commits
- All git commit messages must be written in Spanish.
- Commit messages must follow this structure:

  <tipo>: <descripción breve en español>

  - Detalle 1
  - Detalle 2

- Valid commit types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `style`.
- Never bundle unrelated changes in a single commit.
- Breaking changes must be flagged explicitly with `BREAKING CHANGE:` in the commit body
  before proceeding.
- Always propose a rollback strategy for significant structural changes.
- Branch strategy: `main` (stable, always deployable), `develop` (integration),
  `feat/<name>` (one per feature), `fix/<name>` (one per bug fix).
- Never commit directly to `main` except for documented critical hotfixes.

## Project Structure
- Follow the standard Reflex project structure at all times.
- New modules must be placed in their correct directory — never dump files at the project root.
- State classes must be split by domain — one substate per functional area
  (e.g. `AuthState`, `DataState`, `UIState`).

## Versioning
- Follow semantic versioning for all releases (MAJOR.MINOR.PATCH):
  - MAJOR: breaking changes
  - MINOR: new features, backwards compatible
  - PATCH: bug fixes and minor improvements
- The project version lives in `version.py` at the root of the main package:
  `__version__ = "1.0.0"`.
- `rxconfig.py` imports the version from `version.py` — never duplicate the value.
- Every version bump must be reflected in both `CHANGELOG.md` and `version.py`.

## Quality & Testing
- Required framework: `pytest` + `pytest-asyncio` for async handlers.
- FastAPI endpoint integration tests must use `httpx.AsyncClient`.
- Every new feature must include at least: 1 happy path test + 1 expected error test.
- Tests are located in `tests/` with a directory structure mirroring the tested module.
- Recommended minimum coverage: 70% on business logic modules.
- Tests must pass before any merge — never defer.
- Pydantic V2 schemas must be used for all FastAPI endpoint validation — never raw dicts.
- Flag any introduced dependency with name, version, and justification before adding it.
- Prefer explicit, readable code over compact or clever solutions.

## Design
- Follow the frontend aesthetics guidelines from the `reflex-design` skill.
- No generic AI aesthetics — no Inter/Roboto/Arial fonts, no purple gradients,
  no cookie-cutter layouts.
- Every UI component must reflect a clear, intentional aesthetic direction.
- All styling decisions must be documented in the corresponding module `.md` file.
