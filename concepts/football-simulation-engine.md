---
title: Football Simulation Engine
created: 2026-04-09
updated: 2026-04-09
type: concept
tags: [project, agent, model, rl, deep-learning]
sources: [raw/articles/football-simulator-engine-plan.md]
---

# Football Simulation Engine

## Overview

Design for an autonomous football simulation engine that moves beyond simple RNG (like Top 11) to realistic, logic-driven decision making. The goal is a simulator that is fair, interesting, and captures the nuance of tactics (e.g., possession vs. counter-attack).

## Architecture Models

Two primary approaches are being explored:

1.  **Entity Interaction Model:** Players exist as autonomous entities in a loop. Interactions are resolved via an interaction model between players and the world.
2.  **RPG-Style Choice Model:** At any given moment, the ball carrier has discrete choices (pass, shoot, move). Accumulative choices determine the match flow.

**Active Actors:** All players make decisions, but the ball carrier and closest opponents are "active" (making immediate decisions), while others react to stimuli.

## Logic & Stimuli

### Defensive Logic
Defenders process inputs to decide between three actions: **Hold position**, **Cut passing lane**, or **Close in**.
*   **Stimuli:** Distance to ball, nearest man, distance between ball carrier and nearest opponent.

### Offensive Logic
Teammates process inputs to decide between: **Hold position**, **Supportive position**, or **Offensive position**.
*   **Stimuli:** Distance to ball carrier, distance to goal (own and opponent), proximity of opposition.

## Implementation (3v3 Prototype)

-   **Grid System:** Simplified 2D grid representation.
-   **Neural Network Agents:** Each player is a neural network agent.
    -   *Inputs:* Fixed-order vector of distances and positions (goals, teammates, opponents).
    -   *Outputs:* Classification of actions (pass, shoot, take-on, move).
-   **Interaction Model:** Skill-based weighted RNG for duels (e.g., Dribbling skill vs Tackling skill determines probability).

## Training & Tactics

-   **Reinforcement Learning (RL):** Agents are trained to adopt specific styles (e.g., possession-based teams are rewarded for short passing).
-   **Chemistry:** Variable based on player compatibility.
-   **Hardware Constraint:** Investigating if iOS devices (iPhone/iPad) can support active training and strategy adjustment for a distributed game model.

## Related Concepts

- [[prompt-engineering-patterns]] — Could be used to generate strategic instructions for the agents.
- [[vibe-kanban-agent-spawning]] — Relevant if using agent orchestration tools to run the simulation at scale.
