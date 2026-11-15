# Ideas

Every idea the user raises, newest first. Status is `new`, `planned`, `done` or `dropped`; the outcome links the commit or doc that carried it, or says why it was dropped.

| Date | Idea | Status | Outcome |
|---|---|---|---|
| 2026-11-15 | A lightweight per-project task system (Markdown files per task) as the source of goals for the command center | dropped | Folded into Fleet Command: missions and logs live in its central SQLite database, with an optional Markdown export later |
| 2026-11-15 | Fleet Command: one command center for the fleet of agent chains (fleet state, missions, logs, direction into chains), a server owning a central database, a CLI for agents, TUI and web clients, with agent messaging as a pluggable transport and tmux-agents as the first adapter | planned | Own project at `~/Source/Projects/fleet-command` (CLI `fleet`); the design plan is recorded in its `docs/decisions/` and `docs/technical/`. It is not a skill; it ships the skills agents need |
| 2026-11-14 | A one-line why (the problem it fixes) for each skill, in the root README and each skill README | done | Why lines added in both places |
| 2026-11-14 | A short README in every skill folder, so people opening it on GitHub have something to read | done | Skill READMEs added; `tools/check_skills.py` requires one |
