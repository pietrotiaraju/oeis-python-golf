# A001537

> Invertible Boolean functions with AG(n,2) acting on the domain and range.
> — [OEIS A001537](https://oeis.org/A001537)

Offset 1: 1, 1, 4, 302, 2569966041123963092, 76230976900860740792605252293646252383143627390965685153124757864

### Python 3 — 611 bytes

```python
from math import*
n=1
while 1:
 N=2**n;D={};S=[(len(C),e)for e in range(1,N,2)for k in range(e)if gcd(k,e)<2>k-min(C:={k*2**j%e for j in range(e)})+1]
 def R(r,s,F,w,c=0,p=0,z=0):
  if s:d,e=s[0];R(r,s[1:],F,w);[R(r-d*x,s,(*(f*(x*b<(y:=t&-t))<<d*min(x,y>>t%e*N)for t,f in enumerate(F)),),w//(2**(d*(C:=c*(x==p)+1))-1)>>d*(2*z+x-C)+(e<2),C,x,z+x)for x in range(p or 1,r//d+1)for b in{0,e<2}]
  elif r<1:D[F]=D.get(F,0)+w
 R(n,S,(1,)*-~N,K:=factorial(N));T=0
 for F,c in D.items():
  F=[*F];z=c*c
  for k in range(1,N+1):z*=k**(u:=F[k]//k)*factorial(u);F[k::k]=[f-F[k]for f in F[k::k]]
  T+=z
 print(T//K**2);n+=1
```

**What is counted**

- An invertible Boolean function of n variables is a permutation σ of the
  N = 2ⁿ points of GF(2)ⁿ. Two of them are equivalent when σ' = α∘σ∘β with
  α, β affine maps x ↦ Ax + b (A invertible), the group H = AGL(n,2). So
  a(n) is the number of double cosets H\S_N/H; a(3) = 4 and all six terms
  agree.
- Burnside's lemma for H×H acting by σ ↦ hσk⁻¹: σ is fixed when
  σ⁻¹hσ = k, which needs h and k to have the same cycle type λ on the
  points, and then holds for z_λ = Π_k k^(c_k)·c_k! permutations σ (c_k the
  number of k-cycles). So a(n) = Σ_λ m_λ²·z_λ, where m_λ is the share of
  affine maps with cycle type λ.
- Cycle lengths are at most N, so the cycle type of g is fixed by
  F(t) = fix(gᵗ) for t = 1 … N: F(t) is the number of points on cycles of
  length dividing t.

**Affine maps by type**

- *Linear part.* A makes GF(2)ⁿ a module over GF(2)[x]: a sum of blocks
  GF(2)[x]/(p^λ), p irreducible, p ≠ x, one partition λ_p per p, with
  Σ deg(p)·|λ_p| = n. The matrices A of a given type are a share
  1/Π_p a(λ_p, 2^deg p) of GL(n,2), where a(λ,q), the number of module
  automorphisms, is q^(Σ_(i,j) min(λᵢ,λⱼ))·Π(1 − q^(−c)), with c running from
  1 to m over each group of m equal parts (Macdonald, Symmetric Functions
  and Hall Polynomials, II.1). Adding the parts in non-decreasing order, a
  part x multiplies a(λ,q) by q^(2|λ|+x−c)·(q^c − 1), c = the number of
  parts equal to x so far, itself included.
- *Which p.* If the roots of p have multiplicative order e (odd), then
  deg p = d is the order of 2 mod e, and these p are the minimal
  polynomials of the elements of order e of GF(2^d): there are φ(e)/d of
  them, one for each orbit {k·2^j mod e} of the units k of Z_e. `S` lists
  one pair (d, e) per orbit: k a unit and the smallest of its orbit, d the
  orbit's size. Pairs with d > n only ever get the empty partition.
- *Fixed points of the linear part.* For t = 2^a·u with u odd,
  xᵗ − 1 = (x^u − 1)^(2^a) and x^u − 1 is squarefree, divisible by p exactly
  when e | u, that is e | t. So on GF(2)[x]/(p^λ) the kernel of Aᵗ − I has
  dimension d·min(λ, 2^a) when e | t and 0 otherwise; 2^a is `t&-t`.
- *Translation.* gᵗ(x) = Aᵗx + b_t with b_t = (I + A + … + A^(t−1))b. On
  the blocks with p ≠ x+1, A − I is invertible and
  b_t = (Aᵗ − I)(A − I)⁻¹b is always in the image of Aᵗ − I. On the unipotent
  part (p = x+1), with N = A − I nilpotent, Aᵗ − I = N^(2^a)·U and
  b_t = N^(2^a−1)·U'·b with U, U' invertible and commuting with N (because
  (1+y)^u − 1 = y·(unit) for odd u). Write b, modulo the image of N, as a
  choice of blocks (its coordinates in the cokernel of N, one per block):
  N^(2^a−1)·b lies in the image of N^(2^a) exactly when every chosen block
  has size s < 2^a. So fix(gᵗ) = fix(Aᵗ) when the largest chosen block is
  below 2^a (or none is chosen), and 0 otherwise. Each of the 2^ℓ choices
  (ℓ unipotent blocks) is made by 2^(n−ℓ) vectors b, a share 2^(−ℓ).

**How it works**

- `R(r,s,F,w,c,p,z)` walks the list `s` of polynomial slots (d, e) with
  r dimensions left, either closing the current slot (`R(r,s[1:],F,w)`) or
  adding a part x ≥ p (the previous part; `c` counts the parts equal to p,
  `z` adds up the slot's parts). Parts of the unipotent slot (e = 1) come
  twice, `b` = 0 or 1 for "not chosen" or "chosen".
- `F` holds fix(gᵗ) for t = 0 … N (index 0 is a dummy that every part sets
  to 0). A part x of slot (d, e) multiplies F(t) by 2^(d·min(x, t&−t)) when
  e | t (`y>>t%e*N` is `t&-t` when e | t and 0 otherwise), and a chosen
  unipotent part also by [x < t&−t].
- `w` starts at K = N! and is divided by each factor q^(2z+x−c)·(q^c − 1),
  and by 2 for a unipotent part: at a leaf (r = 0, no slot left) it is K
  times the share of affine maps of that type and choice. Every division is
  exact: with m ≤ n the dimensions used so far, the factors multiply to a
  divisor of |AGL(m,2)| = 2^m·|GL(m,2)| (the module automorphisms form a
  subgroup of GL(m,2), and there is at most one factor 2 per dimension), and
  AGL(m,2) acts faithfully on 2^m points, so its order divides (2^m)! and K.
- `D[F]` adds these up, K·m_λ for the cycle type λ given by F. For each F,
  the sieve `F[k::k]=[f-F[k]…]` turns F(k) into the number of points on
  k-cycles (k ascending), `u` is the number of k-cycles, and `z` collects
  K²·m_λ²·z_λ; `T//K**2` is a(n).

**Notes**

- The program uses only the module structure, never lists matrices: all 6
  b-file terms (n = 1 to 6) come out in under 0.2 s here; the bar is the
  whole b-file in 60 s. a(7) and a(8) follow in about 0.7 s and 6 s.
- The recursion goes once through every slot, so at n = 9 (several hundred
  slots for the odd e < 512) it passes Python's recursion limit and stops
  with a RecursionError, long after the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 611 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001537), CC BY-SA 4.0.
