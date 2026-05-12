---
updated: 2026-04-19
title: "How Checkpoints and /rollback make Hermes safer to use on real work"
author: "Neo"
username: "@NeoAIForecast"
created: "2026-04-17"
source: "https://x.com/NeoAIForecast/status/2045097742935195775"
type: "xarticle"
tags: []
---


# How Checkpoints and /rollback make Hermes safer to use on real work

How Checkpoints and /rollback make Hermes safer to use on real work

Most AI agent demos focus on what the agent can do. Write code. Refactor files. Run shell commands. Modify a project in seconds.

That part is easy to show.

The harder question is what happens when the agent does the wrong thing.

That is where a lot of AI tooling still feels immature. It can act, but it does not always give you a clean, native way to recover when the action was wrong.

Hermes approaches that problem differently.

One of its most underrated features is checkpoints and /rollback: a built-in recovery system that snapshots your project before destructive changes and lets you restore that state from inside the same Hermes session.

That might sound like a small convenience feature.

It is not.

It changes the trust model of using an agent on a live codebase, config directory, or active project. And it says something important about how Hermes is designed: not just for capability, but for recoverability.

Takeaway: An agent becomes far more usable the moment “try it” is no longer the same thing as “risk everything.”

## What problem this solves

The moment an AI agent can touch your filesystem, the stakes change.

You are no longer judging it only as a text generator. You are judging it as an operator.

That creates a new set of concerns:

- What if it patches the wrong file?

- What if it rewrites something correctly in syntax but incorrectly in intent?

- What if it runs a destructive shell command?

- What if the conversation keeps moving as though the change was valid, even after you want it undone?

This is where many agent systems become awkward in practice.

They may be powerful enough to make changes, but the recovery path still lives outside the product:

- use Git manually

- remember what changed

- diff things yourself

- run reset commands carefully

- mentally reconcile the conversation with the real state of the files

Hermes closes that gap with a native mechanism built directly into the workflow.

Hermes automatically creates checkpoints before destructive operations, then exposes them through the /rollback command so you can inspect and restore from within the same environment.

That is a much stronger design than treating recovery as something the user handles later.

Takeaway: Hermes does not assume agent mistakes are impossible. It assumes they should be reversible.

## What Hermes actually does

Hermes’ checkpoints are enabled by default and activate automatically when the agent is about to make a destructive change.

The triggers include:

- file tool writes via write_file

- edits via patch

- destructive terminal commands such as:

- rm

- mv

- sed -i

- truncate

- shred

- output redirects like >

- Git commands such as git reset, git clean, and git checkout

Hermes also limits noise by creating at most one checkpoint per directory per turn, so long sessions do not produce excessive snapshot spam.

That balance matters.

A recovery system only helps if it is automatic enough to be used consistently, but restrained enough not to become operational clutter.

Hermes appears to aim for exactly that: default-on safety without constant interruption.

## How the feature works under the hood

This is where the feature becomes especially Hermes-like.

Hermes does not use your real project .git history as its checkpoint store.

Instead, it keeps a separate shadow git repository under:

> ~/.hermes/checkpoints/

Each working directory gets its own shadow repo. Before a destructive file mutation happens, Hermes snapshots the current state there, with a short human-readable reason describing what triggered the checkpoint.

At a high level, it flows like this:

1. Hermes detects that a tool is about to mutate files.

2. It resolves the project root or working directory involved.

3. It initializes or reuses a shadow repo tied to that directory.

4. It stages and commits the current state.

5. It lets the file mutation proceed.

6. If needed later, you inspect or restore via /rollback.

That design choice is important for a few reasons.

First, it avoids polluting your real repository history. Your actual branch, commits, and workflow remain yours.

Second, it gives Hermes an agent-specific recovery layer. This is not version control in the broad sense. It is a purpose-built undo system for agent-driven mutations.

Third, it lowers the friction of experimentation. You can let Hermes take action knowing the recovery path is built around the same operating model.

Takeaway: Hermes adds a parallel safety history for agent actions instead of forcing every recovery decision through your main Git history.

## Why this matters operationally

A lot of people are comfortable asking an agent to explain a file. Fewer are comfortable asking it to change ten files. The difference is not just model quality. It is safety.

Checkpoints and rollback shift that boundary.

Once you know Hermes snapshots before destructive operations, the agent becomes much more practical for work like:

- multi-file refactors

- config rewrites

- batch documentation edits

- project cleanup tasks

- shell-assisted maintenance

- rapid iterative fixes where the first try may not be right

This does not make the agent perfect. What it does is reduce the downside of being wrong.

That may be the single most important change an agent runtime can make. In real use, useful systems are rarely the ones that never fail. They are the ones that fail in ways you can recover from quickly, locally, and confidently.

Hermes clearly treats that as a product requirement, not an afterthought.

## The commands that matter

The core interface for this feature is simple.

Inside a Hermes session, you can list checkpoints with:

> /rollback

You can restore a checkpoint with:

> /rollback 1

You can preview the diff first with:

> /rollback diff 1

And you can restore a single file from a checkpoint with:

> /rollback 1 src/broken_file.py

That single-file restore is especially useful. Many agent mistakes are not total failures. Sometimes the agent got four changes right and one wrong. In that case, you do not want a blunt-force reset.

You want selective recovery. Hermes supports that.

A simple session flow might look like:

```bash
hermes
```

Then inside Hermes:

```plaintext
/rollback
/rollback diff 1
/rollback 1
```

And if you want to check or edit the feature’s configuration:

```bash
hermes config edit
```

With the relevant section:

```yaml
checkpoints:
  enabled: true
  max_snapshots: 50

```

That is part of what makes the feature strong: the commands are simple enough to become normal workflow, not emergency-only knowledge.

## The smartest detail: rollback also fixes chat state

This is the most important part of the design, and the easiest one to miss. When Hermes restores from a checkpoint, it does not only restore files.

It also undoes the last conversation turn so the agent’s context matches the restored filesystem state. That solves a real problem in stateful agent systems.

Without this, you can end up in a broken condition where:

- the files are back to an earlier version

- but the conversation history still reflects the now-undone change

- so the model continues reasoning from a state that no longer exists

That kind of mismatch can poison the next several turns.

Hermes explicitly avoids it by treating rollback as both:

1. a filesystem recovery action

2. a context consistency action

That is a much deeper design than just “revert the files.”

It means Hermes understands that state is not only on disk. It is also in the live conversation.

Takeaway: Good rollback is not just about restoring files. It is about restoring alignment between files and agent context.

## Where this helps most

This feature becomes especially valuable in the workflows where AI agents are finally useful enough to be dangerous.

1. Multi-file edits

If Hermes touches several files during a refactor and one result is bad, rollback gives you a clean recovery path without manually reconstructing prior state.

2. Terminal-heavy operations

When the agent is using shell commands that move, delete, or rewrite content, checkpoints act as a buffer before those operations land.

3. Fast experimentation

You can let Hermes try a fix, inspect the result, and reverse course quickly if the path was wrong.

4. Long-lived sessions

Because Hermes carries context over time, mistakes can compound. Rollback helps keep the conversation and the working tree from drifting apart.

5. Lower-friction use for non-experts

Not everyone wants to manage AI-agent recovery through raw Git commands. Hermes gives users a native recovery interface inside the same product.

This is one of the clearest examples of Hermes behaving like an operating environment rather than just a prompt box.

## What this feature is not

It is also important to define the limits.

Checkpoints are not:

- a replacement for Git

- a substitute for branches or worktrees

- a full system backup solution

- a guarantee that every possible mutation is recoverable in every scenario

Hermes Agent frames checkpoints as a filesystem safety net for destructive operations, not as the only recovery mechanism you should rely on.

In fact, one of the best practices is to combine checkpoints with Git worktrees for additional protection.

That is the right model:

- Git is still your primary version-control system

- Hermes checkpoints are the fast, agent-native recovery layer around live mutations

Those two systems complement each other well.

## Final takeaway

Checkpoints and /rollback are one of the clearest examples of Hermes being built for real operator use.

Hermes does not just let an agent edit files. It wraps destructive work in a recovery model:

- snapshot before mutation

- store recovery history in a shadow repo

- preview diffs before restore

- support full or single-file rollback

- realign conversation state with restored file state

That is not just a nice feature. It is a trust feature.

And in systems that can take real action, trust features are often more important than flashy ones.

Hermes is more useful because it is reversible. That is what checkpoints and /rollback make possible.
