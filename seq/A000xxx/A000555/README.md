# A000555

> Number of labeled trees of diameter 4 with n nodes.
> — [OEIS A000555](https://oeis.org/A000555)

Offset 5: 60, 720, 6090, 47040, 363384, 2913120, 24560910, 218386080, 2044958916, 20112075984, …

### Python 3 — 111 bytes

```python
from math import*
n=5
while 1:print(n*(sum(comb(n-1,k)*k**(n-1-k)for k in range(n))-(n-1)*(2**(n-2)-1)-1));n+=1
```

**How it works**

- The exponential coefficient of exp(x·exp(x)) at degree m is
  Σₖ₌₀ᵐ C(m,k)k^(m−k), by expanding the outer exponential.
  Thus A000551(n)=n(Σₖ C(n−1,k)k^(n−1−k)−1).
- The OEIS center decomposition gives
  a(n)=A000551(n)−n(n−1)(2^(n−2)−1). Substituting the preceding sum
  gives the displayed program.
- A tree of diameter 4 has a unique central vertex. A diameter-3 tree
  instead gives two height-2 rootings, one at each central endpoint;
  together these contribute n(n−1)(2^(n−2)−2). Stars rooted at a leaf
  contribute another n(n−1). Subtracting both leaves exactly one
  central rooting of each diameter-4 tree.

**Notes**

- The minimum n=5 is included and gives 60. All exponents evaluated
  by this program are nonnegative.
- Every arithmetic operation is exact.
- The reference file contains 24 terms from the published OEIS entry; the verification
  bar is 24 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 111 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000555), CC BY-SA 4.0.
