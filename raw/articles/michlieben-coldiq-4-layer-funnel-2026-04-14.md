---
updated: 2026-04-17
title: 'Source: @michlieben — ColdIQ 4-Layer B2B Funnel Thread'
source: https://x.com/michlieben/status/2043743066146910683
type: post
author: michlieben
username: '@michlieben'
---

# Source: @michlieben — ColdIQ 4-Layer B2B Funnel Thread

**URL:** https://x.com/michlieben/status/2043743066146910683
**Author:** @michlieben (Michiel Lieben)
**Company:** ColdIQ
**Date:** 2026-04-14
**Type:** X/Twitter thread (original, long-form)

How We Built a $7M Funnel With 4 Layers (Most Companies Only Have 2)

Last year, our funnel produced 330,000 website visitors, booked 1,500+ meetings, and added $4M in new ARR. We crossed $7M ARR without raising a single dollar.

When I mapped the architecture behind those numbers, I found four distinct layers. Not channels or campaigns. Layers, each one feeding the next.

Most B2B companies between $1M and $10M only have two of them. That's the gap where pipeline goes to die.

---

# The 2-Layer Trap

Here's how the typical B2B funnel works.

Layer 1: Generate leads. You send cold emails, post on LinkedIn, maybe run some ads. People become aware you exist.

Layer 4: Close leads. Someone books a call, your sales team gets on Zoom, you send a proposal.

Two layers. Generate and close. That's the entire system for most B2B companies under $5M in revenue.

Everything between awareness and the sales call is a void. The prospect clicked your LinkedIn post last Tuesday and now they're on your calendar three weeks later.

You didn't capture, nurture, or score them. They showed up cold, skeptical, and already comparing you with three other vendors they found the same week.

If your only conversion mechanism is "book a call," you're losing everyone who isn't ready for a call right now. That's most people. And those people are the ones who would have closed two months later if you'd caught them.

Think about your own buying behavior.

When was the last time you saw a LinkedIn post, immediately booked a call with that company, and signed a contract? It almost never works that way.

You see the post. You check the website. You leave. 
Maybe you come back a week later. Maybe you don't.

If the company has no mechanism to capture you between that first touchpoint and the eventual decision, they're relying entirely on you remembering them and coming back on your own.

That's not a funnel. That's a coin flip.

---

# Layer 1: Lead Generation

We attracted roughly 330,000 unique visitors to our website in 2025. They came from five channels: automated outbound, LinkedIn publications, LinkedIn Ads, Google Ads, and SEO.

> The key insight: we don't run one channel. We run five, and each one feeds a different part of the funnel rather than dumping into the same pipe.

- Outbound uses Clay for enrichment and Instantly.ai for sequencing.

- Inbound runs through AirOps and Ahrefs for SEO.

- Ads are managed with Fibbler for attribution and LinkedIn for targeting.

- Content is published via Taplio and organized in Notion.

We ship two articles per week and attract over 100,000 visitors quarterly. Our SEO strategy isn't traditional content marketing.

- We build free mini-tools, host them on our domain, and create programmatic pages at scale using Claude Code and AirOps.

- Each tool solves a narrow problem for our ICP, ranks in search, and feeds prospects directly into Layer 2's capture mechanisms.

But the five channels aren't just running in parallel. They're coordinated.

Our team publishes 150+ LinkedIn posts per month across 24 people.

When a post generates meetings, we boost it via Thought Leader Ads at roughly $40 CPM, putting it in front of the exact accounts our outbound team is targeting.

So the prospect sees a LinkedIn post from one of our team members on Monday.

- They get a cold email from us on Wednesday.

- They see a retargeted ad on Friday.

- By the time they visit the website, they've already encountered ColdIQ three to five times across three separate channels, and each touchpoint reinforced the others.

We ran this coordinated approach for AirOps, a client whose pipeline had been stuck at roughly $536K per month for almost a year. We built a Layer 1 that combined outbound with LinkedIn Ads, hitting the same accounts from every angle.

The result: $7.8M in qualified pipeline and $1.5M in closed-won revenue from $233K in ad spend. That's a 15x pipeline ROI. 164 deals created and 1,058 outbound replies, all because the prospect was seeing AirOps content before the cold email ever landed.

Layer 1 is a coverage game. If five channels all hit the same prospect from different angles, the math on everything downstream changes before a single sales call happens.

---

# Layer 2: Lead Capture (The One Most Companies Skip)

This is the first missing layer. The one that separates funnels that plateau from funnels that compound.

Most companies go straight from "generate leads" to "book a call."

The website has a calendar link, sure. But if the prospect isn't ready for a call right now, they leave. You generated all that awareness for nothing because there was no mechanism to catch them on the way out.

At ColdIQ, we built three capture mechanisms for prospects who aren't ready for a sales call:

## Mechanism 1

> Lead magnets and mini-tools that collect email addresses in exchange for something useful.

We've built several using Claude Code and Lovable, hosted on Vercel. Each one solves a narrow, specific problem: a deliverability checker, a subject line analyzer, a cold email grader. 

A prospect gives us their email because the tool saves them real work, and now they're in our system even though they never booked a call. 

These mini-tools and the programmatic SEO pages we created around them now account for roughly 30% of our total website traffic through organic search.

## Mechanism 2

> De-anonymization technology that identifies website visitors who didn't convert.

- We run Instantly.ai, Midbound, and Vector to reverse-identify anonymous traffic on the website.

- We also use Trigify and Jungler to catch social interactions on LinkedIn, identifying prospects who engaged with our posts but never visited the site.

- All of these signals flow into a Clay table where every lead is automatically scored, segmented, and tiered.

- Tier 1 leads, the best fit with the highest intent, get manual personalized outreach.

- Tier 2 leads get multichannel sequences across email and LinkedIn.

- Tier 3 gets automated email only. The routing decisions are based on what the prospect actually did, not a static ICP checklist.

Here's what this looks like in practice.

- A VP of Sales at a $5M SaaS company reads three blog posts about Clay enrichment workflows on a Tuesday afternoon.

- Vector identifies them as a website visitor. Their company matches our ICP filters in the Clay table and they're scored as Tier 2: good fit, moderate intent.

- Wednesday morning, they receive a personalized email referencing Clay enrichment, not a generic pitch about our agency.

- Thursday, they see a LinkedIn post from one of our team members about a Clay workflow we built for a similar client.

- By Friday, they've encountered ColdIQ four times, and every touchpoint was relevant to what they actually care about.

That's what a capture layer does when it's wired properly.

## Mechanism 3

Video sales letters hosted through Wistia on Webflow that articulate the offer before the prospect ever speaks to a human. By the time they book a call, they already understand what we do, how we do it, and roughly what it costs. The sales conversation becomes a fit conversation, not a pitch.

We also use Default for inbound lead routing. When someone enters their email on our website, Default enriches the data on the backend: company size, industry, role, revenue. If they qualify, they see our calendar immediately. If they don't, they're routed to a longer form. One input field for the prospect, zero friction, and the qualification happens automatically behind the scenes without them filling out a 12-field form.

Layer 2 is what turns a "book a call" button into a system that captures demand even when the timing isn't right. And once a prospect is captured, they enter the layer where the real compounding starts.

---

## Layer 3: Lead Management (The Other One Most Companies Skip)

This is the second missing layer. And it's the one that changed my entire understanding of what content is for.

> Leads should never leave your world. They should orbit in it until they're ready to buy.

Early on, I treated content purely as a lead generation tool. Write posts, get followers, hope they book a call. That stopped working quickly because content alone doesn't convert. A LinkedIn post isn't a sales pitch, and a reader isn't a lead.

The shift came when I realized content is a lead management tool. In the beginning, you don't want to treat content as a way to generate inbound leads, but as a way to create trust, which will make your outbound campaigns convert better. That distinction changed everything about how I planned what to post and when.

Layer 3 is what happens after you capture a lead but before they're ready to convert. It has four components:

1. Outreach campaigns to warm leads. These aren't cold blasts. They're targeted sequences to leads who already engaged with content or visited specific pages, scored using Clay with OpenAI and Claude running classification. A prospect who watched 80% of a VSL about our Clay workflows gets a different sequence than someone who downloaded a cold email template. The messaging maps to what they actually demonstrated interest in, not a generic pitch sent to everyone.

2. Newsletter nurture. Roughly 10,000 active subscribers through beehiiv with open rates above 40%. We also built a welcome sequence: the moment someone signs up, they receive the resource they requested within one minute. Three days later, they get an email about the tool stack we use to run our outbound. A few days after that, another email with a specific workflow they can steal. The sequence educates and builds familiarity with how we think. Every edition is designed to keep ColdIQ in the prospect's mental orbit. Not selling. Teaching. When they're ready to buy, they remember who was useful when they weren't.

3. Email marketing sequences via Customer.io, triggered by specific behaviors. Downloaded a lead magnet. Watched a VSL past the 60% mark. Visited the pricing page twice. Submitted an application form but didn't complete the booking. That last trigger is one of our most important: when someone applies for one of our programs but doesn't finish, a follow-up goes out 30 minutes later with a direct link to complete, and if they don't respond, another email follows the next day with useful resources to build trust while they're considering. Each behavior trigger maps to a different intent level, and each intent level gets a sequence designed specifically for it.

To give you a sense of the sophistication: we have separate workflows for prospects who visited our pricing page versus prospects who read our blog. A pricing page visitor is further down the funnel and gets a direct offer email within hours. A blog reader gets an educational sequence that builds toward the offer over multiple touches. The system handles this routing automatically based on which pages they visited and in what order.

4. LinkedIn content nurture at scale. Our team posts consistently across 24 accounts with a combined following above 300,000. Last year, we ran an internal LinkedIn competition: $5,000 for first place, $2,500 for second, $1,500 for third, and $500 to every team member who published 20 or more times in the quarter. The result was 581 posts from 24 people, 27 new clients signed, and $151,000 in new monthly recurring revenue added within 90 days. We're running the competition again this quarter with even larger prizes.

LinkedIn Ads play a direct role in Layer 3 as well. We use Thought Leader Ads to pre-warm the exact accounts our outbound team is targeting.

[Embedded Tweet: https://x.com/i/status/2043682968745705697]

A prospect who has seen three of our boosted posts before receiving a cold email has already built a baseline of familiarity. They recognize the name. They've consumed a useful insight. When the cold email arrives, it feels less cold because the prospect has already been inside our content orbit for weeks. This is the mechanism behind the 2-3x conversion lift we measure on warmed prospects versus cold ones.

The impact of Layer 3 on everything else is measurable.

Prospects who've seen our content three or more times before receiving a cold email convert at two to three times the rate of cold prospects. We tested this across thousands of campaigns. The email didn't sell them. The six weeks of LinkedIn posts before it landed is what made them open it.

Without Layer 3, your sales team works twice as hard because every conversation starts from zero trust.

---

## Layer 4: Lead Conversion

Ironically, this is the simplest layer.

- Video conferencing through Google Meet.

- Proposals sent through Qwilr, where prospects can choose from multiple service packages and sign digitally in one flow.

- CRM managed in Attio.

- And meeting notes captured by Attention, which records and transcribes every sales call, generates a summary, and lets you ask questions about what was discussed after the fact, so nothing from the conversation is lost and the follow-up is based on what the prospect actually said rather than what the rep remembers.

> When Layers 2 and 3 do their job, the prospect arrives warm, informed, and already familiar with how you work. The sales call stops being a pitch and becomes a fit conversation. "Do we both agree this makes sense?" is a fundamentally different meeting than "let me explain who we are and what we do."

We closed over $1,000,000 in new ARR in a single month. That didn't come from a better pitch deck or a new sales hire. It came from the 90 days of capture and nurture that preceded those calls. By the time prospects reached Layer 4, the hard work was already done.

Compare that with a 2-layer funnel where the prospect books a call after seeing a single LinkedIn ad. They don't know your methodology. They haven't read your case studies. They're price-shopping three other vendors in the same week. Your sales team spends the first 20 minutes of every call explaining who you are before they can even start discussing fit. That's the tax you pay for skipping Layers 2 and 3: every sales conversation costs more time, more energy, and closes at a lower rate because you're starting from scratch each time.

## Why Four Layers Compound

When all four layers run together, each one makes every other layer cheaper and more effective.

- Outbound works better because the prospect saw your content before the email arrived.

- Content captures more leads because the de-anonymization tools catch people who would've bounced.

- Nurture sequences close faster because the prospect already trusts you from weeks of newsletters and LinkedIn posts.

- Sales calls convert at higher rates because the prospect is warm, educated, and pre-sold on the value before they ever get on a call.

The architecture scales because each layer compounds the others. Our lead gen layer produced 330,000 visitors and 1,500+ meetings last year. The strongest part of our funnel is, by far, the lead gen: syncing LinkedIn Ads, content, and outbound produces so many leads that we don't need to be 100% perfect lower down the funnel.

That sounds counterintuitive. But it only works because Layers 2 and 3 exist. If we generated 330,000 visitors with only a "book a call" button, most of that traffic would vanish. The capture and management layers are what turn volume into velocity.

Consider the journey of a single lead through all four layers.

1. A CTO at a $3M SaaS company sees a LinkedIn post from one of our team members about signal-based targeting. That's Layer 1.

2. A week later, they visit our website and use a free mini-tool to audit their cold email deliverability. They enter their email to get the results. That's Layer 2.

3. Over the next six weeks, they receive our newsletter, see LinkedIn posts from three different ColdIQ team members, and get a targeted email sequence based on the deliverability tool they used. That's Layer 3.

4. When they finally book a call, they already know our methodology, they've seen our team's expertise across multiple formats, and the sales conversation is about scope and timeline rather than convincing them we know what we're doing. That's Layer 4.

The conversion rate on a lead that traveled through all four layers is a fundamentally different number than a lead who clicked a LinkedIn ad and booked a call the same afternoon.

## Build the Missing Layers

> If you're between $1M and $5M, ask yourself one question: what happens between someone becoming aware of you and booking a sales call?

If the answer is "nothing" or "we follow up by email," you have a 2-layer funnel. You can grow on that, the same way we grew to $40K per month on it. You just can't compound on it.

The revenue ceiling isn't your copy, your channel, or your ICP. It's the layers you never built.