#!/usr/bin/env python3
"""Refuse changes that would weaken the records; run before a branch lands on main.

usage: python tools/guard.py BASE [--strict]

Compared with git BASE, for every sequence that BASE already has:
  - its b-file stays as it is, and so does the bar in meta.json: offset unchanged,
    min_terms not lower, timeout not longer;
  - neither its py3.py, its page nor its meta.json is deleted;
  - a changed py3.py is shorter, unless a commit message since BASE says "fix"
    (a correction of a wrong program may be longer).
New sequences are left to tools/verify.py. With --strict (the ship workflow), a change
outside seq/, bfiles/ and README.md is refused too: tools, workflows and rules go
through a pull request. So is any change to a sequence's review.txt, new sequences
included: a review lands only through a pull request, whose merge is the review.
"""
import json
import re
import subprocess
import sys


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def show(rev, path):
    """The file at rev as bytes, or None."""
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def size(data):
    return len(data) - data.endswith(b"\n")


def check(base, strict):
    problems = []
    fix = re.search(r"\bfix", git("log", "--format=%B", f"{base}..HEAD"), re.I)
    for line in git("diff", "--no-renames", "--name-status", base, "HEAD").splitlines():
        status, path = line.split("\t", 1)
        parts = path.split("/")
        if strict and parts[0] not in ("seq", "bfiles") and path != "README.md":
            problems.append(f"{path}: only seq/, bfiles/ and README.md land without review;"
                            " open a pull request for this")
            continue
        if parts[0] == "bfiles" and len(parts) == 3 and show(base, path) is not None:
            problems.append(f"{path}: the b-file of an existing sequence cannot change")
        if parts[0] != "seq" or len(parts) != 4:
            continue
        if strict and parts[3] == "review.txt":
            problems.append(f"{path}: a review lands only through a pull request"
                            " (python tools/ship.py AXXXXXX --review NOTE)")
            continue
        folder, name = "/".join(parts[:3]), parts[3]
        if show(base, f"{folder}/meta.json") is None:
            continue  # a new sequence
        if status == "D" and name in ("py3.py", "README.md", "meta.json"):
            problems.append(f"{path}: an existing sequence cannot lose it")
        elif name == "py3.py" and show(base, path) is not None:
            old, new = size(show(base, path)), size(show("HEAD", path))
            if new >= old and not fix:
                problems.append(f"{path}: {new} bytes is not shorter than the {old} bytes on main"
                                ' (if the old program is wrong, say "fix" in the commit message)')
        elif name == "meta.json":
            old, new = json.loads(show(base, path)), json.loads(show("HEAD", path))
            if new.get("offset") != old.get("offset"):
                problems.append(f"{path}: the offset cannot change")
            if new.get("min_terms", float("inf")) < old.get("min_terms", float("inf")):
                problems.append(f"{path}: min_terms cannot go down")
            if new.get("timeout", 60) > old.get("timeout", 60):
                problems.append(f"{path}: timeout cannot go up")
    return problems


def main(argv):
    problems = check(argv[0], "--strict" in argv)
    for p in problems:
        print("REFUSED", p)
    print("guard: all good" if not problems else f"guard: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
