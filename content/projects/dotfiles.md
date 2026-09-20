---
title: "dotfiles"
date: 2026-09-15
draft: false
tags: ["linux", "ricing"]
summary: "Tokyo Night on Arch (CachyOS) with KDE Plasma 6 on Wayland, managed with GNU Stow."
repo: "https://github.com/anas1412/dotfiles"
tech: ["Fish", "Kitty", "Kvantum", "GNU Stow"]
showDate: false
---
Tokyo Night across the whole desktop — Plasma 6 on Wayland, Kitty, Fish, Kvantum.

Managed with GNU Stow so each config is a symlink farm rather than a pile of
copies. Same palette as this site.

## Get it

```bash
sudo pacman -S stow
git clone https://github.com/anas1412/dotfiles ~/dotfiles
cd ~/dotfiles
./install.sh
```

Or just some of it: `./install.sh fish kitty`. Stow refuses rather than
overwriting an existing config — move the old one aside and re-run.

## Screenshot

![dotfiles](https://raw.githubusercontent.com/anas1412/dotfiles/main/screenshot.png)

---

{{< github repo="anas1412/dotfiles" showThumbnail=false >}}
