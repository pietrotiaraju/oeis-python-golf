# A001796

> Coefficient of P_1(x) in the Legendre expansion of x^n.
> — [OEIS A001796](https://oeis.org/A001796)

Offset 0: 1, 3, 27, 143, 3315, 20349, 260015, 1710855, 92116035, 631165425, 8775943605, …

### Python 3 — 73 bytes

```python
import math
m=1
while 1:c=3*math.comb(2*m,m)//(m+2);print(c//(c&-c));m+=2
```

**How it works**

- **The normalization.** As in [A001795](../A001795/): xᵐ = (1/Dₘ)·Σ aₖPₖ(x)
  with integer aₖ over the least common denominator Dₘ (Abramowitz and
  Stegun, Table 22.9), e.g. x³ = (3P₁ + 2P₃)/5. This sequence is the P₁
  numerator for odd m = 2n + 1. The Legendre coefficient is
  cₘ,₁ = 3/(m + 2), and Dₘ is the odd part of C(2m, m) (proved on the
  [A001795](../A001795/) page), so a(n) = odd part of C(2m, m) · 3/(m + 2).
- **The program.** Since 3 and m + 2 are odd, that is the odd part of
  3·C(2m, m)/(m + 2), an integer; `c//(c&-c)` divides out the lowest set bit
  of `c`, i.e. the whole power of 2. `m` runs over the odd numbers.

**Notes**

- Checked against the exact rational expansion of xᵐ for m < 120.
- The OEIS formula numerator(3·C(2n + ½, n)/(2n + 3)) is the same number.
- Exact integer arithmetic, so the program is right for every n; a(n) passes
  the 4300-digit int-to-str limit near n = 3600.
- The b-file has 831 terms (n = 0 to 830); the bar is the whole b-file in
  60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001796), CC BY-SA 4.0.
