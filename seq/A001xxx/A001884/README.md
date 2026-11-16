# A001884

> Hit polynomials.
> — [OEIS A001884](https://oeis.org/A001884)

Offset 1: 1, 0, 1, 2, 20, 104, 775, 6140, 55427, 553802, 6087992, 72994152, …

### Python 3 — 166 bytes

```python
from functools import*
n=0
while f:=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)+~-x*sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r+1]if~m&b)):n+=1;x=-~n**n;print(f(n,1,1)//x%x)
```

**How it works**

- **The sequence.** Riordan's hit polynomial of the three-ply staircase is
  H_n(x) = Σ_p x^(hits of p) over the permutations p of 1..n, where a hit
  is an i with |p(i) − i| ≤ 1. a(n) is its coefficient of x¹: the number of
  permutations with exactly one such i (the second column of
  [A080018](https://oeis.org/A080018); the first is
  [A001883](../A001883/)). This reading reproduces every term of the
  b-file.
- **Rooks.** Let r_k count the placements of k non-attacking rooks on the
  band |i − j| ≤ 1. Expanding each factor 1 + (x − 1)·[hit] of the
  permanent gives H_n(x) = Σ_k r_k·(x − 1)^k·(n − k)!, since a placement of
  k rooks lies in (n − k)! permutations.
- **Rows.** `f` walks down the rows exactly as in A001883: with r rows
  left the next row i has band columns i − 1, i, i + 1 (bits 1, 2, 4), `m`
  holds which of columns i − 1 and i are taken, a rook in column b leaves
  (m + b) >> 1 and an empty row m >> 1; m = 1 at the start because column
  0 does not exist, and `[:r+1]` keeps column n + 1 out of the last row.
  Each rook weighs x − 1 (`~-x`), and the rows without a rook are
  multiplied by 1, 2, 3, … in turn (`j`), which makes the (n − k)!.
- **One number for the polynomial.** x is not a symbol but the integer
  nⁿ + 1 (`-~n**n`), so f(n, 1, 1) is the integer H_n(x). Its coefficients
  are counts of permutations, each at most n! < x, so they are exactly the
  base-x digits of H_n(x), and `//x%x` reads the digit of x¹.
- **A fresh cache per n.** x changes with n, so the loop builds a new
  cached lambda for every n; `while f:=cache(…):` does that in the
  condition (a function is always true), and the lambda reads the global
  x set in the body before it is called.

**Notes**

- Exact integer arithmetic and a direct count, so the program is right for
  every n. The recursion goes one or two frames deep per row, so Python's
  default recursion limit would stop it somewhere past n = 500 (an
  interpreter limit), long after the time runs out.
- The b-file has 24 terms (n = 1 to 24) and the bar is all of them in 60
  s; they print in a fraction of a second.
- With x as a parameter of one shared cached lambda the program is 7 bytes
  longer. Counting "marked" rooks instead of using a big x is longer
  still.
- The same template with x = nⁿ and `//x**2%x` or `//x**3%x` gives
  [A001885](../A001885/) and [A001886](../A001886/); with the band
  p(i) − i ∈ {0, 1, 2} it gives [A001888](../A001888/) to
  [A001890](../A001890/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 166 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001884), CC BY-SA 4.0.
