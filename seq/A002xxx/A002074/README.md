# A002074

> Denominators of coefficients in an asymptotic expansion of the confluent hypergeometric function F(1-b; 2; 4b).
> — [OEIS A002074](https://oeis.org/A002074)

Offset 0: 1, 5, 35, 225, 67375, 853125, 955040625, 1861234375, 151365980390625, …

### Python 3 — 163 bytes

```python
from fractions import*
n=0
while 1:
 P=[1]
 for k in range(1,n+1):P+=sum(Fraction((2-2*n)*j-3*k,2*j+3)*P[-j]for j in range(1,k+1))/k,
 print(P[n].denominator);n+=1
```

**How it works**

- **Definition.** Irvine's formula in the entry (which reproduces Henrici's
  table, with his a(5) misprint corrected): f(x) =
  (Σ_(k≥1) 3x^(2k+1)/(2k+1))^(1/3) = x + x³/5 + 18x⁵/175 + …, g is its
  series reversion (g(y) = y − y³/5 + 3y⁵/175 − …), and the n-th term is
  the reduced fraction (2n+1)·[y^(2n+1)] g: 1, −3/5, 3/35, 2/225, ….
  The program follows this definition; it matches all listed terms of
  both [A002073](../A002073/) (numerators, signs included) and
  [A002074](../A002074/) (denominators).
- **Lagrange inversion.** (2n+1)·[y^(2n+1)] g = [x^(2n)] (x/f(x))^(2n+1)
  = [tⁿ] H(t)^α with t = x², H(t) = (f/x)³ = Σ_(j≥0) 3tʲ/(2j+3) and
  α = −(2n+1)/3.
- **Power of a series.** J. C. P. Miller's recurrence for P = H^α
  (H₀ = 1): P₀ = 1 and k·P_k = Σ_(j=1..k) ((α+1)j − k)·H_j·P_(k−j). With
  H_j = 3/(2j+3) the j-th summand is ((2−2n)j − 3k)/(2j+3)·P_(k−j)
  (`Fraction((2-2*n)*j-3*k,2*j+3)`). When `P` has k entries, `P[-j]` is
  P_(k−j). Fractions stay exact and reduced, so P_n's numerator carries
  the sign and its denominator is positive.
- **Loop.** Each n runs the recurrence from scratch up to P_n; n = 0 gives
  P = [1], whose int 1 has numerator and denominator 1.

**Notes**

- [A002073](../A002073/) is the same program with `numerator`.
- Each term costs about n²/2 fraction operations. The b-file has the 15
  terms of the entry (n = 0 to 14), and the bar is all of them in 60 s,
  which takes a fraction of a second. These few terms would fit in a
  table shorter than the program, hence the review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 163 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002074), CC BY-SA 4.0.
