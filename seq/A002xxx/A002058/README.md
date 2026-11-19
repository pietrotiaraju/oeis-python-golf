# A002058

> Number of internal triangles in all triangulations of an (n+1)-gon.
> — [OEIS A002058](https://oeis.org/A002058)

Offset 5: 2, 14, 72, 330, 1430, 6006, 24752, 100776, 406980, 1634380, 6537520, 26075790, …

### Python 3 — 50 bytes

```python
a=2;j=5
while[print(a)]:j+=2;a=a*4*j*~-j//(j*j-25)
```

**How it works**

- **Count.** Put N = n + 1. A triangle of a triangulation of the N-gon is
  internal when none of its sides is a side of the polygon, i.e. the three
  arcs of the boundary between its corners have p, q, r ≥ 2 edges,
  p + q + r = N. The triangulations containing it triangulate the three
  cut-off polygons independently: Cat(p−1)·Cat(q−1)·Cat(r−1) ways. Choosing
  a starting corner (N ways) and an ordered (p, q, r) names each triangle
  three times, so a(n) = (N/3)·Σ Cat(p−1)Cat(q−1)Cat(r−1).
- **Closed form.** With c(x) the Catalan generating function,
  Σ_(p≥2) Cat(p−1)xᵖ = x(c − 1) = x²c², so the sum is
  [x^(N−6)] c⁶ = 6/(2N−6)·C(2N−6, N−6) (Lagrange inversion). Hence
  a(n) = N/(N−3)·C(2N−6, N−6) = (n+1)/(n−2)·C(2n−4, n−5)
  = 2·C(2n−5, n−5), the entry's formula (Callan).
- **Running ratio.** With m = n − 5, a = 2·C(2m+5, m) and
  a(m)/a(m−1) = (2m+5)(2m+4)/(m(m+5)). With j = 2m + 5 this is
  4j(j−1)/(j²−25): `a*4*j*~-j//(j*j-25)`, exact because the product
  equals (j²−25)·a. j starts at 5 (n = 5, a = 2) and grows by 2.

**Notes**

- Stanley's comment in the entry: the old name, "partitions of an n-gon
  into n − 3 parts", was wrong; the data are an auxiliary sequence of
  Cayley's. The program follows the current name and the data, which the
  count above matches.
- `import math` with `2*math.comb(2*m+5,m)` is 55 bytes. a(n) has about
  0.6·n digits; the b-file has the 25 terms of the entry (n = 5 to 29),
  and the bar is all of them in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002058), CC BY-SA 4.0.
