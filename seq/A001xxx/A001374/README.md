# A001374

> Number of relational systems on n nodes. Also number of directed 3-multigraphs with loops on n nodes.
> — [OEIS A001374](https://oeis.org/A001374)

Offset 1: 4, 136, 44224, 179228736, 9383939974144, 6558936236286040064, …

A structure gives each ordered pair (x, y) of nodes, loops included, one of
four values (two binary relations, or an edge multiplicity 0 … 3), counted up
to relabelling the nodes.

### Python 3 — 173 bytes

```python
import math,functools
f=functools.cache(lambda r,*L:r<1or sum(f(r-k,*sorted((*L,k)))<<2*k+4*sum(map(math.gcd,L,[k]*n))for k in range(1,r+1))//r)
n=1
while[print(+f(n))]:n+=1
```

The binary-relation program of [A000595](../../A000xxx/A000595/) with four
values per pair instead of two: every exponent doubles.

**What is counted**

- By Burnside's lemma, a(n) = (1/n!) Σ_π 4^c(π), where c(π) is the number of
  cycles of π on the n² ordered pairs: a structure fixed by π is constant on
  each cycle.
- Pairs (x, y) with x in a cycle of length l and y in one of length m form
  lm pairs in orbits of length lcm(l, m), so gcd(l, m) cycles. Summing over
  ordered pairs of cycles, c(π) = Σᵢ lᵢ + 2·Σ_{i<j} gcd(lᵢ, lⱼ): the formula of
  the entry's PARI program (Andrew Howroyd).

**How it works**

- `f(r,*L)` averages the weight over the permutations of r further points,
  given the cycle lengths `L` already chosen. For each k = 1 … r, exactly
  (r − 1)! of the r! permutations put a fixed new point on a cycle of length
  k, so the average is (1/r)·Σₖ (average over the other r − k points). Adding
  that cycle multiplies the weight by 4^(k + 2·Σ_{l∈L} gcd(k, l)), the shift
  `<<2*k+4*sum(…)`.
- `//r` at every level is exact: each partial sum counts orbits of S_r on the
  structures fixed by a permutation of the other points (de Bruijn's form of
  Burnside's lemma, as on [A000273](../../A000xxx/A000273/)).
- Sorting `L` makes the cache see partitions instead of compositions, so the
  number of states grows like the partitions, not like 2ⁿ. `[k]*n` is a list
  long enough for every `L`. `r<1or` returns `True`, which `+` prints as 1.

**Notes**

- Exact for every n.
- The whole b-file (40 terms, up to a(40), 916 digits) takes about 15 s here (9 reference seconds);
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 173 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001374), CC BY-SA 4.0.
