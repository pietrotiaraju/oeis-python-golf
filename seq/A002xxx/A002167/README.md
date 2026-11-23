# A002167

> High temperature series for spin-1/2 Heisenberg specific heat on 3-dimensional b.c.c. lattice.
> — [OEIS A002167](https://oeis.org/A002167)

Offset 1: 0, 12, -24, 168, 1440, 24480, -297024, 28017216, …

The listed numbers are the coefficients of the free energy: with Pauli
matrices and H = Σ σᵢ·σⱼ over the bonds (x = J/2kT for the Hamiltonian
−2J Σ Sᵢ·Sⱼ, as in [A002164](../A002164/)),
ln⟨e^{xH}⟩/N → Σ a(n)xⁿ/n! per site, where ⟨A⟩ = Tr A/2ᴺ; the specific
heat is C/k = x²·d²(ln Z)/dx² = Σ a(n)xⁿ/(n−2)!. The data fix this
reading: a(2) = 12 and a(3) = −24 are 4 bonds per site times the
cumulants 3 and −6 of one bond σ₁·σ₂ (eigenvalues 1, 1, 1, −3); the
lattice has no triangles.

### Python 3 — 628 bytes

```python
from math import*
n=0
while 1:
 n+=1;T=3*n//2+3;a=0;R=range(n+1)
 for B in range(T**3*4):
  c=B%4;B//=4;l=B%T;m=B//T%T;k=B//T//T;u=T-l-m-k
  if~u<0:
   P=[(x,y,z)for x in range(l)for y in range(m)for z in range(k)if x-y&1|y-z<<1&2==c];S=len(P);Z=[0]*-~n;C=[]
   E=[1<<i|1<<j for i in range(S)for j in range(i)if all(-2<p-q<2 for p,q in zip(P[i],P[j]))]
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

- **Lattice.** Z³ with a bond between points that differ by (±1, ±1, ±1)
  is four disjoint copies of the b.c.c. lattice (the classes of the
  parities of x − y and y − z). It has
  the same free energy per site and is invariant under all unit
  translations, which the finite-lattice method needs.
- **Finite-lattice method**, as on [A002169](../A002169/)'s page: for the
  l × m × k box of points, κₙ(box) = Σ (L−l+1)(M−m+1)(K−k+1)·W(l, m, k)
  over cluster bounding boxes, W = Δ²Δ²Δ²κₙ, and a(n) = Σ W. Summed over
  the boxes with l + m + k ≤ T this is Σ (−1)ᵘC(5, u)·κₙ(σ),
  u = T − |σ| ∈ 0…5.
- **Truncation.** By the bridge lemma of [A002164](../A002164/), a cluster
  F with t bridges and c other bonds has weight 0 below order c + 2t.
  Doubling its bridges gives a bridgeless multigraph, so each of the
  (l−1) + (m−1) + (k−1) coordinate planes cutting the bounding box is
  crossed at least twice, and a bond (±1, ±1, ±1) crosses three of these
  planes: 3(c + 2t) ≥ 2(l + m + k − 3). So T = ⌊3n/2⌋ + 3 suffices.
- **Components.** The box graph falls apart into the four classes
  `x-y&1|y-z<<1&2` = c (`c=B%4`), and cumulants add over components, so
  each class is solved on its own: P lists its points and E its bonds as
  bit masks. Two points of one class are neighbours exactly when no
  coordinate differs by 2 or more (`all(-2<p-q<2…)`), since their three
  differences have the same parity.
- **κₙ of a class** exactly over its 2ˢ spin states, as on A002164's page:
  2H′ (H′ the sum of swaps) is H plus a constant, which only moves κ₁;
  the moments are integers, so the cumulant recursion divides exactly by
  2ˢ. At n = 1 the window holds only boxes without bonds, so a(1) = 0.

**Notes**

- a(5) (T = 10) needs boxes such as 4 × 3 × 3 (classes of 9 sites) and
  takes about 25–40 s here; a(6) (T = 12) needs 4 × 4 × 4, four classes
  of 16 sites at order 6, out of reach. Bar: 5 terms in 120 s. The b-file
  has 15 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 628 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002167), CC BY-SA 4.0.
