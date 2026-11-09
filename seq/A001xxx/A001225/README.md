# A001225

> Number of consistent arcs in a tournament with n nodes.
> — [OEIS A001225](https://oeis.org/A001225)

Offset 2: 1, 2, 5, 7, 11, 14, 20, 24, 30, 35, 44, 50, …

### Python 3 — 344 bytes

```python
def g(I,k,D=[1]):
 F=[0];C=[*map(int.bit_count,P:=range(1<<k))];r=P[:k]
 for S in P[1:]:F+=max(F[S^1<<v]+C[I[v]&S]for v in r if S>>v&1),
 if k>D[0]:print(F[-1]);D[0]=k
 [g([I[u]|(~X>>u&1)<<k for u in r]+[X],k+1)for X in P if all(F[R]+F[~R]+sum(C[I[v]&~R]for v in r if R>>v&1)+C[X^R]<=F[-1]+C[X]<=s+~k*~k//4for R in P)]
s=0
while 1:g([0],1);s+=1
```

**How it works**

- For a tournament T, let f(T) be the largest number of arcs that agree
  with one linear order of its vertices (a largest acyclic set of arcs).
  The OEIS formula a(n) = C(n,2) − A003141(n), with A003141(n) the largest
  number of arcs some n-node tournament needs reversed to become
  transitive, says a(n) = min f(T) over all n-node tournaments: this is
  what the program computes.
- f by a subset DP: `I[v]` is the in-neighbour mask of v and `C` a popcount
  table. Putting v last in S gains its in-arcs from S, so
  F[S] = max over v in S of F[S∖v] + |I[v] ∩ S|, and F[full] = f(T).
- **Symmetry breaking.** Relabel any T along a best order: then the identity
  order 0, 1, …, n−1 is optimal, and f(T) = fw(T), the number of arcs i → j
  with i < j. So a(n) = min fw(T) over labelled tournaments whose identity
  order is optimal ("identity-optimal"). A prefix of an optimal order is
  optimal for the prefix: the arcs between the prefix and the rest count the
  same whatever the inner orders, so a better inner order would give a
  better whole order. Hence every prefix 0, …, k−1 of an identity-optimal T
  is identity-optimal, and the search builds T one vertex at a time
  (`g(I,k)` holds k vertices), keeping only identity-optimal tournaments.
- **Exact extension test.** The new vertex z = k has in-set X. In an order
  of the k+1 vertices let R be the set after z and ~R the set before it.
  The best such order scores F[~R] + F[R] + e(~R→R) for the old vertices
  (e counts arcs from ~R into R: `sum(C[I[v]&~R]…)`) plus |X∖R| + |R∖X|
  = |X △ R| for the arcs at z (`C[X^R]`). R = ∅ is the identity order,
  F[full] + |X|. So the extension is identity-optimal exactly when no R
  scores more than R = ∅: the left half of the chained comparison inside
  `all`. `F[~R]` is F of the complement (index −R−1).
- **Pruning.** With R = all old vertices the test says |X| ≥ k/2, so adding
  the (k+1)-th vertex raises fw by at least ⌈k/2⌉ = ⌊(k+1)²/4⌋ − ⌊k²/4⌋: the
  excess fw − ⌊k²/4⌋ never decreases from a prefix to the whole. Round
  s = 0, 1, 2, … searches depth-first the tree of identity-optimal
  tournaments of excess ≤ s, which by this monotonicity contains every such
  tournament with all its prefixes: the right half of the chain,
  fw ≤ s + ⌊(k+1)²/4⌋ (`~k*~k` is (k+1)²). R = ∅ comes first in `all`, so
  this bound is tested before anything else.
- **Output.** The first time any round reaches k vertices, it prints that
  tournament's `F[-1]` and stores k in `D[0]`. That value is a(k): round
  s−1 visited every identity-optimal k-vertex tournament of excess ≤ s−1
  and found none, so the least excess is s; the tournament found has excess
  ≤ s, hence exactly s, and its F[-1] = fw = f = ⌊k²/4⌋ + s = a(k). Depths
  are reached in order 2, 3, … (the one-vertex root is not printed).
- Every round ends, since the least excess grows without bound (it is of
  order n^(3/2), a known result on ranking tournaments). Correctness does
  not need this: a round that never ended would search an infinite tree with
  finite branching depth-first, which still reaches every depth.

**Golf**

- One search for all n, printing at each new depth, is 16 bytes shorter
  than a search per n that returns `k==n or any(…)` (360 bytes).
- The popcount table `C=[*map(int.bit_count,P:=range(1<<k))]` replaces five
  `.bit_count()` calls (−14 bytes, and faster); `r=P[:k]` is `range(k)`.
- One `all` with the chain `term<=F[-1]+C[X]<=bound` does both tests and
  exits early. `bound>=F[-1]+C[X]==max(…)` has the same length but no early
  exit, and missed 10 terms in 60 s. Precomputing the R terms once per node
  is about 2.5 times faster but 26 bytes longer.

**Notes**

- Exact integer arithmetic; the only facts used are the two lemmas above
  (prefix of an optimal order, |X| ≥ k/2), both proved here.
- The terms agree with a brute force over all labelled tournaments for
  n ≤ 6 and with the OEIS data for n ≤ 11.
- a(2), …, a(11) arrive in about 20 s here (about 8 reference seconds);
  a(11) comes right after a(10), both at excess 5. a(12) = 44 has excess 8
  and needs complete rounds s = 5, 6, 7 first: it did not come within
  several minutes. Memory stays small (recursion depth n).
- The b-file has the 12 known terms (up to a(13)); the bar is 10 terms in
  120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 344 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001225), CC BY-SA 4.0.
