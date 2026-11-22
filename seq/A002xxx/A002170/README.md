# A002170

> High temperature series for spin-1/2 Heisenberg susceptibility on 3-dimensional simple cubic lattice.
> — [OEIS A002170](https://oeis.org/A002170)

Offset 1: 6, 48, 528, 7920, 149856, 3169248, 77046528, 2231209728, …

With Pauli matrices, H = Σ σᵢ·σⱼ over the bonds (x = J/2kT for the
Hamiltonian −2J Σ Sᵢ·Sⱼ, as in [A002164](../A002164/)) and M = Σ σᶻᵢ,
the reduced susceptibility per site is
χ(x) = ⟨M² e^{xH}⟩/(N⟨e^{xH}⟩) → 1 + Σ a(n)xⁿ/n! (⟨A⟩ = Tr A/2ᴺ; M
commutes with H, so this is the field derivative of the free energy).
The data fix this reading: a(1) = 6 is 2 for each of the 3 bonds per
site, since ⟨(σᶻ₁ + σᶻ₂)²·σ₁·σ₂⟩ = 2.

### Python 3 — 554 bytes

```python
from math import*
n=0
while 1:
 n+=1;T=n+3;a=0;R=range(n+1)
 for B in range(T**3):
  l=B%T;m=B//T%T;k=B//T//T;S=l*m*k;u=T-l-m-k
  if~u<0:
   E=[1+2**d<<i for d,q in((1,l),(l,l*m),(l*m,S))for i in range(S)if i%q<q-d];Z=[0]*-~n;W=Z[:];C=[]
   for s in range(2**S):
    v={s:1};q=(2*s.bit_count()-S)**2
    for j in R:
     g=v.get(s,0);Z[j]+=g;W[j]+=q*g;w={}
     for t in(j<n)*[*v]:
      for e in E:w[x]=w.get(x:=t^e*(0<t&e<e),0)+2*v[t]
     v=w
   for i in R:C+=W[i]-sum(comb(i,j)*C[j]*Z[i-j]for j in range(i))>>S,
   a+=(-1)**u*comb(5,u)*C[n]
 print(a)
```

**How it works**

- **Linked clusters.** For a finite graph G let F_G(x) =
  ⟨M² e^{xH_G}⟩/⟨e^{xH_G}⟩. For two parts A, B with no bond between them
  the traces factorize, and the cross term 2⟨M_A e^{xH_A}⟩⟨M_B e^{xH_B}⟩
  vanishes by spin reversal, so F is additive over components, and Möbius inversion over bond subsets writes F_G as a sum of
  weights W(F) over the connected bond sets F ⊆ G (single sites included:
  they give the 1). W(F) collects the words that use every bond of F, so
  it is O(x^{|F|}).
- **Finite-lattice method**, as on [A002169](../A002169/)'s page, with F
  in place of the cumulant: grouping the clusters of the l × m × k box by
  their bounding box gives W(l, m, k) = Δ²Δ²Δ²F and χ = Σ W over all box
  shapes. A connected F with bounding box l × m × k crosses each of the
  (l−1) + (m−1) + (k−1) planes that cut the box, and each bond crosses one
  of them, so |F| ≥ l + m + k − 3: the boxes with l + m + k ≤ T = n + 3
  give order n exactly, and the window over |σ| = T − 5…T with weights
  (−1)ᵘC(5, u), u = T − |σ|, sums them. B runs over range(T³) as three
  digits base T (empty boxes give 0), `~u<0` keeps u ≥ 0.
- **Moments of a box.** Bonds are masks `1+2**d<<i` (A001393's page);
  `0<t&e<e` tests a bond with unequal spins and `t^e` swaps them. The code
  uses 2H′ (H′ the sum of swaps) = H + (number of bonds); the constant
  cancels in the ratio F. For every start state s, `Z[j]` adds the
  diagonal entry of (2H′)ʲ and `W[j]` the same times M² = (2·popcount − S)²
  (M² is diagonal in this basis and commutes with H). `(j<n)*[*v]` skips
  the last matrix–vector product, which no moment needs.
- **Quotient.** F = W/Z as exponential generating functions:
  Fᵢ = (Wᵢ − Σ_{j<i} C(i, j)·Fⱼ·Z_{i−j})/2ˢ. ⟨M²Hʲ⟩ and ⟨Hʲ⟩ are
  identity coefficients of integer combinations of Pauli strings, hence
  integers, so every Fᵢ is an integer and `>>S` divides exactly.

**Notes**

- a(4) needs the boxes 3 × 2 × 2 (12 sites) at order 4 and takes about
  30–60 s here; a(5) needs 3 × 3 × 2 (18 sites), out of reach. The
  window is n + 3 here, not ⌊n/2⌋ + 3 as for the free energy
  ([A002169](../A002169/)): a bridge that separates the two σᶻ of M² may
  occur once, so paths of n bonds count at order n. Bar: 4 terms in
  120 s. The b-file has 17 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 554 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002170), CC BY-SA 4.0.
