---
title: Model Shortcuts
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [orchestration, llm, agent, oss-ai]
sources: []
related_entity: [[hermes-agent]]
---

## Definition

Model shortcuts are user-defined named aliases for `provider/model` pairs — e.g. `claude-planner` resolves to `anthropic/opus-4.6`. They decouple *intent* (what a model should *do*) from *implementation* (which provider and model name backs it).

## The Problem They Solve

In multi-agent workflows, delegation calls, and cron job configurations, specifying models requires hardcoding the full provider+model string:

```yaml
# Every call must know the exact provider and model
delegate_task:
  goal: "Plan the feature"
  model: "anthropic/claude-opus-4.6"   # brittle — renaming breaks every call site
```

This creates three problems:

1. **Refactoring fragility** — swapping `opus-4.6` for `opus-4.7` requires updating every call site
2. **Intent obscurity** — `anthropic/claude-opus-4.6` tells you what the model *is*, not what it's *for*
3. **Orchestrator coupling** — a parent agent orchestrating sub-agents must know the provider landscape, not just the intent tier

## Proposed Design

Shortcuts are defined in `config.yaml` as a top-level `model_aliases:` block:

```yaml
model_aliases:
  claude-planner: anthropic/claude-opus-4.6
  claude-coder: anthropic/claude-sonnet-4-20250514
  gpt-coder-xhigh: openai/gpt-5.4-xhigh
  gpt-coder-fast: openai/gpt-4o
  deepthink: anthropic/claude-opus-4
```

Resolution is **lazy** — the alias maps to a `provider/model` string that is resolved at runtime against whatever providers are currently configured.

### Namespace and Collision Avoidance

To avoid ambiguity with real model identifiers, aliases use a **separate namespace** from provider and model names. Two rules prevent collisions:

1. Aliases **must contain a hyphen** (`claude-planner`, not `claudeplanner`) — any bare identifier without a hyphen is treated as a literal model name
2. Aliases **must be explicitly declared** in `model_aliases:` — no implicit aliases

If a collision is possible (e.g. a provider adds a model literally named `claude-planner`), the alias takes precedence in contexts that explicitly call for an alias, and the literal model takes precedence in contexts that explicitly call for a model name.

## Composition with Existing Features

### Provider Presets (PR #2097)

Provider presets name *endpoints + auth* (e.g. `anthropic`, `openrouter`). Model shortcuts name *provider+model pairs*. They compose cleanly:

```yaml
providers:
  anthropic:          # provider preset from PR #2097
    type: anthropic
    model: claude-opus-4-20250514
    api_key: ${ANTHROPIC_API_KEY}

model_aliases:
  claude-planner: anthropic/claude-opus-4.6   # resolves via the named provider
```

The shortcut resolves through whatever model the provider preset currently points to. Swapping the underlying model in the provider preset automatically propagates to all shortcuts.

### delegate_task Per-Task Overrides (PR #1138)

[PR #1138](https://github.com/NousResearch/hermes-agent/pull/1138) added `model:`, `provider:`, and `backend:` overrides to `delegate_task`. Model shortcuts extend this cleanly:

```yaml
delegate_task:
  goal: "Architect the new service"
  model: "claude-planner"    # resolved at spawn time → anthropic/claude-opus-4.6
```

The orchestrator no longer needs to know that `claude-planner` means `anthropic/opus-4.6` — it just names the capability tier.

### Cron Jobs

Cron job prompts can reference shortcuts directly, making job definitions stable across model upgrades:

```yaml
hermes cron create \
  --name "daily-planning" \
  --model "claude-planner" \
  --prompt "Review outstanding PRs and draft a sprint plan"
```

### Skill Configuration

Skills that accept a model parameter can accept shortcuts:

```yaml
# In a skill's required_inputs or config
model: "${delegate_model|claude-coder}"   # fallback to named shortcut
```

## Resolution Pipeline

When a model string is encountered:

1. **Is it an alias?** → look up in `model_aliases:`, return resolved `provider/model` if found
2. **Is it a bare `provider/model` string?** → use as-is
3. **Is it a single provider name (no `/`)?** → resolve via `providers:` presets, fall back to provider default model
4. **Otherwise** → treat as literal model name against the default provider

This means existing `provider/model` strings continue to work unchanged — aliases are an additive feature that doesn't break backward compatibility.

## Open Design Questions

- **Default alias source** — should aliases be resolved from `model_aliases:` in `config.yaml` only, or should skills and other config sources be able to define their own alias namespaces?
- **Alias locking** — should an alias pin to a specific model version (e.g. `claude-opus-4.6`), or resolve dynamically to whatever the provider preset currently defaults to? The dynamic option is more flexible; the pinned option is more predictable.
- **Display and discovery** — `/model` listing should show aliases alongside provider presets so users can see what shortcut names are available.

## Related Concepts

- [[hermes-agent]] — the agent framework this would be implemented in; PR #2097 (provider presets), PR #1138 (per-task delegate overrides), and PR #1168 (model routing profiles) are all precedents
- [[paperclip-orchestrator]] — an orchestrator that manages multiple agents; named shortcuts would make its delegation calls more intent-based
- [[hermes-tool-plugin-architecture]] — extension layers in Hermes; the alias resolution logic would slot into the model resolution layer
- [[prompt-engineering-patterns]] — prompt patterns where model tier selection matters; shortcuts make tier selection configurable rather than hardcoded in prompts
