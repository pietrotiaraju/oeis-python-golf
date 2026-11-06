# A000579

> Figurate numbers or binomial coefficients C(n,6).
> — [OEIS A000579](https://oeis.org/A000579)

Offset 0: 0, 0, 0, 0, 0, 0, 1, 7, 28, 84, …

### Python 3 — 50 bytes

```python
from math import*
n=0
while[print(comb(n,6))]:n+=1
```

**How it works**

- The sequence is the 6-th binomial column C(n,6). `comb` computes
  the coefficient exactly, returning zero when n<6.
- Starting at the OEIS offset n=0 includes all six initial zeros;
  the first nonzero term is C(6,6)=1.
- A direct binomial call avoids special cases in the multiplicative
  recurrence at the beginning of a column.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000579), CC BY-SA 4.0.
