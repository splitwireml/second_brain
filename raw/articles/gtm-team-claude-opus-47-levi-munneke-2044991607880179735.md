---
updated: 2026-04-19
title: "how to make a $1M/yr GTM team with Claude Opus 4.7"
author: "Levi Munneke"
username: "@levikmunneke"
created: "2026-04-17"
source: "https://x.com/levikmunneke/status/2044991607880179735"
type: "xarticle"
tags: []
---


# how to make a $1M/yr GTM team with Claude Opus 4.7

how to make a $1M/yr GTM team with Claude Opus 4.7

I put together some of our most effective training documents, prompting and SOPs to be able to train Claude's new model opus 4.7 to be a team of A-player GTM engineers.

This way you can take my outbound knowledge that I have gained from sending over a million emails paired with the knowledge of your business and let Opus 4.7 put them together into an outbound motion.

here's the complete system.

every step is just a prompt. every prompt inherits the context from the step before it. the model does the work, you review, you launch.

STEP 1: THE KNOWLEDGE BASE

claude code is only as smart as the context you give it.

this is why I am giving you my documents that I use to train my team on how to run outbound.

before anything  you build a /business-context folder. install claude code, and run this prompt:

i'm setting up claude code to run an outbound automation system. before anything else, build me a /business-context folder with 5 files:

- icp.md (who we sell to)
- offer.md (what we deliver and the outcome)
- positioning.md (why us, objections, who we're not for)
- past-wins.md (top 10 closed clients, how we found them, what triggered the buy)
- tools.md (sending stack, crm, enrichment, anything we'll interface with)

for each file, output a template with only the questions whose answers will actually change what you output downstream. no generic marketing fluff. keep it tight.

-

claude writes the templates. you fill them in with context for your business.

every prompt after this inherits that context automatically.

STEP 2: HAVE CLAUDE FIND YOUR DATA POOL

this can get interesting.

a lot of people copy other people. apollo, zoominfo, lusha. same data, same prospects, same 40 cold emails landing in every inbox.

skip all of this and prompt:

read /business-context completely. based on my icp and past wins, identify 10 data sources where these prospects exist that most of my competitors aren't using.

for each source, tell me:
1. estimated volume of matching prospects in my tam
2. data quality - what fields can i extract
3. scrape-ability - public / paid / api / rate-limited
4. uniqueness - roughly how many competitors are using this source
5. signal strength - what can I infer about buyer intent from someone appearing here

output as a ranked table. prioritize sources with public data, high volume, and low competitor saturation. flag anything legally grey.

claude thinks for a minute and comes back with things like:

google maps (265M listings, almost zero competition in most local niches),

specific subreddits where your icp posts about their exact pain,

niche directories (bar associations, chambers of commerce, trade groups),

podcast guest lists, specific linkedin groups, github repos if you sell to devs, conference attendee lists.

you pick the top 2-3 sources your competitors have never touched.

that's your data moat.

STEP 3: CLAUDE BUILDS A CONTACTS SCRAPER

now. prompt claude code:

build me a production python scraper for [chosen data source]. requirements:

- pull these fields: company name, decision maker name, email, phone, website, industry, location, [custom field 1], [custom field 2]
- output to a date-stamped csv
- deduplicate against a master.db sqlite file that persists across runs so i never pull the same contact twice
- handle rate limiting with exponential backoff
- retry transient failures, log permanent failures to errors.log
- include a --dry-run flag
- write pytest unit tests for the parsing logic

set it up to run on a daily cron. test with 100 records, show me the output, fix any bugs, then tell me when it's production-ready.

claude writes it. runs it. hits an edge case. fixes it. runs it again.

20 minutes later you have a scraper that pulls 500-2,000 fresh contacts per run.

for google maps specifically: claude will wire up rapidapi's business data api with a website contact finder.

for niche directories: claude writes a playwright script that handles pagination, cookie walls, and basic bot detection.

cron job runs at 4am every morning. by the time you wake up, your pipeline has fresh leads. zero manual work after the initial build.

if you want to be able to get even more data, look on API platforms to see what unique data you can pull.

STEP 4: CLAUDE DRAFTS THE SEQUENCES

this is where most "ai outbound" falls apart. people let claude write the full email. it reads like a marketing bot. deliverability tanks. reply rates sit at 0.2%.

you do it differently. claude drafts. you edit for voice. the human stays in the loop for the creative.

email prompt:

read /business-context. draft a 2-email cold sequence targeting [icp]. angle: [specific signal we're scraping for, e.g. "just hired 5+ sales people in the last 90 days"].

constraints:
- under 75 words per email
- subject line under 4 words

write 5 variants of each email. flag any spam trigger words. tell me which variant you'd ship and why.

then the linkedin prompt:

now write the linkedin version of this sequence only for the top 10% of the list. dream accounts, highest fit.

3 touches:
1. profile view + connection request with a personalized note under 200 characters, no pitch
2. day 3 after acceptance: value message, open-ended, no pitch  
3. day 7: soft pitch tied to the same angle as the email sequence

match the tone of the email copy so a prospect who sees both feels like one person reached out. 3 variants per touch.

two channels. coordinated messaging. all written against your actual business context.

STEP 5: TAM COVERAGE MATH

this is the part almost nobody runs. you ask claude:

my tam is approximately 30,000 companies. i want to touch every single one via email in 90 days, and the top 10% via linkedin.

calculate the infrastructure i need. factors:
- 2 email touches per contact over 90 days
- 3 linkedin touches per top 10% prospect over 90 days
- email deliverability target 90%+
- 20 emails per inbox per day
- 50 linkedin actions per account per day (25 messages, 25 inmails)
- new inboxes need 2 weeks warmup before full volume

output: domains needed, inboxes needed, linkedin accounts needed, daily send volume per channel, monthly cost (domains + inboxes + sales nav + sending platform), total touches delivered, cost per touch. sanity-check the numbers.

claude runs it and hands you back the full infrastructure spec:

add instantly or smartlead at $97, plus your claude and vps costs, and you're under $600/mo to touch your entire tam every 90 days with a 10-to-1 email-to-linkedin ratio that keeps linkedin pristine for only the accounts that matter.

WHY THE 10-TO-1 SPLIT MATTERS

email is your coverage layer. hits every company in your tam. low cost per touch. the math works at scale.

linkedin is your precision layer. only for the top 10%, your dream clients, the accounts you'd drop everything for. three touches. highly personalized. written by you, polished by claude.

when you hit a dream account on both channels, they start recognizing your name. that familiarity is what closes the deal two weeks later when they have the right pain at the right time.

volume where volume works. precision where precision works.

7-DAY DEPLOYMENT

day 1 - fill in your business context files. install claude code.

day 2 - run the data pool research prompt. pick your top 2 sources.

day 3 - claude builds the scrapers. you test with 100 contacts.

day 4 -email infrastructure. buy domains & inboxes. warm in instantly.

day 5 - run the sequence prompts. you edit for voice. load into instantly.

day 6 - linkedin accounts configured (alt accs or team). 10% list filtered.

day 7 - test sends at low volume. monitor deliverability. fix edge cases.

week 2 onward - scale volume daily. first meetings booked within 10 days.

month 3 - you've touched your entire tam. you know exactly which messaging works. you're booking 40-80 calls a month.

month 6 - you're looking at $500k-1M in pipeline generated by a system you built in a week with a model that costs less than your monthly starbucks habit.

SYSTEM IMPLEMENTATION

the model is here. the prompts are here. the playbook is here.

you're the only one stopping this from being built.

if you want this exact system built for your offer dm me "OPUS" and i'll walk you through what we'd do for your offer.

or make it easy for you and me: cal.com/leviwelch/30min
