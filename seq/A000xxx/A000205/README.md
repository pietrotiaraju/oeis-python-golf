# A000205

> Number of positive integers <= 2^n of form x^2 + 3 y^2.
> — [OEIS A000205](https://oeis.org/A000205)

Offset 0: 1, 1, 3, 4, 8, 14, 25, 45, 82, 151, 282, 531, 1003, 1907, 3645, …

### Python 3 — 91 bytes

```python
n=0
while r:=range(2<<n//2):print(len({min(x*x+3*y*y,2**n+1)for x in r for y in r})-2);n+=1
```

**How it works**

- This is the [A000018](../A000018/) program with 16y² replaced by 3y².
  Signs do not matter, so x, y ≥ 0, and `range(2<<n//2)` covers every
  x, y with x² + 3y² ≤ 2ⁿ.
- `min(…,2**n+1)` folds every value above 2ⁿ into the single value 2ⁿ + 1,
  which is always in the set because the largest y in the range gives
  3y² > 2ⁿ. The set holds 0, that cap, and each positive value ≤ 2ⁿ once,
  so `-2` leaves a(n).
- The cap cannot be 2ⁿ itself (with `-1`): 2ⁿ is of the form only for even n.
  For odd x, y, x² + 3y² ≡ 4 (mod 8), so x² + 3y² = 2ⁿ with n ≥ 3 forces
  x, y even and the exponent drops by 2 down to 2 = x² + 3y², which has
  no solution.

**Notes**

- These are the Loeschian numbers ([A003136](https://oeis.org/A003136)):
  with u = (x+y)/2, v = (x−y)/2, a form x² + xy + y² with x, y both odd
  becomes 3u² + v², and with x or y even it becomes (x + y/2)² + 3(y/2)²
  directly. `x*x+x*y+y*y` is 2 bytes longer than `x*x+3*y*y`, though.
- Term n runs through 4^(⌊n/2⌋+1) pairs; the program prints a(0)…a(23) in
  about 36 s (CPython 3.12). The bar is 24 terms in 60 s; the b-file goes
  to n = 45.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 91 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000205), CC BY-SA 4.0.
