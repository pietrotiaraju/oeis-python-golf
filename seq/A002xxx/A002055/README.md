# A002055

> Number of diagonal dissections of a convex n-gon into n-4 regions.
> — [OEIS A002055](https://oeis.org/A002055)

Offset 5: 1, 9, 56, 300, 1485, 7007, 32032, 143208, 629850, 2735810, 11767536, 50220040, …

### Python 3 — 58 bytes

```python
import math
m=2
while[print(m*math.comb(2*m,m-2)//2)]:m+=1
```

**How it works**

- **Kirkman–Cayley.** A convex n-gon cut by k non-crossing diagonals
  into k + 1 regions can be cut in
  D(n, k) = C(n−3, k)·C(n+k−1, k)/(k+1) ways (Kirkman's formula, proved by
  Cayley, *On the partitions of a polygon*, 1891; see the entry).
- **Here** n − 4 regions means k = n − 5 diagonals:
  a(n) = C(n−3, 2)·C(2n−6, n−5)/(n−4), the entry's formula, and
  C(n−3, 2)/(n−4) = (n−3)/2. With m = n − 3 (from 2):
  a(n) = m·C(2m, m−2)/2.
- **Exact.** m·C(2m, m−2) is twice the count a(n), so `//2` is exact.
- `import math` and `math.comb` is a byte under `from math import*` with
  `comb`.

**Notes**

- The running ratio a(n)/a(n−1) = 2m²(2m−1)/((m−1)(m²−4)),
  `a=a*m*m*(4*m-2)//~-m//(m*m-4)` from a = 1, m = 2, is 58 bytes too.
  [A002056](../A002056/) is the next diagonal, n − 5 regions.
- a(n) has about 0.6·n digits; the b-file has 96 terms (n = 5 to 100), and
  the bar is the whole b-file in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002055), CC BY-SA 4.0.
