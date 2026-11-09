#!/usr/bin/env python3
"""Commit sequences on their own branch and push it; the ship workflow then lands it on main.

usage: python tools/ship.py AXXXXXX [AXXXXXX ...] [-b BRANCH] [-m MESSAGE] [--no-push]
                            [--review NOTE]

Run it from any checkout of the repository. It
  1. finds the worktree of the branch (add/AXXXXXX unless -b is given), or creates one
     in ../oeis-wt/ next to the shared checkout, from origin/main;
  2. moves the sequences' uncommitted files there if they were written in the shared checkout;
  3. runs tools/verify.py on the sequences and rewrites the records table;
  4. commits what changed ("Add AXXXXXX (N bytes)" unless -m is given);
  5. rebases the branch on origin/main, rebuilding the table if it clashes, and pushes it.
Nothing is ever committed in the shared checkout.

A program that tools/verify.py says needs a review (its terms would fit in a table no
longer than itself, or it spells out terms) cannot land by itself. With --review NOTE,
where NOTE says why the program computes the sequence for every n, ship.py adds its hash
and NOTE to the sequence's review.txt, pushes the branch (review/AXXXXXX unless -b is
given) and opens a pull request that shows the program and the page's argument. The
user's merge is the review.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import verify


def git(*args, cwd, check=True):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and r.returncode:
        sys.exit(f"git {' '.join(args)}: {(r.stderr or r.stdout).strip()}")
    return r


def blob(repo, name):
    """The file as committed at HEAD in repo, or None."""
    r = subprocess.run(["git", "show", f"HEAD:{name}"], cwd=repo, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def worktrees(repo):
    """{branch: path} for every worktree of the repository."""
    found, path = {}, None
    for line in git("worktree", "list", "--porcelain", cwd=repo).stdout.splitlines():
        if line.startswith("worktree "):
            path = Path(line[len("worktree "):]).resolve()
        elif line.startswith("branch refs/heads/"):
            found[line[len("branch refs/heads/"):]] = path
    return found


def paths(aid):
    """The sequence's folder and b-file, relative to a checkout."""
    b = verify.bucket(aid)
    return [f"seq/{b}/{aid}", f"bfiles/{b}/b{aid[1:]}.txt"]


def bring(shared, wt, aid):
    """Move the sequence's uncommitted files from the shared checkout into the worktree."""
    status = git("status", "--porcelain", "--untracked-files=all", "--", *paths(aid), cwd=shared).stdout
    for line in status.splitlines():
        code, name = line[:2], line[3:]
        src, dst = shared / name, wt / name
        if not src.is_file():
            continue
        data = src.read_bytes()
        if dst.is_file() and dst.read_bytes() != data and dst.read_bytes() != blob(shared, name):
            print(f"kept {dst}: it differs from {src}, which is left as it is")
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
        if code == "??":
            src.unlink()
        else:
            git("checkout", "HEAD", "--", name, cwd=shared)
        print(f"moved {name} out of the shared checkout")
    for folder in (shared / paths(aid)[0],):
        try:
            folder.rmdir()
        except OSError:
            pass


def rebuild_table(wt):
    subprocess.run([sys.executable, "tools/verify.py", "--no-run", "--write"], cwd=wt, capture_output=True)
    git("add", "README.md", cwd=wt)


def rebase(wt):
    """Rebase the branch on origin/main; a clash in the records table is settled by rebuilding it."""
    r = git("rebase", "--autostash", "origin/main", cwd=wt, check=False)
    while r.returncode:
        clashes = git("diff", "--name-only", "--diff-filter=U", cwd=wt).stdout.split()
        if clashes != ["README.md"]:
            git("rebase", "--abort", cwd=wt, check=False)
            sys.exit(f"rebase on origin/main stopped ({', '.join(clashes) or 'no clash'}): "
                     f"{(r.stderr or r.stdout).strip()}")
        git("checkout", "--ours", "README.md", cwd=wt)  # during a rebase "ours" is main
        rebuild_table(wt)
        r = git("-c", "core.editor=true", "rebase", "--continue", cwd=wt, check=False)


def programs(folder):
    """The sequence's record and, if it has one, its short-bar record."""
    shorts = sorted((p for p in folder.glob("py3-*.py") if verify.short_terms(p)), key=verify.short_terms)
    return [p for p in (folder / verify.MAIN, *shorts) if p.exists()]


def sizes(wt, aid):
    return ", ".join(f"{f'{verify.short_terms(p)} terms: ' if verify.short_terms(p) else ''}{verify.size(p)} bytes"
                     for p in programs(wt / paths(aid)[0]))


def note_reviews(wt, aids, note):
    """Add NOTE to review.txt for every program of these sequences that needs a review.

    Return {AXXXXXX: {hash: why it needs one}}."""
    out = subprocess.run([sys.executable, "tools/verify.py", *aids, "--needs-review"], cwd=wt,
                         capture_output=True, text=True).stdout
    why = {}
    for line in out.splitlines():
        m = re.fullmatch(r"(A\d{6}) ([0-9a-f]{12}) # (.*)", line)
        if not m:
            continue
        aid, digest, reason = m.groups()
        why.setdefault(aid, {})[digest] = reason
        path = wt / paths(aid)[0] / "review.txt"
        old = path.read_text(encoding="utf-8") if path.exists() else (
            "# Programs read and approved: the first 12 hex digits of the SHA-256 of the program, then why\n"
            "# it computes the sequence for every n. This file changes only through pull requests.\n")
        path.write_text(f"{old}{digest} {note}\n", encoding="utf-8", newline="\n")
    if not why:
        sys.exit("no program here needs a review: ship it without --review")
    return why


def open_review(wt, branch, aids, why, note):
    """Open the pull request whose merge approves the programs."""
    parts = []
    for aid in aids:
        folder = wt / paths(aid)[0]
        page = (folder / "README.md").read_text(encoding="utf-8")
        for prog in programs(folder):
            reason = why.get(aid, {}).get(verify.digest(prog))
            if reason is None:
                continue
            # The argument under this program's heading, up to the page's next section.
            section = page.split(f"### {verify.category(prog)} — ", 1)[-1]
            argument = section.split("**How it works**", 1)[-1].split("\n## ", 1)[0].strip()
            program = prog.read_text(encoding="utf-8").rstrip()
            parts.append(f"## {aid}, {verify.category(prog)}\n\nNeeds a review: {reason}.\n\n"
                         f"```python\n{program}\n```\n\n**How it works** (from the page)\n\n{argument}\n")
    body = (f"Review note: {note}\n\n" + "\n".join(parts) +
            "\nMerging this pull request approves these programs: their hashes are in review.txt,"
            " so tools/verify.py lets them pass.\n")
    title = "Review: " + git("log", "-1", "--format=%s", cwd=wt).stdout.strip()
    r = subprocess.run(["gh", "pr", "create", "--base", "main", "--head", branch, "--title", title,
                        "--body", body], cwd=wt, capture_output=True, text=True)
    print(r.stdout.strip() or f"gh pr create failed: {r.stderr.strip()}")


def main(argv=None):
    sys.stdout.reconfigure(line_buffering=True)  # keep our lines in order with verify.py's
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("aids", nargs="+", metavar="AXXXXXX")
    p.add_argument("-b", "--branch", help="branch to use (default add/AXXXXXX)")
    p.add_argument("-m", "--message", help="commit message")
    p.add_argument("--no-push", action="store_true", help="commit and rebase, but do not push")
    p.add_argument("--review", metavar="NOTE", help="for programs that need a review: record NOTE (why"
                   " the program computes the sequence) and open a pull request instead of landing")
    a = p.parse_args(argv)
    aids = [x.upper() for x in a.aids]
    if len(aids) > 1 and not a.branch:
        p.error("several sequences need -b BRANCH, for example -b golf/import-math")
    branch = a.branch or f"{'review' if a.review else 'add'}/{aids[0]}"
    if a.review and branch.startswith(("add/", "golf/")):
        p.error("--review needs a branch outside add/ and golf/, which land by themselves")

    common = git("rev-parse", "--path-format=absolute", "--git-common-dir", cwd=verify.ROOT).stdout.strip()
    shared = Path(common).resolve().parent
    git("fetch", "-q", "origin", cwd=shared)
    wt = worktrees(shared).get(branch)
    if wt == shared:
        sys.exit(f"{branch} is checked out in the shared checkout {shared}: switch it there to main first")
    if wt is None:
        wt = shared.parent / "oeis-wt" / branch.split("/", 1)[-1]
        if git("rev-parse", "-q", "--verify", f"refs/heads/{branch}", cwd=shared, check=False).returncode == 0:
            git("worktree", "add", "-q", str(wt), branch, cwd=shared)
        else:
            git("worktree", "add", "-q", "-b", branch, str(wt), "origin/main", cwd=shared)
        print(f"worktree {wt} on {branch}")

    for aid in aids:
        bring(shared, wt, aid)
        if not (wt / paths(aid)[0]).is_dir():
            sys.exit(f"{aid}: no {paths(aid)[0]} in {wt}")
    why = note_reviews(wt, aids, a.review) if a.review else {}
    if subprocess.run([sys.executable, "tools/verify.py", *aids, "--write"], cwd=wt).returncode:
        sys.exit("tools/verify.py failed: nothing committed")

    git("add", "--", *(x for aid in aids for x in paths(aid)), "README.md", cwd=wt)
    if git("diff", "--cached", "--quiet", cwd=wt, check=False).returncode:
        if a.message:
            message = a.message
        elif len(aids) == 1:
            new = git("cat-file", "-e", f"origin/main:{paths(aids[0])[0]}/meta.json", cwd=wt, check=False).returncode
            message = f"{'Add' if new else 'Update'} {aids[0]} ({sizes(wt, aids[0])})"
        else:
            message = "Update " + ", ".join(aids)
        git("commit", "-q", "-m", message, cwd=wt)
        print(f"committed on {branch}: {message}")

    rebase(wt)
    if git("rev-list", "--count", "origin/main..HEAD", cwd=wt).stdout.strip() == "0":
        sys.exit(f"{branch} has nothing that main does not have already")
    rebuild_table(wt)
    if git("diff", "--cached", "--quiet", cwd=wt, check=False).returncode:
        git("commit", "-q", "--amend", "--no-edit", cwd=wt)
    # The rules may have changed on main since the worktree was made: check with main's verify.py
    # now, or the ship workflow would refuse the branch after we report it pushed.
    check = subprocess.run([sys.executable, "tools/verify.py", "--no-run"], cwd=wt, capture_output=True, text=True)
    if check.returncode:
        fails = "\n".join(x for x in check.stdout.splitlines() if x.startswith("FAIL"))
        sys.exit(f"after the rebase on origin/main, tools/verify.py fails; not pushed:\n{fails}")
    strict = [] if a.review else ["--strict"]  # a review branch carries review.txt, which --strict refuses
    guard = subprocess.run([sys.executable, "tools/guard.py", "origin/main", *strict], cwd=wt,
                           capture_output=True, text=True)
    if guard.returncode:
        refused = "\n".join(x for x in guard.stdout.splitlines() if x.startswith("REFUSED"))
        sys.exit(f"tools/guard.py refuses the branch; not pushed:\n{refused}")
    if a.no_push:
        print(f"{branch} is ready in {wt}; not pushed")
        return
    git("push", "-q", "--force-with-lease", "-u", "origin", branch, cwd=wt)
    if a.review:
        open_review(wt, branch, aids, why, a.review)
        print(f"pushed {branch}: it lands on main when the user merges the pull request")
        return
    print(f"pushed {branch}: the ship workflow lands it on main once tools/verify.py passes"
          " (Actions tab on GitHub)")


if __name__ == "__main__":
    main()
