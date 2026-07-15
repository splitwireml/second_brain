---
title: Codez
created: 2026-06-11
updated: 2026-06-11
type: entity
tags: [person, x-creator, claude-code, workflow]
sources: [raw/articles/xarticle-how-to-master-dynamic-workflows-in-claude-code-6-p-2062127385923776831.md, raw/articles/xarticle-httpstcoukxbevt5vl-2058156429559636069.md]
---

# Codez

X creator (@0xCodez) writing practical breakdowns of [[claude-code]] usage patterns, especially dynamic workflows as a way to turn one long prompt chain into a reusable multi-agent harness.

## Overview

This article frames dynamic workflows as a runtime harness layer on top of [[claude-code]]: Claude writes JavaScript orchestration code, spawns isolated subagents, and chooses the right model or isolation level per step. The emphasis is less on novelty and more on when to use workflows instead of staying inside one context window.

## Key Content

- [[dynamic-workflows-in-claude-code]] — six recurring workflow patterns and a 14-step mental model for routing, fan-out, verification, tournaments, and loop-until-done execution
- Highlights the three default-harness failure modes: agentic laziness, self-preferential bias, and goal drift
- Connects workflow execution to operational controls like [[goal-primitive]], token budgets, and saving reusable workflow templates as Skills

## 2026-06-11 Update

A second bookmarked X article from Codez failed to export, so the wiki stores it as [[xarticle-httpstcoukxbevt5vl-2058156429559636069]] to preserve the source trail inside the same creator cluster.

## Related

- [[claude-code]]
- [[anthropic]]
- [[dynamic-workflows-in-claude-code]]
- [[goal-primitive]]
