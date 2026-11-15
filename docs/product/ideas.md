# Ideas

Every idea the user raises, newest first. Status is `new`, `planned`, `done` or `dropped`; the outcome links the commit or doc that carried it, or says why it was dropped.

| Date | Idea | Status | Outcome |
|---|---|---|---|
| 2026-11-15 | Layered engineering standards with principles and Swift examples | in progress | Added [engineering-standards](../../skills/engineering-standards/README.md) from the Peaks project’s draft; Why and wording decisions await the user |
| 2026-11-15 | A private design lab for comparing mockups and image rounds before implementation | done | Added [design-lab](../../skills/design-lab/README.md) |
| 2026-11-15 | A lightweight per-project task system (Markdown files per task) as the source of goals for the command center | dropped | Folded into Agent Fleet Command: missions and logs live in its central SQLite database, with an optional Markdown export later |
| 2026-11-15 | Agent Fleet Command: one command center for the fleet of agent chains (fleet state, missions, logs, direction into chains), a server owning a central database, a CLI for agents, TUI and web clients, with agent messaging as a pluggable transport and tmux-agents as the first adapter | in progress | Own project at `~/Source/Projects/agent-fleet-command`, private repo [TheClooneyCollection/agent-fleet-command](https://github.com/TheClooneyCollection/agent-fleet-command) (CLI `fleet-command`, alias `fleet`); v0 and v1 shipped on 2026-11-15 (server, tmux-agents adapter, CLI, TUI, web page, send/inbox/reply, `missions` skill). It is not a skill; it ships the skills agents need |
| 2026-11-14 | A one-line why (the problem it fixes) for each skill, in the root README and each skill README | done | Why lines added in both places |
| 2026-11-14 | A short README in every skill folder, so people opening it on GitHub have something to read | done | Skill READMEs added; `tools/check_skills.py` requires one |
