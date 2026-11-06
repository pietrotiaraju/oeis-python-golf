# A000536

> Number of 3-line Latin rectangles.
> — [OEIS A000536](https://oeis.org/A000536)

Offset 4: 24, 240, 2520, 26880, 304080, 3671136, 47391120, 653463360, 9603708840, 150046937040, …

### Python 3 — 193 bytes

```python
from functools import*
@cache
def f(n,j):return n*f(n-1,0)+(-1)**n if j==0 and n else (n*(n+1-2*j)*f(n-1,j-1)+n*(n-1)*f(n-2,j-1))//j if n>=2*j>0 else int(n==j==0)
n=4
while 1:print(f(n,2));n+=1
```

**How it works**

- Use the K(n,j) recurrence specified by Sean A. Irvine in the OEIS
  entry: K(n,0)=nK(n−1,0)+(−1)^n and
  jK(n,j)=n(n+1−2j)K(n−1,j−1)+n(n−1)K(n−2,j−1).
- The boundary K(0,0)=1 starts the derangement column. Terms with
  n<2j vanish. The requested sequence is K(n,2), from n=4.
- `cache` retains the lower-column values needed by later terms. The
  division by j is exact by the recurrence.

**Notes**

- All counts are exact integers. The recursion and integer conversion
  limits can eventually be reached, as allowed by the repository rules.
- The reference file contains 30 terms from the published OEIS entry; the verification
  bar is 15 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 193 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000536), CC BY-SA 4.0.
