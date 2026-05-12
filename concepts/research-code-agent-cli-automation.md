---
title: Code Agent CLI Automation — Prompting, Model Switching & Sessions
created: 2026-04-02
updated: 2026-04-02
type: concept
tags: [agent, platform]
sources: [raw/articles/x-bookmarks-2026.md]
---

     1|# Research: Code Agent CLI Automation — Prompting, Model Switching & Sessions
     2|
     3|**Date:** 2026-04-02
     4|**Focus:** How much work can be done entirely through the CLI of Claude Code, Codex, and OpenCode
     5|
     6|---
     7|
     8|## Agent CLI Interfaces
     9|
    10|### Claude Code
    11|| Entry Point | Command | Notes |
    12||---|---|---|
    13|| Interactive | `claude` | Default TUI mode |
    14|| Non-interactive | `claude --print [prompt]` | Returns text to stdout |
    15|| Config | `~/.claude.json` + `~/.claude/settings.json` | YAML + JSON |
    16|| Sessions | SQLite in `~/.claude/` (SessionDB) | FTS5 search |
    17|| MCP config | `claude mcp add/remove/list` | User + project-level |
    18|
    19|### Codex
    20|| Entry Point | Command | Notes |
    21||---|---|---|
    22|| Interactive | `codex [prompt]` | Optional prompt on cmd line |
    23|| Non-interactive | `codex exec [prompt]` | `--json` for NDJSON streaming |
    24|| Config | `~/.codex/config.toml` | TOML |
    25|| Sessions | Directory tree `~/.codex/sessions/YYYY/MM/DD/HH/` | JSONL per message |
    26|| MCP config | `~/.codex/config.toml` + `codex mcp` | TOML or CLI |
    27|
    28|### OpenCode
    29|| Entry Point | Command | Notes |
    30||---|---|---|
    31|| Interactive | `opencode [project]` | Default TUI mode |
    32|| Non-interactive | `opencode run [prompt]` | `--session`, `--continue` |
    33|| Config | `~/.config/opencode/opencode.json` | JSON |
    34|| Sessions | SQLite? Bun storage in `~/Library/Application Support/opencode/` | Listed via `opencode session list` |
    35|| MCP config | `~/.config/opencode/opencode.json` | JSON MCP server array |
    36|
    37|---
    38|
    39|## Prompting
    40|
    41|### Can you pipe prompts in?
    42|
    43|| Agent | stdin Pipe | Works? |
    44||---|---|---|
    45|| Claude Code | `echo "prompt" \| claude --print` | YES |
    46|| Codex | `echo "prompt" \| codex exec --json` | YES (NDJSON output) |
    47|| OpenCode | `echo "prompt" \| opencode run` | YES |
    48|
    49|All three support stdin piping for prompts.
    50|
    51|### Structured Output
    52|
    53|| Agent | Mechanism | Verified? |
    54||---|---|---|
    55|| Claude Code | `--json-schema '{"type":"object","properties":{"answer":{"type":"string"}}}'` + `--output-format json` | YES — works, returns `structured_output` field in JSON |
    56|| Codex | `--json` | YES — returns NDJSON with `item.completed` containing text |
    57|| OpenCode | None visible | No native structured output flag |
    58|
    59|---
    60|
    61|## Model Switching
    62|
    63|### Claude Code
    64|```bash
    65|claude --print --model sonnet "prompt"          # alias: sonnet, opus, haiku
    66|claude --print --model claude-sonnet-4-6 "prompt"  # full model name
    67|claude --print --fallback-model haiku "prompt"  # fallback on overload
    68|```
    69|- Uses `anthropic/` prefix in config (e.g. `anthropic/claude-opus-4.6`)
    70|- `--model` accepts aliases or full names
    71|- Session-level override: `--agent` for agent persona, `--effort` for thinking effort
    72|
    73|### Codex
    74|```bash
    75|codex exec -m gpt-4o "prompt"
    76|codex exec -m o3 "prompt"
    77|codex exec -m "provider/model" "prompt"           # dotted model name
    78|```
    79|- Default: `gpt-5.4` (from config)
    80|- Config-level: `-c model="o3"` or `-c model="provider/model"`
    81|- Supports `--oss` for local Ollama/LM Studio
    82|
    83|### OpenCode
    84|```bash
    85|opencode run -m opencode/gpt-5-nano "prompt"
    86|opencode run -m opencode/minimax-m2.7 "prompt"  # [[minimax-m27]] via OpenCode
    87|opencode run -m openrouter/anthropic/claude-opus-4 "prompt"
    88|```
    89|- Extensive model registry via `opencode models` (50+ models across providers)
    90|- Provider namespaces: `opencode`, `openrouter`, `alibaba-coding-plan`, etc.
    91|
    92|---
    93|
    94|## Session Management
    95|
    96|### Claude Code
    97|```bash
    98|# Create with specific UUID (persists automatically)
    99|claude --print --session-id d4d054ff-d34e-4945-b263-6c0eded8dd43 "prompt"
   100|
   101|# Resume a session
   102|claude --print --resume d4d054ff-d34e-4945-b263-6c0eded8dd43 "continue prompt"
   103|
   104|# Fork session on resume
   105|claude --print --resume d4d054ff --fork-session "prompt"
   106|
   107|# Continue most recent (interactive only)
   108|claude --continue
   109|```
   110|- Session IDs must be proper UUIDs (no named sessions via CLI)
   111|- Sessions stored in SQLite, searchable
   112|- `--no-session-persistence` for fire-and-forget
   113|- `--name` for display name in resume picker
   114|- Session IDs are NOT the same as the numeric PID stored in session JSON files
   115|
   116|### Codex
   117|```bash
   118|# Resume most recent (interactive only)
   119|codex resume --last
   120|
   121|# Resume specific session by ID
   122|codex resume SESSION_ID
   123|
   124|# Fork a session
   125|codex fork SESSION_ID
   126|```
   127|- Sessions are directory trees under `~/.codex/sessions/YYYY/MM/DD/HH/`
   128|- Session IDs appear to be in thread format (not simple UUIDs)
   129|- `codex exec` creates ephemeral non-interactive sessions by default
   130|- `codex exec --json` returns `thread_id` for tracking
   131|
   132|### OpenCode
   133|```bash
   134|# Continue most recent session
   135|opencode run -c "prompt"
   136|
   137|# Use specific session
   138|opencode run -s ses_2b1cfec67ffedejQPoa43evN06 "prompt"
   139|
   140|# Fork session on continue
   141|opencode run -c --fork "prompt"
   142|
   143|# List sessions
   144|opencode session list
   145|opencode session delete SESSION_ID
   146|```
   147|- Session IDs are `ses_` prefixed strings (shown in `session list`)
   148|- Sessions persist across `opencode run` invocations when same session ID used
   149|- Sessions stored in Application Support (Bun/native storage)
   150|
   151|---
   152|
   153|## MCP Server Integration
   154|
   155|### Adding TUIs as MCP servers
   156|
   157|All three agents support adding MCP servers, which enables TUI screenshot tools:
   158|
   159|```bash
   160|# Claude Code
   161|claude mcp add --scope user tui-mcp -- npx tui-mcp
   162|
   163|# Codex (config.toml)
   164|[mcp_servers.tui-mcp]
   165|command = "npx"
   166|args = ["-y", "tui-mcp"]
   167|
   168|# OpenCode (opencode.json)
   169|"tui-mcp": {
   170|  "command": ["npx", "-y", "tui-mcp"],
   171|  "enabled": true
   172|}
   173|```
   174|
   175|### tui-mcp results per agent
   176|
   177|| Agent | MCP tools visible? | `launch` works? | `screenshot` works? |
   178||---|---|---|---|
   179|| Claude Code | YES | Blocked by permission | Blocked by permission |
   180|| Codex (bypass) | YES | `posix_spawnp failed` (sandbox blocks node-pty) | N/A |
   181|| OpenCode | YES | `posix_spawnp failed` (environment blocks node-pty) | N/A |
   182|
   183|**Key finding:** tui-mcp's approach (node-pty for PTY spawn) is fundamentally blocked by the sandbox in Codex and OpenCode. Claude Code blocks it via permission system unless `--dangerously-skip-permissions` is used.
   184|
   185|### CLI screenshot tools (work perfectly)
   186|
   187|These don't need MCP — just drop into any agent's shell:
   188|
   189|```bash
   190|# termshot — PNG with terminal window chrome (~30KB)
   191|# Installed: /tmp/termshot (from GitHub releases)
   192|termshot --filename /tmp/shot.png -- ls -la
   193|
   194|# termframe — SVG vector output (~2.3KB)
   195|# Installed via: brew install termframe
   196|termframe -o /tmp/shot.svg -- echo "Hello"
   197|```
   198|
   199|| Agent | termshot | termframe |
   200||---|---|---|
   201|| Claude Code | Blocked (permission) | Blocked (permission) |
   202|| Codex `--dangerously-bypass-approvals-and-sandbox` | WORKS | WORKS |
   203|| OpenCode | WORKS | WORKS |
   204|
   205|---
   206|
   207|## Key CLI Flags for Scripting
   208|
   209|### Claude Code
   210|```bash
   211|--print                      # Non-interactive, stdout response
   212|--output-format json         # Structured JSON output
   213|--session-id UUID            # Named/persistent session
   214|--resume UUID                # Resume session
   215|--fork-session               # Fork on resume
   216|--model MODEL                # Model override
   217|--no-session-persistence     # Ephemeral
   218|--dangerously-skip-permissions  # Skip approval
   219|--permission-mode bypassPermissions  # Alt to above
   220|--system-prompt "..."        # Custom system prompt
   221|--append-system-prompt "..." # Add to default
   222|--json-schema PATH/JSON      # Structured output validation
   223|--max-budget-usd 0.10       # Cost cap
   224|--input-format stream-json   # Streaming input
   225|```
   226|
   227|### Codex
   228|```bash
   229|exec "prompt"                # Non-interactive
   230|--json                       # NDJSON output
   231|--dangerously-bypass-approvals-and-sandbox  # Full bypass
   232|-C /path                     # Working directory
   233|-m provider/model            # Model switch
   234|-s read-only|workspace-write|danger-full-access  # Sandbox level
   235|-a never|on-request|untrusted  # Approval mode
   236|--search                     # Enable web search
   237|--config key=value           # Override config
   238|--include-non-interactive    # Include exec sessions in resume
   239|```
   240|
   241|### OpenCode
   242|```bash
   243|run "prompt"                 # Non-interactive
   244|-c                           # Continue last session
   245|-s SESSION_ID                # Specific session
   246|--fork                       # Fork on continue
   247|-m provider/model            # Model switch
   248|--agent AGENT                # Agent persona
   249|--model MODEL                # Shorthand
   250|```
   251|
   252|---
   253|
   254|## Comparison Summary
   255|
   256|| Capability | Claude Code | Codex | OpenCode |
   257||---|---|---|---|
   258|| CLI non-interactive | `--print` | `exec` | `run` |
   259|| stdin pipe | YES | YES | YES |
   260|| JSON structured output | YES (schema) | YES (NDJSON) | NO |
   261|| Model switch CLI | YES | YES | YES |
   262|| Session create/resume | YES (UUID) | YES (ID) | YES (ses_ ID) |
   263|| Session persistence across calls | YES | Ephemeral by default | YES |
   264|| Native screenshot tool | NO | NO | NO |
   265|| termshot/termframe via shell | Blocked (needs bypass) | Works (bypass) | Works |
   266|| tui-mcp MCP server | Loads (blocked) | Loads (broken) | Loads (broken) |
   267|| MCP server config | `claude mcp` CLI | config.toml | opencode.json |
   268|| Agent persona CLI | `--agent` | Config only | `--agent` |
   269|
   270|---
   271|
   272|## Practical Recommendations
   273|
   274|1. **For headless scripting with screenshots:** Use OpenCode (`opencode run`) or Codex (`codex exec --dangerously-bypass-approvals-and-sandbox`) with termshot/termframe for visual output.
   275|
   276|2. **For structured data extraction:** Claude Code's `--json-schema` + `--output-format json` is the most powerful option — returns validated structured output.
   277|
   278|3. **For session-persistent pipelines:** OpenCode's `ses_` session IDs and Claude Code's UUID-based sessions are the most reliable for CLI-based session management.
   279|
   280|4. **For local model routing:** Codex has `--oss` for local Ollama/LM Studio; OpenCode has extensive provider registry including openrouter.
   281|
   282|5. **For MCP-based TUIs:** tui-mcp is conceptually the right tool but blocked in practice by sandbox restrictions. termshot/termframe remain the reliable alternatives.
   283|

## See Also

- [[claude-code-source-leak]] — Deep dive into Claude Code internals, anti-distillation mechanisms, and source code analysis; complements this CLI comparison
