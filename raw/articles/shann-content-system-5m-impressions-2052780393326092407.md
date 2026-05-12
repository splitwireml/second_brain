---
title: "How to build your content system with AI (and get to 5M impressions)"
author: "Shann³" (@shannholmberg)
authorId: "1455999313453195265"
createdAt: "Fri May 08 15:59:19 +0000 2026"
type: x-article
tags: [content-strategy, ai, social-media, marketing, content-os, workflow]
platform: X
id: "2052780393326092407"
likes: 375
retweets: 32
replies: 13
url: https://x.com/i/status/2052780393326092407
---
# How to build your content system with AI (and get to 5M impressions)

a system that finds your ideas, drafts them in your voice, publishes them, and learns from what works. it took my account to 5M impressions in 2 weeks and 100K bookmarks in 2 months.

content is only as good as the person and the system behind it. low effort going into curating ideas and writing means low-quality content coming out the other side.

I built a system that optimises for one thing: bookmarkable content.

## The non-negotiable

never publish unedited, hand-finish every draft. the system is an accelerator, not autopilot. used as automation, it decays.

the goal is not to fake a voice from prompts. its to build a reusable operating asset from your real writing.

## what "bookmarkable" actually means

a bookmark is a small promise the reader makes to their future self. it says "I will need this again."

before I ship anything, I ask whether the post looks like one of these:
- a checklist
- a blueprint
- a folder structure
- a template
- a framework
- a step-by-step workflow
- a proof screenshot with a takeaway
- a before and after
- a reusable mental model

## the system in one diagram

context lives in two places. the signal layer is everything external you bring in: bookmarks, articles, DMs, competitor posts. knowledge graph is everything internal you already own: personal OS, notes, journals, voice memos, owned content archive.

```
EXTERNAL: SIGNAL LAYER          INTERNAL: KNOWLEDGE GRAPH
X bookmarks, articles,          personal OS, notes,
transcripts, DMs,               journals, voice memos,
replies, competitor             owned content archive
posts                           feeds: original, repurpose

          ↓                           ↓
      STRATEGY + VOICE + STORES
      positioning, voice profile,
      master avoid-slop, ideas, hooks,
      proof bank, feedback log
              ↓
      PRODUCTION LEADER
      opens run folder, routes via
      idea gate, enforces gates
              ↓
      RUN FOLDER (one per content object)
      idea → brief → draft → verify
      → shann review → scheduler → feedback
              ↓
      STORES
      winners, losers, voice rules,
      banned patterns, hooks, proof
```

## the four routes

before a content object enters drafting, the idea gate makes one decision: what kind of content is this?

four routes:
- ORIGINAL: create something drawn directly from you or from your second brain
- REPURPOSE: take owned content and extend it
- REWRITE: take external source material and translate it through your point of view
- RESEARCH + IDEATE: explore a topic, study patterns, generate candidate angles

each route still produces one run folder, with the route declared in content-object.md.

## the folder you can build today

/content-os
  /strategy
      positioning.md, audience.md, pillars.md, source-watchlist.md
  /voice
      voice-profile.md, master-avoid-slop.md
  /stores
      inbox.md, workboard.md, ideas/, hooks/, proof/, feedback/
  /runs
      /active (one folder per content object)
      /archive
  /modules
      /writer (SKILL.md, references/, templates/)
  /workflows
      idea-to-published-post.md, verifier-checklist.md, etc.

## the writer context packet

model writes safe mush because nothing in the context is load-bearing. a tight packet beats a giant context window almost every time.

packet lives inside the run folder as brief.md:

```
writer context packet
─────────────────────
thesis:        one sentence the post must prove
reader:        the specific person who should save it
proof:         numbers, screenshots, stories I am allowed to use
angle:         the unexpected framing
constraints:   format, length, tone, banned phrases
voice anchors: 2-3 lines that sound like me
risks:         what would make this read as slop or as cringe
open loops:    what I do not yet know, that the writer should flag
```

## the bookmarkability rubric

score draft 0, 1, or 2 on each:
1. saves the reader a future task
2. includes proof (numbers, screenshot, named example)
3. gives a reusable takeaway (template, checklist, frame)
4. has a specific audience and job-to-be-done
5. can be applied without me being in the room
6. has a strong screenshot or visual

out of 12. personal bar is 8. below 8 it goes back to the packet, not to the trash.

## the master avoid-slop document

54 patterns, broken into three severity tiers. catches things like:
- promotional language ("groundbreaking", "game-changing")
- significance inflation ("pivotal moment", "testament to")
- vague attribution ("experts believe", "studies show")
- false agency ("the system compounds", "the data tells us")
- rhetorical setups ("the question is whether you X")
- staccato fragmentation ("no X. no Y. no Z.")
- em dash overuse (zero is the target)
- filler adverbs ("actually", "literally", "quietly")

## four prompts you can copy

1. brand foundation extraction (maps to strategy/ + voice/)
2. bookmarkability scoring (maps to stores/ideas/)
3. writer context packet (maps to runs/active/{slug}/brief.md)
4. viral postmortem (maps to draft-package.md, final pass before review)

## two models, two roles

writer (opus 4.7) handles: taste, rhythm, compression, voice, the actual draft
orchestrator (gpt-5.5) handles: routing between layers, packaging context, running verifier, handoff to publish layer

## where to run the system

1. VPS with claude code - rent a small server, put /content-os in git, let claude code run the workflow
2. hermes agent - what I run. built for agents, skills, tool access, file and git operations, browser and search, scheduled jobs, persistent context

## Postiz as the publish layer

once a draft is approved, it goes into Postiz and gets queued. one place to schedule across X, linkedin, instagram, threads, tiktok, youtube, bluesky, reddit, and more. open source and self-hostable, repo is gitroomhq/postiz-app.

## the feedback loop is a moat

most people stop at publish. that is where the system starts earning.

every week I look at: views, bookmarks, bookmark rate, replies, DM follow-ups.

bookmark rate is the one I watch most. it tells me which posts earned the save, not just the scroll.

winners get copied into inputs as examples next to their numbers. losers update voice rules, banned patterns, or the idea filter. the next packet gets sharper because of what I learned this week.

— shann