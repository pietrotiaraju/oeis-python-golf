# A000021

> Number of positive integers <= 2^n of form x^2 + 12 y^2.
> — [OEIS A000021](https://oeis.org/A000021)

Offset 0: 1, 1, 2, 2, 6, 9, 17, 30, 54, 98, 183, 341, 645, 1220, 2327, 4451, …

### Python 3 — 93 bytes

```python
n=0
while 1:r=range(2<<n//2);print(len({min(x*x+12*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

The same program as [A000018](../A000018/) with 12 in place of 16:

- Signs do not matter, so x, y ≥ 0. Any value up to 2ⁿ has x, y ≤ 2^(n/2),
  and `range(2<<n//2)` goes past that bound for every n, so one range
  serves both variables.
- `min(…,2**n+1)` folds every value above 2ⁿ into the single value 2ⁿ + 1.
  That cap is always in the set, because the largest y in the range already
  gives 12y² > 2ⁿ. The set then holds 0 = 0² + 12·0², the cap, and each
  positive value ≤ 2ⁿ once, however many ways it can be written, so `-2`
  leaves a(n).
- The cap is 4 bytes shorter than filtering with a walrus,
  `{v for … if(v:=x*x+12*y*y)<=2**n}` and `-1`.
- A plain `while 1:` body can assign `r=range(…);` directly. That is 4 bytes
  shorter than `while[print(…)]:n+=1`, which needs `[r:=range(…)]and` to
  name the range inside the expression, because a walrus may not appear in a
  comprehension's iterable.

The same two tricks were first used for [A000049](../A000049/).

**Notes**

- Term n runs through 4^(⌊n/2⌋+1) pairs, about 2ⁿ⁺¹ to 2ⁿ⁺², so the
  program prints a(0)…a(23) in about 15 s and a(24) at 39 s (CPython 3.14).
  The bar is 24 terms in 60 s; the b-file goes to n = 45, far beyond any
  enumeration.
- The 101-byte walrus-filter version printed a(0)…a(23) in about 13 s on the
  same machine. Calling `min` on every pair, and adding the cap to the set
  again each time, makes a term take 1.15 to 1.35 times as long.
- x² + 12y² and 3x² + 4y² ([A000049](../A000049/)) are the two reduced
  forms of discriminant −48, one in each genus.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 103 | first entry |
| 2026-11-05 | Python 3 | 101 | one range for x and y, named by a walrus before the set |
| 2026-11-05 | Python 3 | 93 | while 1: body and min cap instead of walrus filter |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000021), CC BY-SA 4.0.
