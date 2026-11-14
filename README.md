# skills

Workflow skills for coding agents. They work in Claude Code, Codex and any agent that reads [Agent Skills](https://agentskills.io) (`SKILL.md` folders).

| Skill | What it does |
| --- | --- |
| `afk` | Away mode: keep working, default and log decisions, brief the user on return. |
| `agent-docs` | Write or edit documents agents read: skills, AGENTS.md, CLAUDE.md. |
| `agent-pool` | Keep a pool of sub agents busy under one coordinator. |
| `avp-mvd-alvr-stutter-resolver` | Audit and fix Vision Pro MVD and ALVR stutter: AWDL channel hopping, router, wired path, subnets. |
| `behavior-tests` | Tests as the user's flow, dependencies injected as plain functions. |
| `logo` | Design a project logo with an image model and add it to the README. |
| `new-project-setup` | Set up a new repo with Git, commit, docs and versioning conventions. |
| `polish-readme` | Polish a README's first screen and intro. |
| `release` | Cut a release by hand: version from commits, tag, GitHub release, post-release steps. |
| `tiny-slice` | Focused pairing, one tiny slice at a time. |
| `wrap-up` | Before clearing a session, report what to save and what is unfinished. |

`afk` and `agent-pool` are written for agents talking through [tmux-agents](https://github.com/TheClooneyCollection/tmux-agents), `logo` generates images with Codex, and `release` publishes with the GitHub CLI (`gh`). The rest have no dependencies.

## Why

Every agent session starts from zero. Without written-down workflows, each one repeats the same archaeology: reading the repo to rediscover a convention, or asking me again how I like something done. That is slow, it costs tokens, and the corrections I make vanish when the session ends.

So I follow one rule: if I do the same sequence twice, I encode it. A skill holds the mechanical part, the exact steps and the gotchas found the hard way, so the agent arrives oriented and my attention goes to the parts that need thinking. My steering goes into them too: "one thing at a time" became `tiny-slice`, and the worry of losing lessons when I clear a session became `wrap-up`. The point is a setup that gets cheaper to work in the more it is used.

More on the thinking behind it: [AgentOS: The Agent Environment That Gets Smarter As You Build](https://blog.nicholas.clooney.io/posts/building-ai-agent-workflows-that-accumulate-context/) and [Wrap up, then clear](https://blog.nicholas.clooney.io/timeline/2026-11-12-shipped-wrap-up-skill/).

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

Issues and pull requests are welcome. Each skill is a folder under `skills/` with a `SKILL.md`. Start with the [docs](docs/README.md); [AGENTS.md](AGENTS.md) lists the conventions for skills, commits and releases.

## License

[MIT](LICENSE)
