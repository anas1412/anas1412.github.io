#!/usr/bin/env python3
"""Pull the trading journal from Google Sheets and rebuild content/trading/_index.md.

    python3 scripts/sync_trades.py          # fetch every tab, regenerate the page
    python3 scripts/sync_trades.py --local  # regenerate from the committed snapshot

Reads all journal tabs and merges them chronologically. The sheets use three
different outcome vocabularies; they are normalised to the newest one. Only the
columns the page shows are kept - date, direction, result, R, P&L, chart, notes.

The sheet must stay viewable by anyone with the link.
"""
import argparse, csv, io, json, os, sys, urllib.request
from collections import OrderedDict
from datetime import datetime

SHEET = "1tXcf-haO-wSi0uQiPA6xDRSOdIcv_mRSULE8tIPbsBU"
TABS = ["301248474", "114438852", "1001618359", "2141663714"]   # oldest -> newest
# gid 0 is an empty template tab (TOTAL trades: 0) - deliberately not listed

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# not under data/ - Hugo treats that as a data directory and fails to parse CSV
SNAPSHOT = os.path.join(ROOT, "scripts", "data", "trades.json")
PAGE = os.path.join(ROOT, "content", "trading", "_index.md")

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


def page(trades):
    by_month = OrderedDict()
    for t in trades:
        key = datetime.strptime(t["date"], "%Y-%m-%d").strftime("%B %Y")
        by_month.setdefault(key, []).append(t)

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
    for month, rows in by_month.items():
        out += [f"## {month}", "",
                "| Day | Dir | Result | R | P&L | Chart | Notes |",
                "|---:|---|---|---:|---:|---|---|"]
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
    os.makedirs(os.path.dirname(PAGE), exist_ok=True)
    open(PAGE, "w", encoding="utf-8").write(page(trades))
    print(f"wrote {PAGE} from {len(trades)} trades ({trades[0]['date']} -> {trades[-1]['date']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
