# skills

Workflow skills for coding agents. They work in Claude Code, Codex and any agent that reads [Agent Skills](https://agentskills.io) (`SKILL.md` folders).

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

`afk` and `agent-pool` are written for agents talking through [tmux-agents](https://github.com/TheClooneyCollection/tmux-agents), and `logo` generates images with Codex. The rest have no dependencies.

## Install

### Claude Code

```
/plugin marketplace add TheClooneyCollection/skills
/plugin install clooney@clooney-skills
```

Skills are then available as `/clooney:tiny-slice` and so on. Update with `/plugin marketplace update clooney-skills`.

### Codex

```sh
codex plugin marketplace add TheClooneyCollection/skills
codex plugin add clooney@clooney-skills
```

Start a new session afterwards. Update with `codex plugin marketplace upgrade clooney-skills`.

### Any agent, with the skills CLI

```sh
npx skills add TheClooneyCollection/skills                     # pick skills interactively
npx skills add TheClooneyCollection/skills --skill tiny-slice  # one skill
```

### By hand

Copy or link a folder from `skills/` into your agent's skills directory:

```sh
git clone https://github.com/TheClooneyCollection/skills
ln -s "$PWD/skills/skills/tiny-slice" ~/.claude/skills/tiny-slice
```

## Contributing

Issues and pull requests are welcome. Each skill is a folder under `skills/` with a `SKILL.md`; see [AGENTS.md](AGENTS.md) for the repo rules.

## License

[MIT](LICENSE)
