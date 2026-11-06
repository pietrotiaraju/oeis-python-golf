# A000590

> a(n) = 13*binomial(2n,n-6)/(n+7).
> — [OEIS A000590](https://oeis.org/A000590)

Offset 6: 1, 13, 104, 663, 3705, 19019, 92092, 427570, 1924065, 8454225, …

### Python 3 — 64 bytes

```python
from math import*
n=6
while[print(13*comb(2*n,n-6)//(n+7))]:n+=1
```

**How it works**

- The Catalan-power coefficient formula gives
  [x^n]x^6C(x)^13=(13/(n+7))C(2n,n−6), where
  C(x)=(1−√(1−4x))/(2x).
- The program evaluates the formula with exact binomial coefficients.
  The loop starts at n=6, where the first coefficient is 1.
- Divisibility follows from the Catalan coefficient interpretation.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 195 terms from the OEIS b-file; the verification
  bar is 195 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000590), CC BY-SA 4.0.
