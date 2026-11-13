# A001665

> Number of self-avoiding n-step walks on Kagome lattice.
> — [OEIS A001665](https://oeis.org/A001665)

Offset 0: 1, 4, 12, 32, 88, 240, 652, 1744, 4616, 12208, …

The kagome lattice: corner-sharing triangles, every point has four
neighbours (two in each of its two triangles). A walk starts at a point,
makes n steps along edges and never visits a point twice; a(n) counts these
walks (all directions, no symmetry reduction). The kagome lattice is
vertex-transitive, so the start does not matter. The entry notes that
Fisher and Sykes had wrong values for a(12) and a(13); the program agrees
with the corrected data.

### Python 3 — 126 bytes

```python
f=lambda p,S:n<len(S)or sum(f(w,S|{w})for d in(1,B,B-1)for w in{p+d,p-d}-S if~w&B+1)
n=B=0
while[print(+f(n,{n}))]:n+=1;B=2<<n
```

**How it works**

- Triangular lattice in skew coordinates (i, j): the six neighbours of a
  point are (i ± 1, j), (i, j ± 1) and ±(i + 1, j − 1). Deleting the points
  with i and j both odd (one coset of the sublattice 2·ℤ²) leaves the
  kagome lattice: every remaining point keeps exactly four of its six
  neighbours, two triangles that share only that point, and the edges
  between remaining points are the kagome edges.
- Code: (i, j) ↦ i + jB, so the six steps are `p±d` for d = 1, B, B − 1.
  For n steps B = 2ⁿ⁺¹ (`B=2<<n`) and the walk starts at (n, 0), the code n:
  then i stays in [0, 2n] ⊂ [0, B), so i = p mod B and j = ⌊p/B⌋ for every
  point of the walk (Python's floor division also for negative j). The code
  is one-to-one on all these points, and `S` is an exact visited set.
- With B a power of two, bit 0 of p is the parity of i and bit n + 1 the
  parity of j. A point is deleted exactly when both bits are set, i.e. when
  `~w&B+1` (the complement's bits 0 and n + 1) is 0; the filter keeps the
  others.
- `f(p,S)` counts the ways to finish a walk standing at p with visited set
  S; it is complete when it has n + 1 points (`n<len(S)`) and then scores
  `True`, printed as 1 by the `+`. For n = 0, B = 0 is never used.

**Golf notes**

- One parity condition cannot pick out a coset of 2·ℤ² from a linear code
  (ℤ²/2ℤ² is not cyclic), so the test needs two bits, and the start must
  keep i away from the "seam" where p mod B wraps around.
- Using B as the only counter (`B<2<<len(S)`, start `B//2`, `B*=2`) or
  complex points (`w.real*w.imag%2<1`) costs as much or more.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator); the default recursion limit would
  matter only near n = 490.
- The time grows like the number of walks (about 2.56ⁿ): a(15) comes after
  about 30 s here and a(16) would need well over a minute.
- The b-file has 32 terms (a(0) to a(31)); the bar is 16 terms (up to
  a(15)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 126 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001665), CC BY-SA 4.0.
