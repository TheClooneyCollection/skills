# Changelog

## Vision Pro MVD and ALVR stutter resolver

`v1.1.0` · 2026-11-14 · Feature

- New `avp-mvd-alvr-stutter-resolver` skill: audits the Mac, router, wired path, subnets and the ALVR PC, and fixes AWDL channel hopping by locking the router to the AWDL social channel.
- The fix is verified at the radio level (a single-channel AWDL schedule); an ALVR retest is still pending.

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
