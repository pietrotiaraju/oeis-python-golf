# A001904

> From higher order Bernoulli numbers: absolute value of numerator of D Number D2n(2n).
> — [OEIS A001904](https://oeis.org/A001904)

Offset 0: 1, 2, 88, 3056, 319616, 18940160, 94645408768, 526713485312, …

### Python 3 — 113 bytes

```python
from math import*
r=[];n=L=1
while 1:j=-1;r=[x:=L]+[x:=(j:=j+2)**2*a*n-x for a in r];L*=n;print(x//gcd(x,L));n+=2
```

**How it works**

- **D-numbers.** Nörlund's D-numbers are defined by
  (t/sinh t)ᵏ = Σ D₂ₙ⁽ᵏ⁾ t²ⁿ/(2n)!; here a(n) = |numerator of D₂ₙ⁽²ⁿ⁾|, e.g.
  D₂⁽²⁾ = −2/3, D₄⁽⁴⁾ = 88/15. By Lagrange inversion (x = sinh t) their e.g.f.
  is (x/asinh x)/√(1 + x²), as the entry says.
- **An integral.** With s = asinh x, x/asinh x = sinh s/s = ½∫₋₁¹ e^(θs) dθ,
  and e^(θs)/√(1 + x²) = (1/θ)·d/dx e^(θs). The classical expansion
  (x + √(1 + x²))^θ = e^(θs) = Σ Pₘ(θ) xᵐ/m! has
  P₂ₙ₊₁(θ) = θ·∏ⱼ₌₁ⁿ (θ² − (2j − 1)²) (central factorial polynomials), so the
  coefficient of x²ⁿ/(2n)! is ½∫₋₁¹ ∏(θ² − (2j − 1)²) dθ. Hence
  |D₂ₙ⁽²ⁿ⁾| = ∫₀¹ ∏ⱼ₌₁ⁿ ((2j − 1)² − θ²) dθ, whose integrand is positive on [0, 1).
  For n = 2 this is ∫₀¹ (1 − θ²)(9 − θ²) dθ = 1/5 − 10/3 + 9 = 88/15.
- **Moments.** Let Jⱼ(i) = ∫₀¹ θ²ⁱ ∏ₗ₌₁ʲ ((2l − 1)² − θ²) dθ. Then
  J₀(i) = 1/(2i + 1) and Jⱼ(i) = (2j − 1)²·Jⱼ₋₁(i) − Jⱼ₋₁(i + 1), and the answer
  is Jₙ(0). Pass n builds the antidiagonal J₀(n), J₁(n − 1), …, Jₙ(0) from the
  previous one, like a Seidel triangle: each new entry is (2j − 1)² times the
  old entry j − 1 minus the new entry j − 1, and the last one is Jₙ(0).
- **Integers.** The entries of antidiagonal m are stored multiplied by
  1·3·5⋯(2m + 1). On the pass for a(m) the program's `n` is the odd number
  2m + 1 and `L` the product of the odd numbers below it, so the new first
  entry 1/(2m + 1) becomes `L` and the old entries are rescaled by `*n`; `j`
  runs 1, 3, 5, …, so `(j:=j+2)**2` is (2j − 1)². After `L*=n`, `x` is
  Jₘ(0)·L and `x//gcd(x,L)` its reduced numerator.

**Notes**

- Exact integer arithmetic, so the program is right for every n; a(200) has
  887 digits; the program stops at the 4300-digit int-to-str limit of
  Python 3.11+, first passed by a(776).
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001904), CC BY-SA 4.0.
