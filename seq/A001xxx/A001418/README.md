# A001418

> Number of ways of folding an n X n sheet of stamps.
> — [OEIS A001418](https://oeis.org/A001418)

Offset 1: 1, 8, 1368, 300608, 186086600, 123912532224, 129950723279272, 162403827553180928

A folding is the order, from bottom to top, of the n² stamps in the folded
pile, so every order of the pile counts (the 2 × 2 sheet has 8 foldings).

### Python 3 — 221 bytes

```python
f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in{n,1}-{p%n<1}for a in range(p-d)if(a//d%n+p//d%n)%2*(~a//d%n)))
n=1
while[N:=n*n,print(f([],0))]:n+=1
```

**How it works**

- **The folding rule.** Folded flat, every stamp lies on the same unit
  square and every crease lies on one of its four edges: the creases between
  columns c and c + 1 lie on one side edge for even c and on the opposite
  one for odd c, and the creases between rows r and r + 1 likewise on the
  top or bottom edge by the parity of r. An order of the stamps in the pile
  is a folding exactly when no two creases on the same edge interleave,
  where {a, b} and {u, v} interleave if exactly one of u, v lies between a
  and b. This is the criterion of Lunnon's map-folding algorithm (Lunnon
  1971, in the OEIS links), the two-dimensional form of Koehler's rule for
  strips ([A000136](../../A000xxx/A000136/)).
- **Stamp by stamp.** Stamp p is row p % n of column p // n. Leaving out
  the last stamps of a folding leaves a folding of the first ones, so every
  folding of N = n² stamps is a folding of the first p stamps with stamp p
  slid into one of the p + 1 gaps of the pile, and only the new creases can
  break the rule. `f(H,p)` tries every gap, keeps those that pass and counts
  the foldings of N stamps it reaches.
- **Heights** are lists compared lexicographically, as in
  [A000136](../../A000xxx/A000136/): `[]` is the bottom gap and `x+[-p]`
  lies just above `x`, so `x` stands for the new stamp in every comparison.
- **The new creases.** Stamp p is joined to p − n (same row, previous
  column) and, unless it starts a column, to p − 1 (the row below):
  `{n,1}-{p%n<1}` (for n = 1 the set is empty, and `{1}-{True}` is too).
  For a crease (a, a + d), `a//d%n` is the row of a when d = 1 and its
  column when d = n, and `p//d%n` the same for p, whose crease sits one row
  or column lower: the two share an edge when these have opposite parities.
  For d = 1 the pair (a, a + 1) is a crease only if a is not in the top
  row, and `~a//d%n` = n − 1 − `a//d%n` is 0 exactly there; for d = n it
  is never 0, as a + n < p ≤ n². The new crease and (a, a + d) do not
  interleave when `(x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])`;
  `H[-d]` is stamp p − d because H holds p heights.

**Notes**

- Exact integers, no stored terms; correctness rests on the folding
  criterion above. The same check gives the 2 × n and 3 × n sheets of
  [A001415](../A001415/) and [A001416](../A001416/).
- The search is depth-first, so it needs almost no memory, but it counts
  every folding one by one: a(4) = 300608 comes after about 60 s here, and
  a(5) = 186086600 is out of reach. The bar is 4 terms in 120 s (the
  b-file has 8).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 221 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001418), CC BY-SA 4.0.
