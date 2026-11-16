# A001888

> Hit polynomials.
> — [OEIS A001888](https://oeis.org/A001888)

Offset 1: 1, 1, 1, 4, 21, 122, 849, 6719, 59873, 593686, 6483027, 77309508, …

### Python 3 — 164 bytes

```python
from functools import*
n=0
while f:=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)+~-x*sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r]if~m&b)):n+=1;x=-~n**n;print(f(n,0,1)//x%x)
```

**How it works**

- **The sequence.** Take the hit polynomial H_n(x) = Σ_p x^(hits of p) over
  the permutations p of 1..n, where a hit is an i with
  p(i) − i ∈ {0, 1, 2} (the matrix of the entry's Mathematica program has
  x where 0 ≤ i − j ≤ 2, the transpose of the same band, which gives the
  same polynomial). a(n) is its coefficient of x¹: the number of
  permutations with exactly one hit (the second column of
  [A080061](https://oeis.org/A080061); the first is
  [A001887](../A001887/)). This reproduces every term of the b-file.
- **Rooks.** If r_k counts the placements of k non-attacking rooks on the
  band, expanding each factor 1 + (x − 1)·[hit] of the permanent gives
  H_n(x) = Σ_k r_k·(x − 1)^k·(n − k)!.
- **Rows.** `f` walks down the rows as in A001887: with r rows left the next
  row i has band columns i, i + 1, i + 2 (bits 1, 2, 4), `m` holds which of
  columns i and i + 1 are taken, a rook in column b leaves (m + b) >> 1 and
  an empty row m >> 1. `(1,2,4)[:r]` keeps the missing columns n + 1 and
  n + 2 out of the last two rows. Each rook weighs x − 1 (`~-x`) and the
  rows without a rook are multiplied by 1, 2, 3, … in turn (`j`), which
  makes the (n − k)!.
- **One number for the polynomial.** x is the integer nⁿ + 1 (`-~n**n`), so
  f(n, 0, 1) is the integer H_n(x). Its coefficients count permutations,
  each at most n! < x, so they are its base-x digits and `//x%x` reads the
  digit of x¹.
- **A fresh cache per n.** x changes with n, so `while f:=cache(…):`
  builds a new cached lambda each time (a function is always true); the
  lambda reads the global x set in the body before the call.

**Notes**

- Exact integer arithmetic and a direct count, so the program is right for
  every n. The recursion goes one or two frames deep per row, so Python's
  default recursion limit would stop it somewhere past n = 500 (an
  interpreter limit), long after the time runs out.
- The b-file has 24 terms (n = 1 to 24) and the bar is all of them in 60
  s; they print in a fraction of a second.
- The tridiagonal version of the same program is
  [A001884](../A001884/); `//x**2%x` and `//x**3%x` with x = nⁿ give
  [A001889](../A001889/) and [A001890](../A001890/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 164 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001888), CC BY-SA 4.0.
