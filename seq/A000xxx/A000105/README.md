# A000105

> Number of free polyominoes (or square animals) with n cells.
> — [OEIS A000105](https://oeis.org/A000105)

Offset 0: 1, 1, 1, 2, 5, 12, 35, 108, 369, 1285, 4655, 17073, 63600, …

No formula is known; the b-file values (n ≤ 59) come from long computer
enumerations. A short program has to list the shapes one by one, so it
gets a dozen terms.

### Python 3 — 217 bytes

```python
U=1,1j,-1,-1j;F=frozenset;S={0:F()}
while[print(len(S))]:S={F(F(u*(w-m*w.real)for w in C)for m in(0,2)for u in U):Q for P in S.values()for Q in{P|{z+d}for z in P or{0}for d in U}-{P}if(C:=[len(Q)*z-sum(Q)for z in Q])}
```

**How it works**

- Cells are Gaussian integers (complex numbers), and `U` holds the four
  unit steps, which double as the four rotations.
- `S` maps the key of each free polyomino with n cells to one shape of that
  class, so `len(S)` is a(n). The next level adds a neighbour `z+d` to every
  stored shape; `-{P}` drops the cases where `z+d` was already a cell.
  Every polyomino with n + 1 cells is one with n cells plus a neighbour
  (take away a leaf of a spanning tree), and a symmetry maps neighbours to
  neighbours, so one shape per class is enough to reach every class.
- The key: `C` lists each cell relative to the centre of mass,
  w = |Q|·z − Σz, scaled by |Q| so it stays a Gaussian integer; it does
  not change when the shape is translated. It is computed once per shape,
  in the `if` clause, which is always true because Q is never empty. Each
  of the 8 symmetries is a rotation `u*` of either w or its mirror image
  w − 2·Re w = −w̄ (`m` = 0 or 2). The key is the set of the 8 transformed
  cell sets, which is the same for congruent shapes and different
  otherwise. The symmetries are linear, so they commute with the centering.
- `P or{0}` starts the empty polyomino (a(0) = 1) off at 0: its four
  one-cell children all get the same key. `while[print(…)]` loops forever
  because `[None]` is a non-empty list.

**Limits**

- a(n) grows like 4.06ⁿ and the program builds every class at every level.
  The bar is 13 terms in 60 s, from a plain program (sorted coordinate
  tuples as canonical forms), and it must come within half the timeout on
  the CI runner. The 209-byte version needed 32 s there. On the same local
  machine this version prints a(0)…a(12) in 42 s against 90 s for the
  209-byte one; a(13) = 238 591 would take about four times as long again.
- The arithmetic is exact: complex numbers hold their parts as floats, and
  every part here is an integer below 4n², far inside the 2⁵³ range where
  floats are exact.

**Notes**

- The 209-byte version centred inside the key, `for z in Q for
  w in[len(Q)*z-sum(Q)]`, so every cell was centred again for each of the
  8 symmetries. Moving that into `if(C:=[…])` costs 8 bytes and halves the
  time.
- Applying `u*w.real+v*w.imag` for all 16 pairs u, v in `U` drops the
  mirror loop (8 of the maps squash the shape onto a line, which keeps the
  key complete), but it is slower. Using every cell as an anchor instead of
  the centre of mass (`for w in[z-y])for y in Q`) builds n times as many
  sets and stops at a(11), short of the bar.
- The b-file goes to n = 59, so the check stops at the timeout every time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 209 | first entry |
| 2026-11-08 | Python 3 | 217 | fix: centre each shape once, so the bar comes within half the timeout |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000105), CC BY-SA 4.0.
