#!/usr/bin/env python3
"""Convert Obsidian wikilinks to markdown links.

Source files keep [[wikilinks]] so Obsidian's graph and autocomplete work.
This runs at build time against a throwaway copy of content/, never against
the files you edit.

    [[note]]              -> [note title](/posts/note/)
    [[note|Alias]]        -> [Alias](/posts/note/)
    [[note#Heading]]      -> [note title](/posts/note/#heading)
    [[note#Heading|Text]] -> [Text](/posts/note/#heading)
    ![[image.png]]        -> ![](/images/image.png)

Resolution is by FILENAME first, then by frontmatter title — the same order
Obsidian uses. Unresolved links are left untouched and reported.
"""
import argparse, os, re, sys

WIKILINK = re.compile(r"(!?)\[\[([^\]\n]+?)\]\]")
FENCE = re.compile(r"(```.*?```|~~~.*?~~~|`[^`\n]+`)", re.S)
TITLE = re.compile(r'^\s*title:\s*["\']?(.+?)["\']?\s*$', re.M)

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".avif", ".mp4"}


def anchor(text):
    """Hugo's default heading anchor: lowercase, non-alphanumerics to hyphens."""
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def build_index(content_dir, static_dir):
    """filename stem -> url, and title -> url. Plus asset name -> url."""
    pages, titles, assets = {}, {}, {}
    for root, _, files in os.walk(content_dir):
        if os.path.basename(root) in {"templates"} or ".obsidian" in root:
            continue
        for f in files:
            full = os.path.join(root, f)
            stem, ext = os.path.splitext(f)
            rel = os.path.relpath(full, content_dir)
            if ext == ".md":
                url = "/" + os.path.dirname(rel).replace(os.sep, "/")
                url = "/" if stem == "_index" and url == "/." else url
                if stem != "_index":
                    url = (url.rstrip("/") + "/" + stem + "/").replace("//", "/")
                elif not url.endswith("/"):
                    url += "/"
                pages.setdefault(stem, url)
                t = TITLE.search(open(full, encoding="utf-8").read(2048))
                if t:
                    titles.setdefault(t.group(1), url)
            elif ext.lower() in IMAGE_EXT:
                assets.setdefault(f, "/" + rel.replace(os.sep, "/"))
    if os.path.isdir(static_dir):
        for root, _, files in os.walk(static_dir):
            for f in files:
                rel = os.path.relpath(os.path.join(root, f), static_dir)
                assets.setdefault(f, "/" + rel.replace(os.sep, "/"))
    return pages, titles, assets


def convert(text, pages, titles, assets, unresolved):
    def one(m):
        bang, inner = m.group(1), m.group(2)
        # inside a markdown table Obsidian writes the alias pipe as \|
        inner = inner.replace("\\|", "|")
        target, _, alias = inner.partition("|")
        target, _, head = target.partition("#")
        target, alias, head = target.strip(), alias.strip(), head.strip()

        if bang:  # ![[asset]]
            url = assets.get(target) or assets.get(os.path.basename(target))
            if not url:
                unresolved.append(inner)
                return m.group(0)
            return f"![{alias or ''}]({url})"

        url = pages.get(target) or titles.get(target)
        if not url:
            unresolved.append(inner)
            return m.group(0)
        label = alias or head or titles_inv.get(url, target)
        return f"[{label}]({url}{'#' + anchor(head) if head else ''})"

    # never touch code spans or fenced blocks
    parts = FENCE.split(text)
    for i in range(0, len(parts), 2):
        parts[i] = WIKILINK.sub(one, parts[i])
    return "".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--content", default="content")
    ap.add_argument("--static", default="static")
    ap.add_argument("--check", action="store_true",
                    help="report unresolved links, change nothing, exit 1 if any")
    a = ap.parse_args()

    pages, titles, assets = build_index(a.content, a.static)
    global titles_inv
    titles_inv = {v: k for k, v in titles.items()}

    unresolved, changed = [], 0
    for root, _, files in os.walk(a.content):
        if ".obsidian" in root:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            src = open(p, encoding="utf-8").read()
            out = convert(src, pages, titles, assets, unresolved)
            if out != src:
                changed += 1
                if not a.check:
                    open(p, "w", encoding="utf-8").write(out)

    verb = "would rewrite" if a.check else "rewrote"
    print(f"wikilinks: {verb} {changed} file(s)")
    if unresolved:
        print("unresolved (left as-is):", file=sys.stderr)
        for u in sorted(set(unresolved)):
            print(f"  [[{u}]]", file=sys.stderr)
        return 1 if a.check else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
