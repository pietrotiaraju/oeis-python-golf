# A002072

> a(n) = smallest number m such that for all k > m, either k or k+1 has a prime factor > prime(n).
> — [OEIS A002072](https://oeis.org/A002072)

Offset 1: 1, 8, 80, 4374, 9800, 123200, 336140, 11859210, 11859210, 177182720, 1611308699, 3463199999, …

### Python 3 — 324 bytes

```python
import math
S={2};P=p=1
while p:=p+1:
 if P**p%p:
  S|={s*p for s in S};P*=p;c=0
  for D in S-{4}:
   m=0;d=1;a=b=math.isqrt(D);h,H,k,J,x,y=b,1,1,0,1,0
   while h*h-D*k*k-1:m=d*a-m;d=(D-m*m)//d;a=(b+m)//d;h,H,k,J=a*h+H,h,a*k+J,k
   for i in[0]*(p//2+2):x,y=h*x+D*k*y,h*y+k*x;c=max(c,(pow(P,len(bin(y)),y)<1)*x//2)
  print(c)
```

**How it works**

- a(n) is the largest x such that x and x + 1 are both p-smooth,
  p = prime(n): every k > a(n) has k or k + 1 with a prime factor > p.
- **Lehmer's method.** Let P be the product of the primes up to p. If x
  and x + 1 are both p-smooth, X = 2x + 1 satisfies X² − 1 = 4x(x+1), so
  X² − 2q·Y² = 1 where q is the squarefree part of 2x(x+1), a squarefree
  p-smooth number, and q ≠ 2 (q = 2 would make x(x+1) a square). D. H.
  Lehmer (*On a problem of Størmer*, Illinois J. Math. 8 (1964), 57–79,
  Theorems 1 and 2) proved that (X, Y) is then among the first
  max(3, (p+1)/2) solutions of this Pell equation. So the p-smooth pairs
  are exactly the pairs ((X−1)/2, (X+1)/2) with X from those solutions
  and the pair smooth.
- **The equations.** `S` holds 2q for every squarefree p-smooth q:
  each new prime p (p is prime exactly when P^p mod p ≠ 0, P being the
  product of the smaller primes) doubles it with `{s*p for s in S}`.
  `S-{4}` drops q = 2.
- **The fundamental solution** of X² − D·Y² = 1, D = 2q, comes from the
  continued fraction of √D: m, d, a run through the standard recurrence
  (m ← d·a − m, d ← (D − m²)/d, a ← ⌊(⌊√D⌋ + m)/d⌋), and h/k are the
  convergents (H, J the previous ones) until h² − D·k² = 1.
- **The first solutions** are (x + y√D) = (h + k√D)^i: `x,y=h*x+D*k*y,h*y+k*x`
  from (1, 0), for i = 1 … ⌊p/2⌋ + 2, at least max(3, (p+1)/2) (checking
  more solutions cannot add a wrong pair).
- **Smoothness.** The pair's product is (x² − 1)/4 = q·y²/2, so the pair
  is p-smooth exactly when y is. y divides P^e for some e exactly when y
  is p-smooth, and any e at least the bit length of y is enough (no
  prime power in y exceeds it); `len(bin(y))` is the bit length plus 2,
  so `pow(P,len(bin(y)),y)<1` is the test. The largest
  smooth pair starts at (x−1)/2 = `x//2` (x is odd), and `c` keeps the
  maximum.

**Notes**

- Exact integer arithmetic; correct for every n by Lehmer's theorem.
- The n-th term solves 2ⁿ − 1 Pell equations with D up to twice the
  primorial, and the continued-fraction periods grow like √D: the 11th
  term (p = 31) takes about 4 s here, the 12th (p = 37, D up to
  1.5·10¹³) far longer. The b-file has 37 terms; the bar is 11 terms in
  60 s.
- [A002071](../A002071/) runs the same search and counts the pairs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 324 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002072), CC BY-SA 4.0.
