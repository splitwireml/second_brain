---
title: Hermes Tool and Plugin Architecture
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [agent, framework, tools]
sources: [raw/articles/hermes-deep-technical-analysis-2026-04-13.md]
related_entity: [[hermes-agent]]
---

# Hermes Tool and Plugin Architecture

How Hermes organizes, discovers, and dispatches capabilities. Four independent extension layers, from trivial to substantial.

## Overview

Hermes has four extension layers that are completely independent of each other:

1. **Tools** — Python files with `registry.register()` call. Zero config, self-discovering.
2. **Skills** — Markdown files with YAML frontmatter. No code required.
3. **Memory Providers** — Plugin directories implementing `MemoryProvider` ABC.
4. **Context Engines** — Plugin directories implementing `ContextEngine` ABC.

## Tool Registry (`tools/registry.py`)

The central registry. Every tool file calls `registry.register()` at module level. That's the entire API for 40+ built-in tools.

```python
registry.register(
    name="my_tool",
    toolset="my_category",
    schema={
        "description": "...",
        "parameters": {
            "type": "object",
            "properties": {...},
            "required": [...]
        }
    },
    handler=my_handler_function,       # sync or async
    check_fn=lambda: bool(os.getenv("MY_API_KEY")),  # availability check
    requires_env=["MY_API_KEY"],        # for toolset metadata
    is_async=False,                     # auto-bridged if True
    emoji="🔧",
)
```

The registry handles:
- **Dispatch** — maps tool name to handler, auto-bridges async
- **Schema retrieval** — returns OpenAI-format schemas with availability filtering
- **Toolset queries** — groups tools by toolset, checks toolset availability
- **Deregistration** — for MCP dynamic tool discovery

Key methods: `register()`, `dispatch()`, `get_definitions()`, `get_all_tool_names()`, `get_toolset_for_tool()`, `is_toolset_available()`, `check_toolset_requirements()`.

## Toolset System (`toolsets.py`)

Tools grouped into named sets. Toolsets can include other toolsets (diamond-safe, cycle-safe):

```python
TOOLSETS = {
    "web": {"tools": ["web_search", "web_extract"], "includes": []},
    "debugging": {"tools": ["terminal", "process"], "includes": ["web", "file"]},
    "safe": {"tools": [], "includes": ["web", "vision", "image_gen"]},
}
```

`resolve_toolset("safe")` recursively expands to all tools from `web + vision + image_gen`. Cycles return empty silently. `resolve_multiple_toolsets()` combines.

Composite `hermes-gateway` includes all 13 messaging platform toolsets.

## Skills System

Skills live in `~/.hermes/skills/<category>/SKILL.md` with YAML frontmatter:

```yaml
---
name: my-skill
description: What it does
argument-hint: topic to research
allowed-tools: Bash, Read, Write
---
# My Skill

Instructions for the agent...
```

Skill invocation: `/skill-name` or `/skills` hub. Skills can include scripts (`scripts/`), references (`references/`), and templates.

Built-in skills: 22 files across agent/AI research, productivity, media, mlops, social-media, etc.

## Memory Provider Plugins (`plugins/memory/`)

7 providers in plugin directories: `honcho`, `mem0`, `byterover`, `holographic`, `openviking`, `retaindb`, `hindsight`.

Each directory has `__init__.py` with either:
- `register(ctx)` function → calls `ctx.register_memory_provider(instance)`
- OR top-level class extending `MemoryProvider` ABC

Discovery scans directories, reads `plugin.yaml` for metadata, loads active provider from `config.yaml.memory.provider`.

## Context Engine Plugins (`plugins/context_engine/`)

Same plugin pattern as memory providers. Default engine is built-in compressor. Swap via `context.engine` in config.yaml.

## Slash Command Registry

`hermes_cli/commands.py` has `COMMAND_REGISTRY` — list of `CommandDef` objects. All downstream consumers auto-derive:
- CLI: `process_command()` resolves aliases
- Gateway: `GATEWAY_KNOWN_COMMANDS` frozenset for hook emission
- Telegram: `telegram_bot_commands()` for BotCommand menu
- Slack: `slack_subcommand_map()` for `/hermes` routing
- Autocomplete: fed to `SlashCommandCompleter`

Adding a command: 1 CommandDef entry + handler in `cli.py` + handler in `gateway/run.py`.

## Related Concepts

- [[a2a-protocol-cross-agent-communication]] — Google A2A protocol, complementary to Hermes's tool dispatch
- [[gsd-2-ai-vibe-coding-framework]] — standalone framework with bundled extensions, comparable extensibility pattern
- [[paperclipai-paperclip]] — uses Hermes via plugin adapter
- [[hermes-agent]] — the entity page for this agent platform
