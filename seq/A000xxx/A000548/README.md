# A000548

> Squares that are not the sum of 2 nonzero squares.
> — [OEIS A000548](https://oeis.org/A000548)

Offset 1: 1, 4, 9, 16, 36, 49, 64, 81, 121, 144, …

### Python 3 — 99 bytes

```python
from math import*
n=0
while n:=n+1:
 if all(isqrt(t:=n*n-k*k)**2!=t for k in range(1,n)):print(n*n)
```

**How it works**

- Test squares n² in increasing order. A representation as two nonzero
  squares exists exactly when n²−k² is a positive square for some
  k=1,…,n−1.
- `isqrt(m)**2==m` is an exact square test. The `all` condition retains
  the candidate only when every positive first coordinate fails.
- This excludes axis representations such as n²=n²+0² by construction.
  Each square is considered once, so the output is increasing.

- The assignment `t:=n*n-k*k` reuses the same exact residual
  on both sides of the square test. Incrementing n in the while
  condition visits precisely 1,2,3,… before testing each square.

**Notes**

- The search is exhaustive and uses no floating point square roots.
- Its work grows with the square root of each candidate. The bar is the
  first 300 qualifying squares rather than a claim of constant-time testing.
- The reference file contains 1000 terms from the OEIS b-file; the verification
  bar is 300 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 103 | first entry |
| 2026-11-06 | Python 3 | 99 | reuse the square residual and increment in the loop condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000548), CC BY-SA 4.0.
