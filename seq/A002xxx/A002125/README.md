# A002125

> a(n) = Sum_{k=0..n} f(k)*f(n-k) where f(k) = A002124(k).
> — [OEIS A002125](https://oeis.org/A002125)

Offset 0: 1, 0, 0, 2, 0, 2, 3, 2, 6, 4, 9, 14, 11, 26, 29, 34, …

### Python 3 — 112 bytes

```python
a=[1];*P,F,n=2,0
while[print(sum(map(int.__mul__,a,a[::-1])))]:n-=1;P+=[n][:F%-n];F*=n*n;a+=sum(a[p]for p in P),
```

**How it works**

- The self-convolution of [A002124](../A002124/) (compositions into odd
  primes), generating function 1/(1 − Σ_{odd p} x^p)².
- The loop is the A002124 record: f(0) = 1 and f(n) = Σ_{odd p ≤ n} f(n − p),
  with `P` holding the negated odd primes and `a[p]` = f(m − p). The print
  pairs the list f(0), …, f(n) with its reverse,
  `sum(map(int.__mul__,a,a[::-1]))`.
- Odd primes come from Wilson's theorem with an extra factor 2:
  F = 2·((m − 1)!)², so F mod m is 2 when m is an odd prime, and 0 for
  m = 1, for m = 2, for m = 4 (F = 72) and for every other composite m.
  `[n][:F%-n]` therefore adds −m to `P` exactly once for an odd prime m
  (a slice `[:2]` of a one-element list) and nothing otherwise; `F*=n*n`
  moves F on to 2·(m!)². The starred assignment sets P = [], F = 2, n = 0.

**Notes**

- The whole b-file, 1001 terms (n = 0 to 1000), takes about 0.2 s here, so
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 112 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002125), CC BY-SA 4.0.
