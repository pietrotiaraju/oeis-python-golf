# A000465

> Number of bipartite partitions of n white objects and 4 black ones.
> — [OEIS A000465](https://oeis.org/A000465)

Offset 0: 5, 12, 29, 57, 109, 189, 323, 522, 831, 1279, …

a(n) counts the multisets of pairs (i, j) ≠ (0, 0) of nonnegative integers
with Σi = n and Σj = 4: the ways to split n identical white and 4 identical
black objects into nonempty unordered parts.

### Python 3 — 138 bytes

```python
a=[1];n=0
while[print(sum(map(int.__mul__,(5,2,0,-3,-5,-1,0,3,1,-1),a[::-1])))]:n-=1;a+=sum(sum(a[d::d])*d<<(d>-5)for d in range(n,0))//n,
```

**How it works**

- **The generating function.** The bivariate g.f. is
  Π_{(i,j)≠(0,0)} (1 − xⁱyʲ)⁻¹. For a fixed j ≥ 1, Euler's identity
  Π_{i≥0} (1 − z·xⁱ)⁻¹ = Σ_m z^m/D_m(x), with z = yʲ and
  D_m = (1−x)(1−x²)…(1−x^m), shows that a black partition λ of 4 with m_j
  parts j contributes P(x)/Π_j D_(m_j), where P = Π_{i≥1}(1−xⁱ)⁻¹ comes
  from j = 0. The five partitions 4, 3+1, 2+2, 2+1+1, 1+1+1+1 give
  A(x) = P·(1/D₁ + 1/D₁² + 1/D₂ + 1/(D₁D₂) + 1/D₄).
- **One denominator.** Every 1 − xⁱ is divisible by 1 − x, so each of the
  five denominators divides D₄, and A = N·P/D₄ with the polynomial
  N = 5 + 2x − 3x³ − 5x⁴ − x⁵ + 3x⁷ + x⁸ − x⁹ (computed exactly; N is the
  tuple in the program). So a(m) = Σ_{k=0}^{9} N_k·e(m−k), where e(m) are
  the coefficients of P/D₄.
- **P/D₄ as an Euler product.** P/D₄ = Π_i (1 − xⁱ)^(−b_i) with b_i = 2
  for i ≤ 4 and 1 above. The logarithmic derivative gives
  m·e(m) = Σ_{d≥1} d·b_d·Σ_{j≥1} e(m − jd), the
  [A000041](../A000041/) recurrence with weights.
- **The code.** Before the append, `a` holds e(0), …, e(m−1), n = −m and
  d = −k runs over −m, …, −1, so `a[d::d]` is e(m−k), e(m−2k), ….
  `sum(…)*d<<(d>-5)` is −k·Σ shifted left once when k ≤ 4, that is
  −k·b_k·Σ (a left shift of a negative number doubles it), and the total
  is −m·e(m), so `//n` is exact. The print takes the dot product of N with
  e(m), e(m−1), …; `map` stops at the shorter list, which handles m < 9.

**Notes**

- Other versions that print the same terms:
  - the original layout, P from the same recurrence and the filters
    1/(1 − x^r) as running queues,
    `T=[L.append(t:=t+L.pop(0))or t for L in Q]` with H₁ + H₂ + H₄ +
    (H₁ + H₂)/(1 − x), H_r = P/D_r: 187 bytes; with the four queues in one
    list `Z` (`Z.append(t:=t+Z[-4*r])or t for r in(1,2,3,4)`): 165 bytes;
  - the denominator (1−x)·D₄ with weights b = 3, 2, 2, 2, 1, … and an
    11-term numerator: 152 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 5001 terms take about 25 s here; term m costs about
  m·ln m big additions. The b-file has 5001 terms (up to a(5000)); the
  bar is the whole b-file in 60 s.
- a(n) grows like e^(π√(2n/3)) times a power of n, so the 4300-digit
  limit is only reached near n = 1.5·10⁷.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 284 | first entry |
| 2026-11-06 | Python 3 | 272 | use sumprod on padded coefficient history and combine queue updates |
| 2026-11-06 | Python 3 | 187 | accumulate the four black-partition filters directly |
| 2026-11-07 | Python 3 | 138 | A = N·P/D₄, weighted Euler transform and a 10-term dot product |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000465), CC BY-SA 4.0.
