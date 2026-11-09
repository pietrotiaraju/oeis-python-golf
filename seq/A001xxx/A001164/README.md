# A001164

> Stirling's formula: denominators of asymptotic series for Gamma function.
> — [OEIS A001164](https://oeis.org/A001164)

Offset 0: 1, 12, 288, 51840, 2488320, 209018880, 75246796800, …

### Python 3 — 172 bytes

```python
from fractions import*
h=[Fraction(1)];d=1
while 1:
 k=len(h)
 if k%2:print((h[-1]*d).denominator);d*=k
 h+=[(h[-1]/k-sum(h[-j]*h[j]/(j+1)for j in range(1,k)))*(k+1)/(k+2)]
```

**How it works**

- Γ(z) ~ √(2π) z^(z−1/2) e^(−z) Σ cₙ z⁻ⁿ with c₀, c₁, c₂, … = 1, 1/12,
  1/288, −139/51840, …; the program prints the denominators.
- Laplace's method: with t = zs, Γ(z+1) = z^(z+1) e^(−z) ∫ e^(−z(s−1−log s)) ds.
  Put s − 1 − log s = u²/2, with s(u) increasing through s(0) = 1. Then the
  integral is ∫ e^(−zu²/2) s′(u) du, and term by term (Watson's lemma)
  ∫ e^(−zu²/2) u²ⁿ du = √(2π/z) (2n−1)!! z⁻ⁿ while odd powers give 0. Since
  Γ(z+1) = zΓ(z) the series is the same, so cₙ = (2n−1)!! h₂ₙ, where
  hₖ = [uᵏ] s′(u).
- Differentiating s − 1 − log s = u²/2 gives s′(s − 1) = us. With
  s − 1 = Σ h_(j−1) uʲ/j, the coefficient of u^(k+1) reads
  hₖ(1 + 1/(k+1)) + Σ_(j=1..k−1) h_(k−j) hⱼ/(j+1) = h_(k−1)/k, so
  hₖ = (h_(k−1)/k − Σ …)·(k+1)/(k+2) from h₀ = 1. This is Peter Luschny's
  formula in the OEIS entry; with k = len(h), `h[-j]` is h_(k−j).
- Each time h has an even index on top (len(h) odd), the program prints the
  denominator of h₂ₙ·d, where d = (2n−1)!! is kept up to date by `d*=k`.
  `Fraction` keeps everything exact and in lowest terms, with the sign in
  the numerator.

**Notes**

- No Bernoulli numbers are needed. The work grows like the square of the
  index, with long rationals: the whole b-file (296 terms) prints in about
  15 s here.
- The same program with `.numerator` gives [A001163](../A001163/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001164), CC BY-SA 4.0.
