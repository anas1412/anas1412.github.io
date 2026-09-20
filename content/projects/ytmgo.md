---
title: "ytmgo"
date: 2026-09-17
draft: false
tags: ["go", "cli", "music"]
summary: "A terminal YouTube Music client in Go — search, queue, bookmark and play without leaving the keyboard."
repo: "https://github.com/anas1412/ytmgo"
demo: "https://anas1412.github.io/ytmgo/"
tech: ["Go", "yt-dlp"]
showDate: false
---

A YouTube Music client that lives in the terminal. Search, download audio,
manage a play queue, bookmark favourites, and play — all from the keyboard.

![ytmgo](https://raw.githubusercontent.com/anas1412/ytmgo/main/ytmgo.png)

![ytmgo](https://raw.githubusercontent.com/anas1412/ytmgo/main/screenshot-catppuccin.png)

<div class="mt-8">{{< button href="https://anas1412.github.io/ytmgo/" target="_blank" >}}Open the live version{{< /button >}}</div>

## Why

Every music client wants to be a browser tab. If the rest of my work happens in
a terminal, the music should too.

## Stack

Written in Go, MIT licensed. The most-starred thing I've published.

## Get it

```bash
curl -fsSL https://raw.githubusercontent.com/anas1412/ytmgo/main/install.sh | bash
```

Detects your system: on Arch it installs `ytmgo-bin` via `paru` or `yay`,
elsewhere it pulls the static binary and its deps. Nothing compiles unless you
ask. From source instead:

```bash
go build -o ytmgo . && ./ytmgo
```

`Tab` focuses search, `Enter` queues a result, `↑↓`/`jk` move.

---

{{< github repo="anas1412/ytmgo" showThumbnail=false >}}
