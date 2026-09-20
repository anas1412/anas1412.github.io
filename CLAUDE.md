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
| `content/templates/post.md` | Obsidian note template (never published) |
| `config/_default/languages.en.toml` | name, headline, bio, social links, site title |
| `config/_default/params.toml` | `colorScheme` (15 options), dark mode, article display |
| `config/_default/menus.en.toml` | the navbar |
| `config/_default/hugo.toml` | baseURL, taxonomies, `ignoreFiles` |
| `archetypes/posts.md` | Hugo CLI template — filename must match the section folder |

The theme is a **Hugo Module**, not vendored code. Update with `hugo mod get -u`.
Never commit `_vendor/`.

## Commands

```sh
hugo server     # localhost:1313, live reload
hugo --quiet    # production build into public/
```

Always build before committing. A malformed frontmatter value fails the
**entire site**, not just one page.

## Hard rules

These are all things that have already broken this site once.

- **No `[[wikilinks]]`.** Hugo renders them as literal `[[text]]`. Use
  `[label](/posts/the-slug/)`.
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
- **`series:` is Hugo-only. `tags:` works in both Hugo and Obsidian.** Obsidian's
  graph draws edges from links and tags, and knows nothing about `series`. Use
  tags for anything that should connect in both places.
- Blowfish warns it caps at Hugo 0.165 while we run 0.166. Benign — it builds
  correctly. Don't downgrade to silence it.

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

Series posts add two more lines:

```yaml
series: ["Notes from the Edge"]
series_order: 3
```

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
