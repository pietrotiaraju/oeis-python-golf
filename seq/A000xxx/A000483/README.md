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

For permutations with no fixed points and exactly k cycles,
the associated first-kind Stirling recurrence is
b(n,k)=(n-1)*(b(n-1,k)+b(n-2,k-1)).
Either insert the new element into a cycle of a permutation
of n-1 elements, or pair it with one of n-1 other elements
as a new 2-cycle. The seed b(0,0)=1 supplies the empty
permutation; all other entries at n=0,1 are zero.
Keep columns 0..3 and print the third column from n=6.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 195 terms in 60 s; the official b-file contains 195 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 142 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000483), CC BY-SA 4.0.
