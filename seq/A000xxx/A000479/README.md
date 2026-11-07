# A000479

> Number of 1-factorizations of K_{n,n}.
> — [OEIS A000479](https://oeis.org/A000479)

Offset 0: 1, 1, 1, 2, 24, 1344, 1128960, 12198297600, 2697818265354240, 15224734061278915461120, …

A 1-factorization of the complete bipartite graph K_{n,n} splits its n²
edges into n perfect matchings. A perfect matching is a permutation p
(left vertex i to right vertex p(i)), and two matchings share no edge
exactly when p(i) ≠ q(i) for every i. So a(n) counts the sets of n
pairwise "compatible" permutations, which are the rows of a Latin square in
some order: a(n) = L(n)/n!, with L(n) the number of Latin squares.

### Python 3 — 167 bytes

```python
from itertools import*
f=lambda Q,k:k<1or sum(f([q for q in Q if all(map(int.__ne__,p,q))>(q<p)],k-1)for p in Q)
n=0
while[print(+f([*permutations(range(n))],n))]:n+=1
```

**How it works**

- `f(Q,k)` counts the k-element sets of pairwise compatible permutations
  taken from the list Q. It picks the smallest member p of the set, and
  recurses on the members of Q that are compatible with p and come after
  it in lexicographic order, so every set is counted once, in increasing
  order.
- `all(map(int.__ne__,p,q))>(q<p)` is "compatible and q > p": `True >
  False` holds only when the rows differ in every place and q < p is
  false (a compatible q is never equal to p for n ≥ 1). It is 2 bytes
  under `q>p and all(…)`.
- `k<1or` ends a branch with a complete set. At n = 0 the top call itself
  returns `True` (the empty factorization of the empty graph), so the
  print uses `+` to show 1.
- f does not depend on n, so it is defined once, outside the loop, and
  the list of permutations is passed in directly.

**Notes**

- The previous record, 231 bytes, ran a cached exact cover over edge
  bitmasks. Counting ordered rows and dividing by n!
  (`f(P:=[…],n)//len(P)`) is 170 bytes and visits n! times as many
  leaves.
- Exact enumeration, so the program is right for every n.
- a(0)–a(5) take about 0.4 s here; a(6) = 1128960 means as many leaves
  and had not finished after 5 minutes. The b-file has 12 terms (up to
  a(11)); the bar is 6 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 259 | first entry |
| 2026-11-06 | Python 3 | 231 | cache the exact-cover lambda and inline the least-edge test |
| 2026-11-07 | Python 3 | 167 | count sets of compatible permutations in increasing order |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000479), CC BY-SA 4.0.
