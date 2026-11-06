# A000594

> Ramanujan's tau function (or Ramanujan numbers, or tau numbers).
> — [OEIS A000594](https://oeis.org/A000594)

Offset 1: 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643, -115920, …

### Python 3 — 150 bytes

```python
from math import*
A=[1];n=0
while[print(A[n])]:n+=1;A+=sum((9*t-n)*(-1)**k*(2*k+1)*A[n-t]for k in range(1,(isqrt(8*n+1)-1)//2+1)if(t:=k*(k+1)//2))//n,
```

**How it works**

- Jacobi's identity gives B(x)=∏ₘ≥₁(1−x^m)³
  =Σₖ≥₀(−1)^k(2k+1)x^(k(k+1)/2). Ramanujan's generating function is
  xB(x)⁸, so `A[n]` is τ(n+1).
- If A=B⁸, then BA′=8B′A. Comparing degree n−1 gives the power-series
  recurrence nAₙ=Σₜ₌₁ⁿ(9t−n)bₜAₙ₋ₜ.
- The only nonzero bₜ occur at triangular t=k(k+1)/2. The integer square
  root sets the exact upper limit on k, avoiding an O(n) dense sum.
- The initial A₀=1 prints τ(1)=1. Each update appends the next exact
  coefficient before the loop advances.

**Notes**

- Every division by n is exact by the formal-series identity. The
  program uses O(√n) summands per new coefficient.
- This computes signed τ values without factoring n or using floats.
- The reference file contains 16091 terms from the OEIS b-file; the verification
  bar is 5000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 150 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000594), CC BY-SA 4.0.
