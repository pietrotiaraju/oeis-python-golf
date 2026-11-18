# A001929

> Number of connected topologies on n labeled points.
> — [OEIS A001929](https://oeis.org/A001929)

Offset 0: 1, 1, 3, 19, 233, 4851, 158175, 7724333, 550898367, 56536880923, 8267519506789, …

No formula is known: the terms come from computer enumerations. A short
program can only list the topologies, so it gets a handful of terms.

### Python 3 — 199 bytes

```python
from itertools import*
n=0
while 1:R=range(n);X=range(1<<n);print(sum(0<sum(all((a&s)%a<1>r[j]*(a>>j&1)&~a for a in r for j in R)for s in X)<3for r in product(*[{k|1<<i for k in X}for i in R])));n+=1
```

**What is counted**

A topology on {0, …, n−1} is the same thing as a quasi-order (a reflexive,
transitive relation ≤): the open sets are the up-sets, and a ≤ b when b lies
in every open set that contains a. The relation is stored as its rows: r[i]
is the bitmask of the up-set {j : i ≤ j}, so bit i of r[i] is set.
The space is connected when ∅ and the whole set are its only clopen sets. A
set s is open and closed exactly when it is an up-set whose complement is an
up-set too, that is, when every row r[i] lies inside s or outside it (if i
is in s its row must be in s; if i is not, no point above i may be in s).

**How it works**

The search is the one of the labeled quasi-order page
[A000798](../../A000xxx/A000798/), with the transitivity test moved into
the count of clopen sets.

- **Every reflexive relation.** `{k|1<<i for k in X}` is the set of the
  2ⁿ⁻¹ masks that contain i, and `product` runs over all 2^(n(n−1)) choices
  of the n rows.
- **One test per row a, point j and set s.**
  `(a&s)%a<1>r[j]*(a>>j&1)&~a` chains two conditions. `(a&s)%a<1` says that
  a & s is 0 or a (a row is never 0, and a proper part of a is a smaller
  nonzero number), so the row is inside s or outside it.
  `1>r[j]*(a>>j&1)&~a` is transitivity: if j is in the row a, the row of j
  has nothing outside a.
- **Counting.** For each relation, the inner `sum` counts the s in X that
  pass for every a and j. If the relation is not transitive, some pair (a, j)
  fails for every s and the count is 0. If it is a quasi-order, the count is
  the number of clopen sets, 2^c for c connected components. So `0<…<3`
  keeps exactly the connected topologies; for n = 0 the only set s = 0
  passes once, which counts the empty topology, a(0) = 1.

**Speed**

The search visits 2^(n(n−1)) relations, each against 2ⁿ sets: a(5) arrives
after about 50 s here, while a(6) would need a thousand times more. The bar is the
first 6 terms within 120 s.

**Notes**

- Exhaustive search with exact arithmetic: right for every n, only slow.
- Testing transitivity first (`…<3for r in product(…)if all(r[j]*(a>>j&1)&~a<1for a in r for j in R)`)
  skips the 2ⁿ sets for most relations and brings a(5) down to about 2 s,
  for 16 more bytes.
- The OEIS relation a(n) = Σ S2(n,k)·[A001927](../A001927/)(k) (the
  classes of x ≤ y ≤ x shrink to points of a connected poset) and the
  logarithm of the e.g.f. of [A000798](../../A000xxx/A000798/) both need
  terms that are just as hard to get.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 199 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001929), CC BY-SA 4.0.
