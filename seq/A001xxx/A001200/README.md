# A001200

> Number of linear geometries on n (unlabeled) points.
> — [OEIS A001200](https://oeis.org/A001200)

Offset 0: 1, 1, 1, 2, 3, 5, 10, 24, 69, 384, 5250, 232929, 28872973

A linear geometry (linear space) on n points is a family of lines, each with
at least two points, such that every pair of points lies on exactly one line;
a(n) counts them up to relabelling the points. Equivalently: partitions of the
edges of the complete graph K_n into cliques. For n = 0, 1 there are no pairs
and the only space has no lines, for n = 2 the only line is the pair itself, so
a(0) = a(1) = a(2) = 1, as in the data. The known terms (n ≤ 12) come from
computer enumerations (Doyen 1967, Betten and Betten 1999); a short program
can only generate and compare up to isomorphism.

### Python 3 — 338 bytes

```python
from itertools import*
L=[frozenset()];R=[];b=1
while[print(len(L))]:
 W={X|{u|b for u in R}for X in L};R+=b,;Q=[*zip(*permutations(R))]
 for l in range(b):T={l}|{u|b for u in R if l&u};W|={w-T|{l|b}for w in W if T<=w}
 L=[e for e in[*W]if e in W!={*map(W.discard,map(set,zip(*[map(sum,zip(*[q for q in Q if m&q[0]]))for m in e])))}];b*=2
```

**How it works**

- Points are the powers of two in `R`, lines are bitmasks, a space is the
  frozenset of all its lines (the 2-point ones too). `L` holds one labelled
  space per isomorphism class on the points so far; its length is printed.
- Adding a point: deleting a point v from a linear space leaves a linear space
  on the other points (lines through v lose v; those left with one point
  vanish). So every space on n points is a space X on n−1 points plus v, where
  the lines through v are some pairwise disjoint lines of X, each extended by
  v, and a 2-line {u, v} for every point u left over.
- `W` starts as each representative X plus all 2-lines `u|b` to the new point
  `b`. For every old mask `l` in turn, a copy of each `w` that still holds `l`
  and all the 2-lines from `l`'s points to `b` (`T<=w`) gets them replaced by
  the single line `l|b`. A 2-line `u|b` disappears once u is on an extended
  line, so this test is exactly "disjoint from the lines already extended",
  and `W` ends with every extension of every representative, each once.
- Isomorphism classes: every space S on n points is isomorphic to some element
  of `W` (relabel the old points so that S minus the new point becomes its
  representative in `L`; the relabelled S is then one of that
  representative's extensions). The program takes each `e` still in `W`,
  keeps it, and removes its images under all n! permutations from `W`, which
  include every element of `W` isomorphic to it; what is kept is one space per
  class, for every n.
- The images are computed column-wise: `Q` lists, for each point, its image
  under every permutation (the first one is the identity, so `q[0]` is the
  point itself). The image of line `m` under all permutations at once is the
  elementwise sum of the columns of its points, and `zip` over the lines gives
  each permutation's image space.

**Golf notes**

- `set.discard` accepts a set and looks it up as a frozenset, so the images
  are plain `set`s.
- `e in W!={*map(W.discard,…)}` is a chained comparison: the orbit is only
  removed when `e` is still there, and the resulting `{None}` never equals `W`.

**Notes**

- Exact set arithmetic, no theorem beyond the point-deletion argument above.
- The cost is a(n)·n! images: a(8) = 69 comes after about 12 s here, a(9)
  would need 384·9! images (minutes). Memory stays under 100 MB.
- The b-file has the 13 known terms; the bar is 9 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 338 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001200), CC BY-SA 4.0.
