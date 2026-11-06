# A000557

> Expansion of e.g.f. 1/(1 - 2*sinh(x)).
> — [OEIS A000557](https://oeis.org/A000557)

Offset 0: 1, 2, 8, 50, 416, 4322, 53888, 783890, 13031936, 243733442, …

### Python 3 — 103 bytes

```python
from math import*
A=[1]
while[print(A[-1])]:n=len(A);A+=2*sum(comb(n,k)*A[n-k]for k in range(1,n+1,2)),
```

**How it works**

- Multiply the exponential generating function by 1−2sinh(x).
  Odd positive degrees of the denominator have exponential coefficient
  −2; every other positive degree vanishes.
- Comparing coefficients therefore gives
  a(n)=2·Σₖ odd C(n,k)a(n−k), plus the coefficient of the numerator.
  The numerator is 1 for A000557 and exp(−x) for A000556.
- For A000556, the n-th term of the sum at k=n when n is odd combines
  with (−1)^n to give 1. This leaves the displayed recurrence with
  k<n and an added 1. For A000557 the odd sum includes k=n.
- The initial constant coefficient is 1 in both cases.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 201 terms from the OEIS b-file; the verification
  bar is 201 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000557), CC BY-SA 4.0.
