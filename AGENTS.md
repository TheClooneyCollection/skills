# skills agent workflow

Workflow skills for coding agents, installable as a Claude Code or Codex plugin, with `npx skills`, or by hand.

- Work from the repository root with relative paths. Run `git` directly, never through `git -C` or after a `cd` elsewhere.
- `README.md` is for people: what the project is, why, its status, how to try it and how to contribute. Technical detail goes in `docs/`, one topic per file under the matching folder (`docs/technical/`, `docs/development/`, `docs/product/`, `docs/research/` for research records, `docs/decisions/` for decisions, see [Decisions](#decisions)), with a one-line entry in that folder's `README.md`, which is its index. A new folder gets its own `README.md` and a line in [docs/README.md](docs/README.md). Name each file after its topic (`docs/technical/save-format.md`) so it can be found by name or search.
- Keep docs concise and practical. Open each doc with a short summary. When agents are likely to repeat a mistake, add a short note in the doc they will read for that task.
- Record every idea the user raises in [docs/product/ideas.md](docs/product/ideas.md), with its status and outcome.
- Track source and docs only: build output, generated files, screenshots and secrets stay out of Git.
- Run tests in the background, without opening windows or taking focus. Tests advance an injected clock instead of waiting on wall time, and wait for conditions with a generous deadline.

## Skills

- Each skill is `skills/<name>/SKILL.md` plus any supporting files. Use the `agent-docs` skill when writing or changing one.
- Each skill folder also has a `README.md` for people browsing it: what the skill does, a one-line **Why** (the problem it fixes, also listed in the root README's Why section), when to use it, what it needs, and its files. Short and plain; keep it in step with `SKILL.md`.
- Skills must not depend on a particular machine: no absolute paths, no references to the author's dotfiles.
- Adding, renaming or removing a skill: update the `skills` list in `.claude-plugin/marketplace.json` and the table in `README.md`. Codex and `npx skills` find skills under `skills/` on their own.
- Claude Code tracks the commit, so leave `version` out of the Claude manifest. Codex caches the plugin by the `version` in `.codex-plugin/plugin.json`, which changes only at a release.
- Check before pushing: `python3 tools/check_skills.py` and `claude plugin validate .` (see [docs/development/checks.md](docs/development/checks.md)). For Codex, add the repo as a marketplace under a throwaway `CODEX_HOME` and run `codex plugin add clooney@clooney-skills`.

## Author only

Steps for the repo's author; contributors skip them.

- After every push to `main`: update the dotfiles copy in the same task, without asking, as in `~/AGENTS.md` "Own skills". A change is live there only after that.
- After pushing a new skill: add a shipped timeline entry on the blog (as in [Release](#release)), dated by the skill commit's time and linking the skill folder.

## Decisions

Standing decisions, which apply to every task:

- None yet.

Area decisions are indexed by area in [docs/decisions/README.md](docs/decisions/README.md): before working in an area, read its entries there. The areas:

- None yet.

Areas grow with the project. Record a new decision as its own file there; when no area fits, add one here as `` `area`: what it covers ``. A standing decision also gets a line in this section.

## Git

- Conventional commits: `feat(scope): ...`, `fix(scope): ...`, `docs`, `chore`, `test`, `refactor`. Imperative subject, lower case after the colon. The scope is the skill name when a commit touches one skill.
- Keep `main` linear. Work on a branch, rebase it onto `main`, and land it with `git merge --ff-only`.
- Push only when the user asks. After a significant change or several commits since the last push, ask the user whether to push.

## Versioning

Releases follow semantic versioning, `vMAJOR.MINOR.PATCH`, derived from conventional commits on the first-parent history of `main`: a `!` subject (`feat!: ...`, `fix(api)!: ...`) bumps MAJOR, a `feat` bumps MINOR, a `fix` bumps PATCH; other commit types do not change the version. Tag only when the user asks, with an annotated tag equal to the derived version: `git tag -a vX.Y.Z -m "vX.Y.Z"`.

Every feat and fix commit adds its own changelog note file, then refreshes CHANGELOG.md: see [docs/development/changelog-notes/README.md](docs/development/changelog-notes/README.md).

## Release

Releases are cut by hand with the `release` skill.

- Version files: `version` in `.codex-plugin/plugin.json`, without the `v`.
- Checks: `python3 tools/check_skills.py`, `python3 tools/test_check_skills.py`, `python3 tools/test_build_changelog.py`, `python3 tools/build_changelog.py --check`, `claude plugin validate .`.
- Prep commit: `chore: release vX.Y.Z`. The first release was `feat!: release v1.0.0`, to lift the derived version to 1.0.0.
- Title: `skills vX.Y.Z`.
- Notes: a short summary of what changed for users, grouped by skill.
- After release: add a shipped timeline entry on the author's blog (github.com/NicholasClooney/blog.clooney.io, its `timeline-entry` skill), dated by the tag's commit time and linking the release.
