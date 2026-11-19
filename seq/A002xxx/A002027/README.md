# A002027

> Number of connected graphs on n labeled nodes, each node being colored with one of 2 colors, such that no edge joins nodes of the same color.
> — [OEIS A002027](https://oeis.org/A002027)

Offset 0: 1, 2, 2, 6, 38, 390, 6062, 134526, 4172198, 178449270, 10508108222, 853219059726, 95965963939958, 15015789392011590, 3282145108526132942, 1005193051984479922206, 432437051675617901246918, …

### Python 3 — 161 bytes

```python
from math import*
A=lambda n:sum(comb(n,r)<<r*(n-r)for r in range(n+1))
L=[]
while[print(a:=A(n:=len(L))-sum(comb(n,k)*k*L[k]//n*A(n-k)for k in range(n)))]:L+=a,
```

**How it works**

- **All coloured graphs.** Colour the n labelled nodes with two colours,
  r nodes with the first: C(n,r) ways. Only the r·(n−r) pairs of nodes
  with different colours may be edges, each present or not, so the
  coloured graphs number A(n) = Σᵣ C(n,r)·2^(r(n−r))
  ([A047863](https://oeis.org/A047863)); `comb(n,r)<<r*(n-r)` multiplies
  by the power of two with a shift.
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
  `n:=len(L)` is bound in `A(n:=len(L))`, before the generator runs.
- At n = 0 the formula gives A(0) = 1 with an empty sum, the OEIS value
  a(0) = 1 (e.g.f. log A(x) + 1). At n = 1, a(1) = A(1) = 2: one node, two
  colours.

**Notes**

- Exact integers, so the program is right for every n. The b-file (n = 0
  to 50) prints in well under a second; the bar is all 51 terms.
- The same template with k colours gives [A002028](../A002028/) (3),
  [A002029](../A002029/) (4) and [A002030](../A002030/) (5);
  [A002031](../A002031/) is this sequence from n = 2.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 161 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002027), CC BY-SA 4.0.
