# A001416

> Number of ways of folding a 3 X n strip of stamps.
> — [OEIS A001416](https://oeis.org/A001416)

Offset 0: 1, 6, 60, 1368, 15552, 201240, 2016432, 21582624, 201060768, …

A folding is the order, from bottom to top, of the 3n stamps in the folded
pile, so every order of the pile counts (the 3 × 1 strip has 6 foldings).

### Python 3 — 206 bytes

```python
f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in(3,p%3)for a in range(p-d)if[a%3<1,a//3+p//3&1][d>2]))
N=0
while[print(+f([],0))]:N+=3
```

**How it works**

- **The folding rule.** Folded flat, every stamp lies on the same unit
  square and every crease lies on one of its four edges: the creases between
  columns c and c + 1 lie on one side edge for even c and on the opposite
  one for odd c; the creases between rows 1 and 2 lie on one of the other
  two edges, those between rows 2 and 3 on the last one. An order of the
  stamps in the pile is a folding exactly when no two creases on the same
  edge interleave, where {a, b} and {u, v} interleave if exactly one of u, v
  lies between a and b. This is the criterion of Lunnon's map-folding
  algorithm (Lunnon 1971, in the OEIS links), the two-dimensional form of
  Koehler's rule for strips ([A000136](../../A000xxx/A000136/)).
- **Stamp by stamp.** Stamp p lies in column p // 3, and each column is
  taken middle row first (p % 3 = 0), then the two outer rows. Leaving out
  the last stamps of a folding leaves a folding of the first ones, so every
  folding of N stamps is a folding of the first p stamps with stamp p slid
  into one of the p + 1 gaps of the pile, and only the new creases can
  break the rule. `f(H,p)` tries every gap, keeps those that pass and counts
  the foldings of N stamps it reaches; the main loop prints the count for
  N = 0, 3, 6, … (`+` turns the `True` of the empty sheet into 1).
- **Heights** are lists compared lexicographically, as in
  [A000136](../../A000xxx/A000136/) and [A001415](../A001415/): `[]` is the
  bottom gap and `x+[-p]` lies just above `x`, so `x` stands for the new
  stamp in every comparison.
- **The new creases.** Stamp p is joined to p − 3 (same row, previous
  column) and, for p % 3 = 1 or 2, to the middle stamp p − d of its column,
  with d = p % 3. So the row creases with d = 1 are exactly those of one
  edge, the ones with d = 2 those of the other: a crease (a, a + d) with
  d < 3 is a real crease of that edge when a % 3 = 0 (`a%3<1`). A column
  crease (a, a + 3) shares the edge of (p − 3, p) when a // 3 and p // 3
  have opposite parities (`a//3+p//3&1`). For a middle stamp d = 0, which
  only compares a stamp with itself and always passes. The new crease and
  (a, a + d) do not interleave when
  `(x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])`; `H[-d]` is stamp
  p − d because H holds p heights.

**Notes**

- Exact integers, no stored terms; correctness rests on the folding
  criterion above. The same check reproduces 3 × 3 = 1368 of
  [A001418](../A001418/) and 3 × 2 = 60 of [A001415](../A001415/).
- The search is depth-first, so it needs almost no memory, and it counts
  every folding one by one: a(n) grows about 10 times per term. The program
  prints a(5) = 201240 after about 29 s here and would need several minutes
  for a(6). The bar is 6 terms in 120 s (the b-file has 15).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 206 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001416), CC BY-SA 4.0.
