---
title: "ORB for MetaTrader 5"
date: 2026-09-16
draft: false
tags: ["trading", "mql5", "python"]
summary: "A configurable opening-range breakout EA for MT5, with a reproducible research harness behind it."
repo: "https://github.com/anas1412/orb-mt5"
demo: "https://anas1412.github.io/orb-mt5/"
tech: ["MQL5", "Python", "MetaTrader 5"]
showDate: false
---

An opening-range breakout expert advisor where **every parameter is an input** - any session, any range length, any signal timeframe, any symbol. Daylight saving
is handled properly, which is where most session-based strategies quietly break.

<div class="mt-8">{{< button href="https://anas1412.github.io/orb-mt5/" target="_blank" >}}Open the live version{{< /button >}}</div>

## Why

Backtests that can't be reproduced aren't research, they're anecdotes. This ships
the harness alongside the EA so a result can be re-run.

```bash
python3 orb.py compile      # build the EA
```

## Stack

MQL5 for the EA, Python for the harness. Runs on Windows and on Linux under Wine.

## Get it

Copy `mql5/` into your terminal's data folder (**File → Open Data Folder**),
compile, and attach to an **XAUUSD M1** chart. The panel starts off.

| From the repo | Goes to |
|---|---|
| `mql5/ORB.mq5` | `MQL5/Experts/` |
| `mql5/CheckBrokerOffset.mq5` | `MQL5/Scripts/` |
| `mql5/TimeZones.mqh` | `MQL5/Include/` |
| `mql5/Panel.mqh` | `MQL5/Include/` |

```bash
python3 orb.py compile     # or F7 in MetaEditor
```

Releases ship source, not a compiled `.ex5`.

---

{{< github repo="anas1412/orb-mt5" showThumbnail=false >}}
