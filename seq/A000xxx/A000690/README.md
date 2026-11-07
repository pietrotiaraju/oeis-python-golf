# A000690

> Landau's approximation to population of x^2 + y^2 <= 2^n.
> — [OEIS A000690](https://oeis.org/A000690)

Offset 0: 1, 2, 3, 4, 7, 13, 24, 44, 83, 157, 297, 567, 1085, …

### Python 3 — 294 bytes

```python
from math import*
print(n:=1);P=9
while F:=1<<P:L=lambda s,a,u=0:sum(comb(P,k+1)*(u:=u+(-1)**k*F//(a*k+1)**s)for k in range(P));Q=lambda s:F*(s>P)or isqrt(L(s,1)*(F+F//(2**s-2))//L(s,2)*Q(2*s));a,b=[isqrt((Q(2)+t<<2*n+1)//n//((L(1,1)>>P)-t))+1>>1for t in(P*P,-P*P)];a-b or print(a);n+=a==b;P+=1
```

**How it works**

a(n) = round(x) with x = K·2ⁿ/√(n log 2), where K = 0.7642236535… is the
Landau–Ramanujan constant. The program computes K² and log 2 with integers
only, encloses x² in an interval that is certainly right, and prints the
rounded value once both ends of the interval round the same way.

- **The constant.** K = 2^(−1/2)·∏_{p≡3 (mod 4)} (1 − p⁻²)^(−1/2), so
  2K² = P₃(2) with P₃(s) = ∏_{p≡3 (mod 4)} (1 − p⁻ˢ)⁻¹. The Euler products
  of λ(s) = Σ_{m odd} m⁻ˢ and of Dirichlet's β(s) = Σ_{m odd} χ₋₄(m)m⁻ˢ
  differ only at the primes p ≡ 3, where they give (1 − p⁻ˢ)⁻¹ and
  (1 + p⁻ˢ)⁻¹; hence λ(s)/β(s) = P₃(s)²/P₃(2s) and
  P₃(2) = √(r(2)·√(r(4)·√(r(8)·…))) with r = λ/β. Since
  P₃(s) < 1 + 2·3⁻ˢ, the nesting can stop with P₃(s) ≈ 1 once s > P.
- **The series.** λ(s) = E(s)·(2ˢ − 1)/(2ˢ − 2), where
  E(s) = Σₖ (−1)ᵏ(k+1)⁻ˢ is the alternating zeta function; E(1) = log 2.
  Both E and β are alternating sums Σ (−1)ᵏcₖ of cₖ = (ak+1)⁻ˢ (a = 1, 2),
  and these cₖ are moments of a positive measure on [0, 1]. For such series
  Euler's transform, S_P = 2⁻ᴾ Σ_{j=1..P} C(P, j)·(sum of the first j terms),
  is within S/2ᴾ of the sum S (Cohen, Rodriguez Villegas and Zagier,
  *Convergence acceleration of alternating series*, Prop. 1, with the
  polynomial (1 − x)ᴾ).
- **Fixed point.** F = 2ᴾ. `L(s,a)` adds the terms ⌊±F/(ak+1)ˢ⌋ into the
  running partial sum u and weights it with C(P, k+1), so L/2ᴾ ≈ F·S.
  `Q(s)` is F·P₃(s): `isqrt` of F·r(s) times Q(2s), with F + ⌊F/(2ˢ−2)⌋
  for F·(2ˢ−1)/(2ˢ−2), and F itself for s > P. `L(1,1)>>P` is F·log 2.
- **Error bound.** Each floor is off by less than 1, so L/2ᴾ is within
  P/2 + 1 of F·S. As E(s) ≥ 3/4 and β(s) ≥ 8/9 for s ≥ 2, every ratio
  F·r(s) has relative error below (2P + 8)/F; an `isqrt` of a product of two
  approximations keeps the larger relative error of the two and adds less
  than 1/F; and stopping at s > P is off by less than 2·3⁻ᴾ. So Q(2) is
  within 1.17·(2P + 9 + log₂P) < P² of F·P₃(2), and `L(1,1)>>P` within
  P/2 + 2 < P² of F·log 2, for every P ≥ 9.
- **Rounding.** With y = 4x² = P₃(2)·2^(2n+1)/(n log 2), the two list
  entries use (Q(2) ± P²)/(F·log 2 ∓ P²) for the upper and the lower end of
  y. round(x) = ⌊(√y + 1)/2⌋ = (isqrt(⌊y⌋) + 1) >> 1 is increasing in y, so
  if both ends give the same value a, then a(n) = a.
- **The loop.** P grows by one on every pass and n only when a term is
  printed, so P − n ≥ 8 and the precision keeps ahead of the 2ⁿ size of the
  terms. A pass that cannot decide simply retries with one more bit.
- a(0) = 1 is printed first: the formula divides by log 1 = 0 there, and the
  OEIS value 1 is the actual count (A000050(0)).

**Notes**

- Only integers, so every printed term is proved, not just checked against
  the b-file. The retry loop ends for every n unless x is exactly a
  half-integer, which would make the definition itself ambiguous (that K is
  irrational is not known, but nothing suggests such a coincidence).
- The program agrees with the b-file on the 872 terms it printed in 400 s
  (513 in 60 s), and an independent implementation (Cohen–Rodriguez
  Villegas–Zagier Chebyshev weights, wider margins) on all 1000. Storing
  Q(2) and log 2 in variables (`q=Q(2);g=L(1,1)>>P;`) is 6 bytes longer and
  about 15% faster. The bar is 400 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 294 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000690), CC BY-SA 4.0.
