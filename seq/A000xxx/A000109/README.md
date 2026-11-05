# A000109

> Number of simplicial polyhedra with n vertices; simple planar graphs with n
> vertices and 3n-6 edges; maximal simple planar graphs with n vertices;
> planar triangulations with n vertices; triangulations of the sphere with n
> vertices; 3-connected cubic planar graphs on 2n-4 vertices.
> — [OEIS A000109](https://oeis.org/A000109)

Offset 3: 1, 1, 1, 2, 5, 14, 50, 233, 1249, 7595, 49566, 339722, 2406841, 17490241, 129664753, …

### Python 3 — 495 bytes

```python
R=lambda a,b,c:{(a,b):c,(b,c):a,(c,a):b}
def C(N):
 for s in 1,-1:
  for a,b in N:
   D={a:0};Q=[(a,b,b)];c=[]
   for x,y,z in Q:
    while(z:=N[(x,z)[::s]])!=y:Q+=[(z,x,x)][z in D:];c+=D[x],D.setdefault(z,len(D))
   yield c
T=R(0,1,2)|R(1,0,2);S=[]
while[print(len(S)or 1)]:
 (u,v),w=T.popitem();T|=R(u,v,k:=len(T))|R(v,w,k)|R(w,u,k);S=[];Q=[T]
 for T in Q:
  for u,v in T:
   if(x:=T[u,v],y:=T[v,u])not in T:
    M=T|R(x,u,y)|R(y,v,x);del M[u,v],M[v,u]
    if(k:=min(C(M)))not in S:S+=k,;Q+=M,
```

**How it works**

- A triangulation is a dict that maps each directed edge (a, b) to the third
  vertex c of the face on its left, so following `T[x,z]` from neighbour to
  neighbour goes once round vertex x. `R(a,b,c)` is the three entries of
  the face (a, b, c).
- It starts from the triangle seen as two faces, (0, 1, 2) and (1, 0, 2):
  the one triangulation with 3 vertices. For each new n it pops a face
  (u, v, w) off the last triangulation found and puts a new vertex inside it,
  which gives one triangulation with n vertices. The new vertex is called
  `len(T)` (6n − 13 after the pop), bigger than every label before it.
- From there it walks the flip graph breadth first. A flip takes an edge uv
  with faces (u, v, x) and (v, u, y) and swaps it for xy, with faces
  (x, u, y) and (y, v, x); it is allowed when x and y are not already
  neighbours. **Wagner's theorem** (1936): any two triangulations of the
  sphere with the same number of vertices are joined by a chain of flips, so
  the walk reaches every class.
- Each flip result is reduced to a canonical code `min(C(M))`, and only codes
  not seen before are kept; the number of codes is a(n). The walk only
  starts from flip results, so the seed is counted when a flip turns it back
  into itself. K4 (n = 4) has no allowed flip at all, so the list stays empty
  there and `len(S)or 1` prints its 1.
- `C` labels the vertices from every directed edge (a, b) and in both
  orientations: a gets 0, and the vertices are taken in label order; each
  one is walked round starting just after the neighbour it was reached from
  (b for a), and every neighbour not yet labelled gets the next label. The
  code lists, step by step, the label of the vertex being walked and of the
  neighbour met. `N[z,x]` instead of `N[x,z]` (the `[::s]`) walks the other
  way round, which is the mirror image.
- The code gives back the whole labelled map: each vertex's neighbours in
  order, except the one its walk started from. That one is its parent, the
  vertex in whose walk its label first appears; for a it is b, the only
  vertex outside a's walk whose walk passes through 0. So two triangulations
  get the same minimum code exactly when one maps onto the other, possibly
  reversed.
- **Whitney's theorem**: a 3-connected planar graph has only one embedding
  in the sphere, up to mirror image, and every triangulation with at least
  4 vertices is 3-connected. So isomorphic maps (in either orientation) are
  the same thing as isomorphic graphs, which is what the sequence counts.

**Notes**

- Each new n is a fresh flip walk over all its triangulations, with a
  canonical code for both ends of every edge, so the cost grows with
  a(n)·n². a(3) … a(10) (8 terms) print in about 12 s, a(11) = 1249 after
  about 2 minutes. The bar is 8 terms in 60 s. The b-file goes to n = 80,
  with a(80) ≈ 1.4·10⁷⁹: far past anything that lists the triangulations
  one by one.
- Correct for every n given the two theorems above; nothing is hard-coded.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 495 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000109), CC BY-SA 4.0.
