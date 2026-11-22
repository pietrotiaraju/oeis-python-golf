# A002171

> Glaisher's chi numbers. a(n) = chi(4*n + 1).
> — [OEIS A002171](https://oeis.org/A002171)

Offset 0: 1, -2, -3, 6, 2, 0, -1, -10, 0, -2, 10, 6, …

### Python 3 — 88 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=2*sum(d*(d|-2)*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- **Generating function.** The entry gives Σ a(n)xⁿ =
  Π_(k≥1) (1 − x^k)²(1 − x^(2k))², the expansion of
  q^(−1/4)·η(q)²η(q²)² (Glaisher's χ(4n + 1) is the coefficient of
  q^(4n+1) in η(4τ)²η(8τ)², the weight-2 newform of level 32). As an
  Euler transform this is Π_k (1 − x^k)^(−c(k)) with c(k) = −2 for odd k
  and c(k) = −4 for even k (the entry's "period 2 sequence [−2, −4]").
- **Recurrence.** Taking the logarithmic derivative of an Euler
  transform gives n·a(n) = Σ_(k=1..n) b(k)·a(n − k) with
  b(k) = Σ_(d|k) d·c(d); grouped by d this is
  n·a(n) = Σ_(d=1..n) d·c(d)·Σ_(j≥1) a(n − jd).
- **Negative indices.** The list `a` holds a(0), …, a(N − 1) and
  `n` = −N. For d = −N, …, −1 the slice `a[d::d]` is
  a(N − |d|), a(N − 2|d|), …, so `sum(a[d::d])` is the inner sum.
- **The weight.** `d|-2` keeps only the lowest bit of d: it is −1 for
  odd d and −2 for even d, so `d*(d|-2)` = |d| or 2|d| = −|d|·c(|d|)/2.
  The outer sum is therefore −N·a(N)/2, and `2*…//n` (n = −N) is a(N).
  The quotient is an integer, so the floor division is exact.
- `while[print(a[-1])]:` prints the newest term (a(0) = 1 first) and
  never ends, since a one-element list is true.

**Notes**

- Exact integer arithmetic, right for every n.
- Term N costs about N·ln N additions (the slices), so the time grows
  like N² log N: the whole b-file (10001 terms) takes 17 reference
  seconds (25 s here), and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002171), CC BY-SA 4.0.
