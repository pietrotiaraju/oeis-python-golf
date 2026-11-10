# A001407

> High temperature series for partition function for spin-1/2 Ising model on f.c.c. lattice.
> — [OEIS A001407](https://oeis.org/A001407)

Offset 0: 1, 0, 0, 8, 33, 168, 962, 5928, 38907, 268056, …

With v = tanh K, the partition function per spin of the face-centred cubic
Ising model is 2 cosh⁶K · Λ(v), Λ(v) = Σ a(n) vⁿ: expanding each bond weight
e^{Kσσ′} = cosh K (1 + vσσ′) turns the partition function of a graph with
s sites and E edges into 2ˢ coshᴱK · Z(v), where Z(v) counts the even
subgraphs (every vertex of even degree) by their number of edges, and Λ is
the per-site limit of Z. So a(3) = 8 and a(4) = 33 are the numbers of
triangles and of four-cycles per site; the simple cubic analogue is
[A001393](../A001393/).

### Python 3 — 456 bytes

```python
import math
t=3
while 1:
 X=8**t**3;Y=X**(t-3);M=X*Y;P=1
 for a in 1,-5,10,-10,5,-1:
  for B in range(2*t*t):V=[(x,y,z)for x in range(B//t%t)for y in range(B%t)for z in range(t-B//t%t-B%t)if(x+y+z+B//t//t)%2];s=len(V);D=[1<<i|1<<j for i in range(s)for j in range(i)if math.dist(V[i],V[j])<2];E=len(D);w=[(1+X)**(E-d)*(1-X)**d for d in range(E+1)];P*=pow(sum(w[sum(0<g&e<e for e in D)]for g in range(1<<s))>>s,a,M)
  t-=1
 print((P+Y*-~X//2)%M//Y-X//2);t+=7
```

**How it works**

- The f.c.c. lattice is the set of integer points with an even coordinate
  sum; the 12 neighbours of a point differ from it by (±1, ±1, 0) up to
  order, so two points of one parity class are neighbours exactly when they
  are at distance √2 (`math.dist(...)<2`; the next distance is 2).
- Finite-lattice method, as in A001393, with boxes of l × m × k integer
  points (free boundaries) that hold the sites of either parity class: `V`
  lists the points with x + y + z + p odd, p = 0 or 1. For
  F(l, m, k) = ln Z(box, p = 0) + ln Z(box, p = 1), group the clusters of
  the cluster expansion by their bounding box: every offset of a cluster's
  box inside a larger box puts it into exactly one of the two classes, so
  F(L, M, N) = Σ (L−l+1)(M−m+1)(N−k+1) w(l, m, k), w = Δ²_l Δ²_m Δ²_k F,
  and ln Λ = Σ w over all shapes (each class of a large box holds half of
  its points).
- Truncation: a bond changes two coordinates by 1, and an Euler circuit
  through the edges of a cluster spanning an l × m × k box changes the
  coordinates by at least 2(l−1) + 2(m−1) + 2(k−1) in total, at most 2 per
  edge; so w(l, m, k) = O(v^{l+m+k−3}) and the boxes with l + m + k ≤
  T = n + 3 give Λ exactly up to vⁿ. Collecting the second differences
  gives A001393's window: Λ ≡ Π Z(σ)^{(−1)ᵘC(5,u)} (mod v^{n+1}) over the
  boxes σ of both classes with T − 5 ≤ l + m + k ≤ T, u = T − (l+m+k).
- The loop runs `t` from n + 3 down through the window with exponents
  `1,-5,10,-10,5,-1`; B runs over range(2t²) and gives the sides B//t%t,
  B%t, t − B//t%t − B%t and the class B//t//t (empty ranges make an empty
  box, Z = 1). Z(σ) is brute force over the 2ˢ spin configurations as in
  A001393: edge masks `1<<i|1<<j`, `0<g&e<e` for an edge joining unequal
  spins, weights (1+v)^{E−d}(1−v)^d.
- Kronecker substitution v ↦ X = 8^{t³} modulo M = X^{n+1} (every Z(σ) is
  ≡ 1 mod X, a unit), and `(P+Y*-~X//2)%M//Y-X//2` (Y = Xⁿ) reads the
  coefficient of vⁿ when all coefficients are below X/4 in size. Bound: on
  a torus of even side L ≥ max(4, n + 1) (N = L³/2 sites, 6N edges) no
  cluster with at most n edges winds around (winding changes a coordinate
  by L > n, at most 1 per edge), so Z_torus ≡ Λᴺ (mod v^{n+1}) and, as in
  A001393, |[vᵏ]Λ| ≤ 2^{k−1}(6N)ᵏ, far below X/4 = 2^{3(n+3)³−2}.

**Golf notes**

- One loop index carries the two free sides and the parity class; the
  third side and empty boxes come free from `range`.
- `math.dist(V[i],V[j])<2` is 7 bytes shorter than summing squared
  coordinate differences and comparing with 2; `from math import*` would
  shadow the three-argument `pow`.
- The two parity classes could share one box (they are not linked, so Z
  of all points is the product), but that squares the number of spin
  configurations.

**Notes**

- Every step is exact integer arithmetic and the truncation order is proved
  above, so the program is correct for every n. a(6) comes after about 2 s
  and a(7), whose largest boxes (3 × 3 × 4, 18 sites per class) need 2¹⁸
  spin configurations, after about 41 s here; a(8) needs 24-site boxes
  (2²⁴ configurations) and is far out of reach.
- The b-file has 16 terms (a(0) to a(15), the terms of the entry); the bar
  is 8 terms (up to a(7)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 456 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001407), CC BY-SA 4.0.
