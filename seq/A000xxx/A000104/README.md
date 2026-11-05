# A000104

> Number of n-celled free polyominoes without holes.
> — [OEIS A000104](https://oeis.org/A000104)

Offset 0: 1, 1, 1, 2, 5, 12, 35, 107, 363, 1248, 4460, 16094, 58937, 217117, 805475, …

### Python 3 — 285 bytes

```python
F=frozenset;L=[()]
while[print(len(L))]:L={F(F(1j**k*(k//4*2*w.real-w)for z in q for w in[z*len(q)-sum(q)])for k in range(8)):q for p in L for z in p or[0]for k in range(4)for q in[(*p,z+1j**k)]if(q[-1]in p)<sum({2*z+d%3+d//3*1j:1-d%2*2for z in q for d in range(9)}.values())}.values()
```

**How it works**

- Cells are Gaussian integers stored as complex numbers, and a polyomino is a
  tuple of cells. `L` holds one polyomino of each class of size n. Each pass
  prints `len(L)` and builds size n + 1: every representative `p` gets each
  neighbour `z+1j**k` of each of its cells `z` in turn.
- Only hole-free polyominoes are kept, and that loses nothing: every hole-free
  polyomino Q with at least 2 cells has a cell c such that Q − c is again a
  hole-free polyomino. Take a leaf block B of the cells' adjacency graph (the
  whole graph if it has no cut cell) and its cut cell v, if any. A cell of B
  other than v is not a cut cell, so removing it keeps Q connected. If none of
  them touched an empty cell, all their neighbours would lie in B; then the
  cell above the highest of them and the cell below the lowest would both have
  to be v, which is impossible. So some such cell c touches the outside, and
  since Q has no holes the outside is a single region, which c joins: Q − c has
  no holes either.
- Holes are counted with the Euler characteristic of the union of the closed
  squares: χ = V − E + F = 1 − (number of holes) for a connected polyomino.
  In doubled coordinates cell z covers the nine points 2z + a + bi with
  a, b ∈ {0, 1, 2}: the middle one stands for the face, the four with a + b odd
  for the edges and the four corners for the vertices. With d = a + 3b, the
  parity of d is that of a + b, so `1-d%2*2` is +1 for faces and vertices and
  −1 for edges. The dict merges the points that neighbouring cells share, and
  the sum of its values is χ. Two cells that touch only at a corner share that
  vertex, so an empty cell closed off except for a diagonal gap counts as a
  hole, as it should (the 7-cell polyomino with a hole).
- `(q[-1]in p)<χ` is a chained comparison: the new cell is not already in `p`,
  and χ ≥ 1, which means χ = 1 since χ ≤ 1. When the new cell is already in
  `p`, χ is that of `p`, 1, and `1<1` is false.
- The dict key names the class. `z*len(q)-sum(q)` is n times the cell's
  position relative to the centroid, which no translation changes and which
  stays in integers. `k//4*2*w.real-w` is −w for k < 4 and the conjugate of w
  for k ≥ 4; multiplied by i^k this gives the four rotations and the four
  reflections. The frozenset of the eight frozensets is the same for two
  copies of a polyomino and different for two polyominoes that are not
  copies.
- The dict comprehension keeps one representative per key, and its `.values()`
  are what the next pass iterates over and counts.
- `L=[()]` starts from the empty polyomino, which gives a(0) = 1; `p or[0]`
  grows it into the single cell. `while[print(…)]` loops forever because
  `[None]` is true.

**Notes**

- Every coordinate stays an integer below n in absolute value, so
  `z*len(q)-sum(q)` stays below 2n² and all the complex arithmetic is exact.
- Every class is grown on its own, and both checks run on every candidate, so
  each term takes about four times as long as the one before: a(0) … a(11)
  print in about 18 s (CPython 3.14), and a(12) takes well over a minute.
  The bar is 12 terms in 60 s. The b-file goes to n = 40 (a(40) ≈ 1.1·10²¹),
  far out of reach of any program that lists the polyominoes one by one.
- `2for` raises a `SyntaxWarning` on stderr, which is ignored.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 285 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000104), CC BY-SA 4.0.
