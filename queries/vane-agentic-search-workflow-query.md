---
title: "Vane agentic search workflow — fixed pipeline vs AI agent with tools"
created: 2026-04-18
updated: 2026-04-18
type: query
tags: [ai-tools, search, self-hosted, rag]
sources: [sources/vane/src/lib/agents/search/index.ts, sources/vane/src/lib/agents/search/classifier.ts, sources/vane/src/lib/agents/search/researcher/index.ts, sources/vane/src/lib/agents/search/researcher/actions/registry.ts, sources/vane/src/lib/agents/search/researcher/actions/plan.ts, sources/vane/src/lib/agents/search/researcher/actions/search/webSearch.ts, sources/vane/src/lib/agents/search/researcher/actions/done.ts, sources/vane/src/lib/prompts/search/classifier.ts]
question: "When you hit search in Vane, is it a fixed pipeline or does the AI agent decide its own plan? Can MCP be connected?"
answer_status: answered
related_pages:
  - [[vane]]
  - [[perplexica]]
  - [[searxng]]
---

## Question

When you hit search in [[vane]], what exactly happens? Is it:
1. A fixed multi-stage pipeline (classify → search → synthesize)?
2. Or an AI agent that gets tools and decides its own plan at runtime?

Also: can MCP (Model Context Protocol) servers be connected to Vane?

## Answer

### Architecture: Hybrid — Fixed Orchestration + Agentic Research Loop

Vane uses a **two-phase architecture**: a deterministic orchestration layer (SearchAgent) that gates a true tool-calling agent (Researcher) for the actual search work.

---

### Phase 1 — SearchAgent.searchAsync() (Fixed Sequence)

The entry point at `POST /api/chat`. Always runs in the same order:

```
1. Upsert DB message record (idempotent)
         ↓
2. CLASSIFY — LLM decides widget/search needs based on query
         ↓
   ┌──────────────────────────────────────────┐
   │  PARALLEL EXECUTION                       │
   │  ┌────────────────┐ ┌─────────────────┐ │
   │  │ WidgetExecutor │ │ Researcher       │ │
   │  │ (always runs)   │ │ (if not skipSearch)│ │
   │  └────────────────┘ └─────────────────┘ │
   └──────────────────────────────────────────┘
         ↓
3. Gather widget outputs + search results into one context block
         ↓
4. STREAM FINAL ANSWER — LLM synthesizes from gathered context
         ↓
5. Update DB → 'completed'
```

The only branching in Phase 1 is: skip research entirely if the classifier says `skipSearch: true` (e.g., math queries answered by the calculation widget alone).

---

### Phase 2 — Researcher (True AI Agent with Tools)

The Researcher is a **tool-calling agent** that runs inside a loop. This is where the AI decides what to do — not a fixed pipeline.

**Loop mechanics:**
- Mode-based iteration limits: `speed=2`, `balanced=6`, `quality=25`
- Each iteration: LLM must call `__reasoning_preamble` FIRST (plan in natural language), then tool calls
- Agent exits when it calls the `done` tool OR hits the iteration cap

**Available tools (registered in ActionRegistry — not MCP):**

| Tool | Function |
|---|---|
| `__reasoning_preamble` | States the agent's plan before any other tool. Speed mode skips this. |
| `web_search` | Searches via [[searxng]] (up to 3 keyword queries per call). The agent decides queries based on prior results. |
| `academic_search` | Separate tool for academic/scholar sources |
| `social_search` | Separate tool for social/discussion forum sources |
| `scrape_url` | Fetch and parse a specific URL found in search results |
| `uploads_search` | Semantic search over user-uploaded files |
| `done` | Signals research complete — agent decides when to call this |

**Iteration flow:**
```
Iteration N:
  1. LLM receives: system prompt + conversation history
  2. LLM calls __reasoning_preamble → emits reasoning block to UI (visible "thinking" step)
  3. LLM calls search/tool(s) or done
  4. ActionRegistry.executeAll() runs the tools in parallel
  5. Results appended to agent's message history as tool results
  6. Loop to next iteration — LLM sees all prior tool results, decides next step
```

The agent sees the same tool-call history pattern as OpenAI/gpt-4o tool-calling. It dynamically decides whether to do more searches or exit via `done` based on how much context it has accumulated.

**Mode differences are baked into the tool prompts:**

- **Speed**: "you get ONE call, make it count, use 3 queries, no iteration" — essentially single-shot
- **Balanced**: "start broad, then narrow, do multiple iterations"
- **Quality**: "never stop before 5-6 iterations unless query is trivially answerable"

---

### Widgets — Parallel Side Channel, Not Agentic

Widgets (Weather, Stock, Calculation) are **not part of the research loop**. They're classified in Phase 1 based on the classifier output, then executed in parallel via WidgetExecutor. Their outputs are injected into the final context block with a note that they shouldn't be cited as sources.

Widget decisions are **deterministic** — based on classification flags, not agent choice.

---

### Can MCP Be Connected to Vane?

**No native MCP support.** The tool system is a custom `ActionRegistry` where tools are TypeScript `ResearchAction` classes registered at startup. MCP is not used anywhere in the codebase.

To extend Vane with MCP you'd need to:
1. Wrap MCP servers as custom `ResearchAction` classes that conform to the registry interface
2. The `scrape_url` action is the closest template — it fetches content and feeds it back into the agent context
3. You'd essentially build MCP-to-internal-tool adapters, one per MCP tool you want to expose

---

## Practical Verdict

Vane is **agentic in the research phase, fixed in orchestration**. The SearchAgent orchestration is a deterministic pipeline, but the Researcher that does the actual search work is a genuine tool-calling loop — the LLM decides what to search, how many queries to run, and when it's done, based on what it finds. The "mode" setting (speed/balanced/quality) controls how aggressively the agent iterates and whether it shows its reasoning steps.

MCP cannot be plugged in natively — Vane's tool system is a custom registry that would require adapter code to bridge any MCP server.
