# A000018

> Number of positive integers <= 2^n of form x^2 + 16*y^2.
> — [OEIS A000018](https://oeis.org/A000018)

Offset 0: 1, 1, 2, 2, 4, 8, 13, 25, 44, 83, 152, 286, 538, 1020, 1942, …

([A000017](https://oeis.org/A000017) is marked erroneous on the OEIS and is
skipped.)

### Python 3 — 93 bytes

```python
n=0
while 1:r=range(2<<n//2);print(len({min(x*x+16*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

- Signs do not matter, so x, y ≥ 0. Any value up to 2ⁿ has x, y ≤ 2^(n/2),
  and `range(2<<n//2)` goes past that bound for every n, so one range
  serves both variables.
- `min(…,2**n+1)` folds every value above 2ⁿ into the single value 2ⁿ + 1.
  That cap is always in the set, because the largest y in the range already
  gives 16y² > 2ⁿ. The set then holds 0 = 0² + 16·0², the cap, and each
  positive value ≤ 2ⁿ once, however many ways it can be written, so `-2`
  leaves a(n).
- The cap is 4 bytes shorter than filtering with a walrus,
  `{v for … if(v:=x*x+16*y*y)<=2**n}` and `-1`.
- A plain `while 1:` body can assign `r=range(…);` directly. That is 4 bytes
  shorter than `while[print(…)]:n+=1`, which needs `[r:=range(…)]and` to
  name the range inside the expression, because a walrus may not appear in a
  comprehension's iterable.

The same two tricks were first used for [A000049](../A000049/).

**Notes**

- Term n runs through 4^(⌊n/2⌋+1) pairs, about 2ⁿ⁺¹ to 2ⁿ⁺², so the
  program prints a(0)…a(23) in about 14 s, a(24) at 36 s and a(25) at 55 s
  (CPython 3.14). The bar is 24 terms in 60 s; the b-file goes to n = 45,
  far beyond any enumeration.
- The 101-byte walrus-filter version printed a(0)…a(23) in about 12 s on the
  same machine. Calling `min` on every pair, and adding the cap to the set
  again each time, makes a term take 1.15 to 1.35 times as long.
- The 103-byte version used `range(1<<n//2)` for y (half the pairs, one
  more term per minute).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 103 | first entry |
| 2026-11-05 | Python 3 | 101 | one range for x and y, named by a walrus before the set |
| 2026-11-05 | Python 3 | 93 | while 1: body and min cap instead of walrus filter |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000018), CC BY-SA 4.0.
