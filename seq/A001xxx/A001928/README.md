# A001928

> Number of connected topologies with n unlabeled nodes.
> — [OEIS A001928](https://oeis.org/A001928)

Offset 0: 1, 1, 2, 6, 21, 94, 512, 3485, 29515, 314474, 4255727, …

No formula is known: the terms come from computer enumerations. A short
program can only list the topologies and compare them up to isomorphism,
so it gets a handful of terms.

### Python 3 — 283 bytes

```python
from itertools import*
n=0
while 1:R=range(n);X=range(1<<n);print(len({min(sum((r[i]>>j&1)<<p[i]*n+p[j]for i in R for j in R)for p in permutations(R))for r in product(*[{k|1<<i for k in X}for i in R])if 0<sum(all((a&s)%a<1>r[j]*(a>>j&1)&~a for a in r for j in R)for s in X)<3}));n+=1
```

**What is counted**

A topology on a finite set is the same thing as a quasi-order (a reflexive,
transitive relation ≤): the open sets are the up-sets, and a ≤ b when b lies
in every open set that contains a. The relation is stored as its rows: r[i]
is the bitmask of the up-set {j : i ≤ j}, so bit i of r[i] is set. The
space is connected when ∅ and the whole set are its only clopen sets, and a
set s is open and closed exactly when every row r[i] lies inside s or
outside it. a(n) counts connected topologies up to relabelling of the points.

**How it works**

The filter is the labeled record [A001929](../A001929/); the relabelling is
the one of the unlabeled pages [A000112](../../A000xxx/A000112/) and
[A001930](../A001930/).

- **Every reflexive relation.** `{k|1<<i for k in X}` is the set of the
  2ⁿ⁻¹ masks that contain i, and `product` runs over all 2^(n(n−1)) choices
  of the n rows.
- **Connected topologies.** `(a&s)%a<1>r[j]*(a>>j&1)&~a` chains two tests
  for a row a, a point j and a set s: a & s is 0 or a (a row is never 0, and
  a proper part of a is a smaller nonzero number), and transitivity, the row
  of j has nothing outside a when j is in a. A relation that is not
  transitive fails at some (a, j) for every s, so the count of passing s is
  0; a quasi-order passes for its 2^c clopen sets, c the number of
  components. `0<…<3` keeps the connected ones, and the empty topology for
  n = 0, where only s = 0 exists.
- **Isomorphism.** `sum((r[i]>>j&1)<<p[i]*n+p[j]…)` writes the relation
  relabelled by the permutation p as an n²-bit number (bit p[i]·n + p[j]
  for each i ≤ j), which determines the relabelled relation. Its minimum
  over all n! permutations is the same for isomorphic topologies and
  different for non-isomorphic ones, so the size of the set of minima is
  a(n).

**Speed**

The search visits 2^(n(n−1)) relations, each against 2ⁿ sets: a(5) arrives
after about 60 s here, while a(6) would need a thousand times more. The bar is the
first 6 terms within 120 s.

**Notes**

- Exhaustive search with exact arithmetic: right for every n, only slow.
- Sets of pairs, as in [A001930](../A001930/), relabel more cheaply, but
  their connectivity test costs more: 290 bytes.
- The OEIS gives a(n) as the inverse Euler transform of A001930 (a topology
  is a multiset of connected ones); that needs the A001930 terms, which are
  just as hard.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 283 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001928), CC BY-SA 4.0.
