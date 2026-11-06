# A000109

> Number of simplicial polyhedra with n vertices; simple planar graphs with n
> vertices and 3n-6 edges; maximal simple planar graphs with n vertices;
> planar triangulations with n vertices; triangulations of the sphere with n
> vertices; 3-connected cubic planar graphs on 2n-4 vertices.
> — [OEIS A000109](https://oeis.org/A000109)

Offset 3: 1, 1, 1, 2, 5, 14, 50, 233, 1249, 7595, 49566, 339722, 2406841, 17490241, 129664753, …

### Python 3 — 415 bytes

```python
R=lambda a,b,c:{(a,b):c,(b,c):a,(c,a):b}
def l(s,D,L):
 for a,b in D:
  for _ in D:D+=[(b,a)][b in L:];L+=b,;b=F[(a,b)[::s]]
 return*map(L.index,L),
n,=S=1,
while[print(len(S))]:
 n+=1;Q=[G:={}];S={*G}
 for i in range(n):G|=R(n,i-1,i)|R(-1,i+1,i)
 for F in Q:Q+=[{k:F[k]for k in F if{*k}^{u,v}}|R(x,u,y)|R(x,y,v)for u,v in F if(u<v)>((x:=F[u,v],y:=F[v,u])in F)]*(S<(S:=S|{min(l(s,[d],[])for s in(1,-1)for d in F)}))
```

The same flip walk as [A000103](../A000103/), which counts the triangulations
with minimum degree 4; here every class found is counted.

**How it works**

- **Maps as dicts.** A triangulation is a dict from each directed edge (a, b)
  to the third vertex c of the face on its left, so following `F[a,b]` from
  neighbour to neighbour goes once round a. `R(a,b,c)` is the three entries
  of the face (a, b, c).
- **A seed for each n.** In the loop `n` is the number of vertices minus 2.
  The vertices are −1, 0, …, n: −1 … n − 1 is a path with a fan from n
  (faces (n, i − 1, i)) and 0 … n a path with a fan from −1
  (faces (−1, i + 1, i)), for i = 0 … n − 1. The polygon −1, 0, …, n is
  triangulated from n on one side and from −1 on the other. For n = 2 that
  is K4.
- **Flips.** An edge uv with faces (u, v, x) and (v, u, y) can be swapped for
  xy, with faces (x, u, y) and (x, y, v), when x and y are not already
  neighbours. The new dict is F without (u, v) and (v, u), plus the two new
  faces. `u<v` takes each edge once. **Wagner's theorem** (1936): any two
  triangulations of the sphere with the same number of vertices are joined by
  a chain of flips. So the walk over `Q` from the seed reaches every class.
- **New classes only.** Each dict taken from `Q` is reduced to a canonical
  code, and `S<(S:=S|{code})` is true exactly when the code was not in `S`
  yet. Its flips are pushed only then (`[…]*True`); for a class already seen
  the list is multiplied by `False` and nothing is pushed. a(n) is `len(S)`,
  printed by the loop header before the next n starts. `S={*G}` is an empty
  set, as G is still empty at that point.
- **Canonical code.** `l(s,[d],[])` walks the map from the directed edge
  d = (u, v): `D` is a queue of (vertex, neighbour to start from), seeded with
  d. Each vertex is walked round from its start, `L` records every neighbour
  met, and a neighbour not yet in `L` joins the queue with the current vertex
  as its start. With `s = -1` the step is `F[b,a]` instead of `F[a,b]`, which
  walks round the other way: the mirror image. The code is `L` with every
  vertex replaced by the position of its first occurrence, so it does not
  depend on the labels. The least code over every directed edge and both
  orientations is the canonical one.
- **Walk lengths.** The inner loop runs over the growing queue, `len(D)`
  steps. After t steps round a vertex, the t neighbours met are in `L`, and
  `D` has one entry for each vertex in `L` plus the seed, so at least t + 1:
  the walk never stops before it is back at its start. Every walk covers the
  whole rotation, then wraps round a little.
- **The code gives back the map.** The step counts follow from the code: each
  first occurrence adds one queue entry. The first walk is u's, starting from
  v = `L[0]`. v's walk comes next and starts at u. Every later walk belongs to
  the next new vertex, starting from the vertex in whose walk it first
  appeared. So the code determines every vertex's neighbours in cyclic order,
  that is, the whole map up to relabelling. Two triangulations get the same
  least code exactly when one maps onto the other, possibly mirrored.
- **Whitney's theorem**: a 3-connected planar graph has only one embedding in
  the sphere, up to mirror image, and every triangulation with at least
  4 vertices is 3-connected. So classes of maps (in either orientation) are
  classes of graphs, which is what the sequence counts.
- **n = 3.** The one triangulation with 3 vertices is the triangle seen as two
  faces, where every flip would make a loop. `n,=S=1,` sets `n` to 1 and `S`
  to the tuple (1,), so the first pass of the loop header prints a(3) = 1
  before the walks start at 4 vertices.

**Notes**

- Each new n is a fresh flip walk over all its triangulations. Every dict in
  `Q` costs 4(3n − 6) walks of about n² steps for its code, and every class
  pushes about 3n dicts. a(3) … a(10) (8 terms) print in about 27 s, a(11) =
  1249 after about 3½ minutes. The bar is 8 terms in 60 s. The b-file goes to
  n = 80, with a(80) ≈ 1.4·10⁷⁹: far past anything that lists the
  triangulations one by one.
- Without `(u<v)>(…)`, written `if(x:=F[u,v],y:=F[v,u])not in F`, it would be
  4 bytes shorter, but every flip would be pushed twice: 8 terms take about
  50 s instead of 27 s, too close to the bar.
- Correct for every n given the two theorems above; nothing is hard-coded
  except the a(3) = 1 explained above.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 495 | first entry |
| 2026-11-05 | Python 3 | 415 | flip walk of A000103 from a fresh seed for each n, loop header prints a(3) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000109), CC BY-SA 4.0.
