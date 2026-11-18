# A001931

> Number of fixed 3-dimensional polycubes with n cells; lattice animals in the simple cubic lattice (6 nearest neighbors), face-connected cubes.
> — [OEIS A001931](https://oeis.org/A001931)

Offset 1: 1, 3, 15, 86, 534, 3481, 23502, 162913, 1152870, 8294738, 60494549, 446205905, …

### Python 3 — 164 bytes

```python
def f(n,U,S):
 t=0
 while U:c=U.pop();N={c+1,c-1,c+K,c-K,c+K*K,c-K*K};t+=n<2or f(n-1,U+[d for d in N-S if d>0],S|N)
 return t
K=3
while 1:print(f(K-2,[0],{0}));K+=1
```

**How it works**

- "Fixed" means counted up to translation only (the OEIS comment), so the
  program counts every polycube with n cells once, from its lowest cell:
  the cell with the least z, then the least y, then the least x, placed
  at the origin. Every other cell (x, y, z) then comes after (0, 0, 0) in
  the order (z, y, x).
- This is Redelmeier's algorithm (1981), as in
  [A001168](../A001168/) for the square lattice, with one more axis. A
  cell is the integer x + K·y + K²·z, so "after the origin" is just
  "code > 0", and the six neighbours are c ± 1, c ± K, c ± K².
- `f(n,U,S)` counts the ways to add n more cells. U is the list of untried
  frontier cells, S every cell seen so far (the polycube and its
  neighbours). Each cell c popped from U is added; its new neighbours,
  not seen and allowed, join what is left of U for the next level. A cell
  popped here is never offered again to its later siblings, which is what
  makes each polycube come out exactly once. On the last cell (`n<2`) the
  count is 1 with no recursion.
- K = n + 2 is enough. Every cell the search sees is a neighbour of a
  polycube of at most n − 1 cells that contains the origin, so each of its
  coordinates lies in −(n − 1)…n − 1 = −(K − 3)…K − 3, and two of them
  differ by at most n < K in each coordinate. Equal codes would need
  Δx ≡ 0 (mod K), so Δx = 0, then Δy = 0 and Δz = 0 the same way: no two
  cells share a code. The sign test is right too: for z ≥ 1 the code is at
  least K² − (K − 3)·K − (K − 3) = 2K + 3 > 0, for z = 0 and y ≥ 1 at least
  K − (K − 3) = 3, and z = y = 0 leaves x; the negative cases are the
  mirror image. The main loop counts with K and asks for K − 2 cells,
  starting at K = 3 for the offset n = 1.

**Notes**

- Each term takes about eight times as long as the one before: 10 terms
  (to a(10) = 8294738) in about 10 s here, 11 in about 80 s. The bar is 10
  terms in 60 s. The recursion is only n deep and the memory stays near
  10 MB.
- Integer arithmetic only, so the count is exact for every n; only the
  time limits it. The b-file has the 22 known terms (from the OEIS data).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 164 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001931), CC BY-SA 4.0.
