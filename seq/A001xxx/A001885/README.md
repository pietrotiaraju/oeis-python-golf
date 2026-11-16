# A001885

> Hit polynomials.
> — [OEIS A001885](https://oeis.org/A001885)

Offset 2: 2, 2, 10, 28, 207, 1288, 10366, 91296, 903037, 9832848, 117032570, …

### Python 3 — 167 bytes

```python
from functools import*
n=1
while f:=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)+~-x*sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r+1]if~m&b)):n+=1;x=n**n;print(f(n,1,1)//x**2%x)
```

**How it works**

- **The sequence.** The hit polynomial H_n(x) = Σ_p x^(hits of p) runs over
  the permutations p of 1..n, where a hit is an i with |p(i) − i| ≤ 1
  (Riordan's three-ply staircase). a(n) is its coefficient of x²: the number
  of permutations with exactly two hits (the third column of
  [A080018](https://oeis.org/A080018); the first is [A001883](../A001883/)).
  This reading reproduces every term of the b-file.
- **Rooks.** If r_k counts the placements of k non-attacking rooks on the
  band, expanding each factor 1 + (x − 1)·[hit] of the permanent gives
  H_n(x) = Σ_k r_k·(x − 1)^k·(n − k)!, because a placement of k rooks lies
  in (n − k)! permutations.
- **Rows.** `f` walks down the rows as in [A001883](../A001883/): with r
  rows left the next row i has band columns i − 1, i, i + 1 (bits 1, 2, 4),
  `m` holds which of columns i − 1 and i earlier rooks hold, a rook in
  column b leaves (m + b) >> 1 and an empty row m >> 1. m = 1 at the start
  because column 0 does not exist, and `[:r+1]` keeps the missing column n +
  1 out of the last row. Each rook weighs x − 1 (`~-x`), and the rows
  without a rook are multiplied by 1, 2, 3, … in turn (`j` is one more than
  the number of such rows so far), which makes the (n − k)!. `r<1or` ends a
  placement with `True` (1), and f(n, 1, 1) is the integer H_n(x).
- **One number for the polynomial.** x is not a symbol but the integer nⁿ
  (`x=n**n`). The coefficients of H_n count permutations, so each is at most
  n!, and n! < nⁿ for every n ≥ 2, which covers all terms here (they start
  at n = 2). They are therefore exactly the base-x digits of H_n(x), and
  `//x**2%x` reads the digit of x².
- **A fresh cache per n.** x changes with n, so `while f:=cache(…):` builds
  a new cached lambda for every n (a function is always true); the lambda
  reads the global x that the body sets before calling it.

**Notes**

- Exact integer arithmetic and a direct count from the definition, so the
  program is right for every n. The recursion goes one or two frames deep
  per row, so Python's default recursion limit would stop it somewhere past
  n = 500 (an interpreter limit), long after the time runs out.
- The b-file has 22 terms (n = 2 to 23) and the bar is all of them in 60 s;
  they print in a fraction of a second. So few terms fit in a table about as
  long as the program, so this record went through review.
- Same template: [A001884](../A001884/) to [A001886](../A001886/) read one
  to three hits; with the band p(i) − i ∈ {0, 1, 2} it gives
  [A001888](../A001888/) to [A001890](../A001890/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 167 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001885), CC BY-SA 4.0.
