# A001890

> Hit polynomials.
> — [OEIS A001890](https://oeis.org/A001890)

Offset 3: 1, 10, 34, 206, 1351, 10543, 92708, 912884, 9917445, 117838808, 1519483258, …

### Python 3 — 165 bytes

```python
from functools import*
n=2
while f:=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)+~-x*sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r]if~m&b)):n+=1;x=n**n;print(f(n,0,1)//x**3%x)
```

**How it works**

- **The sequence.** The hit polynomial H_n(x) = Σ_p x^(hits of p) runs over
  the permutations p of 1..n, where a hit is an i with p(i) − i ∈ {0, 1, 2}
  (the matrix of the entry's Mathematica program has x where 0 ≤ i − j ≤ 2,
  the transpose of the same band, which gives the same polynomial). a(n) is
  its coefficient of x³: the number of permutations with exactly three hits
  (the fourth column of [A080061](https://oeis.org/A080061); the first is
  [A001887](../A001887/)). This reading reproduces every term of the b-file.
- **Rooks.** If r_k counts the placements of k non-attacking rooks on the
  band, expanding each factor 1 + (x − 1)·[hit] of the permanent gives
  H_n(x) = Σ_k r_k·(x − 1)^k·(n − k)!, because a placement of k rooks lies
  in (n − k)! permutations.
- **Rows.** `f` walks down the rows as in [A001887](../A001887/): with r
  rows left the next row i has band columns i, i + 1, i + 2 (bits 1, 2, 4),
  `m` holds which of columns i and i + 1 earlier rooks hold, a rook in
  column b leaves (m + b) >> 1 and an empty row m >> 1. Nothing is taken at
  the start (m = 0), and `(1,2,4)[:r]` keeps the missing columns n + 1 and
  n + 2 out of the last two rows. Each rook weighs x − 1 (`~-x`), and the
  rows without a rook are multiplied by 1, 2, 3, … in turn (`j` is one more
  than the number of such rows so far), which makes the (n − k)!. `r<1or`
  ends a placement with `True` (1), and f(n, 0, 1) is the integer H_n(x).
- **One number for the polynomial.** x is not a symbol but the integer nⁿ
  (`x=n**n`). The coefficients of H_n count permutations, so each is at most
  n!, and n! < nⁿ for every n ≥ 2, which covers all terms here (they start
  at n = 3). They are therefore exactly the base-x digits of H_n(x), and
  `//x**3%x` reads the digit of x³.
- **A fresh cache per n.** x changes with n, so `while f:=cache(…):` builds
  a new cached lambda for every n (a function is always true); the lambda
  reads the global x that the body sets before calling it.

**Notes**

- Exact integer arithmetic and a direct count from the definition, so the
  program is right for every n. The recursion goes one or two frames deep
  per row, so Python's default recursion limit would stop it somewhere past
  n = 500 (an interpreter limit), long after the time runs out.
- The b-file has 21 terms (n = 3 to 23) and the bar is all of them in 60 s;
  they print in a fraction of a second. So few terms fit in a table about as
  long as the program, so this record went through review.
- Same template: [A001888](../A001888/) to [A001890](../A001890/) read one
  to three hits; the tridiagonal band |p(i) − i| ≤ 1 gives
  [A001884](../A001884/) to [A001886](../A001886/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 165 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001890), CC BY-SA 4.0.
