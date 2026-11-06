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

The definition identifies row permutations and excludes zero
rows and repeated rows. Thus each matrix is one n-element
subset of the nonzero binary n-vectors. Enumerate these subsets
with combinations. The function performs integer Gaussian
elimination: swap in a nonzero pivot, then replace a lower
row by pivot*row-entry*pivot_row. This preserves rational rank
and introduces no division. Failure to find a pivot means the
matrix is singular. Sum that indicator over the row subsets.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 5 terms in 10 s; the official b-file contains 9 terms.
- Enumeration grows as C(2^n-1,n). The bar includes all five values through 5 by 5 matrices, including the first nonzero singular counts.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 357 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000410), CC BY-SA 4.0.
