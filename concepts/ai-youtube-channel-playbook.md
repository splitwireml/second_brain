---
title: AI YouTube Channel Playbook
created: 2026-07-24
updated: 2026-08-05
type: concept
tags: [ai-video, video, content, content-strategy, content-automation, content-creator, marketing, youtube, framework, virality, x-article]
sources: [raw/articles/xarticle-how-i-built-a-viral-youtube-channel-from-zero-usin-2079148684697391164.md, raw/articles/xarticle-how-i-use-claude-fable-5-to-build-10kmo-faceless-a-2080651345548480683.md, raw/articles/xarticle-how-to-turn-nexlev-mcp-opus-5-into-a-247-youtube-v-2081430939213906262.md, raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]
related_entity: [[dmtr-btc]]
---

# AI YouTube Channel Playbook

A source-described workflow for building a long-form YouTube channel from zero by reverse-engineering channels that already work, turning the observations into reusable “Bibles,” and closing the loop with analytics and viewer feedback. The durable unit is not a one-off prompt: it is a continuously updated [[content-strategy]] document that governs topic selection, hooks, story, retention, visuals, and scripting.^[raw/articles/xarticle-how-i-built-a-viral-youtube-channel-from-zero-usin-2079148684697391164.md]

## Workflow

1. **Test the niche.** Check whether older videos still attract views, whether the niche monetizes well, and whether a new creator can explain it from a differentiated angle.
2. **Choose reference channels.** Study 3–5 consistent long-form channels rather than guessing from personal interest or a single breakout video.
3. **Build the Bibles.** Use transcripts, comments, articles, and notes to produce Curiosity, Retention, Story, and Topic Bibles; add a Visual Bible from thumbnails, frames, pacing, and composition.
4. **Merge a Master Bible.** Synthesize the five documents into a compact guide organized by topic selection, hook structure, story architecture, retention rhythm, and visual style.
5. **Draft, then humanize.** Use [[claude]] for niche pressure-testing, synthesis, and an initial script; the creator supplies lived experience, judgment, personality, and the final angle.
6. **Run the production checklist.** Read the script aloud, plan B-roll and framing, edit around retention beats, and use the visual rules for thumbnails. The article explicitly defers its named production tools to a promised Part 2.
7. **Rewrite from evidence.** After a week, use comments to find questions and confusion; after 28 days, feed view duration, drop-off, click-through rate, traffic source, and comments back into the Master Bible.

## What is reusable

The framework separates **research**, **synthesis**, **production**, and **learning**. It also separates proven structural patterns from the creator’s own experience: copying a hook without topic expertise is presented as a failure mode, while the human layer is responsible for specificity and judgment. This makes the playbook an upstream long-form counterpart to [[faceless-content-system]] and the shorter-form format-discovery loop in [[ai-video-virality-formats]].

## Evidence boundaries

The author reports reaching monetization in under four months, 15k–40k views on the first ten system-made videos, and $3k–$6k/month in month six. These are source-reported results, not independently audited benchmarks. NotebookLM, Claude, channel sizes, retention figures, and production recommendations are likewise source-described workflow details, not verified platform guarantees.^[raw/articles/xarticle-how-i-built-a-viral-youtube-channel-from-zero-usin-2079148684697391164.md]

## Faceless story-channel variant

A local X Article describes a more production-oriented branch of the playbook: keep one Claude Project per niche, encode chapter lengths, hooks, character state, cliffhangers, and voice directives in JSON, and load 2–3 competitor transcripts as a reference library. Fiction uses a one-line title prompt; documentary work starts with a research brief containing dates, names, timelines, quotes, and citations, followed by script generation and 18 image prompts. This extends the existing research/synthesis loop with a concrete output contract, but the source's capability, speed, revenue, and publish-ready claims are not independently verified. ^[raw/articles/xarticle-how-i-use-claude-fable-5-to-build-10kmo-faceless-a-2080651345548480683.md]

## Nexlev MCP + Opus 5 analyst variant

Haris's article adds a data-connected analyst branch to this playbook. A source-described Nexlev MCP connection gives Opus 5 natural-language access to 60+ YouTube research tools: channel analytics, video performance data, competitor benchmarking, monetisation estimates, niche intelligence, outlier detection, and audience demographics. The proposed interface is a Claude Project whose project knowledge includes a Markdown file named `channel-analyst.md`; the source's title calls the result a 24/7 analyst, but it does not specify scheduling, a daemon, or continuous execution. ^[raw/articles/xarticle-how-to-turn-nexlev-mcp-opus-5-into-a-247-youtube-v-2081430939213906262.md]

### `channel-analyst.md` analytical framework

The supplied file is headed `# channel analyst skill file v1` and tells the model to act as a senior YouTube channel analyst with expertise in faceless channel growth, retention engineering, and monetisation strategy, with access to Nexlev MCP tools for real-time YouTube analytics data. Its four rules are:

1. **Retention is the only metric that matters for distribution.** Trace every conclusion to watch time relative to video length; the source's example is 70% retention in a saturated niche being distributed over 40% retention in an untapped niche.
2. **Script structure determines retention.** Editing, thumbnails, and production value are secondary variables; diagnose the script layer first because it is the skeleton.
3. **Outlier analysis beats average analysis.** Find outlier videos at 5x+ the channel average before deciding what works.
4. **Competitive positioning beats absolute performance.** Interpret a channel relative to its own average and 3–5 direct competitors: 50K views can be excellent for a 10K-average channel and a decline for a 100K-average channel.

### Analysis modes and exact operating sequence

- **Full channel audit:** pull the last 30 videos with Nexlev tools; calculate channel averages for views, retention at 0:30 if available, and upload frequency; identify the top 5 outliers by view-to-average multiple and bottom 5 underperformers; compare hook structure, topic framing, title construction, and thumbnail approach; identify the 3 most actionable changes for average retention; and produce a priority-ranked strategy document.
- **Competitor benchmarking:** pull the last 20 videos from each competitor; map topic overlap; identify topic gaps where competitors have high-performing topics the client has not covered; compare average views per upload; find the competitor with the strongest retention signals and inspect its script-level differences; then produce a competitive positioning map of the client's strengths, weaknesses, and blue-ocean opportunities.
- **Niche opportunity scan:** use Nexlev niche-intelligence tools to find channels with high view-to-subscriber ratios; filter for channels under 50K subscribers with average views above 100K; estimate the RPM bracket, content format, topic categories driving outliers, and monetisation status for each; rank by RPM potential and competition level; and produce 5 niche recommendations with a paragraph of justification each.
- **Retention diagnosis:** request the underperforming video's transcript and check four named mistakes: **delay disease** (the first 15 seconds does not confirm the subject around the viewer's situation), **context dump** (explanation fills the first 90 seconds before a concrete demonstration), **payoff void** (a 30–60 second gap between a mini payoff and the next curiosity trigger), and **grand payoff betrayal** (the title's main promise is not foreshadowed at least 3 times). Then check whether pacing varies through compression, expansion, and shock cycles or stays flat; test authenticity with the exact “would claude write this by default?” question and AI-slop vocabulary patterns; and produce a section-by-section diagnosis with specific rewrite recommendations.

The output contract is to cite specific Nexlev data, use specific numbers rather than ranges or approximations, name the exact problem before proposing a fix, rank recommendations by expected retention impact from highest downward, and never recommend changing the niche as the first action—the script layer is diagnosed first. ^[raw/articles/xarticle-how-to-turn-nexlev-mcp-opus-5-into-a-247-youtube-v-2081430939213906262.md]

### Source prompts and model rationale

The article gives three example prompts. They are preserved here as source text, not validated operating instructions:

```text
"run a full channel audit on [channel name or URL]. i want to understand why our last 10 uploads have averaged 15,000 views when our outlier videos have hit 200,000+. identify the structural differences between the outliers and the underperformers and give me the top 3 changes that would move the average."

"benchmark my channel [URL] against these 4 competitors: [URLs]. show me where i'm winning, where i'm losing, and where the blue ocean opportunities are that none of us are covering."

"scan for untapped niche opportunities in the [broader category] space. i want channels with fewer than 30,000 subscribers that are pulling 100K+ average views. filter by RPM above $8 and show me the content format driving the outliers."
```

The first prompt is described as a 30-video comparison, the second as five-channel simultaneous analysis, and the third as a narrower prompt-level filter than the mode description's under-50K-subscriber rule. The article says a human analyst takes 3–5 hours for the audit while Opus 5 does it in one conversation, and that the niche query once required 2–3 hours of manual filtering but runs in minutes with simultaneous filters; these are source claims.^[raw/articles/xarticle-how-to-turn-nexlev-mcp-opus-5-into-a-247-youtube-v-2081430939213906262.md]

The source presents Opus 5 as Anthropic's most capable publicly available model, “mythos-class” intelligence with safety classifiers, and state-of-the-art across coding, reasoning, vision, knowledge work, and long-horizon agentic tasks. It claims `$10` per million input tokens and `$50` output tokens, a 1M-token context window, self-checking analysis, and a 10-point gain over Opus 4.8 on Hex's core analytics benchmark—the first model to break 90%. It contrasts this with Sonnet 5 at `$2`/`$10` per million tokens, claims a full audit costs under `$5` in tokens versus `$500–$1,000` for a human, and says the task economics compare favorably with a `$5K–$10K` monthly consultant. Model identity, availability, prices, benchmark, context-window size, self-checking behavior, and cost claims are all source-described and unverified. ^[raw/articles/xarticle-how-to-turn-nexlev-mcp-opus-5-into-a-247-youtube-v-2081430939213906262.md]

### Scriptwriting loop and evidence boundary

The intended loop is: the channel audit identifies structural patterns; competitor benchmarking identifies topics; retention diagnosis identifies what to fix; a script brief encodes the fix; and the next skill-file-produced batch is informed by the prior batch's data. The source points to `fyreinteractive.co/newsletter` for a deeper retention-diagnosis-to-script-rewriting discussion and to `fyreinteractive.co/facelessos` for the full FacelessOS offer. It describes FacelessOS as running this loop for 200+ creators and reports Ed taking two faceless channels from zero in January to `$50,000+` in two months, plus Joey's 863,000-view script being derived from an outlier pattern no competitor used. It advertises an analyst skill file, 15 other skill files, and 6 power workflows calibrated across 7,000+ scripts and 42+ niches, followed by a separate claim of 8,000+ scripts, `$5M+` generated for clients, 21 Claude skill files, and 50+ niches. These are attributed promotional claims, not independent evidence. ^[raw/articles/xarticle-how-to-turn-nexlev-mcp-opus-5-into-a-247-youtube-v-2081430939213906262.md]

The source does not provide Nexlev installation or authentication steps, exact tool names/schemas, MCP transport or API endpoints, a dataset or analytics provenance trail, retention-definition details, an evaluation protocol, actual tool-returned outputs, or implementation details for a 24/7 scheduler/worker. It also does not independently establish Opus 5 or Sonnet 5 release/version status. The raw article preserves the linked URLs and its nested X-export frontmatter verbatim. ^[raw/articles/xarticle-how-to-turn-nexlev-mcp-opus-5-into-a-247-youtube-v-2081430939213906262.md]

## Miss Scarlett's one-hour faceless-channel variant

Miss Scarlett's article presents a more execution-oriented branch of this playbook: choose a niche by RPM and repeatability, use [[claude]] for ideas and scripts, generate narration before visuals, assemble in CapCut, package the upload, and batch/schedule posts. The article says the author's main horror channel reached 100,000 subscribers and more than $50,000 from YouTube in recent months while taking about one hour per day; those outcomes, timing, and algorithm claims are source-reported rather than independently audited. ^[raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]

### Policy and evidence boundary

The source says that a July 2026 YouTube rule change began treating lazy, mass-produced AI videos as “inauthentic content,” with a described three-strike path of warning, 90-day suspension, and removal from monetization. It does not say that AI is banned: its proposed safe boundary is one layer of real value in every video—an original written story, a deliberate voice choice that gives the channel identity, original images/covers rather than repeated stock clips, and variation between videos. The rule, enforcement sequence, and “safe” conclusion are source-described and should not be treated as verified platform policy without independent confirmation. ^[raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]

### Niche selection and exact prompt

The source recommends choosing by estimated RPM and repeatability rather than personal interest. Its rough source ranges are finance/business `$15–$40` per 1,000 views, tech/AI `$10–$25`, education/philosophy `$6–$15`, horror/stories `$4–$10`, and kids/general entertainment `$2–$6`. It then asks whether the niche can sustain 200 videos; examples include horror stories, kids stories, philosophy questions, scary history, sleep stories, and motivation. The ranges, the repeatability heuristic, and the claim that horror trades lower RPM for huge, endlessly producible view volume are source claims.

```text
Act as a YouTube strategist for faceless AI channels. I want to start one.
Analyze these niches: [list 5 you are considering].
For each, give me: estimated RPM range, how saturated it is, how easy it is
to make 200+ videos, the audience size, and one content angle nobody is doing
well yet. Then pick the single best one for a beginner and give me 30 video
title ideas for it. If you cannot easily list 30, the niche is too narrow.
```

### Named tool stack and ordered handoffs

The source's intentionally small stack is:

- **Claude** — ideas, scripts, titles, and descriptions; approximately `$20` per month in the source.
- **ElevenLabs** — reads the script aloud; the source recommends choosing one voice and keeping it for channel identity, at approximately `$22` per month.
- **Kling**, **Runway**, or **Higgsfield** — turn still covers/images into moving shots; free tiers are said to exist and paid use is described as about `$20–$30` per month when scaling.
- **CapCut** — drops visuals onto the voice track, adds auto-captions, and exports the assembled video; described as free.
- **Canva** — makes thumbnails; described as free.

The source calls the starting total roughly `$30` per month and says free tiers can be used, even though its individual price estimates imply a different total; this is an internal source claim, not reconciled pricing. It explicitly does not specify a model/version for any tool, an API or connector, audio/video file format, file path, dimensions, frame rate, codec, caption settings, or scheduler implementation. ^[raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]

The source's daily production order and handoffs are:

1. **Ideas:** once a week, ask Claude for a batch of titles and choose the strongest; about 10 minutes for a week of content.
2. **Script:** have Claude write for retention, read it once, and fix anything that feels wrong; about 15 minutes.
3. **Voice:** paste the script into the voice tool, generate, and download; about 5 minutes.
4. **Visuals:** generate a cover and images or moving shots, with one new visual for every pause in the voice; about 15 minutes.
5. **Assembly:** drop visuals onto the voice track in CapCut, turn on auto-captions, and export; about 15 minutes.
6. **Packaging:** have Claude write the title, description, and tags, then make the thumbnail in Canva; about 10 minutes.

The listed timings add up to more than the article's “about one hour” headline, so both are preserved as source-described estimates. The article says several videos can be made in one sitting and scheduled to post automatically through the week; making is “manual-ish” while posting is fully automated, with more of the pipeline expected to automate over time. Its human/automation boundary is “you become the director, the AI becomes the crew.” ^[raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]

### Retention script and packaging prompts

The article supplies this exact script prompt:

```text
You are a senior YouTube scriptwriter for a faceless [niche] channel.
Write a full script for the video titled: [title].
Length: about [8-10] minutes. Audience: [who].

Structure it like this:
- Open with a hook in the first 5 seconds using a shocking line or question.
  No intro and no "hey guys."
- Build tension with specifics and the word "you."
- Main body in 3 to 5 sections. Each one: a bold point, a real example,
  and a small cliffhanger into the next.
- Add a pattern interrupt every 60 to 90 seconds so attention never drops.
- Close by calling back to the hook and asking for the subscribe naturally.

Write for speaking, short sentences, no filler.
Also give me 5 thumbnail ideas and 3 title options.
```

For metadata and packaging it supplies:

```text
Act as a YouTube SEO and packaging expert.
Video topic: [topic]. Niche: [niche].
Give me:
1. A title under 60 characters that triggers curiosity
2. A 200-word description that is SEO friendly with a call to action
3. 15 tags mixing broad and specific
4. 3 pinned comment ideas to boost engagement
Optimize for click-through and watch time.
```

The accompanying heuristics are a simple thumbnail with one focal point, strong emotion or curiosity, high contrast, and at most three words; curiosity-led titles; and a claim that title and thumbnail produce 80% of the result. These are source recommendations, not measured guarantees. ^[raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]

### Monetization, feedback, and scaling rules

The article describes two current monetization levels: level one for fan funding at 500 subscribers, 3 public uploads, and either 3,000 public watch hours in the past year or 3 million Shorts views in 90 days; and level two for ad revenue at 1,000 subscribers plus 4,000 watch hours in the past 12 months or 10 million Shorts views in 90 days. Its proposed strategy is long videos as the money base, cutting each into several Shorts to chase views and feed subscribers back to the main channel, while still requiring value and variety for approval. These requirements and the claim that long videos pay more but grow slower than Shorts are source-described and time-sensitive.

The source further recommends finding videos whose views greatly exceed their channel's subscriber count, adapting the format to a fresh subject, keeping horror suspenseful rather than graphic because gore can trigger limited ads, using YouTube's thumbnail test tool, watching click-through and watch duration during the first 48 hours, building narration before visuals so pauses determine image changes, and publishing 20–30 videos before judging the channel. Its scaling model tests several niche channels for a couple of months, kills flops, and concentrates on the one or two that pop. The first-30-day cadence is: week 1 choose the niche with Claude and set up the stack; week 2 make and post 3–5 videos without judging them; weeks 3–4 keep a fixed schedule and study attention. ^[raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]

The source does not specify the YouTube thumbnail-test interface/menu path, analytics export or evaluation procedure, exact content-review checklist beyond reading and fixing the script, the renderer or image-generation model behind the named tools, the voice model, file formats, storage paths, compression, accessibility/fallback behavior, or how automatic posting is implemented. Its revenue (`$50,000+`), subscriber (`100,000`), RPM, tool-cost, one-hour, monetization, “safe,” and growth claims remain evidence boundaries rather than verified wiki facts. ^[raw/articles/xarticle-i-built-faceless-youtube-channel-with-claude-today-2084611385376285065.md]

## Related

- [[thegoldeenhand]]
- [[vampscally]] — source author of the one-hour faceless-channel variant
- [[dmtr-btc]] — source author and operator of the playbook
- [[fyreinteractive]] — source author of the Nexlev MCP + Opus 5 analyst variant
- [[youtube]] — research surface and long-form publishing platform
- [[claude]] — source-described niche, synthesis, and scripting tool
- [[elevenlabs]] — source-described narration tool
- [[faceless-content-system]] — adjacent multi-platform faceless publishing system
- [[content-strategy]] — broader cadence and audience-planning context
- [[ai-video-virality-formats]] — adjacent short-form format-research loop
