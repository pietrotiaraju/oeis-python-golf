# A000573

> Number of 4 X n normalized Latin rectangles.
> — [OEIS A000573](https://oeis.org/A000573)

Offset 4: 4, 56, 6552, 1293216, 420909504, 207624560256, 147174521059584, 143968880078466048, 188237563987982390784, 320510030393570671051776, …

A 4 × n Latin rectangle has rows that are permutations of 0, …, n−1 and no
repeated symbol in any column; it is normalized when its first row and first
column are in natural order.

### Python 3 — 157 bytes

```python
from itertools import*
n=4
while[print(sum(all(len({*c})>3for c in zip(range(n),*R))for R in product(*[permutations({*range(n)}-{i})for i in(0,1,2)])))]:n+=1
```

**How it works**

- **Fixing the last column instead.** Count the rectangles whose first row
  is 0, …, n−1 and whose last column is (n−1, 0, 1, 2). This is the same
  number: for a symbol permutation π with π(0) = n−1, π(1) = 0, π(2) = 1,
  π(3) = 2, the map L ↦ L′ with L′[r][c] = π(L[r][π⁻¹(c)]) keeps the first
  row in natural order and turns the first column (0, 1, 2, 3) into the
  last column (n−1, 0, 1, 2); it is a bijection between the two kinds of
  rectangle (n ≥ 4, so n − 1 is not among 0, 1, 2).
- **The search.** With the last column fixed, row r of the three lower rows
  is any arrangement of the symbols other than its last entry i = r − 1 in
  the columns 0, …, n−2: `permutations({*range(n)}-{i})`. `product` runs
  over all triples of such rows, and `zip(range(n),*R)` lists the columns
  0, …, n−2 with the first-row entry on top (`zip` stops at the shorter
  rows, so the header's n−1 is dropped). A triple counts when every column
  has 4 distinct entries; the fixed last column is distinct by choice.
- The rows here are permutations of n − 1 symbols, so the search has
  ((n−1)!)³ triples rather than (n!)³, and no row needs a test for its
  first entry.

**Notes**

- Other versions that print the same terms: the memoized row-by-row search
  with column bit masks: 276 bytes.
- Exact counting, so the program is right for every n (it is an exhaustive
  search).
- a(4), a(5), a(6) take about 6 s here; a(7) would need
  (6!)³ ≈ 3.7·10⁸ triples, so a 60-s run prints 3 terms. The b-file has 147
  terms (up to a(150)); the bar is 3 terms in 60 s.
- The run never gets near 4300-digit terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 300 | first entry |
| 2026-11-06 | Python 3 | 276 | cached completion expression and complemented column masks |
| 2026-11-07 | Python 3 | 157 | fix the last column, product of permutations of n − 1 symbols |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000573), CC BY-SA 4.0.
