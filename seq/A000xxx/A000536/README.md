# A000536

> Number of 3-line Latin rectangles.
> — [OEIS A000536](https://oeis.org/A000536)

Offset 4: 24, 240, 2520, 26880, 304080, 3671136, 47391120, 653463360, 9603708840, 150046937040, …

### Python 3 — 77 bytes

```python
a,b,n=1,2,4
while[print(n*(n-1)*((n-3)*b+(n-2)*a)//2)]:a,b=b,(n-1)*(a+b);n+=1
```

**How it works**

- Let D_m count derangements of m elements. Then D₂=1, D₃=2
  and D_m=(m−1)(D_(m−1)+D_(m−2)). Only two consecutive values
  are needed, stored as a=D_(n−2) and b=D_(n−1).
- The K(n,j) recurrence given in the OEIS entry is
  K(n,0)=D_n and
  jK(n,j)=n(n+1−2j)K(n−1,j−1)+n(n−1)K(n−2,j−1).
  At j=1 it gives
  K(n,1)=n(n−1)(D_(n−1)+D_(n−2))=nD_n.
- Substituting that identity at j=2 yields
  **K(n,2)=n(n−1)((n−3)D_(n−1)+(n−2)D_(n−2))/2**.
  This is the expression printed by the program, beginning at n=4.
  No recursive K table or memoization is required.
- After printing, the simultaneous assignment advances a,b to
  D_(n−1),D_n before n increases. At n=4 the expression is
  4·3·(1·2+2·1)/2=24, the first reference value.

**Notes**

- All arithmetic is exact; the factor n(n−1) is even, so the
  final division by 2 is exact. Two derangement values are retained
  regardless of n, apart from their growing integer sizes.
- Python's integer-to-string conversion limit can eventually apply.
- The reference file contains 30 terms. The unchanged verification
  bar is 15 terms in 60 s; all 30 also match this program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 193 | first entry |
| 2026-11-06 | Python 3 | 77 | reduce the K(n,2) recurrence to two consecutive derangements |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000536), CC BY-SA 4.0.
