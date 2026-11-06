# A000413

> Let A(n) = #{(i,j,k): i^2 + j^2 + k^2 <= n}, V(n) = (4/3)*Pi*n^(3/2), P(n) = A(n) - V(n); A000092 gives values of n where |P(n)| sets a new record; sequence gives A(A000092(n)).
> — [OEIS A000413](https://oeis.org/A000413)

Offset 0: 1, 7, 19, 57, 81, 251, 437, 691, 739, 1743, …

### Python 3 — 302 bytes

```python
from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
A=lambda n:sum(2*isqrt(n-a-b)+1for a in Q for b in Q if a+b<=n)
X=lambda n:G*A(n)-s(n*isqrt(12*n*G*G))
p=n=0;Q=[0];G=8**8
print(1)
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while abs(d:=abs(X(n))-abs(X(p)))<n*isqrt(G):G*=2
 0<d==print(A(p:=n))
```

**How it works**

- For the current radius parameter n, Q holds 0 once and each
  positive square through n twice, representing the two signs of
  its root. The walrus increments n before the square test and
  appends `[n,n]` exactly when n is a perfect square.
- For fixed first and second coordinates with squares a,b, there
  are 2⌊√(n−a−b)⌋+1 possible third coordinates. Summing that
  quantity over Q×Q with a+b≤n therefore gives the exact A(n).
  The same Q can recount A(p) for p≤n: the filter excludes all
  squares too large for the older radius.
- To compare P(n)=A(n)−(4π/3)n^(3/2), use the convergent
  identity Σₖ≥₀ k!²/(2k+1)!=2π/(3√3). Multiplying it by
  √(12n³) gives the sphere volume V(n).
- The series-term ratio is (d−1)/(4d), starting at d=3 and
  then increasing d by 2. `s(t)` sums the integer terms from t
  onward, replacing each next term by `t*~-d//4//d` until
  it becomes zero; `~-d` means d−1.
- With t₀=n·⌊√(12nG²)⌋, the result s(t₀) approximates
  G·V(n) from below. Thus X(n)=G·A(n)−s(t₀) approximates
  G·P(n) from above, using exact integer arithmetic throughout.
- p holds the last record radius. Compute
  d=|X(n)|−|X(p)|, and double G until |d|≥n·isqrt(G).
  The error bound below makes the sign of this comparison reliable.
- `0<d==print(A(p:=n))` short-circuits unless d>0. On a
  record it stores n in p and prints the exact count A(n), not
  the estimated discrepancy X(n). The outer condition Q remains
  a nonempty list, so a failed record test does not stop the scan.
- `print(1)` supplies A(0), the origin, before the positive-radius
  records of [A000092](../A000092/). At n=1 the seven lattice
  points beat the origin's discrepancy record, giving the next 7.

**Why the record test is exact**

- The floor-error calculation on [A000092](../A000092/) and
  [A000223](../A000223/) gives
  0≤X(n)−G·P(n)<E_n=(5/3)n+(4/3)K+16/9,
  where K≤log₄t₀+1 counts the nonzero terms in s. The origin
  has zero error, since X(0)=G exactly.
- Absolute value changes a comparison by at most E_n+E_p.
  For p≤n, G=2ᵍ and g≥24, the term-count bound gives the
  coarse estimate E_n+E_p<6n+2g+9, smaller than n·isqrt(G).
  Thus an accepted comparison has the true sign of |P(n)|−|P(p)|.
- Distinct radii cannot tie: equality of their absolute discrepancies
  would make π times a nonzero algebraic number equal an integer,
  contradicting the transcendence of π. The true gap is nonzero,
  while the comparison error and threshold divided by G tend to zero.
  Hence doubling G eventually decides every comparison.

**Notes**

- This is [A000092](../A000092/) with the output changed from
  each record radius to its exact lattice-point count, and `isqrt(G)`
  replacing a floating square root in the stopping threshold.
- Each candidate recomputes two sums over about 2√n square entries,
  so scanning through radius parameter N costs O(N²) pair visits,
  apart from the adaptive precision work. The radii, rather than the
  number of emitted records, drive the runtime.
- G starts at 8⁸=2²⁴ and only doubles. The integer implementation
  has no fixed-precision cutoff; the recursive series can eventually
  meet Python's recursion limit if an unusually close comparison
  requires enough terms.
- The b-file has 43 terms (indices 0 through 42). The bar is the
  first 31 terms in 20 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 302 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000413), CC BY-SA 4.0.
