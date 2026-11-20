# A002010

> Number of rooted planar maps with 2n trivalent vertices and a root vertex of valence 8.
> — [OEIS A002010](https://oeis.org/A002010)

Offset 0: 14, 560, 11200, 197568, 3378944, 57573888, 986442752, 17048894464, …

### Python 3 — 137 bytes

```python
L=[q:=1,4,32];k=3
while 1:k+=3;L+=432*(k*k-1)*L[-2]//(k+6)//(k+9),;*R,x,y=L;print(y-10*x+18*R[-1]+6*q-10*(q:=sum(v*R.pop()for v in R*1)))
```

**How it works**

- **Maps counted.** Rooted planar maps (loops and multiple edges allowed:
  that is what the data count) whose root vertex has valence k and whose
  m other vertices are all trivalent; call the number T(k, m). Here
  a(n) = T(8, 2n).
- **Root-edge decomposition** (Tutte's). If the root edge is a loop, it
  splits the other k − 2 darts at the root vertex into i on one side and
  k − 2 − i on the other, and the two sides are independent maps of the
  same kind, with root valences i and k − 2 − i (an empty side is the
  one-vertex map, T(0, 0) = 1). Otherwise its other end is trivalent, and
  contracting the edge gives a root vertex of valence k + 1; splitting the
  root vertex's first two darts off again inverts this, so these maps are
  in bijection with all maps of root valence k + 1 and m − 1 trivalent
  vertices. With M_k(t) = Σ_m T(k, m)·t^m:
  M_k = t·M_(k+1) + Σ_(i+j=k−2) M_i·M_j, and M_0 = 1. Every term on the
  right has one edge fewer, so this alone fixes all T(k, m) by induction
  on the number of edges; run that way it reproduces the closed form of
  c(n) below for n ≤ 8 and this page's formula for n ≤ 6.
- **Seed.** Erasing a root vertex of valence 2 leaves a rooted cubic map
  (its two darts give the two directions of the root edge), so
  M_2 = C(t²), where C(x) = Σ c(n)xⁿ is the generating function of
  [A002005](../A002005/) (c(0) = 1 is the single loop). The recursion
  gives M_1 = t·C(t²), M_3 = (C − 1)/t and M_4 = (C − 1)/t² − 2C, and then
  each M_(k+1) from M_k.
- **Valence 8.** M_8 = (M_7 − 2M_0M_5 − 2M_1M_4 − 2M_2M_3)/t gives
  a(n) = c(n+3) − 10c(n+2) + 18c(n+1) − 10Q(n+1) + 6Q(n),
  Q(n) = Σ_(i=0..n) c(i)c(n−i), the entry's formula.
- **c(n)**, the number of rooted cubic maps with 2n vertices, is
  2^(2n+1)·(3n)!!/((n+2)!·n!!), the classical closed form (see
  [A002005](../A002005/)). It gives
  (n+1)(n+2)·c(n) = 48(3n−2)(3n−4)·c(n−2), and with k = 3n − 3 this is
  c(n) = 432(k²−1)·c(n−2)/((k+6)(k+9)). The numerator equals
  (k+6)(k+9)·c(n), so the two floor divisions are exact
  (⌊⌊x/p⌋/q⌋ = ⌊x/(pq)⌋).
- **The list.** `L` starts at c(0), c(1), c(2) and each pass appends the
  next c(m) from `L[-2]` = c(m − 2), with k = 3m − 3 (the `for c in L`
  walk of [A002007](../A002007/) would line up only with a two-term
  start, one term too short here). After the append `L` ends at
  c(n + 3).
- **Two convolutions, one sum per pass.** `*R,x,y=L` leaves
  R = c(0…n+1), and `sum(v*R.pop()for v in R*1)` is Q(n+1) (a copy of R
  walked from the front against pops from the back). `q` keeps the
  previous pass's value, Q(n): the print reads `18*R[-1]` and `6*q`
  before `(q:=…)` empties R and stores Q(n+1). `L=[q:=1,4,32]` sets
  Q(0) = 1 inside the list display.

**Notes**

- a(n) has about 1.32·n digits; the b-file has 201 terms (n = 0 to 200),
  and the bar is the whole b-file in 60 s, which takes a fraction of a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 137 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002010), CC BY-SA 4.0.
