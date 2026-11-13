# A001660

> Hypotenusal numbers.
> — [OEIS A001660](https://oeis.org/A001660)

Offset 0: 1, 1, 2, 6, 36, 876, 408696, 83762796636, 3508125906207095591916, …

### Python 3 — 107 bytes

```python
import math
h=[1,2]
while[print(h[-1]-h[-2])]:h+=3-sum((-1)**i*math.comb(h[-i],i+1)for i in range(len(h))),
```

**How it works**

- The hypotenusal numbers are the first differences of Hamilton's numbers
  h(1), h(2), … = 2, 3, 5, 11, 47, 923, … ([A000905](https://oeis.org/A000905)),
  the degrees studied by Sylvester and Hammond ("On Hamilton's numbers",
  1887). The entry computes them, as its Mathematica program does, by the
  Sylvester–Hammond recurrence

  h(1) = 2, h(n) = 2 + Σ_{i=1..n−1} (−1)ⁱ⁺¹·C(h(n−i), i+1),

  with a(0) = 1 and a(n) = h(n+1) − h(n) for n ≥ 1. The program follows
  that definition; it reproduces all 11 terms of the entry.
- The list `h` starts with h(0) = 1, so the first difference printed is
  h(1) − h(0) = 1 = a(0), and then a(n) = h(n+1) − h(n) as each new h is
  appended (`while[print(…)]` is always true).
- With h = [h(0), …, h(n−1)], `h[-i]` is h(n−i) for i = 1 … n−1. The sum
  also runs over i = 0, where `h[-0]` is h(0) = 1 and the term is
  C(1, 1) = 1; starting from 3 instead of 2 cancels it, and saves the `1,`
  of `range(1,len(h))`.

**Notes**

- Exact integer arithmetic (`math.comb` takes arbitrarily large integers),
  so every term the program prints is the one the recurrence defines.
- The terms roughly square at each step: a(15) has 2720 digits and a(16)
  would have about 5400, so after 16 terms Python's 4300-digit limit on
  converting integers to text stops the program with a ValueError. The bar
  is the whole b-file, 11 terms, which take a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001660), CC BY-SA 4.0.
