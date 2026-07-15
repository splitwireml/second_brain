---
title: Paul Solt
created: 2026-04-20
updated: 2026-07-11
type: entity
tags: [person]
sources: [raw/articles/paul-solt-app-store-packaging-250-5k-mrr-2045580498232373433.md, raw/articles/xarticle-how-i-build-apps-with-codex-without-opening-xcode-2040132557983936772.md, raw/articles/xarticle-codex-built-8-features-overnight-5-step-pr-loop-2073470146115490230.md]
---

# Paul Solt

X creator [@PaulSolt](https://x.com/PaulSolt). Covers iOS/macOS development with AI tools and App Store monetization strategies.

## Source

[$250 to $5K MRR: 5 App Store Packaging Rules That Actually Work](https://x.com/PaulSolt/status/2045580498232373433) — Article-format tweet synthesizing Viktor Seraleev's app store experimentation data. Covers 5 rules: icon design, screenshot storytelling, onboarding, paywall placement, and simple user flow.

## Content

The article distills Viktor Seraleev's consulting work on App Store conversion optimization. Key framework: apps stuck at $250-300/month MRR don't have a traffic problem — they have a **packaging problem**. The 5 rules:

1. **Icon** — Bold, clear, readable at 60×60 thumbnail; ChatGPT can generate mood boards to explore styles
2. **Screenshots** — Tell a story across the sequence; don't teach the app, show the outcome; first 3 screenshots seen in search results
3. **Onboarding** — 3-4 screens max, paint the outcome, don't teach usage, get users to the "aha" moment fast; video in onboarding improves conversions
4. **Paywall** — 75% of Viktor's revenue from paywall before using the app; place right after value moment, no hidden close button; use 3-day/7-day/30-day free trial, weekly pricing $5.99-7.99/week
5. **Flow** — One screen, one action, clear path; every extra tap loses users

## Viktor Seraleev Connection

Paul's article references Viktor Seraleev (@seraleev) as the source of the app store conversion data. Viktor's 12 app store experiments are available at super-easy-apps.kit.com.

## Codex / Apple app workflow

Paul's April 2026 article adds an implementation layer to his Codex work: make iPhone and Mac projects agent-friendly before asking the agent to own more of the build loop. The source uses [[appcreator]] to scaffold or retrofit projects, a `Makefile` around `xcodebuild` and `xcbeautify`, separate fast unit-test and slower UI-test targets, runtime logs, focused human steering, and local Apple documentation through DocSetQuery. The reusable synthesis is [[agent-friendly-xcode-projects]]: reduce noisy feedback and expose deterministic checks before increasing agent autonomy.

The workflow's productivity and reliability claims remain source-described; the linked AppCreator positioning and DocSetQuery repository were independently checked.

## Manager-worker PR loop

Paul's July 2026 follow-up documents a concrete [[manager-worker-pr-loop]]: one Codex manager thread coordinates isolated worker threads, watches PRs and CI on a 5–10 minute heartbeat, routes review feedback back to workers, and gates merges on tests plus manual UI checks. The source reports an 8-feature, 12-hour-19-minute run and a four-task proof of concept before scaling; those throughput claims remain source-reported.

## Related

- [[viktor-seraleev]] — primary source for the app store packaging data
- [[app-store-packaging]] — concept page
- [[agent-friendly-xcode-projects]] — Codex/Xcode workflow from the follow-up source
- [[appcreator]] — skill named in the follow-up source
- [[codex]] — coding agent used in the workflow
- [[manager-worker-pr-loop]] — manager/worker PR orchestration from the latest source
