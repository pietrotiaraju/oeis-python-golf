# A001675

> a(n) = round(sqrt( 2*Pi )^n).
> — [OEIS A001675](https://oeis.org/A001675)

Offset 0: 1, 3, 6, 16, 39, 99, 248, 622, 1559, 3907, 9793, 24546, 61529, …

### Python 3 — 130 bytes

```python
import math
t=l=1;q=z=4;n=0
while 4*z**n//t**n<(a:=4*(z+q)**n//t**n)or[print(-~math.isqrt(a)//2),n:=n+1]:l+=2;q*=l//2;z=z*l+q;t*=l
```

**How it works**

- **Rounding without a square root of π.** With X = (2π)ⁿ the term is the
  integer nearest to √X, which is ⌊√X + ½⌋ = ⌊(√(4X) + 1)/2⌋. Since
  ⌊(y + 1)/2⌋ = ⌊(⌊y⌋ + 1)/2⌋ for real y ≥ 0, and ⌊√(4X)⌋ = isqrt(⌊4X⌋)
  (an integer k has k ≤ √(4X) exactly when k² ≤ ⌊4X⌋), the term is
  `-~math.isqrt(⌊4X⌋)//2`, all in integers: it is enough to know
  ⌊4X⌋ = ⌊4·(2π)ⁿ⌋ exactly.
- **A shrinking interval around 2π.** The state is the halved Gibbons spigot
  of [A001674](../A001674/) (π = 2u, u = 1 + 1/3·(1 + 2/5·(1 + …)), started
  at 4u): after k terms 2π lies in [z/t, (z+q)/t], and each term
  (l = 2k+1: q → q·k, t → t·l, z → z·l + q·k) shrinks the width q/t by
  k/(2k+1) < ½. At the start q = z = 4, t = 1 (2π ∈ [4, 8]).
- **Deciding ⌊4X⌋.** 4X lies in [4zⁿ/tⁿ, 4(z+q)ⁿ/tⁿ]; when both ends have
  the same integer part a, so does 4X: the test is false, the list prints
  `-~math.isqrt(a)//2` and steps n (the body still runs, a non-empty list
  being true). Otherwise the body takes in another term and the same n is
  tried again.
- **It never stalls.** For n ≥ 1, 4·(2π)ⁿ is not an integer (π is
  transcendental), so a narrow enough interval decides its integer part.
  (Nor is √(2π)ⁿ ever a half-integer, so the rounding has no ties.) For
  n = 0 both ends are 4, and a(0) = (isqrt(4) + 1)//2 = 1 is printed at
  once.

**Notes**

- Exact integer arithmetic throughout, so the program is right for every n.
- The run slows down as the powers of t = 1·3·5⋯(2k+1) grow; about 260
  terms come in the 60 s limit. The bar is 180 of the 501 terms of the
  b-file, in 60 s.
- Deciding the rounding directly,
  `-~isqrt(4*z**n//t**n)//2<(a:=-~isqrt(4*(z+q)**n//t**n)//2)` (with
  `from math import*`), needs only half the precision and reaches about
  400 terms in the limit, but is 12 bytes longer. `isqrt(a)+1>>1` is as
  long as `-~isqrt(a)//2`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 130 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001675), CC BY-SA 4.0.
