# A001425

> Number of commutative groupoids with n elements.
> — [OEIS A001425](https://oeis.org/A001425)

Offset 0: 1, 1, 4, 129, 43968, 254429900, 30468670170912, …

A commutative groupoid is a set with a binary operation such that
x∘y = y∘x and no other axiom; a(n) counts them on n points up to
isomorphism (relabelling the points).

### Python 3 — 237 bytes

```python
from math import*
from functools import*
f=cache(lambda r,*L:r and sum(f(k,*sorted(L+(r-k,)))for k in range(r))//r or isqrt(prod(sum(l>>(lcm(i,j)>>(j<0))%l*l for l in L)**gcd(i,j)for i in L for j in L+(-2,))))
n=0
while[print(f(n))]:n+=1
```

**How it works**

- A commutative operation is a map from the unordered pairs {x, y}
  (x = y allowed) to the points. By Burnside's lemma a(n) is the average
  over the permutations π of the number of such maps fixed by π. On an
  orbit of π on unordered pairs of length m, a fixed map is determined by
  its value z at one pair, and z can be any point with π^m(z) = z. With L
  the cycle lengths of π that is S(m) = Σ_{l∈L, l | m} l, written
  `sum(l>>m%l*l for l in L)` (a shift by at least l bits clears l), and
  |Fix(π)| = Π over the orbits of S(m).
- The orbits on unordered pairs come from the orbits on ordered pairs,
  where two cycles of lengths i and j give gcd(i, j) orbits of length
  lcm(i, j) (as in [A001329](../A001329/)). Swapping x and y maps an
  ordered orbit to an ordered orbit. A pair of swapped orbits becomes one
  unordered orbit of the same length, so its two factors S(m) in the
  ordered product are the square of what it needs. Only two kinds of
  ordered orbits are swap-invariant, both inside one cycle of length i:
  the diagonal pairs (x, x), length i, which stay of length i, and, for
  even i, the pairs (x, π^{i/2}x), length i, which give an unordered
  orbit of length i/2. So, with g = gcd(i, 2),

  |Fix(π)|² = Π_{i,j∈L} S(lcm(i, j))^gcd(i, j) · Π_{i∈L} S(i/g)^g,

  and the program takes `isqrt` of the product. The second product is a
  pseudo-cycle j = −2 in the inner loop: `lcm(i,-2)>>1` = lcm(i, 2)/2 =
  i/g and `gcd(i,-2)` = g, while real cycles have j > 0 and no shift.
- The sum over permutations is the cycle-by-cycle recursion of
  A001329: the cycle through the first of the r points still free has
  length r − k with probability 1/r, so f(r, L) = (1/r)·Σ_k f(k, L + (r − k)),
  f(0, L) = |Fix| of cycle type L, a(n) = f(n, ()). `cache` with L sorted
  leaves one leaf per partition of n.
- `//r` is exact at every level: f(r, L) is the average, over the
  permutations σ of the r free points, of the number of operations fixed
  by τσ, with τ of type L on the points already used. τ commutes with
  every such σ, and for a permutation g that normalizes a group N the
  average of |Fix(gσ)| over σ ∈ N is the number of N-orbits that g maps
  to themselves (each such orbit contributes |N| solutions of gσy = y),
  an integer.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 37 terms (a(0) to a(36)); the bar is 30 terms (a(0) to
  a(29)) in 60 s. a(29) comes after about 6 reference seconds, the whole
  b-file after about 45.
- Two separate products, Π_{a<b} over pairs of distinct cycles times a
  factor S(i)^⌊i/2⌋·S(i/g) per cycle (Howroyd's formula in the entry), need
  `enumerate` and cost more than the square root.

## First 17 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(16) have to arrive in time.

### Python 3, 17 terms — 196 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or isqrt(prod(sum(l>>(lcm(i,j)>>(j<0))%l*l for l in L)**gcd(i,j)for i in L for j in L+(-2,)))
n=0
while[print(f(n))]:n+=1
```

**How it works**

- The same recursion, square root and pseudo-cycle −2 as the main record,
  without the cache: the new cycle is appended as it comes, `*L,r-k`, so
  `f` visits every composition of n, 2^(n−1) leaves, each computing the
  product for its cycle type. The order of L does not change the product,
  and the integer argument for `//r` is the same, so it is right for
  every n.

**Limits**

- a(16) arrives after about 22 s here (about 10 reference seconds) and
  a(17) after about 55 s, too close to the limit of 30 for an 18-term bar.
  Far short of the main bar of 30 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 237 | first entry |
| 2026-11-09 | Python 3, 17 terms | 196 | first entry: the recursion without the cache |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001425), CC BY-SA 4.0.
