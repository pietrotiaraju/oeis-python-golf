# A000798

> Number of different quasi-orders (or topologies, or transitive digraphs) with n labeled elements.
> — [OEIS A000798](https://oeis.org/A000798)

Offset 0: 1, 1, 4, 29, 355, 6942, 209527, 9535241, 642779354, 63260289423, 8977053873043, …

### Python 3 — 168 bytes

```python
from itertools import*
n=0
while[R:=range(n),print(sum(all(a|r[j]*(a>>j&1)==a for a in r for j in R)for r in product(*[{k|1<<i for k in range(1<<n)}for i in R])))]:n+=1
```

**What is counted**

A quasi-order (preorder) on {0, …, n−1} is a reflexive transitive relation ≤.
It is stored as its rows: r[i] is the bitmask of the up-set {j : i ≤ j}.
Reflexive means bit i of r[i] is set; transitive means that whenever j is in
r[i], everything above j is above i, i.e. r[j] ⊆ r[i]. Finite topologies are
the same objects (open sets = up-sets), which is why the two counts agree.

**How it works**

- **Every reflexive relation.** For each i, `{k|1<<i for k in range(1<<n)}`
  is the set of the 2ⁿ⁻¹ masks that contain i (the set drops the duplicates
  that `|1<<i` creates), and `product` runs over all 2^(n(n−1)) choices of
  the n rows.
- **Transitivity in one test.** `a|r[j]*(a>>j&1)==a` is true when j is not in
  the row a (then r[j] is multiplied by 0) or when r[j] ⊆ a. Multiplying by
  the bit is a byte shorter than a trailing `if a>>j&1`.
- `sum` of the booleans counts the quasi-orders; n = 0 gives the empty
  product, one empty relation, so a(0) = 1.
- `R:=range(n)` inside the `while` list is shared by both loops over the
  points (1 byte under writing `range(n)` twice).

**Speed**

The search visits 2^(n(n−1)) relations: a(5) needs 2²⁰ of them and arrives
after about 2 s here, but a(6) would need 2³⁰, a thousand times more work.
The bar is the first 6 terms within 60 s.

**Notes**

- Growing the quasi-orders one point at a time (a new point x picks its
  down-set and its up-set, and the same transitivity test filters the 4ⁿ
  choices) reaches a(6) in about 40 s but is 188 bytes:
  `Q=[[]];n=0` / `while[print(len(Q))]:Q=[S for R in Q for k in range(4**n)for S in[[r|(k>>i&1)<<n for i,r in enumerate(R)]+[k>>n|1<<n]]if all(a|b==a for a in S for j,b in enumerate(S)if a>>j&1)];n+=1`.
- Rows as Python sets would make the test `all(r[j]<=a for a in r for j in a)`
  16 bytes shorter, but listing the subsets that contain i costs more than that.
- No formula is known; the OEIS gives a(n) = Σ S2(n,k)·A001035(k) in terms of
  labeled posets, which are just as hard to count.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 168 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000798), CC BY-SA 4.0.
