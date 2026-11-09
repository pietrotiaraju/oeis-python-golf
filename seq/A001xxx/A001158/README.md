# A001158

> sigma_3(n): sum of cubes of divisors of n.
> — [OEIS A001158](https://oeis.org/A001158)

Offset 1: 1, 9, 28, 73, 126, 252, 344, 585, 757, 1134, 1332, 2044, …

### Python 3 — 59 bytes

```python
r=[1]
for n in r:r+=n+1,;print(sum(d**3*(n%d<1)for d in r))
```

**How it works**

- The divisor-sum program of [A000203](../../A000xxx/A000203/) with each
  divisor raised to the power 3: `d**3*(n%d<1)` is d^3 when d divides n and 0
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
| 2026-11-09 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001158), CC BY-SA 4.0.
