# A001795

> Coefficient of P_0(x) in the Legendre expansion of x^n.
> — [OEIS A001795](https://oeis.org/A001795)

Offset 0: 1, 1, 7, 33, 715, 4199, 52003, 334305, 17678835, 119409675, 1641030105, …

### Python 3 — 69 bytes

```python
import math
n=0
while 1:c=math.comb(2*n,n)//-~n;print(c//(c&-c));n+=2
```

**How it works**

- **The normalization.** Write xᵐ in Legendre polynomials,
  xᵐ = Σ cₘ,ₖ Pₖ(x) over k ≡ m (mod 2), with
  cₘ,ₖ = (2k + 1)·m(m − 1)⋯(m − k + 1) / ((m − k + 1)(m − k + 3)⋯(m + k + 1)).
  The tables this sequence comes from (Abramowitz and Stegun, Table 22.9) put
  the cₘ,ₖ over their least common denominator Dₘ,
  xᵐ = (1/Dₘ)·Σ aₖPₖ: x⁴ = (7P₀ + 20P₂ + 8P₄)/35, x⁶ = (33P₀ + 110P₂ + 72P₄ +
  16P₆)/231. This sequence is the P₀ numerator for m = 2n, a(n) = D₂ₙ·c₂ₙ,₀ =
  D₂ₙ/(2n + 1); [A001797](../A001797/) and [A001799](../A001799/) are the
  P₂ and P₄ numerators, [A001796](../A001796/) and [A001798](../A001798/) the
  P₁ and P₃ ones for odd m.
- **The denominator.** Dₘ is the odd part of C(2m, m). The top coefficient
  cₘ,ₘ = 2ᵐ/C(2m, m) has exactly that reduced denominator, since
  C(2m, m) has 2-adic valuation s₂(m) ≤ m. No other cₘ,ₖ needs more. With
  j = (m − k)/2 and s = (m + k)/2,
  cₘ,ₖ = (2k + 1)·2ᵏ·m!·s! / (j!·(2s + 1)!). Its 2-adic valuation is
  v₂(m!) − v₂(j!) − j ≥ 0 because m ≥ 2j. For an odd prime p, Legendre's
  formula splits v_p(cₘ,ₖ·C(2m, m)) into one term per power q = pⁱ,
  ⌊m/q + ½⌋ − ⌊j/q⌋ − ⌊s/q + ½⌋ − [q | 2s + 1] + [q | 2k + 1], using
  ⌊2x⌋ − ⌊x⌋ = ⌊x + ½⌋. Because m/q = s/q + j/q, the floors give at least
  0, and at least 1 when q | 2s + 1 and q ∤ j: then s/q + ½ is
  1/(2q) short of an integer and j/q adds at least 1/q. If q divides both
  2s + 1 and j, it also divides 2k + 1 = 2s + 1 − 2j. So every term is
  ≥ 0, and Dₘ·cₘ,ₖ is an integer for every k.
- **The program.** a(n) is the odd part of C(4n, 2n)/(2n + 1), the Catalan
  number C₂ₙ, as on the OEIS page (numerator of C₂ₙ/4ⁿ). `n` runs over the
  even numbers, `math.comb(2*n,n)//-~n` is the Catalan number Cₙ, and
  `c//(c&-c)` divides out its lowest set bit, the whole power of 2.

**Notes**

- Checked against the exact rational expansion of xᵐ for m < 120, including
  Dₘ = odd part of C(2m, m).
- `-~n` is n + 1; `import math` with one `math.comb` is 1 byte shorter than
  `from math import*`.
- Exact integer arithmetic, so the program is right for every n; a(n) passes
  the 4300-digit int-to-str limit near n = 3600.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001795), CC BY-SA 4.0.
