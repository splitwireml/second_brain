---
title: Software Factory with Claude Code
created: 2026-06-11
updated: 2026-08-08
type: concept
tags: [claude-code, workflow, orchestration, agent, testing]
sources: [raw/articles/xarticle-how-to-build-a-software-factory-with-claude-code-t-2058832033628241931.md, raw/articles/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md]
related_entity: [[sairahul1]]
author: [[sairahul1]]
---

# Software Factory with Claude Code

A structured multi-agent coding workflow proposed by [[sairahul1]] as an alternative to ad-hoc [[vibe-coding]] inside one long Claude Code chat. The core claim is that most AI coding failures are workflow failures: one session is being forced to act as analyst, architect, backend engineer, frontend engineer, tester, and reviewer all at once.

## Core idea

Instead of one overloaded conversation, the source splits delivery into a seven-agent chain with narrow scope, explicit handoffs, and three human checkpoints. The goal is not just more automation, but less silent error propagation.

## The seven roles

1. **Codebase Researcher** — maps relevant files, patterns, risks, and test impact before any implementation.
2. **Story Writer** — converts a rough request into a user story, acceptance criteria, edge cases, exclusions, and open questions.
3. **Spec Writer** — turns the approved story into a technical brief covering data model, API, frontend, tests, and risk.
4. **Backend Builder** — implements server-side code and unit tests within a constrained backend scope.
5. **Frontend Builder** — implements UI against the backend's returned contract without inventing new APIs.
6. **Test Verifier** — writes acceptance tests against the story rather than just unit tests around the implementation.
7. **Implementation Validator** — performs an independent gap review against the approved story and spec, reporting severity instead of patching code.

## Why this differs from generic subagents

This pattern is more opinionated than simple [[claude-code-subagents]]. It defines a fixed production chain, forbids scope creep between adjacent roles, and inserts approval gates between problem definition, technical design, and merge. It is closer to a reusable software-delivery harness than to ad-hoc delegation, and overlaps with the broader runtime-harness ideas in [[dynamic-workflows-in-claude-code]].

## Operational principles worth keeping

- **Explore before build** — research runs first, and is read-only.
- **Problem definition before implementation** — story and spec are separate artifacts, each reviewed by a human.
- **Hard role boundaries** — backend and frontend builders cannot edit each other's layer.
- **Acceptance before merge** — feature completion is judged by acceptance tests, not by unit tests alone.
- **Independent validation** — the final reviewer only audits; it does not self-grade by fixing its own findings.

## CLAUDE.md as project memory

The source treats [[karpathy-claude-md]]-style repo memory as foundational infrastructure rather than an optional prompt trick. CLAUDE.md stores stack facts, commands, architectural rules, and anti-patterns so each fresh Claude Code session starts with stable constraints instead of relearning them from chat history.

## Practical effect

The article's framing is that this converts AI from a faster keyboard into a coordinated team. In wiki terms, the concept sits between [[vibe-coding]], [[claude-code-subagents]], and [[dynamic-workflows-in-claude-code]]: same underlying agent primitives, but packaged as a reproducible feature factory with explicit checkpoints and testing discipline.


## Production-line variant: Nazar (2026-08-08)

[[nazik2053]]'s article describes a distinct, more operations-heavy software-factory stack than the earlier fixed seven-agent chain on this page. The common principle is explicit handoff and verification; the source-specific additions are a durable queue, isolated rooms, write-permission wiring, a fail-closed merge gate, and a memory stack that feeds lessons back into future runs. The source identifies the author as Nazar (`@Nazik2053`) and closes with “Written for nazik3502”; that wording is preserved as source evidence, not treated as a second identity. ^[raw/articles/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md]

### Queue and unattended scheduling

The queue is a plain Markdown file at `tasks/QUEUE.md` with `Ready`, `In Progress`, `Blocked`, and `Done Today` sections plus `High Priority` and `Medium Priority` subsections. The source's exact starter shape is:

```text
# Task Queue
## Ready (can be picked up)
### High Priority
- [ ] [HIGH] Fix the checkout webhook retry logic
### Medium Priority
- [ ] Rewrite the onboarding emails
## In Progress
- [ ] @builder: Add the export endpoint
## Blocked
- [ ] Migrate the billing table (needs: schema decision)
## Done Today
- [x] @builder: Ship the pricing page
```

The queue is enforced by a small checker rather than a prompt-only instruction. Its source-described contract is: scan `tasks/QUEUE.md`, read only `Ready`, return exit code `1` when unchecked `HIGH`/`Critical` work exists, return `0` when the queue is empty or all tasks are `LOW`, run before reporting a clean run, and on exit `1` spawn an agent for the urgent job. It prints `CANNOT SKIP QUEUE` and names the job. Ordinary words count too: a line beginning `FIX:` or `BUG:`, or containing `BROKEN`, is high priority even without a tag; `In Progress` is excluded so work is not picked up twice. The article gives policy text rather than the implementation of `check-queue.js`.

The example schedule is:

```cron
0 8 * * *  cd ~/projects/app && node check-queue.js || ./run-agent.sh
0 1 * * *  cd ~/projects/app && ./run-agent.sh --night
```

The article warns that GitHub Actions scheduled workflows are disabled after 60 days without repository activity and allegedly do not warn; it recommends one repository commit per month. It also recommends a fresh session per run rather than one long-lived conversation: delayed calls re-store growing history at the expensive write rate, and the source claims a nightly loop can exceed hundreds of thousands of tokens by hour 20. These schedule, platform, token-cost, and reliability claims are source-described and unverified here.

### Rooms, handoffs, and concurrency

A room is a Git worktree: a separate directory and branch sharing repository history. The source's exact commands are:

```bash
git worktree add ../app-checkout -b checkout
git worktree list
git worktree remove ../app-checkout
```

Claude Code's documented shortcuts are `claude --worktree`, `claude -w --tmux`, and `claude -w "#1234"`; the third pulls a pull request into a separate room, while a subagent started with `isolation: "worktree"` is described as receiving its own worktree. Ignored-but-untracked files do not arrive in a clean room, so the source proposes a root `.worktreeinclude` using `.gitignore` syntax:

```text
.env
.env.local
config/secrets.json
```

Only files that are both matched and ignored are copied; tracked files are not duplicated. Worktree isolation does not isolate running programs: the source calls out shared port `3000`, shared migrations, and the need for an offset port and a separate database branch per room. Its honest laptop ceiling is about two heavy workers at once; six are described as risking OOM crashes, lost work, and corrupted sessions. This is source-described operational guidance, not an independently tested benchmark.

### Permission-shaped wiring

The source rejects splitting workers only by frontend/backend/deploy task because agents can disagree over the same file. Its durable boundary is write permission:

- Testing reads everything and writes only to the test suite.
- Code review writes only to issues and a refactor file.
- Security writes only to a timestamped security report.
- Performance writes reports and nothing else.
- Platform owns build, deploy, and infrastructure, not application code.

The physical supervision layout places reviewers on the left, the lead and product owner in the center, and builders on the right; the operator reads commits and merges from the center. The source sets a `300`-line maximum per file so a change remains checkable. Its worker-start prompt is intentionally short and exact:

```text
Read CLAUDE.md. Read _FRAGILE.md. Read _NEXT_SESSION_MEMO.md.
We're working on RFD_0172. You're role/SECURITY.
Your only write permission is a timestamped SECURITY_REPORT.
```

The article says the coding agent also ships primitives to create a team, assign tasks, list and update tasks, and pass messages between agents. It presents short prompts plus documentation—not elaborate role definitions—as the coordination interface; the source does not name the team API or a specific model/version.

### Gate policy and evidence boundary

The gate identifies machine-authored changes and applies a strict profile. The source's configuration example is:

```yaml
provenance:
  actors: [copilot-swe-agent[bot], claude[bot], devin-ai-integration[bot], cursoragent]
  branch_prefixes: [copilot/, claude/, agent/, devin/]
  title_markers: ["[agent]", "🤖"]
profiles:
  agent:
    auto_merge_paths: ["**/*.md", "**/*.txt", "docs/**"]
    max_files: 5
    max_lines: 150
    require_ci: true
```

The human-review list is:

```yaml
protected_paths:
  - ".github/**"          # CI runs with repository credentials
  - "**/*auth*"
  - "**/*secret*"
  - "**/.env*"
  - "**/migrations/**"    # schema changes are hard to revert
  - "**/*.tf"
  - "**/package-lock.json" # a lockfile edit is a supply-chain change
```

The design choices are fail closed when the policy file cannot be read; optional earned autonomy through a ledger that widens an author's allowlist only after merged work survives, never opening protected paths; and measured risky-pattern rules tuned until false alarms are near zero. The source names downloads piped into a shell, credential literals `sk-live-`, `ghp_`, and `AKIA`, disabled certificate checks, `permissions: write-all`, and `DROP TABLE` as patterns, and warns that concatenation such as `"sk-live-" + "abc123"` can evade a naive matcher. It recommends a demo script with sample-change verdicts and a dry-run that shows what would be filed without filing it.

### Memory and self-improvement

The source's memory stack is:

- `MEMORY.md` — cross-project standards such as use the SDK, never raw SQL in app code, and `300` lines maximum per file.
- `CLAUDE.md` — what the project is and where it is going; every worker reads it first.
- `_FRAGILE.md` — non-obvious failure points such as auth, payments, and access rules.
- `_NEXT_SESSION_MEMO.md` — shift handover: finished, running, and stuck work.
- `_VOCABULARY.md` — canonical names for project concepts, preventing distinctions such as `member`, `members`, and `membership` from drifting.

At shift end, a worker writes what it did and learned, then a plain-code checker validates proposed rules before they enter the instruction file. Rules that grant permissions, name a credential source, or hand over a shell command are rejected by that checker. The source's command surface is:

```text
/wrap      end the shift: update the handover memo, commit, record what shipped
/sup       five-second status of everything in flight
/fragile   check the danger list before touching sensitive code
/plan      plan first, approve, then implement
/research  investigate in a forked context so it never pollutes the main thread
```

The rules file also says: never factor `tedious` or `repetitive` into recommendations; prefer the technically cleaner solution over the easier one; do not estimate human time, report dependencies and risk; find-and-replace migrations across many files are trivial and should never be deferred. The source repeats an installer warning that an instruction template full of unfilled placeholders is worse than no instruction file, so it must be filled before the first run.

### Cost, portfolio framing, and first lines to build

The article claims a six-agent line running `8`–`12` full cycles per day costs about `$10`–`$15` per day in model usage, with a small desk computer and roughly `$4,400` per year for the factory. It also claims heavy sprints consuming more than a billion tokens have stayed under a couple thousand dollars including hosting when context is reused rather than resent; these are source-reported economics, not audited measurements.

Its illustrative `$1M` arithmetic is: `$83,333` per month, a focused product at `$49` per month, about `1,700` paying subscribers, `12` products per year, and roughly `142` customers per product; `$4,400` against `$1,000,000` is presented as under half a percent. The source says the only number to believe is whether one focused product can find `142` paying customers, cites solo operators reaching dozens of customers on niche products, and says a line creates twelve cheap, repeatable attempts rather than guaranteeing a hit. This math and all revenue/performance claims remain source-described.

The five first-line ideas are: Competitor watch (rival sites and ad libraries into reports and jobs); Directory (a searchable industry directory); Nightly fix (reads the error tracker, reproduces the top recurring failure, writes a fix and test, and leaves a pull request within gate limits); Content (research, drafting, editing, and publishing workers); and Product (one product idea per month with tests, a queue, and a rules file). The recommended first action is to create `QUEUE.md` with three jobs and let the schedule take the first at `08:00`. ^[raw/articles/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md]

This source-specific stack should not be collapsed into the earlier [[software-factory-with-claude-code]] seven-role chain: both use narrow roles and review, but Nazar emphasizes queue-first execution, worktree rooms, permission boundaries, fail-closed policy, self-updating Markdown memory, and a gate that separates safe auto-merges from human-owned paths. No named foundation model, version, runnable checker implementation, port allocator, database-branch mechanism, policy parser, ledger schema, or independent cost/performance evaluation is supplied. ^[raw/articles/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md]
## Related

- [[sairahul1]]
- [[claude-code]]
- [[vibe-coding]]
- [[claude-code-subagents]]
- [[dynamic-workflows-in-claude-code]]
- [[karpathy-claude-md]]
