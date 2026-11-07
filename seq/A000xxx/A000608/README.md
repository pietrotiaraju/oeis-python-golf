# A000608

> Number of connected partially ordered sets with n unlabeled elements.
> — [OEIS A000608](https://oeis.org/A000608)

Offset 0: 1, 1, 1, 3, 10, 44, 238, 1650, 14512, 163341, 2360719, 43944974, …

The known terms come from computer enumerations of all posets (Brinkmann
and McKay, up to 16 points). A short program can only enumerate and compare
up to isomorphism, so it gets a handful of terms.

### Python 3 — 285 bytes

```python
from itertools import*
n=0;C=combinations
while 1:R=range(n);r=range(1<<n);print(len({min(sum(1<<p[a]*n+p[b]for a,b in P)for p in permutations(R))for k in r for P in C(C(R,2),k)if{(a,c)for a,b in P for x,c in P if b==x}<={*P}and sum(all(s>>a&1==s>>b&1for a,b in P)for s in r)<3}));n+=1
```

**How it works**

This is the [A000112](../A000112/) record (all posets) with a
connectivity filter; see that page for the enumeration.

- **Posets.** Every poset has a linear extension, so it can be written as a
  transitive set P of pairs (a, b) with a < b. `k` runs over `r`, that is
  range(2ⁿ), which is more than the C(n, 2) pairs, and `C(C(R,2),k)` gives
  the k-subsets; the set inclusion tests transitivity.
- **Connectivity.** A subset s of the elements (bit i for element i) with
  no pair (a, b) of P split between s and its complement is a union of
  connected components. There are 2^c of them for a poset with c
  components, so `sum(all(s>>a&1==s>>b&1…)for s in r)<3` holds exactly when
  c ≤ 1 (for n = 0 only s = 0 exists). `r` serves both loops.
- **Isomorphism.** The canonical form is the smallest bit pattern
  Σ 2^(p[a]·n + p[b]) over all n! relabellings p, and the answer is the
  number of distinct canonical forms of connected posets. The empty poset
  and the one-element poset count as connected, as in the OEIS data.

**Notes**

- Exhaustive search with exact arithmetic: right for every n, only slow.
- n = 6 needs 2¹⁵ subsets; a(0) … a(6) print in about 8 s. n = 7 needs 2²¹
  subsets and tens of thousands of posets times 5040 relabellings, many
  minutes. The bar is 7 terms in 60 s.
- The inverse Euler transform of the A000112 counts would give the same
  numbers, but the recurrence costs more bytes than the filter.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 285 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000608), CC BY-SA 4.0.
