# A000573

> Number of 4 X n normalized Latin rectangles.
> — [OEIS A000573](https://oeis.org/A000573)

Offset 4: 4, 56, 6552, 1293216, 420909504, 207624560256, 147174521059584, 143968880078466048, 188237563987982390784, 320510030393570671051776, …

### Python 3 — 300 bytes

```python
from functools import*
from itertools import*
n=3
while 1:
 n+=1;Q=list(permutations(range(n)))
 @cache
 def f(r,C):
  if r==4:return 1
  return sum(f(r+1,tuple(C[j]|1<<p[j]for j in range(n)))for p in Q if p[0]==r and all(C[j]>>p[j]&1==0 for j in range(n)))
 print(f(1,tuple(1<<j for j in range(n))))
```

**How it works**

- A normalized Latin rectangle has its first row and first column in
  natural order. Start with the first row 0,1,…,n−1.
- Each further row is a permutation whose first entry is its row index.
  Column bit masks forbid any symbol already used in that column.
- `f` counts all completions, memoized by row count and column masks.
  A000573 stops after four rows; A000576 stops after n−2 rows.
- The initial n is chosen so the first output has the OEIS offset.
  No quotient by row permutations is applied: row positions are fixed.

**Notes**

- This is exhaustive Latin rectangle generation using exact counts.
  The search grows quickly; the bar covers the first three terms.
- The reference file contains 147 terms from the OEIS b-file; the verification
  bar is 3 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 300 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000573), CC BY-SA 4.0.
