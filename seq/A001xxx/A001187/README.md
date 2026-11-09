# A001187

> Number of connected labeled graphs with n nodes.
> — [OEIS A001187](https://oeis.org/A001187)

Offset 0: 1, 1, 1, 4, 38, 728, 26704, 1866256, 251548592, 66296291072, 34496488594816, 35641657548953344, 73354596206766622208, 301272202649664088951808, 2471648811030443735290891264, 40527680937730480234609755344896, …

### Python 3 — 121 bytes

```python
from math import*
L=[]
while[print(a:=2**comb(n:=len(L),2)-sum(comb(n,k)*k*L[k]//n<<comb(n-k,2)for k in range(n)))]:L+=a,
```

**How it works**

- Sort the 2^C(n,2) labelled graphs on n nodes by the size k of the
  component of node 1: Σₖ C(n−1,k−1)·c(k)·2^C(n−k,2) = 2^C(n,2), where c(k)
  counts connected graphs. So
  c(n) = 2^C(n,2) − Σₖ₌₁ⁿ⁻¹ C(n−1,k−1)·c(k)·2^C(n−k,2) (E. N. Gilbert, 1956).
- C(n−1,k−1) = k·C(n,k)/n. In that form the k = 0 term vanishes, so the
  list `L` can hold a(0) = 1 at index 0 and `range(n)` covers everything.
  `comb(n,k)*k*L[k]//n` divides before the shift and is exact, and at
  n = 0 the sum is empty, so `//n` never sees a zero.
- `n:=len(L)` is set in the left operand, before the generator runs.

**Notes**

- Exact integers; the whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001187), CC BY-SA 4.0.
