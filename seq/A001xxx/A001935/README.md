# A001935

> Number of partitions with no even part repeated; partitions of n in which no parts are multiples of 4.
> — [OEIS A001935](https://oeis.org/A001935)

Offset 0: 1, 1, 2, 3, 4, 6, 9, 12, 16, 22, 29, 38, 50, 64, 82, 105, 132, 166, …

### Python 3 — 85 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0)if d%4)//n,
```

**How it works**

- **The product.** A partition with no part divisible by 4 has generating
  function Π_{4∤k} 1/(1 − x^k) = Π_{k≥1} (1 − x^{4k})/(1 − x^k), which is
  also the g.f. of partitions with no even part repeated (the entry's
  P(x⁴)/P(x)). So the exponent of 1/(1 − x^k) is c(k) = 1 when 4 ∤ k and
  0 when 4 | k: the Euler transform of the period-4 sequence 1, 1, 1, 0.
- **The recurrence.** Taking the logarithmic derivative of
  Π (1 − x^k)^(−c(k)) and comparing coefficients of x^m gives

  m·a(m) = Σ_{k≥1} k·c(k)·(a(m−k) + a(m−2k) + a(m−3k) + …).

  The right side is m·a(m) exactly, so the floor division is exact.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −k the slice `a[d::d]` is
  a(m−k), a(m−2k), …; `d%4` is 0 exactly when 4 | k, so `if d%4` keeps the
  terms with c(k) = 1. The sign of d cancels against `//n`.

**Notes**

- The same template with a factor in front gives the powers of this
  series: [A001936](../A001936/) (square), [A001937](../A001937/) (cube),
  [A001939](../A001939/) (5th), [A001940](../A001940/) (6th) and
  [A001941](../A001941/) (7th); the 4th power with alternating signs is
  [A001938](../A001938/).
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m); the bar is 8500 of the
  10001 b-file terms in 60 s (about 24 s here); the whole b-file takes
  about 35 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001935), CC BY-SA 4.0.
