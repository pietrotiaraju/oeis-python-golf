# A002032

> Number of n-colored connected graphs on n labeled nodes.
> — [OEIS A002032](https://oeis.org/A002032)

Offset 0: 1, 1, 2, 24, 912, 87360, 19226880, 9405930240, 10142439229440, 24057598104207360, 125180857812868300800, 1422700916050060841779200, 35136968950395142864227532800, …

### Python 3 — 131 bytes

```python
from math import*
L=[]
while[print(perm(n:=len(L))*(a:=2**comb(n,2)-sum(comb(n,k)*k*L[k]//n<<comb(n-k,2)for k in range(n))))]:L+=a,
```

**How it works**

- **Every colouring is proper.** With n colours on n nodes, every colour
  is used exactly once, so no two nodes share a colour and every graph is
  properly coloured, in n! ways (Andrew Howroyd's comment on the entry):
  a(n) = n!·c(n), with c(n) the connected labelled graphs,
  [A001187](../../A001xxx/A001187/). One argument `perm(n)` is n!, five
  bytes under `factorial(n)`.
- **Connected graphs.** Sorting all 2^C(n,2) graphs by the size k of the
  component of node 1 gives
  c(n) = 2^C(n,2) − Σₖ₌₁ⁿ⁻¹ C(n−1,k−1)·c(k)·2^C(n−k,2) (Gilbert, 1956), and
  the code is the A001187 program: C(n−1,k−1) = k·C(n,k)/n makes the k = 0
  term vanish, so `L` holds c(0) = 1 at index 0 and the sum runs over
  `range(n)`. The walrus `a:=` keeps c(n) for the list while
  `perm(n:=len(L))*(…)` prints n!·c(n).

**Notes**

- Exact integers, so the program is right for every n; the whole b-file
  (n = 0 to 50) prints at once, and the bar is all 51 terms.
- The OEIS entry's own formula, f_n(n) with inclusion–exclusion over the
  colours used, gives the same numbers; the shortcut is that with n
  colours on n nodes "uses all colours" already forces them to be distinct.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 131 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002032), CC BY-SA 4.0.
