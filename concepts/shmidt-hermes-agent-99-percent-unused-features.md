---
title: "shmidt Hermes 15 Unused Features"
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [hermes-agent, ai-agent, prompt-engineering, productivity]
sources: [raw/articles/xarticle-shmidt-hermes-agent-99-percent-never-touched-these-2051307460208578864.md]
related_entity: [[shmidt]]
author: [[shmidt]]
---

# shmidt Hermes 15 Unused Features

X Article by [[shmidt]] (@shmidtqq) profiling 15 underutilized Hermes Agent features that most users never touch. 310 likes, 23 RT, May 4 2026.

## Summary

The article argues that most Hermes Agent users only use ~8% of the platform's capability, treating it as a "slightly fancier Telegram bot" while ignoring 92% of features.

## The 15 Features

### Part 1: The Setup You Skipped

1. **SOUL.md + /personality** — Agent reads SOUL.md at boot for persistent voice/persona. /personality switches between named personas on the fly.
2. **MEMORY.md + USER.md** — Persistent files read every session. MEMORY.md = project notebook. USER.md = user profile. FTS5 + LLM indexed.
3. **/insights [days]** — Cross-session analytics: tokens burned, providers used, where agent stalled.
4. **/snapshot** — Full state save before risky operations. /snapshot restore <id> to rollback.

### Part 2: Mid-Flight Controls

5. **/branch (alias /fork)** — Branch session like git commit. Try riskier path without burning good context.
6. **/rollback** — Filesystem checkpoints. Hermes saves every file it touched; skip git.
7. **/btw** — Ephemeral side question using session context. No tools, not persisted.
8. **/steer + /queue** — Mid-flight guidance: /steer redirect next tool call. /queue line up next turn without breaking current.
9. **/yolo, /fast, /reasoning** — Power toggles: /yolo skips dangerous command approval, /fast flips to fast model tier, /reasoning sets reasoning effort.

### Part 3: The Provider Lock-In That Isn't

10. **/model [--provider] [--global]** — Swap models mid-session without restart. Supports Anthropic, OpenAI Codex, OpenRouter, NVIDIA NIM, Kimi, Gemini, Bedrock, Vercel AI Gateway, Xiaomi MiMo, Step Plan, Arcee.
11. **Auxiliary Models** — Route compression, summarization, vision, and titling to different (cheaper) models. Don't pay Opus rates for Haiku-grade work.

### Part 4: The Reach You Never Activated

12. **17-Platform Gateway** — One Hermes process drives Telegram, Discord, Slack, WhatsApp, Signal, Email, SMS, Matrix, Mattermost, Feishu, WeCom, DingTalk, BlueBubbles, Home Assistant, QQBot, CLI, and voice.
13. **/voice** — Real-time voice on CLI, Telegram DMs, Discord channels, and Discord voice rooms.
14. **Cron + /webhook-subscriptions** — Built-in scheduler with plain language schedules. Webhook subscriptions push GitHub/Vercel/Stripe/Uptime payloads to DMs. Zero tokens, zero LLM cost, zero latency.

### Part 5: What Separates Real Users from Tourists

15. **Skills as Slash Commands** — 100+ pre-built skills activated via /. Custom skills can be authored. Author built /sage skill for trend scouting and thread drafting in his voice.

## Key Argument

The article's core thesis: the tool isn't underdelivering — users never gave it the instructions it was waiting for. Most users pay for a fully-loaded agent and use it like a basic Telegram bot.

## Related

- [[hermes-agent]] — The platform being profiled
- [[hermes-memory-architecture]] — Tony Simons' 11-layer memory stack (SOUL.md, MEMORY.md, USER.md are layers 1-2)
- [[hermes-skills-workflow]] — Three Hermes skill patterns by 0xJeff
- [[hermes-agent-15-features]] — Sharbel's earlier 15-feature X Article
- [[hermes-auxiliary-model-configuration]] — Hermes hidden background tasks and cost savings via per-task model config
- [[hermes-tool-plugin-architecture]] — Four extension layers in Hermes
- [[hermes-checkpoints-rollback]] — Checkpoint/rollback technique
- [[context-os]] — Layered memory infrastructure concept relevant to SOUL.md/MEMORY.md/USER.md stack
- [[skillify]] — Garry Tan's methodology for converting failures into tested skills (relevant to custom slash command authoring)
