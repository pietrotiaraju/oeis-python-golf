# A000344

> a(n) = 5*binomial(2n, n-2)/(n+3).
> — [OEIS A000344](https://oeis.org/A000344)

Offset 2: 1, 5, 20, 75, 275, 1001, 3640, 13260, 48450, 177650, 653752, …

### Python 3 — 52 bytes

```python
a=m=1
while[print(a)]:a=4*a-6*a*(m-2)//m//(m+5);m+=1
```

**How it works**

- From the closed form, a(n+1)/a(n) = (2n+2)(2n+1)/((n−1)(n+4)). With
  m = n − 1 (so m = 1 at a(2) = 1) the ratio is (2m+4)(2m+3)/(m(m+5)), and
  splitting off its limit 4 gives 4 − 6(m − 2)/(m(m + 5)).
- So a(n+1) = 4a − 6a(m − 2)/(m(m + 5)), the two-piece division of the
  Catalan record [A000108](../A000108/). The second piece is an integer
  because a(n+1) and 4a are, and `x//m//(m+5)` equals x//(m(m+5)) for positive
  divisors, so the division is exact even when m − 2 < 0 at m = 1.

**Notes**

- The ratio taken whole, `a=a*(2*m+4)*(2*m+3)//m//(m+5)`, is 56 bytes. The
  closed form with `import math` and `5*math.comb(2*n,n-2)//(n+3)` is 62, and
  the ballot form C(2n, n−2) − C(2n, n−3) with two `math.comb` calls is 72.
- Stepping m inside the last divisor, `//((m:=m+1)+4)`, is 2 bytes longer
  than `//(m+5);m+=1`. Starting one step early is impossible: the ratio from
  a(1) to a(2) divides by n − 1 = 0.
- Exact integers, so every term is right. a(7152) is the first term with more
  than 4300 digits, so Python 3.11+ stops there with a `ValueError` from the
  int-to-str limit, which is not counted as a failure.
- The b-file has 299 terms (n = 2 to 300) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 52 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000344), CC BY-SA 4.0.
