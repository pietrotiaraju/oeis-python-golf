# A001197

> Zarankiewicz's problem k_2(n).
> — [OEIS A001197](https://oeis.org/A001197)

Offset 2: 4, 7, 10, 13, 17, 22, 25, 30, 35, 40, 46, 53, 57, 62, 68, 75, 82, 89, 97, 106, …

a(n) is the least k such that every n × n 0/1 matrix with k ones has a
2 × 2 submatrix of ones, so a(n) = z(n) + 1, where z(n) is the largest
number of ones in an n × n matrix in which no two rows share two columns
(the most edges of a bipartite graph with parts n, n and no 4-cycle).

### Python 3 — 249 bytes

```python
p=int.bit_count
g=lambda d,L,k,U:any(k<2or g(d-w,[c for c in L[:L.index(R)]if p(c&R)<2>d-~w-k*w-p(c)],k-1,U|R^R*2)for R in L[::-(k<n)|1]if d<=k*(w:=p(R))>>(R*2&~(R|U)))
n=c=1
while 1:
 n+=1
 while g(c,sorted(range(2**n),key=p),n,2**n):c+=1
 print(c)
```

**How it works**

- A row is an n-bit mask, bit n−1 being the first column. For each n the
  program asks, for c = a(n−1), a(n−1)+1, …, whether some matrix with at
  least c ones has no two rows sharing two columns; the first c that fails
  is a(n). The start is safe: a matrix for n−1 plus a new row and column
  holding a single 1 shows z(n) ≥ z(n−1) + 1 = a(n−1).
- `g(d,L,k,U)` places k more rows that must bring at least d more ones.
  `L` lists the rows still allowed, in increasing order of (weight,
  value). Choosing R keeps, for the next row, only the rows c before R
  in that order that share at most one column with R (`p(c&R)<2`), so
  the rows come out in decreasing order and every pair is checked once.
- Normal form: any matrix can first have its rows sorted by weight and
  then be brought, by sorting rows of equal weight in decreasing order
  and columns in decreasing lexicographic order (read from the top row),
  into a form where both hold at once: each step makes the matrix, read
  row by row as one binary number, larger, so it ends. The search only
  looks for matrices in this form, which loses nothing.
- Bounds: the k rows left weigh at most w = p(R) each, so R is tried only
  if d ≤ k·w; and a row c can only be used later if p(c) ≥ d − (k−1)·w,
  which `p(c&R)<2>d-~w-k*w-p(c)` checks together with the first test
  (2 > d+w+1−k·w−p(c)).
- Column order: bit j+1 of `U` is set once columns j+1 and j have
  differed in some chosen row (bit n is set from the start). While they
  are equal, a row with a 1 in column j must have one in column j+1, so
  `R*2&~(R|U)` is the set of broken pairs. Instead of a separate test,
  the bound k·w is shifted right by that mask: a break makes it 0 (or at
  least 4 times smaller), so the row is dropped. A row let through by the
  weak test is still a genuine row, so correctness never depends on it.
- Order: at the top (k = n) the rows are tried in increasing order
  (`L[::-(k<n)|1]`), deeper in decreasing order. At the top only the
  rows 1…10…0 pass the column test, so the smallest possible largest
  row weight is tried first; when c is reachable a solution turns up
  there quickly, instead of after exhausting heavier first rows that
  cannot work. This makes n = 15 about four times faster.
- Equal rows are never needed: two rows of weight ≥ 2 that are equal
  share two columns, and a repeated single 1 can be moved to a column no
  other one-1 row uses. So R itself is left out of its own list
  (`L[:L.index(R)]`).

**Notes**

- Exhaustive search with exact integers, so it is right for every n.
- Terms up to n = 18 (82) take about 32 s here; n = 19 needs about
  2½ minutes more. The b-file has 23 terms (to n = 24); the bar is 17
  terms with a 120 s timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 249 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001197), CC BY-SA 4.0.
