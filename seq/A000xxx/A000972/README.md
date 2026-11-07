# A000972

> Fermat coefficients.
> — [OEIS A000972](https://oeis.org/A000972)

Offset 7: 1, 12, 66, 245, 715, 1768, 3876, 7752, 14421, 25300, 42287, 67860, 105183, 158224, 231880, 332112, 466089, 642341, 870922, 1163580, …

### Python 3 — 52 bytes

```python
import math
n=7
while[print(math.comb(n,6)//7)]:n+=2
```

**How it works**

- This is the Fermat coefficient (n:7) = C(2n−7, 6)/7 rounded to the
  nearest integer (the entry's ⌊(2k)(2k+1)⋯(2k+5)/7!⌋ with k = n−6 is the
  same number).
- By Lucas' theorem C(N, 6) ≡ C(N mod 7, 6) ∈ {0, 1} (mod 7), so rounding
  is the floor: `math.comb(n,6)//7` with n = 2k−7 running over 7, 9, 11, …
- The centered product (t²−1)(t²−9)(t²−25)//322560 with t = 4k−19 needs no
  import but is 3 bytes longer.

**Notes**

- Exact integer arithmetic.
- The b-file has 994 terms (n = 7..1000) and all of them print in under
  0.1 s; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000972), CC BY-SA 4.0.
