# Checks

`python3 tools/check_skills.py` checks that the skills, plugin manifests and README agree. CI runs it on every push and pull request, with `python3 tools/build_changelog.py --check` and the tool tests (`.github/workflows/check.yml`).

It reports:

- a skill folder without `SKILL.md` or frontmatter, a frontmatter `name` that differs from the folder, a name that is not lowercase-hyphenated or is over 64 characters, a missing description or one over 1024 characters;
- `/Users/...` or `/home/...` paths in skill files, which tie a skill to one machine;
- a skill missing from, or extra in, the `skills` list of `.claude-plugin/marketplace.json` or the README table;
- a `version` in the Claude manifest (Claude Code should track the commit);
- plugin or marketplace names that differ between the Claude and Codex manifests;
- a Codex `version` that is not `MAJOR.MINOR.PATCH`, or that differs from the latest `v*` tag.

The tests are in `tools/test_check_skills.py`; add a case there with each new rule.

`claude plugin validate .` checks the Claude manifest against Claude Code's own rules. CI does not install Claude Code, so run it locally when the manifest changes.
