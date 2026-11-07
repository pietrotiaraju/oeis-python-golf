# A000611

> Number of normalized Latin squares of order n containing no 2 X 2 Latin subsquare.
> — [OEIS A000611](https://oeis.org/A000611)

Offset 1: 1, 0, 1, 0, 6, 40, 17760, 2096640, 29659631400, …

### Python 3 — 192 bytes

```python
from itertools import*
f=lambda p,C:p[0]>n-2or sum(f(q,D)for D in[[q for q in C if not{*zip(p,q)}&{*zip(q,p)}]]for q in D if q[0]-p[0]<2)
n=1
while[print(+f(r:=range(n),permutations(r)))]:n+=1
```

**How it works**

- A square is a set of rows, each row a permutation of 0, …, n−1 (the
  symbol in every column). Normalized means the first row and the first
  column are 0, 1, …, n−1, so the row that starts with j is row j + 1 and
  the first row is the identity.
- Two rows p and q may share a square without a 2×2 Latin subsquare
  (an intercalate) exactly when no pair of `zip(p,q)` is the reverse of a
  pair of `zip(q,p)`: an intercalate on columns c, d is p[c] = q[d] with
  p[d] = q[c], and a clash in one column, p[c] = q[c], gives a pair (x, x)
  that is its own reverse. Intercalates and clashes both live in two rows,
  so a set of rows that is pairwise compatible in this sense is exactly an
  N₂-free Latin square, and `not{*zip(p,q)}&{*zip(q,p)}` is the whole test.
- `f(p,C)` counts the completions of a partial square whose last row is p,
  where C holds the permutations compatible with every earlier row. It keeps
  the members of C compatible with p as D, then goes on with the rows q of D
  whose first symbol is p[0] + 1. Every q in D starts with a symbol no row
  uses yet (a used one would clash in column 0), and those are all larger
  than p[0] because the rows go in order, so `q[0]-p[0]<2` picks exactly the
  next one. The square is full when the last row starts with n − 1.
- The search starts from the identity row `range(n)` (it supports both
  `p[0]` and `zip`) with all n! permutations as candidates; the walrus in
  the call `f(r:=range(n),permutations(r))` names the range for the second
  argument. `for D in[[…]]for q in D` binds the filtered list once per call
  inside the generator. For n = 1 f returns `True`, hence the `+`.

**Notes**

- A plain exhaustive search that meets every N₂-free normalized square
  once: n = 7 (17760 squares, about 3·10⁵ partial squares) takes about 31 s
  here. n = 8 has 2,096,640 squares and is far out of reach, and the b-file's
  last term, n = 9, came from much stronger methods.
- The bar is 7 terms in 120 s; the b-file has 9.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 192 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000611), CC BY-SA 4.0.
