# A000905

> Hamilton numbers.
> — [OEIS A000905](https://oeis.org/A000905)

Offset 1: 2, 3, 5, 11, 47, 923, 409619, 83763206255, 3508125906290858798171, …

### Python 3 — 92 bytes

```python
from math import*
L=2,
while[print(L[0])]:j=1;L=2+sum((-1)**(j:=j+1)*comb(y,j)for y in L),*L
```

**How it works**

- Recurrence of Sylvester and Hammond, as in the OEIS Maple program (the
  formula printed by Lucas is slightly wrong, see the entry):
  a(1) = 2 and a(n) = 2 + Σ_{i=1..n−1} (−1)^(i+1)·C(a(n−i), i+1).
- `L` is a tuple of the terms so far, newest first, so `L[0]` is the term
  just found and the i-th entry pairs with C(·, i+1). Writing j = i+1, the
  sum is Σ (−1)^j·C(L[j−2], j) for j = 2, 3, …
- `j=1;` and the walrus `(j:=j+1)` inside the generator give that index
  4 bytes cheaper than `for j,y in enumerate(L,2)`.
- `L=2+sum(…),*L` puts the new term in front (a tuple display with
  unpacking); `math.comb(y,j)` is 0 when j > y, as the formula needs.

**Notes**

- Exact integer arithmetic, correct for every n by the recurrence.
- The b-file has 14 terms; the bar is the whole b-file in 60 s. The
  program prints a(1) to a(16) at once (the last two are beyond the b-file)
  and then stops with a `ValueError`: a(17) has more digits than the
  4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000905), CC BY-SA 4.0.
