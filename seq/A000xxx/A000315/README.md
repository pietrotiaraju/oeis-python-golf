# A000315

> Number of reduced Latin squares of order n; also number of labeled loops (quasigroups with an identity element) with a fixed identity element.
> — [OEIS A000315](https://oeis.org/A000315)

Offset 1: 1, 1, 1, 4, 56, 9408, 16942080, 535281401856, 377597570964258816, …

### Python 3 — 140 bytes

```python
f=lambda r,c,S:r//n or sum(f(r+-~c//n,-~c%n,S|T)for x in[r+c][r*c:]or range(n)if not(T:={(r,x),(~c,x)})&S)
n=1
while[print(f(0,0,{0}))]:n+=1
```

**How it works**

- A reduced Latin square has symbols 0 … n−1, every symbol once in each
  row and each column, and first row and first column 0, 1, …, n−1 in
  order.
- `f(r,c,S)` fills the cells in reading order, starting at row r,
  column c, and counts the ways to finish. S holds what is used so far:
  `(r,x)` means row r already has symbol x and `(~c,x)` that column c has
  it; `~c` is negative, so the two kinds of keys never clash.
- `[r+c][r*c:]or range(n)` is the list of candidates for the cell: in the
  first row or column (r·c = 0) the slice keeps the one forced symbol r+c,
  elsewhere it is empty and `or` falls back to every symbol.
- `not(T:={…})&S` keeps a symbol only if neither its row nor its column
  has it, and the recursion moves to the next cell with S|T:
  `r+-~c//n,-~c%n` is (r, c+1), wrapping to the next row after the last
  column.
- After the last cell r reaches n and `r//n` returns 1; before that it is
  0 and the sum runs. `{0}` is a starting set that clashes with no key.

**Notes**

- Exhaustive backtracking, exact. The 9408 squares of order 6 take about
  1.5 s here; order 7 has 16 942 080 squares, too many to visit one by one
  in a minute. The bar is 6 terms in 60 s; the b-file has 11 (n = 1 to 11).
- Recursion depth is n² cells, fine for every order that could finish.
- Choosing whole rows (permutations disjoint from the rows above, with
  `itertools`) is about 40 bytes longer, and a single cell index k with
  `(r:=k//n)` and `(c:=k%n)` walruses cannot use the candidate list, since
  a walrus is not allowed in a comprehension's iterable; it is 148 bytes.
- Integer keys such as `{x*n+r,x+~c*n}` are the same length once the
  starting set has to avoid key 0.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 140 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000315), CC BY-SA 4.0.
