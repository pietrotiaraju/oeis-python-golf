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

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 214 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000717), CC BY-SA 4.0.
