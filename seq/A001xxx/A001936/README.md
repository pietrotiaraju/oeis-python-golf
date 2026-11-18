# A001936

> Expansion of q^(-1/4) * (eta(q^4) / eta(q))^2 in powers of q.
> — [OEIS A001936](https://oeis.org/A001936)

Offset 0: 1, 2, 5, 10, 18, 32, 55, 90, 144, 226, 346, 522, 777, 1138, 1648, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=2*sum(d*sum(a[d::d])for d in range(n,0)if d%4)//n,
```

**How it works**

- **The product.** With η(q) = q^(1/24)·Π(1 − q^k), the entry's
  q^(−1/4)·(η(q⁴)/η(q))² is the series Π_{k≥1} ((1 − x^{4k})/(1 − x^k))²,
  the square of [A001935](../A001935/) (partitions with no part
  divisible by 4). As Π (1 − x^k)^(−c(k)) it has c(k) = 2 when 4 ∤ k and
  0 when 4 | k: the Euler transform of the period-4 sequence 2, 2, 2, 0.
- **The recurrence.** Taking the logarithmic derivative and comparing
  coefficients of x^m gives

  m·a(m) = 2·Σ_{4∤j} j·(a(m−j) + a(m−2j) + a(m−3j) + …).

  The right side is m·a(m) exactly, so the floor division is exact.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −j the slice `a[d::d]` is
  a(m−j), a(m−2j), …; `if d%4` drops the j divisible by 4, and the sign of
  d cancels against `//n`.

**Notes**

- The template of [A001935](../A001935/) with the factor 2; the other
  powers are [A001937](../A001937/),
  [A001939](../A001939/), [A001940](../A001940/) and [A001941](../A001941/).
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m); the bar is the whole b-file
  (1001 terms) in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001936), CC BY-SA 4.0.
