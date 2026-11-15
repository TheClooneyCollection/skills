# skills

Workflow skills for coding agents. They work in Claude Code, Codex and any agent that reads [Agent Skills](https://agentskills.io) (`SKILL.md` folders).

| Skill | What it does |
| --- | --- |
| `afk` | Away mode: keep working, default and log decisions, brief the user on return. |
| `agent-docs` | Write or edit documents agents read: skills, AGENTS.md, CLAUDE.md. |
| `agent-pool` | Keep a pool of sub agents busy under one coordinator. |
| `avp-mvd-alvr-stutter-resolver` | Audit and fix Vision Pro MVD and ALVR stutter: AWDL channel hopping, router, wired path, subnets. |
| `behavior-tests` | Tests as the user's flow, dependencies injected as plain functions. |
| `catch-up` | Brief what changed since your last message: landed work, pending work and a decision when needed. |
| `design-lab` | Compare mockups and image rounds in a private, phone-friendly lab before implementation. |
| `engineering-standards` | Build and review app architecture, boundaries, dependencies and testable state. |
| `illustrate-post` | Illustrate a post or doc with image variants from several models, picked from one gallery. |
| `logo` | Design a project logo with an image model and add it to the README. |
| `new-project-setup` | Set up a new repo with Git, commit, docs and versioning conventions. |
| `polish-readme` | Polish a README's first screen and intro. |
| `release` | Cut a release by hand: version from commits, tag, GitHub release, post-release steps. |
| `tiny-slice` | Focused pairing, one tiny slice at a time. |
| `wrap-up` | Before clearing a session, report what to save and what is unfinished. |

`afk` and `agent-pool` are written for agents talking through [tmux-agents](https://github.com/TheClooneyCollection/tmux-agents), `logo` and `illustrate-post` generate images with Codex, and `release` publishes with the GitHub CLI (`gh`). `design-lab` uses Python 3 and headless Chrome, with optional Tailscale for phone review. The rest have no dependencies.

## Why

Each skill started as a problem I kept hitting in my own sessions. The second time I corrected an agent the same way, the correction became a skill:

- `afk`: I used to step away and come back to an agent stalled on its first question. Now it keeps going, decides what it safely can, and briefs me on return.
- `agent-docs`: Skill and AGENTS.md nowadays have a lot of what agents already knew. This trims those away to keep the lines that matter.
- `agent-pool`: I had a pile of work that could run in parallel and wanted 5 to 10 agents on it at once, without them stepping on each other's toes. One coordinator hands out tasks from a queue and merges results, and each member owns its own files.
- `avp-mvd-alvr-stutter-resolver`: My Vision Pro stream stuttered for no obvious reason, and the cause was spread across Wi-Fi settings on the Mac, router and PC. This audits all of them and lists the fixes.
- `behavior-tests`: This is the way.™ My way. Tests written as the user's flow, dependencies injected as plain functions, test factories that crash on anything not provided, fakes as plain data, and an injected clock instead of sleeps. The result: tests that survive any refactor and near-total coverage, cheaply.
- `catch-up`: I come back from a break or a flood of agent notices and ask "catch me up" or "cmu". I want only what changed since my last message, concise and in a fixed shape: what landed, what is pending or blocked, and a decision only if one is needed. Long recaps bury the decision and repeat messages I can already read.
- `design-lab`: With how easy it is to try things with AI agents, I like to experiment with designs. This puts everything together in one place that I can open from my phone: every round, every verdict and the before versions, so I can compare, pick and come back later without anything getting lost in chat.
- `engineering-standards`: I want every app I build to start from the same foundation: simple objects, strong single responsibility, strong boundaries, full dependency injection, and state and logic you can test. Writing it down once means agents build to that standard by default, instead of me re-explaining it on every project.
- `illustrate-post`: I wanted to see the best work from both Claude and an image model before picking a post's images. This has Claude draw the precise diagrams while an image model tries a few consistent styles on every image, all on one page, so I pick per image and mix freely.
- `logo`: This aligns the icon, wordmark and dark-mode versions by building them all from the one image I picked.
- `new-project-setup`: Setting up Git, docs and versioning by hand for every new repo left each one slightly different. Now they all start the same.
- `polish-readme`: A README's first screen decides whether anyone reads on. This gives it one line per feature, self-updating badges, a tidy screenshot grid and claims checked against the code.
- `release`: Releasing means a dozen small steps, and I would hate for me or an agent to ever forget one. Now the agent runs them in order: version, tag, GitHub release, follow-ups. This gives me the automation while keeping a framework and conventions for agents to follow, so releases stay intentional.
- `tiny-slice`: Too many options at once? One small step, me driving.
- `wrap-up`: Worried about losing the lessons a session taught? No more! This lists what to save and what is unfinished before I clear.

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
