# A000575

> Tenth column of quintinomial coefficients.
> — [OEIS A000575](https://oeis.org/A000575)

Offset 0: 10, 80, 365, 1246, 3535, 8800, 19855, 41470, 81367, 151580, …

### Python 3 — 71 bytes

```python
from math import*
n=0
while[print(comb(n+11,9)-(n+3)*comb(n+6,4))]:n+=1
```

**How it works**

- The sequence is `[x⁹](1+x+x²+x³+x⁴)^(n+3)`. Rewriting the inner
  polynomial as (1−x⁵)/(1−x) gives
  (1−x⁵)^(n+3)·(1−x)^(−n−3).
- Only the constant and x⁵ terms of the first factor can contribute
  to degree 9. The negative-binomial expansion of the second factor
  therefore gives C(n+11,9)−(n+3)C(n+6,4), exactly as in the code.
- `comb` computes both binomial coefficients with integers. At the
  required offset n=0 the difference is C(11,9)−3C(6,4)=10.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000575), CC BY-SA 4.0.
