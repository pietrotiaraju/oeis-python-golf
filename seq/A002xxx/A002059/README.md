# A002059

> Number of partitions of an n-gon into (n-4) parts.
> — [OEIS A002059](https://oeis.org/A002059)

Offset 6: 3, 32, 225, 1320, 7007, 34944, 167076, 775200, 3517470, 15690048, 69052555, …

### Python 3 — 55 bytes

```python
import math
m=3
while[print(m*math.comb(2*m,m+3))]:m+=1
```

**How it works**

- **What the data are.** The name does not fit the terms: the diagonal
  dissections of an n-gon into n − 4 parts are [A002055](../A002055/)
  (1, 9, 56, … from n = 5), while this entry has 3, 32, 225, … from n = 6.
  Like [A002058](../A002058/), whose old name of the same kind was
  withdrawn, it is a diagonal of Cayley's auxiliary table V(r, k) (1891,
  p. 240), and no combinatorial meaning is given. The program follows the
  data: Barequet's formula a(n) = (n−3)·C(2n−6, n), from the entry, which
  matches all 24 listed terms (n = 6 to 29), is taken as the definition.
- **Program.** With m = n − 3 (from 3), a(n) = m·C(2m, m+3). `import math`
  and `math.comb` is a byte under `from math import*` with `comb`.

**Notes**

- The running ratio a(n)/a(n−1) = 2j²(2j−1)/((j−1)(j²−9)), j = n − 3,
  is 58 bytes.
- a(n) has about 0.6·n digits; the b-file has the 24 terms of the entry,
  and the bar is all of them in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002059), CC BY-SA 4.0.
