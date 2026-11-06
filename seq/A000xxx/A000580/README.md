# A000580

> a(n) = binomial coefficient C(n,7).
> — [OEIS A000580](https://oeis.org/A000580)

Offset 7: 1, 8, 36, 120, 330, 792, 1716, 3432, 6435, 11440, …

### Python 3 — 50 bytes

```python
from math import*
n=7
while[print(comb(n,7))]:n+=1
```

**How it works**

- The sequence is the 7-th binomial column C(n,7). `comb` computes
  the coefficient exactly, returning zero when n<7.
- Starting at the OEIS offset n=7 prints C(7,7)=1 first, followed
  by the coefficients for all larger n.
- A direct binomial call avoids special cases in the multiplicative
  recurrence at the beginning of a column.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 994 terms from the OEIS b-file; the verification
  bar is 994 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000580), CC BY-SA 4.0.
