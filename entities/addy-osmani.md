---
title: Addy Osmani
created: 2026-06-11
updated: 2026-07-10
type: entity
tags: [person, x-creator, workflow, claude-code, codex]
sources: [raw/articles/xarticle-loop-engineering-2064127981161959567.md, raw/articles/xarticle-own-the-outer-loop-2074927530482835916.md]
---

# Addy Osmani

Addy Osmani (@addyosmani) is a software engineering writer and X creator focused on coding-agent workflows, developer tooling, and the operational patterns that make autonomous agent runs reliable rather than impressive-but-fragile.

## Overview

In this source, Addy frames the shift from prompt engineering to loop design: instead of manually driving every turn, the engineer defines a repeatable system that discovers work, delegates it, verifies output, and persists state across runs.

## Key Content

- [[loop-engineering]] — the five-part loop design pattern: automations, worktrees, skills, connectors, and sub-agents plus persistent external memory
- Connects loop design to concrete execution primitives in [[claude-code]] and [[codex]] rather than treating it as a tool-specific trick
- Emphasizes the risks of weak verification, comprehension debt, and cognitive surrender even when the loop itself is technically sound

## Related

- [[loop-engineering]]
- [[claude-code]]
- [[codex]]
- [[goal-primitive]]
- [[dynamic-workflows-in-claude-code]]
- [[human-in-the-loop]]
