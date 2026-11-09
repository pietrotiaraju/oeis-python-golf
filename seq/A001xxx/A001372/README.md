# A001372

> Number of unlabeled mappings (or mapping patterns) from n points to themselves; number of unlabeled endofunctions.
> — [OEIS A001372](https://oeis.org/A001372)

Offset 0: 1, 1, 3, 7, 19, 47, 130, 343, 951, 2615, 7318, 20491, 57903, 163898, 466199, …

### Python 3 — 200 bytes

```python
from functools import*
r=[n:=0,1]
g=cache(lambda m,k:m<1or k and g(m,k-1)+sum(r[i]*g(m-k*i,k)for i in range(1,m//k+1)))
while[print(+g(-n,-n))]:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
```

**What is counted**

- The graph of a map f: X → X splits into connected components, and each
  component is a cycle of rooted trees (the points on the cycle are the
  roots). So up to relabelling a mapping is a multiset of cycles, up to
  rotation, of rooted trees, and with T(x) = Σ tₖxᵏ the g.f. of rooted trees
  ([A000081](../../A000xxx/A000081/)) the g.f. is
  **∏ₖ≥₁ 1/(1 − T(xᵏ))** (R. C. Read; the PARI program of the entry). It
  follows from the cycle index of the cyclic groups: the multiset of cycles
  has g.f. exp(Σⱼ Σₖ φ(k)/(jk)·log 1/(1 − T(x^(jk)))), and grouping by m = jk
  with Σ_{k|m} φ(k) = m leaves exp(Σₘ log 1/(1 − T(xᵐ))).

**How it works**

- **Partial products.** g(m, k) is the coefficient of xᵐ in
  Pₖ = ∏_{j≤k} 1/(1 − T(xʲ)). From Pₖ = Pₖ₋₁ + T(xᵏ)·Pₖ,
  g(m, k) = g(m, k − 1) + Σᵢ tᵢ·g(m − ki, k) (i ≥ 1), with g(m, 0) = [m = 0].
  T(xᵏ) starts at xᵏ, so the factors with k > m do not touch xᵐ and
  a(m) = g(m, m). `functools.cache` keeps every g(m, k), so each new term
  costs O(m log m) cached steps.
- **The trees.** `r` = [t₀, t₁, …] grows by one term per round with the
  A000081 program: n = −m and
  m·t(m+1) = Σₖ k·tₖ·Σⱼ t(m+1−jk), read with negative slices `r[d::d]`. So
  when a(m) is printed, `r` holds t₀ … t_(m+1), more than g needs.
- `m<1or` returns `True` for g(0, k); the `+` in the print turns a(0) into 1.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n.
- Computing g(m, m) first calls g(m, m − 1), g(m, m − 2), …, g(m, 0) in a
  chain, so the recursion is about m deep: with Python's default recursion
  limit the program stops with a `RecursionError` after a(997), an interpreter
  limit (not counted as a failure). Those 998 terms print in about 7 s here.
  The b-file has 2129 terms (up to a(2128)); the bar is 800 terms in 60 s.
- Multiplying lists of coefficients instead, recomputing the product for every
  term, came to about 210 bytes and is much slower.

## First 20 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(19) have to arrive in time.

### Python 3, 20 terms — 145 bytes

```python
import math
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or math.prod(sum(j*(i%j<1)for j in L)for i in L)
n=0
while[print(f(n))]:n+=1
```

**How it works**

- **Burnside.** Relabelling by a permutation π turns a map f into πfπ⁻¹, and
  the orbits of S_n are the mappings up to relabelling. So
  a(n) = (1/n!) Σ_π |{f : fπ = πf}|.
- **Maps that commute with π.** If fπ = πf, then f(πⁱx) = πⁱf(x), so f is
  fixed by its value y = f(x) at one point x of each cycle of π. Any y works
  as long as πˡy = y for the length l of x's cycle, that is, as long as y lies
  on a cycle whose length divides l. So a cycle of length i has
  Σ j choices, summed over the cycles of π whose length j divides i (every
  point of such a cycle), and the count is the product over the cycles:
  `math.prod(sum(j*(i%j<1)for j in L)for i in L)`.
- **The sum over permutations.** `f(r,*L)` averages over the permutations of
  r further points given the cycle lengths `L` so far: for each length r − k
  of the cycle through a fixed new point, (r − 1)! of the r! permutations,
  then the remaining k points; at r = 0 it returns the count above. `//r` is
  exact at every level (de Bruijn's form of Burnside's lemma, as on
  [A000273](../../A000xxx/A000273/): each partial sum counts orbits of S_r on
  maps fixed by a permutation of the other points), and every partial sum is
  at least 1, so `r and … or …` is safe.
- No rooted trees and no series: 55 bytes under the main record.

**Limits**

- Exact for every n, but the recursion visits all 2ⁿ⁻¹ compositions of n, so
  each term takes more than twice as long as the one before: here a(19)
  arrives after about 12 s (7 reference seconds) and a(20) after about 29 s,
  so the bar is 20 terms. The main record's series reach the 800-term bar.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 200 | first entry |

**Python 3, 20 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 145 | first entry: Burnside over the cycle types, counting the maps that commute with a permutation |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001372), CC BY-SA 4.0.
