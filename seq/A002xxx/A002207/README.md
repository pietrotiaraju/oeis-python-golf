# A002207

> Denominators of logarithmic numbers (also of Gregory coefficients G(n)).
> — [OEIS A002207](https://oeis.org/A002207)

Offset −1: 1, 2, 12, 24, 720, 160, 60480, 24192, 3628800, 1036800, …

### Python 3 — 108 bytes

```python
from fractions import*
v=[]
while v:=[x:=-sum(map(Fraction,v,range(2,len(v)+2)))or 1]+v:print(x.denominator)
```

**How it works**

- **Definition used.** 1/log(1+t) = Σ_(n≥−1) G(n)·tⁿ (the entry's
  formula); these are the denominators of G(n) in lowest terms (the
  numerators are [A002206](../A002206/)).
- **Recurrence.** Let g(m) = (−1)^m·G(m − 1), the coefficients of
  −t/log(1−t) (same denominators). Multiplying by
  −log(1−t)/t = Σ_j t^j/(j+1) gives 1, so g(0) = 1 and
  g(m) = −Σ_(k<m) g(k)/(m−k+1) for m ≥ 1.
- **The list.** `while v:=[x:=…]+v:` computes the next g, puts it at the
  front of `v` (newest first, so `map(Fraction,v,range(2,len(v)+2))`
  pairs g(m−1−j) with the weight 1/(j+2)) and is never empty.
- **The first term.** On the first pass the sum is empty, and `or 1`
  turns its 0 into g(0) = 1. Later sums never fall back to 1, because
  g(m) ≠ 0 for m ≥ 1: integrating (1+t)^y = Σ_k C(y, k)·t^k over
  y ∈ [0, 1] gives t/log(1+t), so G(n) = ∫₀¹ C(y, n+1) dy (Reshetnikov's
  formula in the entry), and on 0 < y < 1 the polynomial
  C(y, n+1) = y(y−1)⋯(y−n)/(n+1)! has the constant sign (−1)ⁿ, so the
  integral is not 0.
- Exact `Fraction` arithmetic, so every term is right.

**Notes**

- The b-file has 102 terms (n = −1 to 100); the bar is the whole b-file
  in 60 s, which takes a fraction of a second; the program prints about
  580 terms in 10 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 108 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002207), CC BY-SA 4.0.
