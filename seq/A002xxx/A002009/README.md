# A002009

> Number of rooted planar maps with 2n+1 trivalent vertices and a root vertex of valence 7.
> — [OEIS A002009](https://oeis.org/A002009)

Offset 0: 56, 1120, 18592, 300288, 4877824, 80349696, 1344154112, 22821564416, …

### Python 3 — 117 bytes

```python
L=[1,4,32];k=3
while 1:k+=3;L+=432*(k*k-1)*L[-2]//(k+6)//(k+9),;*R,x,y=L;print(y-8*x-6*sum(v*R.pop()for v in R[:-1]))
```

**How it works**

- **Maps counted.** Rooted planar maps (loops and multiple edges allowed:
  that is what the data count) whose root vertex has valence k and whose
  m other vertices are all trivalent; call the number T(k, m). Here
  a(n) = T(7, 2n+1).
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
- **Valence 7.** M_7 = (M_6 − 2M_0M_4 − 2M_1M_3 − M_2²)/t gives
  a(n) = c(n+3) − 8c(n+2) + 6c(n+1) − 6Q(n+1), Q(n) = Σ_(i=0..n) c(i)c(n−i),
  the entry's formula. Q(n+1) contains c(0)c(n+1) = c(n+1) once more than
  U(n) = Σ_(i=0..n) c(i)c(n+1−i), so a(n) = c(n+3) − 8c(n+2) − 6U(n).
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
- **The sum.** `*R,x,y=L` leaves R = c(0…n+1); the generator walks
  `R[:-1]` = c(0…n) from the front while `R.pop()` takes c(n+1), c(n), …
  from the back, so it adds c(i)·c(n+1−i): U(n).

**Notes**

- a(n) has about 1.32·n digits; the b-file has 201 terms (n = 0 to 200),
  and the bar is the whole b-file in 60 s, which takes a fraction of a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 117 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002009), CC BY-SA 4.0.
