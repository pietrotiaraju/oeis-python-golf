# A001973

> Expansion of (1+x^3)/((1-x)*(1-x^2)^2*(1-x^3)).
> — [OEIS A001973](https://oeis.org/A001973)

Offset 0: 1, 1, 3, 5, 8, 12, 18, 24, 33, 43, 55, 69, 86, 104, 126, 150, 177, 207, 241, …

### Python 3 — 42 bytes

```python
m=5
while[print((m**3+9*m+142)//288)]:m+=2
```

**How it works**

- **Closed form.** a(n) = ⌊(m³ + 9m + 142)/288⌋ with m = 2n + 5; `m` runs
  over the odd numbers from 5.
- **Why.** Since 1 + x³ = (1 + x)(1 − x + x²) and
  (1 − x)(1 + x)(1 + x + x²)(1 − x + x²) = 1 − x⁶, the generating function
  is (1 − x + x²)²/((1 − x)³(1 − x⁶)). So a(n) − a(n − 6) is the
  coefficient of xⁿ in (1 − 2x + 3x² − 2x³ + x⁴)/(1 − x)³, which is
  C(n + 2, 2) − 2C(n + 1, 2) + 3C(n, 2) − 2C(n − 1, 2) + C(n − 2, 2) =
  (n² − n + 4)/2 for n ≥ 2.
- **The formula does the same.** Lowering n by 6 lowers m by 12, and
  (m³ + 9m) − ((m − 12)³ + 9(m − 12)) = 36m² − 432m + 1836 =
  288(n² − n + 4)/2, a multiple of 288 (n² − n is even), so the floor drops
  by exactly (n² − n + 4)/2. Both sides start 1, 1, 3, 5, 8, 12 for
  n = 0, …, 5, so they agree for every n ≥ 0.
- Exact integer arithmetic throughout.

**Notes**

- Any constant from 118 to 169 works in place of 142; none has two digits.
  Written in n, ⌊(2n³ + 15n² + 42n + 78)/72⌋ (the entry's formula), it is
  50 bytes; m = 2n + 5 removes the n² term. The layered coin-change
  template of [A001300](../A001300/) is longer as well.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001973), CC BY-SA 4.0.
