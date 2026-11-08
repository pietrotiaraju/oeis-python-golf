# A000944

> Number of polyhedra (or 3-connected simple planar graphs) with n nodes.
> — [OEIS A000944](https://oeis.org/A000944)

Offset 1: 0, 0, 0, 1, 2, 7, 34, 257, 2606, 32300, 440564, 6384634, 96262938, 1496225352, 23833988129, 387591510244, 6415851530241, 107854282197058, 1837856160118250, 31696106245572086, …

### Python 3 — 473 bytes

```python
from itertools import*
Q=lambda C,k:any({1<<a|1<<b for a in p[:3]for b in p[-3:]}<=C for p in P)or k>0and any(Q({d^c*(d&c>c&-c)for d in C}-{0},k-1)for c in C)
n=1
while 1:R=range(n);P=[*permutations(R)];E=[1<<a|1<<b for b in R for a in range(b)];print(len({min(sum(1<<sum((d>>i&1)<<p[i]for i in R)for d in G)for p in P)for m in range(3*n+1>>1,3*n-5)for G in combinations(E,m)if all([s:=~r&r+1]+[s:=s|d for d in G*n if d&r<1<=d&s]and s+r+1>>n for r in E)>Q({*G},n-6)}));n+=1
```

**How it works**

- Brute force over labelled graphs, then isomorphism classes. By Steinitz's
  theorem the polyhedral graphs are the 3-connected planar ones. An edge
  {a, b} is the integer 2ᵃ+2ᵇ; `E` lists all of them, and `G` runs over
  the subsets with ⌈3n/2⌉ ≤ m ≤ 3n−6 edges: a 3-connected graph has
  minimum degree 3, a planar one has m ≤ 3n−6. The empty range for n ≤ 3
  gives the zeros.
- 3-connected (for n ≥ 4): for every pair r = {a, b}, flood-fill from the
  lowest vertex outside r (`~r&r+1`) through the edges that avoid r
  (`d&r<1<=d&s`, n passes); the rest is connected when s+r = 2ⁿ−1, i.e.
  `s+r+1>>n` is 1. If no pair disconnects G, neither does one vertex or
  none.
- Planar: by Hall's theorem (1943) a 3-connected graph other than K₅ that
  is not planar contains a subdivision of K₃,₃, and K₅ already fails the
  edge bound. So `Q` looks for a K₃,₃ minor: K₃,₃ as a subgraph (the 9
  cross edges between the first and last three vertices of some
  permutation, a set inclusion; for n < 6 the two triples overlap and ask
  for loops, so it fails), or after contracting any edge, at most n−6
  times (a minor of K₃,₃'s size needs 6 vertices left). Contracting c =
  {a, b} moves every edge at b to a: `d^c` when `d&c>c&-c`, and c itself
  becomes 0.
- Classes: the set of canonical forms, the least Σ 2^(image of d) over all
  vertex permutations, where `sum((d>>i&1)<<p[i]for i in R)` maps an edge.
  The full permutations `P` also serve `Q` (any 6 ordered vertices are the
  first and last three of some permutation).

**Notes**

- Exact search; correctness rests on Steinitz's and Hall's theorems.
- a(6) = 7 after about 40 s here; a(7) would need about 10⁶ edge sets with
  5040 permutations each, out of reach.
- The b-file has 50 terms; the bar is 6 terms in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 473 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000944), CC BY-SA 4.0.
