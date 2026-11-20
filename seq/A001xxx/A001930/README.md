# A001930

> Number of topologies, or transitive digraphs with n unlabeled nodes.
> — [OEIS A001930](https://oeis.org/A001930)

Offset 0: 1, 1, 3, 9, 33, 139, 718, 4535, 35979, 363083, 4717687, …

No formula is known: the terms come from computer enumerations. A short
program can only list the quasi-orders and compare them up to isomorphism,
so it gets a handful of terms.

### Python 3 — 234 bytes

```python
from itertools import*
n=0;P=permutations
while 1:R=range(n);print(len({min(sum(1<<p[a]*n+p[b]for a,b in Q)for p in P(R))for k in range(1<<n)for Q in combinations(P(R,2),k)if{(a,c)for a,b in Q for x,c in Q if b==x!=c!=a}<={*Q}}));n+=1
```

**What is counted**

A topology on a finite set is the same thing as a quasi-order (a reflexive,
transitive relation): the open sets are the up-sets, and the relation is
recovered as a ≤ b when b lies in every open set that contains a. The
reflexive pairs (a, a) carry no information, so a quasi-order is a
transitive digraph without loops, which is the other name in the title.
a(n) counts these relations up to relabelling of the n points.

**How it works**

This is the [A000112](../../A000xxx/A000112/) record (unlabeled posets)
with all ordered pairs instead of the pairs a < b.

- **Every relation.** `P(R,2)` lists the n(n−1) ordered pairs (a, b) with
  a ≠ b, and `combinations(…,k)` gives every k-subset Q. `k` runs over
  range(2ⁿ), which covers 0, …, n(n−1) because n(n−1) < 2ⁿ for every n.
- **Transitivity.** The set of pairs (a, c) with (a, b), (b, c) in Q must be
  inside Q. Loops are left out (`!=c!=a`; the middle `x!=c` always holds),
  since (a, b) and (b, a) together are allowed and only give the implied
  (a, a). So the Q that pass are exactly the quasi-orders minus their
  diagonal, each labeled one once.
- **Isomorphism.** `sum(1<<p[a]*n+p[b]…)` writes the relation relabelled by
  the permutation p as an n²-bit number (bit p[a]·n + p[b] for each pair),
  which determines the relabelled relation. Its minimum over all n!
  permutations is the same for isomorphic relations and different for
  non-isomorphic ones, so the size of the set of minima is a(n).
- n = 0: one empty Q and one empty permutation give the single empty
  topology, a(0) = 1.

**Speed**

The search visits 2^(n(n−1)) pair sets: a(5) needs about a million of them
and arrives after about 13 s here; a(6) would need 2³⁰. The bar is the first
6 terms within 120 s.

**Notes**

- Exhaustive search with exact arithmetic: right for every n, only slow.
- Listing the quasi-orders as rows of bits, as on the labeled page
  [A000798](../../A000xxx/A000798/), is faster but the relabelling of bit
  rows costs 21 more bytes than the relabelling of pairs.
- Connected ones are [A001928](../A001928/) (a(n) is their Euler
  transform); T0 topologies are the posets, [A000112](../../A000xxx/A000112/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 234 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001930), CC BY-SA 4.0.
