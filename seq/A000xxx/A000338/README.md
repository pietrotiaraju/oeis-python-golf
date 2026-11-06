# A000338

> Expansion of x^3*(5-2*x)*(1-x^3)/(1-x)^4.
> — [OEIS A000338](https://oeis.org/A000338)

Offset 3: 5, 18, 42, 75, 117, 168, 228, 297, 375, 462, 558, 663, …

### Python 3 — 38 bytes

```python
m=7
while[print(max(5,m*m//8-3))]:m+=6
```

**How it works**

- Since 1 − x³ = (1 − x)(1 + x + x²), the generating function is
  x³(5 + 3x + 3x² − 2x³)/(1 − x)³. The coefficient of x^k in 1/(1 − x)³ is
  C(k + 2, 2), so a(n) = 5·C(n−1, 2) + 3·C(n−2, 2) + 3·C(n−3, 2) − 2·C(n−4, 2).
  As a polynomial, C(j, 2) = j(j − 1)/2 vanishes at j = 0 and j = 1, so it is
  the true coefficient for every j ≥ 0. For n ≥ 4 all four upper indices are
  ≥ 0 and the sum is the quadratic f(n) = 3(3n − 8)(n − 1)/2.
- Completing the square, 8·f(n) = (6n − 11)² − 25. With m = 6n − 11 = 7, 13,
  19, … (odd, so m² ≡ 1 mod 8), f(n) = (m² − 1)/8 − 3, which is `m*m//8-3`.
- At n = 3 the −2·C(−1, 2) term of the polynomial is −2 instead of 0, so f(3)
  = 3 while a(3) = 5. `max(5,…)` fixes that first term: f(n) ≥ 18 > 5 for
  every n ≥ 4, so the maximum is f(n) there.

**Notes**

- `max(8,m*m>>3)-3` is the same length. Printing the first term separately,
  `print(5);m=13` + `while[print(m*m//8-3)]:m+=6`, is 41 bytes, and patching
  it with `m*m//8-3+(2>>m-7)` (2 at m = 7, 0 from m = 13 on) is 40.
- The floor of a quadratic polynomial that equals f(n) for all n ≥ 4 must
  share its n² and n terms, so it is within 1 of f(3) = 3 at n = 3 and cannot
  give 5: the first term needs a separate fix such as the `max`.
- Exact integers, so every term is right; the int-to-str limit would only be
  reached near n = 10^2150.
- The b-file has 998 terms (n = 3 to 1000) and prints at once; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000338), CC BY-SA 4.0.
