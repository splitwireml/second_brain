---
title: "How to find & fix what's killing your sales (with the Claude Buyer Simulation skill)"
source: "x-bookmarks"
tweet_id: "2047668468904808531"
tweet_url: "https://x.com/itsolelehmann/status/2047668468904808531"
author_name: "Ole Lehmann"
author_handle: "@itsolelehmann"
tweet_date: "Fri Apr 24 13:26:21 +0000 2026"
bookmark_date: "2026-04-24"
content_type: "x_article"
character_count: 8993
retweet_count: 3
like_count: 103
external_urls:
  - "https://github.com/olelehmann1337/claude-skills/blob/main/skills/buy-or-bounce/SKILL.md)"
  - "https://aisolopreneur.lpages.co/claude-cowork-workshop/)"
---

# How to find & fix what's killing your sales (with the Claude Buyer Simulation skill)

How to find & fix what's killing your sales (with the Claude Buyer Simulation skill)

Whatever you use to sell, your landing pages, your emails, or your ads, it all makes perfect sense to you. Because you made it.

But your audience sees something completely different.

So I built a skill that simulates 5 different buyer personas reading whatever you give it, section by section.

It tells you exactly who would buy, who wouldn't, and what to fix so more people convert.

In this article I'll show you exactly how to set it up.

Here's the method and the exact skill I built, so you can run it yourself:

P.S. If you want more AI workflows like this one delivered to your inbox every week, join 37k readers getting them free:

aisolo.beehiiv.com/subscribe

## You'll never see what your buyer sees

Of course it all makes sense to you. You know the product inside out:

- the page

- the emails

- the backstory

- the pricing logic

- why it's worth every dollar

But your buyer has none of that context.

They came to your page after a long day of getting hammered by their boss, fresh off 45 minutes of doomscrolling Instagram.

They're skimming with half their attention. So the second something doesn't add up, they're gone.

All you get back is a conversion rate: a number that says something is wrong but never says what.

And every day that page is live with those blind spots, you're:

- Spending ad dollars sending people to something that's leaking

- Burning audience trust with an offer that confuses them

- Losing sales you'll never know you lost

…all because of a vague headline or a missing proof point you couldn't see from the inside.

You need simulated buyers who can test it from the outside.

## Where this comes from

Shopify had this exact problem at scale.

A merchant changes their storefront. How do they know if it converts better?

The old way: A/B test it, but then you have to wait weeks. And it’s ineffective for small merchants because they don't have enough traffic for testing to work at all.

So Shopify built SimGym. They send hundreds of simulated shoppers to browse a merchant's store. Each shopper has a persona, a budget, and a shopping intent.

Each runs in a real cloud browser, sees the page, decides what to do, clicks, scrolls, adds to cart, or leaves. Basically: a simulated A/B test in minutes instead of weeks.

I rebuilt the concept as a Claude skill. Same idea: simulate buyers walking through whatever you're putting in front of people and reporting back what they'd actually do.

Their version runs on dedicated AI infrastructure that costs millions.

This one is free, gets you the 80/20 result, and runs inside Claude in about 3 minutes.

I call it "buy or bounce."

## The 5 buyers

Each buyer represents a different reason people don't convert.

The Shut-up-and-take-my-Money Buyer Has the problem, has the money, and is actively shopping. If they bounce, something fundamental is broken. This Buyer is your canary. If they won't convert, nobody will.

The Skeptic Been burned before. Every bold claim triggers their BS detector. Scanning for proof: specific numbers, case studies, guarantees, anything that separates real from hype.

The Price-Conscious Buyer Wants the outcome but doing the math on whether it's worth the money the entire time. They need the value to clearly and obviously exceed the cost.

The Confused Visitor Found your page but genuinely can't tell what this is or if it's for them. They'd buy if they understood the offer (and this is the most common and most fixable problem).

The Comparison Shopper Evaluating 2-3 alternatives. Reading your page with one question: "Why this and not that?"

These 5 map to the core reasons people don't buy: broken fundamentals, missing credibility, weak value justification, unclear positioning, no differentiation.

## Why section-by-section matters

This is what separates buy or bounce from just asking Claude to review your page.

Each buyer reads what you give it top to bottom and narrates their internal monologue at every section:

- "Okay, this headline grabs me, I have this problem..."

- "Wait, what does 'transform your workflow' actually mean? That's vague..."

- "These features sound nice but how is this different from the other 3 things I'm looking at..."

- "That price is higher than I expected for something I still don't fully understand..."

- "I'm not clicking this."

You see the exact moment each buyer's interest dies.

And because all 5 walk through the same material, it maps where the friction clusters. If 3 out of 5 bounced at the same section, that's your biggest leak.

Then it tells you exactly what to fix, in what order, with specific rewrite suggestions.

## How to set it up

1. Grab the skill [here](https://github.com/olelehmann1337/claude-skills/blob/main/skills/buy-or-bounce/SKILL.md). Drop it into your Skills in Claude Code or Cowork (Customize > Skills > Add skill).

2. Say "buy or bounce this" and paste whatever you want tested. Landing page URL, email, sales page, ad creative, whatever you're trying to get someone to say yes to.

3. The skill parses it into sections, spawns all 5 buyers in parallel, and each one walks through narrating their buying decision.

4. You get a visual HTML report: conversion score, section-by-section friction map, prioritized fixes with specific rewrites, and full buyer walkthroughs if you want to dig in.

## What happened when I tested my own landing page

I ran buy or bounce on one of my workshop landing pages (now closed, but you can view the page here: https://aisolopreneur.lpages.co/claude-cowork-workshop/)

3 out of 5 would buy. 2 on the fence. Nobody bounced.

1. The Shut-up-and-take-my-Money Buyer converted. The "click-by-click" promise in the subheadline hooked them, and the testimonials sealed it. Angelo going from 5 figures on web designers to doing it himself in hours, Tanya taking a landing page from concept to live in under 2 hours.

2. The Price-Conscious Buyer converted. They did the math: if $197 saves even one project that would've cost $2-5k in freelancer fees, the ROI is obvious. Their words: "If even half of those results are real for me, $197 pays for itself on the first project."

3. The Comparison Shopper converted. They'd seen other AI courses and YouTube tutorials but none showed specific, measurable outcomes from real students.

4. The Skeptic was on the fence. The testimonials and proof story were credible enough to get past initial skepticism, but they wanted to actually see video proof of the 8-minute landing page creation before committing $197. If the story holds up on camera, they're buying.

5. The Confused Visitor was on the fence. They understood what the workshop teaches you to do, but never fully grasped what Claude Cowork itself is. Is it software? A framework? A way of prompting?

Then the synthesis mapped the patterns and gave me specific advice:

- Add one plain-language sentence early on the page explaining what Claude Cowork actually is. The Confused Visitor couldn't tell if it's software, a framework, or a method.

- Add a video demo or screenshots showing the 8-minute landing page creation. The Skeptic needed to see it, not just read about it.

- Double down on testimonials with specific cost/time savings. Angelo's 5 figures saved and Tanya's 2-hour turnaround did the heavy lifting for 2 buyers.

- Clarify the "10M+ people" claim in the subheadline. Multiple buyers couldn't tell if it's my reach or a promise about what they'd achieve.

- Replace the "falling behind" stakes section with aspiration-based framing. 2 buyers came in curious, not panicked, and the fear angle pushed them away.

A prioritized list of what to fix and in what order. All in about 3 minutes.

P.S. If you want to implement AI workflows like this into your business, get them 100% free in your inbox here: aisolo.beehiiv.com/subscribe

## What else to test

Buy or bounce works on anything where you're trying to get someone to say yes.

- Landing pages before you drive traffic. Find what's broken before you spend money on a page that leaks.

- Email sequences before you hit send.

- Ad creatives before you spend budget. Ads have about 2 seconds to make sense to someone who's never heard of you.

- Sales pages before launch.

- Proposals and pitch decks before the meeting.

## Go test something

Think about the page, email, or ad you're about to publish. The one you've been going back and forth on.

Buy or bounce it. Grab the skill here. Say "buy or bounce this" and paste what you want tested.

3 minutes from now you'll know exactly where your buyers would drop off, what's confusing them, and what to fix first so more people actually buy.

P.S. If you want more AI workflows that help you get more customers, more attention, and more done (without working more hours)...

I send them to 37k readers every week for free. Plus you get a free Claude Cowork masterclass when you join: aisolo.beehiiv.com/subscribe
