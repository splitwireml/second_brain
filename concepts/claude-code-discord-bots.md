---
title: Claude Code Discord Bots
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [claude-code, ai-agent, monetization, side-hustle, saas, freelancing, social-media, agent-tool]
sources: [raw/articles/starmexxx-discord-bot-claude-code-2049737716804239591.md]
author: [[starmex]]
---

# Claude Code Discord Bots

Building and monetizing Discord bots using Claude Code as the primary development tool — no Python experience required. The concept is that Claude Code's Discord Channels integration (March 20, 2026) enables a full bot-building workflow entirely within Discord, making custom bot development accessible to non-programmers.

## Core Thesis

Discord runs on bots: 96% of moderation is automated. With 771M registered users, 231M monthly actives, and $725M ARR, it's a platform with proven monetization. The barrier to entry — Python, the Discord API, async programming — has been eliminated by Claude Code.

Claude Code Channels (launched March 20, 2026) connects a live Claude Code session directly to Discord. Developers build, test, and debug bots inside Discord itself.

## Discord Platform Stats (2026)

| Metric | Value |
|--------|-------|
| Registered users | 771M (projected year-end) |
| Monthly active users | 231M (up 9.5% YoY) |
| Daily time per user | 94 minutes average |
| Platform valuation | $14.7B |
| IPO filing | January 2026 (confidential) |
| Non-gaming servers (2024) | 45% of new servers |

## Four Monetization Models

### Model 1: Custom Bots on Demand (Fastest Cash)

Charging $200–$2,000 per custom bot build. Typical pricing:

| Bot Type | Price Range |
|----------|-------------|
| Simple utility (welcome, roles, logging) | $100–250 |
| Economy bot (currency, shop, leaderboard) | $250–500 |
| Full moderation suite | $300–600 |
| AI-powered bot (Claude API integration) | $500–1,500 |
| Complete server setup + bot | $800–2,000 |

Claude builds any of these in 2–4 hours. Effective rate: $75–150/hour.

### Model 2: Bot SaaS Subscription (Scales Largest)

One bot deployed to hundreds of servers, charging $5–$20/month per server.

```
$9/month × 50 servers = $450/month
$9/month × 200 servers = $1,800/month
$9/month × 500 servers = $4,500/month ← full-time income
$9/month × 1,000 servers = $9,000/month
```

### Model 3: Top.gg Listing

Top.gg is the Discord bot App Store. 500K+ bots listed. Premium listings $5–20/month. Top bots get thousands of organic installs monthly.

### Model 4: Server Subscriptions (Discord Native)

Discord now lets server owners charge $5–10/month for exclusive content access. The bot handles payments, role assignment, and access control automatically.

## Claude Code Integration (March 20, 2026)

Claude Code Channels connects a live Claude Code session to Discord:

```bash
# Step 1 — Verify Claude Code version
claude --version  # needs v2.1.80 or later

# Step 2 — Create Discord bot at portal.discord.com

# Step 3 — Connect Claude Code to Discord
claude mcp add discord-channels -- npx -y @claude/discord-channel

# Step 4 — Launch with Discord channel enabled
claude --channels plugin:discord@claude-plugins-official

# Step 5 — Pair via 6-character code in Discord DM
```

## Bot Types Built with Claude Code

All five bot types from the bot economy table can be built by describing the desired functionality to Claude Code:

1. **Moderation bot** — auto-ban, content filtering, spam detection, /warn, /mute, /ban commands
2. **Economy/leveling bot** — virtual currency, /daily, /work, /gamble, leaderboards
3. **AI assistant bot** — /ask, /roast, /summarize commands using Claude API
4. **Welcome/ticket bot** — onboarding flows, role assignment, support ticket workflows
5. **Giveaway bot** — automated prize drawings with reroll capability

## The Midjourney Proof Point

Midjourney built a Discord bot as their only interface for the first year — no website, no app. Result: $2.5M/month revenue, 19.26M users on their Discord server. Distribution beats interface: go where users already are.

## Full Stack

```
IDEA        → Claude analyzes Discord server needs
BUILD       → Claude Code writes complete Python bot
CONNECT     → Claude Code Channels links to Discord
DEPLOY      → Railway ($5/month) or Fly.io
DISTRIBUTE  → Top.gg, r/discordapp, Fiverr
MONETIZE    → Stripe, Top.gg premium, Discord Server Subscriptions
ITERATE     → Claude fixes bugs and adds features
SCALE       → One codebase, 500+ servers
```

## Realistic Timelines

**Custom bot freelancing:**
- Week 1: Learn the workflow
- Week 2: Build first bot (portfolio)
- Week 3: First paid job ($150–300)
- Month 3+: $1,000–3,000/month

**Bot SaaS:**
- Month 1: Launch on Top.gg, 5–10 servers
- Month 4–6: $500–1,500 MRR
- Month 6+: $2,000–5,000 MRR

## Key Resources

- Discord Developer Portal: discord.com/developers/applications
- discord.py docs: discordpy.readthedocs.io
- Bot distribution: top.gg
- Hosting: railway.app
- Claude Code Channels: docs.anthropic.com/en/docs/claude-code/channels

## Related Concepts

- [[vibe-coding]] — natural-language-to-code development approach
- [[claude-code]] — Anthropic's coding agent that powers this workflow
- [[ai-agent-automation]] — broader pattern of AI agents automating workflows
