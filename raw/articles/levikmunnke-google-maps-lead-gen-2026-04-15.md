---
updated: 2026-04-17
title: 'Source: @levikmunneke — Google Maps B2B Lead Gen with Claude Code'
source: https://x.com/levikmunneke/status/2044088273312911516
type: post
---

# Source: @levikmunneke — Google Maps B2B Lead Gen with Claude Code

**URL**: https://x.com/levikmunneke/status/2044088273312911516
**Author**: @levikmunneke (Levi Munnike)
**Date**: 2026-04-15
**Tweet ID**: 2044088273312911516

## Full Thread Text

how I scrape millions of google maps leads with claude code and a $19/mo API

i built a system with claude code and a $19/mo API that pulls unlimited google maps leads, scrapes every website for verified emails, cleans the list automatically, and spits out a CSV ready for outbound.

here's the complete build. step by step. no fluff.

THE PROBLEM WITH MOST B2B LEAD SOURCES

you already know this but let me say it out loud:

ZoomInfo charges you $15,000/year for stale data.

Apollo recycles the same contact pool every agency has already burned.

Lead list vendors sell you CSVs with 40% bounce rates and zero email verification.

meanwhile google maps has 265 million+ business listings, updated constantly, with real phone numbers, real addresses, real websites.

it's the largest verified B2B database on earth and almost nobody is using it for outbound.

why?

because scraping it at scale used to require a full-time developer, weeks of setup, and constant maintenance when google changed their markup.

not anymore.

i built the whole system in one afternoon with claude code.

total cost: $25/mo + claude code.

here's exactly how.

PART 1: THE ARCHITECTURE

before touching any code, understand what we're building:

layer 1: maps data API pulls business listings from google maps by zip code

layer 2: python email scraper hits every website URL from the API results and pulls contact emails from the raw HTML

layer 3: dedup + cleaning pipeline removes garbage, duplicates, and bad data

layer 4: simple frontend dashboard to run searches, monitor jobs, and export CSVs

each layer is independent.

if the API changes, you swap layer 1 and the rest stays.

if you want to add linkedin enrichment later, you add it after layer 2.

build it modular. always.

PART 2: THE MAPS DATA API

go to rapidapi.com and search "maps data" by alexanderxbx.

subscribe to the $3 or the $19/mo plan. ($3 can probably get you 100k leads+)

this API wraps google maps and returns:

- business name
- address
- phone number
- website URL
- google rating + review count
- category
- coordinates

you call it with a keyword + location and get back clean JSON.

simple.

but here's the problem: if you just search "plumber New York" you cap out at a few hundred results.

google maps buries listings after the first page.

the solution is to break every search down by zip code.

PART 3: THE ZIP CODE STRATEGY

the united states has approximately 32,000 active zip codes.

download the full list free on google: search "free US zip code list CSV github" and grab any of the top results. the USPS dataset works fine.

here's why this matters:

when you search "plumber 10001" you get the top results for that specific zip.

when you search "plumber 10002" you get a completely different set.

run your keyword across all 32,000 zips and you're not getting hundreds of listings.

you're getting millions.

for a category like HVAC contractors, roofing companies, or landscapers, you can pull 800k-1.2M raw listings in a single run.

that's before dedup.

after dedup you're usually looking at 400k-700k unique businesses per niche nationally.

for targeted states or metros, you filter down to the relevant zips.

for international scraping: this zip approach is US-specific. for other countries, break by city, region, or postal district depending on what the target country uses. the API supports global searches.

PART 4: BUILDING THE SCRAPER WITH CLAUDE CODE

open claude code in your terminal.

tell it:

> "build me a python script that reads a CSV of US zip codes, takes a keyword input, and calls the maps data API on rapidapi.com by alexanderxbx for each zip. paginate results. save all outputs to a SQLite database with columns: business_name, address, phone, website_url, rating, review_count, category, zip_code. skip duplicates based on phone number and website URL. run requests concurrently with a thread pool of 10. add exponential backoff on 429 errors."

claude code will generate the full script.

test it on 10 zip codes first.

check the SQLite output looks clean.

then let it run.

at 10 concurrent threads on the $19/mo plan, you can pull 50k-80k listings per hour.

for 32,000 zips, a full national run takes 12-24 hours.

set it and forget it.

PART 5: THE EMAIL SCRAPER (THIS IS WHERE MOST PEOPLE STOP)

the API gives you website URLs.

but it doesn't give you email addresses.

most people at this point go buy an enrichment tool for $200/mo that:

1. has the email for 30% of contacts
2. charges you per lookup anyway
3. gives you info@company.com half the time

useless.

instead: scrape the email directly from the website HTML.

tell claude code:

> "build a python script that reads website_url values from the SQLite database where email is NULL. for each URL, use requests with a 5-second timeout and a realistic user agent to fetch the HTML. parse the HTML with BeautifulSoup. extract all email addresses using a regex pattern that catches standard email formats. also check the /contact and /about pages if no email found on the homepage. store the first valid non-generic email found (skip info@, hello@, support@ unless nothing else found). save back to the SQLite database. run with a thread pool of 20. skip URLs that 404 or timeout after 2 attempts."

this is important:

do not use the claude API to parse emails.

just use python regex on raw HTML.

pattern: [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

it's fast. it's free. it finds every email on the page.

no LLM credits burned.

at 20 concurrent threads, you can scrape 10k-15k websites per hour.

on 400k unique listings, email scraping takes 10-20 hours total (can be shortened with smart prompting).

run it overnight twice.

typical result: 35-50% of listings have a scrapeable email.

on 400k leads that's 140k-200k verified email addresses.

for free.

PART 6: THE FRONTEND DASHBOARD

command line is fine for running jobs.

it's terrible for clients, VAs, or anyone else touching the system.

tell claude code:

> "build a simple flask web app with a dark UI. features needed: (1) search form with keyword input and state/zip filter dropdown. (2) job queue showing active and completed scraping jobs with progress bars. (3) database stats showing total leads, leads with emails, leads by category. (4) export button that downloads a filtered CSV. (5) filter options: min rating, min review count, has email only toggle, category filter. run on localhost:5000."

claude code will scaffold the whole thing.

takes about 20 minutes to get it running clean.

now you have a point-and-click lead generation machine.

drop a VA in and they can run targeted scrapes for any niche, any state, any metro without touching the terminal.

PART 7: THE CLEANING AND DEDUP PIPELINE

raw data is garbage.

you need to clean it before anything goes into an outbound sequence.

tell claude code:

> "build a python cleaning script that reads from the SQLite database and outputs a clean CSV. apply these filters: remove any record where email is NULL. remove duplicate emails. remove emails with domains matching a blocklist: gmail.com, yahoo.com, hotmail.com, outlook.com, aol.com (these are personal not business emails). remove records where business_name contains 'permanently closed'. normalize phone numbers to E.164 format. remove records where website_url returns a 404. flag records where review_count is under 5 (low trust). output two CSVs: clean_leads.csv and flagged_leads.csv."

after running this you typically end up with:

- 60-70% of emails dropping (duplicates, personal addresses, dead sites)

- what's left is genuinely usable B2B contact data

on a 400k pull that's 40k-80k clean verified B2B leads.

at $15,000/year for ZoomInfo you're paying $1,250 per month for 40% bounce rates.

at $25/month for this system you're paying $0.50 per 1,000 verified leads.

the math speaks for itself.

## Claims Summary

| Claim | Status |
|-------|--------|
| Google Maps has 265M+ business listings | Likely — widely cited but unverified |
| ZoomInfo costs $15,000/year | Likely — ZoomInfo pricing is public, entry-level is ~$15K |
| RapidAPI "maps data" by alexanderxbx exists | Unverified — not independently confirmed |
| $3/mo plan yields 100k+ leads | Unverified |
| 800k-1.2M raw listings per national niche run | Unverified |
| 35-50% of listings have scrapeable emails | Plausible — based on typical business website rates |
| 60-70% of raw leads drop after cleaning | Plausible — dedup + blocklist is aggressive |
| 40k-80k clean leads per 400k pull | Derived estimate |
| $0.50 per 1,000 verified leads | Derived estimate |
| Full national run: 12-24 hours at 10 threads | Unverified |
| Email scraping: 10-20 hours for 400k listings | Unverified |

## Verification Targets

1. **RapidAPI maps data API by alexanderxbx** — search rapidapi.com for this specific provider
2. **US zip code count (~32,000)** — confirm against USPS data
3. **Google Maps 265M+ listings claim** — check if this number is cited anywhere

## Tags for Concept Page

- `lead-gen` (primary, user-requested)
- `outbound`
- `b2b`
- `web-scraping`
- `claude-code`
- `automation`
- `monetization`