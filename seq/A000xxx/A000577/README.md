# A000577

> Number of triangular polyominoes (or triangular polyforms, or polyiamonds) with n cells (turning over is allowed, holes are allowed, must be connected along edges).
> — [OEIS A000577](https://oeis.org/A000577)

Offset 1: 1, 1, 1, 3, 4, 12, 24, 66, 160, 448, …

### Python 3 — 331 bytes

```python
def c(S,k=5):
 a,b,t=map(min,zip(*S));T=tuple(sorted((x-a,y-b,t)for x,y,t in S))
 return min(T,tuple(sorted((y,x,t)for x,y,t in T)),k and c([(-y-1,x+y+t,1-t)for x,y,t in S],k-1)or T)
L={((0,0,0),)}
while[print(len(L))]:L={c((*S,u))for S in L for x,y,t in S for a,b in((0,0),(1,0),(0,1))if(u:=(x+a*(2*t-1),y+b*(2*t-1),1-t))not in S}
```

**How it works**

- Encode a cell by `(x,y,t)` in triangular-lattice coordinates. For t=0
  its vertices are (x,y), (x+1,y), (x,y+1); for t=1 they are
  (x+1,y+1), (x+1,y), (x,y+1). This stores one triple per cell.
- Its three edge-neighbors have orientation 1−t and positions
  (x,y), (x+2t−1,y), (x,y+2t−1). Starting from one cell, adjoin
  every missing neighbor. Every edge-connected polyiamond is reachable
  by adding cells along a spanning tree of its adjacency graph.
- A 60-degree rotation sends a cell to `(-y-1,x+y+t,1-t)`;
  reflection swaps x and y and preserves t. `c` recursively tries six
  rotations, with and without reflection at each step. Subtracting the minima
  of x and y and sorting the cell triples removes translations and order.
  The third minimum unpacked into `t` is unused.
- Choosing the least of these twelve exact keys identifies precisely
  rotations, reflections and translations. A set removes duplicate
  growth histories. No hole test is applied, so holes remain allowed.

**Notes**

- Arithmetic and symmetry comparisons are exact. Shapes are connected
  along edges; touching at a vertex alone does not add a neighbor.
- Time and memory grow with the number of shapes. The bar is the first
  ten sizes, not a claim of practical enumeration at arbitrary size.
- The reference file contains 52 published OEIS terms; the verification
  bar is 10 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 538 | first entry |
| 2026-11-06 | Python 3 | 393 | encode cells by their centers and grow neighbors directly |
| 2026-11-06 | Python 3 | 331 | one coordinate triple per cell and recursive dihedral canonicalization |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000577), CC BY-SA 4.0.
