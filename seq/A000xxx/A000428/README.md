# A000428

> Euler transform of A000579.
> — [OEIS A000428](https://oeis.org/A000428)

Offset 1: 1, 8, 36, 148, 554, 2094, 7624, 27428, 96231, 332159, …

a(n) is the coefficient of xⁿ in Π_{k≥1} (1 − x^k)^(−C(k+5, 6)): the number of
multisets of parts with sum n when a part k comes in C(k+5, 6) kinds
(A000579 shifted to start at C(6, 6) = 1). This is MacMahon's guess for the
7-dimensional partitions [A000427](../A000427/), which first differs at n = 6
(2094 against 2024).

### Python 3 — 109 bytes

```python
import math
a=[1];n=0
while 1:n-=1;print(x:=sum(d*math.comb(5-d,6)*sum(a[d::d])for d in range(n,0))//n);a+=x,
```

**How it works**

- Write c(k) = C(k+5, 6) and A(x) = Σ a(m)xᵐ with a(0) = 1. Logarithmic
  differentiation of the product gives m·a(m) = Σ_{r=1}^{m} b(r)·a(m−r) with
  b(r) = Σ_{k|r} k·c(k); grouping by k instead of r,

  m·a(m) = Σ_{k=1}^{m} k·c(k)·Σ_{j≥1} a(m − jk).

- Before a(m) is computed the list holds a(0), …, a(m−1) and n = −m. With
  d = −k, the slice `a[d::d]` runs backwards from the end in steps of k:
  a(m−k), a(m−2k), …, and stops at the start of the list. So no divisor sums
  and no bound on j are needed.
- `math.comb(5-d,6)` is C(k+5, 6) = c(k). d and n are both negative, so the
  signs cancel in `d*…//n`, and the division is exact because m·a(m) is that
  sum.
- `print(x:=…)` prints the new term and `a+=x,` appends it; the auxiliary
  a(0) = 1 is never printed.

**Notes**

- `from math import*` with `comb`: 1 byte more; appending first and printing
  `a[-1]`: also 1 more. The same program with `comb(4-d,5)` is
  [A000417](../A000417/).
- Exact integer arithmetic, so the program is right for every n.
- Term m costs about m·log m slice entries: about 4800 terms in 60 s here.
- The b-file has 1000 terms (up to a(1000)); the bar is the whole b-file in
  60 s.
- log a(n) grows like 8·ζ(8)^(1/8)·(n/7)^(7/8), so the 4300-digit
  int-to-str limit only comes near n ≈ 24000, far beyond what prints in
  practice.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 161 | first entry |
| 2026-11-06 | Python 3 | 160 | use a shorter math import |
| 2026-11-06 | Python 3 | 111 | reorder the Euler-transform sum and use one coefficient list |
| 2026-11-07 | Python 3 | 109 | `import math`, print the new term through a walrus |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000428), CC BY-SA 4.0.
