# A001937

> Expansion of (psi(x^2) / psi(-x))^3 in powers of x where psi() is a Ramanujan theta function.
> — [OEIS A001937](https://oeis.org/A001937)

Offset 0: 1, 3, 9, 22, 48, 99, 194, 363, 657, 1155, 1977, 3312, 5443, 8787, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=3*sum(d*sum(a[d::d])for d in range(n,0)if d%4)//n,
```

**How it works**

- **The product.** With η(q) = q^(1/24)·Π(1 − q^k), the entry's
  (ψ(x²)/ψ(−x))³ = q^(−3/8)·(η(q⁴)/η(q))³ is the series Π_{k≥1} ((1 − x^{4k})/(1 − x^k))³,
  the cube of [A001935](../A001935/) (partitions with no part
  divisible by 4). As Π (1 − x^k)^(−c(k)) it has c(k) = 3 when 4 ∤ k and
  0 when 4 | k: the Euler transform of the period-4 sequence 3, 3, 3, 0.
- **The recurrence.** Taking the logarithmic derivative and comparing
  coefficients of x^m gives

  m·a(m) = 3·Σ_{4∤j} j·(a(m−j) + a(m−2j) + a(m−3j) + …).

  The right side is m·a(m) exactly, so the floor division is exact.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −j the slice `a[d::d]` is
  a(m−j), a(m−2j), …; `if d%4` drops the j divisible by 4, and the sign of
  d cancels against `//n`.

**Notes**

- The template of [A001935](../A001935/) with the factor 3; the other
  powers are [A001936](../A001936/),
  [A001939](../A001939/), [A001940](../A001940/) and [A001941](../A001941/).
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m); the bar is 8000 of the
  10001 b-file terms in 60 s (about 24 s here); the whole b-file takes
  about 40 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001937), CC BY-SA 4.0.
