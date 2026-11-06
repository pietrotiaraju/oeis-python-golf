# A000421

> Number of isomorphism classes of connected 3-regular (trivalent, cubic) loopless multigraphs of order 2n.
> — [OEIS A000421](https://oeis.org/A000421)

Offset 1: 1, 2, 6, 20, 91, 509, 3608, 31856, 340416, 4269971, …

### Python 3 — 369 bytes

```python
from itertools import*
n=2
while 1:
 R=range(n);S=set();c=0
 for E in combinations_with_replacement(combinations(R,2),n*3//2):
  if any(sum(E,()).count(i)!=3for i in R):continue
  V={0}
  for _ in R:V|={b for e in E if V&{*e}for b in e}
  if len(V)==n and E not in S:c+=1;S|={tuple(sorted(tuple(sorted((p[a],p[b])))for a,b in E))for p in permutations(R)}
 print(c);n+=2
```

**How it works**

- In the code n is the vertex count, twice the OEIS index. A
  cubic graph has 3n/2 edges, so the loop uses n=2,4,6,… .
- `combinations(R,2)` lists all possible loopless edges.
  Choosing a multiset of 3n/2 of them permits parallel edges and
  lists every loopless multigraph with that many edges once.
- Concatenating the edge pairs counts each endpoint occurrence.
  Requiring exactly three occurrences of each vertex imposes
  degree 3 at every vertex, including multiplicities.
- Starting at V={0}, add the endpoints of every edge touching V.
  Each round advances at least one step along every reachable path;
  after n rounds V is the component of 0. Keep only len(V)=n.
- E is a tuple of edges in lexicographic order. If it has not
  already been marked in S, count a new isomorphism class.
  Relabel every vertex permutation, sort each edge's two endpoints,
  then sort the edge tuple and insert it in S.
- Every relabeled tuple preserves edge multiplicities. Marking the
  entire orbit ensures exactly one representative of each connected
  cubic multigraph contributes to the answer, regardless of its
  automorphism group size.

**Notes**

- This enumerates edge multisets directly. It stores no sequence
  terms, graph catalogue or conjectural extrapolation.
- On two vertices only three parallel edges are possible. The two
  four-vertex classes are K₄ and a 4-cycle with a pair of opposite
  edges doubled.
- The finite search grows rapidly: at six vertices it considers
  C(23,9)=817190 edge multisets, then rejects the wrong degrees
  and disconnected candidates. Orbit marking adds n! permutations
  for each new class and stores their distinct images.
- The b-file has 20 terms. The unchanged bar is the first 3 terms
  in 10 s, corresponding to graphs with 2,4,6 vertices.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 597 | first entry |
| 2026-11-06 | Python 3 | 596 | simplify equivalent expressions |
| 2026-11-06 | Python 3 | 573 | keep processed degree entries and check the whole degree vector |
| 2026-11-06 | Python 3 | 369 | enumerate edge multisets and mark their vertex-permutation orbits |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000421), CC BY-SA 4.0.
