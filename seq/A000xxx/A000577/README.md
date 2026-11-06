# A000577

> Number of triangular polyominoes (or triangular polyforms, or polyiamonds) with n cells (turning over is allowed, holes are allowed, must be connected along edges).
> — [OEIS A000577](https://oeis.org/A000577)

Offset 1: 1, 1, 1, 3, 4, 12, 24, 66, 160, 448, …

### Python 3 — 538 bytes

```python
def c(S):
 H=[]
 for k in range(6):
  for b in(0,1):
   T=[[(y,x)if b else(x,y)for x,y in t]for t in S];a=min(x for t in T for x,y in t);d=min(y for t in T for x,y in t)
   H+=[tuple(sorted(tuple(sorted((x-a,y-d)for x,y in t))for t in T))]
  S=[tuple((-y,x+y)for x,y in t)for t in S]
 return min(H)
L={(((0,0),(0,1),(1,0)),)}
while 1:
 print(len(L));K=set()
 for S in L:
  for t in S:
   for i in range(3):
    a,b,d=t[i],t[(i+1)%3],t[(i+2)%3];u=tuple(sorted((a,b,(a[0]+b[0]-d[0],a[1]+b[1]-d[1]))))
    if u not in S:K.add(c([*S,u]))
 L=K
```

**How it works**

- Represent each equilateral triangle by its three vertices in axial
  triangular-lattice coordinates. Reflecting its opposite vertex across
  an edge with endpoints a,b gives a+b−d, producing the adjacent cell.
- Starting from one cell, adjoin every missing edge-neighbor of every
  current shape. Every connected polyiamond can be constructed this
  way, by adding cells along a spanning tree of its adjacency graph.
- Canonicalization tries the six rotations (x,y)→(−y,x+y), together
  with reflection (x,y)→(y,x). Subtracting the coordinate minima removes
  translations. Sorting vertices and cells gives one key per free shape.
- The set removes duplicate growth histories and all rotations and
  reflections. No hole test is applied, so holes are allowed as required.

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

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000577), CC BY-SA 4.0.
