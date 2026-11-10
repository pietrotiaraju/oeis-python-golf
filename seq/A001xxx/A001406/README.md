# A001406

> High temperature series for partition function for spin-1/2 Ising model on b.c.c. lattice.
> — [OEIS A001406](https://oeis.org/A001406)

Offset 0: 1, 0, 12, 148, 2568, 53944, 1283270, 33268932, 918420570, …

With v = tanh K, the partition function per spin of the body-centred cubic
Ising model is 2 cosh⁴K · Λ(v), Λ(v) = Σ a(n) v²ⁿ: expanding each bond weight
e^{Kσσ′} = cosh K (1 + vσσ′) turns the partition function of a graph with
s sites and E edges into 2ˢ coshᴱK · Z(v), where Z(v) counts the even
subgraphs (every vertex of even degree) by their number of edges, and Λ is
the per-site limit of Z. The lattice is bipartite, so only even powers
occur; a(2) = 12 and a(3) = 148 are the numbers of 4- and 6-cycles per site.
The simple cubic and f.c.c. analogues are [A001393](../A001393/) and
[A001407](../A001407/).

### Python 3 — 574 bytes

```python
import math
n=0
while 1:
 S=n+1;X=8**S**3;Y=X**(2*n);M=X*Y;P=1;Q=[[(1+X)**(k-j)*(1-X)**j+(1-X)**(k-j)*(1+X)**j for j in range(k+1)]for k in range(9)]
 for e in range(32):V=[(x,y,z)for x in range(S-e%2)for y in range(S-e//2%2)for z in range(S-e//4%2)if(x+e//8)%2==(y+e//16)%2==z%2];A,R=sorted([[v for v in V if v[2]%2^r]for r in(0,1)],key=len);N=[sum(1<<i for i,a in enumerate(A)if math.dist(a,b)<2)for b in R];P*=pow(sum(math.prod(Q[m.bit_count()][(g&m).bit_count()]for m in N)for g in range(1<<len(A)))>>len(V),(-1)**(e%8).bit_count(),M)
 print((P+Y*-~X//2)%M//Y-X//2);n+=1
```

**How it works**

- In half-lattice units the b.c.c. sites are the integer points whose three
  coordinates have the same parity, and a bond is a step (±1, ±1, ±1):
  two such points are neighbours exactly when they are at distance √3
  (`math.dist(a,b)<2`; the next distance is 2).
- Finite-lattice method with boxes of l × m × k integer points (free
  boundaries). Relative to the box corner the sites are the points with
  x + c₁ ≡ y + c₂ ≡ z (mod 2) for one of four classes (c₁, c₂) (the four
  cosets of the lattice in ℤ³). With F(l, m, k) the sum of ln Z(box) over
  the four classes, every offset of a cluster's bounding box inside a larger
  box puts the cluster into exactly one class, so
  F(L, M, N) = Σ (L−l+1)(M−m+1)(N−k+1) w(l, m, k), w = Δ²Δ²Δ²F, and
  ln Λ = Σ w (each class of a large box holds a quarter of its points).
- Truncation: every bond changes every coordinate by 1, so an Euler circuit
  through the edges of a cluster whose box has a side of l points has at
  least 2(l − 1) edges: w(l, m, k) = O(v^{2(max(l,m,k)−1)}). So for a(n) the
  boxes with all sides ≤ S = n + 1 suffice, and summing w over them
  telescopes to the first differences
  ln Λ ≡ Δ_lΔ_mΔ_k F(S, S, S) (mod v^{2S}): eight boxes with sides S or
  S − 1 and signs (−1)^{number of S−1 sides}. `e` runs over 32 = 8 boxes ×
  4 classes; `(-1)**(e%8).bit_count()` is the sign.
- Z(box): the box graph is bipartite (z even / z odd), so the spins of the
  larger part R are summed out exactly: a site with k neighbours in the
  smaller part A, j of them with spin −1 (`(g&m).bit_count()` for its
  neighbour mask m), contributes Σ_{σ=±1} Π(1 + vσσᵢ) =
  (1+v)^{k−j}(1−v)^j + (1−v)^{k−j}(1+v)^j, the table `Q`. Then
  Σ over the 2^{|A|} spin patterns g of A of the products is 2ˢ Z(v), and
  `>>len(V)` divides out 2ˢ exactly.
- Kronecker substitution v ↦ X = 8^{S³} modulo M = X^{2n+1}, as in
  A001393: every Z(box) is ≡ 1 (mod X), a unit, so the signs are `pow`
  exponents ±1, and `(P+Y*-~X//2)%M//Y-X//2` (Y = X²ⁿ) reads the
  coefficient of v²ⁿ when all coefficients are below X/4 in size. Bound: on
  a torus of even side L ≥ max(4, 2n + 1) (N = L³/4 sites, 4N edges) no
  cluster with at most 2n edges winds around (that changes a coordinate by
  L, at most 1 per edge), so Z_torus ≡ Λᴺ (mod v^{2n+1}) and, as in
  A001393, |[vᵏ]Λ| ≤ 2^{k−1}(4N)ᵏ, far below X/4 = 2^{3(n+1)³−2}.

**Golf notes**

- Because the truncation depends on the longest side only, the eight-box
  first difference replaces A001393's six-term window over all shapes.
- `sorted(...,key=len)` picks the smaller half of the bipartite box to
  enumerate; summing out the other half turns 2^{lmk/4} configurations into
  at most 2¹² here.
- `range(k+1)` in `Q` matters: `(1+X)**(k-j)` with k < j would be a float
  overflow.

**Notes**

- Every step is exact integer arithmetic and the truncation order is proved
  above, so the program is correct for every n. a(4) (boxes of 5 × 5 × 5
  points) comes after about 13 s here; a(5) needs 6 × 6 × 6 boxes whose two
  halves have 27 sites each, 2²⁷ patterns per class, out of reach.
- The b-file has 9 terms (a(0) to a(8), the terms of the entry); the bar is
  5 terms (up to a(4)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 574 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001406), CC BY-SA 4.0.
