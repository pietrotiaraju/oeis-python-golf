# A000386

> a(n) = A058057(n,n-3).
> — [OEIS A000386](https://oeis.org/A000386)

Offset 0: 0, 0, 0, 1, 6, 20, 134, 915, 7324, 65784, 657180, 7223637, …

### Python 3 — 107 bytes

```python
from math import*
n=0
while[print(-sum((-1)**k*perm(n-k)*comb(k,3)*comb(2*n-k,k)for k in range(n+1)))]:n+=1
```

**How it works**

- [A058057](https://oeis.org/A058057) is the triangle of the "straight"
  ménage hit polynomials: the permanent of the n×n matrix with x where
  0 ≤ i − j ≤ 1 and 1 elsewhere. So a(n) counts the permutations p of
  [n] with exactly 3 hits, a hit being p(i) ∈ {i, i+1}; a brute-force
  count agrees for n ≤ 8.
- The 2n − 1 forbidden cells form a path in which neighbouring cells
  share a row or a column, so k non-attacking rooks on them are k
  pairwise non-adjacent cells of the path: r_k = C(2n−k, k). By
  inclusion–exclusion, Σ_k r_k·(n−k)!·(y−1)^k counts the permutations by
  y^(hits), and its y³ coefficient is
  a(n) = −Σ_k (−1)^k·(n−k)!·C(k, 3)·C(2n−k, k), the formula of
  S. Manyama in the entry.
- `perm(n-k)` is the factorial (one-argument `math.perm`). k runs over
  0 … n; the terms with k < 3 vanish because C(k, 3) = 0, and for n < 3
  the sum is 0.

**Notes**

- Exact integer arithmetic, correct for every n. Each term is a sum of
  n + 1 products, and the whole b-file (451 terms, n = 0 to 450) prints
  in a few seconds; about 970 terms come out in 30 s. The bar is the
  whole b-file in 60 s.
- The other form of the same sum, Σ_j (−1)^(n−j−3)·j!·C(n+j, 2j)·C(n−j, 3)
  (from the g.f. Σ_j j!·t^j/(1 − (y−1)t)^(2j+1) of V. Jovovic), is
  longer, and so is reading digit 3 of the hit polynomial at y = B.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000386), CC BY-SA 4.0.
