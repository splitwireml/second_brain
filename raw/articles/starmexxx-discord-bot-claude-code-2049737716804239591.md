---
title: "Midjourney Makes $2.5M/Month From a Discord Bot. Claude Code Builds Yours This Weekend"
author: "starmex"
username: "@starmexxx"
created: "2026-04-30"
source: "https://x.com/starmexxx/status/2049737716804239591"
type: "x_article"
tags: [claude-code, discord, monetization, side-hustle, freelancing, saas, ai-agent, agent-tool]
---

Midjourney Makes $2.5M/Month From a Discord Bot. Claude Code Builds Yours This Weekend

I found out about this late. Don't make the same mistake.

> Follow & Bookmark this - I'm starmex, I track how AI tools are creating new income streams most people haven't heard of yet. This one surprised even me.

Eight months ago I was reading through a Discord statistics report. Not looking for anything specific. Just following the money.

Then I saw it. Midjourney - the AI image generation tool - runs entirely through a Discord bot. No website. No app. No separate platform. Just a bot in a server.

Monthly revenue: $2,500,000.

Then I kept reading. 771 million registered Discord users by end of 2026. 231 million monthly actives. The average user spends 94 minutes per day on Discord - more than Instagram. 96% of all Discord moderation is handled by automated bots.

Then I looked at what people were selling bots for: $200 to $1,000 per custom bot. Server owners paying $5-15/month for bot subscriptions. Communities paying for premium features, AI moderation, economy systems, welcome flows.

The barrier that kept most people out: you needed to know Python, the Discord API, slash commands, webhooks, async programming.

Claude Code knows all of it. And since March 2026 - Claude Code officially connects directly to Discord.

One weekend. Zero Python written by hand. A working, deployed Discord bot. Here's exactly how.

1/

## What Discord actually is in 2026. Not what you think.

Most people picture gamers yelling into microphones. That's not the platform anymore.

```powershell
Discord stats 2026:
Registered users:                771 million (projected year-end)
Monthly active users:            231 million (up 9.5% YoY)
Daily time per user:             94 minutes average
Heavy users (moderators):        4+ hours/day
Age 18-24:                       35% of traffic
Annual revenue (Discord itself): $725M ARR
Platform valuation:              $14.7 billion
IPO filing:                      January 2026 (confidential)
Non-gaming servers (2024):       45% of all new servers
```

Gaming launched Discord. But by 2026 - education groups, AI communities, crypto projects, startup teams, music collectives. 45% of all new servers created in 2024 were non-gaming. The platform is a communication layer for the internet, not just gamers.

And it runs on bots. 96% of moderation is automated. Economy systems, leveling, welcome messages, ticket systems, polls, giveaways - all bots. Server owners don't know Python. They just know they need a bot that does X, and they'll pay for it.

The bot economy broken down:

```plaintext
Type of bot              Who buys it           Price range
─────────────────────────────────────────────────────────
Moderation bot           Every serious server  $5-15/month SaaS
Economy/leveling         Gaming communities    $10-20/month
AI assistant bot         Businesses, creators  $15-50/month
Custom utility bot       Individual servers    $200-1,000 one-time
White-label bot          Agencies, brands      $500-5,000 setup
```

Claude builds all five types. You describe what you want. Claude writes every line of Python. You deploy to Railway or Fly.io for $5/month. Bot is live.

2/

## What most people missed: March 20, 2026.

On March 20, 2026, Anthropic officially launched Claude Code Channels - a feature that connects a live Claude Code session directly to Discord, Telegram, and iMessage.

What this means for bot builders: Claude Code now has a Discord-native workflow. You build bots inside Discord, test them inside Discord, debug them inside Discord. The terminal and the platform are the same place.

```bash
# Step 1 — Install Claude Code Channels
claude --version  # needs v2.1.80 or later

# Step 2 — Create your Discord bot in Discord Developer Portal
# portal.discord.com → New Application → Bot → Reset Token

# Step 3 — Connect Claude Code to Discord
claude mcp add discord-channels -- npx -y @claude/discord-channel

# Step 4 — Launch with Discord channel enabled  
claude --channels plugin:discord@claude-plugins-official

# Step 5 — DM your bot in Discord
# Bot replies with 6-character pairing code
# Back in Claude Code: /discord:access pair YOUR_CODE
```

From that point forward: you message the bot in Discord, Claude Code receives it, processes it with full access to your local files and tools, replies back through Discord. You're testing your bot while building it, inside the same platform it will run on.

The second thing most people missed: Midjourney's lesson.

Midjourney never built a website for their first year. No landing page, no app, no web interface. Just a Discord bot. Users joined their server, typed /imagine, got images. Simple.

Result: $2,500,000/month. 19.26 million users on their Discord server.

They proved something important: distribution beats interface. Your users are already on Discord. Your bot goes where they already are. No acquisition cost. No onboarding friction. They type a slash command and it works.

3/

## The money math. Four ways Discord bots make money.

Model 1 - Custom bots on demand (fastest cash)

Server owners post in r/discordapp, Discord servers, Fiverr, asking for custom bots. Standard rates:

```powershell
Simple utility bot (welcome, roles, logging):    $100-250
Economy bot (currency, shop, leaderboard):       $250-500
Full moderation suite:                           $300-600
AI-powered bot (Claude API integration):         $500-1,500
Complete server setup + bot:                    $800-2,000
```

Claude builds any of these in 2-4 hours. You charge $300. That's $75-150/hour effective rate. With Claude writing the code.

Model 2 - Bot SaaS subscription (scales biggest)

One bot, hundreds of servers, monthly recurring revenue.

```plaintext
Bot SaaS math:
Charge $9/month per server
50 servers = $450/month
200 servers = $1,800/month
500 servers = $4,500/month  ← full-time income
1,000 servers = $9,000/month

Popular bot categories for subscription:
- AI moderation: auto-ban, content filtering, spam detection
- Welcome systems: custom onboarding flows, role assignment
- Economy bots: virtual currency, shop, games
- Ticket systems: support workflows for communities
- Analytics: server growth, engagement tracking
```

Model 3 - Top.gg listing (passive discovery)

top.gg is the App Store for Discord bots. 500K+ bots listed. Servers browse for bots like apps. You list your bot, optimize the description (Claude writes it), and servers find you organically.

Premium listing: $5-20/month. Top bots get thousands of new server installs monthly without any promotion.

Model 4 - Server subscriptions (new 2024)

Discord now lets server owners charge for access to exclusive content. You build the server, you build the bot that manages it, you charge $5-10/month for premium membership. The bot handles payments, role assignment, and access control automatically.

```powershell
Server subscription math:
100 members × $5/month = $500/month
500 members × $7/month = $3,500/month
1,000 members × $10/month = $10,000/month
```

4/

## Python - the language you don't need to learn.

Every Discord bot runs on Python with the discord.py library. Here's what a real bot looks like:

```python
import discord
from discord.ext import commands
import anthropic

# Bot setup with all intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = anthropic.Anthropic()  # uses ANTHROPIC_API_KEY env var

@bot.event
async def on_ready():
    print(f'{bot.user} is online and ready')
    await bot.tree.sync()  # sync slash commands

@bot.tree.command(name="ask", description="Ask Claude anything")
async def ask_claude(interaction: discord.Interaction, question: str):
    await interaction.response.defer()  # prevent timeout
    
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",  # fastest, cheapest
        max_tokens=1024,
        messages=[{"role": "user", "content": question}]
    )
    
    response = message.content[0].text
    
    # Discord has 2000 char limit — split if needed
    if len(response) > 1900:
        chunks = [response[i:i+1900] for i in range(0, len(response), 1900)]
        await interaction.followup.send(chunks[0])
        for chunk in chunks[1:]:
            await interaction.channel.send(chunk)
    else:
        await interaction.followup.send(response)

bot.run("YOUR_BOT_TOKEN")
```

This is a working AI bot that answers any question using Claude. I didn't write it. Here's the exact prompt that generated it:

```yaml
Build a Discord bot in Python using discord.py library.

The bot has one slash command: /ask [question]
When used:
1. Bot defers response (prevents Discord timeout)
2. Sends question to Claude claude-haiku-4-5-20251001 via Anthropic API
3. Returns Claude's answer to the Discord channel
4. Handles Discord's 2000 character message limit

Use discord.Intents.default() with message_content enabled.
Use bot.tree for slash commands (not prefix commands).
Include on_ready event that syncs slash commands.
Show me how to run this bot and what environment variables I need.
```

Claude outputs the complete file, tells you how to install dependencies, and explains how to get your bot token.

5/

## The full build. Step by step with Claude.

Step 1 - Create your bot in Discord Developer Portal (10 minutes)

```powershell
1. Go to discord.com/developers/applications
2. Click "New Application" → name your bot
3. Go to "Bot" section → click "Reset Token" → copy token
4. Enable "Message Content Intent" under Privileged Gateway Intents
5. Go to OAuth2 → URL Generator:
   - Scopes: bot + applications.commands
   - Bot Permissions: Send Messages, Use Slash Commands,
     Manage Roles, Read Message History
6. Copy generated URL → paste in browser → add to your test server
```

Step 2 - Set up environment (15 minutes)

```bash
# Create project
mkdir my-discord-bot && cd my-discord-bot

# Install dependencies
pip install discord.py anthropic python-dotenv

# Create .env file
echo "DISCORD_TOKEN=your_b...ere" > .env
echo "ANTHROPIC_API_KEY=your_a...ere" >> .env

# Start Claude Code
claude
```

Step 3 - Build your bot's core features

The prompt that builds a complete moderation bot:

```yaml
Build a Discord moderation bot in Python using discord.py.

Features:
1. /warn @user [reason] — warns a user, logs to #mod-logs channel
2. /mute @user [duration] [reason] — mutes user for X minutes
3. /ban @user [reason] — bans with DM notification to user
4. Auto-delete messages with slurs (configurable word list)
5. Anti-spam: mute users who send 5+ messages in 3 seconds
6. /warnings @user — shows warning history for a user
7. All actions logged to a dedicated #mod-logs channel

Store warning data in a local JSON file (warnings.json).
Use discord.py v2.x with app_commands (slash commands).
Include proper error handling and permission checks.
Bot needs: Ban Members, Manage Roles, Manage Messages permissions.
```

The prompt that builds a full economy bot:

```yaml
Build a Discord economy bot in Python.

Features:
- /balance — shows user's coin balance
- /daily — collect daily reward (500 coins, 24hr cooldown)
- /work — random job earns 50-200 coins (1hr cooldown)  
- /shop — displays items for sale
- /buy [item] — purchase item with coins
- /give @user [amount] — transfer coins between users
- /leaderboard — top 10 richest users in server
- /gamble [amount] — 50% chance to double or lose coins

Store all data in SQLite database (economy.db).
Use discord.py v2.x slash commands.
Cooldowns stored per-user per-server (works across multiple servers).
Include admin commands: /addcoins @user [amount], /resetcoins @user
```

Step 4 - Add AI features (this is where the money is)

The prompt that adds Claude-powered AI to any bot:

```yaml
Add AI features to my existing Discord bot.

New commands:
- /roast @user — Claude writes a funny roast of the mentioned user
  based on their recent messages in the server
- /summarize — Claude summarizes the last 50 messages in the channel
- /ask [question] — Claude answers any question
- /vibe — Claude analyzes the current conversation mood
- /advice — Claude gives life advice based on a user's message history

For /roast and /vibe:
- Fetch last 20 messages from the channel using channel.history()
- Pass them to Claude with context about which user is being roasted
- Claude returns response, bot posts it

Use claude-haiku-4-5-20251001 for all commands (fast + cheap).
Add rate limiting: each user can use AI commands once per 30 seconds.
```

Step 5 - Deploy (your bot needs to run 24/7)

```powershell
# Option 1: Railway (easiest, $5/month)
# 1. Push code to GitHub
# 2. Connect Railway to GitHub repo
# 3. Add environment variables in Railway dashboard
# 4. Deploy — Railway runs it forever

# Option 2: Fly.io (more control, free tier available)
fly launch
fly secrets set DISCORD_TOKEN=***
fly secrets set ANTHROPIC_API_KEY=***
fly deploy

# Option 3: VPS (cheapest long-term, $4/month DigitalOcean)
# SSH into server, clone repo, run with screen or systemd
```

6/

## The prompts that build every type of bot.

Welcome bot (every new server needs this):

```yaml
Build a Discord welcome bot in Python.

When a new member joins:
1. DM them a personalized welcome message with server rules
2. Post in #welcome channel: "[user] joined! We now have X members"
3. Auto-assign "Member" role
4. If server has verification: assign "Unverified" role first,
   remove it when they react with ✅ to the rules message

When a member leaves:
- Post in #goodbye channel: "[user] left. X members remaining"

Include a /setwelcome command for admins to customize the message.
Store custom messages per-server in welcome_config.json.
```

Ticket support system:

```yaml
Build a Discord ticket/support bot in Python.

Commands:
- /ticket [issue] — creates private channel #ticket-[number]
  visible only to user + support team role
- /close — closes ticket (archives channel, posts transcript to #logs)
- /adduser @user — adds user to existing ticket
- /priority [low/medium/high] — sets ticket priority

Auto-features:
- First response time tracking
- Daily summary of open tickets posted to #mod-logs
- Auto-close tickets inactive for 48 hours (with warning)

Store ticket data in SQLite. Ticket IDs increment globally.
Support team = anyone with "Support" role.
```

Giveaway bot:

```yaml
Build a Discord giveaway bot in Python.

/giveaway [prize] [duration] [winners] [channel]
- Creates embed with prize info and end time
- Users react with 🎉 to enter
- Bot picks random winner(s) at end time
- Announces winner(s) in same channel
- DMs winners with congratulations

/reroll [message_id] — picks new winner from same giveaway
/giveaway-end [message_id] — ends giveaway early

Duration format: 1h, 30m, 2d
Multiple winners supported (comma-separated @mentions)
```

7/

## The real numbers. What's realistic.

```powershell
Realistic timeline — custom bot freelancing:
Week 1:    Learn the workflow (Claude + discord.py)
Week 2:    Build first bot for free (portfolio piece)
Week 3:    First paid job — $150-300
Month 2:   2-3 jobs/month — $400-900
Month 3+:  Specialization + reputation — $1,000-3,000/month

Realistic timeline — bot SaaS:
Month 1:   Build and launch on Top.gg, 5-10 servers
Month 2-3: 20-50 servers, first paying customers
Month 4-6: 100-200 servers, $500-1,500 MRR
Month 6+:  300-500 servers, $2,000-5,000 MRR
```

Where to find first clients:

```plaintext
r/discordapp         — "Bot Request" posts daily
r/discordbots        — active community
Discord.gg/Discord   — official server has job board  
Fiverr               — "Discord Bot Development" category
Top.gg               — post your bot, inbound requests come
```

The metric that matters: For SaaS bots - server retention after 30 days. If servers kick your bot within a month, it's not solving a real problem. Over 70% 30-day retention means you have something worth scaling.

What Claude can't do:

The code is covered. You still need to understand the Discord communities you're selling to. A moderation bot for a gaming server needs different features than one for a crypto trading community. The code is the same. The understanding of what features matter - that's yours.

8/

## The full stack.

```plaintext
IDEA:        Claude analyzes Discord server needs,
             identifies high-demand bot categories

BUILD:       Claude Code writes complete Python bot
             (commands, events, database, API calls)

CONNECT:     Claude Code Channels links directly to Discord —
             build and test inside the same platform

DEPLOY:      Railway or Fly.io — $5/month, runs 24/7,
             automatic restarts on crash

DISTRIBUTE:  Top.gg listing, r/discordapp, Fiverr

MONETIZE:    Stripe for subscriptions (discord-py-ext-ipc),
             or Top.gg premium listing,
             or Discord Server Subscriptions

ITERATE:     Claude reads error logs, fixes bugs,
             adds features based on server owner requests

SCALE:       One codebase, 500+ servers,
             Claude maintains all of it
```

The only step that requires you: finding server owners who need what you're building, and talking to them.

The window.

771 million Discord users. 94 minutes per day average. A platform filing for IPO in 2026 with $725M ARR that runs on bots.

Midjourney never built a website for their first year. They built a Discord bot. $2.5 million per month.

Claude Code now connects directly to Discord through official Channels support. You build, test, and deploy inside the same platform where your users live. The Python knowledge barrier is gone. The async programming barrier is gone. The Discord API complexity barrier is gone.

Custom bots sell for $200-1,000 each. Bot SaaS scales to thousands of servers. Server subscriptions pay recurring monthly income.

One good bot. One real problem solved for a community that needs it. Claude writes every line.

Where to start:

- Discord Developer Portal: discord.com/developers/applications

- discord.py docs: discordpy.readthedocs.io

- Top.gg (distribution): top.gg

- Railway (hosting): railway.app

- Claude Code Channels docs: docs.anthropic.com/en/docs/claude-code/channels

---

// The window is open. Follow - I'll keep finding them before they close //
