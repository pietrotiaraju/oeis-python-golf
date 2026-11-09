# A001410

> Sum of rows of triangle defined in A001404.
> — [OEIS A001410](https://oeis.org/A001410)

Offset 0: 1, 2, 5, 12, 28, 65, 149, 341, 777, 1769, 4022, 9140, 20763, 47156, 107086, …

### Python 3 — 81 bytes

```python
R=[[1]]
while[print(sum(r:=[sum(R[-n or-1][:n+2])for n in range(len(R))]))]:R+=r,
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
- **Printing.** `while[print(sum(r:=[…]))]:R+=r,` builds row m as r,
  prints its sum a(m), and appends it.
- Exact integer arithmetic, so the program is right for every term.

**Notes**

- The same row step as [A001404](../A001404/). The first record (84 bytes)
  kept row 0 as the first list and looped `for r in R:print(sum(r));R+=…`.
- The b-file has 27 terms (n = 0 to 26); the bar is all of them in 60 s,
  which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 84 | first entry |
| 2026-11-09 | Python 3 | 81 | virtual row [1], row built inside the print (-3) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001410), CC BY-SA 4.0.
