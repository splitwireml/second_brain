---
title: GSD-2 AI Vibe Coding Framework
created: 2026-04-06
updated: 2026-04-06
type: concept
tags: [agent, framework]
sources: [raw/articles/x-bookmarks-2026.md]
---

# GSD-2 — AI Vibe Coding Framework


---

## Overview

GSD-2 ("Get Shit Done 2") is an open-source AI coding agent framework built on the Pi SDK (by Mario Zechner). It evolved from a collection of markdown prompt templates for Claude Code (GSD-1) into a standalone CLI (~4,400 GitHub stars, 80+ contributors, 95 releases). This report covers its architecture, how it differs from v1, its multi-provider design, bring-your-own-agent capabilities, and parallel execution.

**Repo:** github.com/gsd-build/gsd-2
**License:** MIT
**Primary language:** TypeScript
**Install:** `npm install -g gsd-pi@latest`

---

## Research Questions

1. How does GSD-2's architecture differ from GSD-1 (prompt-framework approach)?
2. How does the Pi SDK integration work architecturally?
3. Can you bring your own Claude Code, Codex, and OpenCode with their MCPs/skills?
4. Does it support parallel execution, and can you configure which agents run in parallel?

---

## Answers / Findings

### Q1: Architecture vs GSD-1

GSD-1 was a **markdown prompt framework** — a set of `.md` files installed into `~/.claude/commands/`. It relied entirely on the LLM reading the prompts and following instructions. There was no programmatic control over the agent.

**GSD-2 is a TypeScript application** that embeds the Pi coding agent SDK directly. It has real control over the agent harness:

| Aspect | GSD-1 | GSD-2 |
|--------|-------|-------|
| Runtime | Claude Code slash commands | Standalone CLI via Pi SDK |
| Context control | None — LLM accumulated garbage | Fresh session per unit, injects only needed files |
| Automation | LLM calling itself in a loop | State machine, disk-based state, crash recovery |
| Observability | None | Cost tracking, progress dashboard, stuck detection |
| Parallel execution | None | Multi-worker milestone orchestration |
| Git management | None | Worktree isolation, milestone branches, auto-commit |
| Crash recovery | None | Lock-file detection, resume from disk state |
| Extensibility | Prompt injection | Full TypeScript extension API |

**Key architectural shift:** GSD-2 reads/writes state to `.gsd/` on disk between every unit of work. The LLM never accumulates garbage because every dispatch starts a fresh session. State (`STATE.md`, `roadmap`, `plans/`) lives on disk as the sole source of truth — no in-memory state survives across sessions.

### Q2: Pi SDK Integration

Pi (github.com/badlogic/pi-mono, package `@mariozechner/pi-coding-agent`) is the agent harness layer that GSD builds on top of. The relationship:

- **Pi** = terminal-native coding agent runtime. Handles the agent loop (LLM calls, tool execution, session management, branching, compaction).
- **GSD** = workflow engine + extensions layered on top of Pi. Adds auto mode, state machine, milestone tracking, git management, and 23 bundled extensions.

```
gsd (CLI binary)
  └─ loader.ts          Sets PI_PACKAGE_DIR, GSD env vars, dynamic-imports cli.ts
      └─ cli.ts         Wires SDK managers, loads extensions, starts InteractiveMode
          ├─ onboarding.ts   First-run setup wizard
          ├─ wizard.ts       Env hydration from stored auth.json
          ├─ app-paths.ts    ~/.gsd/agent/, ~/.gsd/sessions/, auth.json
          └─ src/resources/
              ├─ extensions/gsd/    Core GSD extension
              ├─ extensions/...     23 supporting extensions
              ├─ agents/            scout, researcher, worker
              └─ AGENTS.md          Agent routing instructions
```

**Two-file loader pattern:** `loader.ts` sets `PI_PACKAGE_DIR` and GSD env vars with zero SDK imports, then dynamically imports `cli.ts` which does the actual SDK imports. This ensures `PI_PACKAGE_DIR` is set before any SDK code evaluates — avoids Pi's theme resolution colliding with GSD's `src/` directory.

**Lazy provider loading:** LLM provider SDKs (Anthropic, OpenAI, Google, etc.) are lazy-loaded on first use, not at startup. Significantly reduces cold-start time.

**Fresh session per unit:** Every dispatch creates a new Pi agent session. The LLM starts with a clean context window containing only the pre-inlined artifacts it needs. Prevents quality degradation from context accumulation.

**Native Rust engine:** Performance-critical ops (grep, glob, ps, highlight, ast, diff, git read via libgit2, clipboard, etc.) are implemented as Rust N-API modules for ~10x speedups over JavaScript equivalents.

### Q3: Bring Your Own Agents (Claude Code, Codex, OpenCode + MCPs + Skills)

#### MCP Servers

GSD has **native MCP client integration** via the `@modelcontextprotocol/sdk`. It reads MCP config from:

- `.mcp.json` (project root — commit to git)
- `.gsd/mcp.json` (project-local — not committed)

Both locations are checked and merged. Supports `stdio` and `http` transports. GSD's bundled `.mcp.json` includes a `repowise` MCP server for codebase intelligence.

```
~/.claude.json or ~/.claude/mcp.json         (user-level MCP — Claude Code)
.claude/.mcp.json or .claude/mcp.json         (project-level MCP — Claude Code)
.mcp.json                                     (project-level MCP — standard)
```

#### Universal Config Discovery (`universal-config` extension)

GSD ships with a **Universal Config Discovery** extension that scans for existing AI tool configurations across 8 tools:

| Tool | MCP Servers | Context Files | Rules | Skills | Plugins | Settings |
|------|-------------|---------------|-------|--------|---------|---------|
| Claude Code | `.claude.json`, `~/.claude/mcp.json` | `~/.claude/CLAUDE.md`, `CLAUDE.md` | — | `~/.claude/skills/**/SKILL.md` | `~/.claude/plugins/**/package.json` | `~/.claude/settings.json` |
| Cursor | `.cursor/mcp.json` | — | `.cursor/rules/*.mdc`, `.cursorrules` | — | — | `.cursor/settings.json` |
| Windsurf | `.windsurf/mcp_config.json`, `~/.codeium/windsurf/mcp_config.json` | — | `.windsurf/rules/*.md`, `.windsurfrules` | — | — | — |
| Gemini CLI | `~/.gemini/settings.json`, `.gemini/settings.json` | `~/.gemini/GEMINI.md`, `.gemini/GEMINI.md` | — | — | — | — |
| OpenAI Codex | TOML not yet parsed | `~/.codex/AGENTS.md`, `AGENTS.md` | — | — | — | — |
| Cline | `.clinerules` | — | — | — | — | — |
| GitHub Copilot | `.github` | — | — | — | — | — |
| VS Code | `.vscode` | — | — | — | — | — |

**Important:** Universal Config Discovery is **read-only** discovery — it finds these configs but does not automatically import or activate them inside GSD. It surfaces what's configured in competing tools. The discovered items can be used to inform GSD's context injection, but this is passive detection.

#### Claude Code CLI Integration

GSD has a **first-class `claude-code` provider extension** that delegates inference to a locally-installed Claude Code CLI via `@anthropic-ai/claude-agent-sdk`. This is **ToS-compliant** — it uses Anthropic's official SDK, never touches credentials directly.

```
pi.registerProvider("claude-code", {
  authMode: "externalCli",
  api: "anthropic-messages",
  baseUrl: "local://claude-code",
  isReady: isClaudeCodeReady,
  streamSimple: streamViaClaudeCode,
  models: CLAUDE_CODE_MODELS,
});
```

Users with a Claude Code subscription (Pro/Max/Team) get subsidized inference through GSD's UI — no separate API key needed. This is different from the universal-config discovery feature — this is an actual model provider that pipes GSD's requests through Claude Code's CLI.

#### Skills

GSD skills follow the open **Agent Skills standard** (agentsskills.io) and are **not GSD-specific** — they work with Claude Code, OpenAI Codex, Cursor, GitHub Copilot, Windsurf, and 40+ other agents. Skill directories:

| Location | Scope |
|----------|-------|
| `~/.agents/skills/` | Global — shared across all projects and compatible agents |
| `.agents/skills/` (project root) | Project-local — commit to version control |

Global skills take precedence over project skills on name collisions. Skills are installed via `npx skills add <repo>` (skills.sh CLI). During `gsd init`, GSD detects the tech stack and recommends relevant skill packs (SwiftUI, React, Rust, Python, Go, etc.).

**Migrated from v1:** On first launch after upgrading, GSD auto-copies skills from legacy `~/.gsd/agent/skills/` to `~/.agents/skills/`.

#### Summary on Bringing Your Own Setup

| Component | Bring Your Own? | How |
|-----------|----------------|-----|
| Claude Code MCP servers | Partial | Discoverable via universal-config, but not auto-imported into GSD's runtime |
| Claude Code skills | No | Skills follow agentskills.io standard — compatible format, but GSD uses its own skill discovery |
| Claude Code CLI | Yes (as model provider) | Via `claude-code` provider — uses your Claude Code subscription |
| Codex | Partial | Context files (`~/.codex/AGENTS.md`) discoverable; TOML MCP config not yet parsed |
| OpenCode | Partial | Context files discoverable; not a registered model provider |
| MCP servers (general) | Yes | Via `.mcp.json` / `.gsd/mcp.json` native MCP client |
| Custom skills | Yes | Place in `~/.agents/skills/` or `.agents/skills/` |

**Gap for your setup:** GSD does not currently act as a **hub** that picks up and runs your existing Claude Code CLI sessions, Codex sessions, or OpenCode sessions as sub-agents. It can use Claude Code's CLI as a model provider (inference side), but it does not import or replay your existing MCP tool configurations or session contexts from those tools into GSD's runtime. The universal-config extension discovers these configs, but that's passive — no active import.

### Q4: Parallel Execution

**Yes, GSD-2 has parallel execution** — called "Parallel Milestone Orchestration." It's behind a feature flag (`parallel.enabled: false` by default).

#### Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Coordinator (your GSD session)                         │
│  Responsibilities:                                       │
│  - Eligibility analysis (deps + file overlap)            │
│  - Worker spawning and lifecycle                          │
│  - Budget tracking across all workers                    │
│  - Signal dispatch (pause/resume/stop)                   │
│  - Merge reconciliation                                  │
│                                                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Worker 1 │  │ Worker 2 │  │ Worker 3 │  ...          │
│  │ M001     │  │ M003     │  │ M005     │              │
│  └──────────┘  └──────────┘  └──────────┘              │
│       │              │              │                   │
│       ▼              ▼              ▼                   │
│  .gsd/worktrees/ .gsd/worktrees/ .gsd/worktrees/         │
│  M001/           M003/           M005/                   │
└─────────────────────────────────────────────────────────┘
```

#### Worker Isolation

Each worker is a separate `gsd` process with full isolation:

| Resource | Isolation Method |
|----------|-----------------|
| Filesystem | Git worktree — each worker has its own checkout |
| Git branch | `milestone/<MID>` — one branch per milestone |
| State derivation | `GSD_MILESTONE_LOCK` env var — `deriveState()` only sees the assigned milestone |
| Context window | Separate process — each worker has its own agent sessions |
| Metrics | Each worktree has its own `.gsd/metrics.json` |
| Crash recovery | Each worktree has its own `.gsd/auto.lock` |

**Coordinator ↔ Worker IPC:** File-based via `.gsd/parallel/<MID>.status.json` (worker heartbeats) and `.gsd/parallel/<MID>.signal.json` (coordinator signals). Atomic writes (write-to-temp + rename) prevent partial reads.

#### Configuration

```yaml
# In ~/.gsd/PREFERENCES.md or .gsd/PREFERENCES.md
parallel:
  enabled: true           # Master toggle (default: false)
  max_workers: 2         # Concurrent workers: 1-4 (default: 2)
  budget_ceiling: 50.00   # Aggregate cost limit in USD (optional)
  merge_strategy: "per-milestone"  # "per-slice" or "per-milestone"
  auto_merge: "confirm"  # "auto", "confirm", or "manual"
```

#### Commands

| Command | Description |
|---------|-------------|
| `/gsd parallel start` | Analyze eligibility, confirm, start workers |
| `/gsd parallel status` | Show all workers with state, units completed, cost |
| `/gsd parallel stop` | Stop all workers (SIGTERM) |
| `/gsd parallel stop M002` | Stop specific milestone's worker |
| `/gsd parallel pause` | Pause all workers (finish current unit, then wait) |
| `/gsd parallel pause M002` | Pause specific worker |
| `/gsd parallel resume` | Resume all paused workers |
| `/gsd parallel merge` | Merge all completed milestones back to main |
| `/gsd parallel merge M002` | Merge specific milestone back to main |

#### Eligibility Analysis

Before spawning workers, GSD checks:

1. **Not complete** — Finished milestones are skipped
2. **Dependencies satisfied** — All `dependsOn` entries must have status `complete`
3. **File overlap check** — Milestones touching the same files get a warning (but are still eligible)

File overlaps are warnings only — workers operate in separate worktrees, so no filesystem interference. Conflicts are caught at merge time.

#### Key Constraint

**Parallelism is at the milestone level** (not slice/task level), coordinated by the GSD session acting as a coordinator process. You configure `max_workers` (1-4) and `budget_ceiling`. There's no way to say "run Claude Code on milestone A and Codex on milestone B simultaneously" — all workers run the same GSD/agent engine. You can only control **how many** workers run, not **which agent engine** each worker uses.

---

## Multi-Provider Support Architecture

GSD supports **20+ LLM providers** out of the box via the Pi SDK:

### Built-in Providers

| Provider | Auth | Env Variable |
|----------|------|-------------|
| Anthropic (Claude) | OAuth or API key | `ANTHROPIC_API_KEY` |
| OpenAI | API key | `OPENAI_API_KEY` |
| Google Gemini | API key | `GEMINI_API_KEY` |
| OpenRouter | API key | `OPENROUTER_API_KEY` |
| Groq | API key | `GROQ_API_KEY` |
| xAI (Grok) | API key | `XAI_API_KEY` |
| Mistral | API key | `MISTRAL_API_KEY` |
| GitHub Copilot | OAuth | `GH_TOKEN` |
| Amazon Bedrock | IAM credentials | `AWS_PROFILE` / `AWS_ACCESS_KEY_ID` |
| Anthropic on Vertex AI | ADC | `GOOGLE_APPLICATION_CREDENTIALS` |
| Azure OpenAI | API key | `AZURE_OPENAI_API_KEY` |

### Local Providers (via `~/.gsd/agent/models.json`)

- **Ollama** — `baseUrl: http://localhost:11434/v1`, OpenAI-compat
- **LM Studio** — `baseUrl: http://localhost:1234/v1`, OpenAI-compat
- **vLLM** — `baseUrl: http://localhost:8000/v1`, OpenAI-compat
- **SGLang** — `baseUrl: http://localhost:30000/v1`, OpenAI-compat

### Custom Provider Extensions

Community extensions (e.g., `pi-dashscope` for Alibaba DashScope via `npm install -g pi-dashscope`) can add new providers.

### Provider Routing

Per-phase model selection in `PREFERENCES.md`:

```yaml
models:
  research: claude-sonnet-4-6
  planning: claude-opus-4-6
  execution: claude-sonnet-4-6
  execution_simple: claude-haiku-4-5-20250414
  completion: claude-sonnet-4-6
  subagent: claude-sonnet-4-6
```

Dynamic model routing selects the cheapest model for a given capability tier based on cost and capability metadata. Fallback chains are supported per phase.

---

## Bundled Extensions (23 total)

| Extension | Purpose |
|-----------|---------|
| GSD | Core workflow engine — auto mode, state machine, commands, dashboard |
| Browser Tools | Playwright — navigation, forms, screenshots, PDF, device emulation, visual regression |
| Search the Web | Brave Search, Tavily, Jina page extraction |
| Google Search | Gemini-powered web search with AI-synthesized answers |
| Context7 | Up-to-date library/framework documentation |
| Background Shell | Long-running process management with readiness detection |
| Subagent | Delegated tasks with isolated context windows |
| Mac Tools | macOS native app automation via Accessibility APIs |
| **MCP Client** | Native MCP server integration via @modelcontextprotocol/sdk |
| Voice | Real-time speech-to-text (macOS, Linux) |
| Slash Commands | Custom command creation |
| LSP | Diagnostics, definitions, references, hover, rename |
| Ask User Questions | Structured user input with single/multi-select |
| Secure Env Collect | Masked secret collection |
| Async Jobs | `async_bash`, `await_job`, `cancel_job` |
| Remote Questions | Route decisions to Discord, Slack, Telegram |
| TTSR | Tool-triggered system rules — conditional context injection |
| **Universal Config** | Discovery of Claude Code, Cursor, Windsurf, Codex, etc. configs |
| AWS Auth | AWS credential management |
| **Claude Code CLI** | Claude Code CLI as a model provider |
| cmux | Context multiplexing for multi-session coordination |
| GitHub Sync | GitHub issue and PR synchronization |
| Ollama | Local Ollama model integration |
| Shared | Shared utilities across extensions |

---

## Dispatch Pipeline (Auto Mode)

```
1. Read disk state (STATE.md, roadmap, plans)
2. Determine next unit type and ID
3. Classify complexity → select model tier
4. Apply budget pressure adjustments
5. Check routing history for adaptive adjustments
6. Dynamic model routing → select cheapest model for tier
7. Resolve effective model (with fallbacks)
8. Check pending captures → triage if needed
9. Build dispatch prompt (applying inline level compression)
10. Create fresh agent session
11. Inject prompt and let LLM execute
12. On completion: snapshot metrics, verify artifacts, persist state
13. Loop to step 1
```

---

## Source Exploration

Examined files in `~/Documents/Research/gsd-2/sources/gsd-2/`:

- `docs/architecture.md` — Full system structure, dispatch pipeline, key modules
- `docs/parallel-orchestration.md` — 309-line deep-dive on worker isolation, IPC, eligibility, merge
- `docs/configuration.md` — Preferences, MCP config, env vars, git settings
- `docs/skills.md` — Agent Skills standard, skill lifecycle, health dashboard
- `docs/custom-models.md` — models.json schema, provider config, compat flags
- `docs/providers.md` — Step-by-step setup for all 12+ providers
- `docs/migration.md` — `.planning` → `.gsd` migration tool
- `src/resources/extensions/universal-config/discovery.ts` — Parallel config discovery orchestrator
- `src/resources/extensions/universal-config/scanners.ts` — Per-tool config file scanners
- `src/resources/extensions/universal-config/tools.ts` — 8 supported AI coding tools registry
- `src/resources/extensions/claude-code-cli/index.ts` — Claude Code CLI as model provider
- `.mcp.json` — Bundled MCP server config (repowise)
- `VISION.md` — Design principles, architectural constraints, what they won't accept
- `what-is-pi/01-what-pi-is.md` — Pi SDK overview

---

## Key Design Decisions Worth Noting

1. **Extension-first** — Core stays lean; new capabilities go into extensions unless they require core integration
2. **Simplicity over abstraction** — "Three similar lines of code is better than a premature abstraction"
3. **Tests are the contract** — Behavior changes must be accompanied by tests
4. **State on disk** — `.gsd/` is the sole source of truth; no in-memory state survives sessions
5. **Provider-agnostic** — No architectural decisions should privilege one provider over another
6. **GSD won't accept** — Enterprise patterns (DI containers, abstract factories), framework rewrites without clear measurable benefit, heavy orchestration layers duplicating what agent infrastructure already provides

---

## Limitations / Open Questions

1. **OpenCode/Codex as sub-agents:** GSD cannot run OpenCode or Codex as worker agents in its parallel milestone system. They are detectable via universal-config but not executable within GSD's runtime.
2. **Claude Code MCP auto-import:** Universal-config discovers Claude Code MCP servers but doesn't actively import them into GSD's MCP runtime — discovery is passive.
3. **Skills are GSD-native:** While skills follow the agentskills.io standard (theoretically compatible), GSD doesn't pick up your existing Claude Code skill files unless they're placed in `~/.agents/skills/`.
4. **OAuth ToS concern (Reddit discussion):** Community members flagged that using Claude Code OAuth tokens outside Claude's own tools may violate Anthropic's ToS. GSD's `claude-code` provider uses the official `@anthropic-ai/claude-agent-sdk` which is explicitly noted as ToS-compliant, but users with Claude Max subscriptions should verify.
5. **TOML MCP parsing not yet implemented** for Codex — TOML config files are detected and warned about but not parsed.
6. **Nested parallel sessions are blocked** — `GSD_PARALLEL_WORKER` env var prevents workers from spawning their own parallel sessions.

---

## See Also

- [[gsd-2-vs-blueprint]] — Comparison of GSD-2 vs Blueprint
- [[1-bit-bonsai-bitnet-fine-tuning]] — 1-bit LLMs enabling consumer-RTX fine-tuning of vibe coding models
- [[leann-vector-database]] — vector DB context for code search and semantic indexing in vibe coding workflows

## Next Steps / Follow-Up Research

- [ ] Test GSD's MCP client with one of Ali's existing MCP servers (e.g., from `.mcp.json`)
- [ ] Investigate whether GSD's `subagent` extension could wrap Codex/OpenCode as delegated tasks
- [ ] Explore `gsd install npm:pi-dashscope` for DashScope/Qwen model support
- [ ] Check if the `models.json` provider override approach could route GSD through Ali's existing Claude Code OAuth session
- [ ] Try `/gsd prefs import-claude` — the docs mention importing Claude marketplace plugins and skills as namespaced GSD components
- [ ] Compare GSD-2's parallel milestone approach vs. Claude Code's own multi-agent capabilities
