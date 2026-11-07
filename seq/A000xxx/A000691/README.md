# A000691

> Ramanujan's approximation to population of x^2 + y^2 <= 2^n.
> — [OEIS A000691](https://oeis.org/A000691)

Offset 0: 1, 2, 3, 5, 9, 16, 29, 52, 94, 175, 327, 616, 1169, …

### Python 3 — 375 bytes

```python
from math import*
print(n:=1);P=9
while F:=1<<P:R=range(4*P);L=lambda s,a,u=0:sum(comb(P,k+1)*(u:=u+(-1)**k*F//(a*k+1)**s)for k in R);Q=lambda s:F*(s>P)or isqrt(L(s,1)*(F+F//(2**s-2))//L(s,2)*Q(2*s));S=lambda r,X,v=F:X*sum(v//(k-~k)+r+0*(v:=v*X//-~k//F+r)for k in R)**2;a,b=[isqrt(8*(Q(2)+t)*S(t>0,n*((L(1,1)>>P)+t))>>4*P)+1>>1for t in(P*P,-P*P)];a-b or print(a);n+=a==b;P+=1
```

**How it works**

a(n) = round(K·I) with I = ∫₁^(2ⁿ) dt/√(log t) and K = 0.7642236535… the
Landau–Ramanujan constant (the OEIS Maple program). Everything is done with
integers and a certified interval, as in [A000690](../A000690/).

- **The constant.** `L`, `Q` and the bound are those of
  [A000690](../A000690/): with F = 2ᴾ, Q(2) is within P² of F·P₃(2) = 2F·K²,
  and `L(1,1)>>P` within P² of F·log 2. Here `L` runs over `range(4*P)`,
  but C(P, k+1) = 0 for k ≥ P, so the extra terms add nothing.
- **The integral.** With t = eᵘ and X = n log 2,
  I = ∫₀^X eᵘu^(−1/2) du = 2√X·Σₖ Xᵏ/(k!(2k+1)) =: 2√X·σ, so
  y = 4(KI)² = 8·P₃(2)·X·σ².
- `S(r,X)` returns X·σ² in fixed point, X given as F·X: v runs through
  F·Xᵏ/k! and the sum adds ⌊v/(2k+1)⌋. With r = 0 every step rounds down,
  so the result is a lower bound; with r = 1 every value gets +1 after
  rounding and stays above the true one, an upper bound. Every value is
  increasing in X and stays positive.
- The terms beyond 4P are below one unit together: P ≥ n + 8 and X < 0.7n,
  so their sum is under 2·(0.48)^(4P)·2ᴾ < 1, and with r = 1 the last two
  computed terms (true value < ½, computed ≥ 1) already pay for it.
- The list builds the upper end of y from Q(2) + P², F·X taken as
  n·(`L(1,1)>>P` + P²) and r = 1, the lower end from the minus signs and
  r = 0, and rounds both with
  round(x) = (isqrt(⌊4x²⌋) + 1) >> 1. Equal ends prove the term; otherwise
  the next pass has one more bit of precision, as in A000690.
- a(0) = 1 is printed first: the formula gives K·0 = 0 there, but the OEIS
  lists 1, the actual count (A000050(0)).

**Notes**

- Only integers, so every printed term is proved. The retry loop ends unless
  K·I is exactly a half-integer, which would make the definition ambiguous.
- Beyond the 34 terms of the b-file, the values were checked up to n = 149
  against an independent implementation (Cohen–Rodriguez Villegas–Zagier
  Chebyshev weights and the other rounding directions).
- The 34 terms print in well under a second. The bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 375 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000691), CC BY-SA 4.0.
