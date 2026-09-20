#!/usr/bin/env python3
"""Pull the trading journal from Google Sheets and rebuild content/trading/_index.md.

    python3 scripts/sync_trades.py          # fetch every tab, regenerate the page
    python3 scripts/sync_trades.py --local  # regenerate from the committed snapshot

Reads all journal tabs and merges them chronologically. The sheets use three
different outcome vocabularies; they are normalised to the newest one. Only the
columns the page shows are kept - date, direction, result, R, P&L, chart, notes.

The sheet must stay viewable by anyone with the link.
"""
import argparse, csv, io, json, os, re, sys, urllib.request
from collections import OrderedDict
from datetime import datetime

SHEET = "1tXcf-haO-wSi0uQiPA6xDRSOdIcv_mRSULE8tIPbsBU"
TABS = ["301248474", "114438852", "1001618359", "2141663714"]   # oldest -> newest
# gid 0 is an empty template tab (TOTAL trades: 0) - deliberately not listed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# not under data/ - Hugo treats that as a data directory and fails to parse CSV
SNAPSHOT = os.path.join(ROOT, "scripts", "data", "trades.json")
TRADING = os.path.join(ROOT, "content", "trading")

# older tabs spell outcomes differently; "Tape Reading" rows have no P&L or
# risk at all, so they are days the trade was not taken
OUTCOME = {"win": "W", "loss": "L", "breakeven": "BE", "w": "W", "l": "L",
           "be": "BE", "missed": "missed", "tape reading": "missed"}
MISTAKES = {"performance mistake", "analysis mistake"}


def money(s):
    s = (s or "").replace("$", "").replace(",", "").strip()
    try: return float(s)
    except ValueError: return None


def num(s):
    try: return float((s or "").strip())
    except ValueError: return None


def parse_date(s):
    for fmt in ("%B %d, %Y", "%Y-%m-%d", "%m/%d/%Y"):
        try: return datetime.strptime((s or "").strip(), fmt)
        except ValueError: pass
    return None


def rows_from(text):
    out = []
    for r in csv.DictReader(io.StringIO(text)):
        inst = (r.get("instrument") or "").strip()
        d = parse_date(r.get("date"))
        if not d or not inst or inst.startswith("TOTAL"):
            continue                                   # TOTAL / padding rows

        raw = (r.get("outcome") or "").strip()
        pnl = money(r.get("pnl ($)"))
        key = raw.lower()
        if key in OUTCOME:
            result = OUTCOME[key]
        elif pnl is None:
            result = "missed"
        else:                                          # mistake labels: judge by result
            result = "W" if pnl > 1 else ("L" if pnl < -1 else "BE")

        notes = (r.get("notes") or "").strip()
        if key in MISTAKES:
            notes = f"[{raw}] {notes}".strip()          # keep the label, don't lose it

        rr = num(r.get("RR Return"))
        if rr is None and pnl is not None:
            risk = money(r.get("risk ($)"))
            rr = pnl / risk if risk else None

        out.append({
            "date": d.strftime("%Y-%m-%d"),
            "direction": (r.get("direction") or "").strip(),
            "result": result,
            "r": rr,
            "pnl": pnl,
            "chart": (r.get("screenshot") or "").strip(),
            "notes": notes,
        })
    return out


def fetch():
    trades = []
    for gid in TABS:
        url = f"https://docs.google.com/spreadsheets/d/{SHEET}/export?format=csv&gid={gid}"
        trades += rows_from(urllib.request.urlopen(url, timeout=30).read().decode("utf-8"))
    trades.sort(key=lambda t: t["date"])
    return trades


def month_page(month, rows, when):
    """One article per month."""
    out = [
        "---",
        f'title: "{month}"',
        f"date: {when}",
        "draft: false",
        'tags: ["trading"]',
        f'summary: "{len(rows)} trades logged in {month}."',
        "---",
        "",
        "| Day | Dir | Result | R | P&L | Chart | Notes |",
        "|---:|---|---|---:|---:|---|---|",
    ]
    for t in rows:
        day = datetime.strptime(t["date"], "%Y-%m-%d").strftime("%-d")
        r = f"{t['r']:+.2f}" if t["r"] is not None else ""
        p = t["pnl"]
        pnl = "" if p is None else f"{'-' if p < 0 else ''}${abs(p):,.0f}"
        chart = f"[view]({t['chart']})" if t["chart"] else ""
        note = t["notes"].replace("|", "\\|")
        out.append(f"| {day} | {t['direction']} | {t['result']} | {r} | {pnl} | {chart} | {note} |")
    out.append("")
    return "\n".join(out)


def index_page(total, months):
    return "\n".join([
        "---",
        'title: "Trading"',
        'description: "Every trade I take, logged."',
        "showDate: false",
        "---",
        "",
        "Every trade, win or lose, with the chart I took it from.",
        f"{total} logged across {len(months)} months, newest first.",
        f"Last synced {datetime.now():%-d %B %Y}.",
        "",
    ])


def write_all(trades):
    by_month = OrderedDict()
    for t in trades:
        key = datetime.strptime(t["date"], "%Y-%m-%d").strftime("%B %Y")
        by_month.setdefault(key, []).append(t)

    os.makedirs(TRADING, exist_ok=True)
    # drop previously generated month files; the sheet is the source of truth
    for f in os.listdir(TRADING):
        if re.fullmatch(r"\d{4}-\d{2}\.md", f):
            os.remove(os.path.join(TRADING, f))

    for month, rows in by_month.items():
        # dated to the last trade of that month, so the list sorts correctly
        when = rows[-1]["date"]
        slug = datetime.strptime(when, "%Y-%m-%d").strftime("%Y-%m")
        open(os.path.join(TRADING, f"{slug}.md"), "w", encoding="utf-8").write(
            month_page(month, rows, when))

    open(os.path.join(TRADING, "_index.md"), "w", encoding="utf-8").write(
        index_page(len(trades), by_month))
    return by_month


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--local", action="store_true", help="skip the fetch")
    a = ap.parse_args()

    os.makedirs(os.path.dirname(SNAPSHOT), exist_ok=True)
    if a.local:
        trades = json.load(open(SNAPSHOT))
    else:
        try:
            trades = fetch()
        except Exception as e:
            print(f"fetch failed ({e}); using {SNAPSHOT}", file=sys.stderr)
            trades = json.load(open(SNAPSHOT))
        else:
            json.dump(trades, open(SNAPSHOT, "w"), indent=1)

    if not trades:
        print("no trades parsed - has the sheet layout changed?", file=sys.stderr)
        return 1
    months = write_all(trades)
    print(f"wrote {len(months)} month pages from {len(trades)} trades "
          f"({trades[0]['date']} -> {trades[-1]['date']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
