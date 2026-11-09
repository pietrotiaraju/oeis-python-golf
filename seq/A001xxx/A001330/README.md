# A001330

> Number of n-element algebras with 2 binary operations.
> — [OEIS A001330](https://oeis.org/A001330)

Offset 0: 1, 1, 136, 64573605, 768614338015543296, 740148683083442627372862307855625, …

a(n) counts the structures (A, ∘, ⋆) with two binary operations on an
n-element set A, up to relabelling the elements.

### Python 3 — 175 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or prod(sum(l*(lcm(i,j)%l<1)for l in L)**gcd(i,j)for i in L*2for j in L)
n=0
while[print(f(n))]:n+=1
```

**How it works**

- Burnside's lemma, as for one operation in
  [A001329](../A001329/): a permutation π of the n points with cycle
  lengths L fixes Π_{i,j∈L} (Σ_{l∈L, l | lcm(i,j)} l)^gcd(i,j) single
  operations, since the pairs of an i-cycle and a j-cycle form gcd(i, j)
  orbits of length lcm(i, j), and the value on one pair of an orbit can be
  any point of a cycle whose length divides lcm(i, j). A pair of operations
  is fixed when both are, so |Fix(π)| is the square of that product, the
  formula with exponent 2·gcd(i, j) in the entry. `for i in L*2` runs over
  every cycle twice, which squares the product.
- `f` builds π one cycle at a time: the cycle through a fixed point of the
  r points still free has length r − k for each k = 0 … r − 1 with
  probability 1/r, so f(r, L) = (1/r)·Σ_k f(k, L + (r − k)),
  f(0, L) = |Fix| of cycle type L, and a(n) = f(n, ()) is the average of
  |Fix(π)| over all n! permutations. a(0) = 1 is the empty product.
- `//r` at every level is exact: f(r, L) is the average, over the
  permutations σ of the r free points, of the number of pairs of operations
  fixed by τ×σ, with τ a permutation of type L on the points already used.
  σ commutes with τ, so S_r acts on the pairs fixed by τ, and by Burnside's
  lemma the average is its number of orbits, an integer.
- `r and …//r or prod(…)` takes the product when r = 0; for r ≥ 1 the
  quotient is at least 1. The order of L does not change the product.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The OEIS has no b-file beyond the entry's 8 terms (a(0) to a(7),
  synthesized from the data); the bar is all of them in 60 s, and they
  print at once. Without a cache `f` visits all 2^(n−1) compositions of n.
  The cached form of the A001329 record (`from functools import*`,
  `cache(…)` and `*sorted(L+(r-k,))`) costs 41 bytes more and prints
  a(0) to a(30) in 30 s on the PC used.
- `prod(…)**2` is 1 byte longer than `L*2`.
- a(n) ~ n^(2n²)/n!, so Python's 4300-digit int-to-str limit would stop
  the program at a(38), out of reach without the cache.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 175 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001330), CC BY-SA 4.0.
