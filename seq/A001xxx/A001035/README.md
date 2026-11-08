# A001035

> Number of partially ordered sets ("posets") with n labeled elements (or labeled acyclic transitive digraphs).
> — [OEIS A001035](https://oeis.org/A001035)

Offset 0: 1, 1, 3, 19, 219, 4231, 130023, 6129859, 431723379, 44511042511, …

### Python 3 — 168 bytes

```python
from itertools import*
n=0
while[R:=range(n),print(sum(all(r[j]*(a>>j&1)&~a<1for a in r for j in R)for r in product(*[{k&~2**i for k in range(1<<n)}for i in R])))]:n+=1
```

**What is counted**

A poset on {0, …, n−1} is stored as its strict rows: r[i] is the bitmask of
the elements below i, so bit i of r[i] is clear. The relation is transitive
when every j below i has everything below j below i too: j ∈ r[i] ⇒
r[j] ⊆ r[i]. Strict rows plus transitivity already give antisymmetry: a
cycle i < j < i would put i into r[i]. Labeled T0 topologies are the same
objects.

**How it works**

- **Every strict relation.** `{k&~2**i for k in range(1<<n)}` is the set of
  the 2ⁿ⁻¹ masks without bit i (`~2**i` is ~(2**i), since `**` binds tighter
  than unary `~`), and `product` runs over all 2^(n(n−1)) choices of rows.
- **Transitivity in one test.** `r[j]*(a>>j&1)&~a<1` is true when j is not in
  the row a (then r[j] is multiplied by 0) or when r[j] has nothing outside
  a. It is as long as the `a|r[j]*(a>>j&1)==a` of the quasi-order page
  [A000798](../../A000xxx/A000798/), but `<1for` needs no space before `for`.
- n = 0 gives one empty relation, so a(0) = 1.

**Speed**

The search visits 2^(n(n−1)) relations: a(5) needs 2²⁰ of them and arrives
in about 1 s here, while a(6) would need 2³⁰. The bar is the first 6 terms
within 60 s; the b-file has 20 terms.

**Notes**

- Growing the posets one point at a time (the new point m picks its
  down-set and up-set as the two halves of k < 4^m, and the same test keeps
  the transitive ones) reaches a(6) in about 25 s but is 199 bytes:
  `f=lambda s,m:n<=m or sum(f(t,m+1)for k in range(4**m)for t in[[v|(k>>i&1)<<m for i,v in enumerate(s)]+[k>>m]]if all(a|t[j]*(a>>j&1)==a for a in t for j in range(m+1)))`
  / `n=0` / `while[print(+f([],0))]:n+=1`.
- The OEIS relation A000798(n) = Σ S2(n,k)·a(k) (quasi-orders are posets
  of their classes) needs the quasi-orders, which are just as hard.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 168 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001035), CC BY-SA 4.0.
