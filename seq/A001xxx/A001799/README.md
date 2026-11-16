# A001799

> Coefficient of P_4(x) in the Legendre expansion of x^n.
> — [OEIS A001799](https://oeis.org/A001799)

Offset 2: 8, 72, 2160, 15504, 220248, 1564920, 89324640, 640807200, 9246847896, …

### Python 3 — 93 bytes

```python
import math
m=4
while 1:c=math.comb(2*m,m);print(c//(c&-c)*9*m*(m-2)//-~m//(m+3)//(m+5));m+=2
```

**How it works**

- **The normalization.** As in [A001795](../A001795/): xᵐ = (1/Dₘ)·Σ aₖPₖ(x)
  with integer aₖ over the least common denominator Dₘ (Abramowitz and
  Stegun, Table 22.9), e.g. x⁴ = (7P₀ + 20P₂ + 8P₄)/35. This sequence is the
  P₄ numerator for m = 2n. The Legendre coefficient is
  cₘ,₄ = 9m(m − 2)/((m + 1)(m + 3)(m + 5)), and Dₘ is the odd part of
  C(2m, m) (proved on the [A001795](../A001795/) page), so
  a(n) = Dₘ·9m(m − 2)/((m + 1)(m + 3)(m + 5)).
- **The program.** `c//(c&-c)` is the odd part of `c` = C(2m, m) (it divides
  out the lowest set bit, the whole power of 2). Dₘ·cₘ,₄ is an integer, so
  multiplying by 9m(m − 2) first and then dividing by m + 1 (`-~m`), m + 3
  and m + 5 in turn is exact. `m` runs over the even numbers from 4.

**Notes**

- Checked against the exact rational expansion of xᵐ for m < 120.
- Exact integer arithmetic, so the program is right for every n; a(n) passes
  the 4300-digit int-to-str limit near n = 3600.
- The b-file has 829 terms (n = 2 to 830); the bar is the whole b-file in
  60 s, which takes under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001799), CC BY-SA 4.0.
