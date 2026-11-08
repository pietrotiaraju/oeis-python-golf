# A001005

> Number of ways of partitioning n points on a circle into subsets only of sizes 2 and 3.
> — [OEIS A001005](https://oeis.org/A001005)

Offset 0: 1, 0, 1, 1, 2, 5, 8, 21, 42, 96, 222, 495, 1177, 2717, 6435, 15288, …

### Python 3 — 58 bytes

```python
n=1
while[print((1+(B:=4**n)*B*-~B)**n//B**~-n%B//n)]:n+=1
```

**Why the formula**

- The partitions are noncrossing (a(4) = 2, not the 3 pairings of four
  points). The block of point 1, of size k ∈ {2, 3}, splits the other
  points into k independent gaps, so G = 1 + x²G² + x³G³, and u = xG
  satisfies u = x(1 + u² + u³) (Christian Bower's formula in the entry).
- Lagrange inversion gives Wolfdieter Lang's formula from the entry:

  **a(n) = [t^n] (1 + t² + t³)^(n+1) / (n+1).**

**How it works**

- In the code `n` is m = n + 1. With B = 4^m, (1 + B² + B³)^m is the
  polynomial (1 + t² + t³)^m evaluated at t = B; its coefficients are
  nonnegative and add up to 3^m < B, so they are exactly its base-B
  digits. `//B**~-n%B` reads digit m − 1 and `//n` divides by m.
- `1+B*B*-~B` is 1 + B²(B + 1), 1 byte under `(B:=4**n)**3+B*B+1`.

**Notes**

- Exact integer arithmetic, correct for every n.
- About 420 terms in 10 s; the bar is the whole b-file (201 terms) in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001005), CC BY-SA 4.0.
