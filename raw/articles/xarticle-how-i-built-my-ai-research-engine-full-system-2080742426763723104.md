---
source_url: "https://x.com/maxxmalist/status/2080742426763723104"
ingested: 2026-07-26
sha256: 4407202b8f43dfb0b80876969e3c921e151feaa8416d7c1f0c7114cf831ea212
tweet_id: "2080742426763723104"
local_source: "/Users/mali/Development/x-bookmarks/data/run-2026-07-25/2026-07-24/xarticle-how-i-built-my-ai-research-engine-full-system-2080742426763723104.md"
run: "run-2026-07-25"
---
---
title: "How I Built My AI Research Engine (FULL SYSTEM)"
source: "x-bookmarks"
tweet_id: "2080742426763723104"
tweet_url: "https://x.com/maxxmalist/status/2080742426763723104"
author_name: "MAX"
author_handle: "@maxxmalist"
tweet_date: "Fri Jul 24 19:50:27 +0000 2026"
bookmark_date: "2026-07-24"
content_type: "x_article"
character_count: 15913
retweet_count: 15
like_count: 173
---

# How I Built My AI Research Engine (FULL SYSTEM)

How I Built My AI Research Engine (FULL SYSTEM)

im going to show you how to build your own AI research engine with Claude Opus 5, a folder of markdown files that reads reddit, quora, youtube, github and half the internet for you, and hands back a scored queue of things people are desperate for

Every post, product and offer I launched this year came out of this folder, well... almost, but it sound cool

By the end of this article you'll have:

1. A folder that tells your AI exactly where to look and what counts as valuable

2. A scoring system so you stop guessing which idea is worth your time

3. A weekly routine that takes 30 minutes and hands you a queue of ideas

4. A direct connection into the content engine from part 1, so a topic goes in and 8 posts come out

5. And you can build all of it this weekend

let's get it

## The Problem With Searching

You want to write something. You Google "content marketing tips 2026" or whatever you want to find. You get ten articles. All ten say the same four things. You read three of them, you write a post that sounds like the average of those three, and you wonder why it got 400 views

That's not research. That's laundering the consensus

Google is a machine for finding answers that already exist. Which is great when you need to know how to fix a bug or what year something happened

But you're ou're trying to find a GAP, not a right answer here

A gap is a place where people clearly have a problem, they're saying it out loud, and nobody has given them a good answer yet. That's where posts go viral. That's where products get bought. That's where you have an actual edge over everyone else in your niche

And gaps don't show up in search results. By definition. If someone had answered it, it would be an article, and then it would be in Google, and then it wouldn't be a gap anymore

So you have to go where the questions live before the answers do

## What a Gap Actually Looks Like

Let me make this concrete, because "find gaps" sounds like advice from a LinkedIn guy in a quarter-zip

Real example of the shape:

- Someone posts in a subreddit: "is there a tool that just does X? I've tried three and they all do Y instead"

- The post has 240 upvotes

- There are 60 comments

- Not one of them answers the question

Read that again. Two hundred and forty people said "yes, I have this exact problem" and sixty people showed up and none of them could solve it

That's a market telling you what it wants, in its own words, for free, timestamped

Now compare that to what you would have found on Google. You'd have found the three tools that do Y. The ones that already failed these people

> Google shows you what exists, signal mining shows you what's missing.

Once you start seeing it, you can't unsee it. Every forum turns into a list of things people would pay for

The only problem is you can't read 40 subreddits every day. You have a life. So you build a system that reads for you and only shows you the good stuff

## So What Is a Research Engine?

Same idea as the content engine from part 1. It's a folder of markdown files

Some files say WHERE to look. Some say WHAT counts as valuable and what's garbage. Some are the instructions you give the AI. And some are where the results land

You point an AI agent at the folder, it reads the rules, goes looking, and comes back with a list of scored opportunities instead of a pile of links

That's the difference between asking AI to "research my niche" and having a research engine

Ask AI to research your niche and you get a Wikipedia summary. Every time. Because it has no idea what you already know, what you care about, or what "interesting" means to you

Give it a folder that defines all three, and you get a list of things you didn't know yesterday

Think of it like the difference between sending an intern to "go research the market" versus handing them a checklist that says exactly which forums to read, what a good find looks like, what to ignore, and how to write it up

Same intern. Completely different output

## The Structure

Here's exactly what you're building:

> /research-engine
├── index.md
├── sources/
│   ├── reddit.md
│   ├── quora.md
│   ├── x.md
│   ├── youtube.md
│   ├── github.md
│   ├── papers.md
│   └── forums.md
├── filters/
│   ├── signal-rules.md
│   ├── scoring.md
│   └── kill-list.md
├── prompts/
│   ├── harvest.md
│   ├── cluster.md
│   └── teardown.md
└── output/
    ├── opportunities.md
    ├── winners.md
    └── log.md

What each folder does:

sources/ tells the agent where to go and what each place is good for. Reddit is not YouTube is not GitHub. Each one leaks a different kind of information

filters/ is the brain. This is what separates a real signal from noise, and it's the part everyone skips. Don't skip it. A research system without filters just buries you faster

prompts/ are the reusable instructions. Write them once, run them every week

output/ is where findings land. Three files: the live queue, the archive of what already worked for other people, and a log of what you actually shipped

Go make the folder now. Empty files are fine. Then come back and we'll fill them

## Where I Look (And What Each Place Is Actually Good For)

This is sources/. One file per platform and each one answers the same three questions: what is this place good at, what do I search for here, what does a good find look like

reddit.md

The best source on the internet for raw, unfiltered complaining

People are anonymous, so they say the true thing instead of the polite thing

What to look for: "is there a tool that", "am I the only one who", "how do you guys deal with", and any thread where someone lists what they tried and why it all sucked

Sort by top of the month, not all time. All time is already famous. This month is still fresh

The gold is in the comments, not the posts. Especially comments with more upvotes than the post they're replying to. That means the crowd disagreed with the framing, which means there's a better angle sitting right there

quora.md

Underrated and everyone sleeps on it

Quora is where people ask the question they'd be slightly embarrassed to ask a colleague. It's less technical, more human, and it's full of beginners describing their confusion in plain language

Which is exactly the language you should be writing hooks in

What to look for: questions with lots of followers and weak answers. Quora literally shows you how many people are following a question. That's a demand counter sitting on the page

If 900 people are following a question and the top answer is four sentences from 2019, that's not a gap. That's a crater

Also great for finding the exact words normal people use. Builders say "workflow automation". Real people say "I'm tired of copy pasting the same thing". Guess which one makes a better hook

x.md

Best for speed and for what's heating up right now

What to look for: replies to big accounts where someone says "ok but how do you actually do this", quote tweets that disagree, and any thread where the replies are more interesting than the post

X is bad for depth and great for timing. Use it to find out what's rising, then go to Reddit or Quora to find out what people actually struggle with underneath it

youtube.md

The most slept-on research source on this list, and it's not close

Two goldmines:

The comments under big videos in your niche. Specifically the ones that say "how did you do the part at 4:32". That's a person telling you which 20 seconds of an 18 minute video was the only thing they wanted. That's a whole piece of content by itself

And the search bar. Type your topic and read the autocomplete. That's aggregated real search demand, free, updated constantly

Also worth checking: videos with high views and low subscriber counts. Means the topic carried it, not the creator. The topic is the signal

github.md

Only relevant if you're anywhere near tools, software or AI, but if you are, it's incredible

What to look for: issues with lots of thumbs up and no fix for six months. That's a known unsolved problem with a queue of people waiting

Also trending repos. Not to code them. To notice what problem got popular enough that someone built a tool for it this week

forums.md

The niche stuff. Discord servers, Facebook groups, Slack communities, industry forums, Skool and Whop communities, subreddit-adjacent places nobody indexes

This is where your competition isn't looking, because it's annoying to look here, let's be real i woulnd't look there without AI too, that's exactly why it's valuable

## What Counts as a Signal

This is filters/signal-rules.md and it's the single most important file in the system

Everything else is plumbing. This is the part that decides whether your engine finds gold or trash

A signal is:

- The same question asked over and over with no good answer under it

- "Is there a tool that does X" posts

- Complaint threads under a popular product

- A comment with more upvotes than the post it's replying to

- A Quora question with hundreds of followers and a weak top answer

- A GitHub issue with 50+ thumbs and no fix in six months

- A YouTube comment asking how you did the thing at a specific timestamp

- Anyone saying "I would pay for this"

- Anyone describing a manual workaround they built themselves. That's a product with no interface yet

- A paper solving something no product has shipped

- Two people arguing about the right way to do something, because that means there is no accepted right way

Notice what they have in common. Every single one is evidence of unsatisfied demand. Not interest. Not attention. Demand that showed up and left empty handed

Interest is cheap. Everyone is interested in everything. Frustration is expensive, and frustration is what people pay to make stop

## What to Throw Away

This is filters/kill-list.md and writing it is what stops you from drowning

Most people's research problem isn't finding stuff. It's that they find too much stuff and none of it means anything. The kill list fixes that

Ignore:

- Product launches and funding news. Everyone sees these. Zero edge

- Anything sitting at the top of a subreddit's all time. Already covered by fifty people

- Hot takes with no "I have this problem" underneath. Opinions aren't demand

- Anything you already know. Sounds obvious, but half of what feels like research is just reading things that confirm what you think

- Trends with no mechanism. "AI is changing everything" is not a signal, it's weather

- Anything where the only people talking about it are also selling it

- Stuff from more than 6 months ago, unless it's still getting fresh comments

That last one has an exception worth noting. An old thread with new comments is one of the strongest signals there is. It means the problem outlived the discussion

Write your kill list before you start harvesting. It's much harder to throw things away once you've already gotten excited about them

## How I Score Ideas

filters/scoring.md

You'll find more than you can act on. Always. So you need a way to rank that isn't vibes

Five things, 1 to 5 each:

Pain: How much does this hurt? mild annoyance actively costing them money or hours   

Frequency: How often does it come up? saw it once it's everywhere   

Money: Can this connect to something you sell? not really direct line to an offer

Openness: How crowded is the answer? ten good articles exist almost nothing exists

Speed: Is this heating up or dying? fading growing right now

18 and up goes into opportunities.md. Do these

13 to 17 goes in a maybe pile. Revisit next month, some of them start climbing

Under 13 goes straight to the kill list with one sentence on why. That sentence matters. Future you will find the same idea again and needs to know why past you dropped it

The reason this works isn't that the numbers are precise. They're not. It's that scoring forces you to be honest about the fourth column. Openness is where most people lie to themselves. You find an idea, you love it, you don't check whether forty people already made that video

## Clustering

prompts/cluster.md

Harvesting gives you a pile, say 40 signals in a week, but usually 40 signals is useless. It's a to-do list you'll never touch

So you cluster. You take the pile and ask: which of these are secretly the same problem?

And the answer is usually that seven different complaints are one problem wearing seven hats

Example. You collect these separately over a week:

- someone can't keep their AI character looking the same across videos

- someone's brand posts sound different on every platform

- someone's team writes in five different tones

- someone's AI voiceover sounds like a different person each time

- someone asks how to make their thumbnails look like a set

Five different threads, five different platforms, five different words

One problem: consistency at scale

You didn't have five ideas. You had one big one, and now you know it's big, because five separate people arrived at it from five separate directions without talking to each other

That's a piece of information you could not have gotten by reading any single thread. This is where AI earns its keep, because a human reads these on five different days and never connects them

The prompt is basically: here are 40 raw signals, group them by underlying problem, not by topic or platform, name each group in the words the people used, and tell me how many separate sources support each group

40 signals in. 6 real themes out. Now you have something you can actually work with

## Run it every week

Every week, same four steps:

1. HARVEST

Run harvest.md across your sources. Everything goes into a raw file. No judging yet. Judging while collecting makes you miss things

2. CLUSTER

Run cluster.md. 40 raw signals become 6 named themes with source counts attached

3. SCORE

Run each theme through scoring.md. Anything 18+ goes to opportunities.md with the original quotes attached. Everything else goes to maybe or dies with a reason

4. ROUTE

Take the top one or two and send them into the content engine

HARVEST → CLUSTER → SCORE → ROUTE

That's it. That's the entire system. Everything above is just detail on how each step works

## Where It Plugs Into

This is the part I'm most excited about

The topic comes from a scored queue built out of what real people said they were struggling with this week

And because the opportunity file keeps the original quotes attached, your content engine now writes with the actual language people used. Their words become your hooks. That's not a small upgrade, that's most of the reason copy converts

Two folders, one machine:

> research-engine → opportunities.md → index.md → content-engine → 8 native posts

Real world version of that chain: you find a gap on a Wednesday, and by Thursday there are eight platform-native posts about it, written in the exact words the people who have that problem used to describe it

Nobody is out-researching that with a Google search

## How To Actually Run It

Claude Code. That's it. Four steps

1. Install Claude Code and make sure you're on Opus 5

2. Open your terminal and go into the folder:

> cd research-engine

3. Type claude and hit enter

4. Then just talk to it in plain english:

> read index.md and run the harvest prompt across all my
sources. then cluster the results, score them, and write
everything into output/opportunities.md

That's the whole thing

It reads your rules, goes searching, and writes the results back into your own files. You don't copy paste anything. You don't upload anything. The folder updates itself

Once it works, save that sentence into a file called weekly.md so next time you just say "run weekly.md" and go make coffee

30 minutes every sunday and you're good

===

If this was useful, like and RT, it genuinely helps ❤️

Now go make the folder
