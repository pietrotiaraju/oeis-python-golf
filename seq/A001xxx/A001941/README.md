# A001941

> Absolute values of coefficients of an elliptic function.
> — [OEIS A001941](https://oeis.org/A001941)

Offset 0: 1, 7, 35, 140, 483, 1498, 4277, 11425, 28889, 69734, 161735, …

### Python 3 — 87 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=7*sum(d*sum(a[d::d])for d in range(n,0)if d%4)//n,
```

**How it works**

- **The product.** The entry does not say which elliptic function it
  means, but its formula section gives the g.f. Π (1 − x^k)^(−c(k)) with
  c(k) = 7, 7, 7, 0, 7, 7, 7, 0, …, that is
  Π_{k≥1} ((1 − x^{4k})/(1 − x^k))^7 = Π_{k≥1} ((1 + x^{2k})/(1 − x^{2k−1}))^7,
  the seventh power of [A001935](../A001935/). The program follows this
  formula, and it matches all 1001 terms of the b-file. With x → −x the
  series becomes (ψ(x²)/ψ(x))^7, a quotient of Ramanujan theta functions
  whose coefficients are (−1)^n·a(n): hence the absolute values.
- **The recurrence.** Taking the logarithmic derivative and comparing
  coefficients of x^m gives

  m·a(m) = 7·Σ_{4∤j} j·(a(m−j) + a(m−2j) + a(m−3j) + …).

  The right side is m·a(m) exactly, so the floor division is exact.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −j the slice `a[d::d]` is
  a(m−j), a(m−2j), …; `if d%4` drops the j divisible by 4, and the sign of
  d cancels against `//n`.

**Notes**

- The template of [A001935](../A001935/) with the factor 7; the other
  powers are [A001936](../A001936/), [A001937](../A001937/),
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
Sequences](https://oeis.org/A001941), CC BY-SA 4.0.
