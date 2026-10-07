---
title: Content Research Agent Production Prompts
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [agent, workflow, content-marketing, prompting, hooks, mcp]
sources: [raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]
related_entity: [[virlo]]
author: [[dsqjaffa]]
---

# Content Research Agent Production Prompts

Verbatim evidence-to-production and recurrence contracts from jaffa's October 5, 2026 Claude + Virlo guide. Every original prompt fence below is copied mechanically from the local export. The shared context and discovery tasks live in [[content-research-agent-discovery-prompts]], detailed mechanics in [[content-research-agents]]. Jaffa asks Claude to write from proven examples; Matt's October 6 guide rejects AI-written hooks/scripts in [[format-propagation]]—a retained source-specific disagreement, not a resolved benchmark. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

## Prompt 4 — bank 20 hooks by structure

Preserve spoken-first/on-screen-fallback hooks verbatim, group by structure rather than topic, count occurrences and median views, then recommend what to film in 2 sentences. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```
From my agent's outlier videos (niche matches, real
people, no AI, not sponsored), pull 20 hooks word
for word (spoken hook first, else on-screen text).

Group them by structure (the format underneath, e.g. "[small
disaster] + [the product survived]"), never by topic.
Name each one in a few words, count the videos using
it and give its median views.

Return a table: structure, example hook, link, views,
saves + shares per 1,000 views. Then, in 2 sentences, which structure to
film first and why.
```

## Prompt 5 — find repeating formats

Cross-creator replication is at least 2 creators, with 2 example videos per format. Compare the top 25% with the bottom 25% of outliers, not fixed 25-video sets. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```
Using my agent's analyzed videos, find formats used by
at least 2 different creators. For each: the content
format (tutorial, review, storytime...), how it's
filmed (talking head, green screen...), the setting
(kitchen, car, bedroom...) and 2 example videos.
Real people, no AI, not sponsored.

Rank by views AND engagement, then compare the top
25% of outliers with the bottom 25%:
which formats show up more at the top? Then the one
format I should copy this week.
```

## Prompt 6 — saves and shares

Per-1,000-view metrics and low-save/share high-view flags are separate from raw views; preserve the requested top-10 columns and 3-sentence explanation. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```
Re-rank my agent's outlier videos by saves, shares and
comments per 1,000 views (niche matches, real people,
no AI, not sponsored). Flag any video with big views
but almost no saves or shares.

Return the top 10 by saves and shares (link, hook,
views, saves, shares, comments). Then 3 sentences on
what the most-shared videos have in common.
```

## Prompt 7 — one hook, script, then next

Paste the numbered subrequests one at a time. Select hook #[N], retain the source structure, cite the original video, write a 20–30-second talking-head script in the user's voice with no shot list, then Next. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```
1. Give me the top 5 hooks from my agent's outliers,
   adapted to what I sell. Keep each hook's structure.

2. Write a full script for hook #[N]: talking head,
   20-30 seconds, written how I talk, no shot list.
   Cite the video it came from.

3. Next.
```

## Prompt 8 — three concepts from one winner

Given [link], use a 3-line diagnosis, then keep the hook structure and format in 3 offer-specific concepts/scripts. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```markdown
Take the outlier video at [link]. Break down its hook,
its format and why people saved or shared it, in 3
lines.

Then give me 3 new concepts for what I sell that keep
the same hook structure and format, each with a 20-30
second talking-head script in my voice.
```

## Prompt 9 — daily recurring agent

A recurring copy runs daily with the same goal sentence, search phrases and excludes; hook/format analysis and Meta ads stay on. The once-per-chat context still says ask before creating anything new. No agent or schedule was created here. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```
Set up a recurring version of my content marketing
agent that runs daily, with the same goal sentence,
search phrases and excludes. Hook and format analysis
and Meta ads on.
```

## Monday brief — separate recurring-results prompt

Last 7 days; brief under 300 words; 3 double-down / 2 stop / 1 test; every line cites link/views/followers; then 5 scripts. The source does not define whether the script block is inside the brief's word limit or supply timezone/scheduling settings. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```
From my recurring agent's last 7 days of results, give
me a brief under 300 words:
- 3 things to double down on
- 2 things to stop
- 1 thing to test
Each line cites one video (link, views, followers).
Then 5 scripts to record this week.
```

## Related

- [[content-research-agents]] — execution gates, detailed outputs, cadence and evidence limits.
- [[virlo]] — source-described connector and data platform.
- [[dsqjaffa]] — author provenance.
- [[format-propagation]] — Matt's distinct human-taste/no-AI-hooks position.
- [[content-research-agent-discovery-prompts]] — the other half of the task contracts.
