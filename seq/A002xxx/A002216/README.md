# A002216

> Harary-Read numbers: restricted hexagonal polyominoes (cata-polyhexes) with n cells.
> — [OEIS A002216](https://oeis.org/A002216)

Offset 0: 0, 1, 1, 2, 5, 12, 37, 123, 446, 1689, 6693, 27034, …

### Python 3 — 130 bytes

```python
L=[9,14];n=0
while[print((6*L[n]-5*L[n-1]-L[-1]+(9+n%2*6)*L[n//2]+n%3%2*4*L[n//3])//168)]:L+=((6*n+9)*L[-1]-5*n*L[n])//(n+3),;n+=1
```

**How it works**

- **Generating function.** The entry's g.f. is
  (1/(24x²))(12 + 24x − 48x² − 24x³ + S(x)³ − 3(3 + 5x)S(x²) − 4S(x³)),
  S(x) = √((1 − x)(1 − 5x)); it says a(n) = (a₁(n) + a₂(n))/2 with
  a₁ = [A002214](../A002214/), a₂ = [A002215](../A002215/) (Harary and
  Read 1970). Write A(x) = Σ Aₖxᵏ = 1, 1, 3, 10, … for the g.f. of
  [A002212](../A002212/); then 2xA = 1 − x − S, so the coefficients of S
  are 1, −3 and then sₖ = −2Aₖ₋₁ for k ≥ 2.
- **Coefficients.** S³ = (1 − 6x + 5x²)S, and reading off x^(n+2) for
  n ≥ 2 (the polynomial part stops at x³):
  12a(n) = 6Aₙ − 5Aₙ₋₁ − Aₙ₊₁ + (9 + 6[n odd])A⌊ₙ/₂⌋ +
  4[n ≡ 1 mod 3]A₍ₙ₋₁₎/₃.
  The same comes out of the A002214 and A002215 pages' formulas added
  together.
- **n = 0, 1 for free.** Replace A₀ by 9/14: at n = 1 the formula gives
  (−3/14 + 135/14 + 36/14) = 12, so 12a(1) = 12. At n = 0 the program
  reads `L[n-1]` = `L[-1]`, the last entry, here 14A₁, and the numerator
  is 6·9 − 5·14 − 14 + 9·9 = 51, whose floor over 168 is 0 = a(0). A₀
  enters nowhere else, because the A002212 recurrence
  (k + 1)Aₖ = 3(2k − 1)Aₖ₋₁ − 5(k − 2)Aₖ₋₂ (proved on
  [its page](../A002212/)) multiplies it by 0 at k = 2. So `L` = 14A
  with `L[0]` = 9, and the divisor is 12·14 = 168.
- **The loop.** At step n, `L` holds 14A₀ … 14Aₙ₊₁: `L[n]`, `L[n-1]`,
  `L[-1]` are 14Aₙ, 14Aₙ₋₁, 14Aₙ₊₁. After the print the body appends
  14Aₙ₊₂ (the recurrence with k = n + 2) and steps n. `n%3%2` is 1 only
  for n%3 = 1, and then (n − 1)/3 = n//3.

**Notes**

- Exact integers: right for every n. The whole b-file (201 terms, n = 0
  to 200) comes in a few hundredths of a second; the bar is all of it in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 130 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002216), CC BY-SA 4.0.
