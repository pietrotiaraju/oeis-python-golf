# A002169

> High temperature series for spin-1/2 Heisenberg specific heat on 3-dimensional simple cubic lattice.
> — [OEIS A002169](https://oeis.org/A002169)

Offset 1: 0, 9, -18, -162, 2520, 33192, -1019088, -7804944, 723961728, …

The listed numbers are the coefficients of the free energy: with Pauli
matrices and H = Σ σᵢ·σⱼ over the bonds (x = J/2kT for the Hamiltonian
−2J Σ Sᵢ·Sⱼ, as in [A002164](../A002164/)),
ln⟨e^{xH}⟩/N → Σ a(n)xⁿ/n! per site, where ⟨A⟩ = Tr A/2ᴺ. The specific
heat is C/k = x²·d²(ln Z)/dx² = Σ a(n)xⁿ/(n−2)!. The data fix this
reading: a(2) = 9 and a(3) = −18 are 3 bonds per site times the cumulants
3 and −6 of one bond σ₁·σ₂ (eigenvalues 1, 1, 1, −3).

### Python 3 — 509 bytes

```python
from math import*
n=0
while 1:
 n+=1;T=n//2+3;a=0;R=range(n+1)
 for B in range(T**3):
  l=B%T;m=B//T%T;k=B//T//T;S=l*m*k;u=T-l-m-k
  if~u<0:
   E=[1+2**d<<i for d,q in((1,l),(l,l*m),(l*m,S))for i in range(S)if i%q<q-d];Z=[0]*-~n;C=[]
   for s in range(2**S):
    v={s:1}
    for j in R:
     Z[j]+=v.get(s,0);w={}
     for t in v:
      for e in E:w[x]=w.get(x:=t^e*(0<t&e<e),0)+2*v[t]
     v=w
   for i in R:C+=Z[i]-sum(comb(i-1,j-1)*C[j]*Z[i-j]for j in range(1,i))>>S,
   a+=(-1)**u*comb(5,u)*C[n]
 print(a)
```

**How it works**

- **Finite-lattice method.** For a finite graph G, κₙ(G) (the n-th
  cumulant of H_G) is a sum of weights wₙ(F) over the connected bond sets
  F ⊆ G (linked clusters, see [A002164](../A002164/)). Group the clusters of
  the l × m × k box of sites by their bounding box: since the lattice is
  invariant under unit translations,
  κₙ(L, M, K) = Σ (L−l+1)(M−m+1)(K−k+1)·W(l, m, k), so
  W = Δ²_l Δ²_m Δ²_k κₙ (second differences, κₙ = 0 for an empty box) and
  a(n) = Σ W(l, m, k) over all box shapes.
- **Truncation.** By the bridge lemma proved on [A002164](../A002164/)'s
  page, wₙ(F) = 0 unless c + 2t ≤ n, where t counts the bridges of F and c
  its other bonds. Doubling the bridges gives a bridgeless multigraph with
  c + 2t bonds; each of its cuts has at least 2 bonds, and each of the
  (l−1) + (m−1) + (k−1) planes cutting the bounding box is such a cut, met
  only by the bonds in its direction. So c + 2t ≥ 2(l + m + k − 3), and
  only the boxes with l + m + k ≤ T = ⌊n/2⌋ + 3 carry order n.
- **Window.** Summing W over the boxes with l + m + k ≤ T, the coefficient
  of κₙ(σ) is (−1)ᵘC(5, u), u = T − |σ| (worked out on
  [A001393](../A001393/)'s page), so a(n) = Σ (−1)ᵘC(5, u)·κₙ(σ) over the
  boxes with T − 5 ≤ |σ| ≤ T; `~u<0` keeps u ≥ 0 (math.comb is 0 for
  u > 5). B runs over range(T³) as three digits base T, sides 0 to T − 1;
  a box with a zero side has no sites and κₙ = 0.
- **Bonds** as masks `1+2**d<<i` (d = 1, l, l·m), kept when site i has a
  neighbour in that direction (`i%q<q-d`), as on A001393's page.
- **κₙ of a box** exactly, as on A002164's page: the operator 2H′ (H′ the
  sum of swaps) equals H + (number of bonds), which changes only κ₁, and
  a(1) = 0 comes out right since order 1 uses only the one-site box.
  `0<t&e<e` tests whether a bond joins unequal spins, `t^e` swaps them.
  `Z[j]` sums the diagonal of (2H′)ʲ over all 2ˢ states; the moments are
  integers, so the cumulant recursion
  κᵢ = mᵢ − Σ_{j<i} C(i−1, j−1)κⱼm_{i−j} divides exactly by 2ˢ.

**Notes**

- Up to n = 7 the boxes have at most 8 sites and the 7 terms print in
  about 1 s; a(8) needs the 12-site box 3 × 2 × 2 at order 8 (three of them, several minutes here).
  The bar is 7 terms in 120 s. The b-file has 17 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 509 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002169), CC BY-SA 4.0.
