# A000694

> Related to population of numbers of form x^2 + y^2.
> — [OEIS A000694](https://oeis.org/A000694)

Offset 1: 1, 2, 4, 6, 11, 19, 34, 63, 117, 218, 411, 780, 1487, …

### Python 3 — 370 bytes

```python
from math import*
n=1;P=9
while F:=1<<P:R=range(4*P);L=lambda s,a,u=0:sum(comb(P,k+1)*(u:=u+(-1)**k*F//(a*k+1)**s)for k in R);Q=lambda s:F*(s>P)or isqrt(L(s,1)*(F+F//(2**s-2))//L(s,2)*Q(2*s));S=lambda r,X,v=F:X*sum(v//(k-~k)+r+0*(v:=v*X//-~k//F+r)for k in R)**2;a,b=[(isqrt(32*(Q(2)+t)*S(t>0,n*((L(1,1)>>P)+t))>>4*P)+3)//6for t in(P*P,-P*P)];a-b or print(a);n+=a==b;P+=1
```

**How it works**

a(n) = round((2/3)·K·I) with I = ∫₁^(2ⁿ) dt/√(log t) and K the
Landau–Ramanujan constant (the OEIS Maple program). It is
[A000691](../A000691/) with an extra factor 2/3, and the program is the same
certified interval computation.

- Let x = (2/3)KI be the value that is rounded and z = 3x = 2KI. Then
  z² = 4K²I² = 8·P₃(2)·X·σ² (X = n log 2, σ = Σ Xᵏ/(k!(2k+1)),
  2K² = P₃(2)), the quantity A000691 bounds, and the program bounds
  4z² = 32·P₃(2)·X·σ².
- round(z/3) = ⌊(2z + 3)/6⌋ = (isqrt(⌊4z²⌋) + 3)//6, again increasing in
  z². This is one byte shorter than dividing by 9 and keeping A000691's
  `+1>>1`.
- `L`, `Q`, `S` and the error bounds are explained on the
  [A000690](../A000690/) and [A000691](../A000691/) pages: Q(2) and
  `L(1,1)>>P` are within P² of F·P₃(2) and F·log 2 (F = 2ᴾ), `S` rounds
  down for r = 0 and up for r = 1, and a term is printed only when both ends
  of the interval give the same value; otherwise P grows by one and the term
  is tried again.

**Notes**

- Only integers, so every printed term is proved. The retry loop ends unless
  (2/3)·K·I is exactly a half-integer.
- The OEIS notes that Shanks' 1964 table has a wrong a(16) (10555); the
  b-file value 10562 is what the formula gives, and what this program prints.
- Beyond the 33 terms of the b-file the values were checked up to n = 149
  against an independent implementation.
- The 33 terms print in well under a second. The bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 370 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000694), CC BY-SA 4.0.
