# A000664

> Number of graphs with n edges.
> — [OEIS A000664](https://oeis.org/A000664)

Offset 0: 1, 1, 2, 5, 11, 26, 68, 177, 497, 1476, 4613, 15216, …

### Python 3 — 216 bytes

```python
from math import*
f=lambda r,*L:r<1or sum(f(r-k,*L,k)*(1+B**k)**(~-k//2)*(1+B**(k//2))**(~k&1)*prod((1+B**lcm(k,d))**gcd(k,d)for d in L)%B**-~n for k in range(1,r+1))//r
n=0
while 1:B=9**n**2;print(f(2*n)//B**n);n+=1
```

**What is counted**

- Simple unlabelled graphs with n edges and no isolated vertices. Such a
  graph has at most 2n vertices, and padding with isolated vertices is a
  bijection, so a(n) is the number of graphs on 2n vertices with n edges,
  A008406(2n, n) (Max Alekseyev's formula in the entry): the coefficient of
  xⁿ in (1/N!) Σ_σ Π_orbits (1 + x^|orbit|), N = 2n, over the orbits of σ
  on the C(N, 2) vertex pairs.

**How it works**

- The packed-polynomial recursion of [A000663](../A000663/), with the
  orbits of unordered pairs. Between a new cycle of length k and an earlier
  cycle d there are gcd(k, d) orbits of size lcm(k, d). Inside the new cycle
  the pairs {x, x + j} give ⌊(k − 1)/2⌋ orbits of size k and, when k is
  even, one orbit of the k/2 diameters, of size k/2: the factor
  `(1+B**k)**(~-k//2)*(1+B**(k//2))**(~k&1)` (`~k&1` is 1 for even k).
- x is B = 9^(n²) and polynomials are cut mod B^(n+1). A coefficient of
  r·f(r, L) is at most 2n·C(n(2n − 1), n) < 9^(n²), so the low digits never
  overflow, the carries of the unreduced products only move upwards, and
  `//r` is exact digit by digit by de Bruijn's lemma (see A000663).
  The top digit `f(2*n)//B**n` is a(n).

**Notes**

- 2^(2n−1) compositions of 2n: 10 terms in about 54 s here.
- The bar is 8 terms in 60 s; the b-file has 61.

## First four terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(3) have to arrive in time.

### Python 3, 4 terms — 173 bytes

```python
from itertools import*
for n in count():R=range(2*n);print(len({min(sum(1<<2**p[a]+2**p[b]for a,b in G)for p in permutations(R))for G in combinations(combinations(R,2),n)}))
```

**How it works**

- As in the main record: a graph with n edges and no isolated vertices
  touches at most 2n vertices, and padding with isolated vertices is a
  bijection between classes, so a(n) is the number of graphs on 2n vertices
  with n edges.
- A labelled graph on `R=range(2*n)` is a set G of n edges, pairs a < b from
  `combinations(R,2)`.
- For a relabelling p, edge {a, b} goes to {p[a], p[b]}, coded as
  2^p[a] + 2^p[b], a number whose binary digits are exactly the two
  endpoints. `sum(1<<…)` sets one bit per edge, so the number determines the
  relabelled edge set.
- So the minimum over all relabellings is the same for two graphs exactly
  when they are isomorphic: the set of minima has one element per
  isomorphism class, and its size is a(n).
- At n = 0 the one empty graph on no vertices gives a(0) = 1.

**Limits**

- a(3) takes C(15, 3) = 455 graphs times 720 relabellings.
  The four terms arrive in about 0.4 reference seconds (0.9 s on this PC).
- a(4) would take C(28, 4) = 20 475 graphs times 8! = 40 320 relabellings,
  about 8·10⁸ steps, about half an hour here; the main record counts
  with Burnside's lemma over cycle types and reaches eight terms.
- Everything is exact and exhaustive, so the program is right for every n;
  it is only slow.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-07 | 216 | first entry |

**Python 3, 4 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 173 | first entry: graphs on 2n vertices, minimum over relabellings |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000664), CC BY-SA 4.0.
