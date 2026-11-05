# Working in this repository

Several Claude sessions work here at the same time, usually one per sequence, and
the main checkout is shared between them. Rules and layout are in
[CONTRIBUTING.md](CONTRIBUTING.md); a sequence lives in `seq/AXXXxxx/AXXXXXX/`
and its b-file in `bfiles/AXXXxxx/bXXXXXX.txt`.

Only plain Python 3 counts: one `py3.py` per sequence, standard library only.
Don't write `py3-sympy.py` or any other library version, and don't add "with
sympy it would be N bytes" notes to the pages: `tools/verify.py` refuses
`py3-*.py` files.

## Your own worktree

Never commit, switch branches, reset, stash or `git add -A` in the shared
checkout: other sessions have uncommitted work there. Before writing any file,
make a worktree of your own next to it and work only there:

```bash
git fetch origin
git worktree add ../oeis-wt/AXXXXXX -b add/AXXXXXX origin/main
```

(run from the shared checkout; for changes to existing records use a branch
`golf/<short-name>` instead).

## Shipping

When `python tools/verify.py AXXXXXX` passes, ship it from your worktree:

```bash
python tools/ship.py AXXXXXX
```

It moves your files over if you wrote them in the shared checkout, rewrites the
records table, commits ("Add AXXXXXX (N bytes)"), rebases on `origin/main` and
pushes the branch. The `ship` workflow on GitHub then runs the check again and
lands the branch on `main` by itself: no pull request and no merge button.
Several sequences or a golf of existing ones: `python tools/ship.py A000003
A000011 -b golf/import-math -m "A000003, A000011: import math (-1 byte each)"`.

Don't open pull requests for sequence work, and don't edit the records table by
hand: `tools/verify.py --write` rebuilds it.

`tools/guard.py` refuses, for sequences already on `main`: a `py3.py` that is not
shorter (unless the old one is wrong and a commit message says "fix"), any change
to their b-file, a lower `min_terms`, a longer `timeout` or a new offset in
`meta.json`, and deleting their program, page or `meta.json`. The `ship` workflow
also refuses anything outside `seq/`, `bfiles/` and `README.md`: changes to
`tools/`, workflows, `CLAUDE.md` or `CONTRIBUTING.md` need a pull request that
the user merges.
