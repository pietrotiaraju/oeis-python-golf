# A000410

> Number of singular n X n rational (0,1)-matrices.
> — [OEIS A000410](https://oeis.org/A000410)

Offset 1: 0, 0, 6, 425, 65625, 27894671, 35716401889, 144866174953833, 1923407307449265675, …

### Python 3 — 357 bytes

```python
from itertools import*
n=1
def s(V):
 A=[[(x>>i)&1 for i in R]for x in V]
 for i in R:
  p=next((j for j in range(i,n)if A[j][i]),-1)
  if p<0:return 1
  A[i],A[p]=A[p],A[i]
  for j in range(i+1,n):
   b=A[j][i]
   if b:A[j]=[x*A[i][i]-y*b for x,y in zip(A[j],A[i])]
 return 0
while 1:
 R=range(n);print(sum(s(V)for V in combinations(range(1,1<<n),n)));n+=1
```

**How it works**

- The OEIS count identifies row permutations and requires distinct,
  nonzero rows. Encode each binary row by an integer from 1 through
  2ⁿ−1. `combinations(...,n)` then chooses every permitted row
  set once, with no additional division by n!.
- s(V) expands the selected integers into an n×n matrix using
  their bits. It tests rank over the rationals, not over the
  two-element field; integer arithmetic keeps that distinction exact.
- In column i, search rows i through n−1 for a nonzero pivot.
  If none exists, the matrix is singular and the function returns 1.
  Otherwise swap that row into position i.
- For each lower row j with entry b in the pivot column, replace
  row_j by A[i][i]·row_j−b·row_i. Its pivot-column entry
  becomes zero. Multiplication by a nonzero pivot and subtraction
  preserve rational rank, without introducing fractions.
- Successful pivots in all n columns establish full rank, returning
  0. The outer sum therefore counts precisely the singular row
  sets. The size starts at n=1 and advances after each output.

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
- Only one row set and its matrix are needed at a time. The program
  is a complete finite enumeration at each size, with no stored
  sequence values or floating-point rank tolerance.
- The b-file has 9 terms (indices 1 through 9). The bar is the
  first 5 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 357 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000410), CC BY-SA 4.0.
