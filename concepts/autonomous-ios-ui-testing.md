---
title: Autonomous iOS UI Testing
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [agent, platform, product, project]
sources: [raw/articles/flowdeck-autonomous-ios-testing.md]
---

# Autonomous iOS UI Testing

## Overview

Using Claude Code as an autonomous QA agent for iOS apps via **FlowDeck** — a CLI tool that gives agents direct access to the iOS simulator with screenshot, accessibility tree, tap, swipe, type, and assert commands.

## The Gap Claude Code Fills

Claude Code can write XCTest cases but cannot natively:
- Navigate screens or tap buttons
- Verify visual state
- See what actually happened on screen

FlowDeck bridges this by providing structured JSON output of the accessibility tree and simulator control commands.

## How It Works

1. **See** — `flowdeck ui simulator screen --json` returns screenshot + accessibility tree
2. **Act** — `tap`, `swipe`, `type` commands target elements by label (not coordinates)
3. **Verify** — `assert visible` confirms expected state
4. **Repeat** — Agent loops through test scenarios autonomously

**Key advantage over XCUITest:** Uses accessibility tree labels, not coordinates. Survives UI changes, works across screen sizes, requires zero test code maintenance.

## Demo Results

A weather app tested autonomously in 16 minutes with one prompt:
- All screens reviewed for layout issues
- All features tested end-to-end (add/remove cities, check forecasts, switch locations)
- **Bug found and fixed:** City removal index bug — traced to source, patched, verified
- Edge cases tested (malformed input, rapid operations)
- UX observations flagged (not forced as fixes)
- Full summary report generated

## Why This Matters

**Not a replacement** for unit tests or critical path XCUITest coverage. It's the exploratory pass that never happens because nobody has time — the "does this actually work end to end" sweep.

**Time investment:** One prompt, 16 minutes vs hours of writing and maintaining test code.

**Relevance to our projects:** The [[football-simulation-engine]] project targets iOS eventually. Autonomous UI testing would be valuable for validating the simulation interface without manual QA.

## FlowDeck Product

- **Price:** $59/yr after free trial
- **Install:** `curl -sSL https://flowdeck.studio/install.sh | sh`
- **Claude Code integration:** Skill pack installs via `flowdeck -i` → Install Skills → Claude Code → Global
- **Commands:** screen, tap, type, swipe, assert, logs

## Related

- [[research-code-agent-cli-automation]] — Claude Code's CLI capabilities and limitations
- [[football-simulation-engine]] — Future iOS app that would benefit from autonomous testing
- [[prompt-engineering-patterns]] — The testing prompt pattern (act as QA engineer, enumerate steps, fix bugs, report)
