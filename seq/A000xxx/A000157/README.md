# A000157

> Number of Boolean functions of n variables.
> — [OEIS A000157](https://oeis.org/A000157)

Offset 1: 1, 2, 7, 111, 308063, 100126976263592, 131867858014413288241233435594064, …

### Python 3 — 239 bytes

```python
from itertools import*
n=1
while 1:
 t=k=0
 for*m,p in product(range(2**n),permutations(range(n))):
  for w in p:m+=[y^1<<w for y in m];r=b=1
  for x in m:
   while~m[x]:b&=m[x]!=x;m[x],x=-1,m[x];r<<=m[x]<0
  t+=r<<b;k+=4
 print(t//k);n+=1
```

**What is counted**

- OEIS gives a(n) = [A000370](https://oeis.org/A000370)(n)/2, where A000370
  counts Boolean functions of n variables up to permuting the inputs,
  negating inputs and negating the output (NPN classes).
- Permuting and negating inputs is the group B_n of 2ⁿ·n! maps
  g(x) = P·x ⊕ s on the 2ⁿ points of {0,1}ⁿ (P a permutation of the
  coordinates, s a mask). By Burnside's lemma,
  A000370(n) = Σ_g (fix(g) + fix(g·¬)) / (2·|B_n|).
- A function is fixed by g when it is constant on each cycle of g on the
  points, so fix(g) = 2^c(g), with c(g) the number of cycles. It is fixed by
  g·¬ when it alternates along every cycle, which needs every cycle to have
  even length; then there are again 2^c(g) such functions.
- So a(n) = Σ_g 2^c(g)·(2 if all cycles of g are even, else 1) / (4·|B_n|).

**Odd cycle ⟺ fixed point**

The program never measures cycle lengths. For g in B_n, some cycle has odd
length exactly when g has a fixed point. A fixed point is a cycle of length
1. Conversely, if x lies on a cycle of odd length L, let
u = x ⊕ g(x) ⊕ … ⊕ g^(L−1)(x). An affine map over GF(2) commutes with sums of
an odd number of terms, so g(u) = g(x) ⊕ … ⊕ g^L(x) = u, and u is a fixed
point.

**How it works**

- `for*m,p in product(…)` runs over every mask s and permutation p; the
  starred target makes `m` the one-element list `[s]`.
- `for w in p:m+=[y^1<<w for y in m]` doubles the list once per coordinate,
  so that `m[x]` = s ⊕ (bit i of x moved to bit p[i]): `m` is g as a
  permutation of `range(2**n)`. The same line resets `r=b=1` (n times, which
  does no harm).
- The cycle walk marks each visited point with −1, checks `m[x]!=x` on the
  way (`b` stays 1 only if g has no fixed point) and doubles `r` whenever a
  step lands on a visited point, which closes a cycle. At the end
  `r<<b` = 2^c(g)·(2 or 1).
- `for x in m` reads entries that may already be −1. In Python `m[-1]` is
  `m[2**n-1]`, so starting from −1 only walks the cycle of the last point if
  it is still unvisited; each cycle is still walked once. On that path the
  fixed-point test compares with −1 instead of 2ⁿ − 1 and could miss a fixed
  point there, but that is harmless: the fixed points of g form a coset of
  the kernel of x ↦ x ⊕ P·x, so there are none or at least two, and the
  others are tested from their own index.
- `k` grows by 4 per group element, so `t//k` = Σ_g 2^c(g)·(2 or 1) / (4·|B_n|).

**Notes**

- The program walks all 2ⁿ·n! elements on 2ⁿ points: it prints 6 terms in
  about 1.5 s, and the seventh, 645 120 elements on 128 points, takes about
  90 s. The bar is 6 terms in 60 s; the b-file has 11.
- The same formula summed over the conjugacy classes of B_n (signed cycle
  types) reproduces all 11 b-file terms. That version is much longer.
- Tracking the parity of each cycle instead of looking for fixed points
  works too, but costs 11 more bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 239 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000157), CC BY-SA 4.0.
