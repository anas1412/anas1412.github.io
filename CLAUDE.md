# CLAUDE.md

Personal site for Anas Bassoumi. Hugo + the Blowfish theme, deployed to GitHub
Pages on every push to `main`. Live at <https://anas1412.github.io>.

## Where everything is

| Path | What it holds |
|---|---|
| `content/` | **the Obsidian vault** — open this folder in Obsidian, not the repo root |
| `content/posts/` | all writing. One `.md` per post |
| `content/_index.md` | the homepage paragraph |
| `content/about.md` | experience, education, skills |
| `content/projects.md` | projects |
| `content/templates/post.md` | Obsidian template for a standalone post |
| `content/templates/series-post.md` | Obsidian template for a post in a series |
| `config/_default/languages.en.toml` | name, headline, bio, social links, site title |
| `config/_default/params.toml` | `colorScheme` (15 options), dark mode, article display |
| `config/_default/menus.en.toml` | the navbar |
| `config/_default/hugo.toml` | baseURL, taxonomies, `ignoreFiles` |
| `archetypes/posts.md` | Hugo CLI template — filename must match the section folder |

The theme is a **Hugo Module**, not vendored code. Update with `hugo mod get -u`.
Never commit `_vendor/`.

## Commands

```sh
./scripts/build.sh serve    # preview on localhost:1313
./scripts/build.sh          # production build into public/
python3 scripts/test_wikilinks.py   # self-check for the converter
```

**Use the script, not bare `hugo`** — it converts wikilinks first. Bare `hugo`
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
- **Every post needs `title:`.** Without it Hugo publishes an untitled page —
  it does not fall back to the filename.
- **Never name a section after one of Anas's repos.** A repo named `x` serves
  at `anas1412.github.io/x/` and shadows that path on this site. `/notes/` is
  already taken this way — it belongs to a different repo.
- **`draft: true` is not privacy.** The post stays out of the build but the
  repo is public, so the file is still readable on GitHub.
- **`series:` is Hugo-only. `tags:` and `[[wikilinks]]` work in both.**
  Obsidian's graph draws edges from links and tags, and knows nothing about
  `series`.
- Blowfish warns it caps at Hugo 0.165 while we run 0.166. Benign — it builds
  correctly. Don't downgrade to silence it.

## Wikilinks

Write `[[wikilinks]]` normally — Obsidian's graph, autocomplete and backlinks
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

Resolution is by **filename first, then frontmatter title** — the same order
Obsidian uses. Code spans and fenced blocks are skipped. A link that resolves
to nothing is left as-is and reported, never silently dropped.

Check before pushing:

```sh
python3 scripts/wikilinks.py --check    # lists unresolved links, changes nothing
```

## File naming

Posts are named `NN-slug.md` — a zero-padded two-digit number, then the title
slugified.

```
content/posts/03-shadow-work-making-the-unconscious-conscious.md
content/posts/18-conclusion-the-edge-of-transformation.md
```

- **`NN`** — two digits, zero-padded (`01`, not `1`). For a series it matches
  `series_order`. Otherwise continue from the highest number in `content/posts/`.
- **slug** — the title, lowercased, non-alphanumerics collapsed to single
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

Series posts add two more lines — use the **series-post** template, which
includes them:

```yaml
series: ["Notes from the Edge"]
series_order: 3
```

Change the series name and set `series_order` to the next free number in that
series. Blowfish renders the full part list on every post in it.

## Writing style

**Clarity beats everything else.** If a sentence needs re-reading, rewrite it.

- **Show, don't tell.** A number, a screenshot, or a worked example instead of
  an adjective. Not "performance improved dramatically" — "p99 went from 840ms
  to 120ms."
- **Simple language.** Short words, short sentences. Cut jargon unless the
  reader needs the term itself.
- **Break up prose.** Bullet points and tables over paragraphs. If a paragraph
  runs past four or five lines, it is probably a list.
- **Visuals wherever they carry meaning** — see the shortcodes below. A diagram
  of a flow beats three paragraphs describing it.
- **Quote when the source says it better**, and attribute it. Don't pad with
  quotes that only decorate.
- No filler openers, no "in today's world", no summarising what you're about
  to say before saying it.

### Shortcodes for visuals

All verified working in this setup.

Chart — Chart.js config as the body:

```
{{< chart >}}
type: 'line',
data: { labels: ['Jan','Feb'], datasets: [{ label: 'PnL', data: [4, 9] }] }
{{< /chart >}}
```

Diagram — mermaid:

```
{{< mermaid >}}
graph LR
  Idea --> Draft --> Published
{{< /mermaid >}}
```

Images — put the file next to the post and reference it relatively, or use
`{{< figure src="x.png" caption="..." >}}` for a caption.

Also available: `alert`, `lead`, `badge`, `timeline`, `steps`, `tabs`,
`gallery`, `stat`, `katex`, `video`, `youtubeLite`, `github`, `carousel`,
`accordion`, `swatches`, `typeit`. Run
`ls $(hugo mod vendor >/dev/null; echo _vendor/github.com/nunocoracao/blowfish/v3/layouts/shortcodes)`
to see all 44, then delete `_vendor/`.

## Publishing

```sh
git add -A && git commit -m "..." && git push
```

Roughly one minute to live. Check the run with
`gh run list --workflow deploy.yml --limit 1`.
