---
title: Hermes Auto-Think / Auto-Build
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [hermes-agent, ai-agent, self-improvement, skill-authoring, autonomous]
sources: [raw/articles/openclaw-hermes-source-code-elvis-2045155784577687862.md, raw/articles/garrytan-skillify-agent-reliability-2046876981711769720.md, raw/articles/xarticle-shmidt-hermes-agent-99-percent-never-touched-these-2051307460208578864.md]
related_entity: [[hermes-agent]]
---

# Hermes Auto-Think / Auto-Build

## Definition

Auto-Think and Auto-Build are the two complementary self-improvement loops in Hermes Agent that enable autonomous capability growth without human prompting:

- **Auto-Think** — Hermes reasons before acting, using chain-of-thought, `/reasoning` effort controls, and thinking-mode models to decompose problems before execution
- **Auto-Build** — Hermes autonomously writes, patches, and deletes skills based on what it learns, creating procedural memory that compounds across sessions

Together they form the self-improvement engine that makes Hermes "get better the more you use it."

## Auto-Think

### Mechanism

Hermes integrates reasoning models (o-style models) with effort controls via `/reasoning`:

> "Three power toggles. /yolo skips dangerous-command approvals. /fast flips to OpenAI Priority or Anthropic Fast Mode. /reasoning sets effort level for reasoning models. Most people stay on defaults forever and wonder why their sessions feel slow." — @shmidt

### When to Enable Thinking

From @leopardracer's benchmarks: thinking-mode models generate extensive chain-of-thought before answering. Great for complex analysis, disastrous for classification tasks:

> "With thinking enabled, a simple 'is this message a question or a request?' took 30+ seconds. The model generated 500 tokens of internal reasoning... All that thinking for a one-word answer."

**Use thinking for:** Architecture decisions, research synthesis, multi-step debugging, strategic planning

**Skip thinking for:** Fast classification, simple lookups, routine file operations

### Design Pattern

The latent/deterministic distinction from @garrytan:

- **Latent** = judgment tasks (reasoning, synthesis, decision-making) — needs the model
- **Deterministic** = precision tasks (calendar grep, file moves, API calls) — model should NOT do in latent space

The loop that makes this work: "the latent space builds the deterministic tool, then the deterministic tool constrains the latent space."

## Auto-Build

### Mechanism

Hermes has a `skill_manage` tool that lets the agent itself create, patch, and delete skills based on what it learns:

> "[Hermes Agent] has a skill_manage tool that lets the agent itself create, patch, and delete skills based on what it learns. When the agent finishes a complex task or recovers from an error, it proposes a skill and writes it to disk. That's procedural memory the agent earns on its own." — @garrytan

### The Self-Authoring Loop

@elvissun documented the hook after 9 hours studying the source code:

> "The system prompt has a nudge baked in: every N tool calls, consider saving a skill. after task completion, a background review scans for skill-worthy patterns. before context compression kicks in, durable knowledge gets flushed to disk. the prompt is blunt - if an existing skill covers this, patch it in place. only create new if nothing matches."

**Three trigger points:**
1. Every N tool calls → nudge to save a skill
2. After task completion → background review for skill-worthy patterns
3. Before context compression → durable knowledge flushed to disk

### What Gets Skillified

- Complex task completion patterns
- Error recovery procedures
- Multi-step workflows that worked
- Task-specific tool combinations that outperformed defaults

### Skill Explosion Problem

@elvissun identified the long-tail failure mode:

> "the agent wanted to read an image from my desktop. Tried browser read and vision skill, nothing worked. so it wrote a third skill read-local-image skill lol. these are 3 skills all adjacent to 'image + local filesystem + model can see it.'"

The agent is great at spotting "I should bottle this up" but less great at spotting "I already bottled this up three folders over." Net impact: skills accumulate faster than they consolidate.

### Built-In Skill Library

123 SKILL.md files ship on install before Hermes writes its own:
- GitHub PR workflows
- Obsidian
- Google Workspace
- Linear, Notion, Typefully, Perplexity
- Deep research
- Minecraft modpack server (lol)

> "this is what opinionated actually means. you're not getting a blank agent and a framework, you're getting an agent that already knows how to do 100+ things on day one and a self-improvement loop that learns more as you go." — @elvissun

## Key Files

- `tools/skill_manager_tool.py` — skill lifecycle management
- `~/.hermes/skills/` — where autonomous skills are stored
- `~/.hermes/checkpoints/` — shadow git commits before destructive operations (safety net for skill authoring)

## The Combined Loop

```
Task execution (latent reasoning)
    ↓
Failure or complex success
    ↓
skill_manage proposes a skill
    ↓
Deterministic code written to disk
    ↓
Next execution: skill constrains agent behavior
    ↓
Agent uses tool instead of reasoning about it
    ↓
More efficient execution, fewer tool calls
```

**Example from @garrytan:** "The agent used judgment (latent) to write calendar-recall.mjs. Now the skill forces the agent to run that script instead of reasoning about calendar data. The model's intelligence created the constraint that prevents the model from being stupid."

## Related Concepts

- [[hermes-skills-workflow]] — practical skill patterns by @0xJeff
- [[hermes-checkpoints-rollback]] — state recovery for skill authoring
- [[skillify]] — the broader pattern of turning failures into skills
- [[hermes-memory-architecture]] — 11-layer memory system that includes skills as layer 6

## References

- @elvissun — source code analysis of self-improvement loop
- @garrytan — skill_manage tool and latent/deterministic framework
- @shmidt — /reasoning toggle documentation