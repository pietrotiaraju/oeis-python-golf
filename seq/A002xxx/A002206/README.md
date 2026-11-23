# A002206

> Numerators of logarithmic numbers (also of Gregory coefficients G(n)).
> — [OEIS A002206](https://oeis.org/A002206)

Offset −1: 1, 1, −1, 1, −19, 3, −863, 275, −33953, 8183, −3250433, …

### Python 3 — 116 bytes

```python
from fractions import*
v=[];x=s=1
while[print(s*x.numerator)]:v=[x]+v;s=-s;x=-sum(map(Fraction,v,range(2,len(v)+2)))
```

**How it works**

- **Definition used.** 1/log(1+t) = Σ_(n≥−1) G(n)·tⁿ (the entry's
  formula), so f(m) = G(m − 1) are the coefficients of t/log(1+t):
  1, 1/2, −1/12, 1/24, −19/720, … The numerators of A002206 are those of
  G(n) in lowest terms, with sign; the denominators are
  [A002207](../A002207/).
- **Recurrence.** Put g(m) = (−1)^m·f(m), the coefficients of
  −t/log(1−t). Since −log(1−t)/t = Σ_j t^j/(j+1), the product of the two
  series is 1, so Σ_(k=0..m) g(k)/(m−k+1) = 0 for m ≥ 1, that is
  g(0) = 1 and g(m) = −Σ_(k<m) g(k)/(m−k+1). (This is the entry's
  recurrence of Daniel Suteu with the signs moved into g.)
- **The list.** `v` holds g(m−1), g(m−2), …, g(0), newest first, so the
  weights 1/2, 1/3, … run along it: `map(Fraction,v,range(2,len(v)+2))`
  makes the exact fractions g(m−1−j)/(j+2) (`Fraction` takes a `Fraction`
  numerator). The first pass has `x=1`, an int, which also has
  `.numerator`.
- **Sign.** The program prints the numerator of f(m) = (−1)^m·g(m), so
  `s` flips before each new term; m = 0 and 1 both print +1 (G(−1) = 1,
  G(0) = 1/2).
- Exact `Fraction` arithmetic and the generating function alone, so every
  term is right.

**Notes**

- The b-file has 102 terms (n = −1 to 100); the bar is the whole b-file
  in 60 s, which takes a fraction of a second; the program prints about
  550 terms in 10 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002206), CC BY-SA 4.0.
