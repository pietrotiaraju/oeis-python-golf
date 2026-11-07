# A000577

> Number of triangular polyominoes (or triangular polyforms, or polyiamonds) with n cells (turning over is allowed, holes are allowed, must be connected along edges).
> — [OEIS A000577](https://oeis.org/A000577)

Offset 1: 1, 1, 1, 3, 4, 12, 24, 66, 160, 448, …

### Python 3 — 246 bytes

```python
L={((0,1,0),)}
while[print(len(L))]:L={min(tuple(sorted((x-a,t,y-b)[::d]for x,t,y in R))for k in S*6if[R:=[(-y,-t,x+y-t)for x,t,y in R]]for a,_,b in R for d in(1,-1))for S in L for x,t,y in S for k in(1,2,3)if{*S}<(R:={*S,(x-k//2*t,-t,y-k%2*t)})}
```

**How it works**

- **Cells.** With ω = e^(iπ/3) and z = x + yω, the cell `(x,t,y)`,
  t = ±1, is the triangle with vertices z, z − t, z − tω: t = −1 points up,
  t = +1 points down. Its three edge neighbours are the cells
  (z − tω, −t), (z − t, −t) and (z − t(1 + ω), −t), which is
  `(x-k//2*t,-t,y-k%2*t)` for k = 1, 2, 3.
- **Symmetries.** Multiplying by ω (rotation by 60° about the origin) maps
  the cell (z, t) to (ω(z − t), −t), which is `(-y,-t,x+y-t)`. The
  reflection z = x + yω ↦ y + xω keeps t, so it just reverses the tuple
  `(x,t,y)`. Shifting x and y by integers keeps t. These generate all
  symmetries of the triangle tiling.
- **Canonical form.** For each of the 6 rotations of the shape, each cell
  (a, ·, b) taken as the origin and each d = ±1 (reflect or not), the sorted
  tuple of the moved cells is a representative; the least of these 12·n
  tuples is the same for two shapes exactly when a symmetry maps one onto
  the other. The walrus `R:=[…]` rotates `R` in place before each pass.
- **Rotation count.** `for k in S*6` runs 6(n − 1) passes, where S is the
  parent shape: a multiple of 6, so every rotation is reached. `[1]*6` does
  exactly six passes for one more byte.
- **Growth.** Every polyiamond with n ≥ 2 cells has a cell whose removal
  leaves it connected (a leaf of a spanning tree of its cell graph), so
  adding one neighbour to every (n−1)-cell shape in every possible way
  reaches every n-cell shape; the set comprehension removes the repeats.
  `{*S}<(R:={*S,u})` is a proper-subset test, true exactly when the new cell
  u is not already in S, and it leaves the new shape in `R`. Nothing tests
  for holes, so holes are allowed.

**Notes**

- Other versions that print the same terms: `[1]*6` instead of `S*6`:
  247 bytes and about 9 times faster (bar in about 2 s, 12 terms in 60 s);
  the explicit 12-step loop `for k in range(12)` with the reflection
  `(y,x,t)` at k = 6 and cells as `(x,y,t)`: 257 bytes; the recursive
  canonicalization with the least x and y as origin: 331 bytes.
- Exact integer arithmetic, so the program is right for every n (it is an
  exhaustive enumeration).
- The 10 terms of the bar take about 19 s here and the 11th does not come
  within 60 s. The b-file has 52 terms (up to a(52)); the bar is 10 terms in
  60 s.
- The counts are small numbers, far from the 4300-digit int-to-str limit.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 538 | first entry |
| 2026-11-06 | Python 3 | 393 | encode cells by their centers and grow neighbors directly |
| 2026-11-06 | Python 3 | 331 | one coordinate triple per cell and recursive dihedral canonicalization |
| 2026-11-07 | Python 3 | 246 | cells (x, ±1, y): reflection reverses the tuple, inline canonical form over all anchor cells |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000577), CC BY-SA 4.0.
