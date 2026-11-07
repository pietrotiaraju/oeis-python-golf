# A000897

> a(n) = (4*n)! / ((2*n)!*n!^2).
> — [OEIS A000897](https://oeis.org/A000897)

Offset 0: 1, 12, 420, 18480, 900900, 46558512, 2498640144, 137680171200, …

### Python 3 — 51 bytes

```python
a=1;m=4
while[print(a)]:a=a*64*~-m*(m-3)//m//m;m+=4
```

**How it works**

- Ratio of consecutive terms: (4n)!/(4n−4)! over (2n)!/(2n−2)! leaves
  (4n−1)(4n−3)·4, and n!² gives n², so
  a(n)·n² = 4(4n−1)(4n−3)·a(n−1) (Michael Somos' recurrence).
- With `m` = 4n this is a(n) = a(n−1)·64(m−1)(m−3)/m². The product is an
  exact multiple of m², so `//m//m` (floor of a floor) is exact.
- `~-m` is m − 1 without parentheses, 1 byte under `(m-1)`.
- `a=1;m=4`: the first pass of the loop body computes a(1) with m = 4.
  Starting from m = 4n − 3 instead (`a=m=1`, ratio 64m(m+2)/(m+3)²) is the
  same length.
- Two binomials, `comb(4*n,2*n)*comb(2*n,n)` with `from math import*`, are
  65 bytes.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 201 terms (up to a(200)); the bar is the whole b-file in
  60 s. It prints them at once.
- a(n) first has more than 4300 digits at n = 2383, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000897), CC BY-SA 4.0.
