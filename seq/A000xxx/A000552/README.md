# A000552

> Number of labeled rooted trees of height 3 with n nodes.
> — [OEIS A000552](https://oeis.org/A000552)

Offset 4: 24, 300, 3360, 38850, 475776, 6231960, 87530400, 1316954430, 21173760960, 362670636900, …

### Python 3 — 135 bytes

```python
from math import*
f=lambda n,p,h:sum(comb(n,k)*p**k*f(n-k,k,h-1)for k in range(1,n+1))if h else n<1
n=4
while[print(n*f(n-1,1,3))]:n+=1
```

**How it works**

- Choose the root in n ways and group the remaining labeled
  vertices by their distance from it. Height exactly 3 means
  there are 3 nonempty layers after the root.
- Let f(m,p,h) count ways to place m remaining labels in h
  nonempty layers, given p possible parents in the preceding layer.
  Choose k labels for the next layer in C(m,k) ways; each of
  those vertices chooses one of the p parents independently,
  giving p^k choices.
- The remaining labels form h−1 layers whose first parent set
  has size k. Thus

  **f(m,p,h)=Σₖ₌₁ᵐ C(m,k)pᵏf(m−k,k,h−1)**.

- With no layers left, there is one completion exactly when no
  labels remain: `m<1` supplies that boolean base case. Choosing
  k≥1 at every other step enforces nonempty layers and therefore
  the requested exact height.
- Every nonroot vertex has one parent in the preceding layer,
  so the construction is connected and cannot contain a cycle.
  Conversely, every rooted tree determines its unique distance
  layers and all these parent choices, preventing overcounting.
- Print `n*f(n-1,1,3)`: the initial parent set is the single
  chosen root. Starting at n=4 gives the OEIS offset and the
  first value (4)!, the labeled path rooted at its end.

**Notes**

- Exact finite sums and integer powers. The recursion has fixed
  depth 3; it enumerates positive layer sizes and keeps no
  table of earlier tree counts. For fixed height, the number of
  layer-size choices grows polynomially with n.
- Large outputs eventually meet Python's integer conversion limit.
- The reference file has 16 terms. Its unchanged
  verification bar is the complete file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 179 | first entry |
| 2026-11-06 | Python 3 | 135 | count nonempty distance layers directly |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000552), CC BY-SA 4.0.
