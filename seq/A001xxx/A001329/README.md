# A001329

> Number of nonisomorphic groupoids with n elements.
> — [OEIS A001329](https://oeis.org/A001329)

Offset 0: 1, 1, 10, 3330, 178981952, 2483527537094825, 14325590003318891522275680, …

A groupoid (magma) is a set with one binary operation A × A → A and no
axioms; a(n) counts the operations on n points up to relabelling the points.

### Python 3 — 215 bytes

```python
from math import*
from functools import*
f=cache(lambda r,*L:r and sum(f(k,*sorted(L+(r-k,)))for k in range(r))//r or prod(sum(l*(lcm(i,j)%l<1)for l in L)**gcd(i,j)for i in L for j in L))
n=0
while[print(f(n))]:n+=1
```

**How it works**

- Burnside's lemma: a(n) = (1/n!)·Σ_π |Fix(π)|, where a permutation π of
  the n points fixes an operation ∘ when π(x∘y) = πx∘πy for all x, y.
  Take two cycles of π, of lengths i and j. Their i·j pairs (x, y) fall
  into orbits of length lcm(i, j) under (x, y) ↦ (πx, πy), gcd(i, j) of
  them. On one orbit, ∘ is fixed by its value z at one pair, and z can be
  any point with π^lcm(i,j)(z) = z, that is any point of a cycle whose
  length divides lcm(i, j). So with L the list of cycle lengths of π,
  |Fix(π)| = Π_{i,j∈L} (Σ_{l∈L, l | lcm(i,j)} l)^gcd(i,j), Bower's formula
  in the entry. `l*(lcm(i,j)%l<1)` is l when l divides lcm(i, j) and 0
  otherwise.
- Instead of summing over partitions with weights 1/z_λ, `f` builds π one
  cycle at a time, as in [A000088](../../A000xxx/A000088/): the cycle
  through a fixed point of the r points still free has length r − k for
  each k = 0 … r − 1 with probability 1/r. So
  f(r, L) = (1/r)·Σ_k f(k, L + (r − k)), f(0, L) = |Fix| of cycle type L,
  and a(n) = f(n, ()). a(0) = 1 is the empty product.
- `//r` at every level is exact: f(r, L) is the average, over the
  permutations σ of the r free points, of the number of operations fixed by
  τ×σ, with τ a permutation of type L on the points already used. σ
  commutes with τ, so S_r acts on the operations fixed by τ, and by
  Burnside's lemma the average is its number of orbits, an integer.
- f(r, L) depends only on the multiset L, so `cache` with L kept sorted cuts
  the work to one leaf per partition of n instead of one per composition
  (2^(n−1) of them). `r and …//r or prod(…)` takes the product when r = 0;
  for r ≥ 1 the quotient is at least 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 28 terms (a(0) to a(27)); the bar is the whole b-file in
  60 s. a(27) arrives after about 4 reference seconds.
- `sum(l>>lcm(i,j)%l*l for l in L)` (a shift by at least l bits clears l)
  is the same length; `sum(l for l in L if lcm(i,j)%l<1)` is 2 bytes
  longer, and `import math,functools as F` 3 bytes longer.
- a(n) ~ n^(n²)/n!, so Python's 4300-digit int-to-str limit stops the
  program at a(51) (about 4376 digits), after a(50) (4183 digits).

## First 17 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(16) have to arrive in time.

### Python 3, 17 terms — 174 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or prod(sum(l*(lcm(i,j)%l<1)for l in L)**gcd(i,j)for i in L for j in L)
n=0
while[print(f(n))]:n+=1
```

**How it works**

- The same recursion and fixed-point product as the main record, without
  the cache: the new cycle is appended as it comes, `*L,r-k`, so `f` visits
  every composition of n, 2^(n−1) leaves, each computing the product for its
  cycle type. The order of L does not change the product, and the integer
  argument for `//r` is the same, so it is right for every n.

**Limits**

- a(16) arrives after about 9 reference seconds and a(17) after about 24,
  too close to the limit of 30 for an 18-term bar. Far short of the main bar
  of 28 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 215 | first entry |
| 2026-11-09 | Python 3, 17 terms | 174 | first entry: the recursion without the cache |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001329), CC BY-SA 4.0.
