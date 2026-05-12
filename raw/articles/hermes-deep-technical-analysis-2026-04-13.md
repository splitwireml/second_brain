---
updated: 2026-04-17
title: Hermes Deep Technical Analysis
type: article
---

# Hermes Deep Technical Analysis

**Source:** Direct codebase analysis of `~/.hermes/hermes-agent/` (v0.8.0)
**Date:** 2026-04-13
**Analyst:** Hermes Agent (self-research)

---

## Research Questions

1. How easy is it to add additional functionalities?
2. How heavy is the code?

---

## Codebase Metrics

**Total:** ~411K lines across 963 files (including tests)

**Core product code breakdown (excluding tests + bundled last30days skill):**

| Module | Files | Lines |
|---|---|---|
| `gateway/` — messaging platform adapters | 40 | 40,864 |
| `tools/` — tool implementations | 70 | 40,855 |
| `hermes_cli/` — CLI commands | 45 | 39,774 |
| `agent/` — core agent loop + AI logic | 28 | 16,152 |
| `plugins/` — memory + context engine | 17 | 9,817 |
| `environments/` — RL training | 30 | 7,307 |
| `skills/` — built-in skills | 22 | 4,995 |
| `cron/` — scheduler | 3 | 1,794 |
| `acp_adapter/` — VS Code/Zed/JetBrains | 9 | 1,784 |

**Heaviest individual files:**
- `run_agent.py` — 10,524 lines (core conversation loop)
- `cli.py` — 9,878 lines (interactive TUI)
- `gateway/run.py` — 8,911 lines (messaging gateway main loop)
- `hermes_cli/main.py` — 5,929 lines
- `gateway/platforms/feishu.py` — 3,623 lines
- `hermes_cli/auth.py` — 3,257 lines
- `gateway/platforms/discord.py` — 2,957 lines

---

## Architecture Overview

```
tools/registry.py  (no deps — imported by all tool files)
       ↑
tools/*.py  (each calls registry.register() at import time)
       ↑
model_tools.py  (imports tools/registry + all tool modules)
       ↑
run_agent.py, cli.py, batch_runner.py, environments/
```

### Entry Points (3)
- `hermes` CLI → `hermes_cli.main:main`
- `hermes-agent` → `run_agent:main`
- `hermes-acp` → `acp_adapter.entry:main`

### AIAgent (`run_agent.py`)
The core loop is entirely synchronous:
```python
while api_call_count < self.max_iterations and self.iteration_budget.remaining > 0:
    response = client.chat.completions.create(model=model, messages=messages, tools=tool_schemas)
    if response.tool_calls:
        for tool_call in response.tool_calls:
            result = handle_function_call(tool_call.name, tool_call.args, task_id)
            messages.append(tool_result_message(result))
        api_call_count += 1
    else:
        return response.content
```

Messages follow OpenAI format. Reasoning content stored in `assistant_msg["reasoning"]`.

### Tool Registry (`tools/registry.py`)
Singleton registry. Key methods:
- `register()` — called at module level by each tool
- `dispatch()` — executes handler by name, auto-bridges async
- `get_definitions()` — returns OpenAI-format schemas with availability checking
- `deregister()` — for MCP dynamic tool discovery

Error helpers: `tool_error()` and `tool_result()` reduce boilerplate across all tool handlers.

### Toolset System (`toolsets.py`)
Tools grouped into named sets (`web`, `terminal`, `file`, `skills`, etc.). Toolsets can include other toolsets (diamond dependency-safe, cycle-safe). Key function: `resolve_toolset()` recursively resolves all tools. Composite toolset `hermes-gateway` unions all 16 messaging platforms.

### Platform Toolsets
13 messaging platform adapters each have their own toolset (`hermes-telegram`, `hermes-discord`, etc.). All share `_HERMES_CORE_TOOLS` list defined once.

---

## Extension Points

### 1. Tools (Easiest)
Every tool is a standalone Python file calling `registry.register()` at module level:

```python
# From any tool file — no other config needed
registry.register(
    name="my_tool",
    toolset="my_category",
    schema={"description": "...", "parameters": {...}},
    handler=my_handler_function,
    check_fn=lambda: bool(os.environ.get("MY_API_KEY")),
    requires_env=["MY_API_KEY"],
)
```

Auto-discovery: import chain triggers all `tools/*.py` files, each registers itself. No central config. Tools can be async (registry auto-bridges).

**Key files for reference:**
- `tools/registry.py` — the registration API
- `tools/delegate_tool.py` — subagent spawning (1,103 lines, good complex example)
- `tools/skill_manager_tool.py` — skill lifecycle management

### 2. Skills (No-code)
Skills are YAML-frontmatter Markdown files in `~/.hermes/skills/<category>/`. Loaded by `skills_tool`. Structure:
```
SKILL.md          — skill definition (trigger, description, instructions)
scripts/          — optional Python scripts
references/       — documentation, API refs, templates
```

Skill metadata in frontmatter:
```yaml
---
name: skill-name
description: What it does
argument-hint: how to invoke
allowed-tools: Bash, Read, Write
---
```

Built-in skills directory: `hermes-agent/skills/` (22 files, 4,995 lines).
User skills directory: `~/.hermes/skills/` (25+ categories).

### 3. Memory Providers (Plugin Architecture)
`plugins/memory/` has 7 providers: `honcho`, `mem0`, `byterover`, `holographic`, `openviking`, `retaindb`, `hindsight`.

Each is a directory with `__init__.py` implementing `MemoryProvider` ABC. Pattern:
- `register(ctx)` function that calls `ctx.register_memory_provider(ProviderInstance)`
- OR top-level class extending `MemoryProvider`

Discovery at startup via `discover_memory_providers()` → reads `plugin.yaml` for metadata → loads active provider from `config.yaml.memory.provider`.

### 4. Context Engines (Plugin Architecture)
Same pattern as memory providers. Directory: `plugins/context_engine/<name>/`. Default: built-in "compressor". Swap via `context.engine` in config.yaml.

### 5. Slash Commands
Central `COMMAND_REGISTRY` in `hermes_cli/commands.py` — list of `CommandDef` objects. All downstream consumers auto-derive (CLI, gateway, Telegram bot menu, Slack subcommands, autocomplete).

Adding a command:
1. Add `CommandDef` to `COMMAND_REGISTRY`
2. Add handler in `HermesCLI.process_command()` in `cli.py`
3. Add handler in `gateway/run.py` for gateway availability
4. For platform-specific: add in that platform's adapter file

### 6. Messaging Platforms (Heaviest)
13 platform adapters in `gateway/platforms/`. Each extends `gateway/platforms/base.py`. Telegram: ~2,780 lines, Discord: ~2,957 lines. Adding a new platform means modeling off one of these.

---

## Dependencies

**Core (no extras):**
- `openai>=2.21.0,<3`
- `anthropic>=0.39.0,<1`
- `python-dotenv>=1.2.1,<2`
- `fire>=0.7.1,<1`
- `httpx[socks]>=0.28.1,<1`
- `rich>=14.3.3,<15`
- `tenacity>=9.1.4,<10`
- `pyyaml>=6.0.2,<7`
- `requests>=2.33.0,<3`
- `jinja2>=3.1.5,<4`
- `pydantic>=2.12.5,<3`
- `prompt_toolkit>=3.0.52,<4`

**Optional extras (27 groups):** modal, daytona, messaging (13 platforms), cron, cli, dev, tts-premium, slack, pty, honcho, mcp, homeassistant, sms, acp, voice, dingtalk, feishu, rl, yc-bench, all.

---

## Key Implementation Details

### Agent Loop
- Synchronous main loop in `run_agent.py`
- Async support via `_run_async()` bridge for individual tool handlers
- Tool call dispatch via `model_tools.handle_function_call()`
- Context compression via `agent/context_compressor.py`
- Prompt caching via `agent/prompt_caching.py`

### Tool Approval System
`tools/approval.py` — dangerous command detection. Blocks risky shell commands from messaging platforms unless approved. Check functions gate tool availability.

### Terminal Backend
`tools/terminal_tool.py` + `tools/environments/` — 6 execution backends: local, Docker, SSH, Daytona, Modal, Singularity. Config per-task via `register_task_env_overrides()`.

### MCP Integration
`tools/mcp_tool.py` — ~2,195 lines. Connects to any MCP server. Dynamic tool discovery, OAuth, SSE transport. Tools deregistered/re-registered on `notifications/tools/list_changed`.

### Cron Scheduler
`cron/jobs.py` + `cron/scheduler.py` — natural language scheduling, platform delivery. Jobs run in fresh session, skills can be attached.

---

## Observations

### What Makes It Heavy
1. **13 messaging platform adapters** — each has platform-specific API quirks
2. **6 terminal execution backends** — same functionality replicated per-backend
3. **Full MCP client** at ~2,200 lines
4. **CLI TUI** at ~10K lines combining prompt_toolkit, Rich, autocomplete, skin engine
5. **Comprehensive test suite** at ~176K lines

### What Makes It Extensible
1. **Registry pattern** — tools self-register, zero central config
2. **ABC-based plugins** — memory providers and context engines are drop-in directories
3. **Toolset composition** — diamond-safe recursive resolution
4. **Centralized command registry** — single source of truth for slash commands
5. **Skills as files** — no code required for procedural memory

### Trade-off
The codebase is production-grade heavy. A new tool takes minutes (one file, one register call). A new messaging platform takes weeks (model off existing adapter). The core agent loop is not designed to be modified — it has clear interfaces for everything extension-related.