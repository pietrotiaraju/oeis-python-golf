# A001674

> a(n) = floor(sqrt( 2*Pi )^n).
> — [OEIS A001674](https://oeis.org/A001674)

Offset 0: 1, 2, 6, 15, 39, 98, 248, 621, 1558, 3906, 9792, 24546, 61528, …

### Python 3 — 121 bytes

```python
import math
t=l=1;q=z=4;n=0
while z**n//t**n<(a:=(z+q)**n//t**n)or[print(math.isqrt(a)),n:=n+1]:l+=2;q*=l//2;z=z*l+q;t*=l
```

**How it works**

- **No square root of π needed.** With X = (2π)ⁿ, √(2π)ⁿ = √X, and for any
  real X ≥ 0, ⌊√X⌋ = ⌊√⌊X⌋⌋ = `isqrt(⌊X⌋)` (an integer k satisfies
  k ≤ √X exactly when k² ≤ X, that is k² ≤ ⌊X⌋). So it is enough to
  know ⌊X⌋ = ⌊(2π)ⁿ⌋ exactly, and `math.isqrt` gives the term.
- **A shrinking interval around 2π.** The state is Gibbons' spigot of
  [A000796](../../A000xxx/A000796/), in the halved form π = 2u,
  u = 1 + 1/3·(1 + 2/5·(1 + …)), started at 4u instead of 2u: after k terms
  2π = (q·x + z − q)/t with x, the rest of the series, in [1, 2]. So 2π lies
  in [z/t, (z+q)/t]; at the start q = z = 4, t = 1 (2π = 4x ∈ [4, 8]). A
  term (l = 2k+1) does q → q·k, t → t·l, z → z·l + q·k (`q*=l//2` first,
  then `z=z*l+q`), and the width q/t shrinks by k/(2k+1) < ½ each time.
- **Deciding ⌊X⌋.** X lies in [zⁿ/tⁿ, (z+q)ⁿ/tⁿ]; when both ends have the
  same integer part a, so does X = (2π)ⁿ: the test is false, the list
  prints isqrt(a) and steps n, and the body still runs (a non-empty list is
  true). Otherwise the body takes in another term and the same n is tried
  again.
- **It never stalls.** For n ≥ 1, (2π)ⁿ is not an integer (π is
  transcendental), so it sits strictly between two integers and a narrow
  enough interval decides its integer part. For n = 0 both ends are 1
  and a(0) = isqrt(1) = 1 is printed at once.

**Notes**

- Exact integer arithmetic throughout, so the program is right for every n.
- t is the product 1·3·5⋯(2k+1) and the run slows down as the powers grow;
  about 260 terms come in the 60 s limit. The bar is 180 of the 501 terms
  of the b-file, in 60 s.
- Deciding ⌊√X⌋ directly, `isqrt(z**n//t**n)<(a:=isqrt((z+q)**n//t**n))`
  (with `from math import*`), needs only half the precision and reaches
  about 400 terms in the limit, but is 8 bytes longer; computing tⁿ once
  saves time and costs 2 bytes. The same loop gives ⌊πⁿ⌋ in
  [A001672](../A001672/) and the rounded value in [A001675](../A001675/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001674), CC BY-SA 4.0.
