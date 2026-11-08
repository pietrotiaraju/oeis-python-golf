#!/usr/bin/env python3
"""Check every golfed program against its OEIS b-file and keep the README records table in sync.

usage: python tools/verify.py [AXXXXXX ...] [--write] [--no-run] [--since=REF]
                              [--to-bar] [--shard=I/N] [--report=PATH]

  --write        rewrite the records table in README.md instead of only checking it
  --no-run       skip running the programs (sizes, pages and table only)
  --since=REF    run only the programs of sequences whose files changed since git REF
                 (a file moved without changes does not count); still check every page
  --to-bar       stop each program once it has printed its min_terms terms, instead of
                 letting it run through the b-file until the timeout
  --shard=I/N    run only every N-th sequence, starting from the I-th (0 <= I < N)
  --report=PATH  write one tab-separated line per program run: sequence, bytes, min_terms,
                 timeout, reference seconds to reach min_terms, share of the timeout,
                 status, seconds on this machine, speed factor

A program passes when every line it prints is right and its min_terms-th term
arrives within MARGIN (half) of the sequence's timeout. The timeout itself only
stops the run: the margin keeps the verdict from hanging on how fast a machine is.

Times are in reference seconds. Before running programs (and again once a minute)
verify.py runs the fixed benchmark tools/bench.py the same way; a machine where it
takes twice REF_BENCH counts as twice as slow, so its timings are halved and its
timeouts doubled. GitHub's runners differ by up to 2.3 times in speed; the factor
takes that out, and the margin covers what it misses.

Each program runs alone in an empty temporary folder, with an empty environment,
no input and the audit hook of tools/sandbox.py: it cannot read the b-files or any
other file outside the Python installation, start processes or use the network.
"""
import json
import os
import shutil
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
MARGIN = 0.5  # min_terms must arrive within this share of the timeout
REF_BENCH = 0.265  # seconds tools/bench.py takes on a typical GitHub runner (median of 11, 2026-11-08)
RECALIBRATE = 60  # seconds after which the speed factor is measured again
_speed = [None, 0.0]  # [factor, time.monotonic() when measured]
NAME_WIDTH = 70


def category(prog):
    """py3.py -> 'Python 3'."""
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


def run(prog, want, timeout, bar):
    """Run prog until it prints `want` lines or `timeout` seconds pass.

    Return (lines, seconds, stderr tail, seconds until line `bar` arrived or None)."""
    lines, reached = [], []
    with tempfile.TemporaryFile() as err, tempfile.TemporaryDirectory() as box:
        # Alone in an empty folder, with the sandbox hook loaded as sitecustomize.
        shutil.copyfile(prog, Path(box) / "py3.py")
        shutil.copyfile(Path(__file__).with_name("sandbox.py"), Path(box) / "sitecustomize.py")
        env = {"PYTHONPATH": box, "PYTHONDONTWRITEBYTECODE": "1"}
        if "SYSTEMROOT" in os.environ:  # Windows needs it to start at all
            env["SYSTEMROOT"] = os.environ["SYSTEMROOT"]
        proc = subprocess.Popen([sys.executable, "-u", "py3.py"], cwd=box, env=env,
                                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=err, text=True)

        def read():
            for line in proc.stdout:
                lines.append(line.strip())
                if len(lines) == bar:
                    reached.append(time.monotonic() - t0)
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
    return lines[:want], elapsed, tail, (reached or [None])[0]


def speed():
    """How many times slower than the reference this machine is right now (tools/bench.py)."""
    if _speed[0] is None or time.monotonic() - _speed[1] > RECALIBRATE:
        lines, _, tail, _ = run(Path(__file__).with_name("bench.py"), 1, 600, 1)
        if not lines:
            sys.exit(f"tools/bench.py failed: {tail}")
        _speed[:] = float(lines[0]) / REF_BENCH, time.monotonic()
        print(f"  (benchmark {float(lines[0]):.3f} s: speed factor {_speed[0]:.2f})")
    return _speed[0]


def check_program(prog, ref, cfg, page, execute, to_bar=False):
    """Return (record, problems) for one program file; cfg holds the sequence's min_terms and timeout.

    When the program runs, the record also holds `bar_seconds` (reference seconds; None if
    min_terms never came), `raw_seconds`, `factor`, `timeout`, `min_terms` and `status`."""
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
    rec = {"category": category(prog), "bytes": nbytes}
    if execute:
        timeout = cfg.get("timeout", DEFAULT_TIMEOUT)
        limit = timeout * MARGIN
        page_problems = len(problems)
        f = speed()
        lines, elapsed, tail, raw = run(prog, min_terms if to_bar else len(ref), timeout * f, min_terms)
        bar = None if raw is None else raw / f
        bad = next((i for i, (x, y) in enumerate(zip(lines, ref)) if x != y), None)
        if bad is not None:
            problems.append(f"{prog.name}: term {bad + 1} is {lines[bad][:40]!r}, expected {ref[bad][:40]!r}")
        elif bar is None:
            why = f" ({tail[0]})" if tail else ""
            problems.append(f"{prog.name}: only {len(lines)} of {min_terms} terms in {elapsed / f:.0f} "
                            f"reference s ({elapsed:.0f} s here){why}")
        elif bar > limit:
            problems.append(f"{prog.name}: term {min_terms} came after {bar:.2f} reference s ({raw:.2f} s "
                            f"here); it must come within {limit:g}, half the {timeout} s timeout")
        status = "ok" if len(problems) == page_problems else "FAIL"
        at = f"{bar:6.1f}" if bar is not None else " never"
        print(f"  {category(prog):<22} {nbytes:>4} bytes  {len(lines):>5} terms in {elapsed:5.1f} s"
              f"  term {min_terms} at {at} ref s (limit {limit:g})  {status}")
        rec.update(bar_seconds=bar, raw_seconds=raw, factor=f, timeout=timeout, min_terms=min_terms,
                   status=status)
    else:
        print(f"  {category(prog):<22} {nbytes:>4} bytes")
    return rec, problems


def table(rows):
    cats = sorted({r["category"] for _, _, recs, _ in rows for r in recs}, key=lambda c: (c != "Python 3", c))
    out = ["| Sequence | Name | " + " | ".join(cats) + " | Terms checked |", "|---" * (len(cats) + 3) + "|"]
    for aid, name, recs, terms in rows:
        if len(name) > NAME_WIDTH:
            name = name[:NAME_WIDTH].rsplit(" ", 1)[0] + "…"
        for ch in "\\|*_":  # p|n would split the cell, 3*x^2 + 4*y^2 or p_j^k_j turn italic
            name = name.replace(ch, "\\" + ch)
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
    to_bar = "--to-bar" in argv
    since = next((a.split("=", 1)[1] for a in argv if a.startswith("--since=")), None)
    shard = next((tuple(map(int, a.split("=", 1)[1].split("/"))) for a in argv if a.startswith("--shard=")), None)
    report = next((a.split("=", 1)[1] for a in argv if a.startswith("--report=")), None)
    to_run = changed(since) if since else None
    if to_run is not None:
        print(f"changed since {since}: {', '.join(sorted(to_run)) or 'nothing'}")
    problems, rows, timings = [], [], []

    # A bucket is the only kind of name that is its own bucket.
    problems += [f"seq/{p.name}: move it to seq/{bucket(p.name)}/{p.name}/"
                 for p in sorted(SEQ.iterdir()) if p.is_dir() and p.name != bucket(p.name)]
    for k, d in enumerate(sorted((p for p in SEQ.glob("*/A*") if p.is_dir()), key=lambda p: p.name)):
        aid = d.name
        if d.parent.name != bucket(aid):
            problems.append(f"seq/{d.parent.name}/{aid}: move it to seq/{bucket(aid)}/{aid}/")
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
        page = (d / "README.md").read_text(encoding="utf-8")
        ref = bfile(aid)
        recs = []
        selected = (not only or aid in only) and (shard is None or k % shard[1] == shard[0])
        if selected:
            print(f"{aid}  ({len(ref)} terms in b-file)")
        problems += [f"{aid}/{p.name}: only plain Python 3 counts (py3.py, standard library); delete it"
                     for p in sorted(d.glob("py3-*.py"))]
        for prog in sorted(d.glob("py3.py")):
            runs = execute and selected and (to_run is None or aid in to_run)
            rec, probs = check_program(prog, ref, meta, page, runs, to_bar) if selected else (
                {"category": category(prog), "bytes": size(prog)}, [])
            problems += [f"{aid}/{p}" for p in probs]
            if rec:
                recs.append(rec)
                if "status" in rec:
                    timings.append((aid, rec))
        rows.append((aid, meta["name"], recs, min(meta.get("min_terms", len(ref)), len(ref))))

    text = README.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    # Blank lines around the table: without them kramdown (GitHub Pages) reads the
    # comment and the table as one paragraph. GitHub's own renderer does not mind.
    new = f"{head}{START}\n\n{table(rows)}\n\n{END}{tail}"
    if new != text:
        if write:
            README.write_text(new, encoding="utf-8", newline="\n")
            print("README.md records table rewritten")
        else:
            problems.append("README.md records table is out of date: run tools/verify.py --write")

    if report:
        with open(report, "w", encoding="utf-8", newline="\n") as f:
            for aid, r in timings:
                bar, raw = r["bar_seconds"], r["raw_seconds"]
                f.write("\t".join(map(str, (
                    aid, r["bytes"], r["min_terms"], r["timeout"],
                    "" if bar is None else f"{bar:.2f}",
                    "" if bar is None else f"{bar / r['timeout']:.3f}", r["status"],
                    "" if raw is None else f"{raw:.2f}", f"{r['factor']:.3f}"))) + "\n")

    for p in problems:
        print("FAIL", p)
    print("all good" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
