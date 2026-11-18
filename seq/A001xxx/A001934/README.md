# A001934

> Expansion of 1/theta_4(q)^2 in powers of q.
> — [OEIS A001934](https://oeis.org/A001934)

Offset 0: 1, 4, 12, 32, 76, 168, 352, 704, 1356, 2532, 4600, 8160, 14176, …

### Python 3 — 86 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=2*sum(d*sum(a[d::d])<<d%2for d in range(n,0))//n,
```

**How it works**

- **The product.** By Jacobi's triple product, θ₄(q) = Σ (−1)^n q^(n²) =
  Π_{k≥1} (1 − q^{2k})(1 − q^{2k−1})² = Π_{k≥1} (1 − q^k)/(1 + q^k)
  = η(q)²/η(q²) up to the factors q^(1/24). So 1/θ₄(q)² = Π (1 − q^{2k})²/(1 − q^k)⁴
  = Π (1 − q^k)^(−c(k)) with c(k) = 4 for odd k and 2 for even k, the
  entry's first formula.
- **The recurrence.** Taking the logarithmic derivative and comparing
  coefficients of q^m gives

  m·a(m) = Σ_{k≥1} k·c(k)·(a(m−k) + a(m−2k) + a(m−3k) + …).

  The right side is m·a(m) exactly, so the floor division is exact.
- **Negative steps.** As in [A000041](../../A000xxx/A000041/), the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −k the slice `a[d::d]` is
  a(m−k), a(m−2k), …. The weight k·c(k) is 2k for even k and 4k for odd
  k: the factor `2*` gives the 2, and `<<d%2` doubles once more exactly
  when k is odd (`d%2` is 1 for odd d, negative or not). A shift binds
  looser than `*`, so it acts on the whole product `d*sum(…)`; the sign of
  d cancels against `//n`.

**Notes**

- Writing the weight as `d*(d%2+1)` costs 3 bytes more.
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m), on numbers twice as
  long as those of [A001935](../A001935/). The bar is 7000 of the 10001
  b-file terms in 60 s (about 26 s here); 8000 terms take about 34 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001934), CC BY-SA 4.0.
