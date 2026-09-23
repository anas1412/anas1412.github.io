# CLAUDE.md

Personal site for Anas Bassoumi. Hugo + the Blowfish theme, deployed to GitHub
Pages on every push to `main`. Live at <https://anas1412.github.io>.

## Where everything is

| Path | What it holds |
|---|---|
| `content/` | **the Obsidian vault** - open this folder in Obsidian, not the repo root |
| `content/posts/` | all writing. One `.md` per post |
| `content/_index.md` | the homepage paragraph |
| `content/about.md` | experience, education, skills |
| `content/projects/` | one file per project |
| `content/trading/` | **generated** - one article per month, do not hand-edit |
| `scripts/sync_trades.py` | pulls the journal from Google Sheets |
| `scripts/data/trades.json` | committed snapshot, so builds work offline |
| `scripts/commons_image.py` | finds and fetches freely licensed images from Wikimedia Commons |
| `static/images/` | post images: `notes/` for the essay series, `funded/` for Getting Funded |
| `content/templates/post.md` | Obsidian template for a standalone post |
| `content/templates/series-post.md` | Obsidian template for a post in a series |
| `content/templates/project.md` | Obsidian template for a project |
| `config/_default/languages.en.toml` | name, headline, bio, social links, site title |
| `config/_default/params.toml` | `colorScheme` (15 options), dark mode, article display |
| `config/_default/menus.en.toml` | the navbar |
| `config/_default/hugo.toml` | baseURL, taxonomies, `ignoreFiles` |
| `archetypes/posts.md` | Hugo CLI template - filename must match the section folder |

The theme is a **Hugo Module**, not vendored code. Update with `hugo mod get -u`.
Never commit `_vendor/`.

## Commands

```sh
./scripts/build.sh serve    # preview on localhost:1313
./scripts/build.sh          # production build into public/
python3 scripts/test_wikilinks.py   # self-check for the converter
```

**Use the script, not bare `hugo`** - it converts wikilinks first. Bare `hugo`
builds fine but leaves `[[links]]` as visible brackets on the page.

Always build before committing. A malformed frontmatter value fails the
**entire site**, not just one page.

## Hard rules

These are all things that have already broken this site once.

- **Wikilinks are supported, but only through `scripts/build.sh`.** Running
  bare `hugo` renders `[[text]]` literally on the page with no error. Always
  build via the script.
- **Escape `"` inside frontmatter titles**, or the build dies with a YAML
  error and nothing deploys:
  `title: "The Peak of \"Mount Stupid\""`
- **Every post needs `title:`.** Without it Hugo publishes an untitled page - it does not fall back to the filename.
- **Never name a section after one of Anas's repos.** A repo named `x` serves
  at `anas1412.github.io/x/` and shadows that path on this site. `/notes/` is
  already taken this way - it belongs to a different repo.
- **`draft: true` is not privacy.** The post stays out of the build but the
  repo is public, so the file is still readable on GitHub.
- **`series:` is Hugo-only. `tags:` and `[[wikilinks]]` work in both.**
  Obsidian's graph draws edges from links and tags, and knows nothing about
  `series`.
- Blowfish warns it caps at Hugo 0.165 while we run 0.166. Benign - it builds
  correctly. Don't downgrade to silence it.

## Wikilinks

Write `[[wikilinks]]` normally - Obsidian's graph, autocomplete and backlinks
all work, and `scripts/wikilinks.py` converts them at build time.

**Source files are never modified.** The script copies `content/` to
`.wikilinks-build/`, converts there, and Hugo builds from the copy. What you
edit always stays in Obsidian's own syntax.

| You write | Becomes |
|---|---|
| `[[03-shadow-work]]` | link labelled with that post's `title:` |
| `[[03-shadow-work\|the shadow]]` | link labelled *the shadow* |
| `[[03-shadow-work#Some Heading]]` | link to `#some-heading` |
| `![[pic.png]]` | image, resolved from `static/` or `content/` |

Resolution is by **filename first, then frontmatter title** - the same order
Obsidian uses. Code spans and fenced blocks are skipped. A link that resolves
to nothing is left as-is and reported, never silently dropped.

Inside a markdown table write the alias pipe as `\|` - `[[note\|label]]` - exactly as Obsidian does. The converter unescapes it.

Check before pushing:

```sh
python3 scripts/wikilinks.py --check    # lists unresolved links, changes nothing
```

## Trading journal

`content/trading/_index.md` is **generated**. Edits to it are overwritten.
To refresh after logging trades:

```sh
python3 scripts/sync_trades.py     # fetch the sheet, rebuild the page
python3 scripts/sync_trades.py --local   # rebuild from the committed CSV
```

The sheets must stay link-viewable. The script reads **two journals**:

| Journal | Instrument | Tabs | Logs |
|---|---|---|---|
| gold | GOLD | 4 (gid 0 is an empty template, skipped) | dollars + R |
| trading edge | NQ | 7 | risk/return as percentages, no dollars |

They cover different periods, so together they run from January 2024.

**De-duplication is asymmetric, deliberately.** The gold tabs cover distinct
periods and several days hold two or three trades sharing one screenshot - so
gold is never de-duplicated. The NQ sheet is a master tab plus per-period
subsets that repeat it, so it is, on date + chart + result + R + notes.
Widening that key is what stops real same-day trades being collapsed.

Each tab's last rows are a TOTAL plus blank padding; the script drops them, so
`TOTAL trades` never leaks onto the page.

The tabs use three different outcome vocabularies. They are normalised to the
newest one:

| Older tabs | Becomes | Why |
|---|---|---|
| `Win` / `Loss` / `Breakeven` | `W` / `L` / `BE` | newest tab's spelling |
| `Tape Reading` | `missed` | no P&L, risk or RR - the trade wasn't taken |
| `Performance Mistake`, `Analysis Mistake` | `W`/`L`/`BE` by P&L | real trades; the label is prepended to the notes so it isn't lost |

The snapshot lives in `scripts/data/`, **not** `data/`: Hugo treats `data/` as
a data directory and fails the build trying to parse files there.

The script writes one article per month (`YYYY-MM.md`) plus `_index.md`, and
deletes any month file matching that pattern before regenerating - the sheet is
the source of truth, so hand edits are lost.

To change what the pages show, edit `month_page()` in the script, not the
markdown.

It is deliberately a **journal, not a dashboard** - no win rate, profit factor
or equity curve. Each month page is: a table of that month's trades for
scanning, then **one block per trade** - heading, the TradingView chart
inline, the note at full width - for re-reading.

Charts are hotlinked from TradingView's snapshot bucket:
`s3.tradingview.com/snapshots/<first letter, lowercased>/<ID>.png`, derived
from the `tradingview.com/x/<ID>/` share links in the sheet (`snapshot()` in
the script). 96% of trades have one. If that URL scheme ever changes, every
inline chart breaks at once - the `view` link in the table still works, and
the fix is one function.

## File naming

Posts are named `NN-slug.md` - a zero-padded two-digit number, then the title
slugified.

```
content/posts/03-shadow-work-making-the-unconscious-conscious.md
content/posts/18-conclusion-the-edge-of-transformation.md
```

- **`NN`** - two digits, zero-padded (`01`, not `1`). Always continue from the
  highest number already in `content/posts/`, **including for a series**. It is
  a filename counter, not the series position: with more than one series the two
  cannot match, and `series_order` is what orders a series. "Getting Funded"
  starts at file 19 with `series_order: 1`.
- **slug** - the title, lowercased, non-alphanumerics collapsed to single
  hyphens, no trailing hyphen. Keep it under ~60 characters.
- The number is part of the URL: `03-shadow-work-…` serves at
  `/posts/03-shadow-work-…/`.

**Renaming a file changes its URL** and breaks every existing link to it,
including `[[wikilinks]]` in other posts. Pick the name once. If you must
rename, add the old path to the post's frontmatter so the old URL keeps
working:

```yaml
aliases: ["/posts/old-slug/"]
```

## Writing a post

Frontmatter, matching `content/templates/post.md`:

```yaml
---
title: "Plain title, sentence case"
date: 2026-09-20
draft: false
tags: ["topic"]
---
```

Series posts add two more lines - use the **series-post** template, which
includes them:

```yaml
series: ["Notes from the Edge"]
series_order: 3
```

Change the series name and set `series_order` to the next free number in that
series. Blowfish renders the full part list on every post in it.

## Writing style

**Never use em dashes, en dashes, or emojis.** Not in prose, not in frontmatter, not in
commit messages. Where an em dash would go, use a spaced hyphen ( - ), a
comma, a colon, or a full stop. `scripts/sync_trades.py` strips em and en dashes from
sheet notes on every sync so the trading pages comply automatically.

**Clarity beats everything else.** If a sentence needs re-reading, rewrite it.

- **Show, don't tell.** A number, a screenshot, or a worked example instead of
  an adjective. Not "performance improved dramatically" - "p99 went from 840ms
  to 120ms."
- **Simple language.** Short words, short sentences. Cut jargon unless the
  reader needs the term itself.
- **Break up prose.** Bullet points and tables over paragraphs. If a paragraph
  runs past four or five lines, it is probably a list.
- **Visuals wherever they carry meaning** - see the shortcodes below. A diagram
  of a flow beats three paragraphs describing it.
- **Quote when the source says it better**, and attribute it. Don't pad with
  quotes that only decorate.
- No filler openers, no "in today's world", no summarising what you're about
  to say before saying it.

## Editing like a professional writer

When asked to write, rewrite or improve a post, work as a professional writer
and editor who has published books and articles. **Editorial licence is
unconstrained**: rewrite freely, restructure, retitle, cut whole sections, add
new ones, reorder arguments, add images, charts, tables and diagrams. The only
hard limits are the truth rules below and the house rules above.

Keep filenames unchanged when rewriting. Titles can change freely (wikilinks
resolve by filename), but the filename is the URL and other posts link to it.
Titles the author has set by hand stay unless he asks.

### How the rewrites are done

- **Open on something concrete**: a scene, a fact, a claim. Never a greeting,
  a preamble, or a summary of what is coming. "Greetings, Seeker" was cut for
  this reason.
- **One idea per post.** Every section serves it. If a paragraph restates the
  point, delete it.
- **Ground every abstraction in the author's world.** He is a prop firm
  trader and a site reliability engineer. Revenge trading illustrates the
  shadow; the daily loss limit illustrates emotional control; incident drills
  illustrate training the horse. General examples are fine too, but the
  specific ones are what make it his.
- **No formulaic closers.** A recurring image (the rider and the horse) is used
  where it illuminates, never bolted onto the end of every post.
- **Resolve contradictions across posts** instead of repeating both sides.
  "Burn the bridges, no plan B" and "think in probabilities" were reconciled:
  burn bridges on identity, never on risk.
- **Link the series together** with wikilinks where ideas genuinely overlap,
  and link forward and back between series.
- **Short, specific titles.** "Have-Do-Be", "The Weather Inside",
  "Someone Else's Capital", not "X: A Journey Into Y".

### Truth rules

These do not bend, however much licence the writing has.

- **Never invent the author's life.** No made-up events, amounts, durations,
  feelings or firm names. Anchor personal claims to something verifiable:
  `content/about.md`, verbatim journal notes in `scripts/data/trades.json`
  (check the date and wording before quoting), git history, or what the author
  has said. Write in first person only about established facts. When a claim
  cannot be verified, rephrase it so it no longer needs to be, and tell the
  author what was changed.
- **Compute every number** with a script before it appears in prose. Probabilities,
  expectancy, compounding, percentages: run them, do not estimate them.
- **Prose must match its chart.** If the text says "candles 7 to 14" or
  "finishes at +7R", check it against the chart data. Two such errors were
  caught this way.
- **Label synthetic charts as illustrations** in italics under the chart.
- **Quotes must be real and sourced.** Prefer the primary wording over the
  popular paraphrase (Jung from *Aion*, Russell from *The Triumph of
  Stupidity*). Drop misattributed or unsourced lines (the Lincoln, Tesla,
  Drucker and "Unknown" quotes were removed).
- **Science needs a name and its caveats.** Cite the actual research
  (Mullainathan and Shafir on scarcity, Kruger and Dunning 1999) and mention
  known replication problems (the 2018 marshmallow replication). No
  pseudoscience: no "frequencies", "vibration" or unfalsifiable energy claims.
- **Verify external facts** (a firm's rules, a date, a figure) from the source
  at the time of writing, and say "as it stands today" where it can change.

## Images

Every post should carry at least one image that says something. Sources, in
order of preference:

1. **The author's own material** (his TradingView snapshots, project
   screenshots from his repos).
2. **Wikimedia Commons**, licences **Public domain, CC0, CC BY or CC BY-SA
   only**. Never an image found through a general web search: that is
   somebody's copyright.

Use the script:

```sh
python3 scripts/commons_image.py search "Wanderer above the Sea of Fog"
python3 scripts/commons_image.py fetch "Wanderer above the Sea of Fog" 0 static/images/notes/18.jpg
```

`fetch` resizes to 1400px, flattens transparent diagrams onto white (black
lines vanish on the dark theme otherwise), saves a JPEG and prints the licence,
author and Commons URL.

**Choosing.** Pick images that carry the idea, not decoration. The best ones
are metaphors the reader gets instantly:

| Idea | Image |
|---|---|
| a goal that keeps receding | Assereto, *Tantalus* |
| effort that goes nowhere | the Brixton prison treadmill |
| committing in advance | Waterhouse, *Ulysses and the Sirens* |
| a framework patched instead of falsified | Cellarius, Ptolemy's epicycles |
| randomness with a predictable shape | a Galton board |
| a rigged game | Caravaggio, *The Cardsharps* |

Where the text quotes a person, their portrait works. Avoid artwork dominated
by nudity; there is almost always a clothed alternative (Waterhouse's Sirens
over Draper's).

**Review before placing.** Build a contact sheet and look at every candidate:

```sh
magick montage static/images/notes/*.jpg -geometry 260x260+6+6 -tile 5x -background '#1e293b' /tmp/sheet.jpg
```

Reject blurry scans, library rulers in the margin, cluttered photos, and
diagrams that need a paragraph to explain.

**Placing.** Store under `static/images/<series>/NN.jpg`. Insert with `figure`
directly after the paragraph it illustrates, never as a detached gallery:

```
{{< figure src="/images/notes/04.jpg" alt="Tantalus straining toward fruit just out of reach" caption="Gioacchino Assereto, *Tantalus*, 1640s. Condemned to stand beneath fruit that pulls away every time he reaches for it. Public domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:...)." >}}
```

- **alt**: what the image shows, for screen readers.
- **caption**: artist, *title*, year; one sentence on why it is here; then the
  credit. For CC BY and CC BY-SA, name the photographer or author and the
  licence. Encode `(` and `)` in Commons URLs as `%28` and `%29`, or the
  markdown link breaks.
- No double quotes inside captions: the caption is itself a quoted parameter.

## Charts, diagrams and tables

Use whichever carries the idea fastest:

| Use | For |
|---|---|
| **Chart.js** (`chart`) | a mechanism with numbers: equity curves, two traders on the same trades, a challenge passing and failing, compounding |
| **Mermaid** (`mermaid`) | a decision or a cycle: entry rules, Be-Do-Have |
| **Table** | a comparison: rider vs horse, the four boxes of decision vs outcome, qualifies vs does not |

Original charts built from computed data are better than a stock image of a
chart. Mixed charts work (`type: 'bar'` with a `type: 'line'` dataset for a
limit line).

## Verifying before publishing

Screenshots in the preview browser are unreliable for anything below the fold,
so verify in the DOM and the built HTML:

1. No em dashes, en dashes or emojis in any changed file.
2. `python3 scripts/wikilinks.py --check` reports nothing unresolved.
3. `rm -rf public && ./scripts/build.sh` builds clean.
4. Count what should exist in `public/`: canvases, `not-prose mermaid`
   blocks, figures, Commons credit links, and zero raw `[[`.
5. In the browser, confirm charts drew (`Chart.getChart(canvas)`, non-zero
   height) and images loaded (`img.naturalWidth > 0`).
6. **Stage only the files you changed.** Obsidian drops untracked files into
   `content/` (canvases, `.base`, daily notes); `git add -A` would publish them.
7. Commit without any AI attribution trailer, push, then `curl` the live pages.

## The series

| Series | Posts | About |
|---|---|---|
| Notes from the Edge | 01 to 18 | the author's philosophy: three models, the rider and the horse, the edge |
| Getting Funded | 19 to 22 | his path in trading, October 2022 onward, ending with leaving ICT for VWAP fades |

### Shortcodes for visuals

Full reference for all 46: [`docs/shortcodes.md`](docs/shortcodes.md).
The ones below are verified working in this setup.

Chart - Chart.js config as the body:

```
{{< chart >}}
type: 'line',
data: { labels: ['Jan','Feb'], datasets: [{ label: 'PnL', data: [4, 9] }] }
{{< /chart >}}
```

Diagram - mermaid:

```
{{< mermaid >}}
graph LR
  Idea --> Draft --> Published
{{< /mermaid >}}
```

Images - put the file next to the post and reference it relatively, or use
`{{< figure src="x.png" caption="..." >}}` for a caption.

Also available: `alert`, `lead`, `badge`, `timeline`, `steps`, `tabs`,
`gallery`, `stat`, `katex`, `video`, `youtubeLite`, `github`, `carousel`,
`accordion`, `swatches`, `typeit`. Run
`ls $(hugo mod vendor >/dev/null; echo _vendor/github.com/nunocoracao/blowfish/v3/layouts/shortcodes)`
to see all 46, then delete `_vendor/`.

## Publishing

```sh
git add -A && git commit -m "..." && git push
```

Roughly one minute to live. Check the run with
`gh run list --workflow deploy.yml --limit 1`.
