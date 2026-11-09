# A001201

> Number of Steiner triple systems (STS's) on 6n+1 or 6n+3 elements.
> — [OEIS A001201](https://oeis.org/A001201)

Offset 0: 1, 1, 30, 840, 1197504000, 60281712691200, 1348410350618155344199680000

### Python 3 — 195 bytes

```python
f=lambda P:P<{1}or sum(f(P-{(i,j),(i,k),(j,k)})for i,j in[min(P)]for k in range(v)if{(i,k),(j,k)}<P)
v=p=1
while[v%6>3or print(p*f({(i,j)for j in range(v)for i in range(1,j)if i+j-v}))]:p*=v;v+=2
```

**Which orders**

- The title says 6n+1 or 6n+3, but the data (and the comment by Franklin T.
  Adams-Watters) count the systems on v = 3n+1 points for n even and on
  v = 3n points for n odd: v = 1, 3, 7, 9, 13, 15, 19, …, every v ≡ 1 or
  3 (mod 6). The program follows the data. Steiner triple systems are
  labeled: a(2) = 30 is the 7!/168 labelings of the Fano plane.

**How it works**

- A Steiner triple system on the points 0, …, v−1 is a set of blocks
  (3-sets) such that every pair of points lies in exactly one block. So it
  is an exact cover of the set of pairs by triangles.
- `f(P)` counts the ways to cover a set `P` of pairs (i, j), i < j, by
  triangles whose three pairs all lie in `P`. The least pair (i, j) must be
  in exactly one block {i, j, k}; branch on k and remove the block's three
  pairs. Every cover is found once. Since (i, j) is the least pair left,
  a pair (i, k) with k < j or (k, i) with k < i is already covered, so
  the third point always has k > j and the test `{(i,k),(j,k)}<P` over all
  k is exact. An empty `P` has one cover: only the empty set is a proper
  subset of {1}, so `P<{1}` is `True`, worth 1 (a byte under `not P`).
- Symmetry: the blocks through point 0 pair up the other v − 1 points. Any
  two perfect matchings of {1, …, v−1} differ by a permutation that fixes
  0, and that permutation maps the systems containing one matching's blocks
  one to one onto those containing the other's. So all (v−2)!! = 1·3·5⋯(v−2)
  matchings are completed in the same number of ways, and
  a(n) = (v−2)!! × (number of systems containing the blocks {0, x, v−x},
  x = 1, …, (v−1)/2).
- So the search starts from all pairs of 1, …, v−1 except the pairs
  {x, v−x}, i.e. `i+j-v` nonzero; the pairs through 0 are already covered.
  `p` runs through 1·3·5⋯ as v goes over the odd numbers, and is (v−2)!!
  at each v; the orders v ≡ 5 (mod 6) are skipped (`v%6>3`). For v = 1
  and 3 the start set is empty and the count is p = 1.
- For v = 13 the search finds the 115200 completions of the fixed matching,
  and 10395 × 115200 = 1197504000. Of the starting matchings tried, {0, x,
  v−x} and {0, x, x+(v−1)/2} were three times faster than {0, 1, 2},
  {0, 3, 4}, …, because the least-pair order then meets fewer dead ends.

**Notes**

- Exact integer arithmetic; correctness rests only on the symmetry
  argument above.
- a(4) takes about 25 s here; a(5) (v = 15) would need about 446 million
  completions, out of reach. The b-file has 7 terms (up to a(6)); the bar
  is 5 terms in 120 s.
- The recursion is one level (two frames) per block, (v−1)(v−3)/6 deep:
  the default recursion limit is reached only near v = 57.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 195 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001201), CC BY-SA 4.0.
