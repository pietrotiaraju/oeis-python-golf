# A001067

> Numerator of Bernoulli(2*n)/(2*n).
> — [OEIS A001067](https://oeis.org/A001067)

Offset 1: 1, −1, 1, −1, 1, −691, 1, −3617, 43867, −174611, 77683, −236364091, …

### Python 3 — 122 bytes

```python
import math
r=[t:=1];p=1
while[r<[t%2]or print(-(x:=t*(p:=p*-4))//math.gcd(x,(p^-p*p)*p))]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- B₂ₙ/(2n) = (−1)ⁿ⁻¹·T(n) / (4ⁿ(4ⁿ − 1)), where T(n) is the tangent
  number [A000182](../../A000xxx/A000182/)(n). This is the relation
  B₂ₙ = (−1)ⁿ⁻¹·2n·T(n)/(4ⁿ(4ⁿ − 1)) behind the e.g.f. of tan x, divided
  by 2n; the program is the [A000367](../../A000xxx/A000367/) one
  (numerators of B₂ₙ) without its factor 2n (`len(r)*`) and without the
  extra a(0).
- The tangent numbers come from the Seidel–Entringer rows
  `r=[t:=t+x for x in[-t]+r[::-1]]`: row m ends in the zigzag number
  A000111(m), and the filter `r<[t%2]` lets through row 0 (t = 1 = T(1))
  and the odd rows 3, 5, 7, … (t = T(2), T(3), …); see the A000182 page.
- p runs through (−4)ⁿ. The signed denominator D = (−4)ⁿ − (−16)ⁿ =
  (−1)ⁿ⁻¹·4ⁿ(4ⁿ − 1) is `p^-p*p` (the XOR of p with −p², the trick from
  A000367).
- With x = T(n)·p, gcd(x, D·p) = |p|·gcd(T(n), D), so `-x//gcd(x,D*p)` is
  −sgn(p)·T(n)/gcd(T(n), D) = (−1)ⁿ⁻¹·T(n)/gcd: the reduced numerator,
  with the sign of B₂ₙ.

**Notes**

- Exact integer arithmetic, correct for every n; the only theorem used is
  the tangent–Bernoulli relation above. Every fraction is reduced by a
  gcd, so nothing leans on [A046968](https://oeis.org/A046968), which
  first differs at n = 574 (an OEIS comment).
- The whole b-file (314 terms) prints in about 0.2 s. The program stops
  after a(1031), when the next numerator passes the 4300-digit int-to-str
  limit of Python 3.11+. The bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 122 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001067), CC BY-SA 4.0.
