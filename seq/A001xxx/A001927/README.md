# A001927

> Number of connected partially ordered sets with n labeled points.
> — [OEIS A001927](https://oeis.org/A001927)

Offset 0: 1, 1, 2, 12, 146, 3060, 101642, 5106612, 377403266, 40299722580, 6138497261882, …

No formula is known: the terms come from computer enumerations. A short
program can only list the posets, so it gets a handful of terms.

### Python 3 — 212 bytes

```python
from itertools import*
n=0
while 1:R=range(n);X=range(1<<n);print(sum(0<sum(all((a&s)%a<1>r[j]*(a>>j&1)&~a for a in r for j in R)for s in X)<<n-len({*r})<3for r in product(*[{k|1<<i for k in X}for i in R])));n+=1
```

**What is counted**

A poset on {0, …, n−1} is a quasi-order (a reflexive, transitive relation
≤) that is antisymmetric. It is stored as its rows: r[i] is the bitmask of
the up-set {j : i ≤ j}, so bit i of r[i] is set. In a quasi-order r[i] = r[j]
exactly when i ≤ j ≤ i, so a quasi-order is a poset exactly when its n rows
are distinct. The poset is connected when its comparability graph is. A set
s of points is a union of connected components exactly when every row r[i]
lies inside s or outside it: then every comparable pair is on one side, and
a row never leaves the component of its point.

**How it works**

This is the connected-topology record [A001929](../A001929/) with a test
for distinct rows.

- **Every reflexive relation.** `{k|1<<i for k in X}` is the set of the
  2ⁿ⁻¹ masks that contain i, and `product` runs over all 2^(n(n−1)) choices
  of the n rows.
- **One test per row a, point j and set s.**
  `(a&s)%a<1>r[j]*(a>>j&1)&~a` chains two conditions. `(a&s)%a<1` says that
  a & s is 0 or a (a row is never 0, and a proper part of a is a smaller
  nonzero number), so the row is inside s or outside it.
  `1>r[j]*(a>>j&1)&~a` is transitivity: if j is in the row a, the row of j
  has nothing outside a.
- **Counting.** The inner `sum` counts the s in X that pass for every a and
  j. A relation that is not transitive fails at some pair (a, j) for every
  s, so its count is 0. For a quasi-order the count is 2^c, c the number of
  components. `<<n-len({*r})` shifts it left by the number of repeated rows,
  which is 0 for a poset and makes the count at least 4 otherwise (a repeated
  row needs n ≥ 2, so 2^c ≥ 2). So `0<…<3` keeps exactly the connected
  posets; for n = 0 the only set s = 0 passes once, which counts the empty
  poset, a(0) = 1.

**Speed**

The search visits 2^(n(n−1)) relations, each against 2ⁿ sets: a(5) arrives
after about 50 s here, while a(6) would need a thousand times more. The bar is the
first 6 terms within 120 s.

**Notes**

- Exhaustive search with exact arithmetic: right for every n, only slow.
- Listing the strict relations as sets of pairs, as in
  [A000608](../../A000xxx/A000608/), is 222 bytes:
  `r=range(1<<n);print(sum(sum(all(s>>a&1==s>>b&1for a,b in Q)for s in r)<3for k in r for Q in combinations(permutations(range(n),2),k)if{(a,c)for a,b in Q for x,c in Q if b==x}<={*Q}))`
  (after the same first two lines, inside `while 1:` … `;n+=1`); there two pairs (a, b) and
  (b, a) imply the loop (a, a), which is never in Q, so antisymmetry comes free.
- The OEIS gives the e.g.f. as the logarithm of that of the labeled posets
  [A001035](../A001035/), which are just as hard to count.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 212 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001927), CC BY-SA 4.0.
