#!/usr/bin/env python3
"""Check every golfed program against its OEIS b-file and keep the README records table in sync.

usage: python tools/verify.py [AXXXXXX ...] [--write] [--no-run] [--since=REF]

  --write       rewrite the records table in README.md instead of only checking it
  --no-run      skip running the programs (sizes, pages and table only)
  --since=REF   run only the programs of sequences whose files changed since git REF
                (a file moved without changes does not count); still check every page
"""
import json
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEQ = ROOT / "seq"
BFILES = ROOT / "bfiles"
README = ROOT / "README.md"
START, END = "<!-- records:start -->", "<!-- records:end -->"
DEFAULT_TIMEOUT = 60
NAME_WIDTH = 70


def category(prog):
    """py3.py -> 'Python 3', py3-sympy.py -> 'Python 3 + sympy'."""
    return " + ".join(["Python 3"] + prog.stem.split("-")[1:])


def size(prog):
    data = prog.read_bytes()
    if b"\r" in data:
        raise ValueError("use LF line endings")
    return len(data) - data.endswith(b"\n")


def bucket(aid):
    """Folder holding a thousand sequences and their b-files: A000026 -> A000xxx."""
    return aid[:-3] + "xxx"


def bfile(aid):
    path = BFILES / bucket(aid) / f"b{aid[1:]}.txt"
    terms = []
    for line in path.read_text().splitlines():
        if line.strip() and not line.startswith("#"):
            terms.append(line.split()[1])
    return terms


def changed(ref):
    """Sequences whose files differ from git REF, or None (run everything) when git cannot tell."""
    git = subprocess.run(["git", "diff", "--name-only", "--find-renames=100%", "--diff-filter=AM",
                          ref, "--", "seq", "bfiles"], cwd=ROOT, capture_output=True, text=True)
    if git.returncode:
        print(f"git diff {ref} failed, running everything: {git.stderr.strip()}")
        return None
    aids = set()
    for line in git.stdout.splitlines():
        path = Path(line)
        if path.parts[0] == "seq" and len(path.parts) > 3:
            aids.add(path.parts[2])
        elif path.parts[0] == "bfiles" and path.stem.startswith("b"):
            aids.add("A" + path.stem[1:])
    return aids


def run(prog, want, timeout):
    """Run prog until it prints `want` lines or `timeout` seconds pass; return (lines, seconds, stderr tail)."""
    lines = []
    with tempfile.TemporaryFile() as err:
        proc = subprocess.Popen([sys.executable, "-u", prog.name], cwd=prog.parent,
                                stdout=subprocess.PIPE, stderr=err, text=True)

        def read():
            for line in proc.stdout:
                lines.append(line.strip())
                if len(lines) >= want:
                    break

        reader = threading.Thread(target=read, daemon=True)
        t0 = time.monotonic()
        reader.start()
        reader.join(timeout)
        elapsed = time.monotonic() - t0
        proc.kill()
        proc.wait()
        reader.join()
        err.seek(0)
        tail = err.read().decode(errors="replace").strip().splitlines()[-1:]
    return lines[:want], elapsed, tail


def check_program(prog, ref, cfg, page, execute):
    """Return (record, problems) for one program file; cfg holds the sequence's min_terms and timeout."""
    problems = []
    try:
        nbytes = size(prog)
    except ValueError as e:
        return None, [f"{prog.name}: {e}"]
    src = prog.read_text().removesuffix("\n")
    heading = f"### {category(prog)} — {nbytes} bytes"
    if heading not in page:
        problems.append(f"{prog.name}: page has no heading '{heading}'")
    if src not in page:
        problems.append(f"{prog.name}: page does not show the program verbatim")

    min_terms = min(cfg.get("min_terms", len(ref)), len(ref))
    if execute:
        lines, elapsed, tail = run(prog, len(ref), cfg.get("timeout", DEFAULT_TIMEOUT))
        bad = next((i for i, (x, y) in enumerate(zip(lines, ref)) if x != y), None)
        if bad is not None:
            problems.append(f"{prog.name}: term {bad + 1} is {lines[bad][:40]!r}, expected {ref[bad][:40]!r}")
        elif len(lines) < min_terms:
            why = f" ({tail[0]})" if tail else ""
            problems.append(f"{prog.name}: only {len(lines)} of {min_terms} terms in {elapsed:.0f} s{why}")
        status = "ok" if bad is None and len(lines) >= min_terms else "FAIL"
        print(f"  {category(prog):<22} {nbytes:>4} bytes  {len(lines):>5} terms in {elapsed:5.1f} s  {status}")
    else:
        print(f"  {category(prog):<22} {nbytes:>4} bytes")
    return {"category": category(prog), "bytes": nbytes}, problems


def table(rows):
    cats = sorted({r["category"] for _, _, recs, _ in rows for r in recs}, key=lambda c: (c != "Python 3", c))
    out = ["| Sequence | Name | " + " | ".join(cats) + " | Terms checked |", "|---" * (len(cats) + 3) + "|"]
    for aid, name, recs, terms in rows:
        if len(name) > NAME_WIDTH:
            name = name[:NAME_WIDTH].rsplit(" ", 1)[0] + "…"
        name = name.replace("|", "\\|")  # a bare | in a name (p|n) would split the cell
        best = min(r["bytes"] for r in recs)
        cells = []
        for c in cats:
            r = next((r for r in recs if r["category"] == c), None)
            if r is None:
                cells.append("—")
            else:
                cells.append(f"**{r['bytes']}**" if r["bytes"] == best else str(r["bytes"]))
        out.append(f"| [{aid}](seq/{bucket(aid)}/{aid}/) | {name} | " + " | ".join(cells) + f" | {terms} |")
    return "\n".join(out)


def main(argv):
    write = "--write" in argv
    execute = "--no-run" not in argv
    only = {a.upper() for a in argv if not a.startswith("--")}
    since = next((a.split("=", 1)[1] for a in argv if a.startswith("--since=")), None)
    to_run = changed(since) if since else None
    if to_run is not None:
        print(f"changed since {since}: {', '.join(sorted(to_run)) or 'nothing'}")
    problems, rows = [], []

    # A bucket is the only kind of name that is its own bucket.
    problems += [f"seq/{p.name}: move it to seq/{bucket(p.name)}/{p.name}/"
                 for p in sorted(SEQ.iterdir()) if p.is_dir() and p.name != bucket(p.name)]
    for d in sorted((p for p in SEQ.glob("*/A*") if p.is_dir()), key=lambda p: p.name):
        aid = d.name
        if d.parent.name != bucket(aid):
            problems.append(f"seq/{d.parent.name}/{aid}: move it to seq/{bucket(aid)}/{aid}/")
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
        page = (d / "README.md").read_text(encoding="utf-8")
        ref = bfile(aid)
        recs = []
        selected = not only or aid in only
        if selected:
            print(f"{aid}  ({len(ref)} terms in b-file)")
        for prog in sorted(d.glob("py3*.py")):
            runs = execute and selected and (to_run is None or aid in to_run)
            rec, probs = check_program(prog, ref, meta, page, runs) if selected else (
                {"category": category(prog), "bytes": size(prog)}, [])
            problems += [f"{aid}/{p}" for p in probs]
            if rec:
                recs.append(rec)
        rows.append((aid, meta["name"], recs, min(meta.get("min_terms", len(ref)), len(ref))))

    text = README.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{START}\n{table(rows)}\n{END}{tail}"
    if new != text:
        if write:
            README.write_text(new, encoding="utf-8", newline="\n")
            print("README.md records table rewritten")
        else:
            problems.append("README.md records table is out of date: run tools/verify.py --write")

    for p in problems:
        print("FAIL", p)
    print("all good" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
