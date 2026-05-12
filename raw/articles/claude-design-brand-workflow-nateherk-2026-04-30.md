---
title: "Claude Design Built My Brand End to End (without hitting limits)"
source: "x-bookmarks"
tweet_id: "2049671370099826725"
tweet_url: "https://x.com/nateherk/status/2049671370099826725"
author_name: "Nate Herk"
author_handle: "@nateherk"
tweet_date: "Thu Apr 30 02:05:10 +0000 2026"
bookmark_date: "2026-04-30"
content_type: "x_article"
character_count: 11989
retweet_count: 30
like_count: 336
type: article
tags: [ai-design, design, workflow, agent, brand, content]
---

# Claude Design Built My Brand End to End (without hitting limits)

Claude Design Built My Brand End to End (without hitting limits)

## I Burned $500 in Extra Usage on Claude Design

Anthropic dropped Claude Design and the weekly limits are no joke. I burned through my Max 20x quota in a day, then bought top-up after top-up trying to figure out what actually works.

I'm going to show you exactly what I built (a full brand from scratch called Tally) and exactly how to stretch your usage so you don't make the same expensive mistakes I did.

Pitch deck, landing page, mobile app prototype, animated launch video, deployed live to Vercel. Everything on brand. Everything from natural language.

Here's the playbook.

## What Claude Design Actually Is

Anthropic released Claude Design on April 17, 2026, the day after Opus 4.7.

Think of it as a polished cousin to Claude Code, built around vision instead of code execution. Same model muscle, different surface.

It runs on Opus 4.7, which has the strongest vision in the lineup. After every render, Claude Design screenshots the output, looks at the page, finds anything broken, and fixes it before you even see the issue. That self-validating loop is the killer feature.

You can build prototypes (wireframe or high fidelity), slide decks, landing pages, animated promos, mobile mockups, and short brand videos. Anything visual.

Quick context that explains why this thing landed so polished. Krieger left Figma's board right before the Claude Design announcement and joined Anthropic as CPO. The pedigree is in the product.

## Plans, Limits, and Why It Burns Fast

Claude Design is paid only. Pro, Max 5x, and Max 20x all get different weekly quotas, and that quota is separate from your regular Claude and Claude Code usage.

This caught me off guard at first. Design eats tokens hard, especially on Opus 4.7. I'm on Max 20x at $200 a month and burned through 30% of my weekly quota just on a design system and a pitch deck.

If you blow through it, you wait for the weekly reset or pay for top-up usage from your billing balance. Top-ups work, but they get expensive if you're not careful.

The biggest myth is that you should always start with a wireframe. For some projects that's true. For others it's a pure waste. I burned 4% of my weekly quota generating wireframes for the Tally landing page, then realized I already knew the layout I wanted. I scrapped them and went straight to high fidelity. Zero regret.

The lesson. Know what you want before you open Claude Design. Every minute you spend ideating in Design is session burned.

## Start Every Project With a Design System

This is the move that changed everything for me.

A design system in Claude Design holds your colors, typography hierarchy, spacing rules, button styles, hover states, badges, tags, cards, input fields, and icon set. It generates a Design.md spec that becomes the source of truth for every project after.

I built one for AI Automation Society by giving it the website URL plus the GitHub repo. It scraped both, pulled the brand DNA, and produced a spec I now reuse for every video, slide deck, and landing page we ship internally. On a team plan, the system shares across the whole org.

For Tally I had no website yet. I gave it three things:

→ A logo PNG

→ A markdown brand concept doc with mission, audience, color palette, and typography

→ A short note about button feel ("modern, slight glow behind them, very polished")

It generated the system in 5 to 10 minutes. The first pass had issues, mainly the logo getting subtly redrawn instead of preserved. I gave feedback ("the logo is not appearing as it should, keep the PNG exactly as is"), and it fixed it.

Two things to internalize. The verifier agent is real. Claude Design is genuinely looking at what it built and correcting itself. And once the system is locked, you can export the whole thing as a zip and hand it to Claude Code. Same brand, two surfaces.

## Brainstorm in Chat, Execute in Design

This is the single biggest lever for stretching your session.

Don't brainstorm inside Claude Design. Ever. The Design surface is for executing a known brief, not for figuring out what the brief should be.

For Tally I brainstormed the entire brand in regular Claude first. Mission. Audience. Color palette. Typography. Logo concepts. Voice and tone. By the time I opened Claude Design, I had a 372-line markdown doc that was the entire spec.

I also used GPT Image 2 alongside Claude as a logo and brand-guidelines partner. Claude designed the actual brand. GPT Image 2 mocked up logo variations and a one-page brand guidelines visual. It struggles with specific fonts (Roboto Mono and Montserrat both got bent) but the layout was usable enough that I just dropped the official fonts in via Canva.

Same pattern for the pitch deck. I asked regular Claude for the deck outline plus market research before ever opening Design. That move alone saved me roughly 8% of my weekly quota.

Treat AI like a specialist. Each chat gets one job. Don't ask the design tool to also be your strategist.

## The Brand-to-Build Pipeline

Once the design system was locked, I ran the same playbook six times.

1️⃣ Investor pitch deck. Slide deck mode plus the brand markdown plus the outline I built in Claude chat. The verifier agent caught issues on slides 6 and 10 automatically and fixed them before I saw the deck. Final result felt like something a real founder could walk into a VC meeting with.

2️⃣ Landing page wireframes. Three mid-fidelity concepts, mostly light with one dark. The "decide for me" option pushed me to pick distinct vibes (editorial, documentation, modern fintech). Useful for exploring directions, but I already knew what I wanted. Skippable in retrospect.

3️⃣ High-fidelity landing page. Started fresh. Built the full site with hero, weekly digest preview, comparison table, FAQ, and founder note. I generated a logo loop video in Kling (start frame: bone background blink, end frame: the Tally mark) and dropped the MP4 into the hero section so it animates on the right side. The result feels alive without being heavy.

4️⃣ Brand guidelines doc. Built in two minutes from the design system. Now reusable for any future asset.

5️⃣ Mobile app prototype. Same approach, multiple screen states, dark mode iterations. Skipped wireframes and went straight to high fidelity. Faster, cleaner.

6️⃣ Launch video using the HyperFrames skill. This was the surprise. Real motion graphics. Animated text. Scene transitions. Built inside Claude Design from a single prompt because HyperFrames (built by a creator named Haegeon) injects animation primitives into Design.

Every output landed in the same visual world because they all pulled from one design system. That's the unlock. You're not building one-offs anymore. You're building a brand machine.

## The Editing Surface Is the Quiet Superpower

Most people only use the chat panel. That's a token sink.

Claude Design has three editing surfaces inside the canvas, and learning all three is the difference between burning your quota in a week and stretching it across a month.

→ The edit tool. Click any element directly. Change text, color, sizing, padding. Claude applies the change without you having to describe it in a prompt. This is the cheapest edit in the app.

→ The draw tool. Circle a region of the screen, type a comment, send. Claude takes a screenshot, sees the circled area, and acts on it. Useful for non-element things like "make this gradient lighter" or "this section feels heavy."

→ The tweaks panel. Pre-built variations for cover style, background texture, accent colors, and slide chrome. One toggle and the whole deck updates. Massive session saver when you're exploring directions instead of committing to one.

The general rule. If you can change it without prompting, change it without prompting.

## Ship It With Claude Code and Vercel

Designing is half the job. Shipping is the other half.

For the final live build I used Claude Design's "hand off to Claude Code" flow. Two options:

→ Click Share → Download as zip. Extract into a folder, open it in VS Code, run Claude Code there.

→ Click "Hand off to Claude Code." It generates a command. Copy, paste into Claude Code, it pulls the project automatically.

The second option had a 404 error the day I recorded. Use the zip if it's broken.

From Claude Code:

1️⃣ Tell it "this is a website project, push it to a private GitHub repo." If you've already authorized GitHub with Claude Code, it ships immediately. If not, Claude Code will pop the auth flow.

2️⃣ Test on local host first. localhost:3000 (or whatever port). Make sure the site actually renders before you push live.

3️⃣ Connect Vercel. Sign in with GitHub, click Add New → Project, select the repo, click Deploy. 60 seconds later it's on a real domain.

The annoying part. Vercel served a 404 on first deploy because the build was nested in a folder instead of at repo root. Claude Code spotted it instantly, renamed the entry to index.html, pushed the fix, Vercel auto-redeployed. Live again.

Two more things to flag if you do this:

→ Test mobile view before deploying. Claude Design optimizes for desktop by default. Hit F12 in Chrome, switch to mobile mode, check what breaks, and tell Claude Code to fix it. Claude Design and Claude Code don't auto-optimize for mobile, but they'll do it if you ask.

→ Local host URLs are yours alone. If you send someone localhost:3000, they see whatever's on their own machine. Always deploy before sharing.

Custom domain takes about five minutes if you want to ditch the .vercel.app URL. Claude Code can walk you through it.

## How to Stretch Your Weekly Limit

This is the part most tutorials skip. Here's the playbook I run now.

→ Brainstorm and outline in regular Claude chat. It's a separate limit. Treat that chat as the planning room.

→ Drop a tight markdown spec into Claude Design before you ever hit generate. The more context up front, the less iteration you'll burn.

→ Use Opus 4.7 for the planning prompt. Switch to Sonnet 4.6 for tweaks. I built full slide decks and animated assets on Sonnet 4.6 with no quality drop, as long as the spec was tight.

→ Edit and tweak in the canvas. The three editing surfaces above save more session than any prompting trick.

→ Reference real designs by name. "Linear 2023 with higher density" beats "make it clean." "Modern fintech, light bone background" beats "make it minimal."

→ Tell Claude Design what you don't want. Negatives save you a correction round.

→ One major change per prompt. Mega-prompts only land 1 or 2 of the asks. The rest get dropped.

→ Watch the build live. The to-do list and the verifier agent give you visibility. If it's heading the wrong direction, stop it. Letting Claude Design build for ten minutes down the wrong path is the most expensive mistake you can make.

A few quirks worth knowing:

→ File uploads cap around 30 to 40MB. Don't try to drop in a 5-minute video.

→ Long threads pollute context. I haven't proven /clear actually wipes the context window, but exporting and reopening with a fresh session is the safe move when threads get heavy.

→ Design systems with full GitHub repos eat way more tokens than design systems with just a logo and a markdown spec. Give Claude Design exactly what it needs, no more.

If you hit the wall, export. Zip the project, drop it into Claude Code, keep iterating there until your Design quota resets. You don't lose progress. You change surfaces.

## Wrap

Claude Design isn't replacing Figma. It's replacing the gap between an idea and a shipped brand.

Plan in chat. Execute in Design. Ship from Code. Three surfaces, one workflow, one design system glueing them together.

The people getting real value out of this aren't the ones treating it like a chat box. They're the ones treating it like a specialist with its own context, its own quota, and its own role in a larger pipeline.

I walk through every step in the full video. Link in the first reply.