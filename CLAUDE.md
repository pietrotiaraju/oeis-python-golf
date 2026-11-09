# Working in this repository

Several Claude sessions work here at the same time, usually one per sequence, and
the main checkout is shared between them. Rules and layout are in
[CONTRIBUTING.md](CONTRIBUTING.md); a sequence lives in `seq/AXXXxxx/AXXXXXX/`
and its b-file in `bfiles/AXXXxxx/bXXXXXX.txt`.

Only plain Python 3 counts: one `py3.py` per sequence, standard library only.
The one exception is a short-bar record, `py3-N.py` (CONTRIBUTING.md, Short-bar
records): at most one per sequence, same rules, but its bar is the first N terms,
N fewer than the main bar and set from what the short method manages; it usually
needs a review pull request.
Don't write `py3-sympy.py` or any other library version, and don't add "with
sympy it would be N bytes" notes to the pages: `tools/verify.py` refuses any
other `py3-*.py` file.

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

If `tools/verify.py` says a program **needs a review** (its required terms would
fit in a table no longer than the program, or its source spells out terms), it
cannot land by itself: matching the b-file does not show that it computes the
sequence. Make sure the page's "How it works" argues for every n, then ship it
on its own with `python tools/ship.py AXXXXXX --review "why it computes the
sequence for every n"`. That records the note in the sequence's `review.txt`,
pushes `review/AXXXXXX` and opens the one kind of pull request sequence work
uses; the user's merge is the review. Ship the rest of a lot without it. Never
write `review.txt` yourself, and never store terms to get under a bar.

`tools/guard.py` refuses, for sequences already on `main`: a `py3.py` that is not
shorter (unless the old one is wrong and a commit message says "fix"), any change
to their b-file, a lower `min_terms`, a longer `timeout` or a new offset in
`meta.json`, and deleting their program, page or `meta.json`. The `ship` workflow
also refuses `review.txt` and anything outside `seq/`, `bfiles/` and `README.md`: changes to
`tools/`, workflows, `CLAUDE.md` or `CONTRIBUTING.md` need a pull request that
the user merges.
