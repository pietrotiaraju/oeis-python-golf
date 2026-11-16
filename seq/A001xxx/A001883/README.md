# A001883

> Number of permutations s of {1,2,...,n} such that |s(i)-i|>1 for each i=1,2,...,n.
> — [OEIS A001883](https://oeis.org/A001883)

Offset 0: 1, 0, 0, 0, 1, 4, 29, 206, 1708, 15702, 159737, 1780696, 21599745, …

### Python 3 — 149 bytes

```python
from functools import*
f=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)-sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r+1]if~m&b))
n=0
while[print(+f(n,1,1))]:n+=1
```

**How it works**

- **Rooks.** Let B be the band of the n×n board with |i − j| ≤ 1 (Riordan's
  three-ply staircase) and r_k the number of ways to put k non-attacking
  rooks on B. A set of k such rooks is contained in (n − k)! permutations,
  so by inclusion–exclusion a(n) = Σ_k (−1)^k·r_k·(n − k)!.
- **Rows.** `f` walks down the rows and does the whole sum at once. With r
  rows left the next row is i = n − r + 1, and its band cells are the
  columns i − 1, i, i + 1, bits b = 1, 2, 4. The mask `m` says which of
  columns i − 1 and i are already taken by rooks of earlier rows (bits 0
  and 1); column i + 1 is always free, no earlier row reaches it. A rook in
  column b leaves the mask (m + b) >> 1 for the next row (b is not in m, so
  `m+b` is m | b), an empty row leaves m >> 1.
- **Edges.** Column 0 does not exist: the first call has m = 1. Column n + 1
  does not exist either: in the last row (r = 1) `(1,2,4)[:r+1]` drops
  b = 4.
- **The factorial.** Every rook brings the sign −1. The rows without a rook
  are multiplied by 1, 2, 3, … in turn (`j` is one more than the number of
  such rows so far), so a placement of k rooks gets (−1)^k·(n − k)!, as in
  the sum. `r<1or` ends a placement with `True` (1).
- **The cache.** f(r, m, j) does not depend on n, so one `functools.cache`
  serves all terms: a(n) = f(n, 1, 1) adds only O(n) new states to those of
  a(n − 1). The `+` turns the `True` returned for n = 0 into 1.

**Notes**

- Exact integer arithmetic, straight from the definition, so the program
  is right for every n.
- The recursion goes one or two Python frames deep per row and the cache
  keeps O(n²) big integers (about 400 MB by n = 700), so the default
  recursion limit or the memory stops the program somewhere past n = 500;
  those are interpreter limits. The b-file has 201 terms (n = 0 to 200)
  and the bar is all of them in 60 s, which takes under a second.
- The entry's recurrence a(n) = (n+1)a(n−1) − (n−3)a(n−2) − (n−4)a(n−3) +
  (n−4)a(n−4) + a(n−5) + (−1)ⁿ·L(n−3) (L the Lucas numbers) makes a
  114-byte program that matches the whole b-file, but its derivation is in
  Riordan's unpublished 1963 memorandum (which has a known misprint) and
  is not reproduced here, so it is not the record. Kotesovec's order-7
  recurrence in the entry is not proved there either.
- The same recursion with the band moved to p(i) − i ∈ {0, 1, 2} is
  [A001887](../A001887/), and with a weight x − 1 per rook it gives the
  hit numbers [A001884](../A001884/), [A001885](../A001885/) and
  [A001886](../A001886/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 149 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001883), CC BY-SA 4.0.
