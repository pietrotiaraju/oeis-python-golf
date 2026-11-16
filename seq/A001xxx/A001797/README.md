# A001797

> Coefficient of P_2(x) in the Legendre expansion of x^n.
> — [OEIS A001797](https://oeis.org/A001797)

Offset 1: 2, 20, 110, 2600, 16150, 208012, 1376550, 74437200, 511755750, 7134913500, …

### Python 3 — 80 bytes

```python
import math
m=2
while 1:c=math.comb(2*m,m);print(c//(c&-c)*5*m//-~m//(m+3));m+=2
```

**How it works**

- **The normalization.** As in [A001795](../A001795/): xᵐ = (1/Dₘ)·Σ aₖPₖ(x)
  with integer aₖ over the least common denominator Dₘ (Abramowitz and
  Stegun, Table 22.9), e.g. x⁴ = (7P₀ + 20P₂ + 8P₄)/35. This sequence is the
  P₂ numerator for m = 2n. The Legendre coefficient is
  cₘ,₂ = 5m/((m + 1)(m + 3)), and Dₘ is the odd part of C(2m, m) (proved on
  the [A001795](../A001795/) page), so a(n) = Dₘ·5m/((m + 1)(m + 3)).
- **The program.** `c//(c&-c)` is the odd part of `c` = C(2m, m) (it divides
  out the lowest set bit, the whole power of 2). Dₘ·cₘ,₂ is an integer, so
  multiplying by 5m first and then dividing by m + 1 (`-~m`) and by m + 3 is
  exact. `m` runs over the even numbers from 2.

**Notes**

- The power of 2 must go before the factor m, which is even: the odd part
  of 5m·C(2m, m)/((m + 1)(m + 3)) would drop the 2s of m.
- Checked against the exact rational expansion of xᵐ for m < 120.
- Exact integer arithmetic, so the program is right for every n; a(n) passes
  the 4300-digit int-to-str limit near n = 3600.
- The b-file has 830 terms (n = 1 to 830); the bar is the whole b-file in
  60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 80 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001797), CC BY-SA 4.0.
