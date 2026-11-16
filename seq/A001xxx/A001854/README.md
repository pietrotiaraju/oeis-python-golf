# A001854

> Total height of all rooted trees on n labeled nodes.
> — [OEIS A001854](https://oeis.org/A001854)

Offset 1: 0, 2, 15, 148, 1785, 26106, 449701, 8927192, 200847681, 5053782070, …

### Python 3 — 169 bytes

```python
from math import*
T=[P:=[1]];n=1
while[print(n*sum(P[-1]-L[-1]for L in T))]:
 T+=P[:],;P=n*[0]
 for L in T:L+=sum(comb(n-1,j)*-~j*P[j]*L[~j]for j in range(n)),;P=L
 n+=1
```

**How it works**

- **Sum of heights by levels.** The height of a rooted tree is the largest
  distance from its root, so a(n) = Σ_{h≥0} (nⁿ⁻¹ − r_h(n)), where nⁿ⁻¹
  counts the rooted trees on n labeled nodes and r_h(n) those of height at
  most h. Only h ≤ n − 2 contribute.
- **Height-limited trees.** Deleting the root leaves a set of rooted trees
  of height at most h − 1, so with exponential generating functions
  R_h = x·E_h and E_h = exp(R_{h−1}), R_{−1} = 0: r_h(n) = n·e_h(n − 1).
  In a forest counted by e_h(m), the tree that holds node m has j other
  nodes and r_{h−1}(j + 1) = (j + 1)·e_{h−1}(j) shapes, so
  e_h(m) = Σ_{j<m} C(m−1, j)·(j + 1)·e_{h−1}(j)·e_h(m−1−j).
- **One list per level.** `T` holds e_0, e_1, …, each as a list indexed by
  m; at the header they have n entries, e_h(0)…e_h(n−1). A pass appends
  e_h(n) to every level, bottom up, so `P` is the level below (`L[~j]` is
  e_h(n−1−j)); below level 0 sits the zero list `n*[0]`, which makes
  e_0 = 1, 0, 0, … (a single node).
- **The top level is exact.** e_h(m) = e(m) = (m+1)ᵐ⁻¹ for m ≤ h, so a copy
  of the top level, `T+=P[:],`, is a new level that is exact up to the
  current size. The header prints n·Σ (top − e_h(n−1)) over all levels.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 387 terms (n = 1 to 387). A pass costs about n² binomial
  products, so the run grows like n³: 240 terms take about 20 s on this
  PC (1.5–2.6 times slower than the reference) and 60 s give about 290, so
  the bar is 240 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 169 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001854), CC BY-SA 4.0.
