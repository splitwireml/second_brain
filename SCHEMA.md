# Wiki Schema

## Domain
AI/ML agent, local LLM inference, AI-powered content creation, and productivity automation. Covers agent architectures, local inference optimization (Apple Silicon, consumer GPU), vibe coding, UGC systems, B2B services, and the creator-developer crossover. This is a personal knowledge base for understanding what's real vs. hype in the fast-moving AI space.

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `hermes-agent-delegation.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[[wikilinks]]` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages synthesizing 3+ sources, append `^[raw/articles/source-file.md]`
  at the end of paragraphs whose claims come from a specific source. This lets a reader trace each
  claim back without re-reading the whole raw file. Optional on single-source pages where the
  `sources:` frontmatter is enough.

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
# Optional quality signals:
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

`confidence` and `contested` are optional but recommended for opinion-heavy or fast-moving
topics. Lint surfaces `contested: true` and `confidence: low` pages for review so weak claims
don't silently harden into accepted wiki fact.

## raw/ Frontmatter

Raw sources ALSO get a small frontmatter block so re-ingests can detect drift:

```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content below the frontmatter>
---
```

**Tag Taxonomy**
[Stable top-level tags. Add new tags here BEFORE using them.]
Canonicalization note: prefer the stable canonical forms `agent`, `ai-agent`, `tools`, `ai-tools`, `ai-company`, `framework`, `business-models`, `services-as-software`, and `sub-quadratic`. Rewrite wiki pages to those tags. Keep only the minimum legacy aliases needed for raw-source compatibility.

**Legacy aliases (raw-source compatibility only)**
- agents, ai-agents, AI-company

**Core AI/ML**
- ai, llm, model, vision, speech, image, video, generation, inference, quantization, training, fine-tuning, reasoning, moe, multimodal, tokenization, ai-agent, ai-tools, ai-ugc, ai-business, ai-video, ai-model, ai-automation, ai-services, ai-research

**AI/ML & Inference**
- ai-agent, ai-tools, ai, local-llm, inference, optimization, training, fine-tuning, benchmark, evaluation, quantization, architecture, llama.cpp, kv-cache, database, pytorch, ml, machine-learning, lightweight, generative-models, generative-ai, genai

**Local Inference**
- local-llm, mlx, apple-silicon, gpu, consumer-gpu, gguf, onnx, local-ai

**Agent Systems**
- agent, orchestration, workflow, memory, skills, delegation, tools, ai-agent, multi-agent, agent-tool, sandbox, skill, browser-agents, agentic-ai, company-brain

**Content & Creator**
- ugc, content, creator, x, tiktok, instagram, video, viral, seo, marketing, viral-marketing, virality, content-marketing, content-strategy, content-automation, content-creator, ai-ugc, social-media, ai-content

**Business & Monetization**
- monetization, b2b, business, lead-gen, services, agency, productivity, funnel, affiliate-marketing, ecommerce, micro-saas, freelance, course, subscription, business-models, idea, opportunity, side-hustle, freelancing, consulting, sales, finance, client-acquisition

**Web & SEO**
- seo, local-seo, web-scraping, browser-automation, web-development, website, landing-page, conversion, outbound, cold-email, local-business, backlink, tools, tutorial

**Browser & Automation**
- browser-automation, web-scraping, anti-detection, automation, workflow, workflow-automation

**Development**
- coding, agent-tool, prompt-engineering, prompting, cli, ide-extension, desktop-app, framework, developer, code-generation, testing, tooling, github, claude-code

**Image & Video**
- image-generation, video-generation, background-removal, image-segmentation, 3d, 3d-vision, 3dgs, computer-vision, image-to-svg, segmentation, image-processing, seedance-2-0

**Memory & Knowledge**
- memory, knowledge-management, pkm, second-brain, rag, embedding, vector-database, obsidian, organizational-design

**Design & UI**
- ui-design, design-tool, design, product-design, user-experience, onboarding, product, ai-design, html, psychology, behavioral-science

**Personality & Characters**
- ai-persona, character, tiktok, instagram, youtube, platform, ai-curator

**Meta & Identity**
- comparison, method, failure, knowledge, person, company, product, platform, brand
- content-creator, x-creator, ai-curator, ai-influencer, ai-persona, solo-founder, freelancer, bootstrapped, x-article
- open-source, oss-ai, self-hosted, saas, product, tools, no-code, low-code, platform, ai-company, startup, software, enterprise, nous-research

**Tools & Infrastructure**
- tools, platform, product, saas, open-source, self-hosted, no-code, low-code, infrastructure, security, wireguard, caddy, microvm

**Research & Benchmarks**
- research, benchmark, evaluation, cvpr-2026, deep-learning, training, computer-vision, project, enterprise-ai, embodied-ai, robotics, neuroscience, football, marketplace, analytics

**Technical Topics**
- optimization, efficiency, transcription, audio, performance, mcp, protocol, architecture, reasoning, vision-language, diffusion, search, codex, hermes-agent, vibe-coding, export-failure, export-failed, bird-read-failure, koai, moonshot-ai, asr, tts, training-free, cost-optimization, gtm, context-window, pricing, svg, reliability, system-prompt-design, hardware, engineering, career, influencer, skill-learning

**Chinese AI**
- chinese-ai, qwen, minimax, tencent, baidu, bria-ai, bytedance, moonshot-ai, kimi-k2.6

**Business & Freelancing**
- growth, upwork, user-acquisition, openai, anthropic, google, ai-generated-ads, service, thread, ai-agent-automation, mobile-apps, independent-developer, micro-saas, y-combinator, indie-hacker, bootstrapped, founder, solo-founder, side-hustle, freelancing, freelance, freelancer, freelance-business, business-models, business-loop, business, monetization, revenue, income-system, ai-business, ai-monetization, company-building, entrepreneurship, one-person, ai-marketing, paid-ads, facebook-ads, instagram-ads, meta-ads, google-maps, campaign-setup, distribution-strategy, distribution, lead-magnet, buyer-persona, cro, copywriting, hooks, account-warming, cold-calling, peptide-marketing, sales, services-as-software, proposal, job-search, talent, interview, education, podcast, blog, event, experiment, release, retargeting, blog-marketing, ai-writing

**Tag Taxonomy — Extended (2026-06-07 optimization pass)**

**Tools & Platforms**
- cursor, aider, claude, claude-code, claude-skill, claude-desktop, gemini, elevenlabs, fal-ai, comfyui, world-labs, shopify, netflix, harvey, mercado-libre, autogen, langgraph, mem0, n8n, inngest, paperclip, postiz, openclaw, iii, xurl, autobrowse, perplexity, yt-dlp

**Languages & Frameworks**
- python, rust, golang, fullstack, stack, framework, integration, json-rpc, xml-tags

**Infrastructure**
- api, http-api, filesystem, mcp, macos, apple, apple-silicon, metal, cuda, nvidia, aws, cloud, on-device, virtualization, virtio, microvm, ssd-paging, computer-use, browser-automation, anti-detection, configuration, context-engineering, observability, deployment, ingestion-pipeline, indexing, vector-search, vectorization, knowledge-graph, graphrag, rag, embedding, vector-database

**AI/ML Techniques**
- ai-researcher, ai-research, llm-inference, llm-architecture, llm-training, llms, slm, moe, transformer, vllm, tokenizer, tokenization, token-economics, reasoning, inference-engine, inference, quantization, fine-tuning, distillation, sparse-attention, sub-quadratic, subq, model, vision-language, multimodal, multimodal-models, text-to-image, text-rendering, image-to-video, flow-matching, diffusion, egocentric, interactive-segmentation, salient-object-detection, video-segmentation, segmentation, object-detection, object-tracking, pose-estimation, point-tracking, image-segmentation, ocr, document-understanding, document-processing, pdf, image-restoration, alpha-matting, video-matting, reconstruction, dynamic-scenes, 3d-animation, 3d-vision, 3dgs, gaussian-splatting, 3d-scene-generation, framer-motion, scroll-effect, animated-websites, worldmodel, world-models, real-time-generation, rendering, vla, embodied-ai, robotics, simulation, context, context-limits, compression, durable-execution, recency-ranking, search-ranking, semantic-distillation, perception, detection, extended-thinking, pre-fill

**Agent Systems**
- agent, ai-agent, agentic, agentic-ai, multi-agent, agent-swarm, agent-delegation, agent-systems, agent-tool, agentic-workflow, ai-agent-workflow, agent-configuration, ai-agent-teams, ai-agent-memory, ai-agent-automation, delegation, sub-agent, subagents, worker, sandbox, background-agents, browser-agents, autonomous, autobrowse, ai-infra, coordination, orchestration, memory, memory-management, skills, tools, slash-commands, plugin, plugin-system, skill, skill-authoring, skill-management, skill-learning, ai-skill, use-cases, quickstart, ecosystem, community, collaboration, paperclip

**Data & Pipelines**
- data-pipeline, data-extraction, data-prep, ingestion-pipeline, vector-database, embedding, vectorization, indexing, knowledge-graph

**Vision & Multimodal**
- vision, vision-language, computer-vision, 3d-vision, 3d, 3dgs, image-to-video, text-to-image, egocentric, video-matting, salient-object-detection, interactive-segmentation, image-restoration, reconstruction, simulation

**People & Creators**
- person, ai-curator, ai-influencer, ai-persona, content-creator, x-creator, tech-influencer, founder, solo-founder, indie-hacker, freelancer, freelance, bootstrapped, monk

**Companies & Orgs**
- company, ai-company, nous-research, openai, anthropic, google, qwen, moonshot-ai, minimax, baidu, bria-ai, bytedance, tencent, openclaw, huggingface

**Platforms & Products**
- tiktok, instagram, x, youtube, notion, airtable, slack, telegram, obsidian, airr, readwise, blockify, yt-dlp, xurl, vadoo, mengto, sajjad-khader, roboflow, iii

**Image & Video Models**
- kling, higgsfield, comfyui, stable-diffusion, midjourney, sora, seedance, qwen-image-layered, sam3, segment-anything, rmbg, withoutbg, depth-anything

**Meta & Project Management**
- project, project-management, task-management, scheduling, comparison, method, failure, knowledge, brand, idea, opportunity, strategy

**Self-Improvement**
- self-improvement, skill-learning, career, education, learning, fitness, islam, quran

**Knowledge Management**
- pkm, knowledge, knowledge-management, second-brain, organizational-design, obsidian, mem0, rag, knowledge-graph

**Marketing & SEO**
- seo, local-seo, aio, geo, search-ranking, backlinks, backlink, conversion, cro, copywriting, hooks, blog, podcast, viral, viral-marketing, virality, content-marketing, content-strategy, content-automation, content-creator, content-system, content-infrastructure, content-os, ai-content, content-compounding-system, bookmarkable-content, social-media, tiktok, instagram, youtube, x, x-article, marketing, sales

**Sources & Types**
- paper, paper-list, cvpr, cvpr-2026, open-source, open-source-ai-stack, open-source-saas, oss-ai, mit-license, release, podcast, blog, transcription

**Wiki Metadata**
- divyansh-tiwari, wiki, meta, optimization, lint, taxonomy

**Misc**
- music, sports-betting, free-tier, pricing, services-as-software, software, claude-desktop, copyrebeldia, ai-company, better-stack, developer-tools, benchmarking, webdev, ai-coding, ai-tools, cost-reduction, cost-optimization, workflow-optimization, production-llm, few-shot-prompting, terminology, framework-trap, zero-shot, prediction, rl, affiliate, creative, local-first, information-density, layered-image-decomposition, automated-capture, feedback-loop, ux, linkedin-growth, patreon, composition, slideshow, synthesis, vertical-language-models, templates, ux-design, website-design, transformers-js, x-api, documentation, communication, amazon, vibecode, ai-infra, competitor-analysis, serving, teams, compounding, system, pipeline, ingestion, ai-search, control-room, ui, dashboard, ingest-anything, leann, chrome-extension, linkedin, weights, legal, entertainment, messaging, twitter, tom-doerr, claude-cowork, karpathy, mindshare, arbitrage, networking

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Entity Pages
One page per notable entity (person, organization, product, program). Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities ([[wikilinks]])
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts ([[wikilinks]])

## Comparison Pages
Side-by-side analyses. Include:
- What is being compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Query Pages
Filed answers to specific questions. Include:
- Question (explicit)
- Answer
- Practical verdict
- Related pages ([[wikilinks]])

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report

## Wiki Health Rules
- Every page needs minimum 2 outbound wikilinks
- Pages over 200 lines get flagged for splitting
- Tags must come from the taxonomy above
- Provenance markers required on multi-source synthesis pages
- `sources:` (plural) required on all wiki pages — empty array if no direct sources
- Field ordering for concept pages: title, created, updated, type, tags, sources, related_entity, author
- Field ordering for entity pages: title, created, updated, type, tags, sources

## Related

- [[satyam-sales]]

- [[pencil-software]]

- [[falcon-perception]]

- [[cloudflare-email-workers]]

- [[autogen]]

- [[patreon-da-93-backlink]]

- [[meta-meta-prompting]]

- [[google-maps-client-acquisition]]

- [[enterprise-ai-readiness-gap]]

- [[distribution]]
