# A001798

> Coefficient of P_3(x) in the Legendre expansion of x^n.
> — [OEIS A001798](https://oeis.org/A001798)

Offset 1: 2, 28, 182, 4760, 31654, 428260, 2941470, 163761840, 1152562950, 16381761396, …

### Python 3 — 83 bytes

```python
import math
m=3
while 1:c=math.comb(2*m,m);print(c//(c&-c)*7*~-m//(m*m+6*m+8));m+=2
```

**How it works**

- **The normalization.** As in [A001795](../A001795/): xᵐ = (1/Dₘ)·Σ aₖPₖ(x)
  with integer aₖ over the least common denominator Dₘ (Abramowitz and
  Stegun, Table 22.9), e.g. x⁵ = (27P₁ + 28P₃ + 8P₅)/63. This sequence is the
  P₃ numerator for odd m = 2n + 1. The Legendre coefficient is
  cₘ,₃ = 7(m − 1)/((m + 2)(m + 4)), and Dₘ is the odd part of C(2m, m)
  (proved on the [A001795](../A001795/) page), so
  a(n) = Dₘ·7(m − 1)/((m + 2)(m + 4)).
- **The program.** `c//(c&-c)` is the odd part of `c` = C(2m, m) (it divides
  out the lowest set bit, the whole power of 2). Dₘ·cₘ,₃ is an integer, so
  multiplying by 7(m − 1) (`7*~-m`) and then dividing by
  (m + 2)(m + 4) = m² + 6m + 8 is exact. `m` runs over the odd numbers
  from 3.

**Notes**

- Checked against the exact rational expansion of xᵐ for m < 120.
- The OEIS formula (14n/((2n + 3)(2n + 5)))·numerator(C(4n + 2, 2n + 1)/2⁴ⁿ)
  is the same number.
- Exact integer arithmetic, so the program is right for every n; a(n) passes
  the 4300-digit int-to-str limit near n = 3600.
- The b-file has 830 terms (n = 1 to 830); the bar is the whole b-file in
  60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001798), CC BY-SA 4.0.
