# A000529

> Powers of rooted tree enumerator.
> — [OEIS A000529](https://oeis.org/A000529)

Offset 1: 20, 74, 186, 388, 721, 1236, 1995, 3072, 4554, 6542, …

### Python 3 — 108 bytes

```python
from math import*
n=0
while 1:print(sum(c*comb(n+5-j,5)for j,c in enumerate((20,-46,42,-18,3))if j<=n));n+=1
```

**How it works**

- The Maple entry gives the rational generating function
  (x−2)(3x³−12x²+18x−10)/(x−1)⁶
  =(20−46x+42x²−18x³+3x⁴)/(1−x)⁶.
- Expanding (1−x)^−6 gives C(n+5,5). Convolving with the five numerator
  coefficients gives the displayed sum.
- The series has a constant coefficient 20, but this entry numbers its
  first term at offset 1. The program's internal degree is therefore
  one below the printed sequence index.

**Notes**

- The generating function is marked conjectural in the OEIS entry;
  correctness beyond the published terms is conditional on that identity.
  The page does not claim a proof from the terse rooted-tree description.
- All coefficient arithmetic is exact.
- The reference file contains 50 terms from the published OEIS entry; the verification
  bar is 50 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 108 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000529), CC BY-SA 4.0.
