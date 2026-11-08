# A000949

> Number of forests with n nodes and height at most 2.
> — [OEIS A000949](https://oeis.org/A000949)

Offset 0: 1, 1, 3, 16, 101, 756, 6607, 65794, 733833, 9046648, 121961051, …

### Python 3 — 113 bytes

```python
f=lambda m,p=1,h=3,c=1:sum(f(i:=m-j,j,h-1)*(c:=c*p*i//j)for j in range(1,m*h))or m<2
n=1
while[print(+f(n))]:n+=1
```

**How it works**

- The nodes are labeled: the entry's e.g.f. is
  exp(x·exp(x·exp(x))). The height is the number of edges
  on the longest root-to-leaf path. Sort the nodes by depth: levels of
  sizes k₀, k₁, …, k₂ with sum n. The
  labels are split among the levels in n!/(k₀!·k₁!·…) ways and every node
  on level i + 1 picks its parent on level i in k_i^(k_(i+1)) ways, so
  a(n) = Σ n!/(k₀!·k₁!·…)·∏ k_i^(k_(i+1)).
- `f(m,p,h)` adds the levels one at a time: m − 1 nodes are still to be
  placed, the last level placed has p nodes, and h levels are still
  allowed. The next level takes j ≥ 1 of the remaining nodes in
  C(m−1, j)·p^j ways, so f(m, p, h) = Σⱼ C(m−1, j)·p^j·f(m−j, j, h−1),
  and nothing left (m = 1) counts once. The top call has p = 1, a virtual
  super-root that every root hangs from in 1 way, and h = 3 levels.
- `c` builds C(m−1, j)·p^j on the fly: c ← c·p·(m−j)/j, an exact division
  because the numerator is j times the next value. The walrus inside the
  comprehension binds `c` in the lambda's own scope and `c=1` is a
  default argument, so each call starts its own c at 1; this is 14 bytes
  under `import math` and `math.comb(m-1,j)*p**j`. `i:=m-j` in the call
  saves writing `m-j` twice.
- `range(1,m*h)` is empty when h = 0, so the call returns `m<2`: right
  only if no node is left. For h ≥ 1 it runs past j = m − 1, but at
  j = m the factor m − j is 0, c stays 0 from there on, and those calls
  (with i ≤ 0) return at once. This is 2 bytes under `h and` in front
  with `range(1,m)`.
- The same program with only h (and the first index) changed counts the
  other heights: [A000950](../A000950/) (h = 4) and [A000951](../A000951/) (h = 5).
- At n = 0 the top call has an empty sum and returns `m<2`, which is
  `True`; `+f(n)` prints it as 1. From n = 1 on the sums are not empty
  and give ints.

**Notes**

- Exact integer arithmetic, and the recursion visits every sequence of
  level sizes (about n²/2 of them for n nodes, each with a loop of length
  up to 3n): the b-file (101 terms,
  a(0) to a(100)) prints in about 7 s and 162 terms in 60 s here; the bar
  is the whole b-file.
- The `p**~-m` base (the last allowed level takes all remaining nodes)
  with `h and` and h = 2 is faster but 7 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000949), CC BY-SA 4.0.
