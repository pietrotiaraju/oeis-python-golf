# A002209

> Denominators of coefficients for numerical integration.
> — [OEIS A002209](https://oeis.org/A002209)

Offset 0: 1, 2, 12, 8, 720, 288, 60480, 17280, 3628800, 89600, 95800320, …

### Python 3 — 105 bytes

```python
from fractions import*
v=[]
while v:=[x:=1-sum(map(Fraction,v,range(2,len(v)+2)))]+v:print(x.denominator)
```

**How it works**

- **Definition used.** The rationals v(n) = A002208(n)/A002209(n) have the
  generating function −t/((1−t)·log(1−t)) (the entry's formula):
  1, 1/2, 5/12, 3/8, 251/720, … (the Adams–Bashforth coefficients). These
  are their denominators in lowest terms.
- **Recurrence.** −log(1−t)/t = Σ_j t^j/(j+1), and multiplying it by
  Σ v(n)tⁿ gives 1/(1−t), so Σ_(i=0..n) v(i)/(n−i+1) = 1 and
  v(n) = 1 − Σ_(i<n) v(i)/(n−i+1) (Kruchinin's formula in the entry).
- **The list.** `while v:=[x:=…]+v:` computes v(n), puts it at the front
  of `v` (newest first, so `map(Fraction,v,range(2,len(v)+2))` pairs
  v(n−1−j) with the weight 1/(j+2)) and is never empty. The first pass
  has an empty sum and x = 1, an int, which also has `.denominator`.
- Same program as [A002208](../A002208/) with `.denominator`; exact
  `Fraction` arithmetic, so every term is right.

**Notes**

- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second; the program prints about 550
  terms in 10 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002209), CC BY-SA 4.0.
