# A001393

> High temperature series for spin-1/2 Ising free energy on 3-dimensional simple cubic lattice.
> — [OEIS A001393](https://oeis.org/A001393)

Offset 0: 1, 0, 3, 22, 192, 2046, 24853, 329334, 4649601, 68884356, …

With v = tanh K, the partition function per spin of the simple cubic Ising
model is z = 2 cosh³K · Λ(v), Λ(v) = Σ a(n) v²ⁿ (the OEIS comment). Expanding
each bond weight e^{Kσσ′} = cosh K (1 + vσσ′) turns the partition function
of a graph with s sites and E edges into 2ˢ coshᴱK · Z(v), where Z(v) counts
the even subgraphs (every vertex of even degree) by their number of edges.
Λ is the per-site limit Z^{1/N} of these, so a(1) = 0 (no even subgraph has
2 edges) and a(2) = 3 (the three plaquettes at each site).

### Python 3 — 368 bytes

```python
t=3
while 1:
 X=8**t**3;Y=X**(2*t-6);M=X*Y;P=1
 for a in 1,-5,10,-10,5,-1:
  for B in range(t**3):L=B//t;B%=t;s=L*B*max(t-L-B,0);D=[1+2**k<<i for k,q in((1,L),(L,L*B),(L*B,s))for i in range(s)if i%q<q-k];E=len(D);w=[(1+X)**(E-d)*(1-X)**d for d in range(E+1)];P*=pow(sum(w[sum(0<g&e<e for e in D)]for g in range(1<<s))>>s,a,M)
  t-=1
 print((P+Y*-~X//2)%M//Y-X//2);t+=7
```

**How it works**

- Finite-lattice method. Let Z(l, m, k) be the even-subgraph polynomial of
  the l × m × k box of sites (free boundaries). Its logarithm is a sum over
  clusters of polymers (connected even subgraphs, overlapping ones linked),
  and grouping the clusters by their bounding box gives
  ln Z(L, B, C) = Σ (L−l+1)(B−m+1)(C−k+1) w(l, m, k), so that
  w = Δ²_l Δ²_m Δ²_k ln Z (second differences in each direction, with
  ln Z = 0 for an empty box) and ln Λ = Σ w(l, m, k) over all box shapes.
- Truncation: the polymers of a cluster are even subgraphs, so their union
  (with multiplicity) is a connected multigraph with all degrees even; an
  Euler circuit through it goes from one end of the box to the other and
  back in every direction, so a cluster spanning an l × m × k box has at
  least 2(l + m + k − 3) edges and w(l, m, k) = O(v^{2(l+m+k−3)}). Hence
  boxes with l + m + k ≤ T = n + 3 give Λ exactly up to v²ⁿ.
- Collecting the second differences: the coefficient of ln Z(σ) in
  Σ_{|b|≤T} w(b) is Σ_{j≤u} [xʲ](1−x)⁶ = (−1)ᵘ C(5, u), u = T − |σ|. So
  Λ ≡ Π Z(σ)^{(−1)ᵘC(5,u)} (mod v^{2n+1}) over the boxes with
  T − 5 ≤ |σ| ≤ T: integer powers only, no logarithms. The loop runs t from
  n + 3 down through the six window values with exponents
  `1,-5,10,-10,5,-1`, over the boxes with L + B + C = t (B runs over
  range(t³), L = B//t, B%t, and C = t − L − B is clipped at 0: an empty box
  gives Z = 1).
- Z(box) by brute force over the 2ˢ spin configurations, bits of g:
  Σ_σ Π_edges (1 + vσσ′) = 2ˢ Z(v). An edge from site i to i + k (k = 1, L,
  L·B, kept when i % q < q − k with q = L, L·B, s) is the mask
  e = (1 + 2ᵏ) << i, and it joins unequal spins iff `0<g&e<e`. With d such
  edges the configuration weighs (1+v)^{E−d}(1−v)^d (the list `w`).
- Kronecker substitution v ↦ X = 8^{t³}: Z[v]/(v^K) → Z/X^K (K = 2n + 1) is
  a ring homomorphism, and every Z(box) is ≡ 1 (mod X), a unit, so `pow`
  with M = X^K and negative exponents maps the product to the image of Λ.
  P is not reduced after each factor; the last line reduces it.
- Reading the coefficient: the image is Σ λ_k X^k (mod X^K) with λ_{2j} =
  a(j), λ_odd = 0, possibly negative a priori. `(P+Y*-~X//2)%M//Y-X//2`
  (Y = X²ⁿ) rounds the symmetric residue to the top digit, which is λ_{2n}
  whenever every |λ_k| ≤ X/4. Bound: on the torus of side 2n + 1
  (N = (2n+1)³ sites) no cluster with at most 2n edges winds around, so
  Z_torus ≡ Λᴺ (mod v^{2n+1}); with Z_torus = 1 + Q,
  0 ≤ Q ≤ (1+v)^{3N} − 1 coefficientwise and |C(1/N, j)| ≤ 1, this gives
  |λ_k| ≤ 2^{k−1}(3N)^k ≤ (6N)²ⁿ, far below X/4 = 2^{3(n+3)³−2}.

**Golf notes**

- The window form (six exponents, one Z per box) replaces the 27-term
  second differences of every box and needs no series logarithm or
  exponential; with Kronecker integers the whole power-series algebra is
  `pow` and `*`.
- `0<g&e<e` (one edge mask) is shorter than `(g>>i^g>>j)&1` over index
  pairs; the masks `1+2**k<<i` need no parentheses.
- `t+=7` after the six `t-=1` steps moves to the next n, so n itself is
  never stored; `range(t**3)` is empty for t ≤ 0 (n = 0, 1), where
  `range(t*t)` would make boxes with negative sides.

**Notes**

- Exact integer arithmetic throughout; the method is the standard
  finite-lattice method of de Neef and Enting, with the cluster expansion
  as formal power series, so the program is right for every n given
  unlimited time.
- The time is dominated by the largest boxes, 2ˢ configurations each:
  a(5) comes after about 12 s here (3 × 2 × 2 and 3 × 3 × 2 boxes);
  a(6) needs the 3 × 3 × 3 box (2²⁷ configurations) and the 4 × 3 × 2 boxes,
  several minutes.
- The b-file is synthesized from the OEIS data (24 terms, up to a(23));
  the bar is 6 terms (up to a(5)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 368 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001393), CC BY-SA 4.0.
