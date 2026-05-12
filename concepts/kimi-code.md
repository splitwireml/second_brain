---
title: Kimi Code
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [ai-model, coding, koai, moonshot-ai, open-source, vibe-coding]
sources: [raw/articles/xarticle-kimi-k26-complete-az-guide-to-the-chinese-ai-nobod-2053210009689870535.md]
related_entity: [[moonshot-ai]]
author: [[kirillk-web3]]
---

# Kimi Code

Kimi's coding agent — powered by [[kimi-k2.6]], accessible at kimi.com/code. Similar to Claude Code but running K2.6 natively. Takes tasks (outcomes), not just questions.

## Core Distinction

- **Assistant**: you ask, it answers, you implement
- **Agent**: you describe the outcome, it executes, iterates, fixes errors, delivers

Kimi Code does the second.

## 5 Hidden Commands

| Command | Purpose |
|-|
| `@` (context mapping) | Pull live definitions from indexed codebase; eliminates copy-paste hell; chain symbols (`@AuthService.refresh @TokenStore.cleanup`) for cross-file context |
| `/explain` | Generate architectural digest of legacy codebases — thread-safety model, memory allocation patterns, hot path identification; collapses 2-3 day onboarding to 10 minutes |
| `.kimi/rules` | Persistent project-level instructions baked into session DNA; standardize team output, eliminate rework loops; version-control alongside codebase |
| Checkpoint Prompting | Structured status reports at intervals (`[ITERATION N]`, `[PERFORMANCE]`, `[BLOCKERS]`, `[STATE]`); insurance for 6+ hour sessions; crash recovery not restart |
| `/test` | Analyze implementation, identify edge cases, mock dependencies, generate 80% coverage in 2 minutes; includes race conditions, nulls, overflows |

## Key Benchmark Claims

- SWE-Bench: on par with Claude Opus 4.7
- Terminal-Bench: on par with Claude Opus 4.7
- Long-horizon agentic tasks: **exceeds** Opus 4.7 on sustained multi-hour workflows
- Cost: $0.80/M input, $3.60/M output vs Opus 4.7's $5.00/$25.00 — **7x cheaper**

## Real-World Cases

1. **Zig Inference Optimization on Mac**: 4,000+ tool calls, 12+ hours, 14 optimization iterations; 15 → 193 tok/sec (20% faster than LM Studio) without human intervention
2. **Financial Matching Engine Overhaul**: 13 hours, 12 optimization strategies, 1,000+ tool calls, 4,000+ lines modified; medium throughput 0.43 → 1.24 MT/s (+185%), peak 1.23 → 2.86 MT/s (+133%)

## Setup

```bash
# Mac/Linux
curl -LsSf https://code.kimi.com/install.sh | bash

# Windows (PowerShell)
Invoke-RestMethod https://code.kimi.com/install.ps1 | Invoke-Expression

# Verify
kimi --version

# Alternative via uv
uv tool install --python 3.13 kimi-cli
```

Auth: `kimi login` → browser window → Kimi account

## Vibe Coding Prompt: Full-Stack App in One Session

```plaintext
Build a task management app with:
FRONTEND: Next.js 14 + App Router, Tailwind + shadcn/ui, dark mode, responsive
BACKEND: SQLite via Drizzle ORM, tRPC, Zod validation
AUTH: OAuth 2.0 with GitHub login, protected routes
FEATURES: Create/edit/delete tasks, priority, due dates, filter/search
DEPLOY: Vercel, vercel.json, env example
```

Expected: working app in 20–45 minutes.

## Why K2.6 Beats Claude on Coding in Practice

1. **~35% fewer steps** to same outcome → fewer tokens → lower cost → faster execution
2. **Better instruction following** — doesn't drift; surgical precision in large codebases
3. **Better real-world API/tool understanding** — less constant correction

## Troubleshooting Failures

| Failure | Symptom | Fix |
|-|
| Drift | Starts solving different problem | Scope lock: `Scope: [module/file]. Do not change outside this scope.` |
| Context Collapse | Forgets architecture constraints after 2+ hours | Create CONSTRAINTS.md, use `/compact`, break into sub-sessions with `--resume` |
| Silent Regression | Tests pass but something else broke | Prompt: `Run full test suite, verify no unrelated tests failed` |
| Over-Engineering | Rewrites entire module for 3-line fix | `Make minimal change necessary. Do not refactor unrelated code.` |
| Tool Call Failure | Command fails silently, moves on | `After every shell command, verify output. If command fails, stop and report.` |

## Related

- [[kimi-k2.6]] — underlying model
- [[moonshot-ai]] — publisher
- [[vibe-coding-in-production]] — related vibe coding framework
- [[claude-code]] — competitor coding agent