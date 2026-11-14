# A001698

> a(n) = ceiling(sqrt( 2*Pi )^n).
> — [OEIS A001698](https://oeis.org/A001698)

Offset 0: 1, 3, 7, 16, 40, 99, 249, 622, 1559, 3907, 9793, 24547, 61529, …

### Python 3 — 125 bytes

```python
import math
t=l=1;q=z=4;n=0
while-z**n//t**n>(a:=-(z+q)**n//t**n)or[print(-~math.isqrt(~a)),n:=n+1]:l+=2;q*=l//2;z=z*l+q;t*=l
```

**How it works**

- **No square root of π needed.** With X = (2π)ⁿ, √(2π)ⁿ = √X, and
  ⌈√X⌉ is the least integer k with k² ≥ X; since k² is an integer, that
  is the least k with k² ≥ ⌈X⌉, which is 1 + isqrt(⌈X⌉ − 1). So it is
  enough to know ⌈X⌉ exactly.
- **A shrinking interval around 2π**, as in [A001674](../A001674/) (⌊ ⌋ of
  the same powers): Gibbons' spigot of [A000796](../../A000xxx/A000796/) in
  the halved form π = 2u, u = 1 + 1/3·(1 + 2/5·(1 + …)), started at 4u.
  After k terms 2π = (q·x + z − q)/t with x, the rest of the series, in
  [1, 2], so 2π lies in [z/t, (z+q)/t]; at the start q = z = 4, t = 1. A
  term (l = 2k+1) does q → q·k, t → t·l, z → z·l + q·k, and the width
  q/t shrinks by k/(2k+1) < ½ each time.
- **Deciding ⌈X⌉.** `-z**n//t**n` is −⌈zⁿ/tⁿ⌉ and a is −⌈(z+q)ⁿ/tⁿ⌉.
  When both ends have the same ceiling c, so does X between them (X ≤
  (z+q)ⁿ/tⁿ ≤ c and X ≥ zⁿ/tⁿ > c − 1): the test is false, the list prints
  1 + isqrt(c − 1) = `-~math.isqrt(~a)` (~a = −a − 1 = c − 1) and steps n,
  and the body still runs (a non-empty list is true). Otherwise the body
  takes in another term and the same n is tried again.
- **It never stalls.** For n ≥ 1, (2π)ⁿ is not an integer (π is
  transcendental), so a narrow enough interval holds no integer at or above
  its lower end and below its upper end, and the two ceilings agree. For
  n = 0 both ends are 1 and a(0) = 1 + isqrt(0) = 1 comes at once.

**Notes**

- Exact integer arithmetic throughout, so the program is right for every
  n; it does not use ⌈√X⌉ = ⌊√X⌋ + 1, which needs X irrational and fails
  at n = 0.
- t is the product 1·3·5⋯(2k+1) and the run slows down as the powers grow;
  in reference seconds the 180th term comes after about 10 s and the 200th
  after about 15 s, and some 260 terms come in the 60 s limit. The bar is
  200 of the 501 terms of the b-file, in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 125 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001698), CC BY-SA 4.0.
