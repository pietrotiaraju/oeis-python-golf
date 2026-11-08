# A001009

> Triangle giving number L(n,k) of normalized k X n Latin rectangles.
> — [OEIS A001009](https://oeis.org/A001009)

Offset 1 (rows n = 1, 2, …; k = 1 … n in each row): 1, 1, 1, 1, 1, 1, 1, 3, 4, 4, 1, 11, 46, 56, 56, 1, 53, 1064, 6552, 9408, 9408, …

### Python 3 — 152 bytes

```python
f=lambda r,c,S:r//k or sum(f(r+-~c//n,-~c%n,S|T)for x in[r+c][r*c:]or range(n)if not(T:={(r,x),(~c,x)})&S)
n=k=1
while[print(f(0,0,{0}))]:k=k%n+1;n+=k<2
```

**What is counted**

A k × n Latin rectangle has k rows, n columns and symbols 0 … n−1, with no
symbol twice in a row or a column. It is normalized when its first row is
0, 1, …, n−1 and its first column is 0, 1, …, k−1. Row n of the triangle
lists L(n,1), …, L(n,n); the last entry is the number of reduced Latin
squares, [A000315](../../A000xxx/A000315/).

**How it works**

- This is the backtracking of [A000315](../../A000xxx/A000315/) with the
  number of rows cut to k: `f(r,c,S)` fills the cells in reading order and
  stops with 1 when `r//k` says that k rows are complete.
- S holds `(r,x)` (row r has symbol x) and `(~c,x)` (column c has x); the
  negative `~c` keeps the two kinds of keys apart. A symbol is tried only if
  `not(T:={…})&S`.
- `[r+c][r*c:]or range(n)`: in the first row or column (r·c = 0) the only
  candidate is the forced symbol r+c, which is the normalization; elsewhere
  the slice is empty and every symbol is a candidate.
- **Triangle loop.** `k=k%n+1;n+=k<2` steps (n,k) through (1,1), (2,1),
  (2,2), (3,1), …: k wraps from n back to 1 and only then does n grow.

**Notes**

- Exhaustive and exact, no formula used. Rows 1–6 (21 terms) take about
  3 s here; row 7 starts with 1, 309, 35792 at once, but L(7,4) = 1293216
  arrives after about 50 s and L(7,5) = 11270400 would take several minutes.
  The bar is 21 terms (rows 1–6) in 60 s; the b-file has 73 terms (rows
  1–11 and the start of row 12).
- The last row of a Latin square is forced, so L(n,n) = L(n,n−1); the
  program does not use it, since printing the copy costs more bytes than it
  saves time within the bar.
- Recursion depth is k·n cells, fine for every row that could finish.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 152 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001009), CC BY-SA 4.0.
