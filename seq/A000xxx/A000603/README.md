# A000603

> Number of nonnegative solutions to x^2 + y^2 <= n^2.
> — [OEIS A000603](https://oeis.org/A000603)

Offset 0: 1, 3, 6, 11, 17, 26, 35, 45, 58, 73, 90, 106, 123, 146, 168, …

### Python 3 — 75 bytes

```python
n=0
while r:=range(n,1):print(sum(x*x+y*y<=n*n for x in r for y in r));n-=1
```

**How it works**

- a(n) counts the points (x, y) with x, y ≥ 0 and x² + y² ≤ n², all of which
  lie in the square 0 ≤ x, y ≤ n. The program walks that square and adds 1
  (a `True`) for every point inside the quarter disc.
- The counter runs downwards, n = 0, −1, −2, …, and `range(n,1)` is
  n, …, 0: the same squares as 0, …, |n|, a byte under `range(n+1)`; n·n is
  the same either way.
- The range is named in the loop condition (it always contains 0, so it is
  never empty); a walrus cannot sit in a comprehension's iterable. This is the
  template of [A000328](../A000328/) with a quarter instead of the full square;
  [A000604](../A000604/), [A000605](../A000605/) and [A000606](../A000606/) use
  it in three dimensions.

**Notes**

- Exact integer comparisons, so every term is right.
- Faster but longer: one column at a time,
  `sum(math.isqrt(n*n-x*x)+1for x in range(n,1))` with `import math`, is
  80 bytes and does O(n) work per term instead of O(n²).
- The program printed 701 to 754 terms in 60 s in two runs on the reference
  PC. The bar is 540 terms; the b-file has 1001 (n = 0 to 1000).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000603), CC BY-SA 4.0.
