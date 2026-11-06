# A000592

> Number of nonnegative solutions of x^2 + y^2 = z in first n shells.
> — [OEIS A000592](https://oeis.org/A000592)

Offset 0: 1, 3, 4, 6, 8, 9, 11, 13, 15, 17, …

### Python 3 — 116 bytes

```python
from math import*
n=a=0
while 1:
 r=sum(isqrt(n-x*x)**2==n-x*x for x in range(isqrt(n)+1))
 if r:a+=r;print(a)
 n+=1
```

**How it works**

- For each squared radius n, count ordered nonnegative lattice points
  on x²+y²=n. Once x is fixed, the second coordinate exists exactly when
  n−x² is a square; `isqrt` decides this exactly.
- Add this count to the running total and print only for nonempty
  shells. Thus the argument is the shell number, rather than every
  integer radius. This distinction gives 1,3,4,6,8,… as required.
- The origin forms the first shell and contributes the initial 1.
  Pairs (x,y) and (y,x) are counted separately when they differ.

**Notes**

- All nonnegative solutions are covered, including coordinates equal
  to zero. No floating point geometry is used.
- The reference file contains 2750 terms from the OEIS b-file; the verification
  bar is 2750 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000592), CC BY-SA 4.0.
