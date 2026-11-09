#!/usr/bin/env python3
"""Check every golfed program against its OEIS b-file and keep the README records table in sync.

usage: python tools/verify.py [AXXXXXX ...] [--write] [--no-run] [--since=REF]
                              [--to-bar] [--shard=I/N] [--report=PATH] [--needs-review]

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
  --needs-review print `AXXXXXX HASH reason` for every program that needs a review
                 and none in its review.txt (implies --no-run)

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

Matching the b-file shows that a program prints the right terms, not that it computes
the sequence. So a program also needs a person's review when the run cannot tell it
from a stored list of the answers:
  - its min_terms terms fit in a table program no longer than itself (table_bytes), or
  - its source spells out three or more consecutive terms with 8 or more digits in all
    (spelled_terms), which the rules allow only when the page explains why.
Such a program fails until the sequence's review.txt holds a line `HASH note` for it
(HASH from --needs-review). tools/guard.py keeps review.txt off the ship path, so it
changes only through a pull request: whoever merges it has checked that the page
argues for every n.

A program that ends by itself (exit status 0) before the b-file does fails too, unless
meta.json says "finite": true. A crash after the bar (recursion, memory, the 4300-digit
limit) is still not a failure.

A sequence may also hold one short-bar record, py3-N.py with N fewer than its bar: the
same rules, but its bar is the first N terms within half the timeout, and it is always
run as with --to-bar. It is listed in the README's second table.
"""
import ast
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import tokenize
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEQ = ROOT / "seq"
BFILES = ROOT / "bfiles"
README = ROOT / "README.md"
GRACE = 1  # with --to-bar, seconds to wait after the bar to see whether the program ends
START, END = "<!-- records:start -->", "<!-- records:end -->"
SHORT_START, SHORT_END = "<!-- short:start -->", "<!-- short:end -->"
MAIN = "py3.py"  # the record; py3-N.py is the optional short-bar record (SHORT)
SHORT = re.compile(r"py3-([1-9][0-9]*)\.py")
DEFAULT_TIMEOUT = 60
MARGIN = 0.5  # min_terms must arrive within this share of the timeout
REF_BENCH = 0.265  # seconds tools/bench.py takes on a typical GitHub runner (median of 11, 2026-11-08)
RECALIBRATE = 60  # seconds after which the speed factor is measured again
_speed = [None, 0.0]  # [factor, time.monotonic() when measured]
NAME_WIDTH = 70


def short_terms(prog):
    """N for a short-bar record py3-N.py, else None."""
    m = SHORT.fullmatch(prog.name)
    return int(m[1]) if m else None


def category(prog):
    """py3.py -> 'Python 3', py3-5.py -> 'Python 3, 5 terms'."""
    n = short_terms(prog)
    return f"Python 3, {n} terms" if n else "Python 3"


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
        if path.name == "review.txt":  # a review does not change what the program prints
            continue
        if path.parts[0] == "seq" and len(path.parts) > 3:
            aids.add(path.parts[2])
        elif path.parts[0] == "bfiles" and path.stem.startswith("b"):
            aids.add("A" + path.stem[1:])
    return aids


def table_bytes(terms):
    """A low estimate of the shortest program that only stores these terms and prints them.

    The least of: a list literal, `print(*[1,2,3],sep='\\n')`; a bytes literal of the
    values when they are all ASCII; a string of code points, `print(*map(ord,'…'),sep='\\n')`;
    and the digits packed about two to a byte, plus 40 bytes to unpack them."""
    best = min(len("print(*[],sep='\\n')") + len(",".join(terms)),
               40 + (sum(map(len, terms)) + len(terms) + 1) // 2)
    try:
        v = [int(t) for t in terms]
    except ValueError:
        return best
    escaped = (0, 10, 13, 39, 92)  # NUL, the line breaks, the quote and the backslash need an escape
    if all(0 <= x < 128 for x in v):
        best = min(best, len("print(*b'',sep='\\n')") + sum(1 + (x in escaped) for x in v))
    if all(0 <= x < 0x110000 for x in v):
        cost = lambda x: 2 if x in escaped else 6 if 0xD800 <= x < 0xE000 else len(chr(x).encode())
        best = min(best, len("print(*map(ord,''),sep='\\n')") + sum(map(cost, v)))
    return best


def literals(src):
    """What a source spells out: [(its int constants in order, True), (each string's code
    points, False), ...] and the digits of each string and int constant."""
    ints, seqs, blobs = [], [], []
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, SyntaxError):
        return [], []
    for t in tokens:
        if t.type not in (tokenize.NUMBER, tokenize.STRING):
            continue
        try:
            v = ast.literal_eval(t.string)
        except (ValueError, SyntaxError):
            continue
        if isinstance(v, int):
            ints.append(v)
            blobs.append(str(abs(v)))
        elif isinstance(v, (str, bytes)):
            seqs.append((list(v) if isinstance(v, bytes) else [ord(c) for c in v], False))
            blobs.append(re.sub(r"\D", "", v.decode("latin-1") if isinstance(v, bytes) else v))
    return [(ints, True)] + seqs, blobs


def spelled_terms(src, terms, k=3, min_digits=8):
    """(index, count) of the longest run of k or more consecutive terms, with min_digits or
    more digits in all, that the source spells out; None if there is none.

    A run counts when it appears as int constants in a row, as the code points of a string
    (also shifted by a constant, which needs k+1 terms) or as the terms' digits one after
    another inside a string or a number. Only the first 500 terms are looked for."""
    terms = terms[:500]
    try:
        v = [int(t) for t in terms]
    except ValueError:
        return None
    best = None

    def keep(j, n):
        nonlocal best
        if n >= k and sum(len(t.lstrip("-")) for t in terms[j:j + n]) >= min_digits:
            if best is None or n > best[1]:
                best = (j, n)

    dv = [b - a for a, b in zip(v, v[1:])]
    exact, shifted = {}, {}
    for j in range(len(v) - k + 1):
        exact.setdefault(tuple(v[j:j + k]), []).append(j)
    for j in range(len(dv) - k + 1):
        shifted.setdefault(tuple(dv[j:j + k]), []).append(j)
    seqs, blobs = literals(src)
    for s, is_int in seqs:
        ds = [b - a for a, b in zip(s, s[1:])]
        for i in range(len(s)):
            for j in exact.get(tuple(s[i:i + k]), ()):
                n = k
                while i + n < len(s) and j + n < len(v) and s[i + n] == v[j + n]:
                    n += 1
                keep(j, n)
            for j in () if is_int else shifted.get(tuple(ds[i:i + k]), ()):
                n = k
                while i + n < len(ds) and j + n < len(dv) and ds[i + n] == dv[j + n]:
                    n += 1
                keep(j, n + 1)
    for blob in blobs:
        for j in range(len(terms) - k + 1):
            if "".join(terms[j:j + k]) in blob:
                n = k
                while j + n < len(terms) and "".join(terms[j:j + n + 1]) in blob:
                    n += 1
                keep(j, n)
    return best


def digest(prog):
    """First 12 hex digits of the SHA-256 of a program, without its trailing newline."""
    return hashlib.sha256(prog.read_bytes().removesuffix(b"\n")).hexdigest()[:12]


def reviewed(folder):
    """Hashes of the programs approved in the sequence's review.txt."""
    path = folder / "review.txt"
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    return {line.split()[0] for line in lines if line.strip() and not line.startswith("#")}


def review_reasons(src, nbytes, ref, min_terms):
    """Why the b-file check alone cannot vouch for a program (empty when it can)."""
    reasons = []
    t = table_bytes(ref[:min_terms])
    if nbytes >= t:
        reasons.append(f"its {min_terms} required terms fit in a {t}-byte table")
    run = spelled_terms(src, ref)
    if run:
        reasons.append(f"it spells out terms {run[0] + 1}-{run[0] + run[1]}")
    return reasons


def run(prog, want, timeout, bar, grace=0):
    """Run prog until it prints `want` lines or `timeout` seconds pass; after `want` lines,
    wait up to `grace` more seconds to see whether it ends by itself.

    Return (lines, seconds, stderr tail, seconds until line `bar` arrived or None, ended),
    where ended is (exit status, lines printed in all) if the program ended by itself."""
    lines, reached, count = [], [], [0]
    enough = threading.Event()
    with tempfile.TemporaryFile() as err, tempfile.TemporaryDirectory() as box:
        # Alone in an empty folder, with the sandbox hook loaded as sitecustomize.
        shutil.copyfile(prog, Path(box) / "py3.py")
        shutil.copyfile(Path(__file__).with_name("sandbox.py"), Path(box) / "sitecustomize.py")
        env = {"PYTHONPATH": box, "PYTHONDONTWRITEBYTECODE": "1"}
        if "SYSTEMROOT" in os.environ:  # Windows needs it to start at all
            env["SYSTEMROOT"] = os.environ["SYSTEMROOT"]
        proc = subprocess.Popen([sys.executable, "-u", "py3.py"], cwd=box, env=env,
                                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=err, text=True)

        eof = []

        def read():
            for line in proc.stdout:
                count[0] += 1
                if count[0] <= want:
                    lines.append(line.strip())
                if count[0] == bar:
                    reached.append(time.monotonic() - t0)
                if count[0] == want:
                    enough.set()
                    if not grace:
                        break
            else:
                eof.append(True)  # the program closed its output: it ended
            enough.set()

        reader = threading.Thread(target=read, daemon=True)
        t0 = time.monotonic()
        reader.start()
        enough.wait(timeout)
        elapsed = time.monotonic() - t0
        if count[0] >= want:
            reader.join(grace)
        ended = None
        if eof:
            try:
                ended = (proc.wait(5), count[0])
            except subprocess.TimeoutExpired:
                pass
        proc.kill()
        proc.wait()
        reader.join()
        err.seek(0)
        tail = err.read().decode(errors="replace").strip().splitlines()[-1:]
    return lines, elapsed, tail, (reached or [None])[0], ended


def speed():
    """How many times slower than the reference this machine is right now (tools/bench.py)."""
    if _speed[0] is None or time.monotonic() - _speed[1] > RECALIBRATE:
        lines, _, tail, _, _ = run(Path(__file__).with_name("bench.py"), 1, 600, 1)
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
    rec = {"category": category(prog), "bytes": nbytes, "hash": digest(prog),
           "review": review_reasons(src, nbytes, ref, min_terms)}
    rec["reviewed"] = rec["hash"] in reviewed(prog.parent)
    if rec["review"] and not rec["reviewed"]:
        problems.append(f"{prog.name} needs a review: {'; '.join(rec['review'])}, so matching the"
                        " b-file does not show that it computes the sequence (Review in CONTRIBUTING.md)")
    if execute:
        timeout = cfg.get("timeout", DEFAULT_TIMEOUT)
        limit = timeout * MARGIN
        page_problems = len(problems)
        f = speed()
        lines, elapsed, tail, raw, ended = run(prog, min_terms if to_bar else len(ref), timeout * f,
                                               min_terms, GRACE if to_bar else 0)
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
        elif ended and ended[0] == 0 and ended[1] < len(ref):
            problems.append(f"{prog.name}: it ended by itself after {ended[1]} terms, but the b-file has"
                            f" {len(ref)}: a program keeps going while the sequence does")
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
    """The records table and the short-bar records table, as markdown."""
    main = "Python 3"
    out = [f"| Sequence | Name | {main} | Terms checked |", "|---" * 4 + "|"]
    out2 = [f"| Sequence | Name | Short record | Its terms | {main} | Terms checked |", "|---" * 6 + "|"]
    for aid, name, recs, terms in rows:
        if len(name) > NAME_WIDTH:
            name = name[:NAME_WIDTH].rsplit(" ", 1)[0] + "…"
        for ch in "\\|*_":  # p|n would split the cell, 3*x^2 + 4*y^2 or p_j^k_j turn italic
            name = name.replace(ch, "\\" + ch)
        by = {r["category"]: r["bytes"] for r in recs}
        link = f"[{aid}](seq/{bucket(aid)}/{aid}/)"
        out.append(f"| {link} | {name} | {f'**{by[main]}**' if main in by else '—'} | {terms} |")
        for r in recs:
            if r.get("short"):
                out2.append(f"| {link} | {name} | **{r['bytes']}** | {r['short']} | {by.get(main, '—')} | {terms} |")
    return "\n".join(out), "\n".join(out2) if len(out2) > 2 else "None yet."


def put(text, start, end, body):
    """Replace what lies between the markers start and end in text."""
    head, rest = text.split(start, 1)
    _, tail = rest.split(end, 1)
    # Blank lines around a table: without them kramdown (GitHub Pages) reads the
    # comment and the table as one paragraph. GitHub's own renderer does not mind.
    return f"{head}{start}\n\n{body}\n\n{end}{tail}"


def main(argv):
    write = "--write" in argv
    needs_review = "--needs-review" in argv
    execute = "--no-run" not in argv and not needs_review
    only = {a.upper() for a in argv if not a.startswith("--")}
    to_bar = "--to-bar" in argv
    since = next((a.split("=", 1)[1] for a in argv if a.startswith("--since=")), None)
    shard = next((tuple(map(int, a.split("=", 1)[1].split("/"))) for a in argv if a.startswith("--shard=")), None)
    report = next((a.split("=", 1)[1] for a in argv if a.startswith("--report=")), None)
    to_run = changed(since) if since else None
    if to_run is not None:
        print(f"changed since {since}: {', '.join(sorted(to_run)) or 'nothing'}")
    problems, rows, timings, pending = [], [], [], []

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
        problems += [f"{aid}/{p.name}: only plain Python 3 counts (py3.py, standard library, and"
                     " one short-bar record py3-N.py); delete it"
                     for p in sorted(d.glob("py3-*.py")) if not short_terms(p)]
        bar = min(meta.get("min_terms", len(ref)), len(ref))
        shorts = sorted((p for p in d.glob("py3-*.py") if short_terms(p)), key=short_terms)
        if len(shorts) > 1:
            problems.append(f"{aid}: one short-bar record at most, not {', '.join(p.name for p in shorts)}")
        problems += [f"{aid}/{p.name}: a short bar must be fewer terms than the bar of {bar}"
                     for p in shorts if short_terms(p) >= bar]
        for prog in [d / MAIN, *shorts]:
            if not prog.exists():
                continue
            n = short_terms(prog)
            cfg = {**meta, "min_terms": n} if n else meta
            runs = execute and selected and (to_run is None or aid in to_run)
            rec, probs = check_program(prog, ref, cfg, page, runs, to_bar or bool(n)) if selected else (
                {"category": category(prog), "bytes": size(prog)}, [])
            problems += [f"{aid}/{p}" for p in probs]
            if rec:
                rec["short"] = n
                recs.append(rec)
                if "status" in rec:
                    timings.append((aid, rec))
                if rec.get("review") and not rec["reviewed"]:
                    pending.append(f"{aid} {rec['hash']} # {prog.name}: {'; '.join(rec['review'])}")
        rows.append((aid, meta["name"], recs, bar))

    if needs_review:
        print("\n".join(pending) or "no program needs a review")
        return 0

    text = README.read_text(encoding="utf-8")
    records, shorts = table(rows)
    new = put(put(text, START, END, records), SHORT_START, SHORT_END, shorts)
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
