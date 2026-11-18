# A001919

> Eighth column of quadrinomial coefficients.
> — [OEIS A001919](https://oeis.org/A001919)

Offset 3: 6, 40, 155, 456, 1128, 2472, 4950, 9240, 16302, 27456, 44473, 69680, …

### Python 3 — 55 bytes

```python
n=3
while[print((~-(B:=n**7)**4//~-B)**n//B**7%B)]:n+=1
```

**How it works**

- **Quadrinomial coefficients.** a(n) is the coefficient of x⁷ in
  (1 + x + x² + x³)ⁿ, n ≥ 3.
- **One big power.** Put x = B = n⁷: (1 + B + B² + B³)ⁿ = Σⱼ T(n, j)·Bʲ,
  where T(n, j) is the coefficient of xʲ. Carries only travel upwards, so if
  every T(n, j) with j ≤ 7 is below B, the base-B digit 7 is T(n, 7), read off
  by `//B**7%B`. The base polynomial 1 + B + B² + B³ is written
  (B⁴ − 1)/(B − 1), `~-(B:=n**7)**4//~-B` (`~-y` is y − 1), one byte shorter.
- **The bound.** T(n, j) is at most the number of ways to write j as an ordered
  sum of n terms ≥ 0, C(n + j − 1, j), which grows with j, so it is at most
  C(n + 6, 7) = ∏ᵢ₌₁⁷ (n − 1 + i)/i. Each factor is ≤ n and the ones with
  i ≥ 2 are < n for n ≥ 2, so T(n, j) < n⁷ = B.

**Notes**

- The closed form n(n² − 1)(n² − 4)(n² + 21n + 180)/5040 from the entry costs
  62 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 998 terms (n = 3 to 1000); the bar is the whole b-file in
  60 s, which takes a few seconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 55 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001919), CC BY-SA 4.0.
