# A001234

> Unsigned Stirling numbers of the first kind s(n,7).
> — [OEIS A001234](https://oeis.org/A001234)

Offset 7: 1, 28, 546, 9450, 157773, 2637558, 44990231, 790943153, 14409322928, 272803210680, 5374523477960, …

### Python 3 — 69 bytes

```python
import math
m=6
while[print(math.perm((B:=m**m)+m,m+1)//B**7%B)]:m+=1
```

**How it works**

- Same idea as [A000482](../../A000xxx/A000482/): `math.perm(B+m,m+1)` =
  B(B+1)⋯(B+m) is the rising factorial whose coefficients are the
  unsigned Stirling numbers |s(m+1,k)|, and in base B = mᵐ they are its
  digits, so `//B**7%B` reads |s(m+1,7)|.
- No digit carries: the coefficients are nonnegative and sum to (m+1)!,
  and mᵐ > (m+1)! for m ≥ 3. m starts at 6 for a(7) = 1.

**Notes**

- The whole b-file (94 terms) prints at once.
- [A001233](../A001233/) is the previous column.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001234), CC BY-SA 4.0.
