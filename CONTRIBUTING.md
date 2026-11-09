# Rules and how to contribute

## What counts as a program

1. **One program per sequence**, at `seq/AXXXxxx/AXXXXXX/py3.py`: Python 3,
   **standard library only** (no sympy or other packages). Sequences are
   grouped a thousand to a folder named after their first digits, so A000026
   lives in `seq/A000xxx/A000026/` and A300001 in `seq/A300xxx/A300001/`. Its
   b-file follows the same rule: `bfiles/A000xxx/b000026.txt`. A sequence
   may also hold a second, separate record next to it, `py3-N.py`: see
   [Short-bar records](#short-bar-records).
2. **Output:** print the terms in order, starting at the OEIS offset, one term
   per line, and keep going forever (or stop at the end of a finite sequence).
   A program that ends by itself (exit status 0) before printing every term of
   the b-file fails; a crash on an interpreter limit does not. Nothing else goes to stdout; stderr is ignored, so warnings such as the
   `SyntaxWarning` for `1for` are fine.
3. **Interpreter:** CPython 3.12, run as `python -u file.py`, with no other
   command-line flags and no input, alone in an empty folder with an empty
   environment. The program may not read files outside the Python installation
   (the b-files included), write files, list folders, start processes or use the
   network; [`tools/sandbox.py`](tools/sandbox.py) blocks these while it runs.
4. **Size:** the UTF-8 bytes of the file with LF line endings. A single
   trailing newline is not counted.

## What counts as correct

- The program must be **correct for every n**, not only for the terms that get
  checked. Exact arithmetic is expected: floats that happen to round right on
  the b-file are not enough.
- Hard-coding terms is allowed only when the page explains why it is right,
  for example the impossible cases n = 2, 3, 5 in [A300001](seq/A300xxx/A300001/).
  A program that embeds or reads the b-file is not accepted. Where the checked
  terms cannot tell a program from a stored list, a person reads it first: see
  [Review](#review).
- If correctness beyond the b-file rests on a theorem or a conjecture, the
  page must say which.
- Interpreter limits (memory, recursion depth, the 4300-digit int-to-str limit
  of Python 3.11+) are not counted as failures, but the page should mention them.

## Verification

Each sequence's `meta.json` sets a bar: `min_terms` terms, and a `timeout` in
seconds (default: the whole b-file, 60 s). The bar is chosen when the sequence
is added, from what a straightforward program manages, and every program for
that sequence must clear the same bar. Raising it later must not invalidate
existing records.

**The bar must be met within half the timeout.** A time limit is there to tell
algorithms apart, not machines: a smarter method is usually hundreds of times
faster, while two computers differ by a factor of two or three. So a program
counts only if its `min_terms`-th term arrives within **half** of `timeout`;
the other half is margin, so that no verdict hangs on how fast a machine is.

**Times are in reference seconds**, so the verdict is the same on any machine.
Before running programs, and again once a minute, `tools/verify.py` runs the
fixed benchmark [`tools/bench.py`](tools/bench.py) the same way it runs a
program. On a machine where it takes twice `REF_BENCH` (the median of GitHub's
runners), timings count half and timeouts double; on a faster machine, the
other way round. GitHub's own runners differ by up to two times in speed, which
is why plain seconds were not enough; the margin covers what the benchmark
misses. The CI (`ubuntu-latest`, CPython 3.12) remains the official judge.

`tools/verify.py` runs each program, stops it at the timeout, and compares
every printed line with the b-file in [`bfiles/`](bfiles/). A program passes
when every line it printed is right and its `min_terms`-th line came within
half the timeout, in reference seconds. Lines after that are still checked, up to the timeout.
A program that ends by itself before the b-file does fails (rule 2); with
`--to-bar`, `verify.py` waits one more second after the bar to see whether it ends.

The script also checks that each page shows the program verbatim under a
heading `### <category> — <bytes> bytes`, and that the records table in the
[README](README.md) is up to date.

```bash
python tools/verify.py            # everything
python tools/verify.py A300002    # one sequence
python tools/verify.py --write    # also rewrite the records table
python tools/verify.py --since=main  # run only what changed since main
python tools/verify.py --to-bar   # stop each program at min_terms (faster)
```

CI uses `--since`: it runs the programs of the sequences a push or pull
request adds or edits, and checks the pages, sizes and table of all of them.
A program that only moved, unchanged, is not run again.

The `audit` workflow runs every record up to its bar, twelve shards in
parallel, and lists how much of its timeout each one needs. It runs by hand
(Actions → audit → Run workflow) and on every pull request that changes
`tools/verify.py`, so a change of rules is measured against all records first.

## Review

Matching the b-file shows that a program prints the right terms, not that it
computes the sequence. When few terms are required, a list of them can be
shorter than any honest program, and so can a formula that only happens to fit
them. So `tools/verify.py` asks for a person's review when the run cannot vouch
for a program:

- **its terms fit in a table no longer than itself:** a program that only
  stores the `min_terms` required terms (as a list, as a bytes or str literal,
  or as their digits packed two to a byte, plus 40 bytes to unpack them) would
  not be longer; or
- **it spells out terms:** three or more consecutive terms, with 8 or more
  digits in all, appear in its source as numbers in a row, as the code points
  of a string (shifted by a constant or not) or as their digits one after
  another.

Such a program fails until its sequence's `review.txt` holds a line with the
first 12 hex digits of the program's SHA-256 and a note on why it computes the
sequence for every n. `review.txt` changes only through a pull request:
`tools/guard.py` refuses it on the `ship` path, and whoever merges the pull
request has read the program and the page. `python tools/ship.py AXXXXXX
--review "NOTE"` writes the line, pushes a `review/…` branch and opens the pull
request. A golf changes the hash, so every new program needs its own review;
`python tools/verify.py --needs-review` lists the programs that need one and
have none.

The reviewer checks that the page argues for every n (which definition the
program follows, why that agrees with the OEIS entry, which theorem or
conjecture it rests on), that the code does what the page says, and that any
stored data, such as number names, the orders of the sporadic groups or a
finite list, is explained.

## Short-bar records

A bar asks for speed as well as correctness, and for some sequences the speed
costs bytes: the shortest correct method is too slow for the bar. Number of
groups (A000001) is one: six terms in two minutes need a search that fixes the
identity row, while the shortest correct search, over sets of permutations,
reaches a(4) in half a second and would need hours for a(5).

So a sequence may also hold **one short-bar record**, `py3-N.py` next to
`py3.py`, where N is fewer terms than the sequence's bar (A000001 has
`py3-5.py`):

- It follows every rule above except the bar: its first **N** terms must come
  within half the sequence's timeout, in reference seconds. After the N-th
  term `tools/verify.py` waits one more second to see whether it ends.
- N is chosen like the main bar, from what the short method manages: as many
  terms as it reaches comfortably in time, and no fewer. For A000001 that is
  five, because a(5) takes hours. A sequence where a short method reaches
  forty terms gets `py3-40.py`, not `py3-5.py`.
- A later short-bar record must be shorter, at a bar of N or more terms; it may
  replace `py3-N.py` by `py3-M.py` with M ≥ N, never with M < N.
- It must still be correct for every n and keep going: only the speed is
  relaxed. A program that knows it will only be asked for N terms (a list, or a
  formula that happens to fit them) is not a record.
- A few terms fit in a table shorter than most programs, so a short-bar record
  usually needs a review: `python tools/ship.py AXXXXXX --review "NOTE"` opens
  the pull request, and its merge approves the program.
- Its page section comes after the main record's, under a heading
  `### Python 3, N terms — <bytes> bytes`, with its own **How it works**; the
  History table records it under the category `Python 3, N terms`.
- It is listed in the README's short-bar table, next to the main record.

## Sending a record

1. Add or replace the program file. For a new sequence, also add
   `seq/AXXXxxx/AXXXXXX/meta.json` (name, offset, `min_terms`, `timeout`), the
   b-file (`bfiles/AXXXxxx/bXXXXXX.txt`, as downloaded from
   `https://oeis.org/AXXXXXX/bXXXXXX.txt`) and a page
   `seq/AXXXxxx/AXXXXXX/README.md` (copy an existing one).
2. Explain the trick on the page and add a line to its history table.
3. Run `python tools/verify.py --write` and open a pull request. CI runs the
   same check for the sequences the pull request changes.

For a sequence that is already here, `tools/guard.py` (run by CI and the `ship`
workflow) holds the line:

- a new `py3.py` (or `py3-N.py`) must be **shorter** than the one it replaces. A correction of a
  program found wrong may be longer, if a commit message says "fix";
- the b-file and the bar in `meta.json` stay as they are (same offset,
  `min_terms` not lower, `timeout` not longer), and the program, page and
  `meta.json` are not deleted.

With write access to this repository there is a shorter way: push a branch
named `add/…` (new sequences) or `golf/…` (shorter records), for example with
`python tools/ship.py AXXXXXX`. The `ship` workflow merges it into `main`, runs
the guard and the programs it adds or changes, rebuilds the records table and
deletes the branch; if a check fails, nothing reaches `main`. Only `seq/`,
`bfiles/` and `README.md` land this way, and not a `review.txt`: reviews,
changes to tools, workflows or these rules go through a pull request.

Every record here is the **shortest known**, never a proof of minimality: see
[the README](README.md#why-shortest-known).
