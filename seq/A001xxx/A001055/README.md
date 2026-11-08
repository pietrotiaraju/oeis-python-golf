# A001055

> The multiplicative partition function: number of ways of factoring n with all factors greater than 1 (a(1) = 1 by convention).
> — [OEIS A001055](https://oeis.org/A001055)

Offset 1: 1, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 4, 1, 2, 2, 5, 1, 4, 1, 4, …

### Python 3 — 92 bytes

```python
f=lambda n,m=2:1+sum(f(n//d,d)for d in range(m,n)if n%d<1>d*d-n)
n=1
while[print(f(n))]:n+=1
```

**How it works**

- Write a factorization with its factors in nondecreasing order.
  f(n, m) counts those of n whose factors are all ≥ m: either n alone
  (the `1+`), or a smallest factor d with m ≤ d, d | n and d² ≤ n (the
  rest is at least d), followed by a factorization of n/d with factors
  ≥ d.
- `n%d<1>d*d-n` is the chain n%d < 1 and 1 > d·d − n: d | n and d² ≤ n.
- f(1) = 1 + 0 = 1, the empty factorization (a(1) = 1).

**Notes**

- Exact integer arithmetic.
- The whole b-file (10 000 terms) prints in about 15 s; the bar is the
  whole b-file.
- Letting d run up to n with `n<2or sum(…range(m,n+1)…)` is as long, but
  prints True for n = 1.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 92 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001055), CC BY-SA 4.0.
