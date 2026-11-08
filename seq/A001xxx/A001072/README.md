# A001072

> Number of minimally 2-edge-connected non-isomorphic graphs with n nodes.
> — [OEIS A001072](https://oeis.org/A001072)

Offset 3: 1, 1, 3, 4, 11, 23, 63, 159, 459, 1331, 4083, 12750

### Python 3 — 351 bytes

```python
from itertools import*
c=lambda F,s={0}:[s:=s|{v for e in F if{*e}&s for v in e}for _ in R]and s>={*R}
n=3
while[R:=range(n),print(len({min(sum(1<<2**p[x]+2**p[y]for x,y in F)for p in permutations(R))for r in range(n*n)for F in map({(0,1),(0,2)}.union,combinations(combinations(R[1:],2),r))if all(c(F-{e})>all(c(F-{e,f})for f in F)for e in F)}))]:n+=1
```

**What is counted**

A graph is 2-edge-connected when it is connected and has no bridge, and
minimally so when deleting any edge leaves a bridge. For n = 5 the three
graphs are the 5-cycle, K₂,₃ and two triangles sharing a vertex.

**How it works**

- **A degree-2 vertex.** Every minimally 2-edge-connected graph on n ≥ 3
  nodes has a vertex of degree 2. Take an ear decomposition (a cycle, then
  ears: paths or closed paths whose ends are already in the graph); if the
  last ear were a single edge, the earlier ears would still form a
  2-edge-connected graph without it, so the last ear has an inner vertex,
  and that vertex has degree 2. So every class has a labeled copy in which
  node 0 is joined exactly to 1 and 2: the program takes those two edges
  and every subset of the C(n−1,2) edges among 1 … n−1, 2¹⁵ edge sets for
  n = 7 instead of 2²¹.
- **The test.** G is minimally 2-edge-connected exactly when, for every edge
  e, G−e is connected but has a bridge, i.e. some G−e−f is disconnected:
  `all(c(F-{e})>all(c(F-{e,f})for f in F)for e in F)` (True > False; f = e
  just repeats c(F−e)).
- **Connectivity.** `c` grows s from {0} for n rounds inside a list, the
  walrus rebinding the parameter s, and checks `s>={*R}`.
- **Isomorphism.** An edge {a,b} is coded by the bit 2^a + 2^b, which is
  different for every pair; the class of F is named by the least code over
  all n! relabelings, and the set of those codes is counted.

**Speed**

For n = 7 the 32768 edge sets leave 353 labeled graphs and the 11 classes
come after about 35 s here; n = 8 would need 2²¹ edge sets and 8!
relabelings each. The bar is the first 5 terms within 120 s; the b-file is
the OEIS data, 12 terms.

**Notes**

- A recursive connectivity test that stops growing early,
  `c=lambda F,s={0}:s>={*R}or s<(u:=s|{v for e in F if{*e}&s for v in e})and c(F,u)`,
  is 1 byte longer and gets n = 7 in about 22 s.
- The same ear argument bounds the edges: in a minimal graph no ear is a
  single edge (the others would stay 2-edge-connected without it), so each
  of the at most n−3 ears adds k ≥ 1 vertices and k+1 edges, and m ≤ 2n−3.
  Cutting the edge count to that saves only a sixth of the work and costs
  bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 351 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001072), CC BY-SA 4.0.
