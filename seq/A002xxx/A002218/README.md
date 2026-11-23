# A002218

> Number of unlabeled nonseparable (or 2-connected) graphs (or blocks) with n nodes.
> — [OEIS A002218](https://oeis.org/A002218)

Offset 1: 0, 1, 1, 3, 10, 56, 468, 7123, 194066, 9743542, 900969091, 153620333545, …

### Python 3 — 521 bytes

```python
from math import*
P=[0,1];N=1
def F(L,Q,m):
 S[:]=map(int.__add__,S,Q+[L.count(1)*Q[N]])
 for k in range(m,N+1-sum(L)):e=k//2+sum(gcd(k,j)for j in L);F(L+[k],[(sum(Q[i-k*j]*P[j]for j in range(i//k+1))<<e)//k//-~L.count(k)for i in range(N+1)],k)
def l(h):
 d=[0];a=[1]
 for n in range(1,len(h)):d+=(n*h[n]-sum(d[j]*h[n-j]for j in range(n)))//h[0],;a+=(d[n]-sum(j*a[j]for j in range(1,n)if n%j<1))//n,
 return a
while 1:N+=1;P+=0,;S=[0]*N*2;K=perm(N);F([],[K]+[0]*N,1);P[N]=(S[N-1]-S[N+1])//K;print(l(S)[N-1]-l(P[1:])[N-2])
```

**How it works**

Robinson's method (J. Combin. Theory 9 (1970) 327–356), in the language
of species (Bergeron, Labelle and Leroux, *Combinatorial Species and
Tree-like Structures*, §4.2), with every multivariate step pushed down
to power series in one variable.

- **Cycle index sums.** Let G, C, B be the cycle index sums of graphs,
  connected graphs and blocks (K₂ is a block, K₁ is not, as in the entry),
  in the power sums p₁, p₂, …. A permutation of cycle type λ has
  e(λ) = Σᵢ⌊λᵢ/2⌋ + Σ_(i<j) gcd(λᵢ, λⱼ) orbits on vertex pairs, so
  G = Σ_λ 2^e(λ) p_λ / z_λ. Write C• = p₁∂C/∂p₁ (rooted connected
  graphs) and B′ = ∂B/∂p₁. Three standard identities:
  G = E(C) (a graph is a set of components), C• = X·E(B′(C•)) (the
  blocks at the root, each carrying rooted graphs at its other
  vertices), and the dissymmetry theorem for the block–vertex tree,
  C + C•·B′(C•) = C• + B(C•).
- **Inverting C•.** C• = p₁ + …, so it has a plethystic inverse Ψ
  (C•∘Ψ = Ψ∘C• = X, a virtual species). Composing the last identity with
  Ψ and using B′(C•) = sLog(C•/X) gives
  B = C∘Ψ − X + X·sLog((C•/X)∘Ψ), where sLog is the plethystic
  logarithm, sLog(F) = Σ_k μ(k)/k · log F(p_k, p_2k, …).
- **One variable.** Plethysm by Ψ and the substitution pₖ ↦ xᵏ are ring
  maps that commute with pₖ-plethysm, so with ψ(x) = Ψ(x, x², …) the
  number of blocks is b(x) = B(x, x², …) = c(x) − x − x·s(x), where
  c = sLog(g), g(x) = G(ψ(x), ψ(x²), …), and s = sLog(ψ/x) (because
  (C•/X)∘Ψ specializes to x/ψ). C = sLog(G) gives c = sLog(g), and
  C• = p₁(∂G/∂p₁)/G turns C•∘Ψ = X into G•(ψ) = x·G(ψ), with
  G• = p₁∂G/∂p₁ = Σ_λ m₁(λ)·2^e(λ) p_λ / z_λ (m₁ = number of 1s in λ).
  So only the explicit G is ever expanded.
- **Finding ψ.** In [xᴺ](G•(ψ) − x·G(ψ)) the coefficient ψ_N appears
  once, through the p₁ term of G• (coefficient 1): every other monomial
  is a product of at least two series starting at x, or a ψ(xᵏ) with
  k ≥ 2. So with ψ known below N and ψ_N = 0 for the moment,
  ψ_N = [x^(N−1)]G(ψ) − [xᴺ]G•(ψ). That is `P[N]=(S[N-1]-S[N+1])//K`;
  `S` is scaled by K = N! (`perm(N)`). Each pass of the `while` adds one
  coefficient of ψ, and then g is right up to x^(N−1) and ψ/x up to
  x^(N−2), enough for b(N − 1), which is what it prints.
- **The sum over λ** (`F`): partitions with parts in increasing order
  (`m` is the smallest allowed part, `N+1-sum(L)` bounds the next one).
  `Q` is K·2^e(λ)/z_λ · ψ(x^λ₁)ψ(x^λ₂)… truncated at xᴺ: adding a part k
  multiplies by ψ(xᵏ) (the inner sum: [xⁱ] = Σⱼ Q[i − kj]·ψⱼ), by
  2^(⌊k/2⌋ + Σ gcd(k, j)) (`<<e`, the new pair orbits) and divides by k
  and by the new multiplicity of k (z_λ = Πₖ k^mₖ mₖ!). These divisions
  are exact because z_λ divides |λ|!, which divides K. Every node adds
  `Q` to `S` (map with `int.__add__`), and m₁·Q[N] to the extra slot
  `S[N+1]`.
- **sLog** (`l`): for h with h₀ ≠ 0, d = x·h′/h comes from x·h′ = h·d,
  that is n·hₙ = Σ_(j=1..n) dⱼhₙ₋ⱼ, and the coefficients aₙ of sLog(h)
  satisfy Σ_(j|n) j·aⱼ = dₙ (taking x d/dx of log of h = Π(1 − xᵐ)^(−aₘ)).
  d is unchanged by scaling h, so `l(S)` is sLog(g). `a[0]` = 1 stands
  for the "1 +" in x·(1 + s(x)), so b(N − 1) = `l(S)[N-1]-l(P[1:])[N-2]`
  holds at N − 1 = 1 too (b(1) = c₁ − 1 = 0).

**Notes**

- Exact integers throughout. ψ, g and the sLogs have integer
  coefficients (type generating series of virtual species), and every
  floor division is exact at the coefficients that are used; the last
  slot of each list can be a floor, and it is never read.
- ψ starts x − x² − x³ − 3x⁴ − 18x⁵ − ….
- Term N needs all partitions of size ≤ N + 1 (about 2·10⁵ at N = 40).
  The whole b-file (40 terms) comes in about 95 s on this PC (about
  50 reference seconds); the bar is 32 terms in 60 s, which arrive in
  about 8 reference seconds. Memory stays near 10 MB.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 521 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002218), CC BY-SA 4.0.
