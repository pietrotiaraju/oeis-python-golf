# A000604

> Number of nonnegative solutions to x^2 + y^2 + z^2 <= n^2.
> — [OEIS A000604](https://oeis.org/A000604)

Offset 0: 1, 4, 11, 29, 54, 99, 163, 239, 344, 486, 648, 847, 1069, 1355, 1680, …

### Python 3 — 90 bytes

```python
n=0
while r:=range(n,1):print(sum(x*x+y*y+z*z<=n*n for x in r for y in r for z in r));n-=1
```

**How it works**

- a(n) counts the points (x, y, z) with x, y, z ≥ 0 and x² + y² + z² ≤ n²,
  all inside the cube 0 ≤ x, y, z ≤ n; the program walks the cube and adds 1
  for every point inside the ball.
- Same template as [A000603](../A000603/) and [A000328](../A000328/): a
  downward counter n = 0, −1, −2, …, so `range(n,1)` (n, …, 0) has the same
  squares as 0, …, |n| for a byte less, named once in the loop condition (never
  empty) and reused for x, y and z.

**Notes**

- Exact integer comparisons, so every term is right.
- Term n checks (n + 1)³ points, so the program printed 135 to 145 terms in 60 s
  in two runs on the reference PC. The bar is 105 terms; the b-file has 501
  (n = 0 to 500).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000604), CC BY-SA 4.0.
