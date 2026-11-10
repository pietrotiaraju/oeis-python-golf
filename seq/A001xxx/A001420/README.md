# A001420

> Number of fixed 2-dimensional triangular-celled animals with n cells (n-iamonds, polyiamonds) in the 2-dimensional hexagonal lattice.
> — [OEIS A001420](https://oeis.org/A001420)

Offset 1: 2, 3, 6, 14, 36, 94, 250, 675, 1838, 5053, 14016, 39169, 110194, 311751, 886160, 2529260, 7244862, …

Fixed means counted up to translation only, so the single triangle counts
twice (pointing up and pointing down).

### Python 3 — 153 bytes

```python
def f(n,U,S,t=0):
 while U:c=U.pop();N={c+1,c-1,c+K-c%2*2*K};t+=n<2or f(n-1,U+[*N-S],S|N)
 return t
K=3
while[print(f(K//2,[1,0],{*range(-2*K,2)}))]:K+=2
```

**How it works**

- **The cells.** In each row the triangles alternate up and down, and
  triangle x of row y is the integer c = x + K·y, K odd, so c is even
  exactly when x + y is. Each triangle has three neighbours: the two next
  to it in its row, c ± 1, and the one across its horizontal side, c + K
  for even c and c − K for odd c (`c+K-c%2*2*K`). That is the honeycomb
  graph of the triangular tiling: rows y and y + 1 are linked at the
  triangles with x + y even.
- **Redelmeier's algorithm**, as in [A001168](../A001168/) and
  [A001207](../A001207/): every fixed polyiamond is counted once, from its
  least cell in the order "lowest row, then leftmost". `f(n,U,S)` counts
  the ways to add n more cells; U holds the untried frontier cells, S
  every cell seen so far. A cell popped from U is added, and its unseen
  neighbours join what is left of U for the next level; a popped cell is
  never offered again to its later siblings. On the last cell (`n<2`) the
  count is 1.
- **Two kinds of least cell.** A translation keeps the orientation of
  every triangle, so it moves c by an even amount: each polyiamond has
  exactly one translate whose least cell is 0 (an even cell) or 1 (an odd
  one). Starting with U = `[1,0]` counts both kinds: 0 is popped first,
  and the polyiamonds without it then start from 1, its neighbour.
- **Codes.** The loop runs over odd K = 3, 5, 7, … and counts n = K // 2
  cells, so K = 2n + 1. The cells ever seen form a polyiamond of at most
  n − 1 cells and its neighbours, at most n steps from each other; two
  cells with the same code are K·d apart in x for some d ≠ 0, which takes
  at least K > n steps, so no two cells seen share a code. They are also
  less than n steps from the start, so the code is above 1 exactly on the
  rows above it and to its right in its row, and the cells seen with code
  ≤ 1 (row 0 to the left, row −1) have codes from −2K + 1 to 1: S starts
  with that whole range, so they are never offered as neighbours (cell 1
  is in S as well; it comes in only through the starting U).

**Notes**

- Exact integers, no stored terms; the count rests on Redelmeier's
  algorithm.
- Each term takes about three times as long as the one before: a(18) =
  20818498 comes after about 50 s here. The bar is 18 terms in 120 s (the
  b-file has 75). The recursion is only n deep.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 153 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001420), CC BY-SA 4.0.
