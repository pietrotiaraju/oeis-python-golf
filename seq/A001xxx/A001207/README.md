# A001207

> Number of fixed hexagonal polyominoes with n cells.
> — [OEIS A001207](https://oeis.org/A001207)

Offset 1: 1, 3, 11, 44, 186, 814, 3652, 16689, 77359, 362671, 1716033, 8182213, 39267086, …

### Python 3 — 154 bytes

```python
def f(n,U,S,t=0):
 while U:c=U.pop();N={c+1,c-1,c+K,c-K,c-~K,c+~K};t+=n<2or f(n-1,U+[*N-S],S|N)
 return t
K=1
while[print(f(K,[0],{*range(-2*K,1)}))]:K+=1
```

**How it works**

- Redelmeier's algorithm (1981), as in [A001168](../A001168/), on the
  hexagonal lattice. Skewed, the hexagons are the cells (x, y) of the
  plane grid, each one adjacent to (x±1, y), (x, y±1), (x+1, y+1) and
  (x−1, y−1). A cell is the integer x + K·y, so the six neighbours are
  c ± 1, c ± K and c ± (K+1), written `c-~K` and `c+~K`.
- Every fixed polyhex is counted from its least cell in the order "lowest
  row, then leftmost", placed at the origin: its other cells have code
  > 0. `f(n,U,S)` counts the ways to add n more cells; U holds the untried
  frontier cells, S every cell seen so far. A cell popped from U is added,
  and its unseen neighbours join what is left of U for the next level; a
  cell popped here is never offered again to its later siblings, so each
  polyhex comes out exactly once. On the last cell (`n<2`) the count is 1.
- K = n is enough. The cells ever seen are a polyhex of at most n − 1 cells
  and its neighbours, so any two of them are at most n steps apart. Two
  cells with the same code differ by (−K·d, d) with d ≠ 0, whose x and y
  steps have opposite signs: on this lattice that is |K·d| + |d| ≥ n + 1
  steps. So no two cells seen share a code. They are also at most n − 1
  steps from the origin, so |x| < K: the code is positive exactly on the
  rows above the origin and right of it in its row, and the cells seen
  with code ≤ 0 (row 0 left of the origin, row −1) all have codes from
  −2K + 1 to 0.
- Instead of testing `d>0`, S starts with every code from −2K to 0, so
  those cells are never offered: `U+[*N-S]` is 17 bytes shorter than
  `U+[d for d in N-S if d>0]`, and the range costs 13. Counting the
  codes with K = n, and calling `f(K,…)`, saves the `-1` of `f(K-1,…)`;
  the counter `t=0` as a default argument saves a line, and
  `while[print(…)]:` is a byte under `while 1:print(…);`.

**Notes**

- Each term takes about five times as long as the one before: 12 terms (to
  a(12) = 8182213) in about 15 s here, 13 in about 70 s. The bar is 12
  terms in 60 s. The recursion is only n deep.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 154 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001207), CC BY-SA 4.0.
