---
title: Codex Master Guide
created: 2026-05-17
updated: 2026-07-11
type: concept
tags: [tools, agent, workflow, ai, automation, skills]
sources: [raw/articles/xarticle-nateherk-codex-master-guide-2051838770912129464.md, raw/articles/xarticle-how-i-build-apps-with-codex-without-opening-xcode-2040132557983936772.md]
related_entity: [[nate-herk]]
---

# Codex Master Guide

Comprehensive tutorial by [[nate-herk]] on mastering OpenAI Codex. Covers the full lifecycle from blank project to deployed, automated, self-QAing system in one hour.

## The Codex Mental Model

Codex is ChatGPT with local filesystem access, app building, browser automation, and mouse/keyboard control. Closest comparison is [[claude-code]] — same folder-based agent idea, different harness and model family.

- **Claude Code**: Opus, Sonnet, Haiku — better for exploratory thinking
- **Codex**: GPT-5.5, 5.4, etc. — more pragmatic, execution-heavy, stronger at long plans

Mindset shift: stop asking "which tool is best?" Start asking "which tool is right for this specific job?"

## Foundation: Project Setup

A project is just a folder. Codex can read, write, edit, organize, or move any file inside it.

### agents.md
The onboarding doc Codex reads every new chat. Equivalent to Claude Code's `claude.md`. Draft it by telling Codex the project goal in plain English. Sections: context, project goal, product direction, key constraints.

### Plan Mode
Codex brainstorms and plans without executing. Start every meaningful build here. Skipping plan mode is the single biggest reason builds go sideways.

### .env.local
Store API keys here. The dot-prefix tells Codex to exclude from public commits. Never paste keys into random `secrets.txt`.

## Building a Real Deliverable: YouTube Comment Intelligence

**Goal**: Pull 200 recent comments, analyze them, output Excel workbook with charts and creator insights.

**Process**:
1. Plan mode — Codex asks clarifying questions (how many comments, which videos, classification schema)
2. API setup — YouTube Data API v3 key via Google Cloud
3. Connection test — PowerShell failed (TLS), Node worked, Python worked
4. Save failure pattern to project memory so it never retries the broken path

**Workbook tabs**:
- Content category mix
- Tool mention rankings (Claude Code, Codex, API, etc.)
- Question rate, content-requested rate, high-priority items
- Frequent question patterns
- Reply opportunities by priority
- Content idea suggestions from comments
- Raw tab with all 200+ comments

**Lesson**: Vague prompts produce generic insights. Specificity about which patterns matter → more useful output.

## Skills: Reusable Recipes

Skills are markdown files in the `.codex/` folder.

- **Global**: user-level `.codex/` — available in every project
- **Project-level**: inside the project — scoped to that folder
- **Invocation**: slash command (`/youtube-comment-insights`) or natural language

Analogy: chocolate chip pancakes. First time you follow the recipe to a T. Next time you grab the same recipe. Tweak and update — the skill sharpens every use.

## Localhost → Live URL

**Stack**: GitHub + Vercel

1. Connect Codex to GitHub (one CLI auth)
2. Create private repo, push dashboard codebase
3. Connect Vercel to same GitHub account
4. Import repo into Vercel
5. Click deploy → live URL in ~30s

**Killer detail**: every push triggers auto-deploy. Work in Codex → push to GitHub → Vercel updates live site. Three tools, one workflow.

## Weekly Automations

Codex Automations tab = scheduled chats on cron.

**Example**: Every Sunday 5pm — pull fresh comments, update Excel, refresh dashboard, push to GitHub, Vercel auto-deploys.

**Gotchas**:
- **File locks**: Excel open on desktop → Codex can't overwrite. Close it first.
- **Model picker doesn't inherit**: Automation defaults to GPT-5.2 (slow). Must explicitly set GPT-5.5 high per automation.
- **Local only**: Machine must stay on. For 24/7, use cloud (Claude Code has cloud routines; Codex doesn't yet).

## Browser Use as QA Loop

Codex opens dashboard in in-app browser, clicks around, tries to break it, reports issues.

**Six issues found autonomously**:
- External YouTube links not opening in new tab
- Empty explorer state too bare
- Search too literal, no fuzzy matching
- Active tab state visual-only, not accessible
- Two minor UI inconsistencies

**Pattern**: bake QA pass into skill/project memory. Agent tests its own output before returning to user. Stops you from being the QA tester.

**Other browser uses**:
- Log into tools without APIs
- Pull reports from dashboards that don't expose data
- Automate any UI describable in natural language

## Quality-of-Life Details

- **Pet**: animated progress indicator (Codex, Dewey, Sadie, BSOD, Stacky, Fireball)
- **Side chat**: parallel thread, same project context, close when done
- **Personality**: Friendly or Pragmatic (recommended: Pragmatic — concise, direct)
- **Slash menu**: `/personality`, `/pets`, `/skills`, `/browseruse`, `/pdf`, `/skillcreator`
- **@ mention**: tag specific files or plugins in prompts
- **Session bar**: context window usage + remaining limits (5-hour, weekly)
- **Full access mode**: skips approval prompts. Start default, switch once project is trusted.

## Apple app-development variant

[[paul-solt]]'s workflow applies the same context-and-verification logic to iPhone and Mac projects. The project is made agent-friendly through [[appcreator]], a `Makefile`/`xcodebuild` build surface, `xcbeautify`, separate unit/UI test targets, runtime logs, and local Apple documentation. The distinction is useful: [[codex-master-guide]] describes the general agent lifecycle, while [[agent-friendly-xcode-projects]] describes the deterministic substrate that makes an Xcode project legible to the agent.

## Core Principle

Codex is not magic. First builds hit issues. First automations run slow. First skills aren't perfect. Treat every failure as golden knowledge — save the lesson to project memory. The system gets smarter every time you use it.

> "That folder is portable. Open it in Codex, Claude Code, OpenClaude, Cursor, or anything else that speaks markdown. The harness changes. The work doesn't."

## Related Concepts

- [[claude-code-workflows]] — Parallel CLI-agent patterns in the Claude ecosystem
- [[ai-design-workflow]] — Design-to-code pipeline using Claude Design
- [[vibe-coding]] — Broader paradigm of AI-assisted coding
- [[personal-ai-infrastructure]] — OS-layer architecture for persistent agent sessions
- [[codex-gpt-5-5]] — Entity page for the Codex model
- [[agent-friendly-xcode-projects]] — Apple-specific build/test substrate
- [[paul-solt]] — source author for the Apple workflow
