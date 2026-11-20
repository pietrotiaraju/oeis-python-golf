# A002060

> Number of partitions of an n-gon into (n-5) parts.
> — [OEIS A002060](https://oeis.org/A002060)

Offset 7: 4, 60, 550, 4004, 25480, 148512, 813960, 4263600, 21573816, …

### Python 3 — 63 bytes

```python
import math
j=3
while[print(j*-~j*math.comb(j-~j,j+4)//3)]:j+=1
```

**How it works**

- **What the data are.** As for [A002058](../A002058/) and
  [A002059](../A002059/), the name does not fit the terms (the diagonal
  dissections of a heptagon into two parts number 14, not 4). The entry
  says a(n) = V(n, n−5), a diagonal of Cayley's table V(r, k) (1891,
  p. 240), and gives Mathar's program for it,
  V(r, k) = (k−1)·Π_(t=1..k−2) (r+t)/(t+2) · Π_(t=3..k+1) (r−t)/(k−t+2),
  which matches all 23 listed terms (n = 7 to 29); Mathar also notes that
  Cayley's own table has an error at V(15, 10), and the data follow the
  formula. The program takes this formula as the definition.
- **Closed form.** The two products are 2(r+k−2)!/(r!·k!) and
  (r−3)!/((r−k−2)!·(k−1)!), so at k = n − 5, r = n,
  a(n) = (n−3)(n−4)·C(2n−7, n)/3. With j = n − 4 (from 3) this is
  j(j+1)·C(2j+1, j+4)/3: `j*-~j` and `j-~j` = 2j + 1.
- **Exact division.** If j ≢ 1 (mod 3), 3 divides j(j+1); if j ≡ 1, the
  base-3 addition (j+4) + (j−3) carries in the last digit (2 + 1), so 3
  divides C(2j+1, j+4) by Kummer's theorem.

**Notes**

- `import math` with `math.comb` is a byte under `from math import*`.
- a(n) has about 0.6·n digits; the b-file has the 23 terms of the entry,
  and the bar is all of them in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002060), CC BY-SA 4.0.
