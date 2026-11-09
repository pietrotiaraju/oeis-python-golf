# A001168

> Number of fixed polyominoes with n cells.
> — [OEIS A001168](https://oeis.org/A001168)

Offset 0: 1, 1, 2, 6, 19, 63, 216, 760, 2725, 9910, 36446, 135268, 505861, …

### Python 3 — 152 bytes

```python
def f(n,U,S):
 t=0
 while U:c=U.pop();N={c+1,c-1,c+K,c-K};t+=n<2or f(n-1,U+[d for d in N-S if d>0],S|N)
 return t
K=2
while 1:print(f(K-2,[0],{0}));K+=1
```

**How it works**

- Redelmeier's algorithm (1981). Every fixed polyomino is counted from its
  lowest cell in the bottom row taken leftmost, placed at the origin; then all
  its other cells (x, y) have y > 0, or y = 0 and x > 0.
- A cell is the integer x + K·y, so that condition is just "code > 0" and the
  four neighbours are c ± 1, c ± K.
- `f(n,U,S)` counts the ways to add n more cells. U is the list of untried
  frontier cells, S every cell seen so far (the polyomino and its
  neighbours). Each cell c popped from U is added; its new neighbours, not
  seen and allowed, join what is left of U for the next level. A cell popped
  here is never offered again to its later siblings, which is what makes each
  polyomino come out exactly once. On the last cell (`n<2`) the count is 1
  with no recursion.
- K = n + 2 is enough. The cells ever seen are neighbours of a polyomino of at
  most n − 1 cells, so their x differ by at most n < K and two of them never
  share a code; the same bound keeps the sign test right. The main loop
  counts with K and asks for K − 2 cells. For K = 2 the call f(0,…) pops the
  origin and returns 1, which is a(0) = 1.

**Notes**

- Each term takes about four times as long as the one before: 15 terms (to
  a(14) = 7204874) in about 14 s here, 16 in about 55 s. The bar is 15 terms
  in 60 s. The recursion is only n deep.
- With a check on the finished polyomino the same search gives
  [A001170](../A001170/) and [A001169](../A001169/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 152 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001168), CC BY-SA 4.0.
