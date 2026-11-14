# AGENTS.md

Notes for AI agents working in this repo.

- Each skill is `skills/<name>/SKILL.md` plus any supporting files. Use the `agent-docs` skill when writing or changing one.
- Skills must not depend on a particular machine: no absolute paths, no references to the author's dotfiles.
- Follow the commit style `feat(skill-name): ...`, `fix(...)`, `docs(...)`, `chore(...)`. Keep `main` linear.
- Adding, renaming or removing a skill: update the `skills` list in `.claude-plugin/marketplace.json` and the table in `README.md`. Codex and `npx skills` find skills under `skills/` on their own.
- Codex caches the plugin by `version` in `.codex-plugin/plugin.json`; bump it when a change should reach Codex users. Claude Code tracks the commit, so leave `version` out of the Claude manifest.
- Check before pushing: `claude plugin validate .`. For Codex, add the repo as a marketplace under a throwaway `CODEX_HOME` and run `codex plugin add clooney@clooney-skills`.
- The author's dotfiles install these skills from `main` with `.bin/skill-manager update --source clooney`. A change is live there only after it is pushed and that update runs.
