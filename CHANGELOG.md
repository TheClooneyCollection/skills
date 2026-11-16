# Changelog

## Choose what survives a session clear

`v1.10.0` · 2026-11-16 · Feature

- Wrap-up presents numbered choices for completed work, unfinished work and live state, and resumes only work the user explicitly selects.
- Selected context survives in a locally excluded, uncommitted HANDOFF.md, preserving existing content and removing entries only after they are resolved or saved to an approved persistent record.

## Copy gallery item IDs for phone feedback

`v1.9.0` · 2026-11-16 · Feature

- Design-lab galleries now require short, stable item IDs and Copy ID buttons, with text selection when clipboard access is unavailable.
- Each round's landing page lists every item with its ID, making it easy to identify choices from a phone.

## Use the catch-up format when returning from away mode

`v1.8.0` · 2026-11-15 · Feature

- Turn the away log into a catch-up brief, including defaulted decisions and their reasons in the current state.
- Bring parked work into the pending section and ask for a decision only when needed.

## Add concise catch-up briefs

`v1.7.0` · 2026-11-15 · Feature

- Summarise changes since the user's last message as landed work, pending or blocked work, and a decision question only when needed.
- Omit empty parts, tool narration and messages the user can already read.

## Keep skill entry points to the always-needed core

`v1.6.0` · 2026-11-15 · Feature

- Put only the minimal core needed on every invocation in SKILL.md.
- Move other material to reference files linked from the main file at the step that needs them.

## Add layered engineering standards for app code

`v1.5.0` · 2026-11-15 · Feature

- Keep five core rules in the main skill and load structure, screen-state and test references when needed.
- Provide 22 principles with inline Swift examples, encouraging canned values at unit boundaries and separating fixture provenance from invalid test inputs.

## Dark design-lab screenshots no longer depend on the Mac's appearance

`v1.4.1` · 2026-11-15 · Fix

- Use `--blink-settings=preferredColorScheme=0` for dark and `=1` for light screenshots; `--force-dark-mode` never switched `prefers-color-scheme` and only looked right on a Mac in Dark mode.

## Review design labs locally without Tailscale

`v1.4.0` · 2026-11-15 · Feature

- Use the loopback URL on the same machine, or optionally share over a tailnet for phone review.
- Keep the server on 127.0.0.1; public tunnels and binding to 0.0.0.0 are excluded from the workflow.

## Keep hidden files and directory listings out of the design lab

`v1.3.1` · 2026-11-15 · Fix

- Return 404 for dot-prefixed request path segments and directories without index.html, while keeping visual files available without caching on loopback.
- Add offline HTTP tests and include them in release checks.

## Add a private design lab workflow

`v1.3.0` · 2026-11-15 · Feature

- Compare visual directions, mockups and image rounds through one phone-friendly index before implementation.
- Include a gallery guide, sample index and no-store local server.

## Illustrate a post with image variants

`v1.2.0` · 2026-11-14 · Feature

- New `illustrate-post` skill: plans the images with the user, has Claude hand-draw exact diagrams as SVG while an image model makes every concept in 3 or 4 style families, and shows all variants in one local HTML gallery to pick from.
- Only the picked images enter the repo; everything else stays in a gitignored temp folder.

## Vision Pro MVD and ALVR stutter resolver

`v1.1.0` · 2026-11-14 · Feature

- New `avp-mvd-alvr-stutter-resolver` skill: audits the Mac, router, wired path, subnets and the ALVR PC, and fixes AWDL channel hopping by locking the router to the AWDL social channel.
- Verified on a real setup: the AWDL schedule became single-channel and ALVR no longer stutters.

## First stable release

`v1.0.0` · 2026-11-14 · Feature

- The skills install on their own: as a Claude Code plugin (`/plugin marketplace add TheClooneyCollection/skills`), a Codex plugin (`codex plugin marketplace add TheClooneyCollection/skills`), with `npx skills add TheClooneyCollection/skills`, or by copying a folder.
- Ten skills: `afk`, `agent-docs`, `agent-pool`, `behavior-tests`, `logo`, `new-project-setup`, `polish-readme`, `release`, `tiny-slice` and `wrap-up`.
- Plugin and marketplace names (`clooney`, `clooney-skills`) are now stable.

## New projects get a release section

`v0.16.0` · 2026-11-14 · Feature

- The AGENTS.md template now has a `## Release` section (version files, checks, prep commit, title, notes, post-release steps) that the `release` skill reads.

## Release skill

`v0.15.0` · 2026-11-14 · Feature

- New `release` skill: cut a release by hand from the repo's own `## Release` section in AGENTS.md, deriving the version from commits, tagging, publishing the GitHub release and running post-release steps.
- Installed with the rest of the plugin; needs the GitHub CLI (`gh`).

## install as a Claude Code or Codex plugin, or with npx skills

`v0.14.0` · 2026-11-14 · Feature

## wrap-up skips lessons the agent already gets right

`v0.13.0` · 2026-11-12 · Feature

## restore agent-docs SKILL.md overwritten by skill.md

`v0.12.1` · 2026-11-12 · Fix

## replace writing-for-agents with local agent-docs

`v0.12.0` · 2026-11-12 · Feature

## add wrap-up skill

`v0.11.0` · 2026-11-12 · Feature

## generate logo images with Codex

`v0.10.0` · 2026-11-11 · Feature

## add polish-readme skill

`v0.9.0` · 2026-11-11 · Feature

## add logo skill

`v0.8.0` · 2026-11-11 · Feature

## add behavior-tests and agent-pool skills

`v0.7.0` · 2026-10-30 · Feature

## add afk skill, import frontend-design from anthropics/skills

`v0.6.0` · 2026-10-29 · Feature

## research and decisions docs in new-project-setup

`v0.5.0` · 2026-10-29 · Feature

## optional local swift package in new-project-setup

`v0.4.0` · 2026-10-29 · Feature

## add swift reference and templates to new-project-setup

`v0.3.0` · 2026-10-29 · Feature

## add new-project-setup skill

`v0.2.0` · 2026-10-29 · Feature

## add local tiny-slice skill for all agents

`v0.1.0` · 2026-10-25 · Feature
