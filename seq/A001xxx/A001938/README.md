# A001938

> Expansion of k/(4*q^(1/2)) in powers of q, where k defined by sqrt(k) = theta_2(0, q)/theta_3(0, q).
> — [OEIS A001938](https://oeis.org/A001938)

Offset 0: 1, -4, 14, -40, 101, -236, 518, -1080, 2162, -4180, 7840, -14328, …

### Python 3 — 92 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=4*sum(d*(d%-2|d%4)*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- **The product.** The entry's formula section gives the g.f. as
  q^(−1/2)·(η(q)·η(q⁴)²/η(q²)³)⁴ with η(q) = q^(1/24)·Π(1 − q^k), that is
  Π_{k≥1} (1 − q^k)⁴·(1 − q^{4k})⁸/(1 − q^{2k})^12. Written as
  Π (1 − q^k)^(−c(k)), the exponent collects −4 from every k, +12 from
  even k and −8 from multiples of 4: c(k) = −4, 8, −4, 0 for
  k ≡ 1, 2, 3, 0 (mod 4), the entry's "Euler transform of period 4
  sequence [−4, 8, −4, 0]".
- **The recurrence.** Taking the logarithmic derivative and comparing
  coefficients of q^m gives

  m·a(m) = Σ_{k≥1} k·c(k)·(a(m−k) + a(m−2k) + a(m−3k) + …).

  The right side is m·a(m) exactly, so the floor division is exact.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −k the slice `a[d::d]` is
  a(m−k), a(m−2k), …, and the sign of d cancels against `//n`.
- **The period-4 weight.** `d%-2|d%4` is c(k)/4: for odd d, `d%-2` is −1
  and −1 OR anything is −1; for even d it is 0, and `d%4` is 2 when
  k ≡ 2 (mod 4) and 0 when 4 | k.

**Notes**

- The same series is (−1)^n times the 4th power of
  [A001935](../A001935/) (the Euler transform of 4, 4, 4, 0): that
  program with `4*` and the sign `(n%-2|1)` (−1 for odd n) is 2 bytes
  longer; a plain `(-1)**n` would print floats, since n is negative here.
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m). The bar is 7000 of the
  10001 b-file terms in 60 s (about 26 s here); 8000 terms take about 34 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001938), CC BY-SA 4.0.
