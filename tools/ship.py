#!/usr/bin/env python3
"""Commit sequences on their own branch and push it; the ship workflow then lands it on main.

usage: python tools/ship.py AXXXXXX [AXXXXXX ...] [-b BRANCH] [-m MESSAGE] [--no-push]

Run it from any checkout of the repository. It
  1. finds the worktree of the branch (add/AXXXXXX unless -b is given), or creates one
     in ../oeis-wt/ next to the shared checkout, from origin/main;
  2. moves the sequences' uncommitted files there if they were written in the shared checkout;
  3. runs tools/verify.py on the sequences and rewrites the records table;
  4. commits what changed ("Add AXXXXXX (N bytes)" unless -m is given);
  5. rebases the branch on origin/main, rebuilding the table if it clashes, and pushes it.
Nothing is ever committed in the shared checkout.
"""
import argparse
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


def sizes(wt, aid):
    progs = sorted((wt / paths(aid)[0]).glob("py3*.py"), key=lambda p: (p.stem != "py3", p.stem))
    return ", ".join(f"{p.stem[4:]} {verify.size(p)} bytes".lstrip() for p in progs)


def main(argv=None):
    sys.stdout.reconfigure(line_buffering=True)  # keep our lines in order with verify.py's
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("aids", nargs="+", metavar="AXXXXXX")
    p.add_argument("-b", "--branch", help="branch to use (default add/AXXXXXX)")
    p.add_argument("-m", "--message", help="commit message")
    p.add_argument("--no-push", action="store_true", help="commit and rebase, but do not push")
    a = p.parse_args(argv)
    aids = [x.upper() for x in a.aids]
    if len(aids) > 1 and not a.branch:
        p.error("several sequences need -b BRANCH, for example -b golf/import-math")
    branch = a.branch or f"add/{aids[0]}"

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
    if a.no_push:
        print(f"{branch} is ready in {wt}; not pushed")
        return
    git("push", "-q", "--force-with-lease", "-u", "origin", branch, cwd=wt)
    print(f"pushed {branch}: the ship workflow lands it on main once tools/verify.py passes"
          " (Actions tab on GitHub)")


if __name__ == "__main__":
    main()
