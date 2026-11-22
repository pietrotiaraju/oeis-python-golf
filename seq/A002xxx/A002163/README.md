# A002163

> Decimal expansion of square root of 5.
> — [OEIS A002163](https://oeis.org/A002163)

Offset 1: 2, 2, 3, 6, 0, 6, 7, 9, 7, 7, 4, 9, 9, 7, 8, 9, 6, 9, 6, 4, 0, 9, 1, …

### Python 3 — 53 bytes

```python
import math
k=5
while[print(math.isqrt(k)%10)]:k*=100
```

**How it works**

- After j steps k = 5·100ʲ, so √k = √5·10ʲ and its integer part
  ⌊√5·10ʲ⌋ is `math.isqrt(k)`, computed exactly with integers (the
  integer square root, no floats). The last digit, `%10`, is digit j + 1
  of √5 = 2.23606…; for k = 5 it prints ⌊√5⌋ = 2, the first term.
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
  and k = 3 gives [A002193](../A002193/) and [A002194](../A002194/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002163), CC BY-SA 4.0.
