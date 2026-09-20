---
title: "FundingPips Trade Copier"
date: 2026-06-09
draft: false
tags: ["trading", "go", "propfirms"]
summary: "Copies positions and pending orders from a master account to any number of slaves on FundingPips MatchTrader."
repo: "https://github.com/anas1412/fp-mtr-tradecopier"
tech: ["Go", "MatchTrader"]
showDate: false
---

Copies trades - positions and pending limit/stop orders - from one master
account to one or more slave accounts on the FundingPips MatchTrader platform.

## Why

Passing the same challenge on several accounts means placing the same trade
several times, by hand, fast enough that the fills still match. That is exactly
the kind of work that should not be manual.

## Get it

Needs Go 1.22+.

```bash
git clone git@github.com:anas1412/fp-mtr-tradecopier.git
cd fp-mtr-tradecopier
bash install.sh
```

Fetches dependencies and builds the `copier` binary.

## Stack

Go, against the MatchTrader platform API.

---

{{< github repo="anas1412/fp-mtr-tradecopier" showThumbnail=false >}}
