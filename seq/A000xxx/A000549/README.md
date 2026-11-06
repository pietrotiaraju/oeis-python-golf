# A000549

> Numbers that are the sum of 2 squares but not sum of 3 nonzero squares.
> — [OEIS A000549](https://oeis.org/A000549)

Offset 1: 1, 2, 4, 5, 8, 10, 13, 16, 20, 25, …

### Python 3 — 186 bytes

```python
from math import*
n=0
while 1:
 n+=1;r=range(1,isqrt(n)+1)
 if any(isqrt(n-x*x)**2==n-x*x for x in r)and all(isqrt(n-x*x-y*y)**2!=n-x*x-y*y for x in r for y in r if 0<n-x*x-y*y):print(n)
```

**How it works**

- Scan positive n. The first test asks whether n−x² is a square for
  some positive x; the second coordinate may be zero, as permitted in
  the sum-of-two-squares condition.
- The second test rejects n exactly when there are positive x,y with
  n−x²−y² a positive square. Restricting the residual to positive values
  enforces all three nonzero coordinates.
- Every coordinate lies in 1,…,floor(√n), so the loops cover every
  possible representation. `isqrt` makes the square tests exact.

**Notes**

- This follows the definition directly, without assuming the empirical
  generating function mentioned in OEIS.
- Exhaustive testing grows with n; the bar is the first 30 terms.
- The reference file contains 113 terms from the OEIS b-file; the verification
  bar is 30 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 186 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000549), CC BY-SA 4.0.
