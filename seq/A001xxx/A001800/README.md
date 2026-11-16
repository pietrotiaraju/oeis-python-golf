# A001800

> Diagonal 2 of triangle A100258 comprising coefficients of Legendre polynomials.
> — [OEIS A001800](https://oeis.org/A001800)

Offset 0: 1, 3, 30, 70, 315, 693, 12012, 25740, 109395, 230945, 1939938, 4056234, …

### Python 3 — 70 bytes

```python
import math
n=2
while[print(n*math.comb(2*n-2,n)>>n.bit_count())]:n+=1
```

**How it works**

- **The triangle.** Row N of [A100258](https://oeis.org/A100258) holds the
  coefficients of the Legendre polynomial P_N(x) over their least common
  denominator, as in Abramowitz and Stegun: 8P₄ = 35x⁴ − 30x² + 3,
  16P₆ = 231x⁶ − 315x⁴ + 105x² − 5. Diagonal 2 is the coefficient of
  x^(N−2) in row N, for N = n + 2; those entries are all negative, and the
  sequence lists their absolute values.
- **The denominator.** P_N(x) = 2⁻ᴺ Σⱼ (−1)ʲ C(N, j)·C(2N − 2j, N)·x^(N−2j).
  By Kummer's theorem the 2-adic valuation of C(N, j)·C(2N − 2j, N) is
  s₂(j) + s₂(N − 2j) (s₂ = binary digit sum), which is at least
  s₂(N) = s₂(2j + (N − 2j)), the valuation of the leading term j = 0. So
  the least common denominator is that of the leading coefficient,
  2^(N − s₂(N)), and the x^(N−2) entry (j = 1) has absolute value
  N·C(2N − 2, N)/2^s₂(N), the OEIS formula
  (n + 1)·C(2n + 2, n + 1)/2^A000120(n + 2) (since
  N·C(2N − 2, N) = (N − 1)·C(2N − 2, N − 1)).
- **The program.** `n` is N, from 2; `n.bit_count()` is s₂(N) (Python 3.10+),
  and `>>` divides by 2^s₂(N) exactly. `while[print(…)]:n+=1` prints before
  each step.

**Notes**

- Checked against the exact rational Legendre polynomials (Bonnet's
  recurrence) for N < 125.
- `n*math.comb(2*n-2,n)` is 4 bytes shorter than the OEIS form
  `~-n*math.comb(2*n-2,n-1)`, and `n.bit_count()` 4 bytes shorter than
  `bin(n).count("1")`.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001800), CC BY-SA 4.0.
