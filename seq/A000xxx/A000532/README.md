# A000532

> Number of Hamiltonian paths from NW to SW corners in an n X n grid.
> — [OEIS A000532](https://oeis.org/A000532)

Offset 1: 1, 1, 2, 8, 86, 1770, 88418, 8934966, 2087813834, 1013346943033, …

### Python 3 — 125 bytes

```python
f=lambda v,R:sum(f(u,R-{u})for u in{v+1,v-1,v-~n,v+~n}&R)or not R
n=1
while[print(f(-1,{x+x//n for x in range(n*n+1)}))]:n+=1
```

**How it works**

- **The grid.** Cell x = qn + r (row q, column r < n) is stored as
  x + ⌊x/n⌋ = q(n+1) + r, so column n is a gap between rows: the
  neighbours of v are v ± 1 and v ± (n+1) (`v-~n`, `v+~n`), and a step
  can never wrap from the end of one row to the start of the next.
  Neighbours outside the grid are simply not in the set `R`.
- **A tail cell instead of a target.** x = n² adds one more cell, n(n+1)
  (row n, column 0), whose only neighbour is the SW corner (n−1)(n+1). A
  Hamiltonian path of the grid plus that cell that starts at the NW corner
  0 must end at the extra cell, which has a single neighbour, and must
  reach it straight from the SW corner. So these paths are exactly the
  Hamiltonian paths from NW to SW, and the search needs no target test.
- **The search.** `f(v,R)` counts the ways to walk from v through every
  cell of `R` (the cells not yet visited), each step to a neighbour in
  `R`. `{…}&R` lists the unvisited neighbours. When `R` is empty the sum is
  0 and `or not R` returns `True`, one finished path; a dead end with
  cells left returns 0, since `not R` is `False` and the empty sum is 0.
- **The start.** The walk starts at −1, outside the grid: of its
  neighbours −2, 0, n and −n−2 only 0 is a cell (n lies in the gap
  column), so `f(-1,R)` is the count from the corner 0 with every cell
  still to visit, and it is an int even for n = 1.
- **The loop.** `print` sits in the loop condition: it returns `None`, and
  `[None]` is a non-empty list, so the loop never ends (the
  [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: complex cells
  `x%n+x//n*1j` with steps `v±1`, `v±1j`: 130 bytes; complex cells and an
  explicit target test `if R else v==n-1` in place of the tail cell: 136
  bytes; the previous program (a memoized search over bit masks): 232
  bytes.
- An exhaustive search, so the program is right for every n.
- There is no pruning: the search follows every self-avoiding walk from
  the corner. The first five terms print in about 0.6 s here, and a(6) is
  not out after 60 s. The b-file has 21 terms (up to a(21)); the bar is 5
  terms in 60 s.
- The recursion is n² + 2 calls deep, two Python frames per call with the
  generator, so Python's default recursion limit of 1000 would stop it
  around n = 22; the running time stops the program long before.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 232 | first entry |
| 2026-11-07 | Python 3 | 125 | set of unvisited cells, gap column, tail cell after SW |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000532), CC BY-SA 4.0.
