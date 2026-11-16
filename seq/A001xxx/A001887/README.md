# A001887

> Number of permutations p of {1,2,...,n} such that p(i) - i < 0 or p(i) - i > 2 for all i.
> — [OEIS A001887](https://oeis.org/A001887)

Offset 0: 1, 0, 0, 0, 1, 5, 33, 236, 1918, 17440, 175649, 1942171, 23396353, …

### Python 3 — 147 bytes

```python
from functools import*
f=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)-sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r]if~m&b))
n=0
while[print(+f(n,0,1))]:n+=1
```

**How it works**

- **Rooks.** The forbidden cells are the band B of the n×n board with
  j − i ∈ {0, 1, 2}. If r_k counts the ways to put k non-attacking rooks on
  B, a set of k such rooks lies in (n − k)! permutations, so by
  inclusion–exclusion a(n) = Σ_k (−1)^k·r_k·(n − k)!.
- **Rows.** `f` walks down the rows and does the whole sum at once. With r
  rows left the next row is i = n − r + 1, with band cells in columns i,
  i + 1, i + 2 (bits b = 1, 2, 4). The mask `m` says which of columns i and
  i + 1 earlier rooks already hold (column i + 2 is new to this row). A rook
  in column b leaves (m + b) >> 1 for the next row (`m+b` is m | b since b
  is free), an empty row leaves m >> 1.
- **Edges.** Columns n + 1 and n + 2 do not exist: `(1,2,4)[:r]` keeps
  only column i in the last row and columns i, i + 1 in the one before.
  The first row starts with nothing taken, m = 0.
- **The factorial.** Every rook brings the sign −1, and the rows without a
  rook are multiplied by 1, 2, 3, … in turn (`j` is one more than the
  number of such rows so far), so a placement of k rooks gets
  (−1)^k·(n − k)!. `r<1or` ends a placement with `True` (1).
- **The cache.** f(r, m, j) does not depend on n, so one `functools.cache`
  serves all terms and each new term adds only O(n) states. The `+` turns
  the `True` returned for n = 0 into 1.

**Notes**

- Exact integer arithmetic, straight from the definition, so the program
  is right for every n.
- The recursion goes one or two Python frames deep per row and the cache
  keeps O(n²) big integers (here 400 MB at n = 701, after 9 s), so the
  default recursion limit or the memory stops the program somewhere past
  n = 500; those are interpreter limits. The b-file has 301 terms (n = 0
  to 300) and the bar is all of them in 60 s, about a second here.
- Flajolet's order-8 recurrence in the entry needs nine seeds and eight
  terms with linear coefficients; written out it is about as long as this
  program.
- [A001883](../A001883/) is the same recursion for |p(i) − i| ≤ 1, and with
  a weight x − 1 per rook it gives the hit numbers
  [A001888](../A001888/), [A001889](../A001889/) and [A001890](../A001890/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001887), CC BY-SA 4.0.
