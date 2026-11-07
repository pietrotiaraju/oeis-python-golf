# A000092

> Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)*Pi*n^(3/2),
> P(n) = A(n) - V(n); sequence gives values of n where |P(n)| sets a new
> record.
> — [OEIS A000092](https://oeis.org/A000092)

Offset 1: 1, 2, 5, 6, 14, 21, 29, 30, 54, 90, 134, 155, 174, 230, 234, 251, 270, …

### Python 3 — 270 bytes

```python
from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
X=lambda n:H*H*sum(1+2*isqrt(n-a-b)for a in Q for b in Q if a+b<=n)-s(n*isqrt(12*n*H**4))
p=n=0;Q=[0];H=4**6
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while abs(d:=abs(X(n))-abs(X(p)))<n*H:H*=2
 0<d==print(p:=n)
```

**How it works**

The machinery is [A000223](../A000223/)'s, which prints the nearest
integer to P at these same n; here only the record test is left.

- Lattice points: `Q` holds x² for −⌊√n⌋ ≤ x ≤ ⌊√n⌋ (0 once, every other
  square twice). The loop header steps n and appends n twice when it is a
  perfect square. A(n) = Σ (1 + 2⌊√(n − a − b)⌋) over pairs a, b in `Q` with
  a + b ≤ n: each pair (x², y²) is a column of the ball, holding the
  2⌊√t⌋ + 1 values of z with z² ≤ t = n − x² − y². The same sum gives A(m)
  for any m ≤ n, so the record holder m is kept in `p` and its count is
  simply redone. The term is written `1+2*isqrt(…)` because `…+1for` draws
  a SyntaxWarning (`1for` reads as a malformed number literal).
- π without floats: Σ_{k≥0} k!²/(2k+1)! = 2π/(3√3) (the series of
  2 arcsin x/√(1 − x²) at x = ½), so V(n) = √(12n³) · Σ. The term ratio is
  k/(2(2k+1)) = (d − 1)/(4d) with d = 2k + 1, and `t*~-d//4//d` is its
  floor. `s(t)` adds the floored terms until one is 0.
- The working precision is G = H² with H = 2^h, h ≥ 12. `isqrt(12*n*H**4)`
  is ⌊√(12n)·G⌋, so `X(n) = G·A(n) − s(n·⌊√(12n)·G⌋)` is G·P(n) from above.
- The inner loop doubles H until |X(n)| − |X(p)| is at least n·H = n√G away
  from 0, then `0<d==print(p:=n)` prints n and makes it the record when
  d > 0: the chained comparison stops at `0<d` when that is false, so
  `print` runs only for a record (2 bytes under `if d>0:`).
- p = 0 with A(0) = 1 and V(0) = 0 is a record of |P(0)| = 1, and
  P(1) = 7 − 4π/3 ≈ 2.81 beats it, so the records are the same as when
  counting from n = 1.

**Why it is exact**

- A(n) is an exact count.
- X(n) exceeds G·P(n) by less than E_n = (5/3)n + (4/3)K + 16/9, where
  K ≤ log₄ t₀ + 1 is the number of terms of `s`: floors only make terms
  smaller, t₀ is short by less than n, and each later term inherits at most
  ¼ of the previous error plus less than 1 (the bound is worked out on the
  A000223 page). X(0) = G exactly.
- Write G = 2^g with g ≥ 24 even. From t₀ < √12·n^(3/2)·2^g one gets
  K < 1.9 + 0.75·log₂ n + g/2, so E_n + E_m < 6n + 2g + 9 for m ≤ n. That
  is below the threshold T = n·H = n·2^(g/2) (63 against 4096 at n = 1,
  g = 24, and T grows faster in both n and g). So once |d| ≥ T, d has the
  sign of |P(n)| − |P(m)|.
- The doubling ends: |P(n)| = |P(m)| with n ≠ m would make
  (4/3)π(n^{3/2} ∓ m^{3/2}) an integer, and π times a non-zero algebraic
  number is transcendental (Lindemann). The gap is a fixed positive number
  while T/G → 0.
- So every record test is decided exactly, for every n.

**Notes**

- Each n costs two pair sums over `Q`, about 8n `isqrt` calls. Here 39
  terms (up to n = 8154) print in 60 s; the bar's 30 terms end at n = 2757.
- The b-file has 155 terms (up to a(155) = 79 858 350); the bar is 30 terms
  in 60 s.
- The previous record (271 bytes) kept G itself: `X=lambda n:G*sum(…)`,
  `isqrt(12*n*G*G)`, `G=8**8` and the float threshold `n*G**.5` with
  `G*=2`. With H = √G the threshold is `n*H` (4 bytes less) for `H*H*` and
  `H**4` (3 more), and the float is gone: `G**.5` raised OverflowError
  beyond G = 2^1024.
- A000223's triple sum `sum(a+b+c<=n for a in Q for b in Q for c in Q)` is
  6 bytes shorter but O(n^{3/2}) per n: it stops at 26 terms, under the
  bar of 30.
- Limits: the recursion in `s` is about g/2 + 0.75·log₂ n + 2 deep, so it
  reaches Python's default limit of 1000 only if two values of |P| agree to
  about 300 decimal digits.
- The 284-byte version counted A(n) over `R=range(-r,r+1)` and got π² from
  Σ 1/(i²·C(2i, i)) = π²/18: `q` = Σ_{i<k} ⌊32·4ᵏ/(i²·C(2i, i))⌋
  is (4π/3)²·4ᵏ from below, `isqrt(q*n**3)` is 2ᵏ·V(n), and the record was
  stored as the pair (A(m), m). Recounting A(p) and A000223's arcsin series
  for π itself are 13 bytes shorter.
- A list of the plane counts D(m) = 1 + 4·Σ_{i≤√m} ⌊√(m − i²)⌋ gives
  A(n) = 2·Σ_{i≤√n} D(n − i²) − D(n) in O(√n) per n (291 bytes in the old
  layout, 89 terms in 60 s), but costs more bytes than it saves here.
- Floats are not enough: deciding which of two n has the larger |P| needs π
  and the square roots to more digits as n grows, and a fixed precision
  would fail for some n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 285 | first entry |
| 2026-11-05 | Python 3 | 284 | value named in the while condition |
| 2026-11-05 | Python 3 | 271 | A000223's π series, recount A(p), pair sums |
| 2026-11-07 | Python 3 | 270 | precision H = √G, threshold n·H without floats (as in A000413) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000092), CC BY-SA 4.0.
