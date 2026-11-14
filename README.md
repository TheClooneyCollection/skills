# skills

Agent skills I use with Claude Code and Codex. Each skill is a directory under `skills/` with a `SKILL.md`.

| Skill | What it does |
| --- | --- |
| `afk` | Away mode: keep working, default and log decisions, brief the user on return. |
| `agent-docs` | Write or edit documents agents read: skills, AGENTS.md, CLAUDE.md. |
| `agent-pool` | Keep a pool of sub agents busy under one coordinator. |
| `behavior-tests` | Tests as the user's flow, dependencies injected as plain functions. |
| `logo` | Design a project logo with an image model and add it to the README. |
| `new-project-setup` | Set up a new repo with Git, commit, docs and versioning conventions. |
| `polish-readme` | Polish a README's first screen and intro. |
| `tiny-slice` | Focused pairing, one tiny slice at a time. |
| `wrap-up` | Before clearing a session, report what to save and what is unfinished. |

## Install

Link or copy a skill directory into your agent's skills directory, for example:

```sh
ln -s "$PWD/skills/tiny-slice" ~/.claude/skills/tiny-slice
```

## License

MIT
