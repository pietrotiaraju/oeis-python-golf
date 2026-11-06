# A000589

> a(n) = 11*binomial(2n,n-5)/(n+6).
> — [OEIS A000589](https://oeis.org/A000589)

Offset 5: 1, 11, 77, 440, 2244, 10659, 48279, 211508, 904475, 3798795, …

### Python 3 — 64 bytes

```python
from math import*
n=5
while[print(11*comb(2*n,n-5)//(n+6))]:n+=1
```

**How it works**

- The Catalan-power coefficient formula gives
  [x^n]x^5C(x)^11=(11/(n+6))C(2n,n−5), where
  C(x)=(1−√(1−4x))/(2x).
- The program evaluates the formula with exact binomial coefficients.
  The loop starts at n=5, where the first coefficient is 1.
- Divisibility follows from the Catalan coefficient interpretation.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 196 terms from the OEIS b-file; the verification
  bar is 196 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000589), CC BY-SA 4.0.
