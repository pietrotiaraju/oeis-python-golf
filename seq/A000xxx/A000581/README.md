# A000581

> a(n) = binomial coefficient C(n,8).
> — [OEIS A000581](https://oeis.org/A000581)

Offset 8: 1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310, …

### Python 3 — 50 bytes

```python
from math import*
n=8
while[print(comb(n,8))]:n+=1
```

**How it works**

- The sequence is the 8-th binomial column C(n,8). `comb` computes
  the coefficient exactly, returning zero when n<8.
- Starting at the OEIS offset n=8 prints C(8,8)=1 first, followed
  by the coefficients for all larger n.
- A direct binomial call avoids special cases in the multiplicative
  recurrence at the beginning of a column.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 993 terms from the OEIS b-file; the verification
  bar is 993 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000581), CC BY-SA 4.0.
