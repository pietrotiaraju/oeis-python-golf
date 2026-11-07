# A000988

> Number of one-sided polyominoes with n cells.
> — [OEIS A000988](https://oeis.org/A000988)

Offset 0: 1, 1, 1, 2, 7, 18, 60, 196, 704, 2500, 9189, 33896, 126759, 476270, 1802312, 6849777, 26152418, 100203194, 385221143, 1485200848, …

Polyominoes counted up to translation and rotation, but not reflection:
a shape and its mirror image count twice unless they can be turned into
each other (the 7 tetrominoes of Tetris). No formula is known; the b-file
(n ≤ 59) comes from long computer enumerations (Toshihiro Shirakawa and
John Mason, building on the fixed-polyomino counts of A001168). This is
[A000105](../A000105/) (free polyominoes) without the mirror.

### Python 3 — 174 bytes

```python
U=1,1j,-1,-1j;F=frozenset;S=[F()]
while[print(len(S))]:S={F(F(u*(len(Q)*z-sum(Q))for z in Q)for u in U):Q for P in S for Q in{P|{z+d}for z in P or{0}for d in U}-{P}}.values()
```

**How it works**

- Cells are Gaussian integers (complex numbers), and `U` holds the four
  unit steps, which double as the four rotations.
- `S` holds one shape of each one-sided polyomino with n cells, so
  `len(S)` is a(n). The next level adds a neighbour `z+d` to every stored
  shape; `-{P}` drops the cases where `z+d` was already a cell. Every
  polyomino with n + 1 cells is one with n cells plus a neighbour (take
  away a leaf of a spanning tree), and a rotation maps neighbours to
  neighbours, so one shape per class is enough to reach every class.
- The key: |Q|·z − Σz is the cell relative to the centre of mass, scaled
  by |Q| so it stays a Gaussian integer, and it does not change when the
  shape is translated. The key is the set of the 4 rotated copies `u*…`,
  which is the same for shapes that differ by a translation and a
  rotation, and different otherwise. Rotations are linear, so they commute
  with the centering.
- The dictionary keeps one shape per key, and `.values()` hands the shapes
  to the next round (`len` works on it directly), so `S` can start as the
  list `[F()]` holding the empty polyomino. `P or{0}` starts it off at 0:
  its four one-cell children all get the same key.

**Limits**

- a(n) grows like 4.06ⁿ and the program builds every class at every level:
  a(0)…a(11) print in about 17 s and a(12) in about 80 s; a(13) would take
  about four times as long again. The bar is 12 terms in 60 s, from a
  plain program (sorted coordinate tuples as canonical forms) that prints
  a(11) in about 12 s and a(12) just inside 60 s.
- The arithmetic is exact: complex numbers hold their parts as floats, and
  every part here is an integer below 4n², far inside the 2⁵³ range where
  floats are exact.

**Notes**

- Dropping the mirror loop of A000105 makes the key cheaper (4 maps
  instead of 8), but there are about twice as many classes to store and
  grow, so it is slower than A000105 at the same n.
- Anchoring the key at every cell instead of the centre of mass
  (`F(F(u*(z-y)for z in Q)for u in U for y in Q)` over `for P,*_ in S`, as
  in the A000105 notes) is 5 bytes shorter but builds n times as many sets
  and misses the bar.
- The b-file goes to n = 59, so the check stops at the timeout every time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 174 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000988), CC BY-SA 4.0.
