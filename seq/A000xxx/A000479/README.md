# A000479

> Number of 1-factorizations of K_{n,n}.
> — [OEIS A000479](https://oeis.org/A000479)

Offset 0: 1, 1, 1, 2, 24, 1344, 1128960, 12198297600, 2697818265354240, 15224734061278915461120, …

### Python 3 — 259 bytes

```python
from functools import*
from itertools import*
n=0
while 1:
 L=[sum(1<<(i*n+j)for i,j in enumerate(p))for p in permutations(range(n))]
 @cache
 def F(E):
  if not E:return 1
  p=E&-E
  return sum(F(E^x)for x in L if x&p and x&E==x)
 print(F((1<<(n*n))-1));n+=1
```

**How it works**

- A perfect matching of K_(n,n) pairs each left vertex i with
  exactly one right vertex p[i], where p is a permutation of
  0,…,n−1. Enumerating those permutations gives all n!
  matchings without repetitions.
- Encode edge (i,j) as bit i·n+j. Each matching mask is the
  sum of its n distinct bits, and `(1<<(n*n))-1` is the
  mask of every edge of the complete bipartite graph.
- F(E) counts partitions of the remaining edges into matchings.
  Return 1 for E=0. Otherwise isolate the least remaining edge
  p and sum `F(E^x)` over matching masks containing p and
  contained in E.
- Each factorization has exactly one matching covering p, so
  this forces a unique removal order. The factors are unordered,
  and no division by their possible orderings is needed.
- `@cache` reuses counts for identical remaining-edge masks.
  The function is redefined inside the size loop, keeping every
  cache tied to its own n and matching list.
- At n=0 the complete mask is zero and F immediately returns 1,
  the unique empty factorization. Thereafter n increments by one,
  rather than by two as in the complete-graph program.

**Notes**

- Both vertex parts remain labeled. This counts factorizations
  themselves, without identifying them under graph automorphisms.
- Labeling the n matching factors by n symbols produces a Latin
  square: the symbol in cell (i,j) names the factor containing
  that edge. Every factorization gives n! such symbol labelings.
  For n=3 there are 12 labeled Latin squares, hence 12/3!=2
  factorizations, the first value exceeding one.
- The masks and recurrence are exact. Each recursion removes n
  edges, so its depth is n, but the number of cached masks and
  the n! matching candidates make large sizes expensive.
- [A000438](../A000438/) uses the same exact-cover recurrence
  on K_(2n), whose matchings require a different generator and
  whose edge set has a different size.
- The b-file has 12 terms (indices 0 through 11). The bar is the
  first 6 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 259 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000479), CC BY-SA 4.0.
