# A001802

> Diagonal 4 of triangle A100258 comprising coefficients of Legendre polynomials.
> — [OEIS A001802](https://oeis.org/A001802)

Offset 0: 5, 35, 1260, 4620, 30030, 90090, 1021020, 2771340, 14549535, 37182145, 1487285800, 3650610600, …

### Python 3 — 54 bytes

```python
d=5;n=6
while[print(d)]:n+=1;d=d*(2*n-7)*(n&-n)//(n-6)
```

**How it works**

- **The triangle.** Row N of [A100258](https://oeis.org/A100258) holds the
  coefficients of the Legendre polynomial P_N(x) over their least common
  denominator, as in Abramowitz and Stegun: 8P₄ = 35x⁴ − 30x² + 3,
  16P₆ = 231x⁶ − 315x⁴ + 105x² − 5. Diagonal 4 is the coefficient of
  x^(N−6) in row N, for N = n + 6, in absolute value.
- **Closed form.** P_N(x) = 2⁻ᴺ Σⱼ (−1)ʲ C(N, j)·C(2N − 2j, N)·x^(N−2j), and
  the least common denominator of row N is 2^(N − s₂(N)), that of the leading
  coefficient (s₂ = binary digit sum; by Kummer's theorem the 2-adic valuation
  of C(N, j)·C(2N − 2j, N) is s₂(j) + s₂(N − 2j) ≥ s₂(N), as on
  [A001800](../A001800/)). So with j = 3:
  a(n) = C(N, 3)·C(2N − 6, N)/2^s₂(N).
- **A ratio instead of binomials.** From N − 1 to N the binomial part grows by
  C(N, 3)/C(N − 1, 3) · C(2N − 6, N)/C(2N − 8, N − 1) = 2(2N − 7)/(N − 6),
  and dividing by 2^s₂(N) instead of 2^s₂(N − 1) multiplies it by
  2^(s₂(N − 1) − s₂(N)) = 2^(v₂(N) − 1) = (N & −N)/2, since N − 1 → N turns
  v₂(N) trailing ones into a single one.
  So a(n) = a(n − 1)·(2N − 7)·(N & −N)/(N − 6), from a(0) = 5 at N = 6.
- **The program.** `n` is N and `n&-n` is its lowest set bit 2^v₂(N). The
  product is formed before the floor division, and the quotient is the
  integer a(n), so `//` is exact.

**Notes**

- Checked against the exact rational Legendre polynomials (Bonnet's
  recurrence) for N < 126, and against the b-file.
- The ratio is 25 bytes shorter than the closed form
  `comb(n,3)*comb(2*n-6,n)>>n.bit_count()` (with `from math import*`), whose
  `>>n.bit_count()` divides by 2^s₂(N).
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 7130.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 54 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001802), CC BY-SA 4.0.
