# A002013

> Number of filaments with n square cells.
> — [OEIS A002013](https://oeis.org/A002013)

Offset 0: 1, 1, 1, 2, 3, 7, 13, 31, 65, 154, 347, 824, 1905, 4512, 10546, 24935, 58476, 138002, 323894, 763172, 1790585, 4213061, 9878541, 23214728, 54393063, 127687369, 298969219, 701171557, …

### Python 3 — 220 bytes

```python
T=lambda u:min([k>>1^d+k&3for d in u]for k in range(8))
f=lambda t,h,B:t==T(t)and(sum(f(t+[d],q,B|{h+1,h-1,h+1j,h-1j})for d in range(4)if{q:=h+1j**d}-B)if len(t)<n else t<=T(t[::-1]))
n=-1
while[print(+f([],0,{0}))]:n+=1
```

**How it works**

- **Filaments are snakes.** A filament (Tilley, Stanton and Cowan, 1970;
  Ed Pegg Jr's comment: a 2-sided snake polyomino) is a polyomino whose
  cells, joined when they share an edge, form a path. a(n) counts them up
  to rotation and reflection; snakes that wind around a hole count too
  ([A333313](https://oeis.org/A333313) counts the ones without holes). A
  separate brute force over canonical cell sets agrees with the data up
  to n = 11, and the program agrees with the b-file as far as it runs.
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
  lexicographically least walk: at full length `t<=T(t[::-1])` compares it
  with the eight reversed images. `T(u)` is the least of the eight images
  of `u`.
- **Pruning.** The eight maps act letter by letter, so once a prefix is
  larger than one of its images, so is every walk that extends it.
  `t==T(t)` is checked at every node, which keeps about one walk in
  eight (and only walks starting with direction 0).
- **Small n.** `n` counts steps and starts at −1; while len(t) ≥ n the
  empty walk is already a leaf, so the first two lines are a(0) = a(1) = 1
  (no cells, one cell). `+` prints True as 1.

**Notes**

- Exact arithmetic: the cells are complex numbers whose parts are integers
  of size at most n, far inside the 2⁵³ range where floats are exact, and
  1j**d for d < 4 is computed by multiplication, so it is exactly ±1 or
  ±1j; only equality and set membership are used. With exact integer
  counting, the program is right for every n by the argument above.
- The number of walks searched grows about 2.3 times per cell: 18
  terms (n = 0 to 17) take about 30 s on a slow PC, and the bar is
  18 terms in 60 s. The b-file goes to n = 36.
- [A002014](../A002014/) counts the symmetric ones with the same program
  and one changed comparison.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 220 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002013), CC BY-SA 4.0.
