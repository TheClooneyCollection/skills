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

- `afk`: I used to step away and come back to an agent stalled on its first question. Now it keeps going, decides what it safely can, and briefs me on return.
- `agent-docs`: Skill and AGENTS.md files kept growing until the important rules got buried. This trims them to the lines that change what the agent does.
- `agent-pool`: Too much work for one agent, too much chaos with several? One coordinator hands out tasks and merges results, so a pool works in parallel without collisions.
- `avp-mvd-alvr-stutter-resolver`: My Vision Pro stream stuttered for no obvious reason, and the cause was spread across Wi-Fi settings on the Mac, router and PC. This audits all of them and lists the fixes.
- `behavior-tests`: My tests kept breaking on refactors that changed nothing for users. These follow what the user does and sees, so they fail only on real breakage.
- `logo`: Generated logos never matched across icon, wordmark and dark mode. This picks one image and builds the whole set from it.
- `new-project-setup`: Setting up Git, docs and versioning by hand for every new repo left each one slightly different. Now they all start the same.
- `polish-readme`: A README's first screen decides whether anyone reads on, yet mine filled up with vague claims and stale badges. This makes it accurate and quick to scan.
- `release`: Releasing meant a dozen small steps, and I would forget one. Now the agent runs them in order: version, tag, GitHub release, follow-ups.
- `tiny-slice`: Too many options at once? One small step, me driving.
- `wrap-up`: Clearing a session used to wipe out what it had learned. Before I clear, this lists what to save and what is unfinished.

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
