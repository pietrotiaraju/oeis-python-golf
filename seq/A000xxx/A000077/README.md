# A000077

> Number of positive integers <= 2^n of form x^2 + 6 y^2.
> — [OEIS A000077](https://oeis.org/A000077)

Offset 0: 1, 1, 2, 4, 8, 13, 24, 42, 76, 140, 257, 483, 907, 1717, 3272, 6261, …

### Python 3 — 91 bytes

```python
n=0
while r:=range(2<<n//2):print(len({min(x*x+6*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

This is the [A000018](../A000018/) program with 6 in place of 16. The
coefficient has one digit, so it is 1 byte shorter.

- Signs do not matter, so x, y ≥ 0. Any value up to 2ⁿ has x, y ≤ 2^(n/2),
  and `range(2<<n//2)` goes past that bound for every n, so one range
  serves both variables.
- `min(…,2**n+1)` folds every value above 2ⁿ into the single value 2ⁿ + 1.
  That cap is always in the set, because the largest y in the range,
  2^(⌊n/2⌋+1) − 1 ≥ 2^⌊n/2⌋, already gives 6y² ≥ 6·4^⌊n/2⌋ > 2ⁿ. The set
  then holds 0 = 0² + 6·0², the cap, and each positive value ≤ 2ⁿ once,
  however many ways it can be written, so `-2` leaves a(n).
- A range is truthy when it is not empty, so `while r:=range(2<<n//2):`
  names the range and keeps the loop going, with the print and `n+=1`
  after the colon.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Term n runs through 4^(⌊n/2⌋+1) pairs, about 2ⁿ⁺¹ to 2ⁿ⁺², so the
  program prints a(0)…a(23) in about 14 s, a(24) at 35 s and a(25) at 58 s
  (CPython 3.14). The bar is 24 terms in 60 s, as for A000018, A000021 and
  A000024. The b-file goes to n = 48, far beyond any enumeration.
- Capping at 2ⁿ instead, `min(…,2**n)`, would need `-1-n%2`, because 2ⁿ
  is x² + 6y² only for even n. For odd n, x and then y must be even, and
  halving both turns x² + 6y² = 2ⁿ into x² + 6y² = 2ⁿ⁻², down to
  x² + 6y² = 2, which has no solution. That is 2 bytes longer.
- x² + 6y² and 2x² + 3y² ([A000075](https://oeis.org/A000075)) are the
  two reduced forms of discriminant −24, one in each genus.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000077), CC BY-SA 4.0.
