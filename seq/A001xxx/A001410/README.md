# A001410

> Sum of rows of triangle defined in A001404.
> — [OEIS A001410](https://oeis.org/A001410)

Offset 0: 1, 2, 5, 12, 28, 65, 149, 341, 777, 1769, 4022, 9140, 20763, 47156, 107086, …

### Python 3 — 84 bytes

```python
R=[[1]]
for r in R:print(sum(r));R+=[sum(R[-n or-1][:n+2])for n in range(len(r)+1)],
```

**How it works**

- **The recurrence.** The entry defines the triangle by Ralf Stephan's PARI
  program (the Maple program is the same): T(0, 0) = 1, T(m, k) = 0 for
  k > m, T(m, 0) = T(m−1, 0) + T(m−1, 1), and for 1 ≤ k ≤ m
  T(m, k) = Σ_{t=0..k+1} T(m−k, t).
- **Rows.** `R` holds the rows found so far, row m as the list
  T(m, 0), …, T(m, m). `for r in R:` walks a list that grows while it is
  read, so it never ends: each pass prints the sum of row r and appends the next one.
  When r is row m − 1 (the last row), the new row m has len(r) + 1 = m + 1
  entries, and entry n ≥ 1 (the column, `n` in the code) is the sum of the
  first n + 2 entries of row m − n, which is `R[-n]`; column 0 instead uses
  row m − 1, `R[-1]`, and its first two entries. `R[-n or-1]` covers both:
  −0 is falsy, so n = 0 gives −1, and the slice `[:n+2]` is `[:2]` there.
  A slice past the end of a short row just stops there, which supplies the
  zeros T(m−n, t) = 0 for t > m − n.
- Exact integer arithmetic, so the program is right for every term.

**Notes**

- The same program as [A001404](../A001404/) with `print(sum(r))` in place
  of printing the row.
- The b-file has 27 terms (n = 0 to 26); the bar is all of them in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001410), CC BY-SA 4.0.
