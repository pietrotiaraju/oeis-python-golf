# A000410

> Number of singular n X n rational (0,1)-matrices.
> — [OEIS A000410](https://oeis.org/A000410)

Offset 1: 0, 0, 6, 425, 65625, 27894671, 35716401889, 144866174953833, 1923407307449265675, …

The matrices counted have distinct, nonzero rows and are taken up to
permutation of the rows (OEIS comment by Vladeta Jovovic, 2006): a(n) is the
number of n-element sets of nonzero 0/1 vectors of length n that are linearly
dependent over the rationals. So a(n) = C(2ⁿ − 1, n) − A088389(n).

### Python 3 — 214 bytes

```python
from functools import*
from itertools import*
f=cache(lambda M:M==()or sum((-1)**i*f(M[:i]+M[i+1:])for i,r in enumerate(M)if 2*r>>len(M)&1))
n=1
while[print(sum(0==f(V)for V in combinations(range(1,1<<n),n)))]:n+=1
```

**How it works**

- A row is an integer from 1 to 2ⁿ − 1 whose bit j is the entry in column j.
  `combinations(range(1,1<<n),n)` gives every set of n distinct nonzero rows
  exactly once, in increasing order, so the count is over row sets as the
  definition asks. The row order fixes only the sign of the determinant.
- `f(M)`, for a tuple M of k rows, is the determinant of the k×k matrix formed
  by columns 0 … k−1 of those rows (higher bits are ignored). It is the
  cofactor expansion along the last of these columns, column k−1:
  det = Σᵢ (−1)^(i+k−1)·a_{i,k−1}·det(minor without row i and column k−1).
  The minor is again "columns 0 … k−2 of the remaining k−1 rows", which is
  exactly `f(M[:i]+M[i+1:])`, so the recursion needs no column bookkeeping.
- `2*r>>len(M)&1` is bit k−1 of r, the entry a_{i,k−1}; rows with entry 0
  are skipped. The common factor (−1)^(k−1) is dropped, since only whether
  the determinant is zero matters, so the sign is just `(-1)**i`.
  `M==()or` makes the empty determinant 1.
- `cache` remembers every minor. A minor depends only on its tuple of rows,
  so all matrices of one size share them: at n = 5 the 169911 determinants
  need only 36457 distinct proper minors.
- `0==f(V)` counts the singular ones; `while[print(…)]:` prints a(n) and
  keeps looping, because a one-element list is true.

**Notes**

- Without the cache the same expansion is 184 bytes, but five terms take
  about 11 s here. The fraction-free elimination
  `s=lambda A:bool(A)and(not(p:=next((r for r in A if r[0]),[]))or s([[p[0]*x-r[0]*y for x,y in zip(r[1:],p[1:])]for r in A if r is not p]))`
  on bit lists is 275 bytes and takes about 5.7 s for five terms.
- Rank modulo 2 would count something else: the rows (1,1,0), (1,0,1),
  (0,1,1) are dependent mod 2 but have determinant −2.
  [A000409](../A000409/) counts, with the same row convention, only the
  matrices with a zero column or two equal columns: 350 against 425 at n = 4.
- Exact integer arithmetic over a complete enumeration, so the program is
  right for every n.
- The first five terms take about 1.5 s here. a(6) needs
  C(63, 6) = 67945521 determinants, many hours, and the cache then grows by
  about 20 MB a second.
- The b-file has 9 terms (up to a(9)); the bar is 5 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 357 | first entry |
| 2026-11-06 | Python 3 | 275 | recurse on the fraction-free Schur complement |
| 2026-11-07 | Python 3 | 214 | cached cofactor expansion along the last column |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000410), CC BY-SA 4.0.
