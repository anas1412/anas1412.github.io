---
title: "20 October 2022"
date: 2022-10-20
draft: false
tags: ["trading", "beginnings"]
series: ["Getting Funded"]
series_order: 1
summary: "The day I opened a trading account, and the engineering instinct I had to unlearn before anything else."
---

20 October 2022 is the date on the account.

I was still an engineering student. A few weeks earlier I had finished a
DevOps internship, a summer spent building deployment pipelines and watching
dashboards. That kind of work teaches a very specific confidence: systems are
deterministic. Something breaks, you read the logs, you find the cause, you
fix it, and it stays fixed.

I walked into the market carrying that confidence. It was the wrong tool.

{{< figure src="/images/funded/19.jpg" alt="Merchants gathered in the arcaded courtyard of the old Amsterdam exchange" caption="Job Berckheyde, *The Courtyard of the Old Exchange in Amsterdam*, late 1600s. People have been trying to read markets in rooms like this for four hundred years. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Berckheyde,_Job_Adriaensz.%E2%80%94Binnenplaats_van_de_Oude_Beurs_te_Amsterdam_na_1668%E2%80%94c.1670%E2%80%94Museum_Boijmans_Van_Beuningen%E2%80%941043_%28OK%29%E2%80%94WD_item_Q19924911.jpg)." >}}

## A system with no bug

Markets look like systems. There are inputs and outputs, and patterns that
seem to repeat. So the engineer's instinct is to debug: find the setup that
works, remove the one that does not, and ship.

But the same setup that paid on Tuesday loses on Wednesday, and nothing is
broken. There is no stack trace, because there is no bug. A market is not
deterministic. The most you can hold is an
[[01-introduction-the-rider-s-quest-to-the-edge|edge]]: an advantage that
shows up across many trades and is invisible in any single one.

That was hard to accept, because every loss felt like a defect I should have
been able to find.

## Entries were not where the money went

I spent my first months on entries. Which pattern, which confirmation, which
candle. It took far too long to see that entries were not where the result
was being decided.

{{< chart >}}
type: 'line',
data: {
  labels: ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'],
  datasets: [
    { label: 'Takes every loss at 1R', data: [0,2,1,0,2,1,3,2,1,3,5,4,3,5,4,6,5,4,6,5,7], borderWidth: 2.5, tension: 0.2, pointRadius: 0 },
    { label: 'Lets four losses run to 3R', data: [0,2,1,-2,0,-1,1,-2,-3,-1,1,-2,-3,-1,-2,0,-3,-4,-2,-3,-1], borderWidth: 2.5, tension: 0.2, pointRadius: 0, borderDash: [6,4] }
  ]
},
options: { scales: { x: { title: { display: true, text: 'Trade' } }, y: { title: { display: true, text: 'Cumulative R' } } } }
{{< /chart >}}

*An illustration. Twenty identical trades, nine winners and eleven losers,
the same entries and the same winners for both. One trader takes every loss
at 1R. The other holds four of them to 3R, hoping they come back. One finishes
at +7R, the other at -1R.*

Nothing about the entries changed. The difference was four decisions, made in
the minutes when a position was going wrong.

| What I focused on | What actually moved the number |
|---|---|
| finding the right setup | how much I lost when I was wrong |
| being right more often | whether the winners outweighed the losers |
| more indicators, more confirmation | taking the same trade the same way every time |
| the trade in front of me | the next thousand |

## Why this is the first post

Because the beliefs matter more than the details. Everything I have written
since about [[11-the-engine-of-progress-discipline-consistency-and-reflection|discipline]],
[[12-the-great-battle-delayed-vs-instant-gratification|delayed gratification]]
and [[13-thinking-paradigms-process-probability-and-beyond-dualism|thinking in probabilities]]
started here. Not from reading about them. From being on the wrong side of
each one, with money attached.

The useful thing about a beginning is not what you did. It is what you
believed, so you can watch it break.
