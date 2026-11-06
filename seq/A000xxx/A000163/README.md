# A000163

> Series-parallel numbers.
> — [OEIS A000163](https://oeis.org/A000163)

Offset 2: 2, 8, 34, 136, 538, 2080, 7970, 30224, 113874, 426520, …

### Python 3 — 160 bytes

```python
R=[n:=1]
while[print(2*(Q:=sum(R[i]<<3*n*i for i in range(n)))*pow(2-Q,-3,M:=8**n**2)%M>>3*n*~-n)]:R+=sum(R+[d*R[d]*sum(R[-d::-d])for d in range(1,n)])//n,;n+=1
```

**How it works**

- `R` lists the series-parallel network counts F(x) = 1 + S(x)
  (1, 1, 2, 4, 10, … with A000084 after the leading 1). They satisfy
  F = ∏_k (1−x^k)^(−b_k) with b_1 = 1 and b_k = F_k/2 for k ≥ 2 (A000669).
  The log-derivative of the product gives
  n·F_n = Σ_{k<n} F_k + Σ_{d=1..n−1} d·F_d·Σ_{m≥1, dm≤n} F_{n−dm}: the
  first sum is the extra weight of d = 1 (b_1 = 1 but F_1/2 = ½), and
  `R[-d::-d]` walks F_{n−d}, F_{n−2d}, … down to F_0. Since b_n is not in
  the list yet, the d = n term is left out, which is what solving for F_n
  needs.
- a(m+2) is the coefficient of x^m in 2(1+S)/(1−S)³ = 2F/(2−F)³. All
  series coefficients up to x^m are packed into one integer
  Q = Σ F_i·X^i with X = 2^(3n), n = m+1. Modulo M = X^n the map x ↦ X is
  a ring map on series truncated at x^n, and 2−Q is odd, so
  `2*Q*pow(2-Q,-3,M)%M` is 2·Σ_{k≤m} V_k·X^k, V = F/(2−F)³, as long as
  every 2V_k < X. The top digit, `>>3*n*~-n`, is a(m+2).
- No digit overflows: the coefficients are positive, so
  V_m ≤ V(¼)·4^m. S is increasing and reaches 1 at x = 1/d, where
  d = 3.5608… is the growth constant of A000084, so S(¼) ≈ 0.562 < 1,
  V(¼) ≈ 18.6 and 2V_m < 38·4^m < 8^(m+1) for m ≥ 3; m = 0, 1, 2 give
  2, 8, 34.
- `M:=8**n**2` is a byte under `M:=1<<3*n*n`, and `R[i]<<3*n*i for i in
  range(n)` is three under `enumerate`.

**Notes**

- Exact integer arithmetic, correct for every n. The modular inverse of a
  3n²-bit number dominates: about 215 terms come out in 60 s on the
  machine that set the bar, which is 160 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 160 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000163), CC BY-SA 4.0.
