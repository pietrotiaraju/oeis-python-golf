# A000250

> Number of symmetric reflexive relations on n nodes: (1/2)*A000666.
> — [OEIS A000250](https://oeis.org/A000250)

Offset 1: 1, 3, 10, 45, 272, 2548, 39632, 1104306, 56871880, 5463113568, 978181717680, 326167542296048, 202701136710498400, …

### Python 3 — 137 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r-k,*L,k)<<k//2-~sum(map(math.gcd,L,[k]*n))for k in range(1,r+1))//r
n=1
while[print(f(n)>>1)]:n+=1
```

**What is counted**

- A000666(n) counts graphs on n unlabelled nodes where loops are allowed
  (symmetric relations). By Burnside's lemma it is (1/n!) Σ_π 2^T(π), where
  T(π) is the number of orbits of π on the C(n+1, 2) unordered pairs {x, y},
  x = y allowed. A cycle of length k has ⌊k/2⌋ + 1 orbits on its own pairs
  (⌊k/2⌋ edge orbits and one loop orbit), and two cycles of lengths k and l
  have gcd(k, l) orbits of pairs between them.
- a(n) is half of A000666(n), hence the `>>1`, and the halving is exact for
  every n ≥ 1. Grouped by cycle type, A000666(n) = Σ_λ 2^T(λ)/z_λ with
  z_λ = Π k^(c_k)·c_k! (c_k parts equal to k), and every term has 2-adic
  valuation at least the number of parts: each part k brings ⌊k/2⌋ + 1 ≥
  v₂(k) + 1 to T, and the k·C(c_k, 2) ≥ c_k − 1 orbits between equal parts
  make up for v₂(c_k!) ≤ c_k − 1. So the integer A000666(n) is even.

**How it works**

- `f(r,*L)` is (1/r!) Σ_σ 2^N(σ) over the permutations σ of r further points,
  given the lengths `L` of the cycles already chosen, where N counts only the
  orbits of pairs that touch one of the r points. The cycle through one fixed
  point has length k in (r − 1)!/(r − k)! ways, so

  f(r, L) = (1/r) Σ_{k=1..r} 2^(⌊k/2⌋ + 1 + Σ_{l∈L} gcd(k, l)) · f(r − k, L + [k]).

  The new cycle brings its own ⌊k/2⌋ + 1 orbits and gcd(k, l) for every
  earlier cycle; orbits between it and later cycles are counted when those
  are chosen. f(n) with no cycles yet is A000666(n).
- `k//2-~s` is ⌊k/2⌋ + 1 + s, and the whole exponent sits to the right of
  `<<` with no parentheses since `<<` binds looser than `+`.
- `map(math.gcd,L,[k]*n)` pairs k with every earlier cycle: `L` has at most
  n entries, so `[k]*n` is long enough. `import math` plus `math.gcd` is a byte
  shorter than `from math import*` plus `gcd`, and `map` is 2 bytes under
  `sum(math.gcd(k,l)for l in L)`. The import-free count
  `sum(x*l%k<1for l in L for x in range(k))` (gcd(k, l) is the number of x < k
  with k | x·l) is also 139 bytes.
- `r<1or` returns `True` when no points are left, and `True<<s` is an int.

**Dividing by r at every level**

The `//r` is exact because every f(r, L) is an integer, the same argument as
for [A000171](../A000171/). Fix a permutation τ of a set Y with cycle lengths
L. Then 2^N(σ) is the number of on/off patterns on the pairs that touch the r
points X that σ×τ fixes. By de Bruijn's lemma, for a group H normal in G and
g ∈ G, (1/|H|) Σ_{h∈H} fix(hg) is the number of H-orbits that g maps to
themselves; with H = S_r and g = τ, f(r, L) is such a count. So the program
never needs n! or the cycle-type weights z_λ.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The recursion visits all 2^(n−1) compositions of n, so the time doubles
  every term: 23 terms in about 42 s here. The bar is 18 terms in 60 s; the
  b-file has 40. A partition sum like the [A000088](../A000088/) program
  (with `k//2+1` and a final halving) reaches the whole b-file but is about
  40 bytes longer.
- a(n) has a little under 0.15·n² digits, so Python's 4300-digit int-to-str
  limit would only stop the printing at n = 175.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 137 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000250), CC BY-SA 4.0.
