# A002006

> Number of rooted planar maps with 2n trivalent vertices and a root vertex of valence 4.
> — [OEIS A002006](https://oeis.org/A002006)

Offset 0: 2, 24, 272, 3424, 46720, 676608, 10251520, 160900608, 2597746688, 42921562112, …

### Python 3 — 70 bytes

```python
a,b=1,4;k=0
while[print(b-2*a)]:k+=3;a,b=b,432*(k*k-1)*a//(k+6)//(k+9)
```

**How it works**

- **Maps counted.** Rooted planar maps (loops and multiple edges allowed:
  that is what the data count) whose root vertex has valence k and whose
  m other vertices are all trivalent; call the number T(k, m). Here
  a(n) = T(4, 2n).
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
- **Valence 4.** The recursion gives M_4 = (M_3 − 2·M_0·M_1)/t
  = (C(x) − 1)/x − 2C(x) with x = t², so a(n) = c(n+1) − 2c(n): the
  entry's formula.
- **c(n)**, the number of rooted cubic maps with 2n vertices, is
  2^(2n+1)·(3n)!!/((n+2)!·n!!), the classical closed form (see
  [A002005](../A002005/)). It gives
  (n+1)(n+2)·c(n) = 48(3n−2)(3n−4)·c(n−2), and with k = 3n − 3 this is
  c(n) = 432(k²−1)·c(n−2)/((k+6)(k+9)). The numerator equals
  (k+6)(k+9)·c(n), so the two floor divisions are exact
  (⌊⌊x/p⌋/q⌋ = ⌊x/(pq)⌋).

- **The program** is the [A002005](../A002005/) pair step (a, b) =
  (c(n), c(n+1)) printing `b-2*a`.

**Notes**

- a(n) has about 1.32·n digits. The b-file has 201 terms (n = 0 to 200);
  the bar is the whole b-file in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002006), CC BY-SA 4.0.
