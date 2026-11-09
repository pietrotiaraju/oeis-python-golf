# A001284

> Numbers of form m*k with m+1 <= k <= 2m-1.
> — [OEIS A001284](https://oeis.org/A001284)

Offset 1: 6, 12, 15, 20, 24, 28, 30, 35, 40, 42, 45, 48, 54, 56, 60, …

The entries of the triangle [A001283](../A001283/) in increasing order,
each value once.

### Python 3 — 76 bytes

```python
x=y=1
while 1:x+=1;y+=y*y<x;any(2*m*m>x>x%m*x for m in range(y))and print(x)
```

**How it works**

- x = m·k with m + 1 ≤ k ≤ 2m − 1 means: m divides x, and k = x/m
  satisfies m < k < 2m, that is m² < x < 2m². So x is a term exactly when
  it has a divisor m ≥ 1 with m² < x < 2m².
- `y` is kept as the least integer with y² ≥ x: when x grows by one, a y
  with y² ≥ x − 1 but y² < x has y² = x − 1, and then
  (y + 1)² = x + 2y ≥ x, so `y+=y*y<x` is enough. Hence (y − 1)² < x, and
  `range(y)` is exactly the m ≥ 0 with m² < x.
- The chain `2*m*m>x>x%m*x` tests x < 2m² and then x > (x mod m)·x,
  which for x > 0 holds exactly when x mod m = 0: any remainder r ≥ 1 gives
  r·x ≥ x. For m = 0 the first comparison 0 > x is false, so `x%0` is
  never evaluated.
- `any(…)and print(x)` prints x once, however many m work, and the x come
  in increasing order. Exact integers, so every term is right.

**Notes**

- `x<2*m*m>0==x%m` tests the same and is 1 byte longer.
- Each x costs about √x tests; the 10000th term, a(10000) = 36848, comes
  after about 0.5 reference seconds.
- The b-file has 10000 terms; the bar is the whole b-file in 60 s.

## First 5500 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(5500) have to arrive in time.

### Python 3, 5500 terms — 68 bytes

```python
x=1
while 1:x+=1;any(x>m*m>x//2>x%m*x for m in range(x))and print(x)
```

**How it works**

- The same test without the bound `y`: m runs over all of 0, …, x − 1, so
  the chain itself has to check m² < x < 2m². `x>m*m>x//2` does: for even
  x, m² > x/2 is 2m² > x; for odd x, m² > (x − 1)/2 means 2m² ≥ x, and
  2m² = x is impossible.
- Then `x//2>x%m*x` is m | x as in the main record (x//2 ≥ 1 > 0, while a
  remainder r ≥ 1 gives r·x ≥ x > x//2). For m = 0 (x ≥ 2) the comparison
  0 > x//2 fails first, so `x%0` is never evaluated.
- Dropping `y` saves 8 bytes, but every x that is not a term now costs x
  tests instead of √x.

**Limits**

- The work grows like x², and a(n) is about 3.7n, so the terms slow down
  steadily: a(5500) = 19964 arrives after about 16 reference seconds, and
  a(7000) = 25551 after about 27, too close to the limit of 30 for a
  7000-term bar. Far short of the main bar of 10000 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 77 | first entry |
| 2026-11-09 | Python 3, 5500 terms | 70 | first entry: no square-root bound on m |
| 2026-11-09 | Python 3 | 76 | divisibility as x > (x mod m)·x |
| 2026-11-09 | Python 3, 5500 terms | 68 | m² < x < 2m² as x > m² > ⌊x/2⌋ |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001284), CC BY-SA 4.0.
