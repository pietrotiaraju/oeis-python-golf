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

A perfect matching of K_(n,n) is a permutation of its right
vertices. Encode edge (i,j) in bit i*n+j and enumerate these
matching masks. The exact-cover recurrence of [A000438](../A000438/)
counts unordered partitions of all edges into perfect matchings:
the next matching must contain the least uncovered edge,
which selects a unique order for every factorization. The empty
graph at n=0 has one empty factorization.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 6 terms in 10 s; the official b-file contains 12 terms.
- The bar covers n=0 through 5, including the nontrivial counts 2, 24 and 1344. Larger bipartite graphs make the exact-cover search expensive.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 259 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000479), CC BY-SA 4.0.
