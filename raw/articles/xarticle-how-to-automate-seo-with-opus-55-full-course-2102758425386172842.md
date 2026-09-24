---
source_url: "https://x.com/EXM7777/status/2102758425386172842"
ingested: 2026-09-24
sha256: "2c60065c13f514495582a843a36f9d8c2ef9107b697ebbda0f5552b84313e061"
tweet_id: "2102758425386172842"
tweet_url: "https://x.com/EXM7777/status/2102758425386172842"
source_file: "/Users/mali/Development/x-bookmarks/data/run-2026-09-23/2026-09-23/xarticle-how-to-automate-seo-with-opus-55-full-course-2102758425386172842.md"
run: "run-2026-09-23"
---
---
title: "How to automate SEO with Opus 5.5 (Full Course)"
source: "x-bookmarks"
tweet_id: "2102758425386172842"
tweet_url: "https://x.com/EXM7777/status/2102758425386172842"
author_name: "Machina"
author_handle: "@EXM7777"
tweet_date: "Wed Sep 23 13:54:10 +0000 2026"
bookmark_date: "2026-09-23"
content_type: "x_article"
character_count: 19198
retweet_count: 34
like_count: 657
external_urls:
  - "https://ref.viktor.com/machina-x-4)"
  - "https://viktor.com)"
---

# How to automate SEO with Opus 5.5 (Full Course)

How to automate SEO with Opus 5.5 (Full Course)

I'm going to walk you through the SEO & AEO setup i run with AI agents, from the lazy autopilot version to the full Claude Code build on Opus 5.5, step by step...

because search changed shape a while ago, and now your pages have to win two games at once: the blue links on Google and the answers ChatGPT or AI Mode hand back to someone who never clicks anything

and before we touch a single tool, you need to hear the one rule that decides whether any of this is worth your time

a lot of people chase shiny numbers in Google Search Console, more impressions, higher positions, a nicer curve to screenshot... and none of it counts if the pages that rank don't convert

so if your pages have no clear next step, no signup, no booked call, no checkout, fix that first, because every hour you put into this article after that is wasted until they do

here's what we'll cover, in the order you'd actually build it:

- the easy route where one employee runs the whole loop for you

- a zero-to-first-page path if you don't have a site yet

- the same setup built by hand inside Claude Code

- how to pick the one page worth your week

- how to take that page apart and fix it for Google and AI answers

- the weekly loop that keeps it all moving

- a four-week plan so you're not staring at a blank folder

## start with the easy route using Viktor

i'll be straight with you, the Claude Code version later in this article is fun to build, but plenty of you don't want to build anything, you want SEO handled while you run the business

that's where Viktor fits, because it's an AI employee that lives inside your Slack and does the work there, so your whole team sees what it's doing and can jump in

you connect your tools once, most of them with one click, a few with an API key, and Viktor takes care of the login side and starts working right away with no webhooks and no Zapier chains to babysit

for SEO, the connections i'd plug in first are these:

- Google Search Console, so it can read how your pages perform in search

- DataForSEO, for keyword data, live rankings and competitor domains

- Ahrefs, for backlinks and the sites linking to your competitors

- Wordpress/Webflow, if your site lives there, so it can edit page titles, descriptions and schema

- PostHog, so it can see signups and funnels, which is the part everyone forgets

that last one is why this setup works for me

once Viktor can see your search numbers AND your conversion data in the same conversation, it stops recommending pages that bring traffic nobody pays for

then you give it a recurring job, in normal words, like you'd brief a new hire

something like every Monday, pull last week's search performance, line it up with signups per landing page, and bring me the one page that deserves attention, with a link behind every reason

you can get $100 in free credits at [viktor.com](https://ref.viktor.com/machina-x-4)

## starting from zero with no site

quick detour for anyone reading this with no website and no SEO behind them yet, because everything after this section assumes you already have pages to work on

the goal here is small on purpose, one page that sells one thing to one kind of buyer, plus one page that sends people to it

so before you open any builder, write down what you sell and what a conversion means for you, whether that's a signup, a booked call or a purchase

that line becomes the first thing your agent reads later, so it's worth getting right now

then pick one problem your customer already has, and one search topic around it that someone would type right before they'd pay to fix it

a topic people search out of curiosity brings visitors who leave, and a topic people search when they're ready to act brings buyers, so go with the second one

next, put up the simplest site you can in Webflow or WordPress, with your offer, a way to reach you, and nothing fancy - use Claude Code to build it

(the design can stay simple for a while, nobody converts because of a gradient)

on that site, you start with exactly two pages:

- one focused landing page built around that topic and your offer

- one useful supporting page that answers a close question

the landing page gets one clear next step near the top, the same signup, call or checkout you wrote down at the start

the supporting page does the helpful work, answering a question people ask on the way to buying, then links to the landing page so the reader knows where to go next

once both pages are live, you're at the same starting line as everyone else in this guide, and Search Console, DataForSEO, Firecrawl and PostHog get plugged in with the Claude Code build right below

from there, your two pages are the only candidates the weekly loop has to judge, which makes your first month simpler than it is for someone sitting on a pile of old posts

## building our setup in Claude Code

the setup is one folder on your computer, and that folder is the whole brain of your SEO agent, so it's worth getting it right

inside it, i keep three files that the agent reads every single run:

- a brief that explains the business, the offer, who buys and what counts as a conversion

- a state file that holds the current baseline numbers for each page you're working on

- a running log where every run adds a new entry and never deletes an old one

the brief is the file you'll edit the most, because the agent only judges a page as well as it understands what the page is supposed to sell

the log is the one that saves you later, because three weeks from now you won't remember why you changed a title, and the agent won't either unless it wrote it down

then come the tool connections, and i'll keep this to the ones that earn their place

Google Search Console is first, and to reach it from an agent you need a Google account with access to your site, a project in the Google API console and OAuth credentials

it sounds scary, but it takes one sitting and you only do it once

DataForSEO comes next, and it's the tool i lean on most for search data inside an agent, because it's built to be called from code

through it you get keyword volumes, the live top pages for any query, and even what Google's AI Mode shows for a keyword

before you point the agent at it, use their sandbox, which returns fake data in the exact same shape as the real thing and doesn't charge you a cent, so your agent learns the format before it touches your budget

Ahrefs is optional, and i'd only add its API if you already pay for it, because you'll mostly use it to see backlinks and which sites link to competitors instead of you

Parallel is the web search layer, and it's what the agent uses when it needs to look something up outside your own tools, like where your topic gets discussed or what a competitor claims on their pricing page

Firecrawl handles reading pages, because you give it a URL and it crawls the site, deals with JavaScript and sitemaps, and hands back clean text the model can actually read

and for conversions, i use PostHog, whichever the site already has, as long as the conversion is tracked on purpose with a named event instead of whatever the tool picked up by itself

you can wire each of these in as an MCP server or as a small script the agent calls, depending on what the tool offers

Claude Code supports hooks, which are small rules that run before a tool is used, and you can set one that forces the agent to ask you before anything that publishes, edits a live page or submits a URL

for the recurring runs, use a scheduled task where you pick the instructions, the folder, the model and the schedule, and each run opens as a fresh session you can review

i pick Opus 5.5 there, because this whole loop lives or dies on judgment calls about which page deserves your week, and that's where i want the strongest model i have (also cheaper than you'd expect)

keep that task in the permission mode that stops and waits when it hits something it isn't allowed to do, because that pause is your approval step

the cloud routines are handy too, but they run on their own without stopping for approval, so give them read-only access and never hand them the keys to publish

## find the one page worth your week

this is where the conversion rule turns into actual work, because the agent's first job is to find ONE page where better rankings would turn into more money

i know it's tempting to audit the whole site on day one, but a sitewide audit hands you a pile of small problems and no idea which one pays, so we go narrow

the agent opens Search Console first and pulls every page with its impressions, clicks and average position over the last few weeks

then it pulls conversions per landing page from PostHog, and lines them up next to the search numbers, page by page

what you're looking for is a page that already converts the visitors it gets and already shows up in search, but sits just low enough that most searchers never see it

i call that the killer page, because it's the one place where a ranking bump flows straight into signups instead of into a prettier chart

a page with tons of impressions and zero conversions is a trap, and the agent should flag it as one instead of recommending it

once you have two or three candidates, DataForSEO checks the queries behind each page, how many people search them, and who's ranking at the top right now

then the agent looks at the live search page for the main query, because the numbers alone lie all the time

if the top spots are all how-to guides and your candidate is a pricing page, the query wants something different from what you sell, and no amount of tuning will fix that mismatch

so every candidate gets one of three calls from the agent, keep it, keep it once you fix one condition, or drop it

and whatever it decides, it has to explain the call with links to the pages it looked at

if you have Ahrefs connected, this is also the moment to check backlinks, since sometimes a competitor wins on the strength of the sites linking to them, and that's a different job from rewriting the page

a few warnings about Search Console data before you trust it:

- the numbers land two or three days late, so today is always missing

- when you break data down by page and query at once, some rows get dropped

- AI Overview appearances can make average position look better than reality

i'd also tell the agent to pull the data one day at a time and store it in the state file, because that avoids the quota walls and gives you a clean history to compare against later

by the end of this step, you should have one page, one main query, and a short written reason for why that page is the bet

## take the page apart and fix it

now the agent inspects the page you picked, and i like to think of it as a full checkup in four passes, starting with the boring stuff that breaks everything else

first, can Google even reach it, which means Googlebot isn't blocked, the page returns a normal status code, and there's real text on it that can be indexed

Search Console's URL Inspection tool and Page Indexing report answer that in a minute

and if your site leans on JavaScript, have the agent compare what Firecrawl sees after rendering with what the raw page ships

then speed, and for that i run the PageSpeed Insights API on the page, mobile first, and only care about the failures that are big enough to hurt a real visitor

speed and access carry over to AI answers too, because Google says a page has to be crawlable, indexed and eligible for a snippet before it can show up as a link inside AI features

second pass is the competition, and here the agent does what you'd do by hand if you had an empty afternoon

DataForSEO pulls the top ten pages for the main query, Firecrawl scrapes each of those pages in full, and Opus 5.5 reads them side by side with yours

reading the full page is the point, because an agent guessing at what a competitor wrote will invent things, and an agent reading the actual page won't

what you want back is a short list of what the winners cover that you don't, questions they answer that you skip, and anything your page says better than all of them

the rule i give the agent is that every claim in its report comes with the URL it came from, and if some data is missing, it says the data is missing instead of filling the hole with a guess

this is the difference between an audit that looks impressive and one you can act on, because the second you ask where a finding came from, a guessed audit falls apart

third pass is the answer engines, and i'll keep it grounded because this is where the made-up advice piles up

Google says there's no special trick for AI Overviews or AI Mode, the normal SEO basics still apply, and it even tells you not to bother with things like llms.txt files

schema is a good example of hype outrunning evidence, since Ahrefs ran a large matched test adding schema to pages and saw no meaningful jump in AI citations across Google and ChatGPT

so i treat schema as something you add when the page fits a rich result, and never as an AEO shortcut

the changes that make sense for AI answers are about how the page reads:

- answer the question in the first line under each heading

- make each heading match the way people ask the question

- write each section so it makes sense read on its own

- keep your business details the same everywhere they appear online

that last point is bigger than it looks, because AI answers pull heavily from third-party sites like Reddit, YouTube, forums and industry publications, so what others say about you counts as much as your own page

this is where Parallel earns its spot, since the agent uses it to search for where your topic and your brand get discussed

what comes back is a list of places where your details are wrong, and threads where you're missing from a conversation you should be in

to check whether AI answers already cite you, DataForSEO can show what AI Mode returns for your query

Bing Webmaster Tools goes one step further with an AI Performance report listing which of your pages get cited in AI answers

fourth pass is the one this whole article hangs on, the path from the page to the conversion

the agent reads the page like a buyer would and checks whether there's one obvious next step, whether it shows up early enough, and whether the page actually answers the doubts someone has right before they sign up

then it checks the tracking, because if the signup isn't recorded as its own named event, you'll never know whether any of the SEO work paid off

internal links go here too, because the agent spots the pages on your own site that already get traffic and suggests where a link to the money page belongs

at the end of the four passes, the agent writes everything into one report in the folder, ranks the fixes, and recommends ONE change to make first

## run the loop every week

this is the part that turns a one-off audit into a system, and it's also where agents get dangerous if you let them react to everything

the loop i run is short, and the agent repeats it every week on the schedule you set up earlier:

1. pull fresh search numbers and conversions into the state file

2. compare them with the baseline from before the last change

3. check whether anything on the page broke since last week

4. recommend one change with the evidence and the links behind it

5. wait for your yes before drafting or publishing anything

6. write what happened and what changed into the log

one change at a time sounds slow

it is, on purpose, because if you change the title, the intro and the internal links in the same week, you'll never know which one did the work

the agent should also know that small ranking wiggles are normal, since Google itself says positions move around all the time and sometimes come back on their own

so i tell it to ignore anything that moves for less than a couple of weeks, and to never touch a page that's already doing well unless there's a strong reason

some changes show up in a few days and others take months

which is why the log earns its keep, since the agent needs to know how long ago each change went live before it judges anything

and when it does judge, it looks at two things together, the search side and the business side

a page that climbed in search and brought zero extra signups goes in the log as a miss

and a page that stayed flat in rankings but converted better after a clearer call to action goes in as a win, no debate

the same caution applies to AI citations, because Bing says its citation trends can't be tied to one specific change, and a model update on their side can move numbers you had nothing to do with

i also keep the agent's instructions frozen during a test, since changing the prompt mid-experiment makes this week's check incomparable with last week's

when you approve a change, the agent drafts it, in Wordpress, Webflow or wherever your site lives, and you do the final read before it goes live

that last read is where your taste comes in, because the agent is great at finding what's wrong and much worse at knowing what your brand would never say

## your first four weeks

here's how i'd lay out the first month if you were starting from zero today, and i'd follow it in order instead of skipping to the fun part

in week one, you connect everything and set the baseline

that means Search Console, DataForSEO, Firecrawl, Parallel and your conversion tracking, plus Ahrefs if you already have it, with spend limits and approval rules set before the first real run

you write the brief, confirm your signup or sale is tracked as a named event, and let the agent pull a few weeks of history into the state file

if you're going the Viktor route, week one is just connecting the same tools there and giving it the recurring job

in week two, the agent finds the money page and runs the four-pass checkup on it

you read the report, push back on anything that doesn't have a source, and agree on the one change you'll make first

week three is shipping week

the agent drafts the change, you review it, you publish it yourself, and the log records the date and exactly what moved

in week four, you set up the recurring loop and start measuring

the scheduled task or the Viktor job runs every week from now on, and you give the change a few more weeks before calling it a win or a miss

after that, you pick the next change on the same page or the next money page, and the system keeps going with you making one decision a week instead of doing all the digging yourself

this is the whole setup i use, and none of it needs you to be an SEO expert, it needs you to admit which pages make money and which ones just look good

for the autopilot version, Viktor runs this for you inside Slack or Teams with your approval on every sensitive move

if you want to build it yourself, open Claude Code, make the folder, and write the brief tonight

and whatever you pick, make the pages convert before you ask for a single extra visitor

thank you Viktor for sponsoring this guide, you can get $100 in free credits at [viktor.com](https://viktor.com)
