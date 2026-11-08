# A001032

> Numbers k such that sum of squares of k consecutive integers >= 1 is a square.
> — [OEIS A001032](https://oeis.org/A001032)

Offset 1: 1, 2, 11, 23, 24, 26, 33, 47, 49, 50, 59, 73, 74, 88, 96, 97, 107, 121, 122, 146, 169, 177, …

### Python 3 — 495 bytes

```python
from math import*
k=0
while k:=k+1:
 D=range(1,2*k);b=min(k//s**2for s in D if k%s**2<1);N=3*k*k-3;S={k<2or b<2and any(N%d+(T:=N//d-d+6*~k)%12<1>-T for d in D)}
 for f in[f for f in D if N%f**2<1<b]:
  M=N//f//f;R=[0];m=p=1
  while m<M:
   p+=1
   while M%(q:=m*p)<1:R=[y for x in R for y in range(x,q,m)if(y*y-b)%q<1];m=q
  for P in R:
   Q,g,u,w=M,1,f*M,-f*P
   while{t:=(P,Q,g,u,w)}-S:S|={t,Q+g==0==u-~k%2*3};a=(P+isqrt(b)+(Q<0))//Q;P=a*Q-P;Q=(b-P*P)//Q;g=-g;u,w=(a*u+w)%6,u
 if{1}&S:print(k)
```

**How it works**

- With X = 2m + k − 1, the squares m², (m+1)², …, (m+k−1)² add up to
  k(3X² + k² − 1)/12. Write k = b·s² with b squarefree (`b`, the least
  k/s²) and N = 3(k² − 1). Multiplying by 36/k, the sum is a square y²
  exactly when X'² − b·Z² = −N with X' = 3X and Z = 6y/(bs); Z is a
  rational number with b·Z² an integer and b squarefree, so it is an
  integer. Conversely every integer solution gives back a square. The start
  m is a positive integer exactly when X' ≡ 3(k+1) (mod 6) and
  X' ≥ 3(k+1). Only |X'| matters, and 0 and 3 are their own negatives
  mod 6, so the class condition is sign-free.
- k = 1 is always a term (`k<2`).
- Square k (b = 1): (Z − X')(Z + X') = N, so with d = Z − X' a divisor of
  N below √N < 2k and E = N/d, X' = (E − d)/2 and the conditions become
  T = E − d − 6(k+1) ≥ 0 and T ≡ 0 (mod 12):
  `N%d+(T:=N//d-d+6*~k)%12<1>-T`, over `D=range(1,2*k)`.
- Non-square k: if (X', Z) is a solution, so is (X' + Z√b)·ε², where
  ε = t + u√b solves t² − bu² = 1. That keeps X' mod 2 (t² + bu² is odd)
  and keeps 3 | X' (if 3 ∤ b, 3 | X' forces 3 | Z), and it makes X' as
  large as we like, so the bound X' ≥ 3(k+1) takes care of itself: k is
  a term iff the equation has a solution with X' ≡ 3(k+1) (mod 6).
- That is decided with the Lagrange–Matthews–Mollin (LMM) method. A
  solution has gcd f with f² | N; dividing by f leaves a primitive solution
  of x² − by² = −M, M = N/f². These fall into classes by the root z of
  z² ≡ b (mod M), and the solutions with y > 0 in the class of z are
  exactly x = M·A − z·B, y = B at the steps i of the continued fraction of
  (z + √b)/M where (−1)ⁱ·Qᵢ = −1, with A/B the convergent before step i
  and Pᵢ, Qᵢ the usual complete-quotient numbers ((Pᵢ + √b)/Qᵢ).
- The roots: `R` holds all roots modulo a divisor m of M that grows by one
  factor p at a time (p = 2, 3, 4, … while m·p divides M; a composite p
  never does by then); each root x mod m is lifted to the y ≡ x (mod m)
  below m·p with y² ≡ b (mod m·p). Brute force, but it needs no
  factoring.
- Only x mod 6 is needed, and x obeys the convergent recurrence, so `u,w`
  keep it and the one before, mod 6, starting from (f·M, −f·z) (f carries
  the gcd back). A hit is `Q+g==0` (g = (−1)ⁱ) with `u` = 3(k+1) mod 6,
  that is `u-~k%2*3` = 0.
- When to stop: the continued fraction is eventually periodic and (u, w)
  takes 36 values, so the state (P, Q, g, u, w) eventually repeats, after
  which nothing new can happen. `while{t:=(P,Q,g,u,w)}-S:` runs until the
  state has been seen. One set `S` serves every f and z of the same k (the
  future depends only on the state), and it also collects each step's hit
  test and the square-case answer, so `{1}&S` (True == 1) is the verdict.
- The floor of (P + √b)/Q for either sign of Q, √b being irrational, is
  `(P+isqrt(b)+(Q<0))//Q`.

**Notes**

- Exact integer arithmetic; nothing is searched up to a bound. The facts
  used are the reduction above, Pell units, and the LMM theorem (K. R.
  Matthews, The Diophantine equation x² − Dy² = N, D > 0, Expositiones
  Math. 18 (2000) 323–331; R. A. Mollin, Fundamental Number Theory with
  Applications). The mod-6 bookkeeping was checked against a brute-force
  search over Pell orbits on 16 688 pairs (b, M).
- The whole b-file (10 438 terms, k ≤ 250 000) agrees with a faster
  version of the same decision (sympy for the roots); the program itself
  was compared on its first 500 terms.
- Cost: the root search is linear in the largest prime factor of
  M ≈ 3k², and the walk is about a period of √b times the mod-6 orbit.
  It prints 506 terms (k ≈ 7800) in 60 s; the bar is 380 terms with a
  120 s timeout (about 32 s here).
- [A001033](../A001033/) (odd numbers) is the same program with two
  constants changed.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 495 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001032), CC BY-SA 4.0.
