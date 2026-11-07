# A000535

> Card matching: coefficients B[n,2] of t^2 in the reduced hit polynomial A[n,n,n](t).
> — [OEIS A000535](https://oeis.org/A000535)

Offset 1: 0, 27, 378, 4536, 48600, 489780, 4738104, 44535456, 409752432, 3708359550, …

Lay out a deck of n A's, n B's and n C's on 3n places, the first n
marked A, the next n marked B and the last n marked C. a(n) counts the
layouts (cards of one letter are alike) in which exactly two cards lie on
a place marked with their own letter.

### Python 3 — 123 bytes

```python
from math import comb as C
n=1
while[print(3*sum(C(j,2)*C(n,j)*(C(n,j)*C(n,j-2)+2*C(n,j-1)**2)for j in range(2,n+1)))]:n+=1
```

**How it works**

- **The entry's formula.** Record a layout by its 3×3 table: x_{ik}
  cards of letter k in the block of letter i. Rows and columns sum to n,
  a table is realized by Π_i n!/(x_{i1}! x_{i2}! x_{i3}!) layouts, and the
  hits are x_11 + x_22 + x_33. Two hits means diagonal (2,0,0) or (1,1,0)
  up to order, three times each, and then one free entry k fixes the
  table. That gives the formula on the entry:
  a(n) = 3·C(n,2)·Σ_k C(n,k+2)·C(n,k)·C(n−2,k)
  + 3n²·Σ_k C(n,k+1)·C(n−1,k+1)·C(n−1,k), k = 0, …, n−2.
- **One sum.** C(n,2)·C(n−2,k) = C(k+2,2)·C(n,k+2) (both are
  n!/(2·k!·(n−2−k)!)), and n·C(n−1,k) = (k+1)·C(n,k+1),
  n·C(n−1,k+1) = (k+2)·C(n,k+2). With j = k + 2 both sums share the factor
  C(j,2)·C(n,j):
  a(n) = 3·Σ_{j=2}^{n} C(j,2)·C(n,j)·(C(n,j)·C(n,j−2) + 2·C(n,j−1)²).
- **The code.** `comb` is imported as `C` (it appears seven times).
  `range(2,n+1)` starts at 2 because `comb` refuses a negative second
  argument; for n = 1 the range is empty and a(1) = 0. `print` sits in the
  loop condition: it returns `None`, and `[None]` is a non-empty list, so
  the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: the entry's two sums as they
  stand, `3*sum(C(n,2)*C(n,k+2)*C(n,k)*C(n-2,k)+n*n*C(n,k+1)*C(n-1,k+1)*C(n-1,k)for k in range(n-1))`
  with `while 1:…;n+=1`: 141 bytes; the symmetric `C(n,n+2-j)` and
  `C(n,n+1-j)`, which vanish for small j, with `range(n+1)`: 125 bytes.
- Exact integer arithmetic, so the program is right for every n. A count of
  all layouts agrees for n ≤ 7.
- About 980 terms in 60 s here. The b-file has 20 terms (up to a(20)); the
  bar is the whole b-file in 60 s, and it prints in well under a second.
- a(n) grows like 8ⁿ·n, so it passes 4300 digits (Python's int-to-str
  limit) at a(4758), far beyond what prints in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 141 | first entry |
| 2026-11-07 | Python 3 | 123 | both sums merged into one over C(n,j) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000535), CC BY-SA 4.0.
