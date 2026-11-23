# A002208

> Numerators of coefficients for numerical integration.
> — [OEIS A002208](https://oeis.org/A002208)

Offset 0: 1, 1, 5, 3, 251, 95, 19087, 5257, 1070017, 25713, 26842253, …

### Python 3 — 103 bytes

```python
from fractions import*
v=[]
while v:=[x:=1-sum(map(Fraction,v,range(2,len(v)+2)))]+v:print(x.numerator)
```

**How it works**

- **Definition used.** The rationals v(n) = A002208(n)/A002209(n) have the
  generating function −t/((1−t)·log(1−t)) (the entry's formula):
  1, 1/2, 5/12, 3/8, 251/720, … These are the coefficients of the
  Adams–Bashforth formula: v(n) = 1 − |G(0)| − … − |G(n−1)| with the
  Gregory coefficients G of [A002206](../A002206/)/[A002207](../A002207/).
- **Recurrence.** −log(1−t)/t = Σ_j t^j/(j+1), and multiplying it by
  Σ v(n)tⁿ gives 1/(1−t). Comparing coefficients,
  Σ_(i=0..n) v(i)/(n−i+1) = 1, so v(n) = 1 − Σ_(i<n) v(i)/(n−i+1)
  (Kruchinin's formula in the entry).
- **The list.** `while v:=[x:=…]+v:` computes v(n), puts it at the front
  of `v` and is never empty. Newest first, the weights 1/2, 1/3, … run
  along the list: `map(Fraction,v,range(2,len(v)+2))` makes the exact
  fractions v(n−1−j)/(j+2) (`Fraction` takes a `Fraction` numerator). The
  first pass has an empty sum and x = 1, an int, which also has
  `.numerator`.
- Exact `Fraction` arithmetic, so every term is right.

**Notes**

- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second; the program prints about 570
  terms in 10 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 103 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002208), CC BY-SA 4.0.
