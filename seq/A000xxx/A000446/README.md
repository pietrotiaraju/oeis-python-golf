# A000446

> Smallest number that is the sum of 2 squares (allowing zeros) in exactly n ways.
> — [OEIS A000446](https://oeis.org/A000446)

Offset 1: 0, 25, 325, 1105, 4225, 5525, 203125, 27625, 71825, 138125, …

### Python 3 — 370 bytes

```python
from math import*
from functools import*
D=cache(lambda d:{d}|{z for x in range(2,isqrt(d)+1)if d%x<1 for z in(x,d//x)})
F=cache(lambda d,i,b: 1 if d<2 else min([P[i]**~-j*v for j in D(d)if j<=b and(v:=F(d//j,i+1,j))]or[0]))
P=[];p=t=n=1
print(0)
while n:=n+1:
 while len(P)<(2*n).bit_length():
  t*=p*p;p+=1;P+=[p]*(t%p>0<p%4==1)
 print(min(F(k:=n+n,0,k),F(k-1,0,k-1)))
```

**How it works**

- Representations use 0≤x≤y in N=x²+y²: neither signs nor
  swapping the roots create another way, and zero roots are allowed.
  For positive representable N, put d=∏(e_p+1), over its prime
  factors p≡1 mod 4. The two-square theorem gives 4d signed,
  ordered representations, hence **⌈d/2⌉ unordered ones**.
- To account for the ceiling, a generic pair has eight signed,
  ordered variants. A zero root or two equal roots has only four;
  one such exceptional pair occurs exactly when d is odd, giving
  the extra half. Primes 3 mod 4 must have even exponents.
- Removing powers of 2 and squares of primes 3 mod 4 leaves d
  unchanged and decreases N. A positive minimum therefore uses only
  primes 1 mod 4. Their exponents may be taken in decreasing order
  on increasing primes: if p<q and e<f, exchanging pᵉqᶠ for
  pᶠqᵉ multiplies it by (p/q)^(f−e)<1 without changing d.
- Exactly n ways means d=2n−1 or d=2n. For each target d,
  `F(d,i,b)` minimizes the remaining prime-power product, starting
  at P[i], with each next factor j=e+1 at most b. `D(d)`
  supplies divisors j≥2, including d itself; the recursion tries
  P[i]^(j−1) times `F(d//j,i+1,j)`.
- Passing j as the new bound lists the factors in nonincreasing
  order, so every exponent pattern is reached without permuting it.
  `d<2` means the target product has been exhausted and returns 1.
  An impossible branch returns 0; the walrus condition discards it
  before it could incorrectly win the minimum.
- P contains successive primes 1 mod 4. Immediately before
  testing p, t is ((p−1)!)²: multiply by the preceding p²,
  then increment p. For primes, Wilson's theorem makes t%p=1.
  For composite p>4, (p−1)! is divisible by p, so t%p=0.
  The exceptional composite 4 is excluded by p%4==1 anyway.
  Thus `t%p>0<p%4==1` selects exactly the required primes.
- At most ⌊log₂d⌋ nontrivial factors can occur, so
  `(2*n).bit_length()` primes suffice for both targets.
- The assignment `k:=n+n` shares the target 2n between the
  two calls; their order does not affect the minimum. The cached
  lambdas retain the same divisor and product subproblems.
- The outer loop takes the smaller of the two exact minima.
  The first value is handled separately: 0=0²+0² is smaller than
  every positive number with one representation.

**Notes**

- The divisor-factor algorithm is also described on the OEIS page.
  Every step is exact integer arithmetic; the proof concerns all
  exponent patterns, not only the reference terms.
- For n=2, d=3 permits 5²=25, with pairs (0,5) and (3,4).
  For n=3 the minimum is 325=5²·13, giving d=3·2=6 and
  pairs (1,18), (6,17), (10,15).
- Exact-count minima need not increase: a(7)=203125 but a(8)=27625.
  [A000448](../A000448/) asks for at least n ways and can reuse
  the latter value already at n=7.
- `cache` reuses divisor sets and minimum-product subproblems across
  outputs. Appending more primes does not invalidate cached results:
  the existing prime prefix and every already-used P[i] stay fixed.
  The caches grow, and sufficiently large outputs eventually reach
  Python 3.11+'s default 4300-digit conversion limit.
- The b-file has 1458 terms (indices 1 through 1458). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 410 | first entry |
| 2026-11-06 | Python 3 | 405 | simplify the minimum expression |
| 2026-11-06 | Python 3 | 370 | use Wilson prime generation, cached lambdas and a shared target |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000446), CC BY-SA 4.0.
