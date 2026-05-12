---
title: Hermes Skills Workflow Patterns
created: 2026-04-21
updated: 2026-04-21
type: concept
tags: [hermes-agent, skill, workflow-automation, productivity]
sources: [raw/articles/0xjeff-3-hermes-skills-2026-04-20.md]
related_entity: [[hermes-agent]]
author: [[0xJeff]]
---

# Hermes Skills Workflow Patterns

Three Hermes skill patterns for productivity automation, documented by [[0xJeff]].

## Overview

Self-learning + self-remembering allow Hermes to improve with each interaction. 0xJeff's key use cases focus on information consumption acceleration.

## Three Documented Patterns

### 1. X Insights Fetching

Cron jobs following X accounts for macro, geopolitics, tech, and AI insights. Originally used Bird CLI but switched to official X API due to hallucinations (Bird could tweet without permission). X API costs ~$0.50/day but has clear permission settings.

### 2. Bookmark Breakdown

Daily analysis of 10-20 bookmarks with priority ranking based on preferences and investments. Combines X API (for tweets) + Browser Harness (for X articles) + LLM summarization.

### 3. Reflection

Synthesizes past information, preferences, and patterns via external memory provider. Outputs Top 5 Daily insights.

## Key Learnings

- Token management becomes critical as skill count grows
- Bird CLI write permissions must be explicitly restricted
- Browser Harness requires isolated environments and careful credential management
- last30days skill useful for cross-platform activity tracking

## Related Concepts

- [[hermes-checkpoints-rollback]] — State management for skill debugging
- [[agent-teams]] — Multi-agent patterns for long-running workflows
