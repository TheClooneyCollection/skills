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

Each skill started as a problem I kept hitting in my own sessions. The second time I corrected an agent the same way, the correction became a skill:

- `afk`: When I step away, the agent stops at its first question and waits. This keeps it working, decides what it safely can, and briefs me when I am back.
- `agent-docs`: Skills and AGENTS.md files grow long, and the rules that matter get lost. This keeps them short, with only the lines that change what the agent does.
- `agent-pool`: A big backlog is slow with one agent and messy with several. This puts one coordinator in charge of a pool, so agents work in parallel without stepping on each other.
- `avp-mvd-alvr-stutter-resolver`: Streaming to Vision Pro kept stuttering, and the cause hides in Wi-Fi settings spread across the Mac, the router and the PC. This checks them all and says what to fix.
- `behavior-tests`: Tests that check how code works inside break every time it is restructured. This writes tests around what the user does and sees, so they fail only when something is really broken.
- `logo`: Generated logos come out inconsistent across sizes and themes. This designs one with an image model, then builds a matching set that works on light and dark READMEs.
- `new-project-setup`: Every new repo meant setting up the same Git, docs and versioning conventions by hand. This ensures consistency across all of them.
- `polish-readme`: A README's first screen decides whether people keep reading. This makes it accurate and quick to scan: one line per feature, live badges, tidy screenshots.
- `release`: A release is a dozen small steps, and it is easy to miss one. This walks through them in order: version, tag, GitHub release, follow-ups.
- `tiny-slice`: When I want to focus, the agent piles on options and next steps. This keeps us to one small step at a time, with me driving.
- `wrap-up`: Clearing a session throws away what it learned. This lists what is worth saving and what is unfinished before I clear.

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

Issues and pull requests are welcome. Each skill is a folder under `skills/` with a `SKILL.md` for the agent and a `README.md` for people. Start with the [docs](docs/README.md); [AGENTS.md](AGENTS.md) lists the conventions for skills, commits and releases.

## License

[MIT](LICENSE)
