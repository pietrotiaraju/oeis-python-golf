# A001801

> Diagonal 3 of triangle A100258 comprising coefficients of Legendre polynomials.
> — [OEIS A001801](https://oeis.org/A001801)

Offset 0: 3, 15, 105, 315, 6930, 18018, 90090, 218790, 2078505, 4849845, 22309287, 50702925, …

### Python 3 — 54 bytes

```python
d=3;n=4
while[print(d)]:n+=1;d=d*(2*n-5)*(n&-n)//(n-4)
```

**How it works**

- **The triangle.** Row N of [A100258](https://oeis.org/A100258) holds the
  coefficients of the Legendre polynomial P_N(x) over their least common
  denominator, as in Abramowitz and Stegun: 8P₄ = 35x⁴ − 30x² + 3,
  16P₆ = 231x⁶ − 315x⁴ + 105x² − 5. Diagonal 3 is the coefficient of
  x^(N−4) in row N, for N = n + 4, in absolute value.
- **Closed form.** P_N(x) = 2⁻ᴺ Σⱼ (−1)ʲ C(N, j)·C(2N − 2j, N)·x^(N−2j), and
  the least common denominator of row N is 2^(N − s₂(N)), that of the leading
  coefficient (s₂ = binary digit sum; by Kummer's theorem the 2-adic valuation
  of C(N, j)·C(2N − 2j, N) is s₂(j) + s₂(N − 2j) ≥ s₂(N), as on
  [A001800](../A001800/)). So with j = 2:
  a(n) = C(N, 2)·C(2N − 4, N)/2^s₂(N).
- **A ratio instead of binomials.** From N − 1 to N the binomial part grows by
  C(N, 2)/C(N − 1, 2) · C(2N − 4, N)/C(2N − 6, N − 1) = 2(2N − 5)/(N − 4),
  and dividing by 2^s₂(N) instead of 2^s₂(N − 1) multiplies it by
  2^(s₂(N − 1) − s₂(N)) = 2^(v₂(N) − 1) = (N & −N)/2, since N − 1 → N turns
  v₂(N) trailing ones into a single one.
  So a(n) = a(n − 1)·(2N − 5)·(N & −N)/(N − 4), from a(0) = 3 at N = 4.
- **The program.** `n` is N and `n&-n` is its lowest set bit 2^v₂(N). The
  product is formed before the floor division, and the quotient is the
  integer a(n), so `//` is exact.

**Notes**

- Checked against the exact rational Legendre polynomials (Bonnet's
  recurrence) for N < 124, and against the b-file.
- The ratio is 22 bytes shorter than the closed form
  `n*~-n*math.comb(2*n-4,n)>>n.bit_count()+1` (with `import math`), whose
  `>>n.bit_count()` divides by 2^s₂(N).
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 7136.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001801), CC BY-SA 4.0.
