# A002248

> Number of points on y^2 + xy = x^3 + x^2 + x over GF(2^n).
> — [OEIS A002248](https://oeis.org/A002248)

Offset 1: 2, 8, 14, 16, 22, 56, 142, 288, 518, 968, 1982, 4144, 8374, 16472, …

### Python 3 — 46 bytes

```python
a=p=2;b=1
while[print(p+1-b)]:a,b=b,b-2*a;p*=2
```

**How it works**

- **The curve.** E: y² + xy = x³ + x² + x has discriminant −39, odd, so it
  is an elliptic curve over GF(2). Its points over GF(2) are (0, 0) and
  the point at infinity (x = 1 would need y² + y = 1, which has no root
  in GF(2)), so N₁ = 2 and the trace of Frobenius is t = 2 + 1 − N₁ = 1.
- **Weil.** For an elliptic curve over GF(q) with N₁ = q + 1 − t points,
  the number of points over GF(qⁿ) is Nₙ = qⁿ + 1 − (αⁿ + βⁿ), where α
  and β are the roots of x² − tx + q (Hasse; the zeta function of the
  curve). Here x² − x + 2, so sₙ = αⁿ + βⁿ obeys sₙ = sₙ₋₁ − 2sₙ₋₂ with
  s₀ = 2, s₁ = 1: that is [A002249](../A002249/), and
  a(n) = 2ⁿ + 1 − sₙ, the formula in the entry.
- **The program.** (a, b) holds (sₙ₋₁, sₙ) and p = 2ⁿ; the loop prints
  p + 1 − sₙ, then `a,b=b,b-2*a` and `p*=2` move to n + 1. `a=p=2`
  shares the seed 2 of s₀ and 2¹. Exact integers, so it is right for
  every n.

**Notes**

- The entry's order-4 recurrence a(n) = 4a(n−1) − 7a(n−2) + 8a(n−3) −
  4a(n−4) needs four seeds and is longer; tracking sₙ − 1 instead of sₙ
  (`print(p-b)`, `b-2*a-2`) ties at 46.
- The terms pass the 4300-digit int-to-str limit of Python 3.11+ at
  n = 14285, where the program stops with a `ValueError`.
- The b-file has 1000 terms (n = 1 to 1000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002248), CC BY-SA 4.0.
