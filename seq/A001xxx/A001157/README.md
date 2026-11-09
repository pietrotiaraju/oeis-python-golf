# A001157

> a(n) = sigma_2(n): sum of squares of divisors of n.
> — [OEIS A001157](https://oeis.org/A001157)

Offset 1: 1, 5, 10, 21, 26, 50, 50, 85, 91, 130, 122, 210, …

### Python 3 — 58 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(d*d*(n%d<1)for d in r))
```

**How it works**

- The divisor-sum program of [A000203](../../A000xxx/A000203/) with each
  divisor raised to the power 2: `d*d*(n%d<1)` is d^2 when d divides n and 0
  otherwise.
- `r` is both the loop and the list of candidate divisors: while n is
  handled, `r+=n+1,` appends the next n, so `r` is [1, …, n+1]. The extra
  n+1 never divides n (n ≥ 1), and the `for` loop picks up the appended
  values, so the program runs forever.

**Notes**

- Exact for every n: integer arithmetic only.
- Trial division over all d ≤ n+1, so the time grows like n². The bar is the
  whole b-file, 10000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001157), CC BY-SA 4.0.
