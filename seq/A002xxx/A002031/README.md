# A002031

> Number of labeled connected digraphs on n nodes where every node has indegree 0 or outdegree 0 and no isolated nodes.
> — [OEIS A002031](https://oeis.org/A002031)

Offset 2: 2, 6, 38, 390, 6062, 134526, 4172198, 178449270, 10508108222, 853219059726, 95965963939958, 15015789392011590, 3282145108526132942, 1005193051984479922206, 432437051675617901246918, …

### Python 3 — 164 bytes

```python
from math import*
A=lambda n:sum(comb(n,r)<<r*(n-r)for r in range(n+1))
L=[1,2]
while[print(a:=A(n:=len(L))-sum(comb(n,k)*k*L[k]//n*A(n-k)for k in range(n)))]:L+=a,
```

**How it works**

- **Sources and sinks.** In such a digraph no node is isolated, so each
  node is a source (outdegree > 0, indegree 0) or a sink (indegree > 0,
  outdegree 0), and every arc runs from a source to a sink. Colour the
  sources and the sinks with two colours and forget the directions: this
  is a connected graph whose edges join nodes of different colours. Back
  again, orient each edge from the first colour to the second; for n ≥ 2 a
  connected graph has no isolated node, so each node gets the role of its
  colour. Hence a(n) = [A002027](../A002027/)(n) for n ≥ 2, and the
  program is that one started at n = 2.
- **Coloured graphs and the logarithm.** Two-coloured graphs on n labelled
  nodes number A(n) = Σᵣ C(n,r)·2^(r(n−r)) (choose the r nodes of the
  first colour, then any set of the r(n−r) bichromatic pairs), and the
  connected ones c(n) satisfy A(n) = Σₖ₌₁ⁿ C(n−1,k−1)·c(k)·A(n−k) (size k
  of the component of node 1), so
  c(n) = A(n) − Σₖ₌₁ⁿ⁻¹ C(n−1,k−1)·c(k)·A(n−k).
- **Start at n = 2.** `L=[1,2]` holds c(0) = 1 and c(1) = 2, so the first
  pass computes n = len(L) = 2. With C(n−1,k−1) written k·C(n,k)/n the
  k = 0 term vanishes and `range(n)` covers the sum
  (`comb(n,k)*k*L[k]//n` is exact); `comb(n,r)<<r*(n-r)` is the power of
  two as a shift.

**Notes**

- Exact integers, so the program is right for every n. The b-file has
  99 terms (n = 2 to 100) and they print in under a second; the bar is
  the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 164 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002031), CC BY-SA 4.0.
