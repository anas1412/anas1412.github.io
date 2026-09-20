---
title: "Asia Range Breakout Backtester"
date: 2026-08-17
draft: false
tags: ["trading", "python", "backtesting"]
summary: "A Python and FastAPI backtester for an Asia-session opening-range breakout on gold, M1."
repo: "https://github.com/anas1412/orb-backtest-script"
demo: "https://orb-backtest-script--anasbassoumi1.replit.app/"
tech: ["Python", "FastAPI", "pandas"]
showDate: false
---
Marks the high and low of the first N minutes after a configurable session open,
then tests breakouts of that range on M1 gold. Default is 00:00 UTC, 15 minutes.

## Why

Session strategies live or die on timezone handling. Everything here operates in
UTC internally, so the results don't shift twice a year.

## Stack

Pure-Python engine with a FastAPI dashboard on top.

## Get it

```bash
python3 run.py
```

Creates the venv, installs deps and serves on `http://localhost:8000`.

## Screenshot

![orb-backtest-script](https://raw.githubusercontent.com/anas1412/orb-backtest-script/main/docs/screenshot.png)

---

[Source](https://github.com/anas1412/orb-backtest-script) · [Live](https://orb-backtest-script--anasbassoumi1.replit.app/)
*Python, FastAPI, pandas*
