# A402396

> Number of tilings of a 3 X 3 X n box using copies of the seven Soma cube
> pieces (any number of each, in any orientation).
> — [OEIS A402396](https://oeis.org/A402396) (draft when added)

Offset 0: 1, 0, 10392, 4412592, 2635098324, 1393412907584, 770197822607052, 417435568848837808, …

### Python 3 — 411 bytes

```python
from itertools import*
Q=[sum(1<<int(str(a),3)for a in s)for k in(3,4)for s in combinations([i for i in range(223)if'3'>max(str(i))],k)if(W:=sum(d for a in s for d in b'\1\nd'if a+d in s))%9==~-k and'1'in str(W)]
e={0:1}
while 1:
 print(e[0])
 for q in range(9):
  d,e=e,{0:0};W=[P>>q for P in Q if P&-P==1<<q]
  for m,c in d.items():
   for k in[m>>1]if m&1 else[(m|v)>>1 for v in W if v&m<1]:e[k]=e.get(k,0)+c
```

**How it works**

- The pieces are not listed. The Soma pieces are the V tricube and the six
  tetracubes that are not boxes, so they are exactly the sets of 3 or 4 cells
  that are connected and do not fill their bounding box (the other connected
  ones are the straight I3 and I4 and the square O).
- A cell of a 3 × 3 × 3 window is the number x + 10y + 100z with digits 0 to
  2, so two cells are neighbours exactly when they differ by 1, 10 or 100
  (no digit goes past 2, so nothing wraps around a row). `b'\1\nd'` is the
  bytes 1, 10, 100.
- For a set s of k cells, `W` adds 1, 10 or 100 for each pair of neighbours,
  so its digits count the pairs in each direction. `W%9` is the digit sum,
  the number of pairs, and k − 1 pairs among k ≤ 4 cells of the cubic grid
  (which has no triangles) means a tree; that also rules out O, which has 4.
  A tree with 2 or 3 pairs is straight only if they all point the same way;
  otherwise some direction has exactly one pair, which is the `'1'` in
  `str(W)`. The filter keeps 688 placements in the window, the 92
  orientations of the seven pieces.
- `int(str(a),3)` reads the digits of a cell in base 3, giving its bit
  x + 3y + 9z, and `Q` holds the placements as 27-bit masks.
- The box is filled cell by cell, x fastest, then y, then layer by layer. A
  state is the set of cells already covered from the current cell on, bit 0
  being the current cell. If that cell is covered (`m&1`), the only move is
  to go on (`m>>1`); otherwise the piece covering it has it as its first
  cell, so it is one of the placements whose lowest bit is the cell's place q
  in the layer (`W`, shifted down by q), and it must not overlap `m`. After
  each cell the mask moves down one bit.
- After n layers, the tilings of the 3 × 3 × n box are the paths that leave
  nothing sticking out of the box, the count of the empty state. `e` always
  starts from `{0:0}`, so `e[0]` exists. Pieces reach at most two layers
  past their first cell, so 27 bits are enough, and Python integers keep
  the counts exact.

**Notes**

- About 90,000 states remain between layers and up to 330,000 inside a
  layer, so every term costs the same, about 6 s on a desktop PC (some 4
  reference seconds). The bar is 7 terms in 60 s: a(6) comes after about 23
  reference seconds, close to the draft's own cell-by-cell program.
- The draft computes its terms with a layer transfer matrix reduced by the 8
  symmetries of the 3 × 3 square (7,134 states), which is much faster but far
  longer. The b-file's n = 14 to 200 come from that matrix, and its first 13
  terms agree with the cell-by-cell count.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 411 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A402396), CC BY-SA 4.0.
