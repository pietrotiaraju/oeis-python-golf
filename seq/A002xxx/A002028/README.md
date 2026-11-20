# A002028

> Number of connected graphs on n labeled nodes, each node being colored with one of 3 colors, such that no edge joins nodes of the same color.
> — [OEIS A002028](https://oeis.org/A002028)

Offset 0: 1, 3, 6, 42, 618, 15990, 668526, 43558242, 4373213298, 677307561630, 162826875512646, 61183069270120842, 36134310487980825258, 33673533885068169649830, 49646105434209446798290206, …

### Python 3 — 180 bytes

```python
from math import*
A=lambda n,k=3:k<2or sum(comb(n,r)*A(r,k-1)<<r*(n-r)for r in range(n+1))
L=[]
while[print(a:=A(n:=len(L))-sum(comb(n,k)*k*L[k]//n*A(n-k)for k in range(n)))]:L+=a,
```

**How it works**

- **All coloured graphs.** Let Aₖ(n) count the graphs on n labelled nodes
  together with a colouring by k colours in which no edge joins two nodes
  of one colour. Put the n − r nodes of the last colour aside: they may be
  joined to the other r nodes in any of 2^(r(n−r)) ways and not among
  themselves, and the r nodes carry a graph coloured with the other
  k − 1 colours. So Aₖ(n) = Σᵣ C(n,r)·2^(r(n−r))·Aₖ₋₁(r) with A₁(n) = 1,
  which is the lambda: `k<2or` returns True (1) at one colour, and the
  default `k=3` gives A(n) = A₃(n) for three colours.
- **Connected parts.** The coloured graphs counted by A(n) are exactly the
  sets of connected coloured graphs on disjoint label sets (a colouring of
  a graph is proper when it is proper on each component). Sort them by the
  size k of the component of node 1: A(n) = Σₖ₌₁ⁿ C(n−1,k−1)·a(k)·A(n−k),
  the logarithmic transform. Solving for the k = n term,
  a(n) = A(n) − Σₖ₌₁ⁿ⁻¹ C(n−1,k−1)·a(k)·A(n−k).
- **One list.** As in [A001187](../../A001xxx/A001187/), C(n−1,k−1) is
  written k·C(n,k)/n: the k = 0 term then vanishes, so `L[0]` can hold a(0)
  and `range(n)` covers the sum; `comb(n,k)*k*L[k]//n` is an exact
  division, and at n = 0 the sum is empty, so `//n` never sees a zero.
  The loop's `k` is its own name: `A(n-k)` still takes the default colour
  count.
- At n = 0 the formula gives A(0) = 1 with an empty sum, the OEIS value
  a(0) = 1; a(1) = A(1) = 3.

**Notes**

- Exact integers, so the program is right for every n. The recursion is
  not cached: each A(n) costs about n^2/2 calls, and all 51 terms of the
  b-file (n = 0 to 50) take about 0.3 s on a slow PC; the bar is the whole
  b-file.
- [A002027](../A002027/) is the two-colour case, with A₂ written out as one
  sum; [A002030](../A002030/) has five colours.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 180 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002028), CC BY-SA 4.0.
