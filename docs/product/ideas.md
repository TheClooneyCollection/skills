# Ideas

Every idea the user raises, newest first. Status is `new`, `planned`, `done` or `dropped`; the outcome links the commit or doc that carried it, or says why it was dropped.

| Date | Idea | Status | Outcome |
|---|---|---|---|
| 2026-11-17 | Always use explicit external argument labels, including the first parameter, and name functions and parameters together so calls retain domain meaning | done | Extended rule 14 in [engineering-standards](../../skills/engineering-standards/references/structure.md), with required external signatures and closure function types distinguished |
| 2026-11-16 | Preserve necessary diagnostics across error boundaries and treat intentional cancellation as lifecycle control | done | Integrated into the existing typed-error rule in [engineering-standards](../../skills/engineering-standards/references/structure.md) |
| 2026-11-16 | Serialization types with independent responsibilities, meaningful boundary payloads and semantic code grouping | done | Added principles and Swift forms to [engineering-standards](../../skills/engineering-standards/README.md), with final wire-output checks |
| 2026-11-16 | Numbered wrap-up choices and a temporary local handoff across session clears | done | Added explicit save/continue/drop choices and the uncommitted `HANDOFF.md` lifecycle to [wrap-up](../../skills/wrap-up/README.md) |
| 2026-11-16 | Stable gallery item IDs with Copy ID for feedback from a phone | done | Added item IDs, clipboard fallback and a complete round listing to [design-lab galleries](../../skills/design-lab/references/gallery.md) |
| 2026-11-15 | A concise catch-up since the user’s last message, with landed work, pending work and a decision only when needed | done | Added [catch-up](../../skills/catch-up/README.md), requested via the EDControlRoom chain |
| 2026-11-15 | Layered engineering standards with principles and Swift examples | done | Added [engineering-standards](../../skills/engineering-standards/README.md) from a draft written in a private project; the user settled its open questions |
| 2026-11-15 | A private design lab for comparing mockups and image rounds before implementation | done | Added [design-lab](../../skills/design-lab/README.md) |
| 2026-11-15 | A lightweight per-project task system (Markdown files per task) as the source of goals for the command center | dropped | Folded into Agent Fleet Command: missions and logs live in its central SQLite database, with an optional Markdown export later |
| 2026-11-15 | Agent Fleet Command: one command center for the fleet of agent chains (fleet state, missions, logs, direction into chains), a server owning a central database, a CLI for agents, TUI and web clients, with agent messaging as a pluggable transport and tmux-agents as the first adapter | in progress | Own project at `~/Source/Projects/agent-fleet-command`, private repo [TheClooneyCollection/agent-fleet-command](https://github.com/TheClooneyCollection/agent-fleet-command) (CLI `fleet-command`, alias `fleet`); v0 and v1 shipped on 2026-11-15 (server, tmux-agents adapter, CLI, TUI, web page, send/inbox/reply, `missions` skill). It is not a skill; it ships the skills agents need |
| 2026-11-14 | A one-line why (the problem it fixes) for each skill, in the root README and each skill README | done | Why lines added in both places |
| 2026-11-14 | A short README in every skill folder, so people opening it on GitHub have something to read | done | Skill READMEs added; `tools/check_skills.py` requires one |
