# A000259

> Number of certain rooted planar maps.
> — [OEIS A000259](https://oeis.org/A000259)

Offset 1: 1, 3, 13, 63, 326, 1761, 9808, 55895, 324301, 1908878, 11369744, …

### Python 3 — 67 bytes

```python
m=3
while[print(((B:=4**m)-3<<3*m*m-m)//(B*B+~B)//(B-1)**m%B)]:m+=2
```

**How it works**

- The generating function. Write R = x/(1−R)² (so x = R(1−R)²). Then
  Σ a(n)xⁿ = R/(1−R−R²), which is van Hoeij's g.f. on the OEIS page.
  It is also Weiner's proved formula
  a(n) = Σ_k (−1)^(k−1) C(3n, n−k)·(k/n)·F(k−2). That sum is [xⁿ] of
  u(1+u)/(1+u−u²) with u = x(1+u)³, by Lagrange inversion, and putting
  u = R/(1−R) turns it into R/(1−R−R²).
- The coefficient formula. Lagrange inversion in the form
  [xⁿ] K(R) = [tⁿ] K(t)·φ(t)ⁿ·(1 − tφ′(t)/φ(t)), with φ(t) = (1−t)⁻², gives

  a(n) = [t^(n−1)] f(t),  f(t) = (1−3t) / ((1−t−t²)(1−t)^(2n+1)).

  Here 1 − tφ′/φ = (1−3t)/(1−t), and the factor t in R/(1−R−R²) moves the
  index down by one.
- Reading the coefficient off one integer. Let e_j be the coefficients of
  f and set t = 1/B. Then

  B^(n−1)·f(1/B) = Σ_{j<n} e_j·B^(n−1−j) + T,  T = Σ_{j≥n} e_j·B^(n−1−j).

  If 0 ≤ T < 1, the integer part is that sum, and its last base-B digit is
  e_{n−1} = a(n) (since 0 ≤ a(n) < B). Clearing denominators gives
  B^(n−1)·f(1/B) = (B−3)·B^(3n+1) / ((B²−B−1)·(B−1)^(2n+1)). Two floor
  divisions in a row equal one floor division by the product, so
  `…//(B*B+~B)//(B-1)**m%B` is that digit.
- Golf. The loop runs over m = 2n+1 with B = 4^m = 2^(2m). Then
  B^(3n+1) = 2^(m(3m−1)) is the shift `<<3*m*m-m`, and (B−1)^(2n+1) is
  just `(B-1)**m`. `B*B+~B` is B² − B − 1 (`~B` = −B−1). That is 1 byte
  under `B*B-B-1`.

**Why 0 ≤ T < 1** (τ = golden ratio)

- Lower end. The same Lagrange formula with K = 1/(1−t−t²) gives
  e_n = [xⁿ] Σ F(k+1)·R^k. Every [xⁿ]R^k is ≥ 0 and [xⁿ]Rⁿ = 1, so
  e_n ≥ F(n+1) ≥ 1.
- Size of the coefficients. e_j = Σ_i F(j−i+1)·d_i, where d_i is the
  coefficient of (1−3t)(1−t)^(−2n−1), so |d_i| ≤ 4·C(2n+i, i). With
  F(k+1) ≤ τ^k and Σ_i C(2n+i, i)·τ^(−i) = (1−1/τ)^(−2n−1) = τ^(4n+2),
  this gives |e_j| ≤ 4τ^(j+4n+2).
- So everything in T after e_n/B adds up to at most
  4τ^(5n+3)/(B(B−τ)). This is below 1/B ≤ e_n/B once
  4τ^(5n+3) < 4·16ⁿ − τ, which holds for n ≥ 4 (τ⁵ ≈ 11.09 < 16).
  So T > 0. Also T ≤ 4τ^(5n+2)/B + (that tail) < 0.61 for n ≥ 4. The same
  bound gives a(n) < B. Terms n ≤ 3 (and the whole b-file) were checked
  directly.

**Other versions**

- 73 bytes, and faster (568 terms in 60 s here):
  `n=1` / `while[print(((C:=8**n+1)-3)*C**(3*n)//(C*C+~C)>>6*n*n&C-2|2>>n)]:n+=1`.
  This uses the ternary-tree variable u = x(1+u)³ instead. Here
  a(n) = [t^(n−1)] (1−2t)(1+t)^(3n)/(1+t−t²). That is a binomial power, so
  B + 1 = C is the walrus variable and dividing by B^(2n) is a shift. In
  other words, a(n) = Σ_{k=1..n} (−1)^(k−1)·L(k)·C(3n, n−k), with Lucas
  numbers L and no division by n. The catch is n = 1: the series there is
  1 − 2t² − 3t³ − …, so the part after the digit is negative and the floor
  gives 0. `|2>>n` patches that one term, and the patch costs more than the
  R form saves.
- A P-recurrence needs order 3 with degree-5 coefficients (no order 2 up to
  degree 11), far longer.

**Notes**

- Exact integer arithmetic, correct for every n (the bound above). It gets
  448 terms in 60 s locally (the division by (B−1)^m dominates), and the
  bar is 350. Terms pass the 4300-digit int-to-str limit of Python 3.11+
  only near n ≈ 5200, far beyond what fits in the time.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000259), CC BY-SA 4.0.
