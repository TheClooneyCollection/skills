# AGENTS.md

Notes for AI agents working in this repo.

- Each skill is `skills/<name>/SKILL.md` plus any supporting files. Use the `agent-docs` skill when writing or changing one.
- Skills must not depend on a particular machine: no absolute paths, no references to the author's dotfiles.
- Follow the commit style `feat(skill-name): ...`, `fix(...)`, `docs(...)`, `chore(...)`. Keep `main` linear.
- The author's dotfiles install these skills from `main` with `.bin/skill-manager update --source clooney`. A change is live there only after it is pushed and that update runs.
