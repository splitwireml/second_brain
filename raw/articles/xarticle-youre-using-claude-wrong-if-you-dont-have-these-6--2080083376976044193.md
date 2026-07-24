---
source_url: https://x.com/aiwithremy/status/2080083376976044193
ingested: 2026-07-24
sha256: a60cbce9f7f8fbdef9118a00684ec11741e8b09140850fc02f433bd744048715
---
---
title: "You're Using Claude Wrong If You Don't Have These 6 MCPs"
source: "x-bookmarks"
tweet_id: "2080083376976044193"
tweet_url: "https://x.com/aiwithremy/status/2080083376976044193"
author_name: "AI with Remy | Learn AI"
author_handle: "@aiwithremy"
tweet_date: "Thu Jul 23 00:11:37 +0000 2026"
bookmark_date: "2026-07-23"
content_type: "x_article"
character_count: 9254
retweet_count: 0
like_count: 4
external_urls:
  - "https://aiwithremy.com/)"
  - "https://awr-gamut-exploration.vercel.app/self-paced#reserve)"
  - "https://awr-gamut-exploration.vercel.app/enterprise)"
---

# You're Using Claude Wrong If You Don't Have These 6 MCPs

You're Using Claude Wrong If You Don't Have These 6 MCPs

an ai education business, an ecom brand, and a marketing agency I ran for two years before exiting it last year. all of it runs almost entirely out of claude. none of it works the way it does without six specific tools plugged in underneath it. here's exactly what they are and what they actually do.

---

## what an mcp actually is, in plain terms

before mcps existed, getting claude to actually do something in another app meant custom programming, api work, real technical lift. claude speaks english. gmail speaks french. notion speaks spanish. slack speaks chinese. your browser speaks japanese. teaching claude to speak all of those languages directly takes forever.

mcp stands for model context protocol, built by anthropic, and it's the translator sitting between claude and every tool. claude still only speaks english. the tools still only speak whatever they speak. claude makes a call to the mcp server, the server translates it, and the tool just works. that's the entire mechanism. anyone talking about "a notion mcp" or "a gmail mcp" is just describing that same translator layer pointed at a different tool.

all six of these work in claude chat, claude code, and cowork. cowork's the better default of the three, more agentic, better at actually getting things done rather than just talking through them.

six of these are non negotiable.

---

## 1. n8n, for building and running actual automations

n8n is a workflow automation tool, same category as zapier or make. the mcp lets claude build client automation workflows directly, and it doesn't stop at building, it can run them too.

a real test of this: create a workflow that runs every day at 7am and emails the weather for melbourne, using the n8n mcp to build it. claude wrote the plan, listed the nodes, built the whole thing, and it went live in n8n without ever manually opening the platform.

it also handles real business infrastructure, not just demos. one live workflow triggers off a webhook the moment someone enters their email on a lead magnet landing page, and automatically sends the lead magnet straight to their inbox. built entirely inside claude, no manual setup inside n8n itself.

most client automation work now runs through this exact loop. plan with claude first, spend maybe 10% of total time on the actual build once the plan's approved. the planning is the real work. the build is fast once the plan's right.

---

## 2. nano banana, for realistic product and ad imagery

nano banana is currently one of the strongest image generation models available, particularly for realistic looking shots and text heavy creative like ads. connect it through the mcp and claude generates images directly instead of just describing what an image should look like.

a quick test of it: write an image prompt for a lobster sitting on top of a mac mini, then generate it directly through the nano banana mcp. one instruction, no separate tool, no copying a prompt somewhere else. this is also the exact same model behind the full ecom product shoot workflow built for a furniture store, one reference photo turning into a complete shoot, editorial angle, close ups, technical drawing, catalog piece, run across an entire product catalog.

---

## 3. firecrawl, for anything a normal web search can't touch

claude can already search the web without help. what it can't do without firecrawl is actually extract content from a specific page, scrape a google doc, or pull structured data off a website. firecrawl fixes that gap entirely.

a real example: point it at a landing page and ask for a full breakdown, the branding, the fonts, a cro audit identifying what's hurting conversion. it came back with the full color palette, the design philosophy, specific headlines that were working, and a list of real issues, no pricing above the fold, an ignored section, exact color values. that's not a summary of the page. that's an actual audit, generated automatically.

it also handles things a normal web search flat out can't reach. asked to scrape three separate google docs and save each one as its own markdown file, it just did it, no manual copy pasting, no exporting first. most of the time it reaches for firecrawl on its own now, without needing to be told to.

---

## 4. perplexity, for research without ever leaving claude

before this mcp, research meant a completely separate perplexity subscription, a new session with zero context about whatever was already happening in claude, doing the research, then manually bringing it back over. genuinely annoying, every single time.

the perplexity mcp removes that step entirely. a weekly research agent, one piece of a small newsletter team built specifically for this, an email designer agent and a research agent working alongside each other, fires off perplexity searches directly inside the same conversation to find what's new in ai over the past seven days. no context lost, no separate tab. any research now happens exactly where the work's already sitting.

---

## 5. apify, for scraping literally anything

apify is a library of scrapers, google maps, tiktok, ecom, reddit, comment threads, lead lists, thousands of them. if only one mcp could ever get set up, this would probably be the one purely on breadth alone.

a real test of it: point it at a competitor's x account and ask for a full breakdown, top performing posts, writing style, what's working, what isn't. it came back with follower data, 21 posts analyzed with full metrics, and a genuine writing style breakdown. there's also a custom skill built on top of this specifically for turning any x thread or article link straight into a clean document.

---

## 6. playwright, for anything that needs an actual browser

playwright gives claude direct access to a real browser, which matters most for platforms with no api available at all. linkedin is the clearest example, connection requests and outreach are heavily restricted there, no clean automation path exists through official channels.

with the mcp connected through a browser extension already logged into a real account, claude can navigate to a specific profile, find the actual connect button, not the follow button, and send a request with a personal note attached. watched it happen in real time, click by click, find the button, add the note, send. genuinely funny watching an agent do something this fiddly correctly on the first try.

it also pairs well with firecrawl specifically, anything too large or too dynamic for firecrawl to scrape cleanly, playwright picks up instead, since it's working through an actual browser rather than pulling raw page content.

the honorable mentions, worth setting up if you already use these

→ supabase, the backend for web apps and websites, claude handles it directly without ever opening the dashboard

→ github, for managing code across apps and websites

→ notion, still useful for anything that needs to stay publicly visible, even while migrating most notes elsewhere

→ cal.com, for scheduling

→ stripe, for invoices and payment links generated directly through claude

---

## setting these up is easier than it sounds

the actual install process intimidates people more than it should. for claude code specifically, mcps get added inside a single file called claude.json. claude chat and cowork work off a completely different location, a desktop config file reached through developer settings. a fair number are already available pre built inside settings without any manual config at all.

for the custom ones, the actual move is simple: paste the mcp's documentation link straight into claude and ask it to walk through the setup step by step. hit an error along the way, copy the exact error message back into the same chat, and it keeps walking through the fix. that habit, defaulting to asking claude how to do something instead of guessing, ends up mattering more than any individual tool on this list.

---

## why this actually matters

context and skills get most of the attention, but none of it moves anywhere without the tools layer connecting claude to the outside world in the first place. the model can be as sharp as it wants. without a way to actually reach gmail, a website, a browser, an ad account, it's just a very smart conversation with no hands.

six tools, properly connected, turned an entire business, education, consulting, ecom, into something that runs almost entirely from one interface. that's not a coding project. that's an afternoon of setup, done once.

p.s. if you want the exact install links and step by step setup for all six, grab the full guide through the newsletter at [aiwithremy.com](https://aiwithremy.com/)

and if you want a complete system built around your entire business, not just six tools, that's what the AI course hands over. reserve your seat here → [awr-gamut-exploration.vercel.app/self-paced#reserve](https://awr-gamut-exploration.vercel.app/self-paced#reserve)

running a team of 20 or more and need this rolled out company wide instead of just for yourself? that's a different scope entirely → [awr-gamut-exploration.vercel.app/enterprise](https://awr-gamut-exploration.vercel.app/enterprise)

remy
