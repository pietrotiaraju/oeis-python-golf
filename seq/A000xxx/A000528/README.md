# A000528

> Number of types of Latin squares of order n. Equivalently, number of nonisomorphic 1-factorizations of K_{n,n}.
> — [OEIS A000528](https://oeis.org/A000528)

Offset 1: 1, 1, 1, 2, 2, 17, 324, 842227, 57810418543, 104452188344901572, …

A Latin square of order n is an n×n table in which each of n symbols
appears once in every row and once in every column. Two squares have the
same type if one becomes the other by permuting rows, permuting columns,
renaming symbols and possibly transposing; a(n) counts the types.

### Python 3 — 270 bytes

```python
from itertools import*
n=0
while Q:=[*permutations(range(n:=n+1))]:print(len({f"{min(sorted([z.index(b[a.index(s)])for s in z]for b in T)for T in(L,[*zip(*L)])for z in Q for a in T)}"for L in product(*[[p for p in Q if p[k]*n+k==p[0]]for k in Q[0]])if{*zip(*L)}<={*Q}}))
```

**How it works**

- **Fewer squares to try.** Every type contains a square whose first
  column is 0, 1, …, n−1 and whose diagonal is all 0. Rename the symbols
  so that the first column reads 0, …, n−1; then row i has its 0 in some
  column c(i), c is a permutation with c(0) = 0, and moving column c(i) to
  place i puts every 0 on the diagonal and keeps the first column.
- **The rows.** Row k must start with k and have 0 in place k. Since
  p[0] < n, the test `p[k]*n+k==p[0]` holds exactly when p[k] = 0 and
  p[0] = k. `product` takes one such permutation for each row, and
  `{*zip(*L)}<={*Q}` keeps the tuples whose columns are all permutations,
  that is, the Latin squares.
- **The key of a type.** A square is reduced if its first row and first
  column are 0, …, n−1. For a row a of T and a permutation z, the rows
  z⁻¹∘b∘a⁻¹∘z (for all rows b of T) form a square isotopic to T in which
  row a has become 0, …, n−1: the columns are reordered by a⁻¹∘z and the
  symbols renamed by z⁻¹. Its first column is a permutation, so sorting
  the rows makes it reduced. Conversely, a reduced isotope of T takes its
  first row from some row a and its columns in some order γ, and then the
  renaming is forced; z = a∘γ gives it. So the code builds every reduced
  square of the class of T, and running T over the square and its
  transpose (`[*zip(*L)]`) covers types. The least of them is the same for
  every square of a type and different for different types.
- **The code.** In `[z.index(b[a.index(s)])for s in z]`, `a.index(s)` is
  the column where row a holds s, `b[…]` reads row b there, and `z.index`
  renames the symbol. The minimum is a list of lists, so an f-string turns
  it into a string that a set can hold, and `len` of the set is a(n).
  `Q[0]` is (0, 1, …, n−1), the row indices. `while Q:=…` sets n and the
  permutations at once, and the list is never empty, so the loop never
  ends.

**Notes**

- Other versions that print the same terms: taking one row per first
  entry from consecutive blocks of `Q`, `zip(*[iter(Q)]*(len(Q)//n))`,
  without the zero diagonal: 250 bytes, but that tries 4⁴ = 256 times as
  many tuples for n = 5 (7962624 in all) and a(5) is not out after 80 s
  here; the previous program (a row-by-row search over reduced squares):
  366 bytes.
- An exhaustive search, so the program is right for every n. The same key
  over all reduced squares gives 1, 1, 1, 2, 2, 17 for n ≤ 6 (9408
  reduced squares of order 6).
- The five terms of the bar print in about 1.3 s here (31104 candidate
  tuples for n = 5). a(6) would need 120·24⁵ ≈ 9.6·10⁸ tuples and does
  not come out in any reasonable time. The b-file has 11 terms (up to
  a(11)).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 449 | first entry |
| 2026-11-06 | Python 3 | 366 | generate canonical keys directly and test zipped columns |
| 2026-11-07 | Python 3 | 270 | product over rows with zero diagonal, f-string key |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000528), CC BY-SA 4.0.
