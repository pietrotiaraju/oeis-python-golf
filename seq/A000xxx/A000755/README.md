# A000755

> No-3-in-line problem on n X n grid: total number of ways of placing 2n points on n X n grid so no 3 are in a line. No symmetries are taken into account.
> — [OEIS A000755](https://oeis.org/A000755)

Offset 1: 0, 1, 2, 11, 32, 50, 132, 380, 368, 1135, 1120, 4348, 3622, 10568, 30634, 46304, 55576, 152210, 258176, 941580, …

### Python 3 — 172 bytes

```python
f=lambda P,r=0:r==n or sum(f(P+[(r,a),(r,b)],r+1)for a in range(n)for b in range(a)if len({(c,(y-c<<n)//(r-x))for c in(a,b)for x,y in P})==4*r)
n=1
while[print(f([]))]:n+=1
```

**How it works**

- **Two points per row.** Three points in one row are collinear, so 2n
  points on n rows means exactly two in every row. `f` fills the rows in
  order, trying every pair of columns b < a for row r, and counts the
  completed grids (`r==n` is True, i.e. 1).
- **Only lines through a new point need checking.** The grid built so far is
  already free of collinear triples, so a new point w = (r, c) is allowed
  exactly when no two earlier points lie on one line through w, i.e. when
  the slopes from w to the earlier points are distinct. The two new points
  share row r, so no line through both meets an earlier row. Vertical lines
  are slope 0 in these coordinates, so a third point in a column is caught
  too.
- **Exact slopes without fractions.** Every earlier point is in a lower row,
  so the slope is (y−c)/(r−x) with 1 ≤ r−x ≤ n−1. Two different such
  fractions differ by at least 1/(n−1)², and 2ⁿ ≥ (n−1)², so after scaling
  by 2ⁿ they differ by at least 1 and `(y-c<<n)//(r-x)` (a floor) tells
  them apart, while equal fractions give equal floors. Tagging each slope
  with its point c and asking for 4r distinct keys (2r earlier points, two
  new points) tests both new points at once.

**Speed**

The search visits every valid partial grid row by row: a(7) arrives after
about 6 s here, a(8) after about two minutes. The bar is the first 7 terms
within 60 s.

**Notes**

- `Fraction` slopes or a running n! as the scale (`(y-c)*F//(r-x)`, with
  `F*=n` in the loop) cost 6 or more bytes over the shift.
- [A000769](../A000769/) counts the same grids up to the 8 symmetries of the
  square with this search and Burnside's lemma.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000755), CC BY-SA 4.0.
