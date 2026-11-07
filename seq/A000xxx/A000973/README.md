# A000973

> Fermat coefficients.
> — [OEIS A000973](https://oeis.org/A000973)

Offset 8: 1, 15, 99, 429, 1430, 3978, 9690, 21318, 43263, 82225, 148005, 254475, 420732, 672452, 1043460, 1577532, 2330445, 3372291, 4790071, 6690585, …

### Python 3 — 52 bytes

```python
import math
n=8
while[print(math.comb(n,7)//8)]:n+=2
```

**How it works**

- This is the Fermat coefficient (n:8) = C(2n−8, 7)/8 (the entry's
  formula), which is always an integer: the seven factors 2n−14, …, 2n−8
  include 16·(n−7)(n−6)(n−5)(n−4), and the product of four consecutive
  integers is divisible by 8, so the 2⁷ in 7!·8 = 2⁷·315 divides the
  product, and so does the odd part 315 of 7!.
- `math.comb(n,7)//8` with n = 2k−8 running over 8, 10, 12, …; the
  centered product c(c²−1)(c²−4)(c²−9)//40320 is 3 bytes longer.

**Notes**

- Exact integer arithmetic.
- The b-file has 993 terms (n = 8..1000) and all of them print in under
  0.1 s; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000973), CC BY-SA 4.0.
