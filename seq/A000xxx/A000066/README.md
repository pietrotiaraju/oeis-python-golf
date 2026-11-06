# A000066

> Smallest number of vertices in trivalent graph with girth (shortest cycle) = n.
> — [OEIS A000066](https://oeis.org/A000066)

Offset 3: 4, 6, 10, 14, 24, 30, 58, 70, 112, 126 (every known term; the sequence is marked hard).

### Python 3 — 225 bytes

```python
g=1;v=0
def f(E):L=sum(E,(0,));U={x for x in range(v)if L.count(x)<6};B={i:=min(U|{v})};exec('B|={b for a,b in E if a in B};'*g);return i==v or any(f(E+[(i,j),(j,i)])for j in U-B if~-j in L)
while 1:v+=2;g+=f([])!=0!=print(v)
```

**How it works**

- a(n) is the order of the (3, n)-cage. Cages are strictly monotone in the
  girth (n(3, g) < n(3, g + 1); see Exoo and Jajcay's *Dynamic Cage Survey*),
  so the smallest cubic graph with girth **at least** n has girth exactly n,
  and the next term is larger. The program keeps `g` = n − 2 and an even
  order `v`, asks `f` whether a cubic graph on v vertices with girth ≥ g + 2
  exists, prints v and moves to the next girth when it does, and raises v
  by 2 every round either way.
- `f(E)` grows the graph edge by edge. `E` holds each edge in both
  directions, so `L=sum(E,(0,))` lists every vertex twice per edge; the
  extra leading 0 makes vertex 0 count odd, which `<6` (degree < 3) does
  not mind, and keeps 0 in `L` from the start. `U` is the set of vertices
  below v with degree < 3, and `i` its smallest member (v if `U` is empty:
  then every vertex has degree 3 and `i==v` reports success).
- The new edge from `i` may not close a cycle shorter than g + 2, so its
  far end must lie outside `B`, the ball of radius g around `i`. `exec` runs
  `B|={b for a,b in E if a in B};` g times; the set grows in place, so the
  function's own `B` sees it (this needs CPython 3.12: since PEP 709 a comprehension
  in `exec`'d code is inlined and can read `B`; before, `B` was looked up as a global). It is 6 bytes under the
  `[B:=B|{…}for _ in'.'*g]` walrus loop, at the price of a compile per call.
- Symmetry breaking is what makes it fast: vertices are numbered in the
  order they are first used, so the far end j is either a vertex already in
  use or the next unused number. In use means 1 ≤ j ≤ max + 1, i.e.
  `~-j in L` (j = 0 never qualifies: it is either `i` or already of degree
  3). Without this the search tries every labelling and stalls at girth 6.
- `g+=f([])!=0!=print(v)`: the chain stops at `f([])!=0` when the search
  fails; when it succeeds it prints v and adds `None!=0`, i.e. 1, to g.

**Why it is right**

- Every graph it accepts is simple and cubic on exactly v vertices (edges
  only join vertices of degree < 3 below v; `i` itself is in `B`, and so
  are its neighbours, as g ≥ 1), and every cycle has length ≥ g + 2: look
  at the last edge of the cycle to be added; the rest of the cycle was then
  a path of length ≤ g joining its ends, so the far end was in `B`.
- Conversely, take any connected cubic graph G of girth ≥ g + 2 on v
  vertices and follow the search, mapping the numbered vertices into G.
  The smallest vertex `i` of degree < 3 still misses an edge of G; its other
  end is either already numbered or gets the next number. It is not in `B`:
  the partial graph without that edge sits inside G without it, where the
  two ends are at distance ≥ g + 1. So that branch survives at every step,
  and when no vertex below v is short of degree 3 the copy of G is complete.
  A smallest cubic graph of girth ≥ g + 2 is connected (any component is
  one), so the search succeeds exactly from a(n) on.

**Notes**

- Six terms (4, 6, 10, 14, 24, 30) print in about 6 s, so the bar is 6
  terms in 60 s. The seventh, 58, needs a proof that no cubic graph of
  girth 9 has 46 to 56 vertices (46 is the Moore bound); that took
  Brinkmann, McKay and Saager a large computer search in 1995, far beyond a
  minute of Python.
- The `[B:=B|{…}for _ in'.'*g]` version (231 bytes) runs about five times
  faster but prints no more terms within any reasonable time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 225 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000066), CC BY-SA 4.0.
