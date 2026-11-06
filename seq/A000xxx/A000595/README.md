# A000595

> Number of binary relations on n unlabeled points.
> — [OEIS A000595](https://oeis.org/A000595)

Offset 0: 1, 2, 10, 104, 3044, 291968, 96928992, 112282908928, 458297100061728, 6666621572153927936, …

### Python 3 — 294 bytes

```python
from math import*
from functools import*
@cache
def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1,1)for p in P(n-j,j)]
n=0
while 1:
 H=factorial(n);print(sum((H//prod(j**p.count(j)*factorial(p.count(j))for j in set(p)))*2**sum(gcd(i,j)for i in p for j in p)for p in P(n))//H);n+=1
```

**How it works**

- Burnside's lemma averages fixed structures over vertex permutations.
  A permutation type p has n!/∏ᵣ r^mᵣmᵣ! representatives; `P` generates
  each integer partition once and the product computes this class size.
- For binary relations, a pair of vertex cycles of lengths i,j gives
  gcd(i,j) orbits of ordered pairs. Each orbit independently belongs to
  the relation or not, giving 2^Σᵢⱼ gcd(i,j). Loops are included.
- For tournaments, an even vertex cycle would reverse an edge, so only
  odd cycle types can fix a tournament. Their unordered-edge orbit count
  is (Σᵢⱼ gcd(i,j)−number of cycles)/2. Each orbit has two orientations.
- Weighting and dividing by n! gives the required unlabeled count.
  The empty partition correctly supplies a(0)=1.

**Notes**

- This enumerates permutation cycle types, rather than all labeled
  structures. Every exponent, weight and final division is exact.
- Partition growth still limits performance at large n; the verification
  bar records a practical prefix without limiting mathematical validity.
- The reference file contains 51 terms from the OEIS b-file; the verification
  bar is 25 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 294 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000595), CC BY-SA 4.0.
