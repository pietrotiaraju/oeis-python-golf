# A000587

> Rao Uppuluri-Carpenter numbers (or complementary Bell numbers): e.g.f. = exp(1 - exp(x)).
> — [OEIS A000587](https://oeis.org/A000587)

Offset 0: 1, -1, 0, 1, 1, -2, -9, -9, 50, 267, …

### Python 3 — 98 bytes

```python
from math import*
A=[1]
while[print(A[-1])]:n=len(A)-1;A+=-sum(comb(n,k)*A[k]for k in range(n+1)),
```

**How it works**

- With F(x)=exp(1−exp(x)), differentiation gives F′(x)=−exp(x)F(x).
  Comparing exponential coefficients gives
  a(n+1)=−Σₖ₌₀ⁿ C(n,k)a(k), with a(0)=1.
- `A` stores those initial coefficients. The update appends exactly the
  next binomial convolution and prints it on the next pass.
- Negative values and cancellations are handled by signed integers;
  this never approximates either exponential numerically.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 596 terms from the OEIS b-file; the verification
  bar is 596 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000587), CC BY-SA 4.0.
