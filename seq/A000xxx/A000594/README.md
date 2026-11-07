# A000594

> Ramanujan's tau function (or Ramanujan numbers, or tau numbers).
> — [OEIS A000594](https://oeis.org/A000594)

Offset 1: 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643, -115920, …

τ(n) is the coefficient of xⁿ in x·Π_{k≥1} (1 − x^k)²⁴.

### Python 3 — 83 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=24*sum(d*sum(a[d::d])for d in range(n,0))//-n,
```

**How it works**

- **The recurrence.** Let A(x) = Π_{k≥1} (1 − x^k)²⁴ = Σ_m a(m)·x^m, so
  τ(m+1) = a(m). The logarithmic derivative is
  x·A′(x)/A(x) = −24 Σ_{k≥1} k·x^k/(1 − x^k) = −24 Σ_{t≥1} σ(t)·x^t, and
  comparing coefficients of x^m gives

  m·a(m) = −24 Σ_{k=1}^{m} k·(a(m−k) + a(m−2k) + a(m−3k) + …),

  which is −24 Σ_t σ(t)·a(m−t) grouped by the divisor k of t. The right side
  is m·a(m) exactly, so the floor division by m is exact.
- **Negative steps.** The list `a` holds a(0), …, a(m−1) and n = −m. For
  d = −k the slice `a[d::d]` is a(m−k), a(m−2k), …, so `d*sum(a[d::d])` is
  −k times the inner sum; the minus signs of d and of −24 cancel against
  `//-n`, which divides by m.
- `*a,n=1,0` sets a = [a(0)] = [1] and n = 0. `print(a[-1])` in the loop
  condition prints τ(1) = 1 first and then each new coefficient.

**Notes**

- Other versions that print the same terms: counting n up with `n+=1`,
  `range(-n,0)` and `//n`: also 83 bytes; `a=[1]` with `len(a)` in place of
  n: 85 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m): about 7800 terms in 60 s
  here. The b-file has 16091 terms; the bar is 5000 terms in 60 s.
- |τ(n)| ≤ d(n)·n^(11/2) (Deligne), so the 4300-digit int-to-str limit is
  out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 150 | first entry |
| 2026-11-06 | Python 3 | 83 | use the logarithmic derivative of the discriminant product |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000594), CC BY-SA 4.0.
