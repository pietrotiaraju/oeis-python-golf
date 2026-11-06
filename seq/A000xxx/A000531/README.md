# A000531

> From area of cyclic polygon of 2n + 1 sides.
> — [OEIS A000531](https://oeis.org/A000531)

Offset 1: 1, 7, 38, 187, 874, 3958, 17548, 76627, 330818, 1415650, …

### Python 3 — 71 bytes

```python
from math import*
n=1
while 1:print(((2*n+1)*comb(2*n,n)-4**n)//2);n+=1
```

**How it works**

- The OEIS formula is ((2n+1)!/(n!)²−4^n)/2. Since
  (2n+1)!/(n!)²=(2n+1)C(2n,n), one binomial coefficient supplies the
  factorial quotient directly.
- n begins at 1, giving (3·2−4)/2=1. `//2` is exact because the central
  binomial coefficient is even for every positive n.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 100 terms from the OEIS b-file; the verification
  bar is 100 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000531), CC BY-SA 4.0.
