---
title: AppCreator
created: 2026-07-11
updated: 2026-07-11
type: entity
tags: [product, ai-tools, agent, automation, coding]
sources: [raw/articles/xarticle-how-i-build-apps-with-codex-without-opening-xcode-2040132557983936772.md]
---

# AppCreator

AppCreator is a Paul Solt skill for scaffolding new Xcode projects or retrofitting existing iPhone and Mac projects to be easier for coding agents to operate.

## Source-described mechanism

- Wraps `xcodebuild` commands in a `Makefile`.
- Uses `xcbeautify` to reduce verbose compiler output to readable build and test feedback.
- Exposes a repeatable `make` build-and-run action for Codex or another agent.
- Includes safety scripts and project rules intended to prevent dangerous Git commands and irreversible file deletion.

The source describes these capabilities and the linked landing page confirms AppCreator's agent-friendly Xcode positioning. The exact implementation and reliability of the skill were not independently audited.

## Related

- [[agent-friendly-xcode-projects]] — workflow pattern built around AppCreator
- [[paul-solt]] — author and operator
- [[codex]] — agent used in the source workflow
