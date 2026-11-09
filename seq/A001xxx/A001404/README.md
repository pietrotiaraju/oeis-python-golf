# A001404

> Triangle of values of 2-d recurrence.
> — [OEIS A001404](https://oeis.org/A001404)

Offset 0: 1, 1, 1, 2, 2, 1, 4, 5, 2, 1, 9, 11, 5, 2, 1, 20, 25, 12, 5, 2, 1, …

### Python 3 — 80 bytes

```python
R=[[1]]
while 1:R+=[print(x:=sum(R[-n or-1][:n+2]))or x for n in range(len(R))],
```

**How it works**

- **The recurrence.** The entry defines the triangle by Ralf Stephan's PARI
  program (the Maple program is the same): T(0, 0) = 1, T(m, k) = 0 for
  k > m, T(m, 0) = T(m−1, 0) + T(m−1, 1), and for 1 ≤ k ≤ m
  T(m, k) = Σ_{t=0..k+1} T(m−k, t).
- **Rows.** `R` holds a virtual row [1] and then the rows found so far,
  row m as the list T(m, 0), …, T(m, m). Before row m is built, `R` has
  m + 1 lists, so `range(len(R))` gives the columns n = 0…m. Entry n ≥ 1
  is the sum of the first n + 2 entries of row m − n, which is `R[-n]`;
  column 0 instead uses row m − 1, `R[-1]`, and its first two entries.
  `R[-n or-1]` covers both: −0 is falsy, so n = 0 gives −1, and the slice
  `[:n+2]` is `[:2]` there. A slice past the end of a short row just stops,
  which supplies the zeros T(m−n, t) = 0 for t > m − n. The virtual row is
  only read when row 0 is built (as `R[-1]`, giving T(0, 0) = 1), since
  `R[-n]` for n ≤ m never reaches back past row 0.
- **Printing.** `print(x:=…)or x` prints each entry as it is computed
  (one term per line, rows in order) and keeps it in the row, since
  `print` returns None. The comprehension is evaluated in full before
  `R+=[…],` appends the row.
- Exact integer arithmetic, so the program is right for every term.

**Notes**

- Read by rows: T(0,0); T(1,0), T(1,1); T(2,0), ….
- The first record (89 bytes) kept row 0 as the first list and printed each
  finished row with `print(*r,sep='\n')` from a `for r in R:` loop.
- The b-file (built from the entry's data) has 69 terms, rows 0 to 10 and
  the start of row 11; the bar is all of them in 60 s, which takes a
  fraction of a second. Row sums are [A001410](../A001410/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 89 | first entry |
| 2026-11-09 | Python 3 | 80 | virtual row [1], each entry printed as it is computed (-9) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001404), CC BY-SA 4.0.
