# A001764

> a(n) = binomial(3*n,n)/(2*n+1) (enumerates ternary trees and also noncrossing trees).
> — [OEIS A001764](https://oeis.org/A001764)

Offset 0: 1, 1, 3, 12, 55, 273, 1428, 7752, 43263, 246675, …

### Python 3 — 55 bytes

```python
import math
j=1
while[print(math.comb(j,j//3)//j)]:j+=3
```

**How it works**

- With j = 3n + 1, C(j, n)/j = (3n+1)!/(n!·(2n+1)!·(3n+1))
  = (3n)!/(n!·(2n+1)!) = C(3n, n)/(2n+1). The loop steps j by 3 from 1, and
  `j//3` is n.
- The quotient is an integer (it counts ternary trees), so `//j` is exact
  and every term is right.

**Notes**

- a(5193) is the first term over 4300 digits, where Python's int-to-str
  limit would stop the program; long before that it slows down, since each
  term is a fresh binomial (about 5000 terms in 12 s here).
- The ratio recurrence, updated before the step so it can start at
  `a=w=1` (w = 3n − 2 for the new n):
  `while[print(a)]:a=a*w*-~w*27//(w+2)//(4*w+14);w+=3`, is 56 bytes.
- The b-file has 1001 terms (a(0) to a(1000)); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001764), CC BY-SA 4.0.
