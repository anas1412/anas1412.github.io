#!/usr/bin/env python3
"""Pull the trading journal from Google Sheets and rebuild content/trading/_index.md.

    python3 scripts/sync_trades.py          # fetch the sheet, regenerate the page
    python3 scripts/sync_trades.py --local  # regenerate from data/trades.csv only

The sheet must be viewable by anyone with the link. A snapshot is kept in
data/trades.csv so builds never depend on the network.
"""
import argparse, csv, io, os, sys, urllib.request
from collections import OrderedDict
from datetime import datetime

SHEET = "1tXcf-haO-wSi0uQiPA6xDRSOdIcv_mRSULE8tIPbsBU"
GID = "2141663714"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET}/export?format=csv&gid={GID}"

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# not under data/ — Hugo treats that as a data directory and fails to parse CSV
CSV_PATH = os.path.join(ROOT, "scripts", "data", "trades.csv")
PAGE = os.path.join(ROOT, "content", "trading", "_index.md")


def money(s):
    s = (s or "").replace("$", "").replace(",", "").strip()
    try:
        return float(s)
    except ValueError:
        return 0.0


def num(s):
    try:
        return float((s or "").strip())
    except ValueError:
        return None


def load(text):
    """Real trades only — the sheet carries a TOTAL row and blank padding."""
    return [r for r in csv.DictReader(io.StringIO(text))
            if (r.get("date") or "").strip() and (r.get("instrument") or "").strip()
            and not (r.get("instrument") or "").startswith("TOTAL")]


def page(rows):
    by_month = OrderedDict()
    for r in rows:
        k = datetime.strptime(r["date"], "%B %d, %Y").strftime("%B %Y")
        by_month.setdefault(k, []).append(r)

    out = [
        "---",
        'title: "Trading"',
        'description: "Every trade I take, logged."',
        "showTableOfContents: true",
        "showDate: false",
        "---",
        "",
        "Every trade, win or lose, with the chart I took it from.",
        f"Last synced {datetime.now():%-d %B %Y}.",
        "",
    ]

    for month, trades in by_month.items():
        out += [f"## {month}", "",
                # day only - the month is the heading, and a wrapping date
                # column squeezes everything else
                "| Day | Dir | Result | R | P&L | Chart | Notes |",
                "|---:|---|---|---:|---:|---|---|"]
        for r in trades:
            d = datetime.strptime(r["date"], "%B %d, %Y").strftime("%-d")
            rr = num(r["RR Return"])
            pnl = money(r["pnl ($)"])
            shot = f"[view]({r['screenshot']})" if r.get("screenshot") else ""
            note = (r.get("notes") or "").strip().replace("|", "\\|")
            out.append(f"| {d} | {r['direction']} | {r['outcome']} | "
                       f"{rr:+.2f} | {'-' if pnl < 0 else ''}${abs(pnl):,.0f} | {shot} | {note} |")
        out.append("")

    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--local", action="store_true", help="skip the fetch")
    a = ap.parse_args()

    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    if a.local:
        text = open(CSV_PATH, encoding="utf-8").read()
    else:
        try:
            text = urllib.request.urlopen(URL, timeout=30).read().decode("utf-8")
        except Exception as e:
            print(f"fetch failed ({e}); falling back to {CSV_PATH}", file=sys.stderr)
            text = open(CSV_PATH, encoding="utf-8").read()
        else:
            open(CSV_PATH, "w", encoding="utf-8").write(text)

    rows = load(text)
    if not rows:
        print("no trades parsed — has the sheet's layout changed?", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(PAGE), exist_ok=True)
    open(PAGE, "w", encoding="utf-8").write(page(rows))
    print(f"wrote {PAGE} from {len(rows)} trades")
    return 0


if __name__ == "__main__":
    sys.exit(main())
