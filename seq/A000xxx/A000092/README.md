# A000092

> Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)*Pi*n^(3/2),
> P(n) = A(n) - V(n); sequence gives values of n where |P(n)| sets a new
> record.
> — [OEIS A000092](https://oeis.org/A000092)

Offset 1: 1, 2, 5, 6, 14, 21, 29, 30, 54, 90, 134, 155, 174, 230, 234, 251, 270, …

### Python 3 — 284 bytes

```python
from math import*
n=a=m=q=k=0
while R:=range(-(r:=isqrt(n:=n+1)),r+1):
 A=sum(2*isqrt(t)+1for x in R for y in R if(t:=n-x*x-y*y)>=0)
 while abs(d:=abs(A*2**k-isqrt(q*n**3))-abs(a*2**k-isqrt(q*m**3)))<=A:k+=3;q=sum(32*4**k//i//i//comb(2*i,i)for i in range(1,k))
 if d>0:print(m:=n);a=A
```

**How it works**

- A(n) = Σ (2⌊√t⌋ + 1) over the columns (x, y) with t = n − x² − y² ≥ 0:
  a column holds the 2⌊√t⌋ + 1 values of z with z² ≤ t. `R` is
  −⌊√n⌋ … ⌊√n⌋, and `if(t:=…)>=0` drops the columns outside the disc.
- Everything is compared at scale S = 2ᵏ, in integers. Since
  2·arcsin²(x) = Σ (2x)²ⁱ/(i²·C(2i, i)), at x = ½ the sum
  Σ 1/(i²·C(2i, i)) is π²/18, so (4π/3)² = 32·Σ 1/(i²·C(2i, i)).
  `q` = Σ_{i<k} ⌊32·4ᵏ/(i²·C(2i, i))⌋ is (4π/3)²·4ᵏ from below, and
  `isqrt(q*n**3)` is S·V(n) from below. `A*2**k-isqrt(q*n**3)` is then
  S·P(n) up to a small error: no π, no √n, no floats.
- The record is kept as the pair (a, m) = (A(m), m) and measured again at the
  current precision on every test, so d ≈ S·(|P(n)| − |P(m)|). While
  |d| ≤ A(n) the sign is not certain yet: k grows by 3 (eight times the
  scale) and `q` is recomputed. k never goes back down, so almost every n
  is decided at once with the precision already reached (k = 21 by
  n ≈ 8000).
- a = m = 0 is a record of 0, so n = 1 is the first record. q = k = 0 at the
  start gives d = A − a, between 0 and A, so the very first test always
  refines before deciding anything.
- `if d>0:print(m:=n);a=A` prints the new record and stores it.

**Why it is exact**

- One term's error: √(Q·n³) − ⌊√(q·n³)⌋ lies in [0, ρₖ·n^{3/2} + 1), where
  Q = (4π/3)²·4ᵏ and ρₖ = (Q − q)/√Q. The floors lose less than k − 1 in
  all, and since C(2i, i) ≥ 4ⁱ/(2√i) the terms from i = k on add up to less
  than 85.4/k^{3/2}. That gives ρ₃ = 0.416 and ρₖ < 0.041 for k ≥ 6.
- So d is within 2·(0.416·n^{3/2} + 1) < 0.84·n^{3/2} + 2 of
  S·(|P(n)| − |P(m)|), as m < n. And A(n) ≥ 0.84·n^{3/2} + 2 for every
  n ≥ 1: the unit cubes centred at the lattice points of the ball cover the
  ball of radius √n − √3/2, so A(n) ≥ (4π/3)(√n − √3/2)³, which is at least
  1.5·n^{3/2} ≥ 0.84·n^{3/2} + 2 from n = 9 on; n ≤ 8 is checked directly
  (A = 7, 19, 27, 33, 57, 81, 81, 93). Once |d| > A(n),
  d therefore has the sign of |P(n)| − |P(m)|.
- The refining ends: |P(n)| = |P(m)| would make (4π/3)(n^{3/2} ∓ m^{3/2})
  an integer, and π times a non-zero algebraic number is transcendental
  (Lindemann). The true gap times 2ᵏ grows without bound while the error
  stays below A(n).
- So every record test is decided exactly, for every n.

**Notes**

- The count costs about πn `isqrt` calls per n: the 30 terms of the bar
  (n ≤ 2757) print in about 2 s and about 44 terms (n ≈ 10 700) in 60 s. The
  b-file's 155 terms go up to n = 79 858 350.
- The bar is 30 terms in 60 s. This straightforward count manages about 44;
  counting every (x, y, z) of the cube, 7 bytes shorter, is O(n^{3/2}) per n
  and stops at 26 or 27 terms.
- A list of the plane counts D(m) = 1 + 4·Σ_{i≤√m} ⌊√(m − i²)⌋ gives
  A(n) = 2·Σ_{i≤√n} D(n − i²) − D(n) in O(√n) per n:
  `R=range(isqrt(n)+1);D+=1+4*sum(isqrt(n-i*i)for i in R),;A=2*sum(D[n-i*i]for i in R)-D[n]`
  with `D=[1]` is 291 bytes and prints 89 terms (n = 494 550) in 60 s, all
  matching the b-file, close pairs such as 201 600, 201 601 included.
- Floats are not enough: deciding which of two n has the larger |P| needs π
  and the square roots to more digits as n grows, and a fixed precision
  would fail for some n.
- A fixed precision per n, as in [A000036](../A000036/), would need a lower
  bound for |K − (4π/3)·α| with α = n^{3/2} ∓ m^{3/2} algebraic of degree up
  to 4, that is a transcendence measure of π rather than Mahler's
  irrationality measure. Refining until the sign is certain needs no such
  bound, only that the two values are never equal.
- The 285-byte version began its `while 1:` body with `n+=1;R=range(…);`.
  Naming the value in the loop condition is 1 byte shorter and keeps the
  loop going, because the range always holds 0, and `n:=n+1` moves into it.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 285 | first entry |
| 2026-11-05 | Python 3 | 284 | value named in the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000092), CC BY-SA 4.0.
