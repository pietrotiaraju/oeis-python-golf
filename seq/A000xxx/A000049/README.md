# A000049

> Number of positive integers <= 2^n of the form 3*x^2 + 4*y^2.
> — [OEIS A000049](https://oeis.org/A000049)

Offset 0: 0, 0, 2, 3, 5, 9, 16, 29, 53, 98, 181, 341, 640, 1218, 2321, …

### Python 3 — 93 bytes

```python
n=0
while r:=range(2<<n//2):print(len({min(3*x*x+4*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

- Signs do not matter, so x, y ≥ 0. A value up to 2ⁿ has 3x² ≤ 2ⁿ and
  4y² ≤ 2ⁿ, so x, y < 2^(n/2), and `range(2<<n//2)` goes past that bound
  for every n. One range serves both variables.
- `min(…,2**n+1)` folds every value above 2ⁿ into the single value 2ⁿ + 1.
  That cap is always in the set, because the largest x in the range already
  gives 3x² > 2ⁿ. The set then holds 0 = 3·0² + 4·0², the cap, and each
  positive value ≤ 2ⁿ once, so `-2` leaves a(n).
- The cap is 4 bytes shorter than filtering with a walrus,
  `{v for … if(v:=3*x*x+4*y*y)<=2**n}` and `-1`.
- A range is truthy when it is not empty, so `while r:=range(2<<n//2):`
  names the range and keeps the loop going, with the print and `n+=1`
  after the colon. That is 1 byte shorter than a `while 1:` body that
  assigns `r=range(…);`, and 5 bytes shorter than `while[print(…)]:n+=1`,
  which needs `[r:=range(…)]and` to name the range inside the expression,
  because a walrus may not appear in a comprehension's iterable.

**Notes**

- Term n costs about 2ⁿ⁺² pairs, so the program prints a(0)…a(23) in
  about 16 s, a(24) at 37 s and a(25) at 56 s. The bar is 24 terms in 60 s,
  as for the other "positive integers ≤ 2ⁿ of a form" sequences here
  ([A000018](../A000018/), [A000021](../A000021/),
  [A000024](../A000024/)). The b-file goes to n = 49, far beyond any
  enumeration.
- The 94-byte version had a `while 1:` body starting `r=range(2<<n//2);`.
  It runs at the same speed.
- The 103-byte walrus-filter version is about twice as fast, because it skips
  the `min` call and the larger values never reach the set.
- 3x² + 4y² and x² + 12y² ([A000021](../A000021/)) are the two reduced
  forms of discriminant −48, one in each genus. The numbers they represent
  are [A020677](https://oeis.org/A020677).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 94 | first entry |
| 2026-11-05 | Python 3 | 93 | range named in the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000049), CC BY-SA 4.0.
