# A000367

> Numerators of Bernoulli numbers B_2n.
> — [OEIS A000367](https://oeis.org/A000367)

Offset 0: 1, 1, −1, 1, −1, 5, −691, 7, −3617, 43867, −174611, 854513, …

### Python 3 — 138 bytes

```python
import math
r=[t:=1];p=1
print(1)
while[r<[t%2]or print(-(x:=len(r)*t*(p:=p*-4))//math.gcd(x,(p^-p*p)*p))]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- For n ≥ 1, B_2n = (−1)^(n−1)·2n·T(n) / (4ⁿ(4ⁿ − 1)), where T(n) is the
  tangent number [A000182](../A000182/)(n) (this is the classical relation
  behind the e.g.f. tan x = Σ (−1)^(n−1) 2^(2n)(2^(2n) − 1) B_2n x^(2n−1)/(2n)!).
  So a(n) is that fraction's numerator, with its sign.
- The tangent numbers come from the A000182 program unchanged: the
  Seidel–Entringer rows `r=[t:=t+x for x in[-t]+r[::-1]]`, with row m
  ending in the zigzag number A000111(m), and the filter `r<[t%2]` that
  lets through row 0 and the odd rows 3, 5, 7, … (the A000182 page proves
  it). Row 2n − 1 has 2n entries, so `len(r)*t` is 2n·T(n).
- p runs through (−4)ⁿ, one step per printed term. The denominator
  D = (−4)ⁿ − (−16)ⁿ = (−1)^(n−1)·4ⁿ(4ⁿ − 1) is `p^-p*p`: for even n the
  bits of 4ⁿ lie below the run of ones of −16ⁿ, so XOR adds them; for odd n
  both are negative and XOR leaves the bits 2n … 4n−1, which is 16ⁿ − 4ⁿ
  (the same trick as in [A000187](../A000187/)).
- The sign and the reduction come from one floor division. With
  x = 2n·T(n)·p, gcd(x, D·p) = |p|·gcd(2n·T(n), D), so `-x//gcd(x,D*p)` is
  exactly −sgn(p)·2n·T(n)/gcd(2n·T(n), D); −sgn(p) = (−1)^(n−1) is the sign
  of B_2n, so this is the signed numerator. Only `math.gcd` is needed, 7
  bytes under `fractions.Fraction(…).numerator` with its import.
- a(0) = 1 (B_0 = 1) is printed first. The filter then lets row 0 through,
  where the formula runs with n = 1 but `len(r)*t` = 1·1 instead of
  2·T(1) = 2: that gives 1/12 instead of 1/6, whose numerator is the same,
  a(1) = 1. Rows 3, 5, 7, … give a(2), a(3), … with the right 2n.

**Notes**

- Exact integer arithmetic, correct for every n; the only theorem used is
  the tangent–Bernoulli relation above.
- With `from fractions import*` and `Fraction(len(r)*t,(p:=p*-4)^-p*p).numerator`
  (and the filter `len(r)%2`) the program is 145 bytes.
- Row m has m + 1 entries, so the triangle costs about 2n² big-integer
  additions for a(n). The whole b-file (250 terms) prints in about 0.1 s;
  the program stops after a(1031), when the next numerator passes the
  4300-digit int-to-str limit of Python 3.11+. The bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 138 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000367), CC BY-SA 4.0.
