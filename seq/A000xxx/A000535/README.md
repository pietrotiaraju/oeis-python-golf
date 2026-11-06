# A000535

> Card matching: coefficients B[n,2] of t^2 in the reduced hit polynomial A[n,n,n](t).
> — [OEIS A000535](https://oeis.org/A000535)

Offset 1: 0, 27, 378, 4536, 48600, 489780, 4738104, 44535456, 409752432, 3708359550, …

### Python 3 — 141 bytes

```python
from math import comb as C
n=1
while 1:print(3*sum(C(n,2)*C(n,k+2)*C(n,k)*C(n-2,k)+n*n*C(n,k+1)*C(n-1,k+1)*C(n-1,k)for k in range(n-1)));n+=1
```

**How it works**

- Evaluate the two finite binomial sums given in the OEIS entry for
  B[n,2]. Both run over k=0,…,n−2, so their summands can be
  added inside one sum and the common factor 3 taken outside.
  The first retains its factor C(n,2), the second its factor n².
  Import `comb` as C to shorten the repeated exact binomials.
- At n=1 both ranges are empty, so the required first value is 0.
  Thereafter all binomial arguments are nonnegative and `comb` evaluates
  each term exactly.
- This extracts the fixed card-matching coefficient directly instead of
  constructing the full reduced hit polynomial.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 20 terms from the OEIS b-file; the verification
  bar is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 179 | first entry |
| 2026-11-06 | Python 3 | 141 | combine the two finite sums and alias comb |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000535), CC BY-SA 4.0.
