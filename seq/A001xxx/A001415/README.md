# A001415

> Number of ways of folding a 2 X n strip of stamps.
> — [OEIS A001415](https://oeis.org/A001415)

Offset 0: 1, 2, 8, 60, 320, 1980, 10512, 60788, 320896, 1787904, 9381840, …

A folding is the order, from bottom to top, of the 2n stamps in the folded
pile, so every order of the pile counts (the 2 × 1 strip has 2 foldings, the
2 × 2 sheet 8).

### Python 3 — 190 bytes

```python
f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in(2,p%2)for a in range(p-d)if a&d^p&d))
N=0
while[print(+f([],0))]:N+=2
```

**How it works**

- **The folding rule.** Folded flat, every stamp lies on the same unit
  square and every crease lies on one of its four edges: the creases between
  columns c and c + 1 lie on one side edge for even c and on the opposite
  one for odd c, and the creases between the two rows all lie on one top or
  bottom edge. An order of the stamps in the pile is a folding exactly when
  no two creases on the same edge interleave, where {a, b} and {u, v}
  interleave if exactly one of u, v lies between a and b. This is the
  criterion of Lunnon's map-folding algorithm (Lunnon 1971, in the OEIS
  links), the two-dimensional form of Koehler's rule for strips
  ([A000136](../../A000xxx/A000136/)).
- **Stamp by stamp.** Stamp p is row p % 2 of column p // 2. Leaving out
  the last stamps of a folding leaves a folding of the first ones (fewer
  creases to check), so every folding of N stamps is a folding of the first
  p stamps with stamp p slid into one of the p + 1 gaps of the pile, and
  only the new creases can break the rule. `f(H,p)` tries every gap, keeps
  those that pass and counts the foldings of N stamps it reaches; the main
  loop prints the count for N = 0, 2, 4, … (`+` turns the `True` of the
  empty sheet into 1).
- **Heights.** `H[a]` is the height of stamp a, a list compared
  lexicographically, as in [A000136](../../A000xxx/A000136/): `[]` is the
  bottom gap, and `x+[-p]` lies just above `x` and below every other
  height above `x` (those that start with `x` were made at an earlier,
  smaller p). Nothing lies between `x` and the new stamp, so `x` stands for
  it in every comparison.
- **The new creases.** Stamp p is joined to stamp p − d with d = 2 (same
  row, previous column) and, for odd p, d = 1 (same column, other row);
  for even p the second value is d = 0, which selects nothing. A crease
  (a, a + d) lies on the same edge as (p − d, p) when `a&d^p&d` is
  nonzero: for d = 1 those are the row creases (a even), for d = 2 the
  column creases whose column a // 2 has the parity of (p − 2) // 2. The
  new crease and (a, a + d) do not interleave when
  `(x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])`; `H[-d]` is stamp
  p − d because H holds p heights.

**Notes**

- Exact integers, no stored terms; correctness rests on the folding
  criterion above. The same check reproduces the 2 × n terms of
  [A001416](../A001416/) and [A001418](../A001418/) (2 × 3 = 60,
  2 × 2 = 8).
- The search is depth-first, so it needs almost no memory, and it counts
  every folding one by one: a(n) grows about 5.5 times per term. The
  program prints a(8) = 320896 after about 47 s here and would need a few
  more minutes for a(9). The bar is 9 terms in 120 s (the b-file has 21).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 190 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001415), CC BY-SA 4.0.
