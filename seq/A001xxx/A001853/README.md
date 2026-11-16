# A001853

> Total height of trees with n nodes.
> — [OEIS A001853](https://oeis.org/A001853)

Offset 1: 0, 1, 3, 8, 22, 58, 158, 425, 1161, 3175, 8751, 24192, 67239, …

### Python 3 — 151 bytes

```python
T=[P:=[n:=0,1]]
while[print(sum(P[-1]-L[-1]for L in T))]:
 n-=1;T+=P[:],;P=-n*[0,0]
 for L in T:L+=sum(d*P[-d]*sum(L[d::d])for d in range(n,0))//n,;P=L
```

**How it works**

- **Sum of heights by levels.** The height of a rooted tree is the largest
  distance from its root, so a(n) = Σ_{h≥0} #{trees of height > h}
  = Σ_h (r(n) − r_h(n)), where r = [A000081](../../A000xxx/A000081/) counts
  rooted trees and r_h(n) those of height at most h (Riordan 1960). Every
  tree on n nodes has height at most n − 1, so only h ≤ n − 2 contribute.
- **Height-limited trees.** The subtrees of the root form a multiset of
  trees of height at most h − 1, so R_h(x) = x·exp(Σ_k R_{h−1}(xᵏ)/k) with
  R_{−1} = 0. In coefficients this is A000081's recurrence with the level
  below as weights: (m − 1)·r_h(m) = Σ_{d, j≥1} d·r_{h−1}(d)·r_h(m − jd).
- **One list per level.** `T` holds the lists of levels h = 0, 1, …, each
  in the layout of A000081's program: the index is the node count, `n`
  counts down, `P[-d]` is r_{h−1}(|d|) and `sum(L[d::d])` reads
  r_h(m − j|d|) from the end of the list. Each pass appends the next
  coefficient to every level, bottom up, so `P` already holds the level
  below when a level is extended; below level 0 sits the zero list
  `-n*[0,0]`.
- **The top level is r.** r_h(k) = r(k) for k ≤ h + 1, so a copy of the top
  level, `T+=P[:],`, is a new level that is exact up to the current size.
  After a pass `P` is the top level, and the header prints
  Σ (top − r_h) over all levels; the top one adds 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 300 terms (n = 1 to 300); the bar is the whole b-file in
  60 s. A pass costs about n² steps, so the run grows like n³; the 300
  terms take about 16 s on this PC, 1.5–2.6 times slower than the
  reference.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 151 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001853), CC BY-SA 4.0.
