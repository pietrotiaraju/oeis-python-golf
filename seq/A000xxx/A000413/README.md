# A000413

> Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)*Pi*n^(3/2), P(n) = A(n) - V(n); A000092 gives values of n where |P(n)| sets a new record; sequence gives A(A000092(n)).
> — [OEIS A000413](https://oeis.org/A000413)

Offset 0: 1, 7, 19, 57, 81, 251, 437, 691, 739, 1743, …

Here A(m) counts the integer points (i, j, k) with i² + j² + k² ≤ m, and
P(m) = A(m) − (4/3)π·m^(3/2) is its error against the volume of the ball.
The radii m where |P(m)| sets a new record are [A000092](../A000092/), with
m = 0 counted as the first record; a(n) is the count A(m) at the n-th of
them. So a(1) = A(1) = 7, a(2) = A(2) = 19, a(3) = A(5) = 57.

### Python 3 — 298 bytes

```python
from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
A=lambda n:sum(1+2*isqrt(n-a-b)for a in Q for b in Q if a+b<=n)
X=lambda n:H*H*A(n)-s(n*isqrt(12*n*H**4))
p=n=0;Q=[0];H=4**6
print(1)
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while abs(d:=abs(X(n))-abs(X(p)))<n*H:H*=2
 0<d==print(A(p:=n))
```

**How it works**

- `Q` holds x² for −⌊√n⌋ ≤ x ≤ ⌊√n⌋: 0 once and every positive square
  twice. The loop header steps n and appends n twice when it is a perfect
  square; the list is never empty, so the loop never ends.
- `A(m)` is the exact count for any m ≤ n: each pair a = x², b = y² from
  `Q` with a + b ≤ m is a column of the ball holding the
  2⌊√(m − a − b)⌋ + 1 values of z with z² ≤ m − a − b. So the record radius
  p can simply be recounted. The term is written `1+2*isqrt(…)` because
  `…+1for` draws a SyntaxWarning.
- The volume without floats: Σ_{k≥0} k!²/(2k + 1)! = 2π/(3√3) (the series
  of 2 arcsin x/√(1 − x²) at x = ½), so V(m) = √(12m³)·Σ. The term ratio is
  k/(2(2k + 1)) = (d − 1)/(4d) with d = 2k + 1; `t*~-d//4//d` is the floor
  of the next term (`~-d` is d − 1), and `s(t)` adds terms until one is 0.
- The working precision is H = 2^h with h ≥ 12. `isqrt(12*n*H**4)` is
  ⌊√(12m)·H²⌋, so X(m) = H²·A(m) − s(m·⌊√(12m)·H²⌋) is H²·P(m) from above.
- The inner loop doubles H until d = |X(n)| − |X(p)| satisfies |d| ≥ n·H.
  Then d has the sign of |P(n)| − |P(p)| (next section), and
  `0<d==print(A(p:=n))` stops at `0<d` unless n is a record; on a record
  it stores n in p and prints A(n) (2 bytes under `if d>0:`).
- `print(1)` is a(0) = A(0). The scan starts from p = 0, where X(0) = H²
  exactly and |P(0)| = 1; P(1) = 7 − 4π/3 ≈ 2.81 beats it, so the later
  records are those of A000092.

**Why the record test is exact**

- 0 ≤ X(m) − H²·P(m) < E_m = (5/3)m + (4/3)K + 16/9, where
  K ≤ log₄ t₀ + 1 is the number of nonzero terms of `s` and t₀ the first
  one (the bound is worked out on the [A000223](../A000223/) page).
  Since | |x| − |y| | ≤ |x − y|, d is within E_n + E_p of
  H²·(|P(n)| − |P(p)|).
- Write H² = 2^g, g ≥ 24. From t₀ < √12·n^(3/2)·2^g one gets
  K < 1.9 + 0.75·log₂ n + g/2, so E_n + E_p < 6n + 2g + 9 for p ≤ n. That is
  below n·H = n·2^(g/2) (63 against 4096 at n = 1, g = 24, and the right
  side grows faster in both n and g). So once |d| ≥ n·H, the sign of d is
  the true one.
- The doubling ends: |P(n)| = |P(p)| with n ≠ p would make
  (4/3)π·(n^(3/2) ∓ p^(3/2)) an integer, and π times a nonzero algebraic
  number is transcendental (Lindemann). The true gap is a fixed positive
  number, while the threshold n·H is a vanishing fraction of the scale H².

**Notes**

- This is [A000092](../A000092/)'s program with the record count printed
  instead of the radius. With the precision kept as G = H² and the
  threshold `n*isqrt(G)` it is 302 bytes; A000092's float threshold
  `n*G**.5` saves 3 of those bytes but raises OverflowError beyond
  G = 2^1024. A000223's triple count
  `sum(a+b+c<=n for a in Q for b in Q for c in Q)` is 6 bytes shorter than
  the pair sum, but costs O(n^(3/2)) per radius: 24 terms in 20 s here,
  under the bar.
- Exact integer arithmetic and an exact record test, so the program is
  right for every n. The only limit is the recursion in `s`, about
  g/2 + 0.75·log₂ n + 2 deep: it reaches Python's default limit of 1000
  only if two values of |P| agree to about 300 decimal digits.
- Each radius costs two pair sums over the roughly 4n pairs of `Q`, so the
  scan up to radius N takes O(N²) steps. Here 33 terms (record radius
  3150) print in 20 s, with H reaching 2^14.
- The b-file has 43 terms (up to a(42)); the bar is 31 terms in 20 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 302 | first entry |
| 2026-11-07 | Python 3 | 298 | precision H = √G, threshold n·H without isqrt |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000413), CC BY-SA 4.0.
