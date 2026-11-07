# A000606

> Number of nonnegative solutions to x^2 + y^2 + z^2 <= n.
> — [OEIS A000606](https://oeis.org/A000606)

Offset 0: 1, 4, 7, 8, 11, 17, 20, 20, 23, 29, 35, 38, 39, 45, 51, …

### Python 3 — 89 bytes

```python
n=0
while r:=range(n,1):print(sum(x*x+y*y+z*z<=-n for x in r for y in r for z in r));n-=1
```

**How it works**

- a(n) counts the points (x, y, z) with x, y, z ≥ 0 and x² + y² + z² ≤ n.
  Every such coordinate is at most √n ≤ n, so the cube 0 ≤ x, y, z ≤ n holds
  them all; the program walks it and adds 1 for every point inside the ball.
- Same template as [A000604](../A000604/): a downward counter
  n = 0, −1, −2, …, with `range(n,1)` (n, …, 0, the same squares as
  0, …, |n|) named once in the loop condition. The bound is now the counter
  itself, so the test reads `<=-n`.

**Notes**

- Exact integer comparisons, so every term is right.
- The cube side |n| + 1 is far more than the ⌊√n⌋ + 1 needed, but a tighter
  range costs bytes. Term n checks (n + 1)³ points, so the program printed 144 to
  151 terms in 60 s in two runs on the reference PC. The bar is 110 terms; the b-file has 1001
  (n = 0 to 1000).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 89 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000606), CC BY-SA 4.0.
