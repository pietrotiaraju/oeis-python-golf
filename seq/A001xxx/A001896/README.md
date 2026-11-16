# A001896

> Numerators of cosecant numbers -2*(2^(2*n - 1) - 1)*Bernoulli(2*n); also of Bernoulli(2*n, 1/2) and Bernoulli(2*n, 1/4).
> — [OEIS A001896](https://oeis.org/A001896)

Offset 0: 1, −1, 7, −31, 127, −2555, 1414477, −57337, 118518239, −5749691557, …

### Python 3 — 135 bytes

```python
import math
r=[t:=1];p=1
print(1)
while[r<[t%2]or print(-(x:=len(r)*t*((p:=p*4)-2))//math.gcd(x,p*p-p))]:r=[t:=x-t for x in[t]+r[::-1]]
```

**How it works**

- The cosecant numbers are c(n) = −2(2^(2n−1) − 1)B(2n) = −(4ⁿ − 2)B(2n), and
  B(2n) = (−1)^(n−1)·2n·T(n)/(4ⁿ(4ⁿ − 1)) with T(n) = E(2n − 1) the tangent numbers (Euler zigzag
  numbers of odd index: 1, 2, 16, 272, …). So c(n) = −2n·(−1)^(n−1)T(n)·(4ⁿ − 2)/(4ⁿ(4ⁿ − 1)), and
  the numerator is that fraction reduced by a gcd, as in [A000367](../../A000xxx/A000367/).
- `r` runs through the rows of a signed Seidel–Entringer (boustrophedon) triangle:
  `[t:=x-t for x in[t]+r[::-1]]` starts the new row at t − t = 0 and then takes alternating
  partial sums of the reversed row. If row k is s·(−1)ⁱR(k, i), with R the usual boustrophedon,
  the next row is s·(−1)^(k−1)·(−1)ⁱR(k + 1, i); from row 0 = [1] this gives last entries
  t = (−1)^(k(k−1)/2)·E(k): 1, 1, −1, −2, 5, 16, −61, −272, … For k = 2n − 1 that is
  (−1)^(n−1)T(n), the sign the formula needs, and the row has length 2n.
- `p` is 4ⁿ, and `-(x:=len(r)*t*((p:=p*4)-2))//math.gcd(x,p*p-p)` is −x/g with x = 2n·t·(4ⁿ − 2)
  and g = gcd(x, 4ⁿ(4ⁿ − 1)): the numerator of c(n) = −x/(4ⁿ(4ⁿ − 1)), sign included, since the
  denominator is positive.
- Which rows print: after the first, every row starts with 0, so `r<[t%2]` is true exactly when
  t is odd. The secant numbers E(2n) are all odd and the tangent numbers T(n) are even for
  n ≥ 2 (2ⁿ⁻¹ divides T(n)), so rows 3, 5, 7, … print c(2), c(3), c(4), … The start row [1]
  is not below [1], so it prints too, standing in for row 1 = [0, 1] (whose 1 is odd): with
  length 1 instead of 2 it gives x = 2 instead of 4, and both reduce to the numerator −1 of
  c(1) = −1/3. c(0) = 1 is printed first.

**Notes**

- Exact integer arithmetic, so the program is right for every n. The b-file has only the
  18 terms of the entry (to c(17)); they come at once. The first 200 numerators were also
  checked against −(4ⁿ − 2)B(2n) from an exact `Fraction` recurrence.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 135 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001896), CC BY-SA 4.0.
