# A000665

> Number of 3-uniform hypergraphs on n unlabeled nodes, or equivalently number of relations with 3 arguments on n nodes.
> — [OEIS A000665](https://oeis.org/A000665)

Offset 0: 1, 1, 1, 2, 5, 34, 2136, 7013320, 1788782616656, 53304527811667897248, …

### Python 3 — 188 bytes

```python
from math import*
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<k*(k+3)//6+1-sum(sum(k*d*e//lcm(k,d,e)for e in(*L,k))+gcd(k+d,2*k)for d in L)//2for k in range(-r,0))//r
n=0
while[print(+f(n))]:n+=1
```

**What is counted**

- Sets of 3-element subsets of n nodes up to relabelling: by Burnside's
  lemma a(n) = (1/n!) Σ_σ 2^T(σ), where T(σ) is the number of orbits of σ
  on the C(n, 3) triples.

**How it works**

- The recursion of [A000250](../A000250/): f(r, L) = (1/r) Σ_k 2^W·f(r − k,
  L + [k]), where W counts the orbits of triples that meet the new cycle
  (length k) and otherwise only earlier cycles L. They are of four kinds:
  - all three points in the new cycle: ⌈(k − 1)(k − 2)/6⌉ orbits;
  - one point in each of k and two different earlier cycles d, e:
    kde/lcm(k, d, e);
  - two points in one cycle and one in the other, for k and an earlier d:
    t(k, d) + t(d, k), where t(c, d) = ⌊(c − 1)/2⌋·gcd(c, d) +
    [c even]·gcd(c/2, d). The pairs {x, x + j} of a c-cycle form orbits of
    size c, except the diameters j = c/2 with orbits of size c/2, and an
    orbit of size s next to a d-cycle gives gcd(s, d) orbits.
- With g = gcd(k, d), t(k, d) + t(d, k) = ((k + d − 2)·g + g·[v₂(k) ≠
  v₂(d)])/2 (the PARI formula of the entry). The sum over pairs d < e is
  half the sum over ordered pairs minus the d = e terms kd²/lcm(k, d) =
  d·g, and kdk/lcm(k, d, k) = k·g. Everything fits in one ordered sum:

  W = ⌈(k − 1)(k − 2)/6⌉ + ½·Σ_{d∈L} (Σ_{e∈L+[k]} kde/lcm(k, d, e) −
  gcd(k + d, 2k)),

  because 2g − g·[v₂(k) ≠ v₂(d)] = gcd(k + d, 2g) = gcd(k + d, 2k).
- Lengths are stored negated (`range(-r,0)`): then ⌈(k − 1)(k − 2)/6⌉ is
  `k*(k+3)//6+1`, the triple products are negative, and the bracket is
  `-sum(sum(…)+gcd(k+d,2*k)…)//2`. The double sum is even, so the halving
  is exact, and `//r` is exact by de Bruijn's lemma (see A000250).
- `r<1or` returns `True` for n = 0, hence the `+` in the print.

**Notes**

- 2^(n−1) compositions: 19 terms in about 33 s here. a(46) would have
  about 4510 digits, past Python's 4300-digit int-to-str limit.
- The bar is 15 terms in 60 s; the b-file has 29.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 188 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000665), CC BY-SA 4.0.
