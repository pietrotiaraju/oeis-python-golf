# A000483

> Associated Stirling numbers: second-order reciprocal Stirling numbers (Fekete) a(n) = [[n, 3]]. The number of 3-orbit permutations of an n-set with at least 2 elements in each orbit.
> — [OEIS A000483](https://oeis.org/A000483)

Offset 6: 15, 210, 2380, 26432, 303660, 3678840, 47324376, 647536032, 9418945536, 145410580224, …

### Python 3 — 142 bytes

```python
from math import*
A=[[1,0,0,0],[0,0,0,0]];n=1
while 1:
 n+=1;A+=[[0]+[(n-1)*(A[-1][k]+A[-2][k-1])for k in range(1,4)]]
 if n>5:print(A[-1][3])
```

**How it works**

- Let b(n,k) count permutations of n elements with k cycles,
  every cycle having length at least 2. To include the new element,
  either insert it into an existing cycle in n−1 possible places,
  or pair it with one of n−1 elements as a new 2-cycle. Hence

  **b(n,k)=(n−1)(b(n−1,k)+b(n−2,k−1)).**

- The empty permutation gives b(0,0)=1. There are no permitted
  permutations on one element, so the first two rows are
  `[1,0,0,0]` and `[0,0,0,0]`, columns k=0 through 3.
- At each pass increment n, then compute its row from `A[-1]`
  and `A[-2]`. The prefixed zero is b(n,0); the comprehension
  constructs columns k=1,2,3 using only the two preceding rows.
- Three nontrivial cycles need at least six elements. `if n>5`
  skips the earlier zeros, and `A[-1][3]` prints the desired column.
  At n=6 every cycle is a pair, so a(6)=6!/(2³3!)=15.

**Notes**

- This counts cycles of permutations, with their cyclic ordering,
  rather than just set-partition blocks. The minimum cycle length
  rules out fixed points entirely; compare [A000454](../A000454/)
  and [A000482](../A000482/) for ordinary first-kind columns.
- Exact integer recurrence. A stores four entries per generated row,
  although the update reads only the last two rows. Thus storage grows
  linearly with n and each row uses three recurrence evaluations.
- Factorial growth eventually reaches Python 3.11+'s default
  4300-digit output conversion limit, an interpreter limit.
- The b-file has 195 terms (indices 6 through 200). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 142 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000483), CC BY-SA 4.0.
