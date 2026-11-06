# A000582

> a(n) = binomial coefficient C(n,9).
> — [OEIS A000582](https://oeis.org/A000582)

Offset 9: 1, 10, 55, 220, 715, 2002, 5005, 11440, 24310, 48620, …

### Python 3 — 50 bytes

```python
from math import*
n=9
while[print(comb(n,9))]:n+=1
```

**How it works**

- The sequence is the 9-th binomial column C(n,9). `comb` computes
  the coefficient exactly, returning zero when n<9.
- Starting at the OEIS offset n=9 prints C(9,9)=1 first, followed
  by the binomial coefficients for every larger n.
- A direct binomial call avoids special cases in the multiplicative
  recurrence at the beginning of a column.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 992 terms from the OEIS b-file; the verification
  bar is 992 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000582), CC BY-SA 4.0.
