# A001905

> From higher-order Bernoulli numbers: absolute value of numerator of D-number D2n(2n-1).
> — [OEIS A001905](https://oeis.org/A001905)

Offset 1: 1, 17, 1835, 195013, 3887409, 58621671097, 327585142651, 83717985168643, …

### Python 3 — 121 bytes

```python
from math import*
r=[];n=3;L=1
while 1:j=0;r=[x:=L]+[x:=(j:=j+2)**2*a*n-x for a in r];L*=n;print(x//gcd(x,L//(n-2)));n+=2
```

**How it works**

- **D-numbers.** Nörlund's D-numbers are defined by
  (t/sinh t)ᵏ = Σ D₂ₙ⁽ᵏ⁾ t²ⁿ/(2n)!; here a(n) = |numerator of D₂ₙ⁽²ⁿ⁻¹⁾| for
  n ≥ 1, e.g. D₂⁽¹⁾ = −1/3, D₄⁽³⁾ = 17/5. By Lagrange inversion (x = sinh t),
  Σ D₂ₙ⁽²ⁿ⁻¹⁾ x²ⁿ/(2n)! = (x/asinh x)²/√(1 + x²), as in the entry's PARI program.
- **A derivative.** With c(x) = x/asinh x,
  x·c′ = c − (x/asinh x)²/√(1 + x²), so the e.g.f. is c − x·c′ and
  D₂ₙ⁽²ⁿ⁻¹⁾ = (1 − 2n)·[x²ⁿ/(2n)!] c.
- **An integral.** With s = asinh x, c = sinh s/s = ½∫₋₁¹ e^(θs) dθ, and the
  classical expansion e^(θs) = (x + √(1 + x²))^θ = Σ Pₘ(θ) xᵐ/m! has
  P₂ₙ(θ) = θ²·∏ⱼ₌₁ⁿ⁻¹ (θ² − (2j)²) (central factorial polynomials). So
  a(n) is the numerator of (2n − 1)·∫₀¹ θ² ∏ⱼ₌₁ⁿ⁻¹ ((2j)² − θ²) dθ, whose
  integrand is ≥ 0 on [0, 1]. For n = 2: 3·∫₀¹ θ²(4 − θ²) dθ = 3·(4/3 − 1/5) = 17/5.
- **Moments.** As in [A001904](../A001904/): Jⱼ(i) = ∫₀¹ θ²ⁱ⁺² ∏ₗ₌₁ʲ ((2l)² − θ²) dθ
  has J₀(i) = 1/(2i + 3) and Jⱼ(i) = (2j)²·Jⱼ₋₁(i) − Jⱼ₋₁(i + 1); each pass
  appends one moment and recomputes the antidiagonal, whose last entry is
  Jₙ₋₁(0) for a(n).
- **Integers.** On the pass for a(m) the program's `n` is 2m + 1, the odd
  denominator of the newest moment; `j` runs 2, 4, 6, …, and the entries are
  stored multiplied by `L` = 3·5⋯n (the old ones rescaled by `*n`, the new one
  entering as the old `L`). The value is (2m − 1)·x/L = (n − 2)·x/L; as n − 2
  divides L, its reduced numerator is `x//gcd(x,L//(n-2))`.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(200) has
  887 digits; the program stops at the 4300-digit int-to-str limit of
  Python 3.11+, first passed by a(776).
- The b-file has 200 terms (n = 1 to 200); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001905), CC BY-SA 4.0.
