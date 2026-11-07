# A000421

> Number of isomorphism classes of connected 3-regular (trivalent, cubic) loopless multigraphs of order 2n.
> — [OEIS A000421](https://oeis.org/A000421)

Offset 1: 1, 2, 6, 20, 91, 509, 3608, 31856, 340416, 4269971, …

### Python 3 — 247 bytes

```python
from itertools import*
n=2
while 1:R=range(n);print(len({min(sum(4**(2**p[a]+2**p[b])for a,b in E)for p in permutations(R))for E in combinations_with_replacement(combinations(R,2),n*3//2)if len(dict(E))>n-2and{*map(sum(E,()).count,R)}=={3}}));n+=2
```

**How it works**

- In the code n is the number of vertices, twice the OEIS index, so the loop
  runs n = 2, 4, 6, … . A cubic multigraph on n vertices has 3n/2 edges, and
  `combinations_with_replacement(combinations(R,2),n*3//2)` lists every
  multiset of 3n/2 loopless edges (pairs a < b) exactly once.
- `sum(E,())` is the list of all edge ends; `{*map(….count,R)}=={3}` keeps
  the multisets where every vertex has degree 3.
- `dict(E)` maps each smaller end a to some b > a, so `len(dict(E))>n-2`
  says that every vertex below n − 1 has a neighbour with a larger label.
  Such a graph is connected (climb from any vertex to n − 1), and every
  connected graph has such a labelling: number the vertices in breadth-first
  order from a root, backwards, so the root gets n − 1 and every other vertex
  is adjacent to its parent, which has a larger label. So the kept multisets
  contain at least one labelling of every connected cubic multigraph and no
  disconnected one. This replaces a reachability loop.
- `sum(4**(2**p[a]+2**p[b])for a,b in E)` encodes the graph relabelled by
  the permutation p as one integer: 2^x + 2^y determines the pair {x, y}, and
  in a loopless cubic multigraph no edge has multiplicity above 3, so the
  multiplicities are base-4 digits. The encoding is injective on labelled
  multigraphs, and its minimum over all n! relabellings is the same for
  isomorphic graphs and different for non-isomorphic ones.
- The set of these minima has one element per isomorphism class, and `len`
  counts them.

**Notes**

- The minimum of `sorted(2**p[a]+2**p[b]for a,b in E)`, wrapped in `str(…)`
  for hashing: 250 bytes. The witness the other way round, every vertex above
  0 has a smaller neighbour (`len({b for a,b in E})>n-2`): 256. Marking the
  whole orbit of each new graph in a set, with a reachability loop for
  connectivity, was the earlier 369-byte program.
- Brute force over exact integers, so the program is right for every n.
- n = 6 runs through C(23, 9) = 817190 edge multisets and 720 relabellings
  of each of the kept ones: the three terms take about 2.5 s here. The fourth
  term (n = 8: 3.9·10⁹ multisets) is out of reach.
- The b-file has 20 terms (up to a(20)); the bar is 3 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 597 | first entry |
| 2026-11-06 | Python 3 | 596 | simplify equivalent expressions |
| 2026-11-06 | Python 3 | 573 | keep processed degree entries and check the whole degree vector |
| 2026-11-06 | Python 3 | 369 | enumerate edge multisets and mark their vertex-permutation orbits |
| 2026-11-07 | Python 3 | 247 | minimum base-4 code over relabellings; `dict(E)` as connectivity witness |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000421), CC BY-SA 4.0.
