# A002164

> E.g.f.: high-temperature series in J/2kT for logarithm of partition function for the spin-1/2 linear (1D) Heisenberg model.
> — [OEIS A002164](https://oeis.org/A002164)

Offset 1: 0, 3, -6, -30, 360, 504, -44016, 204048, 8261760, -128422272, …

With Pauli matrices and H = Σᵢ σᵢ·σᵢ₊₁ on a chain (−βH for the Hamiltonian
−2J Σ Sᵢ·Sᵢ₊₁ is x·H with x = J/2kT), a(n) is the n-th cumulant per site of
H under the normalized trace ⟨A⟩ = Tr A/2ᴺ:
ln⟨e^{xH}⟩/N → Σ a(n)xⁿ/n! as N → ∞. The data fix this normalization:
a(2) = 3 and a(3) = −6 are the second and third cumulants of one bond
σ₁·σ₂ (eigenvalues 1, 1, 1, −3).

### Python 3 — 350 bytes

```python
from math import*
C=[0,1,0];N=0
while 1:
 N+=1;R=range(2*N+3);T=[0]*5*N;K,C=C,[]
 for s in range(2**N):
  v={s:1}
  for j in R:
   T[j]+=v.get(s,0);w={}
   for t in v:
    for i in range(N):w[u]=w.get(u:=t^(0<t>>i&3<3)*3<<i,0)+2*v[t]
   v=w
 for n in R:C+=T[n]-sum(comb(n-1,j-1)*C[j]*T[n-j]for j in range(1,n))>>N,
 for n in R[-4:-2]:print(C[n]-K[n])
```

**How it works**

- **Linked clusters.** For a finite graph G let κₙ(G) be the n-th cumulant
  of H_G = Σ_{edges} σᵤ·σᵥ. The trace of operators on disjoint sets of sites
  factorizes, so ln⟨e^{xH}⟩ is additive over connected components, and
  Möbius inversion over edge subsets gives κₙ(G) = Σ wₙ(F) over the
  connected edge sets F ⊆ G, with a weight wₙ(F) that depends only on F. On
  a line the connected edge sets are the paths Pₖ (k bonds), so a chain of
  N + 1 sites has κₙ = Σₖ (N + 1 − k)·wₙ(Pₖ), and the difference between the
  chains of N + 1 and N sites is Σ_{k ≤ N} wₙ(Pₖ), while a(n) = Σₖ wₙ(Pₖ).
- **Bridge lemma.** wₙ(F) is the sum, over the words of n edges that use
  every edge of F, of their joint cumulants, so it is enough that a joint
  cumulant vanishes when some bridge e = uv of F occurs only once. Split the
  sites of F at e into the side A of u and the side B of v. Operators on A
  and on B commute, so cyclically every word with one X_e is
  Tr(P_uv·α·β), with α on A and β on B products of bond operators (here
  X = σ·σ = 2P − 1 and P is the swap). Tr(P_uv·α⊗β) = Tr_u(α′β′), where α′
  is the partial trace of α down to u and β′ that of β down to v; both
  commute with SU(2), so they are multiples of the identity, and
  Tr(P_uv·αβ) = Tr(αβ)/2 = ⟨P⟩·Tr(αβ). So every moment with one X_e
  factorizes as ⟨X_e⟩ times the moment without it (also inside
  e^{Σ tₑXₑ}, by Duhamel's formula), which makes all joint cumulants with a
  single X_e zero. On a path every bond is a bridge, so wₙ(Pₖ) = 0 for
  n < 2k: the chains of N + 1 and N sites give a(n) exactly for all
  n ≤ 2N + 1, for every n with no conjecture involved.
- **Moments.** Pass N works on the chain of N + 1 sites (bits of an int)
  with the operator 2H′, H′ = Σ swaps. Since σ·σ = 2P − 1, 2H′ = H + N: the
  shift changes only κ₁, and `C=[0,1,0]` (the previous pass for one site,
  with κ₁ = 1 put in) makes a(1) come out 0. `0<t>>i&3<3` tests whether the
  spins i and i + 1 differ, and `t^3<<i` swaps them. `T[j]` adds the
  diagonal entries ⟨s|(2H′)ʲ|s⟩ over the 2ᴺ states with the last spin down;
  spin reversal gives the other half the same values. Each Tr Hʲ is a sum of
  ±2^{i+c} over products of i ≤ j swaps with c ≥ N + 1 − i cycles, so the
  moments ⟨(2H′)ʲ⟩ are integers and `>>N` divides exactly.
- **Cumulants.** κₙ = mₙ − Σ_{j<n} C(n−1, j−1)·κⱼ·m_{n−j} with
  mₖ = `T[k]`/2ᴺ, evaluated as one integer division. Pass N computes κ
  through order 2N + 2 and prints a(2N − 1), a(2N) as `C[n]-K[n]`, with
  `K` the list of pass N − 1 (exact through 2N).

**Notes**

- Pass N costs about 4ᴺ steps (5× per pass in practice): the bar, 18 terms
  (N = 9, 512 starting states), takes about 11 s here, and 20 terms about
  54 s. The b-file has 51 terms (Shiroishi and Takahashi, from an integral
  equation of the quantum transfer matrix method); this brute force checks
  the 18 required ones from the definition alone.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 350 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002164), CC BY-SA 4.0.
