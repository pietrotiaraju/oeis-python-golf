# A000605

> Number of points of norm <= n in cubic lattice.
> — [OEIS A000605](https://oeis.org/A000605)

Offset 0: 1, 7, 33, 123, 257, 515, 925, 1419, 2109, 3071, 4169, 5575, 7153, 9171, 11513, …

### Python 3 — 92 bytes

```python
n=0
while r:=range(n,1-n):print(sum(x*x+y*y+z*z<=n*n for x in r for y in r for z in r));n-=1
```

**How it works**

- a(n) counts all integer points (x, y, z) with x² + y² + z² ≤ n² (any signs),
  all inside the cube −n ≤ x, y, z ≤ n; the program walks the cube and adds 1
  for every point inside the ball.
- The counter runs downwards, n = 0, −1, −2, …, so the cube's side is
  `range(n,1-n)`, two bytes under `range(-n,n+1)`; n·n is the same either way.
  The range is named in the loop condition (it always contains 0) and reused
  for x, y and z: the 3-D version of [A000328](../A000328/), and the all-signs
  version of [A000604](../A000604/).

**Notes**

- Exact integer comparisons, so every term is right.
- Term n checks (2n + 1)³ points, so the program printed 83 to 88 terms in 60 s
  in two runs on the reference PC. The bar is 64 terms; the b-file has 10001
  (n = 0 to 10000).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000605), CC BY-SA 4.0.
