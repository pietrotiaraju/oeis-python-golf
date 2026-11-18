# A001939

> Expansion of (psi(-x) / phi(-x))^5 in powers of x where phi(), psi() are Ramanujan theta functions.
> — [OEIS A001939](https://oeis.org/A001939)

Offset 0: 1, 5, 20, 65, 185, 481, 1165, 2665, 5820, 12220, 24802, 48880, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=5*sum(d*sum(a[d::d])for d in range(n,0)if d%4)//n,
```

**How it works**

- **The product.** With η(q) = q^(1/24)·Π(1 − q^k), the entry's
  (ψ(−x)/φ(−x))⁵ = q^(−5/8)·(η(q⁴)/η(q))⁵ is the series Π_{k≥1} ((1 − x^{4k})/(1 − x^k))⁵,
  the fifth power of [A001935](../A001935/) (partitions with no part
  divisible by 4). As Π (1 − x^k)^(−c(k)) it has c(k) = 5 when 4 ∤ k and
  0 when 4 | k: the Euler transform of the period-4 sequence 5, 5, 5, 0.
- **The recurrence.** Taking the logarithmic derivative and comparing
  coefficients of x^m gives

  m·a(m) = 5·Σ_{4∤j} j·(a(m−j) + a(m−2j) + a(m−3j) + …).

  The right side is m·a(m) exactly, so the floor division is exact.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −j the slice `a[d::d]` is
  a(m−j), a(m−2j), …; `if d%4` drops the j divisible by 4, and the sign of
  d cancels against `//n`.

**Notes**

- The template of [A001935](../A001935/) with the factor 5; the other
  powers are [A001936](../A001936/), [A001937](../A001937/),
  [A001940](../A001940/) and [A001941](../A001941/).
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m); the bar is 7000 of the
  10001 b-file terms in 60 s (about 25 s here); 8000 terms take about 29 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 87 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001939), CC BY-SA 4.0.
