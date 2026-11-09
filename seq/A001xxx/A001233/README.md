# A001233

> Unsigned Stirling numbers of first kind s(n,6).
> — [OEIS A001233](https://oeis.org/A001233)

Offset 6: 1, 21, 322, 4536, 63273, 902055, 13339535, 206070150, 3336118786, 56663366760, 1009672107080, 18861567058880, …

### Python 3 — 69 bytes

```python
import math
m=5
while[print(math.perm((B:=m**m)+m,m+1)//B**6%B)]:m+=1
```

**How it works**

- Same idea as [A000482](../../A000xxx/A000482/): `math.perm(B+m,m+1)` =
  B(B+1)⋯(B+m) is the rising factorial whose coefficients are the
  unsigned Stirling numbers |s(m+1,k)|, and in base B = mᵐ they are its
  digits, so `//B**6%B` reads |s(m+1,6)|.
- No digit carries: the coefficients are nonnegative and sum to (m+1)!,
  and mᵐ > (m+1)! for m ≥ 3. m starts at 5 for a(6) = 1.

**Notes**

- The whole b-file (95 terms) prints at once.
- [A001234](../A001234/) is the next column.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001233), CC BY-SA 4.0.
