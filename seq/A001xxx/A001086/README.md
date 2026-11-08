# A001086

> Continued fraction associated with y(y+1) = x(x^2 -1).
> — [OEIS A001086](https://oeis.org/A001086)

Offset 0: 0, 3, 4, 1, 1, 5, 2, 168, 46793, 1, 7, 1, 51, 1, 7, 1, 6, 2, 1, 1, 1, 10, 1, …

### Python 3 — 415 bytes

```python
import math
K=s=0
while K:=K+9:
 j=H=4**K;S=2*H;F=lambda w:4*w*(w*w-S*S)+S**3;w=[H,0,-3*H];V=[];i=0
 while j:=j//2:w=[v+j*(F(v+j)*F(v)>0)for v in w]
 for c in 0,1:
  for u in S,w[0]:
   X=[u-x-(x<u)+2*c for x in w];L=0
   for _ in X*K:a,b,e=[math.isqrt(x+L)+c for x in X];L+=a*b+b*e+e*a
   V+=(a,e)[c],
 n,m,N,M=V;a,b,c,d=2*n-M,4*n,2*N-m,4*N
 while d and(n:=a//b)==c//d:i+=1;s+=i>s!=print(n);a,b,c,d=d,c-n*d,b,a-n*b
```

**How it works**

- The curve y² + y = x³ − x (conductor 37, the subject of Guy's paper)
  becomes Y² = 4x³ − 4x + 1 with Y = 2y + 1. The cubic has three real
  roots e₁ ≈ 0.8375 > e₂ ≈ 0.2696 > e₃ ≈ −1.1071, so the real curve is an
  egg over [e₃, e₂] and a branch over [e₁, ∞). The number expanded is the
  place of the generator P = (0, 0) on the egg as a fraction of the real
  period, t = (1/ω)·∫ from e₃ to 0 of dx/|Y| ≈ 0.3105413587, with
  ω = 2∫ from e₁ to ∞ of dx/Y ≈ 2.9934586 (the real part of the elliptic
  logarithm of P over ω). The multiples nP move on by t of the period each
  time, alternating between egg and branch.
- The program uses 2P = (1, 0) on the branch instead, which needs no
  integral over the egg: its elliptic logarithm is 2t·ω, so
  t = 1/2 − (∫ from 1 to ∞ of dx/Y)/(2ω). In Carlson's form
  ∫ from x₀ to ∞ of dx/Y = R_F(x₀ − e₁, x₀ − e₂, x₀ − e₃), with
  R_F(x, y, z) = ½∫₀^∞ dt/√((t+x)(t+y)(t+z)), so
  t = 1/2 − R_F(1 − e₁, 1 − e₂, 1 − e₃) / (4·R_F(0, e₁ − e₂, e₁ − e₃)).
- All numbers are integers at the scale S = 2·4ᴷ. The three roots come
  from one bisection of F(w) = 4w³ − 4wS² + S³ on the brackets
  [S/2, S], [0, S/2] and [−3S/2, −S] (the list `w`, steps `j` halving
  from S/4 to 1), which leaves each root e·S inside (w, w + 1).
- The arguments of R_F are u − e for u = S (the point x₀ = 1) or u = e₁
  (the period). `u-x-(x<u)+2*c` bounds them from below for c = 0 and from
  above for c = 1; the `-(x<u)` makes e₁ − e₁ come out as 0 or 2
  instead of −1.
- Carlson's duplication R_F(x+λ, y+λ, z+λ) = R_F(x, y, z)/2, with
  λ = √x√y + √y√z + √z√x, is used without the usual division by 4, so all
  three arguments get the same λ: only the running total `L` is kept. The
  differences stay put while the arguments grow fourfold each step, so the
  three draw together. R_F decreases in each argument, so square roots
  rounded down (c = 0) or up (`+c`) keep lower and upper bounds at every
  step, and at the end R_F lies between 1/√max and 1/√min. The order of
  the arguments never changes, so the min and max are the first and the
  last: `(a,e)[c]`, their square roots from the last step.
- Both R_F go through the same 3K steps, so the factor 2^(−3K) cancels:
  with n, N the bounds for the first and m, M for the second,
  t ∈ [1/2 − M/(4n), 1/2 − m/(4N)], the fractions a/b and c/d.
- Continued fraction of an interval: while both ends have the same floor
  n, n is certainly the next partial quotient; then [lo, hi] becomes
  [1/(hi − n), 1/(lo − n)], that is (a, b, c, d) → (d, c − nd, b, a − nb).
  `d and` stops the round if lo was exactly n.
- Rounds K = 9, 18, 27, …; `i` numbers the partial quotients of the
  round, and `s+=i>s!=print(n)` prints only the ones past the s already
  printed (the chained comparison calls print only when i > s, and then
  adds 1 to s).

**Notes**

- Certified: every rounding is directed and the rest is exact integer
  arithmetic, so each printed partial quotient is proven. t is irrational
  (P has infinite order, and a rational t would make it a torsion point),
  so the intervals pin down every partial quotient in turn and the program
  never stalls.
- Facts used: the Carlson forms of the elliptic integrals and the
  duplication theorem. That this t is the number of the entry rests on the
  data: all 73 terms match, and the egg integral, done by quadrature,
  agrees with the 2P formula to 30 digits. The first 273 terms also agree with
  mpmath at 1500 digits.
- 79 terms in 2 s, 273 in 60 s; the b-file is the 73 terms of the entry,
  and the bar is all of it.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 415 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001086), CC BY-SA 4.0.
