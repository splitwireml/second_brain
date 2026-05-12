---
updated: 2026-04-17
title: kevinnguyendn — Obsidian + ByteRover (2026-04-13)
source: https://x.com/kevinnguyendn/status/2043567698253427144?s=46&t=T9l90q-jwkdpKALhZFMoiQ
type: post
---

# kevinnguyendn — Obsidian + ByteRover (2026-04-13)

- URL: https://x.com/kevinnguyendn/status/2043567698253427144?s=46&t=T9l90q-jwkdpKALhZFMoiQ
- Tweet ID: 2043567698253427144
- Author: @kevinnguyendn (andy nguyen)
- Created at: 2026-04-13 05:51:21 UTC
- Captured: 2026-04-13
- Article title: Obsidian + ByteRover: Your Personal Knowledge Base Now Lives Inside Every AI Coding Agent

## Source text

Obsidian + ByteRover: Your Personal Knowledge Base Now Lives Inside Every AI Coding Agent

You’ve spent months, maybe years building a second brain in Obsidian. It’s packed with architecture decisions, design sketches, and deep-dive research on things like authentication patterns.

But there’s a problem: The moment you open a coding agent like Claude Code, Cursor or Codex, that knowledge vanishes. When you ask your agent to refactor a module, it has no idea you’ve already documented the exact trade-offs and strategies required. Your personal notes and your codebase live in two completely different worlds.

ByteRover finally bridges that gap.

## The Structural Accident That Makes It Work

ByteRover doesn't need a complex bridge because it shares the same DNA as Obsidian. Both systems are built on a simple, zero-infra philosophy:

- Directories of Markdown files with YAML frontmatter, organized into folders, with no database.
- No proprietary format, no binary blobs, no encoding layer. Just .md files on disk.

Because your vault is structurally identical to a ByteRover Context Tree, ByteRover can treat your notes as a native knowledge source.

## Why This Changes Your Workflow

Using the ByteRover source feature (released in ByteRover CLI v3.2.0), you can now link your Obsidian vault as a read-only knowledge source:

- Federated Search: Search across your vault knowledge and your project code in a single query.
- Scale with Every Project: You can link the same curated vault to every project you own. Curate once and search from everywhere.
- Universal Support (by connecting to 22+ coding agents): Your vault becomes available to 22+ coding agents (including Claude Code, Cursor, Windsurf and more) with zero extra configuration.
- Read-Only Safety: Agents can read and learn from your notes to give better suggestions, but they can never modify or delete your vault content.
- Zero Friction: You don’t need Obsidian running. No plugins, no REST APIs, and no API keys are required. It’s just Markdown on disk.

## Setup from source

Step 1 — Initialize ByteRover in your vault

```bash
cd ~/Documents/MyVault
brv
```

Running brv starts the TUI for initial setup. Use /providers to set up your LLM and /connectors to link your favorite coding agent. Once done, run /exit.

Note: ByteRover creates a .brv/ directory. If you want it invisible in Obsidian, add .brv to your .obsidianignore file.

Step 2 — Curate your vault knowledge

```text
> curate the knowledge from ./Architecture/ to context tree
> curate all notes from ./Decisions/ to context tree
> curate the knowledge from ./Design/api-design.md to context tree
```

The agent extracts the knowledge and writes it into .brv/context-tree/, making it structured, indexed, and searchable.

Step 3 — Link the vault to your project

```bash
cd ~/code/my-project
brv source add ~/Documents/MyVault
```

ByteRover validates the link and registers it as a read-only source. Verify with `brv source list`.

Step 4 — Search across everything

```bash
brv search "authentication flow"
brv query "What did we decide about the auth refresh token strategy?"
```

## Repo and release verification

Confirmed separately from GitHub API on 2026-04-13:

- Repo: `campfirein/byterover-cli`
- Description: ByteRover CLI (`brv`) — portable memory layer for autonomous coding agents
- Homepage: https://docs.byterover.dev/
- GitHub stars at capture time: 4,461
- Release tag: `v3.2.0`
- Release published: 2026-04-11T04:16:59Z
- Release highlights confirmed: `brv source add <path>`, cross-project read-only knowledge sources, git-style worktree links, resolver-aware `brv status`

## Extraction notes

Confirmed:
- The X post is a long-form article/tweet by @kevinnguyendn promoting ByteRover CLI v3.2.0’s source-linking workflow for Obsidian vaults.
- The post explicitly frames Obsidian vaults as structurally compatible with ByteRover’s markdown-based context tree.

Likely:
- The “22+ coding agents” support count is a product claim from the post and was not independently enumerated here.
- The “5 minutes” setup time is marketing framing rather than independently verified timing.

Speculative:
- None beyond the author’s own forward-looking workflow claims.