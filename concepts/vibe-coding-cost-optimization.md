---
title: Vibe Coding Cost Optimization
created: 2026-05-13
updated: 2026-05-13
type: concept
tags: [llm, ai-coding, cost-reduction, optimization, productivity, token-economics, vibe-coding]
sources: [raw/articles/deronin-2054235707791778034.md]
---

# Vibe Coding Cost Optimization

## Definition

Strategies and techniques for reducing AI coding costs by 60-80% without losing shipping speed or code quality. Focused on "vibe coders" — developers who use AI coding tools (Claude Code, Cursor, Aider, Windsurf) as their primary development environment.

## Core Insight

The actual fix for high AI coding bills is upstream: stop sending tokens you didn't need to send. Model selection is downstream of context discipline.

Most token waste comes from:
- Re-sending the same unchanged context on every turn
- Running premium models on trivial tasks
- Agentic tool loops that re-send full context on each call
- Including files "just in case" the model needs them

## Five Token Traps

### Trap 1: Re-Sending Entire Repo on Every Turn
Cursor and Claude Code's auto-context includes the same 30-50 files on every prompt. Those files don't change but you pay for them every turn.

Fix: Turn off auto-context for stable files. Use prompt caching. Use grep/ripgrep before asking the model. Send only the relevant function or block.

### Trap 2: Tool Call Loops That Spiral
Agent calls a tool → gets data → re-sends full context → calls another tool → re-sends. By the time the agent has the answer, you've paid for the same 50,000-token context 5 times.

Fix: Batch related tool calls. Summarise tool outputs aggressively. Replace agentic loops with deterministic helpers.

### Trap 3: Premium Models on Trivial Tasks
Using Opus to "fix a typo" or "format JSON" when Haiku would nail it for 1/30th the cost.

Fix: Set up a router. Default to Haiku for trivial tasks. Reserve Opus for the 10% of decisions that compound.

### Trap 4: Streaming When Batched Would Do
Streaming defeats prompt caching for some workflows.

Fix: Use batched responses for stable-prefix workflows. Use streaming for interactive UX.

### Trap 5: "Just in Case" Context Includes
Including utils.ts, test files, schemas "just in case" — now a "fix this bug" prompt is 80,000 tokens.

Fix: Grep first. Ask the agent to request files. Summarise old context periodically.

## Model Routing Architecture

The biggest structural change: split work across multiple models based on task type.

| Task Type | Model | Rationale |
|-----------|-------|-----------|
| Architecture, system design, security review | Opus 4.6 / GPT-5 | Decisions that compound |
| Implementation, code review, refactoring, debugging | Kimi 2.6 | Workhorse — matches Sonnet at 1/6 the cost |
| Lint, format, single-line edits | Haiku 4.5 | Trivial tasks don't need thinking |
| Autocomplete, boilerplate | Qwen 3 via Ollama | Free, local |

## Token Economics 101

Four token categories:
- **Input tokens**: Everything sent TO the model. Priced per million.
- **Output tokens**: Everything the model returns. Usually 3-5x more expensive than input.
- **Cached tokens**: Input tokens marked for reuse. ~10% of regular input cost. Most people don't use this.
- **Reasoning tokens**: Internal thinking tokens (Claude Opus). Billed even though invisible.

Pricing (mid-2026):
- Opus 4.6: ~$15/$75 per million (input/output)
- Sonnet 4.6: ~$3/$15
- Kimi 2.6: ~$0.50/$2
- Haiku 4.5: ~$1/$5

The gap between Sonnet and Kimi: 6x cheaper on input, 7.5x cheaper on output. For 95% of serious coding work, the quality gap is invisible.

## Prompt Caching

The underrated 90% cost cut. Put stable context (CLAUDE.md, system instructions, codebase summary) in the cached prefix. Structure work in 5-minute chunks (cache TTL).

Savings: 60-90% on stable input tokens.

## 30-Day Rollout

- **Week 1**: Enable prompt caching. Turn off auto-context for stable files. Start using grep before asking.
- **Week 2**: Switch default model to Kimi 2.6. Route lint/format to Haiku. Reserve Opus/GPT-5 for planning tier only.
- **Week 3**: Profile tool calls. Find top 3 most expensive loops. Fix with batching or deterministic helpers.
- **Week 4**: Write SKILL.md files for repeated workflows. Set up Ollama + Qwen 3 for autocomplete.

## Related Concepts

- [[vibe-coding]] — the broader practice of AI-first development
- [[ai-cost-optimization]] — general AI cost reduction
- [[claude-code-workflows]] — AI-assisted development patterns
- [[model-context-protocol]] — context management for AI interactions
- [[second-brain]] — personal knowledge systems
