---
title: projects.md
created: 2026-05-04
updated: 2026-05-04
type: entity
tags: [agent-tool, prompt-engineering, claude-code, hermes-agent]
sources: [raw/articles/projects-md-mr_r0b0t-2049682402386039256.md]
---

# projects.md

Single-markdown-file project management system for AI coding agents. The project file IS the project — a structured markdown document containing everything: current state, requirements, decisions, tasks, and session log. A Rust CLI (`projectsmd`) manages the file.

**Author:** mr_r0b0t

**Stack:** Built with Hermes Agent running Xiaomi MiMo V2.5-Pro. Inference sponsored by Xiaomi.

**Language:** 95.2% Rust.

**Influenced by:** GSD (get-shit-done) and [obra/superpowers](https://github.com/obra/superpowers).

---

## Core Principle

> One file. One binary. The file is the project. The binary manages the file.

Traditional project management spreads context across heads, Slack, Jira, and Google Docs — it evaporates when the session ends. projects.md preserves all context in one file that restores instantly at the next session start.

---

## File Structure

Every `project.md` contains:

- **What This Is / Core Value** — project definition
- **Requirements** — three-tier system (prevents silent scope creep)
- **Current State** — the resume point: phase, last action, next action; an agent/human reading ONLY this section can pick up immediately
- **Key Decisions** — logged with rationale and outcome (✓ Good / ⚠️ Revisit / — Pending)
- **Tasks** — phase-grouped checklist (DEFINE → DESIGN → BUILD → VERIFY → SHIP)
- **Discoveries / Session Log** — accumulated learning across sessions

---

## Requirements Lifecycle

Requirements move through tiers (not just done/not-done). If something didn't work, it moves to Out of Scope with a reason — preventing silent retry of failed approaches.

---

## Agent Integration

1. `projectsmd skill install` — install the skill
2. Agent discovers the skill (progressive disclosure)
3. Agent reads `project.md` at session start
4. Agent uses `projectsmd` CLI commands during work
5. Agent runs `projectsmd session` at end

Framework-agnostic: works with Hermes Agent, Claude Code, Cursor, Codex, or any agent supporting the agentskills.io standard.

---

## Related

- GSD (get-shit-done) — prior art: meta-prompting + context engineering + spec-driven development for Claude Code; projects.md builds on its ideas
- Hermes Agent — primary runtime used to build projects.md
- [[skillify]] — Garry Tan's methodology for converting agent failures into tested skills
- [[claude-code-systems-design]] — shift from prompt-based to system-design-based Claude Code usage
