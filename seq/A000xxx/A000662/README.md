# A000662

> Number of relations with 3 arguments on n nodes.
> — [OEIS A000662](https://oeis.org/A000662)

Offset 1: 2, 136, 22377984, 768614354122719232, …

### Python 3 — 159 bytes

```python
import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<k*k-3*sum(k*d*e//math.lcm(k,d,e)for d in L for e in(*L,k))for k in range(-r,0))//r
n=1
while[print(f(n))]:n+=1
```

**What is counted**

- A ternary relation is any subset of [n]³, counted up to relabelling the
  n nodes. By Burnside's lemma a(n) = (1/n!) Σ_σ 2^T(σ), where T(σ) is the
  number of orbits of σ on the ordered triples. Triples whose coordinates
  lie in cycles of lengths a, b, c form abc/lcm(a, b, c) orbits, the
  formula of Bower in the OEIS entry.

**How it works**

- The recursion of [A000250](../A000250/) and [A000171](../A000171/):
  f(r, L) = (1/r) Σ_k 2^W·f(r − k, L + [k]) over the length k of the cycle
  through one of the r remaining points, where W counts the orbits of
  triples that use the new cycle and earlier ones only. With the new cycle
  in all three places that is k³/k = k²; in two places, 3·k·gcd(k, d) for
  each earlier d; in one place, 3·kde/lcm(k, d, e) for each ordered pair of
  earlier cycles. Since kdk/lcm(k, d, k) = k·gcd(k, d), the middle term is
  the e = k case of the last one:

  W = k² + 3·Σ_{d∈L} Σ_{e∈L+[k]} kde/lcm(k, d, e).

- Cycle lengths are stored negated (`range(-r,0)`, `f(r+k,…)`), which is a
  byte under `range(1,r+1)`. A product of three negative lengths is
  negative and `lcm` ignores signs, so the double sum is negated, hence
  `k*k-3*sum(…)`; the two `for` clauses make it one `sum`.
- `//r` at every level is exact by de Bruijn's lemma, as explained on the
  [A000250](../A000250/) page: each f(r, L) is an orbit count.

**Notes**

- The recursion visits the 2^(n−1) compositions of n: the whole b-file
  (15 terms) takes about 3 s here and 18 terms about 27 s.
- a(25) has about 4680 digits, so Python's 4300-digit int-to-str limit
  would stop the output after 24 terms.
- The bar is the whole b-file, 15 terms, in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 159 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000662), CC BY-SA 4.0.
