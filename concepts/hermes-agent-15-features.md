---
title: hermes-agent-15-features
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [hermes-agent, agent-tool, productivity]
sources: [raw/articles/sharbel-hermes-agent-features-2049158152709382177.md]
author: [[sharbel]]
---

# Hermes Agent 15 Features

X Article by [[sharbel]] profiling 15 underutilized Hermes Agent features, ranked by impact. Published May 2026; 1,218 likes, 131 retweets.

## The Setup Most People Skip Entirely

### 1. /personality + SOUL.md

Hermes reads `SOUL.md` at boot — defines the agent's voice permanently across every session and platform. Use `/personality` to switch between named personas mid-conversation. Stop retyping role primers every session.

### 2. MEMORY.md + USER.md

Two persistent files read every session. `MEMORY.md` is the agent's notebook on project truth. `USER.md` knows the user's role, tone, context, tradeoffs. Indexed with FTS5 + LLM summarizer for cross-session retrieval (8+ weeks).

### 3. /insights [days]

Analytics across every session: token usage by project, provider costs, failure patterns. `/insights 30` shows the last month at a glance.

### 4. /snapshot

Save the entire Hermes config and state as a snapshot before risky changes. `/snapshot restore <id>` to rollback. The "about to refactor SOUL.md" safety command.

## Mid-Flight Control Nobody Uses

### 5. /branch (alias /fork)

Branch the current session to explore a different path without losing the original. Like git for conversations. Try riskier approaches without burning good context.

### 6. /rollback

Filesystem checkpoints — Hermes keeps checkpoints of every file it touched. Restore any checkpoint without reaching for git.

### 7. /btw

Ephemeral side question using session context but not persisted. The "quick gut check without polluting my main thread" command.

### 8. /steer and /queue

Mid-flight correction without killing the run. `/steer use staging API not prod` — the next tool call sees the note without interrupting the current turn or losing prompt cache warmth. Pair with `/queue` to line up the next turn.

### 9. /yolo, /fast, /reasoning

Power toggles: `/yolo` skips dangerous-command approvals; `/fast` switches to OpenAI Priority Processing or Anthropic Fast Mode; `/reasoning` sets o-style model reasoning effort level.

## The Provider Lock-In That Isn't

### 10. /model [--provider] [--global]

Hermes is provider-agnostic. One command swaps the model without restart: Anthropic Opus 4.7, OpenAI Codex, OpenRouter, NVIDIA NIM, Kimi, Gemini, AWS Bedrock, Vercel AI Gateway, Xiaomi MiMo, Step Plan, Arcee. `/model anthropic:claude-opus-4-7` or `/model openrouter:kimi-k2.6`.

### 11. Auxiliary models

Different models for different side tasks: Opus 4.7 as main brain, Haiku 4.5 for compression, tiny model for title generation. Configure once via `hermes model` auxiliary screen. Avoid paying Opus rates for Haiku-grade work.

## The Reach Nobody Activates

### 12. 17-platform gateway

Telegram, Discord, Slack, WhatsApp, Signal, Email, SMS, Matrix, Mattermost, Feishu, WeCom, DingTalk, BlueBubbles, Home Assistant, QQBot, plus CLI and voice. One Hermes process drives all of them via `hermes gateway`.

### 13. /voice (real-time voice on 4 platforms)

Real-time voice in CLI, Telegram DMs, Discord channels, and Discord voice channels. Type `/voice` and talk.

### 14. Cron + /webhook-subscriptions

Built-in cron scheduler: plain-language schedules with delivery destinations. "Every Friday at 5pm, summarize this week's GitHub commits and post to Slack #standups." Paired with `/webhook-subscriptions` for the inverse: GitHub, Vercel, Stripe, uptime checks push directly to DMs — zero LLM cost and latency.

## The Thing That Separates Serious Users

### 15. Skills are slash commands

100+ built-in skills, all slash commands: `/architecture-diagram`, `/excalidraw`, `/manim-video`, `/research-paper-writing`, `/linear`, `/google-workspace`, `/imessage`, `/youtube-content`, `/codex`, `/claude-code`, `/test-driven-development`, `/systematic-debugging`. Also: write your own. Custom skills persist across all platforms and sessions.

## Related Concepts

- [[hermes-agent]] — the product itself
- [[mcp]] — Model Context Protocol for tool extensions
