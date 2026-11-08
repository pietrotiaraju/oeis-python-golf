# A001008

> a(n) = numerator of harmonic number H(n) = Sum_{i=1..n} 1/i.
> — [OEIS A001008](https://oeis.org/A001008)

Offset 1: 1, 3, 11, 25, 137, 49, 363, 761, 7129, 7381, 83711, 86021, 1145993, …

### Python 3 — 69 bytes

```python
from math import*
P=F=n=1
while[print(P//gcd(P,F))]:n+=1;P=P*n+F;F*=n
```

**How it works**

- F = n! and P = n!·H(n), an integer, so H(n) = P/F and its numerator in
  lowest terms is P/gcd(P, F).
- n!·H(n) = n·(n−1)!·H(n−1) + (n−1)!, hence `P=P*n+F;F*=n` after `n+=1`.

**Notes**

- Exact integer arithmetic.
- The whole b-file (2296 terms) prints in under a second; the bar is the
  whole b-file. The numerators pass 4300 digits near n = 9900, where
  Python's int-to-str limit stops the program.
- `from fractions import*` with `h+=Fraction(1,n)` and `h.numerator` is
  77 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001008), CC BY-SA 4.0.
