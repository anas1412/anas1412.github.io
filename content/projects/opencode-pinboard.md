---
title: "Pinboard"
date: 2026-07-06
draft: false
tags: ["tooling", "bun", "react"]
summary: "A local ticket workspace for opencode - turns AI coding sessions into tickets, worktrees and PRs."
repo: "https://github.com/anas1412/opencode-pinboard"
demo: "https://anas1412.github.io/opencode-pinboard/"
tech: ["Bun", "React", "Fastify", "SQLite", "Electrobun"]
showDate: false
---

Tickets, git worktrees and pull requests for AI coding sessions, running locally.

![opencode-pinboard](https://raw.githubusercontent.com/anas1412/opencode-pinboard/main/public/OG-preview.png)

<div class="mt-8">{{< button href="https://anas1412.github.io/opencode-pinboard/" target="_blank" >}}Open the live version{{< /button >}}</div>

## Why

An agent session is a unit of work. Treating it like one - with a ticket, a
branch and a PR - makes it reviewable instead of disposable.

Not affiliated with opencode; built by a user, not the team.

## Get it

```bash
curl -fsSL https://raw.githubusercontent.com/anas1412/opencode-pinboard/main/pinboard.sh | bash
```

There's a compiled installer binary on the releases page too.

---

{{< github repo="anas1412/opencode-pinboard" showThumbnail=false >}}
