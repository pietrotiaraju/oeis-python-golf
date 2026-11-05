# A000223

> Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)Pi*n^(3/2), P(n) = A(n) - V(n); A000092 gives values of n where |P(n)| sets a new record; sequence gives nearest integer to P(A000092(n)).
> — [OEIS A000223](https://oeis.org/A000223)

Offset 1: 3, 7, 10, 19, 32, 34, 37, 51, 81, 119, 122, 134, 157, 160, …

### Python 3 — 293 bytes

```python
from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
X=lambda n:G*sum(a+b+c<=n for a in Q for b in Q for c in Q)-s(n*isqrt(12*n*G*G))
p=n=0;Q=[0];G=8**8
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while min(abs(d:=abs(x:=X(n))-abs(X(p))),(y:=x+G//2)%G)<n*G**.5:G*=2
 if d>0:print(y//G);p=n
```

**How it works**

- Lattice points: `Q` holds x² for −⌊√n⌋ ≤ x ≤ ⌊√n⌋ (0 once, every other
  square twice). The loop header steps n and appends n twice when it is a
  perfect square. Then `sum(a+b+c<=n for a in Q for b in Q for c in Q)` is
  A(n), and also A(m) for any m ≤ n, so the record holder m is kept in `p`
  and its count is simply redone.
- π without floats: Σ_{k≥0} k!²/(2k+1)! = 2π/(3√3) (the series of
  2 arcsin x/√(1 − x²) at x = ½), so V(n) = √(12n³) · Σ. The term ratio is
  k/(2(2k+1)) = (d − 1)/(4d) with d = 2k + 1, and `t*~-d//4//d` is its
  floor (nested floors). `s(t)` adds the floored terms until one is 0.
- Error bound: with t₀ = n·⌊√(12n)·G⌋, `X(n) = G·A(n) − s(t₀)` is at least
  G·P(n) and exceeds it by less than E_n = (5/3)n + (4/3)K + 16/9, where
  K ≤ log₄ t₀ + 1 is the number of terms. Floors only make terms smaller;
  t₀ is short by less than n; each later term inherits at most ¼ of the
  previous error plus less than 1, so the k-th is short by less than
  n/4^k + 4/3; and the true tail after the first zero term is below
  (4/3)(n/4^K + 4/3). For n = 0 everything is exact: X(0) = G.
- Decisions: G starts at 2^24 and only doubles. With T = n√G the inner loop
  doubles G until both |X(n)| − |X(m)| and (X(n) + G/2) mod G are at least
  T. For 2^24 ≤ G < 2^1024 one has T ≥ E_n + E_m (at n = 1 it is 4096
  against about 41, and T grows faster in both n and G; checked by script
  for every such power of two). So the sign of |X(n)| − |X(m)| is the sign
  of |P(n)| − |P(m)|, and ⌊(X(n) + G/2)/G⌋ = ⌊P(n) + ½⌋, the nearest
  integer: X(n) is an upper bound, so the only danger is a multiple of G
  just below X(n) + G/2, and the mod test rules that out.
- The loop always ends: π is transcendental (Lindemann), so π·α is not
  algebraic for algebraic α ≠ 0. P(n) = ±P(m) with n ≠ m would give
  (4/3)π(n^(3/2) ∓ m^(3/2)) = A(n) ∓ A(m), and P(n) + ½ ∈ ℤ would make
  π·n^(3/2) rational. Both gaps are fixed positive numbers while T/G → 0.
- Start: p = 0 with A(0) = 1 and V(0) = 0, so the first threshold is
  |P(0)| = 1; P(1) = 7 − 4π/3 ≈ 2.81 beats it, so the records are the same
  as when counting from n = 1. The program prints round(P) with its sign,
  so a negative record (none so far, see Hasler's comment on the OEIS page)
  would also come out right.
- `min(…)<n*G**.5` tests both conditions with one tolerance; Python
  compares ints with floats exactly.

**Notes**

- Each n costs two triple sums over `Q`, about 16·n^(3/2) steps. Here 20
  terms take 3.5 s and 26 take 26 s; the 27th (n = 1890) is out of reach
  in 60 s. The bar is 20 terms in 60 s.
- Some n come close to the record: G is up to 2^40 by n = 990.
- Limits: `G**.5` raises OverflowError beyond G = 2^1024, which would take a
  gap below about n·2^−511; the recursion in `s` is then about 520 deep,
  under the default limit.
- Longer variants: keeping A(m) next to m instead of recounting it (13 bytes,
  2–3 times faster); the 2D count `2*isqrt(n-a-b)+1` over pairs (299 bytes,
  38 terms in 60 s); Euler's π/2 = Σ k!/(2k+1)!!, which needs
  t₀ = ⌊(8/3)n^(3/2)·G⌋ (3 bytes); cubes over `range(-r,r+1)` instead of
  `Q` (1 byte); the exact t₀ = ⌊√(12n³)·G⌋ (2 bytes, needed only if T lost
  its factor n).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 293 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000223), CC BY-SA 4.0.
