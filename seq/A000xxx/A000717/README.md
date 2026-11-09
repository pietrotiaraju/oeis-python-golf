# A000717

> Number of graphs with n nodes and floor(n(n-1)/4) edges.
> — [OEIS A000717](https://oeis.org/A000717)

Offset 1: 1, 1, 1, 3, 6, 24, 148, 1646, 34040, 1358852, 106321628, 16006173014, 4525920859198, …

### Python 3 — 214 bytes

```python
from math import*
f=lambda r,*L:r<1or sum(f(r+k,*L,k)*(1+X**-k)**(~k//2)*(1+-~k%2*X**(-k//2))*prod((1+X**lcm(k,l))**gcd(k,l)for l in L)for k in range(-r,0))//r
n=1
while 1:X=1<<n*n;print(f(n)//X**(n*n-n>>2)%X);n+=1
```

**How it works**

- Pólya counting with weights: the graphs on n unlabeled nodes with m edges
  number [x^m] (1/n!)·Σ_π Π_c (1 + x^|c|), the product running over the
  orbits c that the node permutation π has on the C(n, 2) possible edges
  (a graph fixed by π is a union of whole orbits, and an orbit of length
  |c| adds |c| edges).
- The orbits come from the cycles of π: two cycles of lengths a and b give
  gcd(a, b) orbits of length lcm(a, b), and one a-cycle gives ⌊(a−1)/2⌋
  orbits of length a on its own edges, plus one of length a/2 (the
  diameters) when a is even.
- `f` is the cycle-at-a-time recursion of [A000088](../A000088/) with that
  product in place of 2^(number of orbits): the cycle through a fixed free
  point has length k with probability 1/r, the new cycle multiplies in
  `(1+X**-k)**(~k//2)` (its own length-a orbits, a = −k),
  `(1+-~k%2*X**(-k//2))` (the diameter orbit, a factor 1 when a is odd) and
  `(1+X**lcm(k,l))**gcd(k,l)` for every earlier cycle l, and the sum is
  divided by r. Each coefficient of f(r, L) is an orbit count of edge sets
  of a fixed size, so every `//r` is exact (de Bruijn's form of Burnside's
  lemma, applied size by size).
- The polynomial in x is one big integer with x = X = 2^(n²) (Kronecker
  substitution): every coefficient, even before a division, is below
  n·2^C(n,2) < X, so no digit spills into the next. The answer is digit
  m = ⌊n(n−1)/4⌋ = `n*n-n>>2` of f(n) in base X.
- Cycle lengths are negated (`range(-r,0)`, `f(r+k,…)`), as in A000088:
  `~k//2` is ⌊(a−1)/2⌋, `-~k%2` is 1 exactly when a is even, and `lcm` and
  `gcd` ignore signs. `r<1or` returns True (1) at the leaves.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Without a cache the recursion visits all 2^(n−1) compositions of n with
  polynomials of about n⁴/2 bits: 17 terms in about 30 s and no 18th within
  60 s on the PC used. The bar is 13 terms in 60 s; the b-file has 40.

## First six terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(6) have to arrive in time.

### Python 3, 6 terms — 177 bytes

```python
from itertools import*
n=1
while R:=range(n):print(len({min(sum(1<<2**p[a]+2**p[b]for a,b in G)for p in permutations(R))for G in combinations(combinations(R,2),n*n-n>>2)}));n+=1
```

**How it works**

- A labelled graph on the nodes `R` is a set G of edges, pairs a < b from
  `combinations(R,2)`, and `combinations(…,n*n-n>>2)` lists every one with
  ⌊n(n − 1)/4⌋ edges (`n*n-n>>2` is (n² − n) >> 2).
- For a relabelling p, edge {a, b} goes to {p[a], p[b]}, coded as
  2^p[a] + 2^p[b], a number whose binary digits are exactly the two
  endpoints. `sum(1<<…)` sets one bit per edge, so the number determines the
  relabelled edge set.
- So the minimum over all relabellings is the same for two graphs exactly
  when they are isomorphic: the set of minima has one element per
  isomorphism class, and its size is a(n).

**Limits**

- a(6) takes C(15, 7) = 6435 graphs times 720 relabellings.
  The six terms arrive in about 11.3 reference seconds (21.4 s on this PC).
- a(7) would take C(21, 10) = 352 716 graphs times 5040 relabellings,
  about 1.8·10⁹ steps, hours instead of seconds; the main record counts with
  Burnside's lemma over cycle types and reaches thirteen terms.
- Everything is exact and exhaustive, so the program is right for every n;
  it is only slow.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 214 | first entry |

**Python 3, 6 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 177 | first entry: every labelled graph, minimum over relabellings |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000717), CC BY-SA 4.0.
