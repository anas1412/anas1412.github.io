#!/usr/bin/env python3
"""Find and fetch freely licensed images from Wikimedia Commons.

    python3 scripts/commons_image.py search "Wanderer above the Sea of Fog"
    python3 scripts/commons_image.py fetch "Wanderer above the Sea of Fog" 0 static/images/notes/18.jpg

`search` lists the top results with licence, size and author.
`fetch` downloads result N, resizes to at most 1400px wide, flattens any
transparency onto white (so diagrams stay readable on the dark theme), saves a
JPEG, and prints the licence, author and Commons page URL for the caption.

Only publish images whose licence is Public domain, CC0, CC BY or CC BY-SA,
and always credit them. See CLAUDE.md, "Images".
"""
import io, json, os, re, sys, urllib.parse, urllib.request

UA = "anas1412.github.io image sourcing (anasbassoumi@gmail.com)"


def _get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60).read()


def search(query, n=5):
    url = ("https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrnamespace=6"
           f"&gsrsearch={urllib.parse.quote(query)}&gsrlimit={n}&prop=imageinfo"
           "&iiprop=url|extmetadata|size|mime&iiurlwidth=1400&format=json")
    pages = json.loads(_get(url)).get("query", {}).get("pages", {}).values()
    out = []
    for p in sorted(pages, key=lambda p: p.get("index", 0)):
        ii = p["imageinfo"][0]; m = ii.get("extmetadata", {})
        g = lambda k: re.sub(r"<[^>]+>", "", m.get(k, {}).get("value", "")).strip()
        out.append(dict(title=p["title"], licence=g("LicenseShortName"), author=g("Artist"),
                        credit=g("Credit"), width=ii.get("width"), height=ii.get("height"),
                        thumb=ii.get("thumburl"),
                        page=ii.get("descriptionurl", "").replace("(", "%28").replace(")", "%29")))
    return out


def fetch(query, index, dest):
    from PIL import Image
    r = search(query)[index]
    im = Image.open(io.BytesIO(_get(r["thumb"])))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA"); bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[-1]); im = bg
    else:
        im = im.convert("RGB")
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    im.save(dest, "JPEG", quality=82, progressive=True, optimize=True)
    r.update(file=dest, size=f"{im.width}x{im.height}", kb=os.path.getsize(dest) // 1024)
    return r


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "search":
        for i, r in enumerate(search(" ".join(sys.argv[2:]))):
            print(f"[{i}] {r['licence'][:14]:14} {r['width']}x{r['height']:<6} {r['title'][5:70]}  ({r['author'][:40]})")
    elif len(sys.argv) == 5 and sys.argv[1] == "fetch":
        r = fetch(sys.argv[2], int(sys.argv[3]), sys.argv[4])
        print(json.dumps({k: r[k] for k in ("title", "licence", "author", "credit", "page", "size", "kb")}, indent=1))
    else:
        sys.exit(__doc__)
