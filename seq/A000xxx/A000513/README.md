# A000513

> Number of equivalence classes of n X n matrices over {0,1} with rows and columns summing to 4, where equivalence is defined by row and column permutations. Also number of isomorphism classes of bicolored quartic bipartite graphs, where isomorphism cannot exchange the colors.
> — [OEIS A000513](https://oeis.org/A000513)

Offset 1: 0, 0, 0, 1, 1, 4, 16, 194, 3529, 121790, …

### Python 3 — 596 bytes

```python
from math import*
from functools import*
P=cache(lambda n,m=1:[((j,*p),-z*j*~p.count(j))for j in range(m,n+1)for p,z in P(n-j,j)]if n else[((),1)])
def a(n,k):
 k=min(k,n-k)
 if k<1:return 1>>-k
 T=0;H=factorial(n)**2
 for R,r in P(n):
  for S,s in P(n):
   @cache
   def f(i,j,h,D):
    if i==len(R):return 1
    if j==len(S):return h<1and f(i+1,0,k,[*zip(*sorted(zip(S,D)))][1])
    d=gcd(R[i],S[j]);u=S[j]//d;v=R[i]//d
    return sum(comb(d,t)*f(i,j+1,h-t*u,D[1:]+(D[0]-t*v,))for t in range(min(d,h//u,D[0]//v)+1))
   T+=H//r//s*f(0,0,k,(k,)*len(S))
 return T//H
n=0
while 1:n+=1;print(a(n,4))
```

**How it works**

- Apply Burnside's lemma to the independent row and column permutation
  groups S_n×S_n. `P` generates each cycle type R together with its
  denominator z(R)=∏ⱼ j^mⱼmⱼ!, so its conjugacy class has n!/z(R) elements.
  Adding a part j multiplies the denominator by j times its new multiplicity;
  `-~p.count(j)` is exactly that multiplicity.
- For a row cycle of length r and a column cycle of length s, the cell
  action has d=gcd(r,s) orbits. Selecting t of them has weight C(d,t),
  adds t·s/d ones to each row, and t·r/d ones to each column.
- The cached recurrence `f(i,j,h,D)` visits these cycle pairs. `h` is the
  remaining degree in row cycle i. `D[0]` is the current column-cycle
  deficit; rotating D after each choice brings the next column to the front.
  The bound on t keeps both deficits nonnegative.
- At the end of a row cycle, require h=0 and sort the deficits within
  equal-length column cycles before memoization. Once all rows are filled,
  their total is n·k. The column total is the same and no deficit is negative,
  so every remaining column deficit is zero; the terminal count is 1.
- Put H=(n!)². Each fixed-matrix count has integer weight H/z(R)/z(S);
  sum these weighted counts and divide by H. Complementation gives
  a(n,k)=a(n,n−k); degree 0 has one class and negative degree has none.
  A000519 sums all degrees and removes the all-zero matrix.

The transition bounds keep `h` nonnegative, so `h<1` tests exactly zero.
Sorting `(cycle length, residual degree)` pairs and transposing them
extracts the same tuple of residual degrees. Every partition here is
nonempty (n≥1), so the second transposed component always exists.

In the early case k≤0, `1>>-k` is 1 for k=0 and 0 for every
negative k, exactly the required counts without a Boolean output.

**Notes**

- This is an exact orbit count for every n, including disconnected
  graphs. No color swapping or matrix transposition is included in the
  equivalence relation.
- The zero terms for n below the prescribed degree follow from the
  impossibility of placing more than n ones in a row.
- The state space grows quickly; the verification bar covers the first
  few orders and the program continues with the same exhaustive recurrence.
- The reference file contains 22 terms from the OEIS b-file; the verification
  bar is 8 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 776 | first entry |
| 2026-11-06 | Python 3 | 607 | carry cycle-type denominators and merge the orbit recurrences |
| 2026-11-06 | Python 3 | 596 | transpose sorted residual pairs and short-circuit the zero-degree test |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000513), CC BY-SA 4.0.
