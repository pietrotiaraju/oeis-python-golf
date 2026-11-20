# A002014

> Number of symmetric filaments (strip polyominoes) with n square cells.
> — [OEIS A002014](https://oeis.org/A002014)

Offset 0: 1, 1, 1, 2, 2, 5, 5, 12, 12, 27, 28, 64, 67, 147, 158, 348, 373, 799, 879, 1886, 2069, 4335, 4864, 10204, 11432, 23488, 26814, 55179, 62925, 127133, 147414, 298212, 345415, …

### Python 3 — 220 bytes

```python
T=lambda u:min([k>>1^d+k&3for d in u]for k in range(8))
f=lambda t,h,B:t==T(t)and(sum(f(t+[d],q,B|{h+1,h-1,h+1j,h-1j})for d in range(4)if{q:=h+1j**d}-B)if len(t)<n else t==T(t[::-1]))
n=-1
while[print(+f([],0,{0}))]:n+=1
```

**How it works**

- **Symmetric filaments.** A filament (Tilley, Stanton and Cowan, 1970) is
  a polyomino whose cells, joined when they share an edge, form a path: a
  snake polyomino, holes allowed. a(n) counts, up to rotation and
  reflection, those with a symmetry other than the identity. The title's
  "strip polyominoes" is the older name; a separate brute force over
  canonical cell sets agrees with the data up to n = 11 under this
  reading, and the program agrees with the b-file as far as it runs.
- **Walks.** Trace a snake with n ≥ 2 cells from one end: a walk of
  n − 1 unit steps, kept as the list `t` of directions d = 0…3 (the step
  is 1j**d; cells are complex numbers and `h` is the head). Each snake is
  traced by exactly two walks, one from each end, and a walk traces a
  snake exactly when every new cell q is free and touches no cell but the
  head. The set `B` turns this into the one test `{q}-B`: it holds the
  first cell and the four neighbours of every cell before the head, so
  each step adds the neighbours of the old head.
- **One walk per class.** The symmetries of the square act on directions;
  `k>>1^d+k&3`, that is (k >> 1) xor ((d + k) mod 4), runs through all
  eight of them for k = 0…7. Read from the other end, a walk is reversed
  and every step turned around (d + 2, itself one of the eight maps). So a
  free snake is an orbit of walks under the 16 maps t ↦ g(t) and
  t ↦ g(reversed t), and the program counts each orbit by its
  lexicographically least walk. `T(u)` is the least of the eight images
  of `u`.
- **Pruning.** The eight maps act letter by letter, so once a prefix is
  larger than one of its images, so is every walk that extends it.
  `t==T(t)` is checked at every node, which keeps about one walk in
  eight (and only walks starting with direction 0).
- **Small n.** `n` counts steps and starts at −1; while len(t) ≥ n the
  empty walk is already a leaf, so the first two lines are a(0) = a(1) = 1
  (no cells, one cell). `+` prints True as 1.
- **Symmetric classes.** A symmetry g ≠ 1 of a snake with n ≥ 2 cells maps
  its two walks to each other or to themselves. If g fixes a walk letter
  by letter, it fixes every direction the walk uses; a symmetry other
  than 1 fixes at most one direction and its opposite, and a walk using
  only those is a straight bar, which a half turn also maps to its own
  reversal. So a snake is symmetric exactly when its walk t equals one of
  its eight reversed images. For the least walk of a class (`t==T(t)`
  along the way) that means `t==T(t[::-1])` at full length: this one
  comparison is the only change from [A002013](../A002013/), which has
  `t<=T(t[::-1])`. For n ≤ 1 the empty walk passes, matching
  a(0) = a(1) = 1.

**Notes**

- Exact arithmetic: the cells are complex numbers whose parts are integers
  of size at most n, far inside the 2⁵³ range where floats are exact, and
  1j**d for d < 4 is computed by multiplication, so it is exactly ±1 or
  ±1j; only equality and set membership are used. With exact integer
  counting, the program is right for every n by the argument above.
- All classes are still searched, so the time is that of A002013: 18
  terms (n = 0 to 17) take about 30 s on a slow PC, and the bar is
  18 terms in 60 s. The b-file goes to n = 33.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 220 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002014), CC BY-SA 4.0.
