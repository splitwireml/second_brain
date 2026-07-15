---
title: Claude-Obsidian Second Brain Stack
created: 2026-06-27
updated: 2026-07-08
type: concept
tags: [agent, workflow, memory, knowledge-management, obsidian, pkm, second-brain]
sources: [raw/articles/xarticle-the-10-step-second-brain-2069494292695932964.md, raw/articles/xarticle-this-ai-brain-will-make-you-so-smart-its-almost-un-2070848134209556898.md, raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md, raw/articles/xarticle-your-second-brain-is-useless-until-ai-maintains-it-2073375316840415716.md]
related_entity: [[moysei]]
---

# Claude-Obsidian Second Brain Stack

A ten-step-plus operator pattern for turning an [[obsidian]] vault into persistent, maintained working context instead of a passive note archive. Across sources, the stack combines a local markdown vault, an Obsidian REST bridge, MCP wiring, identity files, folder-level information architecture, selective extraction into structured notes, immutable raw sources, schema-guided synthesis, and scheduled/linted maintenance so the agent stops starting from a blank slate.

## Core flow

1. **Store notes locally in Obsidian** so the knowledge layer stays plain-text and model-portable.
2. **Expose the vault through the Obsidian Local REST API plugin** while Obsidian is running.
3. **Connect Claude through [[mcp]]** using the `mcp-obsidian` bridge.
4. **Interview the user into `CLAUDE.md`** so the model loads goals, projects, strengths, and communication style every session.
5. **Adopt [[andrej-karpathy]]'s `raw/` + `wiki/` split** so sources stay immutable while synthesized pages compound.
6. **Teach Obsidian-specific output formats** via the official `kepano/obsidian-skills` repository.
7. **Connect changing external data** like calendar events and captured materials.
8. **Schedule daily maintenance** to ingest new material, flag stale notes, and summarize change overnight.
9. **Use scoped credentials instead of prompt-only safety rules** for destructive operations.
10. **Bootstrap from community starter repos** when the user wants a packaged implementation instead of manual assembly.

## Additional details from Jey's six-step framing

The second source extends the same pattern with more emphasis on identity, note taxonomy, and self-maintenance cadence.^[raw/articles/xarticle-this-ai-brain-will-make-you-so-smart-its-almost-un-2070848134209556898.md]

- **Identity should be split into multiple files**, not just a single operating note: `USER.md` for role and work style, `SOUL.md` for voice and behavioral rules, and `IDENTITY.md` for the agent's own role definition.^[raw/articles/xarticle-this-ai-brain-will-make-you-so-smart-its-almost-un-2070848134209556898.md]
- **Vault structure should map to operating domains** such as People, Projects, Decisions, Companies, Meetings, Daily, and Knowledge, with optional MOCs once a topic gets dense.^[raw/articles/xarticle-this-ai-brain-will-make-you-so-smart-its-almost-un-2070848134209556898.md]
- **Ingestion should be extractive rather than archival**: meetings are useful because they can be distilled into decisions, commitments, preferences, and insights instead of being stored as raw transcripts.^[raw/articles/xarticle-this-ai-brain-will-make-you-so-smart-its-almost-un-2070848134209556898.md]
- **Nightly scheduled tasks are the compounding layer**: the vault behaves like a brain only when it revisits, links, and prunes notes while the user is away.^[raw/articles/xarticle-this-ai-brain-will-make-you-so-smart-its-almost-un-2070848134209556898.md]

## Chewa's eight-rule operating discipline

[[chewadot]] sharpens the same stack into eight rules that make the vault feel less like a note archive and more like a self-maintaining operating system.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]

1. **Voice beats keyboard** — capture has to be frictionless enough to happen at a crosswalk, which makes voice-to-inbox the preferred default.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
2. **One inlet, many outlets** — there should be exactly one dump zone for raw thought, while Claude handles downstream routing into topics, projects, and people.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
3. **Morning belongs to Claude, night belongs to you** — scheduled filing, backlinking, and daily-digest generation should finish before the human starts work.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
4. **The raw folder is sacred** — original captures stay immutable, while rewrites land in a processed layer so the system preserves source truth rather than silently rewriting memory.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
5. **Backlinks matter more than note count** — every new note should attach to multiple existing notes, including at least one much older note, so graph density compounds over time.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
6. **Weekly synthesis is the reread layer** — the real durable artifact is a once-a-week synthesis file that surfaces recurring themes, contradictions, and half-kept promises.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
7. **Context should preload every session** — Claude should begin with active work, open hypotheses, and recent decisions instead of forcing the user to re-explain themselves.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
8. **Graph growth is the pulse** — the success metric is not accumulated files but rising connection density across the vault.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]

## What this source adds

The new source pushes this concept away from generic "AI second brain" rhetoric and toward operating discipline:

- **Capture friction is the first bottleneck** — if capture requires typing or classification, the system dies at the inbox.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
- **Raw immutability is a design rule, not a folder preference** — preserving unedited source material protects against quiet memory drift as the agent rewrites notes.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
- **Link density is the real health metric** — a warehouse of files is not yet a thinking system; the graph only comes alive once Claude is explicitly instructed to backlink new notes into older context.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]

## DegenCalls' AI-maintained wiki thesis

[[degen-calls]] reframes the stack as a move from disposable retrieval to compounding knowledge: uploading a document and asking a chatbot is useful, but the synthesis usually disappears when the chat ends. The durable pattern is a local markdown wiki where raw evidence remains immutable, the LLM compiles sources into pages, the schema defines maintenance rules, and health checks/linting keep links, contradictions, indexes, and stale claims visible.^[raw/articles/xarticle-your-second-brain-is-useless-until-ai-maintains-it-2073375316840415716.md]

Operationally, this strengthens the Karpathy-inspired `raw/` + `wiki/` split already in the stack. The human role narrows to choosing sources, reviewing weak synthesis, and asking better questions; the AI role becomes clerical and structural: summarize, link, revise, cite, lint, and maintain. The article also clarifies why markdown matters: the knowledge base remains inspectable, versionable, portable, and easy for agents or scripts to modify rather than becoming trapped inside a proprietary chatbot interface.^[raw/articles/xarticle-your-second-brain-is-useless-until-ai-maintains-it-2073375316840415716.md]

## Evidence layers

**Confirmed**
- The raw source explicitly instructs readers to use Obsidian as the markdown store, Claude Code as the file-writing agent, the Obsidian Local REST API plugin as the bridge, and `mcp-obsidian` as the MCP connector.^[raw/articles/xarticle-the-10-step-second-brain-2069494292695932964.md]
- `mcp-obsidian` exists as a published npm package described as a "Model Context Protocol server for Obsidian Vaults."^[raw/articles/xarticle-the-10-step-second-brain-2069494292695932964.md]
- `obsidian-local-rest-api` exists as a published npm package for interacting with notes via a REST API.
- The GitHub repositories `kepano/obsidian-skills`, `AgriciDaniel/claude-obsidian`, `eugeniughelbur/obsidian-second-brain`, and `coleam00/second-brain-starter` all exist publicly.
- Jey's source explicitly recommends a plain-file Obsidian vault, three identity files (`USER.md`, `SOUL.md`, `IDENTITY.md`), seven core folders plus optional MOCs, extractive meeting summaries, and nightly scheduled maintenance at 11 p.m.^[raw/articles/xarticle-this-ai-brain-will-make-you-so-smart-its-almost-un-2070848134209556898.md]
- Chewa's source explicitly recommends voice-first inbox capture, a single raw inlet, scheduled morning filing, immutable raw notes, minimum backlink targets, weekly synthesis files, and automatic session preloading from the vault.^[raw/articles/xarticle-the-self-writing-vault-8-rules-for-pointing-claude-2071564521735684253.md]
- DegenCalls' article explicitly argues that the core value is maintenance: raw sources plus schema-governed wiki synthesis, health checks, indexes, citations, and contradiction tracking make knowledge cumulative rather than another one-off retrieval session.^[raw/articles/xarticle-your-second-brain-is-useless-until-ai-maintains-it-2073375316840415716.md]

**Likely**
- The pattern is most valuable for users who already accumulate meaningful notes, captures, or project context; an empty vault has little leverage.
- The daily 7 a.m. maintenance loop is operationally plausible once ingestion and routing are stable, but the article does not show a working production run.
- Measuring graph density and forcing links to old notes would materially improve retrieval quality compared with simple folder filing alone.

**Speculative**
- The articles' framing that one evening of setup is enough to "never re-explain yourself again" is marketing compression; long-term value still depends on note quality, retrieval discipline, and workflow upkeep.
- The Porto case study in Chewa's article is anecdotal and unverified in the raw export.
- The exact subscription pricing claim for Claude Pro from the first source was not independently verified during this ingest.

## Related

- [[obsidian-ai-second-brain]] — broader concept page for the recurring pattern
- [[obsidian-knowledge-vault-system]] — adjacent implementation with stronger capture and automation emphasis
- [[obsidian-vault-as-agent-context-source]] — narrower pattern focused on exposing a vault to an agent
- [[obsidian-vault-intelligence]] — adjacent argument that vault value comes from retrieval and synthesis rather than collection alone
- [[second-brain]] — umbrella PKM concept
- [[degen-calls]]
- [[chewadot]]
- [[moysei]]
- [[claude-code]]
- [[obsidian]]
