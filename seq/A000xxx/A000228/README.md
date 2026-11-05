# A000228

> Number of hexagonal polyominoes (or hexagonal polyforms, or planar polyhexes) with n cells.
> — [OEIS A000228](https://oeis.org/A000228)

Offset 1: 1, 1, 3, 7, 22, 82, 333, 1448, 6572, 30490, 143552, …

No formula is known; the b-file values (n ≤ 36) come from long computer
enumerations. A short program has to list the shapes one by one, so it
gets ten terms. It is the hexagonal version of
[A000105](../A000105/) (free polyominoes).

### Python 3 — 229 bytes

```python
D=1,1j,1j-1,-1,-1j,1-1j;F=frozenset;S=[F({0})]
while[print(len(S))]:S={F(F(u*w.real+v*w.imag for w in[len(Q)*z-sum(Q)for z in Q])for u in D for v in D if u-v in D):Q for P in S for Q in{P|{z+d}for z in P for d in D}-{P}}.values()
```

**How it works**

- Cells are complex numbers in axial coordinates: x + yi stands for the
  hexagon at x·e₁ + y·e₂, where e₁ and e₂ are unit steps 60° apart. The six
  neighbour steps `D` are then ±1, ±i and ±(i − 1).
- `S` holds one shape of each free polyhex with n cells, so `len(S)` is
  a(n). The next level adds a neighbour `z+d` to every stored shape, and
  `-{P}` drops the cases where `z+d` was already a cell. Every polyhex with
  n + 1 cells is one with n cells plus a neighbour (take away a leaf of a
  spanning tree), and a symmetry maps neighbours to neighbours, so one shape
  per class is enough to reach every class.
- The 12 symmetries of the hexagonal grid are linear maps in these
  coordinates. A linear map L is a symmetry exactly when L(1) = u and
  L(i) = v are two unit steps 60° apart, like 1 and i are, and that holds
  exactly when u − v is a unit step too. So `for u in D for v in D if u-v in D`
  runs over the 12 symmetries (6 rotations, 6 reflections), and
  `u*w.real+v*w.imag` applies one to w.
- The key: w = |Q|·z − Σz is the cell relative to the centre of mass,
  scaled by |Q| so it stays on the grid, and it does not change when the
  shape is translated. The symmetries are linear, so they commute with the
  centering. The key is the set of the 12 transformed cell sets, which is
  the same for congruent shapes and different otherwise.
- The dictionary keeps one shape per key; `.values()` hands the shapes to
  the next round, and `len` works on it directly. `S` starts as a list
  holding the one-cell shape.

**Limits**

- a(n) grows like 5.18ⁿ and the program builds every class at every level:
  a(1)…a(10) print in about 35–50 s, and a(11) = 143 552 would take about
  five times as long again. The bar is 10 terms in 60 s, from a plain
  program (sorted coordinate tuples as canonical forms) that gets there in
  about 50 s.
- The arithmetic is exact: complex numbers hold their parts as floats, and
  every part here is an integer below 2n², far inside the 2⁵³ range where
  floats are exact.

**Notes**

- All 36 pairs u, v (no `if u-v in D`) would be 11 bytes shorter but give
  a wrong key: the map with L(1) = 1, L(i) = −1 + i, say, sends the step
  i − 1 to −2 + i, which is not a step, so the set of 36 images is not the
  same for congruent shapes. In the square grid of A000105 every pair of
  unit steps gives a map that keeps the steps, which is why that trick
  works there.
- Using every cell as an anchor instead of the centre of mass
  (`F(u*(z-y).real+v*(z-y).imag for z in Q)for y in Q`) puts genuine
  polyhexes in the key, so the key set itself can be iterated with
  `for P,*_ in S` and the dictionary goes away: 216 bytes. But it builds n
  times as many sets and reaches only a(9) in 60 s, short of the bar.
- The b-file goes to n = 36, so the check stops at the timeout every time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 229 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000228), CC BY-SA 4.0.
