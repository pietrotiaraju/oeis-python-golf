# A001521

> a(1) = 1; thereafter a(n+1) = floor(sqrt(2*a(n)*(a(n)+1))).
> — [OEIS A001521](https://oeis.org/A001521)

Offset 1: 1, 2, 3, 4, 6, 9, 13, 19, 27, 38, 54, 77, 109, 154, 218, 309, 437, …

### Python 3 — 53 bytes

```python
import math
a=1
while[print(a)]:a=math.isqrt(2*a*-~a)
```

**How it works**

- The definition, step by step: `math.isqrt(m)` is the exact integer square
  root ⌊√m⌋, and `2*a*-~a` is 2a(a + 1) (`-~a` = a + 1), so
  `a=math.isqrt(2*a*-~a)` is a(n+1) = ⌊√(2a(n)(a(n) + 1))⌋.
- `import math` plus one `math.isqrt` is a byte shorter than
  `from math import*` plus `isqrt`.

**Notes**

- This is the Graham–Pollak sequence: by their theorem, a(2n+1) − 2a(2n−1)
  are the binary digits of √2 (see the entry). A float square root would go
  wrong once a(n)² passes 2⁵³; `isqrt` is exact for every size.
- a(n) grows like (√2)ⁿ, so the 5000 terms of the b-file reach 753 digits;
  Python's 4300-digit int-to-str limit would stop the program at about
  n = 28500.
- The bar is the whole b-file (5000 terms) in 60 s, which takes well under a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001521), CC BY-SA 4.0.
