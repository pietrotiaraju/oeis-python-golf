# A001922

> Numbers k such that 3*k^2 - 3*k + 1 is both a square (A000290) and a centered hexagonal number (A003215).
> — [OEIS A001922](https://oeis.org/A001922)

Offset 0: 1, 8, 105, 1456, 20273, 282360, 3932761, 54776288, 762935265, 10626317416, …

### Python 3 — 37 bytes

```python
a=b=0
while[print(a:=a-~b)]:b+=12*a-6
```

**How it works**

- **One condition.** The centered hexagonal numbers
  ([A003215](https://oeis.org/A003215)) are exactly the values
  3k² − 3k + 1 for k ≥ 1, so the second condition always holds and the
  terms are the k ≥ 1 for which 3k² − 3k + 1 = m² is a square.
- **Pell equation.** 4(3k² − 3k + 1) = 3(2k − 1)² + 1, so the condition is
  X² − 3Y² = 1 with X = 2m, Y = 2k − 1 > 0. Its solutions with X, Y ≥ 0 are
  X + Y√3 = (2 + √3)ʲ, j ≥ 0: Y = 0, 1, 4, 15, 56, 209, …, with
  Xⱼ₊₁ = 2Xⱼ + 3Yⱼ and Yⱼ₊₁ = Xⱼ + 2Yⱼ. Mod 2 this swaps the parities, so X
  is even exactly when j is odd, and then Y is odd. The terms are therefore
  k = (Y₂ₙ₊₁ + 1)/2: 1, 8, 105, …
- **Recurrence.** Yⱼ₊₂ = 4Yⱼ₊₁ − Yⱼ, so Y₂ₙ₊₃ = 14Y₂ₙ₊₁ − Y₂ₙ₋₁ and
  a(n + 1) = 14a(n) − a(n − 1) − 6, with a(0) = 1, a(1) = 8. The entry's
  closed forms (the order-3 recurrence 15, −15, 1 and the formula with
  7 ± 4√3) are the same sequence; all 801 terms of the b-file agree.
- **Program.** With printed values xₙ and bₙ the value of `b` after pass n,
  `a:=a-~b` is xₙ₊₁ = xₙ + bₙ + 1 and `b+=12*a-6` is
  bₙ = bₙ₋₁ + 12xₙ − 6; subtracting xₙ − xₙ₋₁ − 1 = bₙ₋₁ gives
  xₙ₊₁ = 14xₙ − xₙ₋₁ − 6. The start `a=b=0` gives x₀ = 1, b₀ = 6, x₁ = 8.

**Notes**

- a(n) = [A001921](../A001921/)(n) + 1, and m runs through
  [A001570](../A001570/). The start `a=b=0` needs the + 1 in `a-~b`
  (a + b + 1); `a=1;b=7` / `a+=b;b+=12*a-6` is 38 bytes.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 3760.
- The b-file has 801 terms (n = 0 to 800); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001922), CC BY-SA 4.0.
