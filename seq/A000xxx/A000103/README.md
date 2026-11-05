# A000103

> Number of n-node triangulations of sphere in which every node has degree >= 4.
> — [OEIS A000103](https://oeis.org/A000103)

Offset 4: 0, 0, 1, 1, 2, 5, 12, 34, 130, 525, 2472, 12400, 65619, 357504, …

There is no formula. The known terms come from plantri, which generates the
triangulations one by one, so a short program has to enumerate too: it walks
through every triangulation with n vertices and counts those without a vertex
of degree 3.

### Python 3 — 427 bytes

```python
R=lambda a,b,c:{(a,b):c,(b,c):a,(c,a):b}
def l(s,D,L):
 for a,b in D:
  for _ in D:D+=[(b,a)][b in L:];L+=b,;b=F[(a,b)[::s]]
 return*map(L.index,L),
n=3
while 1:
 n+=1;Q=[G:={}];S={N:=0}
 for i in range(2,n):G|=R(n,i-1,i)|R(1,i+1,i)
 for F in Q:
  if{c:=min(l(s,[d],[])for s in(1,-1)for d in F)}-S:S|={c};N+=c[3]>0;Q+=[{k:F[k]for k in F if{*k}^{u,v}}|R(x,u,y)|R(x,y,v)for u,v in F if(u<v)>((x:=F[u,v],y:=F[v,u])in F)]
 print(N)
```

**How it works**

- **Maps as dicts.** A triangulation is a dict from each directed edge (a, b)
  to the third vertex c of the face on its left, so following `F[a,b]` from
  neighbour to neighbour goes once round a. `R(a,b,c)` is the three entries
  of the face (a, b, c).
- **A seed for each n.** Vertices 1 and n are joined to everything and
  2 … n − 1 form a path: faces (n, i − 1, i) and (1, i + 1, i) for
  i = 2 … n − 1. For n = 4 that is K4.
- **Flips.** An edge uv with faces (u, v, x) and (v, u, y) can be swapped for
  xy, with faces (x, u, y) and (x, y, v), when x and y are not already
  neighbours. The new dict is F without (u, v) and (v, u), plus the two new
  faces. `u<v` takes each edge once. **Wagner's theorem** (1936): any two
  triangulations of the sphere with the same number of vertices are joined by
  a chain of flips. So the walk over `Q` from the seed reaches every class.
  Each dict popped from `Q` is reduced to a canonical code `c`, and only a
  code not in `S` yet gets its flips pushed.
- **Canonical code.** `l(s,[d],[])` walks the map from the directed edge
  d = (u, v): `D` is a queue of (vertex, neighbour to start from), seeded with
  d. Each vertex is walked round from its start, `L` records every neighbour
  met, and a neighbour not yet in `L` joins the queue with the current vertex
  as its start. With `s = -1` the step is `F[b,a]` instead of `F[a,b]`, which
  walks round the other way: the mirror image. The code is `L` with every
  vertex replaced by the position of its first occurrence, so it does not
  depend on the labels. `c` is the least code over every directed edge and
  both orientations.
- **Walk lengths.** The inner loop runs over the growing queue, `len(D)`
  steps. After t steps round a vertex, the t neighbours met are in `L`, and
  `D` has one entry for each vertex in `L` plus the seed, so at least t + 1:
  the walk never stops before it is back at its start. Every walk covers the
  whole rotation, then wraps round a little.
- **The code gives back the map.** The step counts follow from the code: each
  first occurrence adds one queue entry. The first walk is u's, starting from
  v = `L[0]`. v's walk comes next and starts at u, so u shows up as the first
  entry of the second walk. Every later walk belongs to the next new vertex,
  starting from the vertex in whose walk it first appeared. So the code
  determines every vertex's neighbours in cyclic order, that is, the whole
  map up to relabelling. Two triangulations get the same least code exactly
  when one maps onto the other, possibly mirrored.
- **Whitney's theorem**: a 3-connected planar graph has only one embedding in
  the sphere, up to mirror image, and every triangulation with at least
  4 vertices is 3-connected. So classes of maps (in either orientation) are
  classes of graphs, which is what the sequence counts.
- **Minimum degree for free.** A code starts with the walk round u:
  0, 1, …, deg(u) − 1, then 0 again. A smaller degree puts the second 0
  earlier, so the least code starts at a vertex of minimum degree. That
  degree is at least 3, and `c[3]` is 0 exactly when it is 3. `N+=c[3]>0`
  counts the rest. K4 and the bipyramid (n = 4, 5) have degree-3 vertices,
  so the first two terms come out 0 with no special case.
- **Small things.** `S` starts as `{0}`, which no code equals, and that line
  also sets `N` to 0. `{c:=…}-S` is shorter than `(c:=…)not in S`. The flips
  are one list comprehension, with a filtered dict comprehension in place of
  a copy plus `del`. `return*map(L.index,L),` returns a tuple without
  parentheses.

**Limits**

- The walk visits every triangulation with n vertices ([A000109](../A000109/):
  233 for n = 10, 1249 for n = 11, 7595 for n = 12), and each code costs
  4(3n − 6) walks of about n² steps. a(4) … a(10) (7 terms) print in about
  25 s, and a(11) = 34 after about 4 minutes. The bar is 7 terms in 60 s.
- `D+=[(b,a)][b in L:]` is 6 bytes shorter than `b in L or D.append((b,a))`
  but builds a list at every step: 7 terms take about 25 s instead of 17 s.
- Walking only the triangulations with minimum degree 4 would be far
  faster, but it does not work: in the bipyramid over an (n − 2)-cycle every
  edge has an end of degree 4, so no flip keeps the minimum degree at 4 and
  that class is not connected by flips from there.
- Correct for every n given the two theorems above. Nothing is hard-coded.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 427 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000103), CC BY-SA 4.0.
