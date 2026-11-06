# A000512

> Number of equivalence classes of n X n matrices over {0,1} with rows and columns summing to 3, where equivalence is defined by row and column permutations.
> — [OEIS A000512](https://oeis.org/A000512)

Offset 1: 0, 0, 1, 1, 2, 7, 16, 51, 224, 1165, …

### Python 3 — 776 bytes

```python
from math import*
from functools import*
@cache
def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1)for p in P(n-j,j)]
def a(n,k):
 if k<0 or k>n:return 0
 k=min(k,n-k)
 if k==0:return 1
 T=0;H=factorial(n)
 for R in P(n):
  w=H//prod(j**R.count(j)*factorial(R.count(j))for j in set(R))
  for S in P(n):
   @cache
   def f(i,D):
    if i==len(R):return int(not any(D))
    r=R[i]
    def g(j,k,E):
     if j==len(S):return f(i+1,tuple(v for s,v in sorted(zip(S,E))))if k==0 else 0
     s=S[j];d=gcd(r,s);u=s//d;v=r//d
     return sum(comb(d,t)*g(j+1,k-t*u,E+(D[j]-t*v,))for t in range(min(d,k//u,D[j]//v)+1))
    return g(0,k,())
   T+=w*(H//prod(j**S.count(j)*factorial(S.count(j))for j in set(S)))*f(0,(k,)*len(S))
 return T//(H*H)
n=0
while 1:n+=1;print(a(n,3))
```

**How it works**

- Apply Burnside's lemma to the independent row and column permutation
  groups S_n×S_n. `P` generates integer partitions, hence one representative
  per permutation cycle type. A type R occurs n!/∏ᵣ r^mᵣmᵣ! times.
- For a row cycle of length r and a column cycle of length s, the cell
  action has d=gcd(r,s) orbits. Selecting t of those orbits has weight
  C(d,t), adds t·s/d ones to each row, and t·r/d ones to each column.
- `g` chooses these orbit counts across one row cycle, enforcing its
  required degree. `f` advances through row cycles and tracks the remaining
  column degrees. Equal-length column cycles are interchangeable, so their
  remaining degrees are sorted before memoization.
- Weight the fixed-matrix counts by the two conjugacy-class sizes and
  divide by (n!)². Complementation gives a(n,k)=a(n,n−k); degree 0 has
  one class. A000519 sums all degrees and removes the all-zero matrix.

**Notes**

- This is an exact orbit count for every n, including disconnected
  graphs. No color swapping or matrix transposition is included in the
  equivalence relation.
- The zero terms for n below the prescribed degree follow from the
  impossibility of placing more than n ones in a row.
- The state space grows quickly; the verification bar covers the first
  few orders and the program continues with the same exhaustive recurrence.
- The reference file contains 28 terms from the OEIS b-file; the verification
  bar is 8 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 776 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000512), CC BY-SA 4.0.
