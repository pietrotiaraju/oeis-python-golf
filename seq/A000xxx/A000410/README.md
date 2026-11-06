# A000410

> Number of singular n X n rational (0,1)-matrices.
> — [OEIS A000410](https://oeis.org/A000410)

Offset 1: 0, 0, 6, 425, 65625, 27894671, 35716401889, 144866174953833, 1923407307449265675, …

### Python 3 — 275 bytes

```python
from itertools import*
s=lambda A:bool(A)and(not(p:=next((r for r in A if r[0]),[]))or s([[p[0]*x-r[0]*y for x,y in zip(r[1:],p[1:])]for r in A if r is not p]))
n=1
while 1:
 R=range(n);print(sum(s([[x>>i&1 for i in R]for x in V])for V in combinations(range(1,1<<n),n)));n+=1
```

**How it works**

- The row convention identifies row permutations and requires
  distinct, nonzero rows. The combinations of n integers from
  1 through 2ⁿ−1 choose each permitted row set exactly once.
  Their bits form an n×n integer matrix A.
- The function s tests singularity over the rationals. An empty
  matrix is nonsingular for this recursion. In a nonempty matrix,
  choose the first row p with nonzero first entry; if none exists,
  the first column vanishes and the matrix is singular.
- For every other row r, eliminate its first entry by replacing
  the row with p[0]·r−r[0]·p. This uses a nonzero multiplier,
  so it preserves rank over the rationals without introducing
  fractions. Remove the pivot row and the now-zero first column;
  the original matrix is singular exactly when this smaller
  matrix is singular.
- The expression `r is not p` removes only the chosen row object.
  Other rows with equal values must remain: duplicates reveal a
  rational dependence rather than disappearing from the problem.
- Recurse until a pivot is missing or the matrix is empty. The
  outer sum converts the resulting booleans to integer counts.
  Every count therefore includes all rational dependencies.

**Notes**

- Rank modulo 2 would count a different sequence. For example rows
  (1,1,0), (1,0,1), (0,1,1) have determinant −2: they are
  independent over the rationals, despite dependence modulo 2.
- [A000409](../A000409/) counts only the zero-column or
  repeated-column degeneracies within the same row convention.
  Here all rational dependencies are counted: at n=4 the two
  counts are respectively 350 and 425.
- There are C(2ⁿ−1,n) candidates. Even n=5 already tests
  C(31,5)=169911 matrices, and each elimination takes O(n³)
  arithmetic operations. The division-free updates can also grow
  intermediate integers, so larger sizes become expensive quickly.
- Only one row set and its elimination path are retained at a time.
  The program
  is a complete finite enumeration at each size, with no stored
  sequence values or floating-point rank tolerance.
- The b-file has 9 terms (indices 1 through 9). The bar is the
  first 5 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 357 | first entry |
| 2026-11-06 | Python 3 | 275 | recurse on the fraction-free Schur complement |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000410), CC BY-SA 4.0.
