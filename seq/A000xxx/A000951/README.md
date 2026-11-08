# A000951

> Number of forests with n nodes and height at most 4.
> — [OEIS A000951](https://oeis.org/A000951)

Offset 1: 1, 3, 16, 125, 1296, 16087, 229384, 3687609, 66025360, 1303751051, …

### Python 3 — 112 bytes

```python
f=lambda m,p=1,h=5,c=1:sum(f(i:=m-j,j,h-1)*(c:=c*p*i//j)for j in range(1,m*h))or m<2
n=2
while[print(f(n))]:n+=1
```

**How it works**

- The nodes are labeled: the entry's e.g.f. is
  exp(x·exp(x·exp(x·exp(x·exp(x))))). The height is the number of edges
  on the longest root-to-leaf path. Sort the nodes by depth: levels of
  sizes k₀, k₁, …, k₄ with sum n. The
  labels are split among the levels in n!/(k₀!·k₁!·…) ways and every node
  on level i + 1 picks its parent on level i in k_i^(k_(i+1)) ways, so
  a(n) = Σ n!/(k₀!·k₁!·…)·∏ k_i^(k_(i+1)).
- `f(m,p,h)` adds the levels one at a time: m − 1 nodes are still to be
  placed, the last level placed has p nodes, and h levels are still
  allowed. The next level takes j ≥ 1 of the remaining nodes in
  C(m−1, j)·p^j ways, so f(m, p, h) = Σⱼ C(m−1, j)·p^j·f(m−j, j, h−1),
  and nothing left (m = 1) counts once. The top call has p = 1, a virtual
  super-root that every root hangs from in 1 way, and h = 5 levels.
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
  other heights: [A000949](../A000949/) (h = 3) and [A000950](../A000950/) (h = 4).
- Offset 1: the loop starts at n = 1, that is m = 2.

**Notes**

- Exact integer arithmetic. The recursion visits every sequence of level
  sizes (about n⁴/24 of them for n nodes, each with a loop of length up to
  5n), so it slows down quickly:
  53 terms in 60 s here (the b-file has 100); the bar is 41 terms.
- Remembering f with `functools.cache` makes it polynomial but costs about
  30 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 112 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000951), CC BY-SA 4.0.
