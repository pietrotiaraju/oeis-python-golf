# A001334

> Number of n-step self-avoiding walks on hexagonal [ =triangular ] lattice.
> — [OEIS A001334](https://oeis.org/A001334)

Offset 0: 1, 6, 30, 138, 618, 2730, 11946, 51882, 224130, 964134, …

The walks live on the triangular lattice (OEIS calls it hexagonal: every
point has 6 neighbours), start at the origin and never visit a point twice.

### Python 3 — 108 bytes

```python
f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for d in(1,B,~B)for w in{p+d,p-d}-S)
B=1
while[print(+f(0,{0}))]:B+=1
```

**How it works**

- The triangular lattice is Z² with the six steps ±(1, 0), ±(0, 1),
  ±(1, 1): the three vectors u = (1, 0), v = (0, 1) and u + v make the
  triangles. A point (i, j) is stored as the integer i + jB, so the six
  steps are ±1, ±B and ±(B + 1), written `for d in(1,B,~B)for w in{p+d,p-d}-S`
  (`~B` is −(B + 1)); the set difference keeps the unvisited neighbours w
  with no walrus or `if`.
- B = n + 1. A point (i, j) is |i| + |j| steps from the origin when i and
  j have opposite signs, and max(|i|, |j|) steps otherwise. If i + jB = 0
  with j ≠ 0, then i = −jB has the opposite sign and |i| ≥ B, so the point
  is at least B + 1 steps away. Two points of an n-step walk are at most
  n < B steps apart, so the encoding is injective on every walk and `S`, a
  set of integers, is an exact visited set.
- `f(p,S)` counts the ways to finish a walk that stands at p with visited
  set S. The walk is complete when it has n + 1 points (`B<=len(S)`) and
  then scores `True`; otherwise it sums over the unvisited neighbours.
- The loop prints a(n) and then raises B. a(0) needs no step; `+` prints
  its `True` as 1.

**Golf notes**

- The six steps written out with a walrus test,
  `for d in(1,-1,B,-B,B+1,~B)if{w:=p+d}-S`, cost 3 bytes more; the
  [A000765](../../A000xxx/A000765/) form, differences `a-b` of `U=0,1,B`,
  costs 9 more.
- `len(S)//B or` in place of `B<=len(S)or` returns the integer 1 and
  saves the `+`, but is one byte longer itself: the same size.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator), so Python's default recursion limit
  of 1000 would only matter near n = 490; memory stays tiny (one set per
  level).
- The time grows like the number of walks (about 4.15ⁿ): a(10) comes after
  about 10 s and a(11) after about 40 s here (about 23 reference seconds).
- The b-file has 41 terms (a(0) to a(40), from Jensen's enumeration); the
  bar is 12 terms (up to a(11)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 108 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001334), CC BY-SA 4.0.
