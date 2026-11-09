# A001188

> Number of even graphs with n edges.
> — [OEIS A001188](https://oeis.org/A001188)

Offset 1: 1, 2, 8, 60, 672, 9953, 184557, 4142631, 109813842, 3373122370, 118280690398, 4678086540493, 206625802351035, 10107719377251109, 543762148079927802, 31975474310851749920, …

### Python 3 — 158 bytes

```python
from math import*
r=[s:=1];G=[1];C=[]
while 1:n=len(C);C+=s*s-sum(comb(n,i)*C[i]*G[n-i]for i in range(n)),;G+=s*s,;r=[s]+[s:=s+x for x in r];print(C[-1]+1>>1)
```

**How it works**

- "Even graph" is the old name for a bipartite graph (every cycle even).
  The terms count connected bipartite multigraphs with n labelled edges
  (vertices unlabelled, none isolated): a(2) = 2 (a path, a double edge),
  a(3) = 8 (a triple edge 1, paths 3, a star 1, a double edge with a
  pendant edge 3). This is the count behind S. A. Irvine's Maple program
  in the entry, e.g.f. (eˣ − 1 + log Σₖ Bₖ²·xᵏ/k!)/2, which reproduces
  R. W. Robinson's 50 terms (E. N. Gilbert, *Enumeration of labelled
  graphs*, 1956).
- Why: a pair (P, Q) of set partitions of the n edges is a bipartite
  multigraph with its two sides marked. The blocks of P are the left
  vertices, the blocks of Q the right ones, and edge e joins its P-block
  to its Q-block. There are Bₙ² pairs, so the connected ones (the join of
  P and Q is one block) number c(n) = n!·[xⁿ] log Σₖ Bₖ²·xᵏ/k!. Swapping the
  sides gives each connected graph twice, except the one with
  P = Q = {all edges} (n parallel edges), so a(n) = (c(n) + 1)/2.
- The Bell numbers come from the Bell triangle: `r=[s]+[s:=s+x for x in r]`
  turns a row into the next, and `s` is always the last entry, the next
  Bell number. `G` holds Bₖ² from k = 0 on, `C` holds c(1), c(2), ….
- The logarithm is the usual recurrence
  c(N) = g(N) − Σₖ₌₁ᴺ⁻¹ C(N−1,k−1)·c(k)·g(N−k) with g(k) = Bₖ²; here `n` is
  N − 1 and `G[n-i]` is g(N−1−i). The new square `s*s` is used before it
  joins `G`.

**Notes**

- `C[-1]+1>>1` is the halving (c(N) is odd). Exact integers; the 50 terms
  of the b-file print at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 158 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001188), CC BY-SA 4.0.
