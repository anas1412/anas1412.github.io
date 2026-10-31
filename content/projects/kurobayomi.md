---
title: "Kurobayomi - anime and manga on Linux and Windows"
date: 2026-10-29
draft: false
tags: ["product", "rust", "desktop"]
summary: "A native desktop app to watch anime and read manga: library, reader, video player, sources you add yourself, and AniList and MyAnimeList tracking."
repo: "https://github.com/kurobayomi/kurobayomi"
demo: "https://kurobayomi.github.io/"
tech: ["Rust", "GTK4", "mpv", "WASM"]
showDate: false
---

A desktop app in the spirit of Aniyomi: one library for your anime and manga, a reader and a video player built in, and progress that syncs to AniList or MyAnimeList.

![Kurobayomi welcome screen](https://raw.githubusercontent.com/kurobayomi/kurobayomi/main/docs/images/getting-started/01-welcome.png)

<div class="mt-8">{{< button href="https://github.com/kurobayomi/kurobayomi/releases/latest/download/Kurobayomi-Setup-x86_64.exe" >}}Download for Windows{{< /button >}} {{< button href="https://github.com/kurobayomi/kurobayomi/releases/latest/download/Kurobayomi-x86_64.AppImage" >}}Download for Linux{{< /button >}}</div>

## What it does

- **Your own files:** drop manga (CBZ, EPUB, image folders) and anime (MKV, MP4) into a folder and they join the library.
- **Sources you add:** paste a repository link and its sources appear. The app ships with none.
- **One search** across every source.
- **Built-in player** on mpv, with quality, subtitles, audio and a Skip button for openings.
- **Built-in reader:** left to right, right to left or long strip, per title.
- **Tracking** with AniList and MyAnimeList, updated as you read and watch.
- **Imports Aniyomi and Tachiyomi backups.**
- **Updates itself** in the background.

## Get it

- **Windows 10 and 11:** run the installer. No administrator prompt needed.
- **Linux:** make the AppImage executable and run it. Needs glibc 2.39 or newer (Ubuntu 24.04, Fedora 40, Arch).

```bash
chmod +x Kurobayomi-x86_64.AppImage
./Kurobayomi-x86_64.AppImage
```

---

{{< github repo="kurobayomi/kurobayomi" showThumbnail=false >}}
