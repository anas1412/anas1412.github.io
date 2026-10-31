---
title: "Tackora - a team board for coding agents"
date: 2026-10-15
draft: false
weight: 5
tags: ["product", "ai-agents", "rust"]
summary: "Your team's coding agents on one board: Claude Code, Codex, OpenCode and Gemini CLI run on your own machines and end in a pull request."
repo: "https://github.com/anas1412/tackora"
tech: ["Rust", "Axum", "Postgres", "React"]
showDate: false
---

A shared board for the coding agents a team already uses. Every ticket is one agent session: pick the agent and the machine, watch it work, answer it when it asks, review the pull request it opens.

Agents run on your own machines through a small runner started with `npx`, so code, keys and sign-ins never leave them.

## Get it

```bash
npx tackora@latest start
```
