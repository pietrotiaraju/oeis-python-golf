# A000574

> Coefficient of x^5 in expansion of (1 + x + x^2)^n.
> — [OEIS A000574](https://oeis.org/A000574)

Offset 3: 3, 16, 51, 126, 266, 504, 882, 1452, 2277, 3432, …

### Python 3 — 62 bytes

```python
from math import*
n=3
while[print(comb(n+1,4)*(n+12)//5)]:n+=1
```

**How it works**

- To obtain degree 5 in (1+x+x²)^n, choose either five linear terms,
  three linear terms and one quadratic, or one linear and two quadratics.
  This gives C(n,5)+4C(n,4)+3C(n,3).
- Simplifying yields C(n+1,4)(n+12)/5, the expression used here.
  It is valid from the OEIS offset n=3, where it gives 3.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 998 terms from the OEIS b-file; the verification
  bar is 998 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000574), CC BY-SA 4.0.
