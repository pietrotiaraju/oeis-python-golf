# A000793

> Landau's function g(n): largest order of permutation of n elements. Equivalently, largest LCM of partitions of n.
> — [OEIS A000793](https://oeis.org/A000793)

Offset 0: 1, 1, 2, 3, 4, 6, 6, 12, 15, 20, 30, 30, 60, 60, 84, 105, 140, 210, 210, 420, …

### Python 3 — 116 bytes

```python
from math import*
f=lambda n,m=2,l=1:max([l]+[f(n-k,k+1,lcm(l,k))for k in range(m,n+1)])
n=0
while[print(f(n))]:n+=1
```

**How it works**

- g(n) is the largest lcm of a partition of n. Only the set of distinct
  parts ≥ 2 matters: repeated parts and 1s do not change the lcm, and
  any set of distinct parts with sum ≤ n becomes a partition of n by
  adding 1s. So g(n) is the largest lcm over sets of distinct integers
  ≥ 2 with sum ≤ n.
- `f(n,m,l)` walks those sets in increasing order: n is the budget left,
  m the smallest part still allowed, l the lcm so far. Each next part k
  runs from m to n and the call goes on with budget n−k, smallest part
  k+1 and lcm `lcm(l,k)`. `max([l]+[…])` also counts stopping here, and
  `f(n)` with the defaults m = 2, l = 1 is g(n).
- Requiring k+1 (distinct parts) instead of k costs nothing and cuts the
  search from all partitions to partitions into distinct parts.

**Notes**

- Exact integer arithmetic (`math.lcm`, Python 3.9+), no theorem needed;
  the recursion is only as deep as the number of parts, about √(2n).
- The search is exponential in √n: 105 terms in 60 s. A knapsack over
  prime powers (one power per prime) reaches about 1000 terms but is 50
  bytes longer.
- The b-file has 10001 terms; the bar is 80 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000793), CC BY-SA 4.0.
