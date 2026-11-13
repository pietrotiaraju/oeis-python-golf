# A001568

> Related to 3-line Latin rectangles.
> — [OEIS A001568](https://oeis.org/A001568)

Offset 1: 1, −1, −1, 2, 49, 629, 6961, 38366, −1899687, −133065253, …

### Python 3 — 96 bytes

```python
P=[];d=0;u=v=s=1
while[print(s)]:k=d;d+=1;u,v=v,-v-2*k*u;P=[s:=v]+[s:=s+d*(k:=k-1)*p for p in P]
```

**How it works**

- **What the terms are.** Kerawala (1947) and Riordan expanded the
  number of 3 × n Latin rectangles: with c(n) = A000186(n)/n!² (first
  row fixed, so this is the count divided by n!³),
  c(n) ~ e⁻³·Σ_m a(m+1)/(m!·nᵐ) = e⁻³(1 − 1/n − 1/(2!n²) + 2/(3!n³) +
  49/(4!n⁴) + …). The entry gives no formula; its Sage program solves
  for the coefficients one at a time from a recurrence of A000186, and
  the program here follows the same principle in a better basis. It
  matches all 18 terms of the entry, signs included.
- **The recurrence.** [A000186](../../A000xxx/A000186/)'s page derives
  u_n = n·u_(n−1) + u_(n−2) + 2u_(n−3) + E_n for u_n = A000186(n)/n!,
  with E_n the coefficients of (1 − 2x)e^(2x)/(1 + x), which are
  bounded. Dividing by n!:
  c(n) = c(n−1) + c(n−2)/(n(n−1)) + 2c(n−3)/(n(n−1)(n−2)) + E_n/n!.
  The last term is below every power of n, so the expansion
  e³c(n) ≈ Σ β_m·n⁻ᵐ satisfies the recurrence formally; in the
  coefficient of n^(−m−1), β_m appears only as −m·β_m, so β₀ = 1 fixes
  every β_m, and a(m+1) = m!·β_m.
- **A basis that diagonalises it.** With φ_r(n) = (n−r)!/n! =
  1/(n(n−1)⋯(n−r+1)): φ_r(n) − φ_r(n−1) = −r·φ_(r+1)(n),
  φ_r(n−2)/(n(n−1)) = φ_(r+2)(n) and φ_r(n−3)/(n(n−1)(n−2)) =
  φ_(r+3)(n). So Σ g_r·φ_r(n) solves the formal recurrence exactly when
  r·g_r = −g_(r−1) − 2g_(r−2), that is **Σ g_r·x^r = e^(−x−x²)**.
- **Back to powers of 1/n.** φ_r(n) = Σ_(m≥r) S₂(m−1, r−1)·n⁻ᵐ for
  r ≥ 1 (the Stirling g.f. Σ_m S₂(m, k)t^m = t^k/Π_(i≤k)(1 − it)), so
  β_m = Σ_r g_(r+1)·S₂(m−1, r). For example
  a(5) = 4!·(g₂·1 + g₃·3 + g₄·1) = 24·(−1/2 + 5/2 + 1/24) = 49.
- **A transposed Stirling table.** Let L(0, r) = g_(r+1) and
  L(j+1, r) = L(j, r+1) + r·L(j, r). With ℓ_j(y) = Σ_r L(j, r)y^r/r!
  the rule is ℓ_(j+1) = (1 + y)ℓ_j′, which is d/dx after y = e^x − 1,
  so L(j, 0) is the j-th derivative at 0 of
  ℓ₀(e^x − 1) = Σ_r g_(r+1)(e^x − 1)^r/r!, i.e. Σ_r g_(r+1)·S₂(j, r) =
  β_(j+1).
- **Antidiagonals.** Along D = j + r, scaled to integers,
  X_j = (D+1)!·L(j, D − j): X₀ = G_(D+1) with G_k = k!·g_k (1, −1, −1,
  5, 1, −41, …, G_k = −G_(k−1) − 2(k−1)G_(k−2)), and
  X_j = X_(j−1) + (D+1)(D − j)·P_(j−1) with P the previous antidiagonal.
  The last weight is 0 and X_D = (D+1)!·β_(D+1) = a(D+2) is where the
  running sum `s` ends.
- **The code.** `s=1` prints a(1). A pass takes k = D, then d = D + 1;
  `u,v` become G_D, G_(D+1) (the starting u is never used, since it is
  multiplied by k = 0); `d*(k:=k-1)` counts the weights down
  (D+1)(D−1), …, (D+1)·0.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (18 terms, up to a(18)) prints at once; the program
  reaches a(989) in about 2 s, where the next term passes Python's
  4300-digit int-to-str limit and it stops with a ValueError.
- The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 96 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001568), CC BY-SA 4.0.
