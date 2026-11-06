# A000588

> a(n) = 7*binomial(2n,n-3)/(n+4).
> — [OEIS A000588](https://oeis.org/A000588)

Offset 0: 0, 0, 0, 1, 7, 35, 154, 637, 2548, 9996, …

### Python 3 — 77 bytes

```python
from math import*
n=0
while[print(7*comb(2*n,n-3)//(n+4)if n>=3 else 0)]:n+=1
```

**How it works**

- The Catalan-power coefficient formula gives
  [x^n]x^3C(x)^7=(7/(n+4))C(2n,n−3), where
  C(x)=(1−√(1−4x))/(2x).
- The program evaluates the formula with exact binomial coefficients.
  The three initial zero coefficients are printed before n=3.
- Divisibility follows from the Catalan coefficient interpretation.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 201 terms from the OEIS b-file; the verification
  bar is 201 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000588), CC BY-SA 4.0.
