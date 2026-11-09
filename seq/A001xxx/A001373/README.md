# A001373

> Number of functional digraphs (digraphs of functions on n nodes where every node has outdegree 1 and loops of length 1 are forbidden).
> — [OEIS A001373](https://oeis.org/A001373)

Offset 0: 1, 0, 1, 2, 6, 13, 40, 100, 291, 797, 2273, 6389, 18264, 51916, 148666, …

That is, maps f from n points to themselves with no fixed point f(x) = x, up
to relabelling.

### Python 3 — 246 bytes

```python
from functools import*
r=[n:=0,1];B=[1]
g=cache(lambda m,k:m<1or k and g(m,k-1)+sum(r[i]*g(m-k*i,k)for i in range(1,m//k+1)))
while[print(B[0])]:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;B=[g(-n,-n)-sum(map(int.__mul__,r[2:],B))]+B
```

**What is counted**

- All mappings up to relabelling ([A001372](../A001372/)) are multisets of
  cycles of rooted trees, with g.f. A(x) = ∏ₖ 1/(1 − T(xᵏ)), T the g.f. of
  rooted trees ([A000081](../../A000xxx/A000081/)). A cycle of length 1 is a
  single rooted tree (its root is the fixed point), and multisets of rooted
  trees have g.f. T(x)/x (a forest plus one new root is a tree). Splitting a
  mapping into its components with a fixed point and the others gives
  A(x) = (T(x)/x)·B(x), so B(x) = (x/T(x))·∏ₖ 1/(1 − T(xᵏ)), the formula
  of the entry (Read; Arndt's PARI program).

**How it works**

- `g(m,k)` is the coefficient of xᵐ in ∏_{j≤k} 1/(1 − T(xʲ)), by
  g(m, k) = g(m, k − 1) + Σᵢ tᵢ·g(m − ki, k), and g(m, m) = A001372(m): the
  program of [A001372](../A001372/), which also explains the tree list `r`
  (`r[i]` = tᵢ, one new tree count per round).
- **The division.** T(x)/x = Σ t(i+1)xⁱ starts with t₁ = 1, so
  b(m) = a(m) − Σᵢ t(i+1)·b(m − i) over i = 1…m. `B` keeps b(m − 1), …, b(0)
  newest first, and `map(int.__mul__,r[2:],B)` pairs t₂ with b(m − 1), t₃ with
  b(m − 2), and so on. When b(m) is computed, `r` already holds t₀ … t(m+1).
- `B=[1]` prints b(0) = 1 (the empty map) before the first round.

**Notes**

- Exact integer arithmetic and exact divisions, so the program is right for
  every n.
- The recursion of `g` is about m deep (see [A001372](../A001372/)), so the
  program stops with a `RecursionError` near a(997), an interpreter limit. The
  whole b-file (509 terms, up to a(508)) prints in about 1 s; the bar is the
  whole b-file in 60 s.
- Putting x/T(x) into the base case `g(m,0)` instead of dividing at the end
  is 5 bytes longer.

## First 20 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(19) have to arrive in time.

### Python 3, 20 terms — 148 bytes

```python
import math
f=lambda r,*L:sum(f(k,*L,r-k)for k in range(r))//r if r else math.prod(sum(j*(i%j<1)for j in L)-1for i in L)
n=0
while[print(f(n))]:n+=1
```

**How it works**

- **Burnside.** Relabelling by a permutation π turns a map f into πfπ⁻¹; it
  keeps f free of fixed points, and the orbits of S_n are the maps up to
  relabelling. So a(n) = (1/n!) Σ_π |{f without fixed points : fπ = πf}|.
- **Maps that commute with π.** If fπ = πf, then f(πⁱx) = πⁱf(x), so f is
  fixed by its value y = f(x) at one point x of each cycle of π, and y may be
  any point on a cycle whose length divides the length of x's cycle: for a
  cycle of length i, Σ j choices over the cycles of π of length j dividing i
  (the [A001372](../A001372/) count). A point πⁱx of this cycle is fixed by f
  exactly when πⁱy = πⁱx, that is, when y = x. So the maps without fixed
  points are those that avoid the one choice y = x on every cycle, and their
  number is the product of (Σ j) − 1 over the cycles:
  `math.prod(sum(j*(i%j<1)for j in L)-1for i in L)`.
- **The sum over permutations.** `f(r,*L)` averages over the permutations of
  r further points given the cycle lengths `L` so far: for each length r − k
  of the cycle through a fixed new point, (r − 1)! of the r! permutations,
  then the remaining k points; at r = 0 it returns the count above. `//r` is
  exact at every level (de Bruijn's form of Burnside's lemma, as on
  [A000273](../../A000xxx/A000273/)).
- A partial sum can be 0 (a cycle of length 1 with nothing else to map to
  leaves no choice: a(1) = 0), so the program uses `… if r else …` rather
  than `r and … or …`.
- No rooted trees, no series and no division: 98 bytes under the main record.

**Limits**

- Exact for every n, but the recursion visits all 2ⁿ⁻¹ compositions of n, so
  each term takes more than twice as long as the one before: here a(19)
  arrives after about 13 s (8 reference seconds) and a(20) after about 27 s,
  so the bar is 20 terms. The main record reaches the whole b-file.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 246 | first entry |

**Python 3, 20 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 148 | first entry: Burnside over the cycle types, maps that commute with a permutation and avoid y = x on every cycle |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001373), CC BY-SA 4.0.
