# A001501

> Number of n X n 0-1 matrices with all column and row sums equal to 3.
> — [OEIS A001501](https://oeis.org/A001501)

Offset 0: 1, 0, 0, 1, 24, 2040, 297200, 68938800, 24046189440, 12025780892160, …

### Python 3 — 159 bytes

```python
from math import*
C=comb;f=factorial;n=0
while 1:R=range(n+1);print(sum(C(n,k)**2*C(k,j)*f(k)*f(3*n-3*k+j)*12**k*(-3)**j>>j for k in R for j in R)//36**n);n+=1
```

**Why the formula**

- Each row is a set of three columns (a 0-1 row with three ones), i.e. a monomial of degree 3 in column
  variables x₁, …, xₙ. Multiplying one such monomial per row, the
  exponent of x_c is the sum of column c, so a(n) is the coefficient of
  x₁³⋯xₙ³ in e₃ (the sum of all products of three different variables) raised to the n-th power.
- In power sums pₘ = Σ x_cᵐ, e₃ = (p₁³ − 3p₁p₂ + 2p₃)/6. Expand the n-th power with the
  multinomial theorem: i factors p₁³, j factors −3p₁p₂ and l factors
  2p₃ (i + j + l = n).
- The coefficient of x₁³⋯xₙ³ in p₁^(3i+j)·p₂^j·p₃^l: each p₃ fills a whole
  column, different ones different columns (n!/(n−l)! ways); each p₂ takes
  a column of its own among the rest, since 2 + 2 > 3 ((n−l)!/i! ways);
  the 3i + j factors p₁ then put one unit into each of the j columns of
  the p₂'s and three into each of the other i columns ((3i+j)!/6^i ways).
- So a(n) = 6^(−n) Σ n!/(i!·j!·l!) · (−3)^j·2^l · n!/i! · (3i+j)!/6^i, which
  is Shanzhen Gao's double sum in the OEIS entry (with the sign (−1)^j). With k = j + l = n − i
  (so n!²/(i!²·j!·l!) = C(n,k)²·k!·C(k,j)) and (−18)^j·12^l = 12^k·(−3/2)^j:

  36ⁿ·a(n) = Σ_(k=0..n) Σ_(j=0..k) C(n,k)²·k!·C(k,j)·(3(n−k)+j)!·12^k·(−3/2)^j.

**How it works**

- `k` and `j` both run over 0 … n (`R=range(n+1)`): for j > k the factor
  `C(k,j)` is 0, so those terms are exact zeros. For j ≤ k, 2^j divides
  12^k, so the shift `>>j` (floor division by 2^j, exact here, also for
  the negative terms) leaves an integer, and the sum is exactly 36ⁿ·a(n):
  `//36**n`.
- `C=comb`, `f=factorial`. The range is set in the loop body: an
  assignment expression cannot be the iterable of a comprehension.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 186 terms (n = 0 to 185); the bar is the whole
  b-file in 90 s. The double sum costs O(n²) factorials per term; the
  last b-file term comes after about 36 s on this PC (20 reference seconds).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 159 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001501), CC BY-SA 4.0.
