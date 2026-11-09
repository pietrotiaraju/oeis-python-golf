# A001198

> Zarankiewicz's problem k_3(n).
> — [OEIS A001198](https://oeis.org/A001198)

Offset 3: 9, 14, 21, 27, 34, 43, 50, 61, 70, 81, 93, 106, 121, 129, …

a(n) is the least k such that every n × n 0/1 matrix with k ones has a
3 × 3 submatrix of ones, so a(n) = z(n) + 1, where z(n) is the largest
number of ones in an n × n matrix in which no three rows share three
columns (the most edges of a bipartite graph with parts n, n and no
K_{3,3}).

### Python 3 — 275 bytes

```python
p=int.bit_count
g=lambda d,L,k,U,X:any(k<2or g(d-w,[c for c in L[L.index(R):]if max(p(c&R&r)for r in X)<3>d-~-~w-k*w-p(c)],k-1,U|R^R*2,X+[R])for R in L if d<=k*(w:=p(R))>>(R*2&~(R|U)))
n=c=2
while 1:
 n+=1
 while g(c,sorted(range(2**n),key=p)[::-1],n,2**n,[0]):c+=1
 print(c)
```

**How it works**

- The same search as [A001197](../A001197/), with the 2 × 2 test
  replaced by a 3 × 3 one. A row is an n-bit mask, bit n−1 being the
  first column. For each n the program asks, for c = a(n−1), a(n−1)+1, …,
  whether some matrix with at least c ones has no three rows sharing
  three columns; the first c that fails is a(n). The start is safe: a
  matrix for n−1 plus a new row and column holding a single 1 shows
  z(n) ≥ z(n−1) + 1 = a(n−1).
- `g(d,L,k,U,X)` places k more rows that must bring at least d more
  ones; `X` holds the rows placed so far (after a dummy 0, so that `max`
  never sees an empty list) and `L` the rows still allowed, in
  decreasing order of (weight, value). Choosing R keeps, for the next
  row, only the rows c from R on such that c, R and any earlier row r
  share at most two columns (`max(p(c&R&r)for r in X)<3`). R stays in
  its own list: equal rows can be needed here (for n = 3 the best matrix
  is 111, 111, 110), and a third copy is then removed by the same test.
- Normal form: any matrix can first have its rows sorted by weight and
  then be brought, by sorting rows of equal weight in decreasing order
  and columns in decreasing lexicographic order (read from the top row),
  into a form where both hold at once: each step makes the matrix, read
  row by row as one binary number, larger, so it ends. The search only
  looks for matrices in this form, which loses nothing.
- Bounds: the k rows left weigh at most w = p(R) each, so R is tried only
  if d ≤ k·w; and a row c can only be used later if p(c) ≥ d − (k−1)·w.
  The chain `…<3>d-~-~w-k*w-p(c)` checks this together with the
  three-row test (3 > d+w+2−k·w−p(c)).
- Column order: bit j+1 of `U` is set once columns j+1 and j have
  differed in some chosen row (bit n is set from the start). While they
  are equal, a row with a 1 in column j must have one in column j+1, so
  `R*2&~(R|U)` is the set of broken pairs, and the bound k·w is shifted
  right by it: a break makes it 0 (or at least 4 times smaller), so the
  row is dropped. A row let through by the weak test is still a genuine
  row, so correctness never depends on it.

**Notes**

- Exhaustive search with exact integers, so it is right for every n.
- Most of the time goes into showing that c = a(n) is impossible, which
  visits the whole pruned tree, so the increasing order at the top that
  helps A001197 gains nothing here and is left out.
- Terms up to n = 11 (70) take about 11 s here; proving a(12) = 81 alone
  takes about 70 s more. The b-file has 14 terms (to n = 16); the bar is
  9 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 275 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001198), CC BY-SA 4.0.
