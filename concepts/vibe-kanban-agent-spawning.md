---
title: Vibe Kanban Agent Spawning Architecture
created: 2026-04-08
updated: 2026-04-08
type: concept
tags: [agent, orchestration]
sources: [raw/articles/x-bookmarks-2026.md]
---

# Vibe Kanban — Agent Spawning Architecture Deep Dive

## Overview
    10|
    11|Vibe Kanban (github.com/BloopAI/vibe-kanban-agent-spawning, 24K+ stars) is an open-source orchestration platform written primarily in Rust (50%) with a TypeScript/React frontend (46%). It manages multiple AI coding agents (Claude Code, Codex, Gemini CLI, Cursor, OpenCode, Copilot, Amp, Droid, Qwen Code, etc.) through a kanban board interface, running them in parallel with isolated git worktrees.
    12|
    13|This report focuses on the core technical question: **how does Vibe Kanban spawn, manage, and detect completion of agent instances?**
    14|
    15|## Research Questions
    16|
    17|1. **Agent spawning architecture** — How does it detect, configure, and launch agent instances?
    18|2. **Protocol/interface layer** — What communication protocol does it use to talk to spawned agents?
    19|3. **Task delegation & state management** — How are tasks passed and results streamed back?
    20|4. **Completion detection** — How does it know when an agent has finished executing?
    21|5. **Configuration & extensibility** — How are new agent types registered?
    22|
    23|## Answers / Findings
    24|
    25|### 1. Agent Spawning Architecture
    26|
    27|Vibe Kanban uses a **trait-based executor system** in Rust. Every coding agent is a backend executor implementing the `StandardCodingAgentExecutor` trait.
    28|
    29|**Core trait interface** (`crates/executors/src/executors/mod.rs`):
    30|
    31|```rust
    32|#[async_trait]
    33|#[enum_dispatch(CodingAgent)]
    34|pub trait StandardCodingAgentExecutor {
    35|    fn apply_overrides(&mut self, _executor_config: &ExecutorConfig) {}
    36|    fn use_approvals(&mut self, _approvals: Arc<dyn ExecutorApprovalService>) {}
    37|    async fn spawn(&self, current_dir: &Path, prompt: &str, env: &ExecutionEnv)
    38|        -> Result<SpawnedChild, ExecutorError>;
    39|    async fn spawn_follow_up(&self, current_dir: &Path, prompt: &str, session_id: &str,
    40|        reset_to_message_id: Option<&str>, env: &ExecutionEnv) -> Result<SpawnedChild, ExecutorError>;
    41|    async fn spawn_review(&self, current_dir: &Path, prompt: &str, session_id: Option<&str>,
    42|        env: &ExecutionEnv) -> Result<SpawnedChild, ExecutorError>;
    43|    fn normalize_logs(&self, _raw_logs_event_store: Arc<MsgStore>, _worktree_path: &Path)
    44|        -> Vec<JoinHandle<()>> { vec![] }
    45|    fn default_mcp_config_path(&self) -> Option<std::path::PathBuf>;
    46|    fn get_availability_info(&self) -> AvailabilityInfo;
    47|    async fn discover_options(&self, ...) -> BoxStream<'static, json_patch::Patch>;
    48|    fn get_preset_options(&self) -> ExecutorConfig;
    49|}
    50|```
    51|
    52|Each agent has its own executor file:
    53|- `crates/executors/src/executors/claude.rs` — Claude Code
    54|- `crates/executors/src/executors/codex.rs` — OpenAI Codex
    55|- `crates/executors/src/executors/gemini.rs` — Gemini CLI
    56|- `crates/executors/src/executors/cursor.rs` — Cursor
    57|- `crates/executors/src/executors/opencode.rs` — OpenCode
    58|- `crates/executors/src/executors/copilot.rs` — GitHub Copilot
    59|- `crates/executors/src/executors/amp.rs` — Amazon Amp
    60|- `crates/executors/src/executors/droid.rs` — Factory Droid
    61|- `crates/executors/src/executors/qwen.rs` — Qwen Code
    62|
    63|**Enum dispatch pattern:** Vibe Kanban uses `enum_dispatch` (zero-cost abstraction) with a `CodingAgent` enum that dispatches to the correct executor at compile time:
    64|
    65|```rust
    66|#[enum_dispatch(CodingAgent)]
    67|pub trait StandardCodingAgentExecutor { ... }
    68|```
    69|
    70|### 2. Protocol/Interface Layer
    71|
    72|Vibe Kanban does NOT use a unified protocol to talk to agents. Instead, **each executor knows how to invoke its specific agent as a subprocess**. The common contract is:
    73|
    74|1. **Locate the binary** — find the CLI tool on PATH
    75|2. **Build the command** — construct `tokio::process::Command` with the right args
    76|3. **Set working directory** — `cwd` is the git worktree
    77|4. **Inject the prompt** — pass the task description as an argument or via stdin
    78|5. **Stream stdout/stderr** — pipe output to the UI via WebSocket
    79|6. **Monitor exit** — detect when the process is done
    80|
    81|**SpawnedChild structure:**
    82|
    83|```rust
    84|pub struct SpawnedChild {
    85|    pub child: AsyncGroupChild,           // The spawned process group
    86|    pub exit_signal: Option<ExecutorExitSignal>,  // Optional completion signal
    87|    pub cancel: Option<CancellationToken>,        // Cancellation token
    88|}
    89|```
    90|
    91|**ACP (Agent Control Protocol):** Some agents (Claude Code, Codex) support ACP — a JSON-RPC 2.0 protocol over stdin/stdout. Vibe Kanban has an ACP harness (`crates/executors/src/executors/acp/harness.rs`) that can communicate with agents supporting this protocol for structured interaction (message editing, follow-ups, approvals).
    92|
    93|### 3. Task Delegation & State Management
    94|
    95|**The full execution flow:**
    96|
    97|```
    98|User creates Kanban issue → selects agent → clicks "Start"
    99|         │
   100|         ▼
   101|1. WorkspaceManager creates git worktree + branch
   102|   (git worktree add -b <branch> <path> <base>)
   103|         │
   104|         ▼
   105|2. Setup script runs (if configured in project settings)
   106|         │
   107|         ▼
   108|3. Executor.spawn() called with:
   109|   - current_dir: worktree path
   110|   - prompt: task title + description
   111|   - env: execution environment (API keys, etc.)
   112|         │
   113|         ▼
   114|4. Agent process spawned as subprocess in worktree
   115|   (tokio::process::Command with process group)
   116|         │
   117|         ▼
   118|5. Output streamed via WebSocket to frontend
   119|   (raw stdout/stderr, normalized for some agents)
   120|         │
   121|         ▼
   122|6. Exit detected → commits reviewed → PR created
   123|```
   124|
   125|**Git Worktree Isolation:** This is the key architectural decision. Each task gets its own git worktree — a linked working directory sharing the same `.git` object database but with independent files, HEAD, and index. This means:
   126|- Agents never conflict (different working directories)
   127|- All agents share the same repo history
   128|- Changes are isolated to branches
   129|- Clean up is `git worktree remove --force`
   130|
   131|**State tracking:** SQLite database tracks:
   132|- `ExecutionProcess` — running/completed/stopped status
   133|- `Workspace` — worktree path, branch, associated task
   134|- `CodingAgentTurn` — individual agent interaction turns
   135|- Task status: `todo` → `inprogress` → `inreview` → `done`
   136|
   137|**Real-time streaming:** Output is streamed to the frontend via WebSocket. The `msg_stores` system buffers messages per execution, and the UI polls/subscribes for updates. Log normalization (`normalize_logs()`) converts raw agent output into structured actions (reasoning, commands, file edits) for richer display.
   138|
   139|**MCP integration:** Vibe Kanban exposes an MCP server that external agents can use. The `start_workspace_session` MCP tool can programmatically spawn agent sessions:
   140|
   141|```
   142|Supported executors via MCP:
   143|- CLAUDE_CODE, GEMINI, CODEX, CURSOR_AGENT, OPENCODE
   144|- Custom agents (DROID, etc.)
   145|- Custom: "custom:ralph_loop" (via RFC #2775)
   146|```
   147|
   148|### 4. Completion Detection — How It Knows When an Agent Is Done
   149|
   150|This is the most nuanced part of the architecture. Vibe Kanban uses a **dual-mode exit detection** system in `container.rs`:
   151|
   152|```rust
   153|// Exit monitor (simplified from container.rs)
   154|tokio::select! {
   155|    // Mode 1: Executor signals completion via oneshot channel
   156|    exit_result = &mut exit_signal_future => {
   157|        // Executor signaled: kill process group, record exit
   158|        command::kill_process_group(&mut child).await;
   159|        status_result = match exit_result {
   160|            Ok(ExecutorExitResult::Success) => Ok(success_exit_status()),
   161|            Ok(ExecutorExitResult::Failure) => Ok(failure_exit_status()),
   162|            Err(_) => Ok(success_exit_status()), // Channel closed = success
   163|        };
   164|    }
   165|    // Mode 2: OS process exit (polls try_wait() every 250ms)
   166|    _ = process_exit_rx.recv() => {
   167|        // Process exited on its own
   168|        status_result = child.try_wait();
   169|    }
   170|}
   171|```
   172|
   173|**Two completion detection modes:**
   174|
   175|| Mode | How It Works | Used By |
   176||------|-------------|---------|
   177|| **Exit Signal** | Agent's read_loop detects a completion message (e.g., `Result` in stream-json), sends via `oneshot::Sender`, container receives on `Option<Receiver>` | Codex, ACP-based agents, agents that don't auto-exit |
   178|| **OS Process Exit** | Polls `try_wait()` every 250ms, detects when process naturally exits | Gemini CLI, OpenCode, agents that exit after completing |
   179|
   180|**The Codex pattern** (`codex.rs:554-558`):
   181|```rust
   182|let (exit_tx, exit_rx) = oneshot::channel();
   183|// Pass exit_tx to read_loop
   184|// When Codex signals completion, read_loop sends ExecutorExitResult::Success
   185|Ok(SpawnedChild { child, exit_signal: Some(exit_rx), cancel: Some(cancel) })
   186|```
   187|
   188|**The ACP pattern** (`acp/harness.rs`):
   189|```rust
   190|// Same oneshot channel pattern
   191|// When ACP session completes, sends through the channel
   192|```
   193|
   194|**Known issue — Claude Code** (GitHub #2495): Claude Code in `-p --output-format=stream-json` mode does NOT exit after completing a task — it stays alive waiting for more messages on stdin. The Claude executor currently returns `exit_signal: None`, which means:
   195|- The exit monitor waits on `std::future::pending()` for the signal (never fires)
   196|- The OS exit branch polls `try_wait()` (never fires because process is alive)
   197|- Sessions get stuck in "running" forever
   198|
   199|The suggested fix: wire up an `exit_signal` for Claude Code, matching the Codex/ACP pattern — when the read_loop sees `CLIMessage::Result`, send through the channel before breaking.
   200|
   201|**Custom executors** (RFC #2775): For custom agents, completion is detected purely by OS process exit code:
   202|- Exit code `0` → task moves to Review
   203|- Non-zero → marked as failed
   204|- No structured output parsing, no exit signals — fire-and-forget
   205|
   206|### 5. Configuration & Extensibility
   207|
   208|**Adding a new agent currently requires:**
   209|1. Create a new Rust file in `crates/executors/src/executors/<agent>.rs`
   210|2. Implement `StandardCodingAgentExecutor` trait
   211|3. Add variant to the `CodingAgent` enum
   212|4. Register in the executor dispatcher
   213|5. TypeScript types auto-generated via `ts-rs`
   214|
   215|**Custom Executor RFC (#2775)** — proposes a config-driven approach so new agents can be added without code changes:
   216|
   217|```json
   218|{
   219|  "executors": {
   220|    "CUSTOM": {
   221|      "RALPH_LOOP": {
   222|        "CUSTOM": {
   223|          "command": "npx",
   224|          "args": ["fabis-ralph-loop", "full-pipeline", "--iterations", "20"],
   225|          "prompt_mode": "arg",
   226|          "env": { "NODE_ENV": "development" }
   227|        }
   228|      }
   229|    }
   230|  }
   231|}
   232|```
   233|
   234|**Prompt modes for custom executors:**
   235|- `None` — no prompt passed
   236|- `Arg` — appended to command arguments
   237|- `Stdin` — piped to stdin
   238|- `Env` — set as environment variable
   239|- `File` — written to a temp file, path passed as arg
   240|
   241|**Executor Profiles:** Agents can have multiple profiles (DEFAULT, PLAN, ROUTER, etc.) with different configurations (model selection, approval mode, max turns). Profiles are stored in `crates/executors/default_profiles.json` and can be overridden via `profiles.json`.
   242|
   243|## Architecture / Technical Details
   244|
   245|```
   246|┌─────────────────────────────────────────────────────────┐
   247|│                    Frontend (React/TS)                   │
   248|│  Kanban Board  │  Task Panel  │  Settings  │  Preview    │
   249|└──────────────────────┬──────────────────────────────────┘
   250|                       │ WebSocket + REST API
   251|┌──────────────────────┴──────────────────────────────────┐
   252|│                  Backend (Rust/Axum)                      │
   253|│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐ │
   254|│  │  HTTP API   │  │   MCP Server │  │  Container Mgr  │ │
   255|│  │  (routes)   │  │  (task ops)  │  │  (lifecycle)    │ │
   256|│  └──────┬──────┘  └──────┬───────┘  └────────┬────────┘ │
   257|│         │                │                    │          │
   258|│  ┌──────┴────────────────┴────────────────────┴──────┐  │
   259|│  │           Executor Dispatcher                     │  │
   260|│  │  (enum_dispatch → StandardCodingAgentExecutor)     │  │
   261|│  └──────┬──────┬──────┬──────┬──────┬──────┬─────────┘  │
   262|│         │      │      │      │      │      │            │
   263|│    ┌────┴┐ ┌───┴──┐ ┌──┴──┐ ┌─┴───┐ ┌─┴──┐ ┌─┴────┐   │
   264|│    │Claude│ │Codex │ │Gemini│ │Cursor│ │Open│ │Custom│   │
   265|│    │ Code │ │      │ │ CLI  │ │Agent │ │Code│ │Exec  │   │
   266|│    └──┬───┘ └──┬───┘ └──┬──┘ └──┬──┘ └─┬──┘ └──┬───┘   │
   267|│       │        │        │       │       │       │       │
   268|│  ┌────┴────────┴────────┴───────┴───────┴───────┴────┐  │
   269|│  │           Subprocess Spawner (tokio::process)       │  │
   270|│  │  - Process groups (AsyncGroupChild)                 │  │
   271|│  │  - Exit monitoring (oneshot + try_wait polling)     │  │
   272|│  │  - Output streaming (stdout/stderr → WebSocket)     │  │
   273|│  └─────────────────────────┬──────────────────────────┘  │
   274|└────────────────────────────┼─────────────────────────────┘
   275|                             │
   276|              ┌──────────────┼──────────────┐
   277|              │              │              │
   278|         ┌────┴────┐   ┌────┴────┐   ┌────┴────┐
   279|         │Worktree 1│   │Worktree 2│   │Worktree 3│
   280|         │(Claude)  │   │(Codex)  │   │(Gemini) │
   281|         │branch:   │   │branch:  │   │branch:  │
   282|         │feat-auth │   │feat-api │   │fix-bug  │
   283|         └──────────┘   └─────────┘   └─────────┘
   284|```
   285|
   286|## Source Exploration
   287|
   288|| Source | What Was Found |
   289||--------|---------------|
   290|| `crates/executors/src/executors/mod.rs` | `StandardCodingAgentExecutor` trait, `SpawnedChild` struct, `ExecutorExitResult` enum |
   291|| `crates/local-deployment/src/container.rs` | Exit monitor with `tokio::select!`, process group management, workspace lifecycle |
   292|| `crates/executors/src/executors/claude.rs` | Claude Code executor (stream-json mode, exit_signal: None bug) |
   293|| `crates/executors/src/executors/codex.rs` | Codex executor with proper oneshot exit_signal pattern |
   294|| `crates/executors/src/executors/acp/harness.rs` | ACP harness for JSON-RPC agent communication |
   295|| GitHub Issue #2775 | RFC for generic custom executor — config-driven, no code changes needed |
   296|| GitHub Issue #2495 | Bug: Claude Code executor never signals completion, sessions stuck forever |
   297|| `crates/services/src/services/worktree_manager.rs` | Git worktree creation/removal logic |
   298|| `crates/services/src/services/workspace_manager.rs` | Top-level workspace creation entry point |
   299|
   300|## Code Examples
   301|
   302|### How an agent is spawned (simplified flow):
   303|
   304|```rust
   305|// 1. User clicks "Start" on a task → API route calls container
   306|let workspace = workspace_manager.create_workspace(&task, &repo).await?;
   307|
   308|// 2. Container creates execution process record
   309|let exec_process = ExecutionProcess::create(&db.pool, &workspace, &executor_action).await?;
   310|
   311|// 3. Executor's spawn() is called
   312|let spawned = executor.spawn(
   313|    &worktree_path,      // isolated directory
   314|    &task_description,   // the prompt
   315|    &execution_env       // env vars
   316|).await?;
   317|
   318|// 4. Exit monitor spawned as background task
   319|let monitor = container.spawn_exit_monitor(
   320|    &exec_process.id,
   321|    spawned.exit_signal  // Some(receiver) or None
   322|);
   323|
   324|// 5. Output streamed via WebSocket while agent works
   325|// 6. Exit detected → cleanup → status updated
   326|```
   327|
   328|### How completion is detected (Codex example):
   329|
   330|```rust
   331|// In codex.rs - spawn method
   332|let (exit_tx, exit_rx) = oneshot::channel();
   333|
   334|// Spawn read_loop that watches for completion messages
   335|let read_loop = tokio::spawn(async move {
   336|    while let Some(msg) = reader.next().await {
   337|        match msg {
   338|            CLIMessage::Result { is_error, .. } => {
   339|                let result = if is_error {
   340|                    ExecutorExitResult::Failure
   341|                } else {
   342|                    ExecutorExitResult::Success
   343|                };
   344|                let _ = exit_tx.send(result); // Signal completion!
   345|                break;
   346|            }
   347|            _ => { /* stream to UI */ }
   348|        }
   349|    }
   350|});
   351|
   352|Ok(SpawnedChild {
   353|    child,
   354|    exit_signal: Some(exit_rx),  // Container will wait on this
   355|    cancel: Some(cancel),
   356|})
   357|```
   358|
   359|## Executor Deep Comparison: Source Code Analysis
   360|
   361|> Direct analysis of `crates/executors/src/executors/{claude,codex,opencode,gemini,cursor}.rs`
   362|
   363|### Spawning Mechanism
   364|
   365|| Executor | How It Launches | Base Command | Process Input |
   366||---|---|---|---|
   367|| **Claude Code** | Subprocess with stream-json | `npx @anthropic-ai/claude-code -p` | Stdin (after protocol init) |
   368|| **Codex** | Subprocess in `app-server` mode | `npx @openai/codex app-server` | JSON-RPC over stdin/stdout |
   369|| **OpenCode** | Spawns HTTP server, then calls REST API | `npx opencode-ai serve --hostname 127.0.0.1 --port 0` | HTTP POST to `/sessions` |
   370|| **Gemini** | Subprocess with `--experimental-acp` flag | `npx @google/gemini-cli --experimental-acp` | Via ACP harness (JSON-RPC stdin/stdout) |
   371|| **Cursor** | Subprocess with stream-json | `cursor-agent -p --output-format=stream-json` | Stdin (piped then shutdown) |
   372|
   373|**Key difference:** OpenCode is the ONLY one that spawns an HTTP server and communicates via REST. All others are stdin/stdout subprocess protocols. Gemini delegates ALL spawning logic to the shared `AcpAgentHarness`.
   374|
   375|### Communication Protocol
   376|
   377|| Executor | Protocol | Submodule | How It Works |
   378||---|---|---|---|
   379|| **Claude Code** | Custom `ProtocolPeer` + `ClaudeAgentClient` | `client.rs`, `protocol.rs`, `types.rs` | Full handshake: initialize -> set_permission_mode -> send_user_message |
   380|| **Codex** | JSON-RPC 2.0 via `AppServerClient` | `client.rs`, `jsonrpc.rs` | Creates `JsonRpcPeer` on stdin/stdout, connects client, calls `thread_start` + `turn_start` |
   381|| **OpenCode** | HTTP REST via SDK | `sdk.rs` | Spawns server, waits for URL on stdout, calls `run_session()` via HTTP POST |
   382|| **Gemini** | ACP (Agent Control Protocol) | Uses shared `AcpAgentHarness` | Delegates everything to the harness |
   383|| **Cursor** | stream-json (simplest) | `mcp.rs` (for server trust only) | Writes prompt to stdin, shuts down stdin, returns child. No protocol layer. |
   384|
   385|### Completion Detection
   386|
   387|| Executor | Exit Signal | Reliability |
   388||---|---|---|
   389|| **Claude Code** | **NONE** (`exit_signal: None`) | **BROKEN** -- stays alive after completing (issue #2495) |
   390|| **Codex** | **YES** (`oneshot::channel`) | **Best** -- JsonRpcPeer detects completion in JSON-RPC stream |
   391|| **OpenCode** | **YES** (`oneshot::channel`) | **Good** -- sends result after `run_session()` HTTP call returns |
   392|| **Gemini** | **Via ACP Harness** | **Medium** -- managed internally by harness |
   393|| **Cursor** | **NONE** (raw `AsyncGroupChild`) | **Low** -- relies on OS process exit only |
   394|
   395|### Config Options Comparison
   396|
   397|| Field | Claude | Codex | OpenCode | Gemini | Cursor |
   398||---|---|---|---|---|---|
   399|| `model` | Yes | Yes | Yes | Yes | Yes |
   400|| `auto_approve / yolo / force` | `dangerously_skip_permissions` | `sandbox` + `ask_for_approval` | `auto_approve` | `yolo` | `force` |
   401|| `effort / reasoning` | `effort` (Low/Med/High/Max) | `model_reasoning_effort` | N/A | N/A | `reasoning` (per-model) |
   402|| `agent` (sub-agent) | Yes | N/A | `agent` + `variant` | N/A | N/A |
   403|| `plan mode` | `plan` | `plan` | N/A | N/A | N/A |
   404|| `sandbox mode` | N/A | Yes (Auto/RO/Write/Danger) | N/A | N/A | N/A |
   405|| `prompt compaction` | N/A | `compact_prompt` | `auto_compact` | N/A | N/A |
   406|| `hooks system` | Yes (PreToolUse/Stop) | N/A | N/A | N/A | N/A |
   407|| `model router/proxy` | `claude_code_router` | N/A | N/A | N/A | N/A |
   408|| `OSS mode` | N/A | `oss` | N/A | N/A | N/A |
   409|
   410|### Spawn Flow Details (from source)
   411|
   412|**Claude Code** (`spawn_internal`, L614-705):
   413|```
   414|1. Build command: npx @anthropic-ai/claude-code -p --output-format=stream-json
   415|2. Spawn subprocess, take stdin/stdout pipes
   416|3. Create ClaudeAgentClient + ProtocolPeer
   417|4. ProtocolPeer::spawn(child_stdin, child_stdout, client, cancel)
   418|5. Initialize control protocol -> set_permission_mode -> send_user_message(prompt)
   419|6. Return SpawnedChild { child, exit_signal: None, cancel: Some(cancel) }
   420|```
   421|BUG: `exit_signal: None` at L702. The protocol peer sends the message but nothing signals completion back.
   422|
   423|**Codex** (`spawn_app_server`, L624-745):
   424|```
   425|1. Build command: npx @openai/codex app-server
   426|2. Spawn subprocess, take stdin/stdout pipes
   427|3. Create oneshot::channel for exit_signal
   428|4. Build AppServerClient + JsonRpcPeer
   429|5. client.initialize() -> task(client, exit_tx) [launch_codex_agent]
   430|6. launch_codex_agent: thread_start -> turn_start(prompt)
   431|7. JsonRpcPeer detects completion in JSON-RPC stream -> sends through exit_tx
   432|8. Return SpawnedChild { child, exit_signal: Some(exit_rx), cancel: Some(cancel) }
   433|```
   434|Most structured: uses closure pattern (`task: F`) so the spawn_app_server handles all boilerplate and delegates agent logic.
   435|
   436|**OpenCode** (`spawn_inner`, L158-245):
   437|```
   438|1. Build command: npx opencode-ai serve --hostname 127.0.0.1 --port 0
   439|2. Spawn server subprocess
   440|3. Wait for server URL on stdout (wait_for_server_url)
   441|4. Create oneshot::channel for exit_signal
   442|5. Build RunConfig { base_url, directory, prompt, model, agent, ... }
   443|6. tokio::spawn: run_session(config) or run_slash_command(config)
   444|7. HTTP POST to server, when call returns -> send exit_signal
   445|8. Return SpawnedChild { child, exit_signal: Some(exit_rx), cancel: Some(cancel) }
   446|```
   447|UNIQUE: Only executor using HTTP. Spawns a local server, then acts as a client to it.
   448|
   449|**Gemini** (`spawn`, L84-108):
   450|```
   451|1. Build command: npx @google/gemini-cli --experimental-acp [--model X] [--yolo]
   452|2. harness = AcpAgentHarness::new()
   453|3. harness.spawn_with_command(current_dir, prompt, command, env, cmd, approvals)
   454|4. Returns whatever the harness returns
   455|```
   456|Thinnest: literally 25 lines of spawn code. Delegates ALL protocol management to the shared ACP harness.
   457|
   458|**Cursor** (`spawn`, L186-222):
   459|```
   460|1. Build command: cursor-agent -p --output-format=stream-json [--force|--trust] [--model X]
   461|2. mcp::ensure_mcp_server_trust(self, current_dir)
   462|3. Spawn subprocess, take stdin pipe
   463|4. stdin.write_all(prompt).await; stdin.shutdown().await
   464|5. Return child.into() // raw AsyncGroupChild, NO exit_signal, NO cancel token
   465|```
   466|Simplest but most fragile: fire-and-forget stdin. No protocol layer, no exit signaling, no cancellation.
   467|
   468|### Unique Capabilities
   469|
   470|**Claude Code** (3,278 lines -- most complex):
   471|- Hook system (PreToolUse/Stop callbacks for approval gating)
   472|- Claude Code Router (proxy to non-Claude models via `@musistudio/claude-code-router`)
   473|- Sub-agent selection
   474|- Effort levels for compute budgeting (Low/Med/High/Max)
   475|- Full protocol handshake: initialize -> set_permission_mode -> send_user_message
   476|- **Known bug**: `exit_signal: None` causes stuck sessions (#2495)
   477|
   478|**Codex** (746 lines -- most structured):
   479|- Sandbox modes (Auto, ReadOnly, WorkspaceWrite, DangerFullAccess)
   480|- Approval policies (UnlessTrusted, OnFailure, OnRequest, Never)
   481|- Review mode with dedicated `spawn_review()`
   482|- Thread management (`thread_start`, `thread_fork` for session continuation)
   483|- Collaboration mode negotiation
   484|- OSS mode flag
   485|- Cleanest exit signal implementation (oneshot + JSON-RPC completion detection)
   486|
   487|**OpenCode** (822 lines -- most different architecture):
   488|- HTTP server mode (ONLY one not using stdin/stdout protocol)
   489|- Auto-compact for context window management
   490|- Server password auth (`OPENCODE_SERVER_PASSWORD`)
   491|- SDK layer: `run_session()` / `run_slash_command()` abstractions
   492|- Agent variant system
   493|
   494|**Gemini** (236 lines -- thinnest wrapper):
   495|- Only 4 config fields (model, yolo, append_prompt, cmd)
   496|- Delegates everything to shared `AcpAgentHarness`
   497|- Yolo mode (`--yolo --allowed-tools run_shell_command`)
   498|- OAuth-based auth detection (`.gemini/oauth_creds.json`)
   499|
   500|**Cursor** (1,491 lines):
   501|
## Related

- [[paperclip-vs-vibe-kanban]] — detailed architecture comparison between Paperclip and Vibe Kanban
- [[autonomous-ios-ui-testing]] — FlowDeck CLI for autonomous iOS UI testing; relevant to agent tool-use and testing workflows

