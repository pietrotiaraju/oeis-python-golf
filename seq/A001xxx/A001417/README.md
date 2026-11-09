# A001417

> Number of ways of folding a 2 X 2 X ... X 2 n-dimensional map.
> — [OEIS A001417](https://oeis.org/A001417)

Offset 0: 1, 2, 8, 96, 4608, 798720, 361267200, 362794844160

A folding is the order, from bottom to top, of the 2ⁿ cells in the folded
pile, so every order of the pile counts (the 2 × 2 map has 8 foldings).

### Python 3 — 196 bytes

```python
f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in D for a in range(p-d)if a&d<p&d))
D=[];N=1
while[print(f([],0))]:D+=N,;N*=2
```

**How it works**

- **The folding rule.** Number the cells 0, …, 2ⁿ − 1 so that bit k of a
  cell is its k-th coordinate; the creases of dimension k join a and
  a + 2ᵏ for every a with bit k clear. Folded flat, all cells lie on one
  unit cube and each dimension has a single crease line, so all creases of
  dimension k lie on the same face. An order of the cells in the pile is a
  folding exactly when no two creases of the same dimension interleave,
  where {a, b} and {u, v} interleave if exactly one of u, v lies between a
  and b: this is the criterion of Lunnon's multi-dimensional map-folding
  algorithm (Lunnon 1971, in the OEIS links), the general form of Koehler's
  rule for strips ([A000136](../../A000xxx/A000136/)).
- **Cell by cell.** Leaving out the last cells of a folding leaves a
  folding of the first ones, so every folding of N = 2ⁿ cells is a folding
  of cells 0, …, p − 1 with cell p slid into one of the p + 1 gaps of the
  pile, and only the creases of p can break the rule. `f(H,p)` tries every
  gap, keeps those that pass and counts the foldings of N cells it reaches;
  the main loop prints the count for N = 1, 2, 4, …, with `D` holding the
  powers of two below N, one per dimension.
- **Heights** are lists compared lexicographically, as in
  [A000136](../../A000xxx/A000136/): `[]` is the bottom gap and `x+[-p]`
  lies just above `x`, so `x` stands for the new cell in every comparison.
- **The new creases.** For d = 2ᵏ, `p&d` is d when bit k of p is set (then
  p − d is the neighbour of p across that crease line, and `H[-d]` its
  height, since H holds p heights) and 0 otherwise. `a&d<p&d` picks the
  creases (a, a + d) of the same dimension, bit k of a clear, with
  a + d < p, only when p itself has such a crease. The new crease and
  (a, a + d) do not interleave when
  `(x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])`.

**Notes**

- Exact integers, no stored terms; correctness rests on the folding
  criterion above. The same rule, with the four edges of a rectangular
  map, gives [A001415](../A001415/), [A001416](../A001416/) and
  [A001418](../A001418/).
- The search is depth-first, so it needs almost no memory, but it counts
  every folding one by one: a(4) = 4608 comes after about 1.5 s here, and
  a(5) = 798720 takes far longer than the time limit (32 cells, about
  170 times as many foldings). The bar is 5 terms in 60 s (the b-file has
  8).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 196 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001417), CC BY-SA 4.0.
