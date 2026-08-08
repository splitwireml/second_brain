---
title: Higgsfield
created: 2026-05-31
updated: 2026-08-08
type: entity
tags: [tools, ai-tools, genai, generation, video-generation]
sources: [raw/articles/xarticle-35k-motion-website-playbook-higgsfield-claude-code-2067204840342630789.md, raw/articles/thread-VadimStrizheus-2080128784418660566.md, raw/articles/xarticle-ai-video-workflow-2026-cinematic-masterpiece-2078133327714738454.md, raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md, raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]
---

# Higgsfield

AI video generation platform — character animation, video generation from image prompts. Part of the [[video-generation]] ecosystem.

The new source describes Higgsfield as the generative motion layer in a Claude/Claude Code motion-website workflow, including an MCP connector and a source-described Motion Website Generator skill. These capabilities and the associated economics remain source claims pending independent verification. ^[raw/articles/xarticle-35k-motion-website-playbook-higgsfield-claude-code-2067204840342630789.md]

## Archive clipping workflow

[[vadim-strizheus]]'s local thread describes using Higgsfield MCP with [[claude]] to process a 44-minute podcast into 20 ranked vertical clips, with hook scoring and a reported $1.04 credit cost. The thread presents this as a source-described processing workflow rather than independently verified Higgsfield performance or pricing. ^[raw/articles/thread-VadimStrizheus-2080128784418660566.md]

## Cinematic shot-generation role

The [[voyzlab]] article presents Higgsfield as a simpler starting aggregator with 15+ models, Cinema Studio virtual lenses (`35mm`, `50mm`, `85mm`), and a connector for driving generation from inside a Claude chat. These counts and capability descriptions are source claims, not independent product verification. ^[raw/articles/xarticle-ai-video-workflow-2026-cinematic-masterpiece-2078133327714738454.md]

## Seedance 2.5 CLI and agentic workflow (2026-08-04)

Machina's source describes Higgsfield as one surface, login, and credit pool for AI-video models, with an agentic CLI rather than only a manual generate button. The locally preserved setup commands are:

```text
npm install -g @higgsfield/cli
higgsfield auth login
npx skills add higgsfield-ai/skills
```

The article says the same CLI used for Seedance 2.0 is intended to carry Seedance 2.5 when access opens, allowing Claude Code or another harness to control model choice, submission order, retries, and a fleet of 30-second jobs—one per shot—then stitch them into an ad, launch video, or short film. These access, CLI, and capability statements are source-described; no command execution or independent product verification was performed. ^[raw/articles/xarticle-how-to-master-seedance-25-full-course-2084666171446726767.md]

## UGC factory surface (Machina, 2026-08-08)

Machina's source describes Higgsfield as one login, one surface, and one credit pool over image, character, video, and audio models. It presents two operating doors: **Supercomputer**, which needs no setup and runs product/niche research, scripts, images, clips, montage, and coherence refinement; and a DIY path where Higgsfield models are addressed from Claude Code so the agent owns model choice, ordering, retries, and the pipeline. The source's product capabilities, access, and “planning is free until render” framing are source-described rather than independently verified.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

The article says a UGC ad normally crosses research, writing, product image, character, video clips, audio, and assembly, creating quality-loss handoffs. Its DIY example renders the hook first, approves face and voice, attaches approved-hook audio to later clips, runs the remaining shots in parallel within the backend concurrency cap, and uses `ffmpeg` for ordered concatenation and loudness normalization. These are the source-described roles of the platform and Claude Code, not independently executed commands.^[raw/articles/xarticle-how-to-build-an-ai-ugc-factory-in-claude-code-2085362363214201033.md]

## Related

- [[video-generation]] — video generation more broadly
- [[ai-video]] — AI video generation
- [[kling]] — competing video generation platform
