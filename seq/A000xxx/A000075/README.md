# A000075

> Number of positive integers <= 2^n of form 2*x^2 + 3*y^2.
> — [OEIS A000075](https://oeis.org/A000075)

Offset 0: 0, 1, 2, 4, 7, 14, 23, 42, 76, 139, 258, 482, 907, 1717, 3269, …

### Python 3 — 93 bytes

```python
n=0
while r:=range(2<<n//2):print(len({min(2*x*x+3*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

- This is the [A000018](../A000018/) program with the form 2x² + 3y².
  Signs do not matter, so x, y ≥ 0, and any value up to 2ⁿ has
  x ≤ 2^((n−1)/2) and y < 2^(n/2). `range(2<<n//2)` goes past both bounds
  for every n, so one range serves both variables.
- `min(…,2**n+1)` folds every value above 2ⁿ into the single value 2ⁿ + 1.
  That cap is always in the set, because the largest y in the range already
  gives 3y² > 2ⁿ. The set then holds 0 = 2·0² + 3·0², the cap, and each
  positive value ≤ 2ⁿ once, however many ways it can be written, so `-2`
  leaves a(n).
- A range is truthy when it is not empty, so `while r:=range(2<<n//2):`
  names the range and keeps the loop going, with the print and `n+=1`
  after the colon.

**Notes**

- [A000067](../A000067/) caps at 2ⁿ itself and subtracts 1, which works
  because 2ⁿ is always of the form x² + 2y². Here 2ⁿ = 2·(2^k)² when
  n = 2k+1, but 4^k is never 2x² + 3y²: if v = 2x² + 3y² is even then y is
  even and v/2 = x² + 6(y/2)²; if that is even too then x is even and
  v/4 = 2(x/2)² + 3(y/2)². So 4^k is of the form exactly when 4^(k−1) is,
  and 1 is not. The cap 2**n would count 4^k wrongly for every even n.
- Filtering with a walrus, `{v for … if(v:=2*x*x+3*y*y)<=2**n}` and `-1`,
  is 97 bytes.
- Term n runs through 4^(⌊n/2⌋+1) pairs, about 2ⁿ⁺¹ to 2ⁿ⁺², so the
  program prints a(0)…a(23) in about 9 s, a(24) at 22 s and a(25) at 44 s
  (CPython 3.14). The bar is 24 terms in 60 s, as for the other
  "positive integers ≤ 2ⁿ of a form" sequences here; the b-file goes to
  n = 48, far beyond any enumeration.
- 2x² + 3y² and x² + 6y² are the two reduced forms of discriminant −24,
  one in each genus. The numbers 2x² + 3y² represents are
  [A002480](https://oeis.org/A002480).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000075), CC BY-SA 4.0.
