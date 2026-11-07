# A000576

> a(n) is the number of (n-2) X n normalized Latin rectangles.
> — [OEIS A000576](https://oeis.org/A000576)

Offset 3: 1, 3, 46, 6552, 11270400, 335390189568, 224382967916691456, 4292039421591854273003520, 2905990310033882693113989027594240, …

A k × n Latin rectangle has rows that are permutations of 0, …, n−1 and no
repeated symbol in any column; it is normalized when its first row and first
column are in natural order. Here k = n − 2.

### Python 3 — 163 bytes

```python
from itertools import*
n=3
while[print(sum(all(len({*c})>n-3for c in zip(range(n),*R))for R in product(*[permutations({*range(n)}-{i})for i in range(n-3)])))]:n+=1
```

**How it works**

- The [A000573](../A000573/) search with k = n − 2 rows instead of 4. It
  counts the rectangles whose first row is 0, …, n−1 and whose last column
  is (n−1, 0, 1, …, n−4). For a symbol permutation π with π(0) = n−1 and
  π(r) = r − 1 for 1 ≤ r ≤ n − 3, the map L ↦ L′ with
  L′[r][c] = π(L[r][π⁻¹(c)]) keeps the first row in natural order and turns
  the first column (0, 1, …, n−3) into that last column, so the two counts
  agree.
- Each of the n − 3 lower rows is an arrangement of the symbols other than
  its last entry i in the columns 0, …, n−2,
  `permutations({*range(n)}-{i})` for i in `range(n-3)`. `product` runs over
  all choices, `zip(range(n),*R)` lists the columns under the first row, and
  a choice counts when every column has n − 2 distinct entries,
  `len({*c})>n-3`.
- For n = 3 there are no lower rows: `product()` yields one empty choice,
  every column holds one entry, and the count is 1.

**Notes**

- Other versions that print the same terms: the memoized row-by-row search
  with column bit masks: 279 bytes.
- Exact counting, so the program is right for every n (it is an exhaustive
  search).
- a(3), …, a(6) take about 8 s here; a(7) would need (6!)⁴ ≈ 2.7·10¹¹
  choices, so a 60-s run prints 4 terms. The b-file has 9 terms (up to
  a(11)); the bar is 3 terms in 60 s.
- The run never gets near 4300-digit terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 302 | first entry |
| 2026-11-06 | Python 3 | 279 | cached completion expression and complemented column masks |
| 2026-11-07 | Python 3 | 163 | fix the last column, product of permutations of n − 1 symbols |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000576), CC BY-SA 4.0.
