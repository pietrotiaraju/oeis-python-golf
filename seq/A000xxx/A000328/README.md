# A000328

> Number of points of norm <= n^2 in square lattice.
> — [OEIS A000328](https://oeis.org/A000328)

Offset 0: 1, 5, 13, 29, 49, 81, 113, 149, 197, 253, 317, 377, 441, 529, 613, …

### Python 3 — 77 bytes

```python
n=0
while r:=range(n,1-n):print(sum(x*x+y*y<=n*n for x in r for y in r));n-=1
```

**How it works**

- a(n) counts the integer points (x, y) with x² + y² ≤ n², all of which lie
  in the square −n ≤ x, y ≤ n. The program walks that whole square and adds
  1 (a `True`) for every point inside the disc.
- The counter runs downwards, n = 0, −1, −2, …, so the square's side is
  `range(n,1-n)`, a byte under `range(-n,n+1)` for an upward counter; n·n is
  the same either way.
- The range is named in the loop condition (it is never empty, since it
  always contains 0), and the same `r` serves for x and y.

**Notes**

- Exact integer comparisons, so every term is right.
- Faster but longer: one column at a time with `math.isqrt`,
  `4*sum(isqrt(n*n-x*x)for x in range(n))+1` (a quarter disc with x ≥ 0,
  y ≥ 1, four times, plus the origin) is 81 bytes and prints the whole
  b-file in under a minute. Counting a quarter by brute force with
  `x*x+~y*~y<=n*n` over `range(n+1)` is 4 times faster but 81 bytes, and
  the upward counter with `range(-n,n+1)` is 78.
- Term n checks (2n + 1)² points, so the program prints about 520 terms
  (n ≈ 520) in 60 s. The bar is 400 terms; the b-file has 10001 (n = 0 to
  10000).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 77 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000328), CC BY-SA 4.0.
