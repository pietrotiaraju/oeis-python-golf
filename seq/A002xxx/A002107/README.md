# A002107

> Expansion of Product_{k>=1} (1 - x^k)^2.
> — [OEIS A002107](https://oeis.org/A002107)

Offset 0: 1, -2, -1, 2, 1, 2, -2, 0, -2, -2, 1, 0, …

### Python 3 — 82 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=-2*sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- **The recurrence.** For F = Π_{k≥1} (1 − x^k)², the logarithmic
  derivative gives x·F′/F = −2·Σ_k k·x^k/(1 − x^k), and comparing
  coefficients of x^m:

  m·a(m) = −2·Σ_{k≥1} k·(a(m−k) + a(m−2k) + a(m−3k) + …),

  so the floor division by m is exact.
- **Negative steps** (as in [A000041](../../A000xxx/A000041/) and the
  theta pages from [A001934](../../A001xxx/A001934/) on): the list `a`
  holds a(0), …, a(m−1) and n = −m. For d = −k the slice `a[d::d]` is
  a(m−k), a(m−2k), …, so `d*sum(a[d::d])` is −k times that sum; the sign
  cancels against `//n`.
- `while[print(a[-1])]:` prints the newest term before each step; a
  one-element list is always true.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The slices cost about m·ln m additions for a(m). The b-file has 10001
  terms (n = 0…10000); the bar is all of them in 60 s, about 25 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002107), CC BY-SA 4.0.
