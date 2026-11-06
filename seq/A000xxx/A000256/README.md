# A000256

> Number of simple triangulations of the plane with n nodes.
> — [OEIS A000256](https://oeis.org/A000256)

Offset 3: 1, 1, 0, 1, 3, 12, 52, 241, 1173, 5929, 30880, 164796, 897380, 4970296, 27930828, …

### Python 3 — 92 bytes

```python
import math
a=m=1
while[print(abs(a))]:a=(7*math.comb(3*m,m-1)//m+(8*m+5)*a)//(12-32*m);m+=1
```

**What is counted**

- These are Tutte's rooted *simple* triangulations: no separating triangles
  (4-connected, apart from the single triangle and K₄), counted by number of
  nodes. Write a_m = a(m + 3), so a_0 = a_1 = 1 (triangle, K₄), a_2 = 0 and
  a_3 = 1 (octahedron).
- Tutte (1962, eq. 2.6) relates their generating function y(z) = Σ a_m z^m to
  the rooted simplicial polyhedra g(x) = Σ 2(4n+1)!/((n+1)!(3n+2)!) xⁿ
  ([A000260](https://oeis.org/A000260)): y(x·g²) = 2 − 1/g.

**From Tutte's equation to a recurrence**

- With x = θ(1 − θ)³ one has g = (1 − 2θ)/(1 − θ)³, so z = x·g² =
  θ(1 − 2θ)²/(1 − θ)³ and y = 2 − (1 − θ)³/(1 − 2θ).
- T = (1 − θ)/(1 − 2θ) satisfies T = 1 + z·T³, so T is the ternary-tree series
  Σ t_m z^m with t_m = C(3m, m)/(2m + 1) = C(3m, m − 1)/m
  ([A001764](https://oeis.org/A001764)), and y = 2 − T³/(2T − 1)².
- Differentiating through T (T′ = T⁴/(3 − 2T)) shows that A = y − 2 satisfies

  z(32 + 8z)·A′ + (13z − 12)·A = 7T + 5,

  a rational identity in θ (checked with sympy). Coefficient by coefficient
  this is a two-term recurrence, Vladeta Jovovic's formula on the OEIS page:

  4(8m − 3)·A_m + (8m + 5)·A_{m−1} = 7·t_m  (m ≥ 1),  A_0 = −1,

  and A_m = a_m for m ≥ 1, while A_0 = a_0 − 2 = −1.

**How it works**

- The program runs the recurrence for S = −A instead:
  S_m = (7t_m + (8m + 5)S_{m−1})/(12 − 32m), with S_0 = −A_0 = 1. That start
  value is the true a_0, and S_m = −a_m ≤ 0 for m ≥ 1, so `abs` prints the
  right term every time. Some sign fix is needed either way, because the
  recurrence only knows the virtual A_0 = −1; `print(1);a=m=1` with A and no
  `abs` is 2 bytes longer.
- `7*math.comb(3*m,m-1)//m` is 7t_m (4 bytes under `comb(3*m,m)//(2*m+1)`).
  The outer `//(12-32*m)` is exact because the quotient is ±a_m, an integer,
  and Python's floor division of an exact multiple is exact for negative
  divisors too.
- m starts at 1 together with a (`a=m=1`) and is bumped after the update, so
  no separate `m=0`.
- The homogeneous part of the recurrence is solved by (8m + 5)(−1/4)^m, which
  is why no recurrence of this kind can start from the real a_0 = 1: the
  m = 1 step would give a_1 = −6/20.

**Notes**

- Exact integer arithmetic; correctness for every n rests on Tutte's equation
  (W. T. Tutte, A census of planar triangulations, Canad. J. Math. 14 (1962)
  21–38) and his formula for A000260.
- The whole b-file (198 terms) prints in well under a second, and that is the
  bar.
- a(n) grows like (27/16)ⁿ, so Python's 4300-digit int-to-str limit would only
  stop the printing near n = 19000.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000256), CC BY-SA 4.0.
