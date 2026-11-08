# A001070

> Number of normalized Latin squares with second row even.
> — [OEIS A001070](https://oeis.org/A001070)

Offset 1: 0, 0, 1, 2, 36, 4704, 8501760, 267533746176, 188809932117639168, 3790336726450693283512320

### Python 3 — 191 bytes

```python
f=lambda r,c,S,p:sum(f(r+-~c//n,-~c%n,S|T,p+len({(r*r,y)for y in range(x,n)}&S))for x in[r+c][r*c:]or range(n)if not(T:={(r,x),(~c,x)})&S)if r<n else p&1
n=1
while[print(f(0,0,{0},n>1))]:n+=1
```

**What is counted**

Normalized (reduced) Latin squares of order n have first row and first
column 0, 1, …, n−1; there are [A000315](../../A000xxx/A000315/)(n) of them.
This sequence counts those whose second row, read as a permutation, is
even. For n = 1 there is no second row, and for n = 2 it is the
transposition 1 0, so both terms are 0.

**How it works**

- The search is A000315's: cells in reading order, S holding `(r,x)` and
  `(~c,x)` for the symbols used in each row and column, and
  `[r+c][r*c:]or range(n)` forcing the first row and column.
- **Parity on the way.** p gains `len({(r*r,y)for y in range(x,n)}&S)`, the
  number of symbols y ≥ x already placed in row r². For r = 1 these are the
  earlier entries of the second row that are larger than x, so p collects
  exactly its inversions. Row r² = 0 is the identity, where nothing earlier
  is larger, and for r ≥ 2 the row r² lies below the current one and is
  still empty (or does not exist), so the other rows add nothing.
- **Start value.** p starts at `n>1`: for n ≥ 2 it is 1, so the leaf value
  `p&1` is 1 exactly when the inversion count is even; for n = 1 it is 0 and
  the only square counts 0.
- `…if r<n else p&1` is as long as `r//n and p&1or …` but stops for sure: the
  `and/or` form falls through into the sum when the leaf is 0, which for
  n = 1 keeps adding rows forever.

**Notes**

- Exhaustive and exact. The 9408 reduced squares of order 6 (4704 of them
  even, exactly half) take about 1 s here; order 7 has 16 942 080 squares,
  too many in a minute. The bar is 6 terms in 60 s; the b-file is the OEIS
  data, 10 terms.
- A sign-weighted sum, a(n) = (A000315(n) + Σ sign(row 2))/2, needs both
  counts and is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 191 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001070), CC BY-SA 4.0.
