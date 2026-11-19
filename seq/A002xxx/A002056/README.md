# A002056

> Number of diagonal dissections of a convex n-gon into n-5 regions.
> — [OEIS A002056](https://oeis.org/A002056)

Offset 6: 1, 14, 120, 825, 5005, 28028, 148512, 755820, 3730650, 17978180, 84987760, …

### Python 3 — 61 bytes

```python
a=1;j=5
while[print(a)]:j+=2;a=a*4*j*(j*j-1)//(j*j-25)//(j-3)
```

**How it works**

- **Kirkman–Cayley.** A convex n-gon cut by k non-crossing diagonals
  into k + 1 regions can be cut in
  D(n, k) = C(n−3, k)·C(n+k−1, k)/(k+1) ways (Kirkman's formula, proved by
  Cayley, *On the partitions of a polygon*, 1891; see the entry).
- **Here** n − 5 regions means k = n − 6 diagonals:
  a(n) = C(n−3, 3)·C(2n−7, n−6)/(n−5) = (n−3)(n−4)/6·C(2n−7, n−6), the
  entry's formula.
- **Running ratio.** a(n)/a(n−1) = 2(n−3)(n−4)(2n−7)/((n−1)(n−5)(n−6))
  (the entry's recurrence). With j = 2n − 7 the four linear factors pair
  up around j: (n−3)(n−4) = (j²−1)/4 and (n−1)(n−6) = (j²−25)/4, while
  n − 5 = (j−3)/2, so a(n) = 4j(j²−1)·a(n−1)/((j²−25)(j−3)). j starts at
  5 (n = 6, a = 1) and grows by 2.
- **Exact.** 4j(j²−1)·a(n−1) equals (j²−25)(j−3)·a(n), and nested floor
  divisions by positive integers equal one division by the product.

**Notes**

- `import math` with `m*-~m*math.comb(2*m+1,m-2)//6`, m = n − 4, is
  64 bytes. a(n) has about 0.6·n digits; the b-file has 95 terms (n = 6 to
  100), and the bar is the whole b-file in 60 s, which takes a fraction of
  a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002056), CC BY-SA 4.0.
