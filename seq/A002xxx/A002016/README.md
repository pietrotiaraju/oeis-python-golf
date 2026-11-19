# A002016

> Number of first n tetrahedral numbers (A000292) that are relatively prime to n.
> — [OEIS A002016](https://oeis.org/A002016)

Offset 1: 1, 1, 3, 1, 2, 2, 4, 2, 6, 1, 8, 2, 10, 2, 5, 4, 14, 3, 16, 2, 7, …

### Python 3 — 83 bytes

```python
from math import*
n=1
while[print(sum(gcd(comb(k+3,3),n)<2for k in range(n)))]:n+=1
```

**How it works**

- The tetrahedral numbers are T(j) = j(j + 1)(j + 2)/6 = C(j + 2, 3). For
  each n the program counts j = 1, …, n with gcd(T(j), n) = 1: with
  k = j − 1 running over `range(n)`, T(j) is `comb(k+3,3)`.
- `gcd(…,n)<2` is True exactly when the gcd is 1 (n ≥ 1, so the gcd is
  never 0), and `sum` counts the Trues.

**Notes**

- `range(3,n+3)` with `comb(k,3)` is two bytes longer; writing T(j) as
  `k*-~k*(k+2)//6` with `import math` is longer too.
- The b-file has 1000 terms (n = 1 to 1000); the bar is the whole b-file
  in 60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002016), CC BY-SA 4.0.
