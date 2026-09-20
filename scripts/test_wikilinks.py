#!/usr/bin/env python3
"""Run: python3 scripts/test_wikilinks.py  — fails loudly if conversion breaks."""
import os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "posts/shadow-work.md": '---\ntitle: "Shadow Work"\n---\nbody\n',
    "posts/other.md": '---\ntitle: "Some Other Note"\n---\nbody\n',
    "about.md": '---\ntitle: "About"\n---\nbody\n',
    "posts/subject.md": (
        '---\ntitle: "Subject"\n---\n'
        "bare [[shadow-work]]\n"
        "alias [[shadow-work|the shadow]]\n"
        "heading [[shadow-work#Making It Conscious]]\n"
        "both [[shadow-work#Making It Conscious|see here]]\n"
        "bytitle [[Some Other Note]]\n"
        "root [[about]]\n"
        "image ![[pic.png]]\n"
        "missing [[does-not-exist]]\n"
        "code `[[shadow-work]]` stays\n"
        "```\n[[shadow-work]]\n```\n"
    ),
}
EXPECT = [
    "bare [Shadow Work](/posts/shadow-work/)",
    "alias [the shadow](/posts/shadow-work/)",
    "heading [Making It Conscious](/posts/shadow-work/#making-it-conscious)",
    "both [see here](/posts/shadow-work/#making-it-conscious)",
    "bytitle [Some Other Note](/posts/other/)",
    "root [About](/about/)",
    "image ![](/images/pic.png)",
    "missing [[does-not-exist]]",            # unresolved left alone
    "code `[[shadow-work]]` stays",          # code span untouched
]

d = tempfile.mkdtemp()
try:
    for rel, body in FILES.items():
        p = os.path.join(d, "content", rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, "w").write(body)
    os.makedirs(os.path.join(d, "static", "images"), exist_ok=True)
    open(os.path.join(d, "static", "images", "pic.png"), "wb").write(b"\x89PNG")

    subprocess.run([sys.executable, os.path.join(HERE, "wikilinks.py"),
                    "--content", os.path.join(d, "content"),
                    "--static", os.path.join(d, "static")],
                   check=False, capture_output=True)

    got = open(os.path.join(d, "content", "posts", "subject.md")).read()
    fails = [e for e in EXPECT if e not in got]
    # the fenced block must survive untouched
    if "```\n[[shadow-work]]\n```" not in got:
        fails.append("fenced code block was rewritten")

    if fails:
        print("FAIL:")
        for f in fails:
            print("  missing:", f)
        print("\n--- got ---\n" + got)
        sys.exit(1)
    print(f"ok — {len(EXPECT)} cases pass")
finally:
    shutil.rmtree(d)
