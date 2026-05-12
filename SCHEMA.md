# Wiki Schema

## Domain
AI/ML agents, local LLM inference, AI-powered content creation, and productivity automation. Covers agent architectures, local inference optimization (Apple Silicon, consumer GPU), vibe coding, UGC systems, B2B services, and the creator-developer crossover. This is a personal knowledge base for understanding what's real vs. hype in the fast-moving AI space.

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

## Tag Taxonomy
[Stable top-level tags. Add new tags here BEFORE using them.]

**AI/ML & Models**
- ai, llm, model, vision, speech, image, video, generation, inference, quantization
- local-llm, mlx, apple-silicon, gpu, consumer-gpu, gguf, onnx

**Agent Systems**
- agent, agents, orchestration, workflow, memory, skills, delegation, tools

**Content & Creator**
- ugc, content, creator, x, tiktok, instagram, video, viral, seo, marketing

**Business & Monetization**
- monetization, b2b, business, lead-gen, services, agency, productivity

**Technical**
- open-source, oss, computer-vision, architecture, coding, optimization, research

**Meta**
- comparison, method, failure, knowledge, person, company, product, platform

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