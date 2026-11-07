# A000846

> a(n) = C(3n,n) - C(2n,n).
> — [OEIS A000846](https://oeis.org/A000846)

Offset 0: 0, 1, 9, 64, 425, 2751, 17640, 112848, 722601, 4638205, 29860259, …

### Python 3 — 64 bytes

```python
from math import*
n=0
while[print(comb(3*n,n)-comb(2*n,n))]:n+=1
```

**How it works**

- The definition, term by term: `math.comb` is exact, so a(n) is
  `comb(3*n,n)-comb(2*n,n)` and a counter `n` runs from 0.
- With two calls, `from math import*` (17 bytes) beats `import math` plus
  two `math.` prefixes (21 bytes).
- Carrying both binomials by their ratios instead,
  C(3n+3,n+1) = C(3n,n)·3(3n+1)(3n+2)/((2n+1)(2n+2)) and
  C(2n+2,n+1) = 4·C(2n,n) − 2·C(2n,n)/(n+1), costs more than the two calls.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 5188, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000846), CC BY-SA 4.0.
