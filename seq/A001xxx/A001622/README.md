# A001622

> Decimal expansion of golden ratio phi (or tau) = (1 + sqrt(5))/2.
> — [OEIS A001622](https://oeis.org/A001622)

Offset 1: 1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0, 4, 5, …

### Python 3 — 63 bytes

```python
import math
k=1
while[print((math.isqrt(5*k*k)+k>>1)%10)]:k*=10
```

**How it works**

- With k = 10ʲ, the j-th digit after the first is ⌊φ·k⌋ mod 10, and
  φ·k = (k + √(5k²))/2.
- `math.isqrt(5*k*k)` is ⌊√(5k²)⌋ exactly (integer square root, no
  floats). Since k is a whole number, ⌊(k + x)/2⌋ = ⌊(k + ⌊x⌋)/2⌋ for any
  real x ≥ 0, so `isqrt(5*k*k)+k>>1` is exactly ⌊φ·10ʲ⌋, and `%10` keeps
  its last digit.
- `while[print(…)]:k*=10` prints and moves to the next power of ten forever
  (a one-element list is always true). For k = 1 it prints ⌊φ⌋ = 1, the
  first term.

**Notes**

- Exact integer arithmetic, so every digit is right; the OEIS keyword
  "changed" does not affect the terms, which are the digits 1, 6, 1, 8, …
  of φ = 1.6180339887…
- Each digit costs one integer square root of a 2j-digit number, so the
  total time grows roughly like the cube of the number of digits: about
  24000 digits come in the 60 s limit. The bar is 15000 of the
  100000 digits in the b-file, in 60 s.
- A digit-by-digit square root (keeping the remainder 5·100ʲ − r² from one
  digit to the next) is much faster but well over 100 bytes;
  `from math import*` costs one byte more than `import math` here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001622), CC BY-SA 4.0.
