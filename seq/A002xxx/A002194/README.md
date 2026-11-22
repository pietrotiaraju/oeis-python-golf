# A002194

> Decimal expansion of sqrt(3).
> — [OEIS A002194](https://oeis.org/A002194)

Offset 1: 1, 7, 3, 2, 0, 5, 0, 8, 0, 7, 5, 6, 8, 8, 7, 7, 2, 9, 3, 5, 2, 7, 4, …

### Python 3 — 53 bytes

```python
import math
k=3
while[print(math.isqrt(k)%10)]:k*=100
```

**How it works**

- After j steps k = 3·100ʲ, so √k = √3·10ʲ and its integer part
  ⌊√3·10ʲ⌋ is `math.isqrt(k)`, computed exactly with integers (the
  integer square root, no floats). The last digit, `%10`, is digit j + 1
  of √3 = 1.73205…; for k = 3 it prints ⌊√3⌋ = 1, the first term.
- `while[print(…)]:k*=100` prints and moves to the next power of 100
  forever (a one-element list is always true).

**Notes**

- Exact integer arithmetic, so every digit is right for every n.
- Each digit costs one integer square root of a (2j+1)-digit number, so
  the time grows faster than quadratically: the whole b-file, 20000
  digits, takes some 25 reference seconds (about 40 s here), 16000 of
  them about half as long. The bar is 16000 digits in 60 s.
- Every printed value is one digit, so the 4300-digit int-to-str limit
  does not apply.
- `from math import*` costs one byte more than `import math`. A
  digit-by-digit square root that keeps the remainder from one digit to
  the next is much faster but far longer. The same program with k = 2
  and k = 5 gives [A002193](../A002193/) and [A002163](../A002163/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002194), CC BY-SA 4.0.
