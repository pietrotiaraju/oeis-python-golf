# A000532

> Number of Hamiltonian paths from NW to SW corners in an n X n grid.
> — [OEIS A000532](https://oeis.org/A000532)

Offset 1: 1, 1, 2, 8, 86, 1770, 88418, 8934966, 2087813834, 1013346943033, …

### Python 3 — 232 bytes

```python
from functools import*
n=0
while 1:
 n+=1
 @cache
 def f(v,S):
  if v==n*(n-1):return int(S==(1<<(n*n))-1)
  return sum(f(w,S|1<<w)for w in(v-n,v+n,v-1,v+1)if 0<=w<n*n and abs(w//n-v//n)+abs(w%n-v%n)==1 and S>>w&1==0)
 print(f(0,1))
```

**How it works**

- Number grid vertices row by row. The northwest corner is 0 and the
  southwest corner is n(n−1). `S` is the bit mask of visited vertices.
- The recursive search extends the path to every unvisited grid neighbor.
  The Manhattan-distance check prevents a horizontal step from wrapping
  around a row boundary.
- Reaching the target counts only if every one of the n² vertices was
  visited. Otherwise it returns zero, since a Hamiltonian path cannot
  revisit its endpoint later. The 1×1 grid has the single empty path.
- `cache` merges subproblems with the same endpoint and visited set.

**Notes**

- The count is exhaustive for each grid size, and no reversal factor
  is needed because the two endpoints are fixed.
- The visited-set state space is exponential; the bar covers sizes 1–5.
- The reference file contains 21 terms from the OEIS b-file; the verification
  bar is 5 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 232 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000532), CC BY-SA 4.0.
