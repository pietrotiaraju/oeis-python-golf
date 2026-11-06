# A000577

> Number of triangular polyominoes (or triangular polyforms, or polyiamonds) with n cells (turning over is allowed, holes are allowed, must be connected along edges).
> — [OEIS A000577](https://oeis.org/A000577)

Offset 1: 1, 1, 1, 3, 4, 12, 24, 66, 160, 448, …

### Python 3 — 393 bytes

```python
def c(S):
 H=[]
 for k in range(6):
  for b in(0,1):
   T=[(y,x)if b else(x,y)for x,y in S];a=min(x for x,y in T)//3*3;d=min(y for x,y in T)//3*3
   H+=[tuple(sorted((x-a,y-d)for x,y in T))]
  S=[(-y,x+y)for x,y in S]
 return min(H)
L={((1,1),)}
while 1:
 print(len(L));L={c([*S,u])for S in L for x,y in S for a,b in[(1,1),(-2,1),(1,-2)]for d in[3-2*(x%3)]for u in[(x+a*d,y+b*d)]if u not in S}
```

**How it works**

- Represent each triangle by three times its center in axial triangular-
  lattice coordinates. Its coordinates are both 1 modulo 3 for an upward
  cell and both 2 modulo 3 for a downward cell. The first cell is (1,1).
- An upward cell has neighbors offset by (1,1), (−2,1), and (1,−2).
  A downward cell uses their negatives. `3-2*(x%3)` selects the sign.
  Adjoining each missing neighbor generates every edge-connected shape,
  by the spanning-tree argument for its cell adjacency graph.
- Canonicalization tries six rotations (x,y)→(−y,x+y), together with
  reflection (x,y)→(y,x). Subtracting the coordinate minima rounded down
  to multiples of 3 removes translations while preserving the two cell
  orientations. Sorting the centers gives one key per free shape.
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
| 2026-11-06 | Python 3 | 393 | encode cells by their centers and grow neighbors directly |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000577), CC BY-SA 4.0.
