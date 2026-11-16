# A001829

> Related to graded partially ordered sets.
> — [OEIS A001829](https://oeis.org/A001829)

Offset 0: 1, 6, 46, 450, 5650, 91866, 1957066, 55363650, 2109599650, 109773407466, …

### Python 3 — 150 bytes

```python
import math,functools as F
g=F.cache(lambda m,p=0,j=6:sum(math.comb(m,q)*g(m-q,q,j-1)<<p*q for q in range(m+1)if j)or m<1)
n=0
while[print(g(n))]:n+=1
```

**How it works**

- **The count.** Klarner's c(6, n): put n labeled points on 6 numbered
  levels and join points of neighbouring levels by any set of edges, so
  a(n) = Σ n!/(p₁!⋯p₆!)·2^(p₁p₂+p₂p₃+⋯) over compositions of n (Sean
  A. Irvine's formula on the OEIS page). Each choice is a labeled poset
  (the edges are its cover relations) with a rank function into 6 levels.
- **Level by level.** Let g(m, p, j) count the ways to spread m labeled
  points over j more levels when the level above holds p points: choose
  the q points of the next level (C(m, q) ways) and any edges to the p
  points above (2^(pq) ways), so
  g(m, p, j) = Σ_q C(m, q)·2^(pq)·g(m − q, q, j − 1), g(m, p, 0) = [m = 0],
  and a(n) = g(n, 0, 6).
- **The program.** `F.cache` memoizes g; the table does not depend on n, so
  all terms up to n cost O(n³) cached calls. In
  `sum(…for q in range(m+1)if j)or m<1` the `if j` empties the sum on the
  last level, where `or m<1` gives True or False (1 or 0); above it the
  sum is at least 1 (the q = m term), so the `or` never fires.
  `import math,functools as F` is 7 bytes under two `from … import*`
  lines.
- Four and five levels ([A001827](../A001827/), [A001828](../A001828/))
  are shorter as a double sum, after summing out every other level in the
  e.g.f.; with 6 levels that leaves three kept levels, and the triple sum
  is longer (168 bytes for six levels).

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(n)
  passes the 4300-digit int-to-str limit near n = 237. The recursion is
  only 6 levels deep.
- The b-file has 113 terms (n = 0 to 112); the bar is the whole b-file in
  60 s, which takes a few seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 150 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001829), CC BY-SA 4.0.
